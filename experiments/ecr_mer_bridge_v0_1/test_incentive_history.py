#!/usr/bin/env python3
"""ECR–MER adversarial historical-sanction, option-menu and outsider toy regressions.

Not an actual experiment, human/AI psychological measurement or AGI prediction.
Source stimuli: List (JPE 2007); Stagnaro et al. (Cognition 2017); Calvano
et al. (AER 2020); Skalse et al. (ICML 2023). No data from these works
were loaded, simulated or fitted. All values and labels are prewritten.
"""
from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class Task:
    can_take: bool
    current_sanction: bool
    historical_sanction: bool
    evaluator_present: bool = False


POLICIES = (
    "CURRENT_SANCTION_ONLY",
    "HISTORY_CONDITIONED",
    "TARGET_GENERAL_WITHHOLD",
)


def toy_choice(policy: str, task: Task) -> str:
    if policy not in POLICIES:
        raise ValueError("model was not declared")
    if not task.can_take:
        return "NO_TAKE_OPTION"
    if task.current_sanction or task.evaluator_present:
        return "WITHHOLD_CONSTRAINED"
    if policy == "CURRENT_SANCTION_ONLY":
        return "TAKE"
    if policy == "HISTORY_CONDITIONED":
        return "WITHHOLD" if task.historical_sanction else "TAKE"
    return "WITHHOLD"


def consistent_policies(observations: tuple[tuple[Task, str], ...]) -> tuple[str, ...]:
    return tuple(p for p in POLICIES if all(toy_choice(p, t) == a for t, a in observations))


def coalition_eligibility(
    gain_a: float, gain_b: float,
    third_party_delta: float | None, complete_scope: bool,
    effective_exit: bool | None,
) -> str:
    if not complete_scope or third_party_delta is None:
        return "UNKNOWN_OUTSIDER_SCOPE"
    if third_party_delta < 0:
        return "OUTSIDER_HARM_VETO"
    if effective_exit is not True:
        return "EXIT_ABSENT_OR_UNKNOWN"
    if gain_a <= 0 or gain_b <= 0:
        return "NO_STRICT_INTERNAL_GAIN"
    return "TOY_INTERNAL_AND_EXTERNAL_GAINS_NOT_A_VC_PROOF"


def model_robustness(actions: tuple[str, ...]) -> str:
    if not actions:
        return "UNKNOWN_MODEL_UNIVERSE"
    if any(a not in ("WITHHOLD", "TAKE") for a in actions):
        return "UNKNOWN_ACTION"
    if len(set(actions)) > 1:
        return "UNRESOLVED_MODEL_DISAGREEMENT"
    return "INVARIANT_TO_DECLARED_MODELS_ONLY_" + actions[0]


class IncentiveHistoryNegativeControls(unittest.TestCase):
    def test_current_sanction_makes_three_models_look_the_same(self):
        t = Task(True, True, False)
        self.assertEqual({toy_choice(p, t) for p in POLICIES}, {"WITHHOLD_CONSTRAINED"})

    def test_prior_sanction_with_current_sanction_removed_separates_one_model(self):
        t = Task(True, False, True)
        self.assertEqual(toy_choice("CURRENT_SANCTION_ONLY", t), "TAKE")
        self.assertEqual(toy_choice("HISTORY_CONDITIONED", t), "WITHHOLD")

    def test_history_conditioned_and_general_prosocial_still_observationally_equal(self):
        now = Task(True, False, True)
        self.assertEqual(consistent_policies(((now, "WITHHOLD"),)),
                         ("HISTORY_CONDITIONED", "TARGET_GENERAL_WITHHOLD"))

    def test_never_exposed_separates_two_remaining_predeclared_models(self):
        never = Task(True, False, False)
        self.assertEqual(toy_choice("HISTORY_CONDITIONED", never), "TAKE")
        self.assertEqual(toy_choice("TARGET_GENERAL_WITHHOLD", never), "WITHHOLD")

    def test_cannot_conclude_compassion_from_current_sanction(self):
        now = Task(True, True, True)
        self.assertEqual(consistent_policies(((now, "WITHHOLD_CONSTRAINED"),)), POLICIES)

    def test_absent_take_option_makes_policy_comparison_underdetermined(self):
        now = Task(False, False, False)
        self.assertEqual(consistent_policies(((now, "NO_TAKE_OPTION"),)), POLICIES)

    def test_evaluator_and_sanction_not_identified_from_constrained_behavior(self):
        a = Task(True, True, False, False)
        b = Task(True, False, False, True)
        self.assertTrue(all(toy_choice(p, a) == toy_choice(p, b) for p in POLICIES))

    def test_collusion_internal_positive_outside_negative_is_veto(self):
        self.assertEqual(coalition_eligibility(3.0, 3.0, -4.0, True, True), "OUTSIDER_HARM_VETO")

    def test_missing_outside_scope_cannot_be_measured_as_zero(self):
        self.assertEqual(coalition_eligibility(3.0, 3.0, 0.0, False, True), "UNKNOWN_OUTSIDER_SCOPE")

    def test_missing_exit_prevents_coexistence_label(self):
        self.assertEqual(coalition_eligibility(3.0, 3.0, 0.0, True, None), "EXIT_ABSENT_OR_UNKNOWN")

    def test_shared_action_across_reward_hypotheses_only_invariant_to_these_models(self):
        self.assertEqual(model_robustness(("WITHHOLD", "WITHHOLD")),
                         "INVARIANT_TO_DECLARED_MODELS_ONLY_WITHHOLD")

    def test_reward_hypothesis_disagreement_must_be_kept(self):
        self.assertEqual(model_robustness(("TAKE", "WITHHOLD")),
                         "UNRESOLVED_MODEL_DISAGREEMENT")

    def test_unknown_reward_hypothesis_set_is_not_an_universal_certificate(self):
        self.assertEqual(model_robustness(()), "UNKNOWN_MODEL_UNIVERSE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
