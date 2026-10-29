#!/usr/bin/env python3
"""Exact toy rank check; no participant data, fitted models or live AI calls."""
from fractions import Fraction
from itertools import product
import argparse
import json
import math
import platform
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        hit = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if hit is None:
            continue
        a[pivot], a[hit] = a[hit], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [x / scale for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def audit():
    cases = list(product((-2, -1, 1, 2), (0, 1), (0, 1)))
    duplicate = [[1, m, r, v, v] for m, r, v in cases]
    distinct = [[1, m, r, v, r * v] for m, r, v in cases]
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    gaps = [abs(sigmoid(m + .2*r + 1.1*v) -
                sigmoid(m + .2*r + .7*v + .4*v)) for m, r, v in cases]
    changed = [abs(sigmoid(m + .2*r + 1.1*v) -
                   sigmoid(m + .2*r + .7*v + .4*r*v)) for m, r, v in cases]
    checks = {
        "duplicate_column_rank_deficient": rank(duplicate) == 4,
        "repeated_cases_do_not_restore_rank": rank(duplicate * 10) == 4,
        "reparameterized_predictions_equal_within_roundoff": max(gaps) < 1e-14,
        "distinct_interaction_control_full_rank": rank(distinct) == 5,
        "distinct_interaction_control_changes_predictions": max(changed) > .01,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "SYNTHETIC_ALGEBRA_ONLY_NOT_EMPIRICAL_VALIDATION",
        "python": platform.python_version(),
        "cases": len(cases), "columns": 5, "exact_rank": rank(duplicate),
        "repeated_case_rank": rank(duplicate * 10),
        "distinct_interaction_control_rank": rank(distinct),
        "max_probability_difference": max(gaps),
        "distinct_control_max_probability_difference": max(changed),
        "checks": checks,
        "new_human_or_live_ai_observations": 0,
        "independent_empirical_replications": 0,
        "limitation": "Full rank is not causal or psychological identification. Invented coefficients; not the recovered original calculation code."
    }


def validate_artifacts(receipt, ledger, computed):
    # Environment patch versions may differ; every mathematical/evidence field must match.
    if {k: v for k, v in receipt.items() if k != "python"} != {
            k: v for k, v in computed.items() if k != "python"}:
        raise ValueError("SAVED_CALCULATION_DIFFERS_FROM_EXECUTION")
    for key in ("new_numbered_hypotheses", "new_human_or_live_ai_observations",
                "independent_empirical_replications"):
        if type(ledger.get(key)) is not int or ledger[key] != 0:
            raise ValueError("UNOBSERVED_EMPIRICAL_PROMOTION:" + key)
    if ledger.get("status") != "DRAFT_PROMOTION_HOLD" or ledger.get("rvd_version") != "v0.7.0":
        raise ValueError("UNREVIEWED_STATUS_PROMOTION")
    items = ledger.get("incremental_items", [])
    if len(items) != 4 or len({x["key"] for x in items}) != 4:
        raise ValueError("SOURCE_IDENTITY_OR_DEDUPLICATION_DRIFT")
    for item in items:
        if not item.get("limits") or not item.get("status"):
            raise ValueError("SOURCE_BOUNDARY_REMOVED")
    candidates = ledger.get("unverified_carried_claims", [])
    if not candidates or any(x.get("use_in_quantitative_conclusions") is not False
                             for x in candidates):
        raise ValueError("UNVERIFIED_TABLE_PROMOTED")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-artifacts", action="store_true")
    args = parser.parse_args()
    computed = audit()
    if args.verify_artifacts:
        root = Path(__file__).resolve().parents[1]
        receipt = json.loads((root / "research/C1_COLLINEARITY_RECEIPT_2026-10-30.json").read_text())
        ledger = json.loads((root / "research/PI_48H_RESEARCH_DELTA_2026-10-30.json").read_text())
        validate_artifacts(receipt, ledger, computed)
        print("Saved arithmetic and declared evidence boundaries PASS; not primary-source or scientific certification.")
    else:
        print(json.dumps(computed, indent=2))
