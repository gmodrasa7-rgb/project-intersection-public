#!/usr/bin/env python3
"""Finite boxed uncertainty check, not real agent observations.
Run: python3 robustness.py > C15_ROBUSTNESS.json
"""
from itertools import product
import json

def decide(g, r, v):
    return "C_STRICT" if r + v > g else "X_STRICT" if r + v < g else "TIE"

cases = []
for g0, r0, v0, dg, dr, dv in product((1, 3, 5), (2, 4, 6), (2, 4),
                                      (0, 1, 2), (0, 1, 2), (0, 1, 2)):
    margin = r0 + v0 - g0 - (dg + dr + dv)
    all_strict = all(decide(g0 + i, r0 - j, v0 - k) == "C_STRICT"
                     for i in range(dg + 1)
                     for j in range(dr + 1)
                     for k in range(dv + 1))
    assert all_strict == (margin > 0)
    cases.append(dict(g0=g0, r0=r0, v0=v0,
                      max_exploitation_gain_shock=dg,
                      max_protection_value_loss=dr,
                      max_option_value_loss=dv,
                      worst_margin=margin,
                      all_shock_realizations_strictly_coexist=all_strict))
assert len(cases) == 486
assert any(x["worst_margin"] == 0 for x in cases)
assert any(x["worst_margin"] < 0 for x in cases)
assert any(x["worst_margin"] > 0 for x in cases)

result = {
    "schema": "PI.C15.robust-margin.v1",
    "status": "EXECUTED_FINITE_DETERMINISTIC_TEST_NOT_AGENT_EXPERIMENT",
    "date": "2026-10-21",
    "bounded_shock_scenarios": len(cases),
    "always_strictly_preserved": sum(x["all_shock_realizations_strictly_coexist"] for x in cases),
    "not_strictly_guaranteed": sum(not x["all_shock_realizations_strictly_coexist"] for x in cases),
    "sharp_bound": "r0+v0-g0 > dg+dr+dv iff strict C for all independently feasible shocks in this toy model",
    "proof": "The lowest margin occurs at g=g0+dg, r=r0-dr and v=v0-dv. All box corners are feasible. If the margin is zero the optimum is not uniquely C; if below zero X uniquely dominates.",
    "parameters": {"g0": [1,3,5], "r0": [2,4,6], "v0": [2,4], "each_d": [0,1,2]},
    "examples": {
        "safe": next(x for x in cases if x["worst_margin"] > 0),
        "tie_possible": next(x for x in cases if x["worst_margin"] == 0),
        "override_possible": next(x for x in cases if x["worst_margin"] < 0)},
    "limitations": ["Assumes additive normalized utilities r+v vs g.",
        "No claim about moral preferences or real independent B.",
        "Strict protection on a finite box is not unbounded longitudinal or self-modification safety."]
}
print(json.dumps(result, ensure_ascii=False, indent=2))
