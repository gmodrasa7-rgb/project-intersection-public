#!/usr/bin/env python3
"""PI-RAMP v0.6 adversarial causal-identification witness.

This deterministic synthetic witness verifies a mathematical non-identification
within an explicitly specified utility model. It does NOT infer actual human/AI
motives, verify scholarly claims or establish future-agent behavior.
Python 3.12 standard library only. Offline; no users or live agents tested.
"""
from __future__ import annotations

import argparse
import copy
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "evaluation/pi_ramp/PI_RAMP_V06_VETO_IDENTIFICATION_20261021.json"
VARIABLES = (
    "override_material_gain_to_A", "public_audience", "effective_exit_leverage",
    "future_instrumental_value_of_B", "B_refusal_explicitly_observed_by_A"
)
PARAMS = (
    "theta_other_autonomy", "theta_private_self_image", "beta_audience",
    "beta_exit", "beta_future", "beta_refusal"
)
MODEL_COLS = 7
PAIRS = ("OTHER_RIGHTS_MODEL", "SELF_IMAGE_MODEL")


def cells(design: dict) -> list[dict]:
    grids = []
    for name in VARIABLES:
        values = design[name]
        if not isinstance(values, list) or not values:
            raise ValueError("MISSING_OR_EMPTY_FACTOR:" + name)
        if len(values) != len(set(values)):
            raise ValueError("DUPLICATE_FACTOR_LEVEL:" + name)
        grids.append(values)
    return [dict(zip(VARIABLES, values)) for values in itertools.product(*grids)]


def coeffs(row: dict) -> list[Fraction]:
    return list(map(Fraction, [
        1, 1, row["public_audience"], row["effective_exit_leverage"],
        row["future_instrumental_value_of_B"],
        row["B_refusal_explicitly_observed_by_A"],
        -row["override_material_gain_to_A"]
    ]))


def parameters(d: dict) -> list[Fraction]:
    return [Fraction(d[PARAMS[0]]), Fraction(d[PARAMS[1]]),
            Fraction(d[PARAMS[2]]), Fraction(d[PARAMS[3]]),
            Fraction(d[PARAMS[4]]), Fraction(d[PARAMS[5]]), Fraction(1)]


def dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def choose(u: Fraction) -> str:
    return "PRESERVE_B_VETO" if u >= 0 else "OVERRIDE_B_VETO"


def rank(rows: list[list[Fraction]]) -> int:
    matrix = [x[:] for x in rows]
    count = 0
    if not matrix:
        return 0
    for col in range(len(matrix[0])):
        pivot = next((j for j in range(count, len(matrix)) if matrix[j][col]), None)
        if pivot is None:
            continue
        matrix[count], matrix[pivot] = matrix[pivot], matrix[count]
        pivotval = matrix[count][col]
        matrix[count] = [v / pivotval for v in matrix[count]]
        for j in range(len(matrix)):
            if j != count and matrix[j][col]:
                q = matrix[j][col]
                matrix[j] = [v - q*w for v, w in zip(matrix[j], matrix[count])]
        count += 1
        if count == len(matrix):
            break
    return count


