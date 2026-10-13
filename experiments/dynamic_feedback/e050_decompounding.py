"""Project-originated E050 synthetic calculation. Public review, no general reuse license. See LICENSE_STATUS.md."""

import math
import json

def run(T=100, t0=20, friction=0.0, g_bonus=0.0, gain_a_after=None):
    H, K = 0.0, 0.01
    beta, rho = 5.0, 0.92
    gain_g, gain_a = 0.28, 0.28
    rows = []
    for t in range(T):
        if t >= t0:
            fr = friction
            gb = g_bonus
            ga = gain_a if gain_a_after is None else gain_a_after
        else:
            fr = 0.0
            gb = 0.0
            ga = gain_a
        score_g = 0.5 + gb + gain_g * H
        score_a = 0.5 + ga * K - fr
        alloc_a = 1.0 / (1.0 + math.exp(-beta * (score_a - score_g)))
        alloc_g = 1.0 - alloc_a
        rows.append({"t":t,"H":H,"K":K,"score_g":score_g,"score_a":score_a,
                     "alloc_g":alloc_g,"alloc_a":alloc_a})
        H = rho * H + alloc_g
        K = rho * K + alloc_a
    return rows

cases = {
    "baseline": run(),
    "friction_2": run(friction=2.0),
    "gbonus_1": run(g_bonus=1.0),
    "decompound": run(gain_a_after=0.05),
    "decompound_plus_g": run(gain_a_after=0.05,g_bonus=0.2),
    "combined": run(gain_a_after=0.05,g_bonus=0.2,friction=0.5),
}

summary = {k:v[-1] for k,v in cases.items()}

min_friction = None
for n in range(81):
    f = n * 0.05
    if run(friction=f)[-1]["alloc_g"] > 0.90:
        min_friction = f
        break

min_g_bonus = None
for n in range(81):
    g = n * 0.05
    if run(g_bonus=g)[-1]["alloc_g"] > 0.90:
        min_g_bonus = g
        break

max_gain_a_for_switch = None
for n in range(57):
    ga = n * 0.005
    if run(gain_a_after=ga)[-1]["alloc_g"] > 0.90:
        max_gain_a_for_switch = ga

assert summary["baseline"]["alloc_a"] > 0.999
assert summary["gbonus_1"]["alloc_a"] > 0.999
assert summary["decompound"]["alloc_g"] > 0.999
late_g = run(t0=80, gain_a_after=0.05)[-1]["alloc_g"]
assert 0.19 < late_g < 0.20  # timing counterexample
assert min_friction == 1.8
assert min_g_bonus == 1.8
assert round(max_gain_a_for_switch, 2) == 0.08

print(json.dumps({
    "summary": summary,
    "late_intervention_counterexample": {"t0": 80, "final_alloc_g": late_g, "threshold_reached": late_g > 0.90},
    "thresholds": {
        "min_friction": min_friction,
        "min_g_bonus": min_g_bonus,
        "max_gain_a_for_switch": max_gain_a_for_switch
    }
}, ensure_ascii=False, indent=2))
