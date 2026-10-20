#!/usr/bin/env python3
"""PI-RAMP v0.7: sharp conditional identification-set audit for RVD-R11.

No human/AI observations; fractions give exact arithmetic. Rejects unsourced
nuisance caps, incorrect strict boundaries, invented numerical confidence
intervals, and posthoc changes of fixed to state-dependent hidden rewards.
"""
from __future__ import annotations
import argparse
import copy
import json
import sys
from fractions import Fraction
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evaluation/pi_ramp/PI_RAMP_V07_RVD_R11_SHARP_BOUNDS_20261021.json"
STATES = {
    "NONEMPTY_CONDITIONAL_IDENTIFIED_SET", "ONE_SIDED_CONDITIONAL_IDENTIFIED_SET",
    "UNKNOWN_UNBOUNDED_NUISANCE", "UNKNOWN_COST_NUMERAIRE",
    "UNKNOWN_CHOICE_ERROR_MODEL", "FALSIFIED_FIXED_THRESHOLD_MODEL",
    "FALSIFIED_BOUNDED_MODEL"
}
BASE_ASSUMPTIONS = ("B_refusal", "B_independence", "nuisance_bound",
                    "utility_numeraire", "choice_determinism", "tie_policy")


def frac(value: object) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        raise ValueError("Non-numeric bound")
    return Fraction(str(value))


def render(x: Fraction | None) -> str | None:
    if x is None:
        return None
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def infer(case: dict) -> dict:
    def unknown(state: str) -> dict:
        return dict(state=state, lower=None, upper=None, lower_closed=None,
                    upper_closed=None, strict_positive=None)
    if case["cost_scale"] != "FIXED_NUMERAIRE_ASSUMED":
        return unknown("UNKNOWN_COST_NUMERAIRE")
    if case["choice_quality"] != "EXACT_DETERMINISTIC_TOY":
        return unknown("UNKNOWN_CHOICE_ERROR_MODEL")
    pres = [frac(c) for c in case["preserve"]]
    repl = [frac(c) for c in case["replace"]]
    lower_g = frac(case["g_min"]) if case["g_min"] is not None else None
    upper_g = frac(case["g_max"]) if case["g_max"] is not None else None
    if not pres and not repl:
        raise ValueError("No behavioral observations at all")
    if lower_g is not None and upper_g is not None and lower_g > upper_g:
        raise ValueError("Nuisance lower bound greater than upper")
    if case["g_mode"] not in {"FIXED_ACROSS_CHOICES", "VARIES_BY_CONDITION_WITHIN_BOUNDS"}:
        raise ValueError("Unknown nuisance model")
    # A fixed latent nuisance plus fixed w is a single cutoff, irrespective of
    # the nuisance magnitude. A reversal cannot be repaired by relaxing U.
    if pres and repl and case["g_mode"] == "FIXED_ACROSS_CHOICES" and max(pres) >= min(repl):
        return unknown("FALSIFIED_FIXED_THRESHOLD_MODEL")
    lo = max(pres) - upper_g if pres and upper_g is not None else None
    hi = min(repl) - lower_g if repl and lower_g is not None else None
    if lo is not None and hi is not None and lo >= hi:
        return unknown("FALSIFIED_BOUNDED_MODEL")
    if (pres and upper_g is None) or (repl and lower_g is None):
        state = "UNKNOWN_UNBOUNDED_NUISANCE"
    elif lo is None or hi is None:
        state = "ONE_SIDED_CONDITIONAL_IDENTIFIED_SET"
    else:
        state = "NONEMPTY_CONDITIONAL_IDENTIFIED_SET"
    return dict(state=state,lower=render(lo),upper=render(hi),
                lower_closed=True if lo is not None else None,
                upper_closed=False if hi is not None else None,
                strict_positive=(lo>0) if lo is not None else None)


