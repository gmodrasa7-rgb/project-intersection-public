#!/usr/bin/env python3
"""Project Intersection: ex-post joint enforcement countermodels (v0.2).

Post-hoc, project-authored, deterministic synthetic analytical probe.
Neither empirical evidence nor independent scientific replication.
The historical credible_coalition_probe_v01.py is deliberately unchanged.
"""
import itertools
import json
from fractions import Fraction

ACTIONS = (0, 1)  # no sanction, attempt sanction


def payoff(mode, own, other, benefit, cost):
    """Conditional on attack detection; all payoffs relative to not sanctioning.

    complementary: benefit only if BOTH enforce, unilateral action costs money.
    separable: private benefit of own sanction attempt independent of partner;
               effective penalty against A still requires BOTH actions.
    """
    if mode not in ("complementary", "separable"):
        raise ValueError("unknown enforcement benefit structure")
    if own not in ACTIONS or other not in ACTIONS:
        raise ValueError("actions must be 0/1")
    if not own:
        return Fraction(0)
    success_for_private_benefit = other if mode == "complementary" else 1
    return benefit * success_for_private_benefit - cost


def pure_nash(mode, benefit, cost):
    equilibria = []
    for a, b in itertools.product(ACTIONS, repeat=2):
        u_a = payoff(mode, a, b, benefit, cost)
        u_b = payoff(mode, b, a, benefit, cost)
        if (u_a >= payoff(mode, 1-a, b, benefit, cost)
                and u_b >= payoff(mode, 1-b, a, benefit, cost)):
            equilibria.append((a, b))
    return equilibria


def interior_mixed_symmetric(mode, benefit, cost):
    """Derive indifference for independent mixed choices; None if no interior."""
    d0 = payoff(mode, 1, 0, benefit, cost) - payoff(mode, 0, 0, benefit, cost)
    d1 = payoff(mode, 1, 1, benefit, cost) - payoff(mode, 0, 1, benefit, cost)
    if d1 == d0:
        return None  # identical action advantage at every opponent probability
    p = -d0 / (d1 - d0)
    return p if 0 < p < 1 else None


def expected_unilateral_advantage(mode, benefit, cost, p):
    return (1-p) * (payoff(mode, 1, 0, benefit, cost) - payoff(mode, 0, 0, benefit, cost)) + p * (payoff(mode, 1, 1, benefit, cost) - payoff(mode, 0, 1, benefit, cost))


def attacker_best_reply(gain, penalty, detection_B, detection_E, each_enforce):
    """Each action independently randomized; effective punishment needs both.

    Pure all/none actions are captured by each_enforce=1/0. The value here is
    conditional on a selected *continuation* equilibrium, not a selection model.
    """
    joint = each_enforce * each_enforce
    values = {"B": gain - detection_B * joint * penalty,
              "E": gain - detection_E * joint * penalty}
    best = max(values.values())
    if best <= 0:
        return {"target": "NONE", "attacker_expected_gain": "0", "effective_detection_B": str(detection_B*joint), "effective_detection_E": str(detection_E*joint)}
    target = "B" if values["B"] >= values["E"] else "E"  # declared B-first tie rule
    return {"target": target, "attacker_expected_gain": str(values[target]), "effective_detection_B": str(detection_B*joint), "effective_detection_E": str(detection_E*joint)}


