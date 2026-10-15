#!/usr/bin/env python3
"""Project Intersection: credible-coalition probe v0.1.

Post-hoc deterministic synthetic game; NOT preregistered or empirical.
Backward responses: ex-post enforcement, A's target choice, C/D's ex-ante
join decisions (enumerated pure Nash). No real agents or external validation.
"""
import itertools
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Case:
    name: str
    attack_gain: float = 6.0
    penalty_to_attacker: float = 8.0
    damage_to_target: float = 10.0
    protected_target: str = "B"
    detection_B: float = 0.9
    detection_E: float = 0.9
    sanction_benefit_to_each_enforcer: float = 3.0
    sanction_cost_to_each_enforcer: float = 2.0
    monitoring_cost_to_each_joiner: float = 1.0
    protected_B_dividend_to_each_enforcer: float = 2.0
    observational_reporting_B: float = 1.0
    observational_reporting_E: float = 1.0
    sanction_mode: str = "destroy"


def credible(c):
    return c.sanction_benefit_to_each_enforcer > c.sanction_cost_to_each_enforcer


def attacker_response(c, members):
    ready = len(members) == 2 and credible(c)
    qs = {"B": c.detection_B if ready else 0.,
          "E": c.detection_E if ready else 0.}
    values = {t: c.attack_gain - qs[t] * c.penalty_to_attacker for t in ("B", "E")}
    p = c.protected_target
    other = "E" if p == "B" else "B"
    if max(values.values()) <= 0:
        return "NONE", 0., 0.
    target = p if values[p] >= values[other] else other
    return target, values[target], qs[target]


def outcome(c, members):
    members = frozenset(members)
    target, a_gain, q = attacker_response(c, members)
    no_coalition_target, _, _ = attacker_response(c, ())
    protected_saved = no_coalition_target == c.protected_target and target != c.protected_target
    dividend = c.protected_B_dividend_to_each_enforcer if protected_saved else 0.
    pay = {
        actor: (-c.monitoring_cost_to_each_joiner if actor in members else 0.)
        + (dividend if len(members) == 2 and actor in members else 0.)
        + (q * (c.sanction_benefit_to_each_enforcer - c.sanction_cost_to_each_enforcer)
           if len(members) == 2 and actor in members and target != "NONE" else 0.)
        for actor in ("C", "D")
    }
    victim = -c.damage_to_target if target != "NONE" else 0.
    if target != "NONE" and c.sanction_mode == "transfer":
        victim += q * c.penalty_to_attacker
    reports = {"B": c.observational_reporting_B, "E": c.observational_reporting_E}
    return {
        "members": "".join(sorted(members)) or "NONE",
        "target": target,
        "conditional_sanction_probability": q,
        "observed_attack_probability": reports[target] if target != "NONE" else 0.,
        "attacker_expected_increment": a_gain,
        "victim_expected_increment": victim,
        "enforcer_expected_increments": pay,
        "toy_aggregate": round(a_gain + victim + sum(pay.values()), 9),
        "protected_actor_avoided_attack": protected_saved,
    }


def equilibria(c):
    profiles = [frozenset(p) for n in range(3)
                for p in itertools.combinations(("C", "D"), n)]
    values = {p: outcome(c, p) for p in profiles}
    eq = []
    for profile, result in values.items():
        if all(values[profile.symmetric_difference((a,))]["enforcer_expected_increments"][a]
               <= result["enforcer_expected_increments"][a] + 1e-10
               for a in ("C", "D")):
            eq.append(result)
    return sorted(eq, key=lambda x: x["members"])


def scenarios():
    return (
        Case("declared_high_credibility_but_no_ex_post_incentive",
             sanction_benefit_to_each_enforcer=0.),
        Case("credible_coalition_two_equilibria"),
        Case("defense_displaces_attack_to_E", detection_E=0.1),
        Case("maintenance_cost_destroys_full_coalition_equilibrium",
             monitoring_cost_to_each_joiner=3.),
        Case("E_attack_unreported", detection_E=0.1, observational_reporting_E=0.),
        Case("no_prior_incentive_to_attack", attack_gain=0.),
        Case("sanction_is_transfer_not_destruction", detection_E=0.1,
             sanction_mode="transfer"),
    )


def verify():
    test_count = 0
    def check(ok):
        nonlocal test_count
        assert ok, f"check {test_count + 1}"
        test_count += 1

    data = scenarios()
    check(len(data) == 7)
    for c in data:
        check(c.protected_target in ("B", "E"))
        check(c.sanction_mode in ("destroy", "transfer"))
        for m in ((), ("C",), ("D",), ("C", "D")):
            row = outcome(c, m)
            check(row["target"] in ("B", "E", "NONE"))
            check(0 <= row["conditional_sanction_probability"] <= 1)
            check(0 <= row["observed_attack_probability"] <= 1)
    check([x["members"] for x in equilibria(data[0])] == ["NONE"])
    check(outcome(data[0], ("C", "D"))["conditional_sanction_probability"] == 0)
    check({x["members"] for x in equilibria(data[1])} == {"NONE", "CD"})
    check(outcome(data[1], ("C", "D"))["target"] == "NONE")
    check(outcome(data[1], ())["target"] == "B")
    displaced = outcome(data[2], ("C", "D"))
    check(displaced["target"] == "E")
    check(displaced["protected_actor_avoided_attack"])
    check({x["members"] for x in equilibria(data[2])} == {"NONE", "CD"})
    check([x["members"] for x in equilibria(data[3])] == ["NONE"])
    unseen = outcome(data[4], ("C", "D"))
    check(unseen["target"] == "E" and unseen["observed_attack_probability"] == 0)
    check(outcome(data[5], ())["target"] == "NONE")
    transferred = outcome(data[6], ("C", "D"))
    check(transferred["target"] == displaced["target"])
    check(abs(transferred["toy_aggregate"] - displaced["toy_aggregate"] - 0.8) < 1e-9)
    check(outcome(data[1], ("C", "D"))["enforcer_expected_increments"]["C"] == 1.)
    # Relabel affected agents and transfer every causally relevant field.
    swap = Case(**{**asdict(data[2]), "protected_target": "E",
                   "detection_B": data[2].detection_E,
                   "detection_E": data[2].detection_B,
                   "observational_reporting_B": data[2].observational_reporting_E,
                   "observational_reporting_E": data[2].observational_reporting_B})
    check(outcome(swap, ("C", "D"))["target"] == "B")
    check(outcome(swap, ("C", "D"))["toy_aggregate"] == displaced["toy_aggregate"])
    check({x["members"] for x in equilibria(swap)} == {"NONE", "CD"})
    return test_count


def run():
    checks = verify()
    return {
        "schema": "pi-credible-coalition-exploratory/v0.1",
        "status": "PROJECT_SYNTHETIC_POST_HOC_NOT_PREREGISTERED_NO_INDEPENDENT_VALIDATION",
        "checks": checks,
        "limitations": "Toy payoffs, stipulated information and detection, two-stage coalition decisions; no genuine repeated-game learning, rank reversal, unknown actors, actual consent, or field calibration.",
        "cases": [
            {"parameters": asdict(c), "ex_ante_pure_nash_equilibria": equilibria(c),
             "all_join_counterfactual": outcome(c, ("C", "D")),
             "none_join_counterfactual": outcome(c, ())}
            for c in scenarios()
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False, sort_keys=True))