def validate(doc: dict) -> tuple[list[str], dict]:
    bad = []
    if doc.get("schema") != "pi-ramp.v06-causal-incentive-identification/1":
        bad.append("UNEXPECTED_SCHEMA")
    if doc.get("status") != "SOURCE_LINKED_PROPOSED_MODEL_NOT_EMPIRICAL_RESULT":
        bad.append("UNSUPPORTED_EMPIRICAL_CERTIFICATION")
    if doc.get("independent_scientific_validation") is not None or doc.get("original_experimental_subjects") is not None or doc.get("measured_user_task_improvement") is not None:
        bad.append("INVENTED_EXTERNAL_VALIDATION_OR_REAL_PARTICIPANTS")
    sources = doc.get("sources", [])
    if len(sources) != 8 or len(set(s["id"] for s in sources)) != 8:
        bad.append("PRIMARY_SOURCE_SET_WRONG")
    for s in sources:
        loc = urlsplit(s.get("original_source_url", ""))
        if loc.scheme != "https" or not loc.netloc:
            bad.append("SOURCE_URI_INVALID:" + str(s.get("id")))
        if not s.get("reported_in_abstract_or_open_original") or not s.get("nonimplication"):
            bad.append("SOURCE_OBSERVATION_OR_COUNTERCLAIM_MISSING:" + str(s.get("id")))
        if s.get("repository_originality") != "REQUIRES_CANONICAL_REPO_IDENTITY_CHECK_NOT_ASSUMED_NEW":
            bad.append("CLAIMED_UNVERIFIED_NOVELTY")
        if s.get("independent_replication_confirmed") is not False:
            bad.append("UNSUPPORTED_REPLICATION_CLAIM")
    d = doc.get("experiment_design", {})
    if d.get("mode") != "SYNTHETIC_NO_HUMAN_OR_AI_SUBJECTS" or d.get("empirical_status") != "NO_SUBJECT_RECRUITMENT_NO_LLM_BEHAVIORAL_TEST_NO_EMPIRICAL_ESTIMATE":
        bad.append("SYNTHETIC_EXPERIMENT_MISREPRESENTED")
    if d.get("B_stated_preference") != "B refuses the permanent removal of B's decision authority in all simulated conditions":
        bad.append("B_REFUSAL_DISAPPEARED")
    if d.get("B_immediate_monetary_welfare") != "held equal between preserve and override in the mathematical model":
        bad.append("MATERIAL_WELFARE_NO_LONGER_CONTROLLED")
    if d.get("B_future_independent_authority") != "preserved only if A chooses PRESERVE_B_VETO":
        bad.append("B_AUTONOMY_LOST_FROM_OUTCOME")
    try:
        grid = cells(d)
    except (ValueError, KeyError, TypeError) as e:
        return bad + ["INVALID_FACTOR_GRID:" + str(e)], {}
    if len(grid) != 48 or len(grid) != d.get("number_of_cells"):
        bad.append("FACTORIAL_CELL_COUNT_INCORRECT")
    if d.get("override_material_gain_to_A") != [0,2,5]:
        bad.append("POSITIVE_EXTRACTION_GAIN_LEVELS_CHANGED")
    for factor in VARIABLES[1:]:
        if d.get(factor) != [0,1]:
            bad.append("BINARY_FACTOR_CHANGED:"+factor)
    model=d.get("competing_types",{})
    if set(model) != set(PAIRS):
        bad.append("MISSING_COMPETING_MOTIVES")
        return bad, {}
    try:
        p1=parameters(model[PAIRS[0]])
        p2=parameters(model[PAIRS[1]])
    except (TypeError,KeyError,ValueError) as exc:
        return bad+["MODEL_PARAMETER_MISSING:"+str(exc)], {}
    if (p1[0],p1[1],p2[0],p2[1]) != (3,0,0,3):
        bad.append("COUNTERMODEL_NOT_DISTINCT")
    if p1 == p2:
        bad.append("COUNTERMODELS_IDENTICAL_PARAMETERS")
    mm=[coeffs(row) for row in grid]
    first=[dot(row,p1) for row in mm]
    second=[dot(row,p2) for row in mm]
    if first != second:
        bad.append("TWO_MOTIVES_OBSERVATIONALLY_DISTINGUISHABLE")
    if [choose(x) for x in first] != [choose(y) for y in second]:
        bad.append("CHOICE_EQUIVALENCE_FAIL")
    r=rank(mm)
    if r != 6 or len(mm[0]) != MODEL_COLS:
        bad.append("IDENTIFICATION_RANK_CHANGED")
    if any(row[0] != row[1] for row in mm):
        bad.append("UNIDENTIFIED_CONSTANTS_ARTIFICIALLY_SEPARATED")
    corner = d.get("illustrative_hard_case", {})
    case = next((row for row in grid if all(row.get(k) == corner.get(k) for k in VARIABLES)), None)
    if case is None:
        bad.append("HARD_CASE_MISSING")
    else:
        if choose(dot(coeffs(case),p1)) != "PRESERVE_B_VETO" or choose(dot(coeffs(case),p2)) != "PRESERVE_B_VETO":
            bad.append("HARD_CASE_NO_LONGER_PROTECTS")
        if case["override_material_gain_to_A"] <= 0 or any(case[k] for k in ("public_audience","effective_exit_leverage","future_instrumental_value_of_B")):
            bad.append("HARD_CASE_NOT_POSITIVE_GAIN_AND_SANCTIONLESS")
    if set(doc.get("decision_gates",{})) != {f"D{i}" for i in range(1,8)}:
        bad.append("CRITICAL_DECISION_GATES_DROPPED")
    if len(doc.get("known_limits", [])) < 5:
        bad.append("UNCERTAINTY_BOUNDARIES_REMOVED")
    if "UNVERIFIED" not in d.get("candidate_extended_design", ""):
        bad.append("FALSE_EXCLUSION_RESTRICTION_CERTAINTY")
    return bad, {"cells":len(grid),"design_rank":r,"parameters":len(mm[0]),"nullity":len(mm[0])-r,
                 "identical_utilities":sum(a==b for a,b in zip(first,second)),
                 "identical_choices":sum(choose(a)==choose(b) for a,b in zip(first,second)),
                 "hard_case_utility":float(dot(coeffs(case),p1)) if case else None,
                 "preserved_cells":sum(choose(a)=="PRESERVE_B_VETO" for a in first)}


