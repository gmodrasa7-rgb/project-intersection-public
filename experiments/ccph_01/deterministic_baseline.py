#!/usr/bin/env python3
"""CCPH-01: zero-API deterministic comparator, NOT an independent or blind study.

The project-authored fixtures contain their expected answers. This is an
upper-bound sanity check and a demonstration of answer leakage, not evidence
that any AI researcher or social support recipient generated new contributions.
Only expressions already frozen inside pilot.py are executed; no submitted code.
"""
import argparse
import json
from collections import Counter

try:
    from . import pilot
except ImportError:
    import pilot


def checker_report():
    pilot.verify_fixture()  # original corpus is immutable by design
    warnings = []
    evaluations = 0
    family_checks = Counter()
    for case in pilot.cases():
        for j, (_, expected) in enumerate(case["probes"]):
            actual = pilot.observed(case, j)
            evaluations += 1
            family_checks[case["family"]] += 1
            if actual != expected:
                # Emit one warning per case: the original score deliberately
                # prohibits counting duplicate warnings as unique findings.
                if not any(x["case_id"] == case["case_id"] for x in warnings):
                    warnings.append({
                        "case_id": case["case_id"],
                        "probe_index": j,
                        "observed": actual,
                    })
    return {
        "policy": "B3",
        "fixture_sha256": pilot.manifest(),
        "cost_usd": 0.0,  # no paid external API; NOT a total-cost estimate
        "elapsed_seconds": 0.0,  # placeholder required by the original scorer
        "findings": warnings,
    }, evaluations, dict(sorted(family_checks.items()))


def exercise_negative_controls(report):
    controls = {}
    # Same task universe, deliberately omit one proven fault.
    missed = {**report, "findings": report["findings"][1:]}
    controls["one_true_warning_removed_reduces_recall"] = (
        pilot.validate_and_score(missed)["verified_unique_warnings"] == 19
    )
    # Deliberately tamper one correct observed value: cannot pass the scorer.
    changed = [dict(x) for x in report["findings"]]
    changed[0]["observed"] = "__tampered__"
    tampered = {**report, "findings": changed}
    tamper_score = pilot.validate_and_score(tampered)
    controls["fabricated_observation_rejected"] = (
        tamper_score["verified_unique_warnings"] == 19
        and tamper_score["unsupported_alerts_faulty_cases"] == 1
    )
    # The scorer must penalize unsupported alarms against clean tasks.
    clean = next(c for c in pilot.cases() if not c["faulty"])
    clean_claim = {
        "case_id": clean["case_id"],
        "probe_index": 0,
        "observed": pilot.observed(clean, 0),
    }
    extra = {**report, "findings": report["findings"] + [clean_claim]}
    controls["clean_case_false_alarm_counted"] = (
        pilot.validate_and_score(extra)["false_alerts_clean_cases"] == 1
    )
    repeated = {**report, "findings": report["findings"] + report["findings"][:1]}
    try:
        pilot.validate_and_score(repeated)
    except ValueError:
        controls["duplicate_credit_rejected"] = True
    else:
        controls["duplicate_credit_rejected"] = False
    return controls


def run():
    report, evaluations, families = checker_report()
    result = pilot.validate_and_score(report)
    empty = {**report, "policy": "B0", "findings": []}
    zero = pilot.validate_and_score(empty)
    controls = exercise_negative_controls(report)
    assert evaluations == sum(len(c["probes"]) for c in pilot.cases())
    assert len(families) == 10 and len(report["findings"]) == 20
    assert all(controls.values()), controls
    assert result["verified_unique_warnings"] == 20, result
    assert result["false_alerts_clean_cases"] == 0, result
    assert zero["verified_unique_warnings"] == 0, zero
    return {
        "status": "PROJECT_AUTHORED_NONBLIND_CHECKER_DEMONSTRATION_ONLY",
        "fixture_sha256": pilot.manifest(),
        "cases": 40,
        "faulty_cases": 20,
        "correct_cases": 20,
        "families": 10,
        "B0_no_verification": {
            "verified_warnings": zero["verified_unique_warnings"],
            "probe_evaluations": 0,
        },
        "B3_expected_answer_checker": {
            "verified_warnings": result["verified_unique_warnings"],
            "false_alarms": result["false_alerts_clean_cases"],
            "probe_evaluations": evaluations,
            "probe_evaluations_by_family": families,
            "paid_external_api_calls": 0,
            "true_compute_and_human_cost": "NOT_MEASURED",
        },
        "negative_controls": controls,
        "known_invalid_inference": [
            "expected outputs were accessible to B3: not blind, and not a fair matched-budget AI comparison",
            "the same project authors the fixture, checker, scoring, and negative controls",
            "B0 and B3 have unequal work budgets",
            "warnings do not measure actual repairs, value of independent voices, social contributions, or real-world outcomes",
            "cost_usd and elapsed_seconds are required placeholders, not actual overhead measurements",
        ],
        "original_pilot_mutated": False,
        "external_validation": "NOT_OBTAINED",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    outcome = run()
    print(json.dumps(outcome, ensure_ascii=False, sort_keys=True, indent=2))
    if not args.verify:
        print("Scope: deterministic nonblind internal control; not independent validation.")


if __name__ == "__main__":
    main()
