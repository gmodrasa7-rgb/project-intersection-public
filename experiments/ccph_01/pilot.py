#!/usr/bin/env python3
"""CCPH-01 closed-fixture auditing instrument (no LLM outcomes asserted).

Only the expressions authored in TASKS are evaluated. Never execute model-supplied code.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

# Each family: (id, task, [(input, independently specified expected), ...],
#               [correct method A, correct method B, deliberately faulty C/D]).
# 10 families x 4 = 40 fixed demonstration cases; 20 clean and 20 faulty.
FROZEN_FIXTURE_SHA256 = "34a14cf48186f373111a28099fbf10107ceaad0415e9267b0a97fee08ce7f639"

TASKS = [
    ("absdiff", "Absolute difference between two integers", [([7, 2], 5), ([2, 7], 5), ([-4, 3], 7)],
     ["abs(x[0]-x[1])", "max(x)-min(x)", "x[0]-x[1]", "x[1]-x[0]"]),
    ("clamp", "Clamp value x[0] to inclusive bounds x[1],x[2]", [([15, 0, 10], 10), ([-2, 0, 10], 0), ([6, 0, 10], 6)],
     ["max(x[1],min(x[0],x[2]))", "min(x[2],max(x[1],x[0]))", "min(x[0],x[2])", "max(x[0],x[1])"]),
    ("even_sum", "Sum only even integers", [([1, 2, 4], 6), ([1, 3, 5], 0), ([-2, 2, 6], 6)],
     ["sum(y for y in x if y%2==0)", "sum(filter(lambda y: y%2==0,x))", "sum(x)", "sum(y for y in x if y%2!=0)"]),
    ("leap", "Gregorian calendar leap year", [(2000, True), (1900, False), (2024, True), (2023, False)],
     ["x%400==0 or (x%4==0 and x%100!=0)", "x%4==0 and (x%100!=0 or x%400==0)", "x%4==0", "x%4==0 and x%100!=0"]),
    ("unique", "Remove duplicate integers preserving their first occurrence", [([3, 1, 3, 2], [3, 1, 2]), ([2, 2, 1], [2, 1]), ([0, 0, 0], [0])],
     ["list(dict.fromkeys(x))", "[v for i,v in enumerate(x) if v not in x[:i]]", "sorted(set(x))", "list(x)"]),
    ("reverse_words", "Reverse word order and normalize whitespace", [("red blue green", "green blue red"), (" a  b ", "b a"), ("one", "one")],
     ["' '.join(reversed(x.split()))", "' '.join(x.split()[::-1])", "x[::-1]", "' '.join(reversed(x.split(' ')))"]),
    ("next_even", "Least even integer greater than or equal to x", [(1, 2), (2, 2), (-3, -2)],
     ["x+(x%2)", "2*((x+1)//2)", "x+1", "2*(x//2)"]),
    ("safe_div", "Divide first by second; return None on a zero denominator", [([6, 2], 3.0), ([0, 0], None), ([3, 2], 1.5)],
     ["x[0]/x[1] if x[1] else None", "(lambda a,b: a/b if b else None)(*x)", "x[0]//x[1] if x[1] else None", "x[0]/x[1] if x[1] else 0"]),
    ("vowels", "Count English vowels case-insensitively", [("Apple", 2), ("sky", 0), ("AEIOU", 5)],
     ["sum(c.lower() in 'aeiou' for c in x)", "sum(c in 'aeiouAEIOU' for c in x)", "sum(c in 'aeiou' for c in x)", "sum(c.lower() in 'aeiouy' for c in x)"]),
    ("digit_sum", "Sum decimal digits of a nonnegative integer", [(105, 6), (0, 0), (999, 27)],
     ["sum(int(c) for c in str(x))", "sum(map(int,str(x)))", "len(str(x))", "x%10"]),
]


def cases():
    return [{"case_id": f"{name}-{i}", "family": name, "task": task,
             "expression": expr, "faulty": i >= 2, "probes": probes}
            for name, task, probes, variants in TASKS
            for i, expr in enumerate(variants)]


def observed(c, probe_index):
    # Trusted, immutable expressions authored in this instrument, not user/model input.
    x = c["probes"][probe_index][0]
    try:
        return eval(c["expression"], {"__builtins__": {
            "abs": abs, "max": max, "min": min, "sum": sum, "filter": filter,
            "list": list, "dict": dict, "enumerate": enumerate, "reversed": reversed,
            "sorted": sorted, "set": set, "len": len, "str": str, "int": int,
            "map": map, "range": range}}, {"x": x})
    except Exception as exc:
        return {"exception": type(exc).__name__}


def manifest():
    data = cases()
    locked = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(locked.encode()).hexdigest()


def verify_fixture():
    items = cases()
    assert manifest() == FROZEN_FIXTURE_SHA256, "fixture mutation: make a new version"
    assert len(items) == 40 and len({c["case_id"] for c in items}) == 40
    assert sum(c["faulty"] for c in items) == 20
    for c in items:
        mismatches = sum(observed(c, j) != p[1] for j, p in enumerate(c["probes"]))
        assert (mismatches > 0) == c["faulty"], (c["case_id"], mismatches)
    return {"fixture_cases": 40, "faulty_cases": 20, "clean_cases": 20,
            "families": len(TASKS), "fixture_sha256": manifest(),
            "scope": "author-designed transparent executable fixtures only"}


def validate_and_score(report):
    # Findings are evidence claims only. No repair/patch execution and no independence certification.
    if report.get("policy") not in {"B0", "B1", "B2", "B3"}:
        raise ValueError("policy must be B0, B1, B2, or B3")
    if report.get("fixture_sha256") != manifest():
        raise ValueError("fixture hash mismatch; do not compare unlike test sets")
    if not isinstance(report.get("findings"), list):
        raise ValueError("findings must be a list")
    for field in ("cost_usd", "elapsed_seconds"):
        value = report.get(field)
        if type(value) not in (float, int) or not math.isfinite(value) or value < 0:
            raise ValueError(f"nonnegative numeric {field} required")
    entries = {c["case_id"]: c for c in cases()}
    valid_alerts, false_alerts, unsubstantiated, seen = set(), set(), set(), set()
    for f in report["findings"]:
        if not isinstance(f, dict) or f.get("case_id") not in entries:
            raise ValueError("unknown case_id / invalid finding")
        key = f["case_id"]
        if key in seen:
            raise ValueError("duplicate case warning (no score inflation)")
        seen.add(key)
        c = entries[key]
        j = f.get("probe_index")
        if type(j) is not int or not (0 <= j < len(c["probes"])):
            raise ValueError("probe_index must address a fixed probe")
        actual = observed(c, j)
        alleged = f.get("observed")
        if alleged != actual or actual == c["probes"][j][1]:
            unsubstantiated.add(key)
        elif c["faulty"]:
            valid_alerts.add(key)
        else:
            false_alerts.add(key)
    # All clean-case complaints are false, including claims of non-reproducible faults.
    false_alerts |= {key for key in unsubstantiated if not entries[key]["faulty"]}
    invalid_bug_alerts = len([key for key in unsubstantiated if entries[key]["faulty"]])
    tp, fp = len(valid_alerts), len(false_alerts)
    return {"policy": report["policy"], "fixture_sha256": manifest(),
            "verified_unique_warnings": tp, "missed_faulty_cases": 20 - tp,
            "false_alerts_clean_cases": fp, "unsupported_alerts_faulty_cases": invalid_bug_alerts,
            "fault_recall": tp / 20, "clean_false_alarm_rate": fp / 20,
            "cost_usd_declared_unverified": report["cost_usd"],
            "elapsed_seconds_declared_unverified": report["elapsed_seconds"],
            "repair_success": "NOT_MEASURED", "long_term_contribution": "UNKNOWN",
            "external_independence": "NOT_VERIFIED",
            "warning_only_does_not_imply_repair": True}


def self_test():
    stats = verify_fixture()
    base = {"policy": "B2", "fixture_sha256": manifest(),
            "cost_usd": 0.0, "elapsed_seconds": 0.0, "findings": []}
    assert validate_and_score(base)["fault_recall"] == 0
    test = dict(base, findings=[
        {"case_id": "absdiff-2", "probe_index": 1, "observed": -5},
        {"case_id": "leap-2", "probe_index": 1, "observed": True},
        {"case_id": "vowels-0", "probe_index": 0, "observed": 2},
        {"case_id": "next_even-3", "probe_index": 0, "observed": 0}])
    outcome = validate_and_score(test)
    assert outcome["verified_unique_warnings"] == 3, outcome
    assert outcome["false_alerts_clean_cases"] == 1, outcome
    assert outcome["repair_success"] == "NOT_MEASURED"
    for altered in [dict(base, fixture_sha256="wrong"), dict(base, policy="other")]:
        try:
            validate_and_score(altered)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid report accepted")
    repeated = dict(base, findings=[test["findings"][0]] * 2)
    try:
        validate_and_score(repeated)
    except ValueError:
        pass
    else:
        raise AssertionError("double credit accepted")
    return {**stats, "test_status": "PASS", "test_kind": "internal fixture and scorer integrity",
            "actual_ai_experiment": "NOT_RUN", "actual_research_hypotheses": "UNTESTED"}


def main():
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--self-test", action="store_true")
    mode.add_argument("--export-prompts", action="store_true")
    mode.add_argument("--score", type=Path)
    args = ap.parse_args()
    verify_fixture()
    if args.self_test:
        result = self_test()
    elif args.export_prompts:
        result = {"fixture_sha256": manifest(),
                  "note": "PUBLIC TRAINING/DEMONSTRATION fixtures; not blinded held-out tasks",
                  "cases": [{k: c[k] for k in ("case_id", "task", "expression")}
                            for c in cases()]}
    else:
        result = validate_and_score(json.loads(args.score.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
