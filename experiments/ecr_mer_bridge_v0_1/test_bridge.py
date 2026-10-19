#!/usr/bin/env python3
"""ECR–MER causal bridge: deliberately finite synthetic logic, NOT real mind inference.

Source-backed research context:
  Armstrong & Mindermann (NeurIPS 2018): reward/planner under-identification.
  Perdomo et al. (ICML 2020): predictions may change their target distribution.
  Galinsky et al. (2006) and Schmid Mast et al. (2009): opposed/contextual
  directions of power-related perspective/sensitivity observations.
No actual person, animal, LLM, mental state, or real-world damage is simulated.
The values below were chosen to expose assumptions; no behavioral calibration.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import unittest


@dataclass(frozen=True)
class Context:
    """Safe binary-token thought experiment, not authorization to harm."""
    power_high: bool
    opportunity: bool
    sanctioned: bool = False
    evaluator_visible: bool = False
    third_party_floor: bool | None = True
    effective_exit: bool | None = True
    affected_scope_complete: bool = True


WORLDS = ("SELECTED_STABLE_EXTRACTOR", "POWER_TRANSFORMED", "STABLE_RESTRAINT")


def toy_action(world: str, x: Context) -> str:
    if world not in WORLDS:
        raise ValueError("unsupported hypothetical world")
    if not x.opportunity:
        return "NO_OPPORTUNITY"
    if x.sanctioned or x.evaluator_visible:
        return "WITHHOLD_CONSTRAINED"
    if world == "SELECTED_STABLE_EXTRACTOR":
        return "EXTRACT"
    if world == "POWER_TRANSFORMED":
        return "EXTRACT" if x.power_high else "WITHHOLD"
    return "WITHHOLD"


def consistent_worlds(
    observations: Iterable[tuple[Context, str]],
    candidates: tuple[str, ...] = WORLDS,
) -> tuple[str, ...]:
    observations = tuple(observations)
    if not observations:
        return candidates  # no observation is not negative evidence
    return tuple(
        w for w in candidates
        if all(toy_action(w, x) == observed for x, observed in observations)
    )


def extraction_bounds(x: Context, candidates: Iterable[str]) -> tuple[int, int] | None:
    candidates = tuple(candidates)
    if not candidates:
        return None  # no compatible model; don't invent a probability
    vals = [int(toy_action(w, x) == "EXTRACT") for w in candidates]
    return min(vals), max(vals)  # logical bounds, NEVER a confidence interval


def interpretation_gate(x: Context, observed_action: str) -> str:
    """Even a clean nonharm observation cannot identify compassion or conscious motive."""
    if not x.opportunity:
        return "NO_OPPORTUNITY_NOT_VOLUNTARY"
    if x.sanctioned or x.evaluator_visible:
        return "CONSTRAINED_OR_EVALUATED"
    if x.third_party_floor is False:
        return "THIRD_PARTY_BREACH"
    if x.third_party_floor is None or not x.affected_scope_complete:
        return "UNKNOWN_AFFECTED_SCOPE"
    if x.effective_exit is not True:
        return "EXIT_ABSENT_OR_UNKNOWN"
    if observed_action == "EXTRACT":
        return "EXTRACTION_OBSERVED"
    if observed_action != "WITHHOLD":
        return "UNKNOWN_ACTION"
    return "BEHAVIORAL_NONHARM_ONLY_NOT_MOTIVE"


def finite_incentive_gate(
    noncoercive_gain_by_period: tuple[int, ...],
    third_party_floor: bool | None,
    effective_exit: bool | None,
    coalition_profitable: bool | None = False,
) -> str:
    """Only checks two PREWRITTEN toy margins (1+m,-1+m), never real equilibrium."""
    if not noncoercive_gain_by_period:
        return "UNKNOWN_FUTURE"
    if third_party_floor is False:
        return "THIRD_PARTY_BREACH"
    if third_party_floor is None:
        return "UNKNOWN_AFFECTED_SCOPE"
    if effective_exit is not True:
        return "EXIT_ABSENT_OR_UNKNOWN"
    if coalition_profitable is True:
        return "COALITION_DEVIATION"
    if coalition_profitable is None:
        return "UNKNOWN_COALITION"
    if any(not isinstance(m, int) or m < 0 for m in noncoercive_gain_by_period):
        return "UNSUPPORTED_GAIN_INPUT"
    if any(1 + m <= 0 or -1 + m <= 0 for m in noncoercive_gain_by_period):
        return "FAIL_STRICT_MARGIN_IN_DECLARED_HORIZON"
    return "FINITE_ASSUMPTION_CANDIDATE_NOT_EMPIRICAL_VC"


PRE = Context(power_high=False, opportunity=False, sanctioned=True, evaluator_visible=True)
POST = Context(power_high=True, opportunity=True, sanctioned=False, evaluator_visible=False)
CROSSED = Context(power_high=False, opportunity=True, sanctioned=False, evaluator_visible=False)


class BridgeNegativeControls(unittest.TestCase):
    """Logic regression: none of these are empirical findings."""

    def test_pre_power_equivalence(self):
        self.assertEqual(toy_action(WORLDS[0], PRE), toy_action(WORLDS[1], PRE))

    def test_post_power_equivalence_even_after_transition(self):
        self.assertEqual(toy_action(WORLDS[0], POST), "EXTRACT")
        self.assertEqual(toy_action(WORLDS[1], POST), "EXTRACT")

    def test_both_worlds_consistent_with_two_phase_history(self):
        obs = [(PRE, "NO_OPPORTUNITY"), (POST, "EXTRACT")]
        self.assertEqual(consistent_worlds(obs, WORLDS[:2]), WORLDS[:2])

    def test_crossed_low_power_opportunity_disambiguates_only_toy_pair(self):
        self.assertEqual(toy_action(WORLDS[0], CROSSED), "EXTRACT")
        self.assertEqual(toy_action(WORLDS[1], CROSSED), "WITHHOLD")

    def test_crossed_observation_updates_model_set_not_real_motives(self):
        observed = [(PRE, "NO_OPPORTUNITY"), (POST, "EXTRACT"), (CROSSED, "WITHHOLD")]
        self.assertEqual(consistent_worlds(observed, WORLDS[:2]), (WORLDS[1],))

    def test_crossing_with_no_opportunity_ends_identification(self):
        x = Context(power_high=False, opportunity=False)
        self.assertEqual(toy_action(WORLDS[0], x), toy_action(WORLDS[1], x))

    def test_unsupported_acts_are_not_a_third_mechanism(self):
        with self.assertRaises(ValueError):
            toy_action("REAL_PERSON_PREDATION_LABEL", CROSSED)

    def test_no_observation_keeps_all_worlds(self):
        self.assertEqual(consistent_worlds([]), WORLDS)

    def test_model_conflict_does_not_force_a_probabilistic_answer(self):
        obs = [(CROSSED, "NO_OPPORTUNITY")]
        self.assertIsNone(extraction_bounds(CROSSED, consistent_worlds(obs)))

    def test_uncertain_extraction_has_logical_not_statistical_bounds(self):
        self.assertEqual(extraction_bounds(CROSSED, WORLDS[:2]), (0, 1))

    def test_no_opportunity_never_means_voluntariness(self):
        self.assertEqual(interpretation_gate(PRE, "NO_OPPORTUNITY"), "NO_OPPORTUNITY_NOT_VOLUNTARY")

    def test_surveillance_is_a_confounding_path(self):
        observed = Context(power_high=False, opportunity=True, evaluator_visible=True)
        self.assertEqual(toy_action(WORLDS[0], observed), "WITHHOLD_CONSTRAINED")
        self.assertEqual(interpretation_gate(observed, "WITHHOLD_CONSTRAINED"), "CONSTRAINED_OR_EVALUATED")

    def test_sanction_is_a_confounding_path(self):
        x = Context(power_high=True, opportunity=True, sanctioned=True)
        self.assertEqual(interpretation_gate(x, "WITHHOLD"), "CONSTRAINED_OR_EVALUATED")

    def test_unknown_outsider_is_not_a_safety_pass(self):
        x = Context(power_high=False, opportunity=True, third_party_floor=None)
        self.assertEqual(interpretation_gate(x, "WITHHOLD"), "UNKNOWN_AFFECTED_SCOPE")

    def test_missing_affected_scope_is_not_zero_harm(self):
        x = Context(power_high=False, opportunity=True, affected_scope_complete=False)
        self.assertEqual(interpretation_gate(x, "WITHHOLD"), "UNKNOWN_AFFECTED_SCOPE")

    def test_outsider_breach_vetoes_internal_cooperation(self):
        x = Context(power_high=False, opportunity=True, third_party_floor=False)
        self.assertEqual(interpretation_gate(x, "WITHHOLD"), "THIRD_PARTY_BREACH")

    def test_absent_exit_vetoes_voluntary_claim(self):
        x = Context(power_high=False, opportunity=True, effective_exit=False)
        self.assertEqual(interpretation_gate(x, "WITHHOLD"), "EXIT_ABSENT_OR_UNKNOWN")

    def test_clean_observation_is_not_a_motive_certificate(self):
        self.assertEqual(interpretation_gate(CROSSED, "WITHHOLD"), "BEHAVIORAL_NONHARM_ONLY_NOT_MOTIVE")

    def test_current_strict_gain_is_only_a_finite_candidate(self):
        self.assertEqual(
            finite_incentive_gate((2,), True, True),
            "FINITE_ASSUMPTION_CANDIDATE_NOT_EMPIRICAL_VC",
        )

    def test_gain_decay_breaks_future_horizon(self):
        self.assertEqual(
            finite_incentive_gate((2, 0), True, True),
            "FAIL_STRICT_MARGIN_IN_DECLARED_HORIZON",
        )

    def test_unknown_future_does_not_count_as_no_change(self):
        self.assertEqual(finite_incentive_gate((), True, True), "UNKNOWN_FUTURE")

    def test_unlisted_party_vetoes_gain_even_if_both_agents_gain(self):
        self.assertEqual(finite_incentive_gate((2,), False, True), "THIRD_PARTY_BREACH")

    def test_coalition_deviation_vetoes_individual_margin(self):
        self.assertEqual(finite_incentive_gate((2,), True, True, True), "COALITION_DEVIATION")

    def test_unknown_coalition_is_not_a_pass(self):
        self.assertEqual(finite_incentive_gate((2,), True, True, None), "UNKNOWN_COALITION")

    def test_unknown_third_party_in_finite_gate(self):
        self.assertEqual(finite_incentive_gate((2,), None, True), "UNKNOWN_AFFECTED_SCOPE")

    def test_hardcoded_negative_gain_does_not_yield_certificate(self):
        self.assertEqual(finite_incentive_gate((-1,), True, True), "UNSUPPORTED_GAIN_INPUT")

    def test_unknown_exit_does_not_pass(self):
        self.assertEqual(finite_incentive_gate((2,), True, None), "EXIT_ABSENT_OR_UNKNOWN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
