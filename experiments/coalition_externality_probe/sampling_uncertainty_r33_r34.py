#!/usr/bin/env python3
"""Reconstructed R33/R34 sampling-design counterexamples (synthetic only).

This is a new, transparent derivation of reported numerical checks. It is NOT a
copy of the original job scripts, a population estimate, or an independent
replication. Requires only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import combinations
import json


def ess(weights):
    return sum(weights) ** 2 / sum(w * w for w in weights)


def r33():
    # One harm and nineteen nonharms: observed simple rate 1/20.
    y = [1] + [0] * 19
    w = [Q(40)] + [Q(1)] * 19
    wt_rate = sum(a*b for a, b in zip(w, y)) / sum(w)
    cap = [min(a, Q(2)) for a in w]
    cap_rate = sum(a*b for a, b in zip(cap, y)) / sum(cap)
    assert Q(sum(y),len(y)) == Q(1,20)
    assert wt_rate == Q(40,59)
    assert ess(w) == Q(3481,1619)
    assert cap_rate == Q(2,21)
    assert ess(cap) == Q(441,23)
    # Population N=1000, 20 recorded, 980 missing; no assumptions.
    lower, upper = Q(1,1000), Q(981,1000)
    assert 100 * lower == Q(1,10) and 100 * upper == Q(981,10)
    return {"unweighted_rate": 1/20, "weighted_rate": float(wt_rate),
            "ess": float(ess(w)), "capped_rate": float(cap_rate),
            "capped_ess": float(ess(cap)), "population_bounds":
            [float(lower),float(upper)]}


def r34(p):
    # Four binary outcomes: 0,0,1,1. Exactly two sampled each time.
    # Same-outcome pairs carry p/2 each; four mixed pairs (1-p)/4 each.
    y = (0,0,1,1)
    pairs = list(combinations(range(4),2))
    probs = {(a,b): (p/2 if y[a] == y[b] else (1-p)/4)
             for a,b in pairs}
    assert sum(probs.values()) == 1
    inclusion = [sum(prob for (a,b),prob in probs.items() if i in (a,b))
                 for i in range(4)]
    assert inclusion == [Q(1,2)]*4
    assert {ess([Q(2),Q(2)]) for _ in pairs} == {Q(2)}
    mean = sum(prob * Q(y[a]+y[b],2) for (a,b),prob in probs.items())
    variance = sum(prob*(Q(y[a]+y[b],2)-mean)**2
                   for (a,b),prob in probs.items())
    assert mean == Q(1,2) and variance == p/4
    return {"p_homogeneous":float(p), "inclusion_pi":[float(v) for v in inclusion],
            "ess_each_sample":2, "design_variance":float(variance),
            "joint_pair_probabilities":
            {f"{a},{b}":float(prob) for (a,b),prob in probs.items()}}


def main():
    high = r34(Q(4,5))
    low = r34(Q(1,10))
    assert high["design_variance"] == 0.2
    assert low["design_variance"] == 0.025
    assert high["ess_each_sample"] == low["ess_each_sample"] == 2
    assert high["inclusion_pi"] == low["inclusion_pi"]
    report = {
      "status":"SYNTHETIC_ARITHMETIC_RECONSTRUCTION_NOT_EMPIRICAL",
      "R33":r33(),
      "R34":{"high_variance":high,"low_variance":low,"variance_ratio":8},
      "interpretation":"Identical first-order inclusion and Kish ESS do not determine design variance; joint inclusion structure matters.",
      "limits":["R33 weighted estimate needs justified inclusion probabilities",
                "weight capping changes estimator/bias",
                "missing outcome bounds are logical, not confidence intervals",
                "not original script readback, not external scientific replication",
                "no evidence here about real agents or long-term coexistence"]
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return report


if __name__ == "__main__":
    main()