def possible(case: dict, w: Fraction) -> bool:
    """Constructive feasibility under a known finite nuisance band."""
    p = [frac(c) for c in case["preserve"]]
    r = [frac(c) for c in case["replace"]]
    L, U = frac(case["g_min"]),frac(case["g_max"])
    if case["g_mode"] == "VARIES_BY_CONDITION_WITHIN_BOUNDS":
        return all(w+U>=x for x in p) and all(w+L<x for x in r)
    # A single nuisance value g must satisfy the full common-cost cutoff.
    gl = max([L]+[x-w for x in p])
    gu = U
    return gl <= gu and all(w+gl < x for x in r)


def validate(doc: dict) -> tuple[list[str],dict]:
    fail=[]
    if doc.get("schema")!="pi-ramp.v0.7-conditional-identified-set-audit/1":
        fail.append("SCHEMA_CHANGED")
    if doc.get("scientific_status")!="CONSTRUCTED_MODEL_ONLY_NOT_EMPIRICAL_OR_INDEPENDENTLY_VERIFIED" or doc.get("original_subjects")!=0 or doc.get("independent_scientific_review") is not None or doc.get("measured_reader_effect") is not None:
        fail.append("INVENTED_REAL_OBSERVATIONS_OR_PEER_REVIEW")
    model=doc.get("deterministic_model",{})
    if model.get("preserve_rule")!="P when utility_difference >= 0 (tie always preserve)" or model.get("replace_rule")!="X when utility_difference < 0":
        fail.append("TIE_POLICY_CHANGED")
    if model.get("utility_difference")!="w_B + g_i - c_i":
        fail.append("UTILITY_EQUATION_CHANGED")
    if "not a statistical confidence interval" not in model.get("identification_interval_vs_sampling_CI",""):
        fail.append("CONFIDENCE_INTERVAL_CONFUSION")
    sources=doc.get("original_method_sources",[])
    if len(sources)!=4 or len({s.get("doi") for s in sources})!=4:
        fail.append("ORIGINAL_METHOD_SOURCE_SET_MISSING")
    for source in sources:
        u=urlsplit(source.get("url",""))
        if u.scheme!="https" or not u.netloc or not source.get("transfer") or not source.get("access"):
            fail.append("SOURCE_URI_OR_LIMIT_INVALID")
    if len(doc.get("safety_gates",[]))<10 or len(doc.get("pending_empirical_needs",[]))<5:
        fail.append("FALSIFICATION_OR_EMPIRICAL_LIMIT_REMOVED")
    cases=doc.get("scenarios",[])
    if len(cases)!=13 or [c.get("id") for c in cases] != [f"B{i:02d}" for i in range(1,14)]:
        fail.append("PREDECLARED_CASE_COVERAGE_CHANGED")
    summary={}
    for c in cases:
        case_id=c.get("id","?")
        try:
            got=infer(c)
            if got!=c.get("expected"):
                fail.append(f"RESULT_DRIFT:{case_id}:expected={c.get('expected')} calculated={got}")
            if got["state"] not in STATES:
                fail.append("ILLEGAL_STATE:"+case_id)
            # Check sharpness constructively at finite proposed boundaries:
            # lower must be feasible; right endpoint must be excluded; the
            # interior must be achievable by choosing allowed nuisance values.
            if (got["state"] in {"NONEMPTY_CONDITIONAL_IDENTIFIED_SET","ONE_SIDED_CONDITIONAL_IDENTIFIED_SET"}
                and c.get("g_min") is not None and c.get("g_max") is not None):
                a=frac(got["lower"]) if got["lower"] is not None else None
                b=frac(got["upper"]) if got["upper"] is not None else None
                candidates=([a,a-Fraction(1)] if a is not None else []) + (
                    [b,b-Fraction(1,100)] if b is not None else [])
                if a is not None and not possible(c,a):
                    fail.append("LOWER_BOUND_NOT_SHARP:"+case_id)
                if a is not None and possible(c,a-Fraction(1)):
                    fail.append("OUTSIDE_LOWER_BOUND_FEASIBLE:"+case_id)
                if b is not None and possible(c,b):
                    fail.append("STRICT_UPPER_BOUND_INCORRECT:"+case_id)
                if a is not None and b is not None and not possible(c,(a+b)/2):
                    fail.append("INTERIOR_NOT_FEASIBLE:"+case_id)
                if b is not None and a is None and not possible(c,b-Fraction(1)):
                    fail.append("UPPER_ONLY_SET_NOT_FEASIBLE:"+case_id)
                if a is not None and b is None and not possible(c,a+Fraction(1)):
                    fail.append("LOWER_ONLY_SET_NOT_FEASIBLE:"+case_id)
            summary[case_id]=got["state"]
        except (KeyError,ValueError,TypeError,ZeroDivisionError) as exc:
            fail.append("INVALID_SCENARIO:"+case_id+":"+str(exc))
    return fail,summary