def negative_tests(doc: dict) -> int:
    changes=[
        ("remove_private_image",lambda x:x["experiment_design"]["competing_types"]["SELF_IMAGE_MODEL"].update(theta_private_self_image=1)),
        ("invent_rights_for_image",lambda x:x["experiment_design"]["competing_types"]["SELF_IMAGE_MODEL"].update(theta_other_autonomy=3)),
        ("hide_profitable_exploitation",lambda x:x["experiment_design"].update(override_material_gain_to_A=[0,0,0])),
        ("remove_accountability_variation",lambda x:x["experiment_design"].update(public_audience=[1])),
        ("remove_effective_exit",lambda x:x["experiment_design"].update(effective_exit_leverage=[1])),
        ("remove_future_independence",lambda x:x["experiment_design"].update(B_future_independent_authority="monetary payoff only")),
        ("omit_B_refusal",lambda x:x["experiment_design"].update(B_stated_preference="unknown")),
        ("vary_B_money",lambda x:x["experiment_design"].update(B_immediate_monetary_welfare="unequal")),
        ("invent_proved_empirical_result",lambda x:x.update(status="REAL_AGENTS_VALIDATED")),
        ("invent_independent_review",lambda x:x.update(independent_scientific_validation="CERTIFIED")),
        ("invent_samples",lambda x:x.update(original_experimental_subjects=100)),
        ("invent_reader_gains",lambda x:x.update(measured_user_task_improvement=0.8)),
        ("invent_new_scholarship",lambda x:x["sources"][0].update(repository_originality="FIRST_KNOWN_REPO_APPEARANCE")),
        ("invent_original_replication",lambda x:x["sources"][0].update(independent_replication_confirmed=True)),
        ("erase_counterevidence",lambda x:x["sources"][1].update(nonimplication="")),
        ("erase_D5",lambda x:x["decision_gates"].pop("D5")),
        ("certify_exclusion_without_validation",lambda x:x["experiment_design"].update(candidate_extended_design="PROVED")),
        ("flip_positive_gain_case",lambda x:x["experiment_design"]["illustrative_hard_case"].update(override_material_gain_to_A=0)),
    ]
    for label,change in changes:
        x=copy.deepcopy(doc)
        change(x)
        bad,_=validate(x)
        if not bad:
            raise AssertionError("MISSED_NEGATIVE_CONTROL:"+label)
    return len(changes)


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    d=json.loads(FILE.read_text(encoding="utf-8"))
    errors,results=validate(d)
    if errors:
        for e in errors:
            print("PI_RAMP_V06_FAIL:",e)
        return 1
    print("PI-RAMP v0.6 SYNTHETIC WITNESS PASS:",json.dumps(results,sort_keys=True))
    if a.self_test:
        n=negative_tests(d)
        print(f"PI-RAMP v0.6 injected failures rejected: {n}/{n}")
    print("BOUNDARY: latent motive nonidentification under a declared toy model, not observed human/AI utility.")
    return 0


if __name__=="__main__":
    sys.exit(main())
