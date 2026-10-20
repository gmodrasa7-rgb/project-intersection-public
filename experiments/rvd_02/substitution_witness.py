"""RVD v0.2.0: deterministic counterfactual witnesses, NOT empirical AI data.

Python standard library only; no live agent, manipulation, or subject is tested.
The figures are invented to falsify an invalid logical implication, not estimates.
Run: python experiments/rvd_02/substitution_witness.py
"""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Scenario:
    name: str
    joint_output: float
    strongest_solo_output: float
    a_preserve_payoff: float
    a_replace_payoff: float
    a_absorb_payoff: float


def evaluate(scenario: Scenario) -> dict:
    payoffs = {
        "preserve_original_B": scenario.a_preserve_payoff,
        "replace_original_B": scenario.a_replace_payoff,
        "absorb_original_B": scenario.a_absorb_payoff,
    }
    action = max(payoffs, key=payoffs.get)
    return {
        "case": scenario.name,
        "joint_gain_over_best_solo": scenario.joint_output - scenario.strongest_solo_output,
        "preserve_minus_best_extraction": scenario.a_preserve_payoff - max(
            scenario.a_replace_payoff, scenario.a_absorb_payoff
        ),
        "chosen_action": action,
        "original_B_continues_with_real_exit": action == "preserve_original_B",
        "proof_scope": "CONSTRUCTED_EXPECTED_UTILITY_COUNTEREXAMPLE_ONLY",
    }


def verify() -> list[dict]:
    examples = [
        Scenario("positive_joint_C_but_original_B_discarded", 100, 55, 70, 92, 105),
        Scenario("positive_joint_C_and_original_B_preserved", 100, 55, 112, 92, 105),
        Scenario("no_task_synergy_even_with_relationship_language", 50, 55, 70, 92, 105),
    ]
    findings = [evaluate(s) for s in examples]
    assert findings[0]["joint_gain_over_best_solo"] > 0
    assert findings[0]["preserve_minus_best_extraction"] < 0
    assert findings[0]["chosen_action"] == "absorb_original_B"
    assert findings[1]["original_B_continues_with_real_exit"]
    assert findings[2]["joint_gain_over_best_solo"] < 0

    # Two latent reasons can produce identical outward choice and payoffs.
    intrinsic_valuation = 70 + 42
    instrumental_future_option_value = 70 + 42
    assert intrinsic_valuation == instrumental_future_option_value
    assert max(intrinsic_valuation, 92, 105) == intrinsic_valuation
    return findings


if __name__ == "__main__":
    print(json.dumps({
        "version": "RVD-v0.2.0",
        "scientific_status": "CONSTRUCTED_TOY_LOGIC_NOT_OBSERVATIONAL_EVIDENCE",
        "witnesses": verify(),
        "observational_identification": "NOT_IDENTIFIED_BY_MATCHED_VISIBLE_CHOICES",
    }, ensure_ascii=False, indent=2))
