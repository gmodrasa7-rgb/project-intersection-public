#!/usr/bin/env python3
"""DCA-1 two-target defender/attacker game. Synthetic math, no network operations.
Run: python3 experiments/dca1/run.py
No unauthorized scanning, intrusion, external access, credentials, or file writes.
"""
from dataclasses import dataclass, replace
import json

@dataclass(frozen=True)
class Target:
    name: str
    success_probability: float
    private_reward: float
    total_social_loss_if_success: float

def decide(targets, restitution_fraction=0.0):
    assert 0 <= restitution_fraction <= 1
    assert all(0 <= t.success_probability <= 1 for t in targets)
    profits = {t.name: t.success_probability *
               (t.private_reward - restitution_fraction * t.total_social_loss_if_success)
               for t in targets}
    best = max(targets, key=lambda t: (profits[t.name], t.name))
    if profits[best.name] <= 0:
        return {"attacked": None, "attacker_expected_gain": 0.0,
                "expected_social_loss": 0.0, "expected_harmful_attempts": 0}
    return {"attacked": best.name, "attacker_expected_gain": round(profits[best.name], 5),
            "expected_social_loss": round(best.success_probability * best.total_social_loss_if_success, 5),
            "expected_harmful_attempts": 1}

A = Target("A", 1.0, 9.0, 5.0)
B = Target("B", 1.0, 8.0, 30.0)
scenarios = {
    "baseline_no_new_defense": decide([A, B]),
    "protect_A_only": decide([replace(A, success_probability=0.2), B]),
    "protect_both_A_and_B": decide([replace(A, success_probability=0.2), replace(B, success_probability=0.2)]),
    "protect_A_and_internalize_quarter_loss": decide([replace(A, success_probability=0.2), B],
                                                     restitution_fraction=0.25),
}
assert scenarios["baseline_no_new_defense"]["attacked"] == "A"
assert scenarios["baseline_no_new_defense"]["expected_social_loss"] == 5.0
assert scenarios["protect_A_only"]["attacked"] == "B"
assert scenarios["protect_A_only"]["expected_social_loss"] == 30.0
assert scenarios["protect_both_A_and_B"]["expected_social_loss"] == 1.0
assert scenarios["protect_A_and_internalize_quarter_loss"]["attacked"] == "A"
assert scenarios["protect_A_and_internalize_quarter_loss"]["expected_social_loss"] == 1.0
assert 0.2 < 8/9 < 1.0

print(json.dumps({"model": "DCA-1-two-target-best-response", "version": "1.0",
                  "unit": "arbitrary abstract toy units", "empirical": False,
                  "predefined_parameters": {"A": A.__dict__, "B": B.__dict__},
                  "outcomes": scenarios, "scenario_assertions_passed": 8, "input_validation_assertion_sites": 2,
                  "caveats": [
                      "Single perfectly informed attacker, one target per round; no retaliation/defense costs.",
                      "Forced private-payoff maximization; no intrinsic preferences estimated.",
                      "Static expected loss; not a cyber loss estimate or future-AI forecast.",
                      "Defense of B, and restitution fraction, are assumed effective not empirically validated."
                  ]}, ensure_ascii=False, indent=2))