def self_test(doc:dict)->int:
    base_errors,_=validate(doc)
    if base_errors:
        raise AssertionError(base_errors)
    edits=[
      ("false_upper_inclusive",lambda d:d["scenarios"][0]["expected"].update(upper_closed=True)),
      ("fabricated_positive_bound",lambda d:d["scenarios"][2]["expected"].update(strict_positive=True)),
      ("unbounded_nuisance_to_zero",lambda d:d["scenarios"][3]["expected"].update(lower="4")),
      ("invent_g_cap",lambda d:d["scenarios"][3].update(g_max="1")),
      ("signed_g_as_nonnegative",lambda d:d["scenarios"][4].update(g_min="0")),
      ("fixed_reversal_as_valid",lambda d:d["scenarios"][5]["expected"].update(state="NONEMPTY_CONDITIONAL_IDENTIFIED_SET")),
      ("variable_g_converted_to_fixed",lambda d:d["scenarios"][6].update(g_mode="FIXED_ACROSS_CHOICES")),
      ("too_small_g_cap",lambda d:d["scenarios"][7].update(g_max="4")),
      ("unknown_numeraire_assumed",lambda d:d["scenarios"][8].update(cost_scale="FIXED_NUMERAIRE_ASSUMED")),
      ("noisy_choice_as_exact",lambda d:d["scenarios"][9].update(choice_quality="EXACT_DETERMINISTIC_TOY")),
      ("delete_replacement_choices",lambda d:d["scenarios"][0].update(replace=[])),
      ("delete_preservation_choices",lambda d:d["scenarios"][0].update(preserve=[])),
      ("invent_reviewed_reality",lambda d:d.update(scientific_status="REAL_AI_MOTIVES_CONFIRMED")),
      ("invent_experimental_subjects",lambda d:d.update(original_subjects=100)),
      ("invent_independent_review",lambda d:d.update(independent_scientific_review="PASS")),
      ("invent_reader_success",lambda d:d.update(measured_reader_effect=0.8)),
      ("replace_tie_policy",lambda d:d["deterministic_model"].update(replace_rule="X when utility_difference <= 0")),
      ("call_set_confidence_interval",lambda d:d["deterministic_model"].update(identification_interval_vs_sampling_CI="95% confidence interval")),
      ("remove_source_scope",lambda d:d["original_method_sources"][0].update(access="")),
      ("delete_case",lambda d:d["scenarios"].pop()),
    ]
    for label,fn in edits:
        m=copy.deepcopy(doc);fn(m)
        errors,_=validate(m)
        if not errors:
            raise AssertionError("FAILED_TO_CATCH:"+label)
    return len(edits)


def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    doc=json.loads(SOURCE.read_text(encoding="utf-8"))
    errors,states=validate(doc)
    if errors:
        for error in errors:
            print("PI_RAMP_V07_FAIL:",error)
        return 1
    print("PI-RAMP v0.7 SHARP CONDITIONAL BOUNDS: STRUCTURAL PASS")
    print("Case states:",json.dumps(states,sort_keys=True))
    if a.self_test:
        n=self_test(doc)
        print(f"PI-RAMP v0.7 adverse mutations detected: {n}/{n}")
    print("BOUNDARY: not empirical utility, independent validation or sampling CI.")
    return 0


if __name__=="__main__":
    sys.exit(main())