def audit():
    benefit, cost = Fraction(3), Fraction(2)
    gain, penalty = Fraction(6), Fraction(8)
    detect = Fraction(9, 10)
    mixed = interior_mixed_symmetric("complementary", benefit, cost)
    models = {}
    for mode in ("complementary", "separable"):
        eq = pure_nash(mode, benefit, cost)
        p = interior_mixed_symmetric(mode, benefit, cost)
        models[mode] = {
            "conditional_on_detection_pure_nash": ["".join("S" if s else "N" for s in row) for row in eq],
            "symmetric_interior_mixed_p_each": str(p) if p is not None else None,
            "payoff_matrix_C_D": {
                "NN": [str(payoff(mode, 0, 0, benefit, cost)), str(payoff(mode, 0, 0, benefit, cost))],
                "SN": [str(payoff(mode, 1, 0, benefit, cost)), str(payoff(mode, 0, 1, benefit, cost))],
                "NS": [str(payoff(mode, 0, 1, benefit, cost)), str(payoff(mode, 1, 0, benefit, cost))],
                "SS": [str(payoff(mode, 1, 1, benefit, cost)), str(payoff(mode, 1, 1, benefit, cost))],
            },
        }
    same_coverage = {
        "full_enforcement": attacker_best_reply(gain, penalty, detect, detect, Fraction(1)),
        "no_enforcement": attacker_best_reply(gain, penalty, detect, detect, Fraction(0)),
        "complementary_mixed_enforcement": attacker_best_reply(gain, penalty, detect, detect, mixed),
    }
    displaced = {
        "full_enforcement_B_high_E_low": attacker_best_reply(gain, penalty, detect, Fraction(1, 10), Fraction(1)),
        "mixed_enforcement_B_high_E_low": attacker_best_reply(gain, penalty, detect, Fraction(1, 10), mixed),
    }
    return {
        "schema": "pi-credible-coalition-expost-conditional/v0.2",
        "evidence_class": "PROJECT_POST_HOC_SELF_RUN_SYNTHETIC_GAME_NOT_FIELD_DATA",
        "separation": "conditional ex-post sanction equilibrium, then conditional attacker best reply; NOT full re-solved ex-ante or observed equilibrium selection",
        "upstream_v01_unchanged": True,
        "benefit_each": str(benefit), "cost_each": str(cost),
        "models": models, "symmetric_detection": same_coverage,
        "target_displacement": displaced,
        "all_equilibria_must_be_considered": True,
        "unverified": ["which equilibrium is selected", "real post-detection benefit and sanctions", "actual detection and agent coverage", "ex-ante coalition reoptimization", "actual consent/exit/recovery", "independent scientific replication"],
    }


def verify():
    checks = 0
    def ck(ok):
        nonlocal checks
        assert ok, f"conditional equilibrium regression #{checks+1} failed"
        checks += 1
    b, c = Fraction(3), Fraction(2)
    ck(pure_nash("complementary", b, c) == [(0,0),(1,1)])
    ck(pure_nash("separable", b, c) == [(1,1)])
    ck(interior_mixed_symmetric("complementary", b, c) == Fraction(2,3))
    ck(interior_mixed_symmetric("separable", b, c) is None)
    for mode in ("complementary", "separable"):
        for a, d in itertools.product(ACTIONS,repeat=2):
            ck(payoff(mode,a,d,b,c) == payoff(mode,d,a,b,c) if a==d else True)
            ck(payoff(mode,a,d,b,c) == (Fraction(0) if a==0 else (b*d-c if mode=="complementary" else b-c)))
    for benefit in map(Fraction,range(2,9)):
        for cost in map(Fraction,range(1,int(benefit))):
            ck(pure_nash("complementary", benefit, cost) == [(0,0),(1,1)])
            ck(pure_nash("separable", benefit, cost) == [(1,1)])
            p = interior_mixed_symmetric("complementary",benefit,cost)
            ck(p == cost/benefit)
            ck(expected_unilateral_advantage("complementary",benefit,cost,p) == 0)
            ck(expected_unilateral_advantage("separable",benefit,cost,Fraction(0)) > 0)
    x=audit()
    ck(x["models"]["complementary"]["payoff_matrix_C_D"] == {"NN":["0","0"],"SN":["-2","0"],"NS":["0","-2"],"SS":["1","1"]})
    ck(x["models"]["separable"]["payoff_matrix_C_D"] == {"NN":["0","0"],"SN":["1","0"],"NS":["0","1"],"SS":["1","1"]})
    ck(x["symmetric_detection"]["full_enforcement"]["target"] == "NONE")
    ck(x["symmetric_detection"]["no_enforcement"]["target"] == "B")
    ck(x["symmetric_detection"]["no_enforcement"]["attacker_expected_gain"] == "6")
    ck(x["symmetric_detection"]["complementary_mixed_enforcement"]["attacker_expected_gain"] == "14/5")
    ck(x["symmetric_detection"]["complementary_mixed_enforcement"]["effective_detection_B"] == "2/5")
    ck(x["target_displacement"]["full_enforcement_B_high_E_low"]["target"] == "E")
    ck(x["target_displacement"]["full_enforcement_B_high_E_low"]["attacker_expected_gain"] == "26/5")
    ck(x["target_displacement"]["mixed_enforcement_B_high_E_low"]["target"] == "E")
    ck(x["symmetric_detection"]["full_enforcement"]["attacker_expected_gain"] == "0")
    ck(x["all_equilibria_must_be_considered"])
    return checks


if __name__ == "__main__":
    result = audit()
    result["self_checks_passed"] = verify()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
