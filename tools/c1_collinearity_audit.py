#!/usr/bin/env python3
"""Exact toy rank check; no participant data, fitted models or live AI calls."""
from fractions import Fraction
from itertools import product
import json
import math
import platform


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


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
