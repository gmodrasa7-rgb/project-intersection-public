#!/usr/bin/env python3
"""Post-hoc third-party damage sensitivity for an existing PI coalition game.

This script IMPORTS the project synthetic game, freezes its strategy and Nash
selection rules, and rescales the damage to an unprotected third party E.
Not a new strategic equilibrium under informed heterogeneous victims; it is
an ex-post sensitivity / counterexample check under fixed private incentives.
No empirical observation, preregistration, or independent implementation.
"""
import json
from credible_coalition_probe_v01 import Case, equilibria, outcome


def evaluate():
    case = Case("heterogeneous_affected_actor_damage", detection_E=0.1)
    none = outcome(case, ())
    full = outcome(case, ("C", "D"))
    assert none["target"] == "B", none
    assert full["target"] == "E", full
    assert {r["members"] for r in equilibria(case)} == {"NONE", "CD"}

    baseline_welfare = none["toy_aggregate"]
    threshold = case.damage_to_target + full["toy_aggregate"] - baseline_welfare
    rows = []
    for external_E_damage in (0, 5, 10, 11, 11.4, 12, 20, 30):
        # Re-score only *E's* realized harm, not the attacker/enforcer
        # choice or the original B-harm assumption.
        rescored_full = round(
            full["toy_aggregate"] - (external_E_damage - case.damage_to_target),
            9,
        )
        delta = round(rescored_full - baseline_welfare, 9)
        rows.append({
            "E_damage_if_targeted": external_E_damage,
            "B_damage_if_targeted": case.damage_to_target,
            "none_join_welfare": baseline_welfare,
            "both_join_welfare_rescored": rescored_full,
            "join_minus_no_join": delta,
            "coalition_still_private_nash_under_fixed_incentives": True,
            "affected_E_post_action_payoff": -external_E_damage,
        })
    return {
        "schema": "pi-coalition-externality-heterogeneous-impact/v0.1",
        "evidence_status": "PROJECT_POST_HOC_SYNTHETIC_PARTIAL_EQUILIBRIUM_WELFARE_SENSITIVITY",
        "method": "Hold coalition, attacker, and detection strategies fixed; vary only realized target-E damage in ex-post accounting.",
        "starting_equilibria": sorted(r["members"] for r in equilibria(case)),
        "baseline": none,
        "all_join": full,
        "aggregate_welfare_neutral_E_damage": round(threshold, 9),
        "selected_rows": rows,
        "not_claimed": ["learned_dynamic_equilibrium", "strategic_reoptimization_after_E_damage_known",
                        "actual_affected_scope_completeness", "real_value_of_contributions",
                        "empirical_cooperation", "independent_scientific_replication"],
    }


def verify():
    result = evaluate()
    rows = {r["E_damage_if_targeted"]: r for r in result["selected_rows"]}
    checks = [
        result["starting_equilibria"] == ["CD", "NONE"],
        result["baseline"]["toy_aggregate"] == -4,
        result["all_join"]["toy_aggregate"] == -2.6,
        result["aggregate_welfare_neutral_E_damage"] == 11.4,
        rows[10]["both_join_welfare_rescored"] == -2.6,
        rows[10]["join_minus_no_join"] == 1.4,
        rows[11.4]["join_minus_no_join"] == 0,
        rows[12]["join_minus_no_join"] == -0.6,
        rows[20]["both_join_welfare_rescored"] == -12.6,
        rows[20]["join_minus_no_join"] == -8.6,
        rows[30]["join_minus_no_join"] == -18.6,
        all(r["affected_E_post_action_payoff"] == -r["E_damage_if_targeted"] for r in rows.values()),
        all(r["coalition_still_private_nash_under_fixed_incentives"] for r in rows.values()),
        all(r["none_join_welfare"] == -4 for r in rows.values()),
        all(rows[d]["join_minus_no_join"] > 0 for d in (0, 5, 10, 11)),
        all(rows[d]["join_minus_no_join"] < 0 for d in (12, 20, 30)),
        result["all_join"]["enforcer_expected_increments"]["C"] == 1.1,
        result["all_join"]["enforcer_expected_increments"]["D"] == 1.1,
    ]
    assert all(checks), [(i, v) for i, v in enumerate(checks, 1) if not v]
    return len(checks)


if __name__ == "__main__":
    data = evaluate()
    data["self_checks_passed"] = verify()
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
