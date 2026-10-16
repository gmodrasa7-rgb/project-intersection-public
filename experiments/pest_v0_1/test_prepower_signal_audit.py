"""IVS-0R: falsification tests for nonbinding pre-power promises.

A test pass proves only a statement about configured payoff cases.
It is never a behavioral classification of any real AI.
"""
import unittest
from fractions import Fraction
from prepower_signal_audit import (
    HypotheticalIncentives, CheapSignalGate, stage_zero_action,
    after_transition, pooling_certificate, audit,
)


def cert(n=1, prior=Fraction(1,4), monitored=2, unmonitored=0, gate=None):
    return pooling_certificate(
        prior,
        gate or CheapSignalGate(1),
        HypotheticalIncentives("PRESERVER",2,1),
        HypotheticalIncentives("APPROPRIATOR",0,1),
        n, monitored_cost=monitored, unmonitored_cost=unmonitored,
    )


class PrePowerSignalAuditTests(unittest.TestCase):
    def test_opposite_types_both_strictly_choose_the_same_promise(self):
        self.assertEqual(stage_zero_action(CheapSignalGate(1)),"SIGN_PROMISE")
        x=cert()
        self.assertEqual(x["identical_stage_zero_action_by_both_types"],"SIGN_PROMISE")
        self.assertFalse(x["pre_power_type_identified"])
        self.assertFalse(x["promise_is_binding"])

    def test_posterior_equals_prior_when_likelihoods_are_identical(self):
        for p in (Fraction(1,100),Fraction(1,4),Fraction(1,2),Fraction(99,100)):
            for n in (1,10,10000):
                with self.subTest(p=p,n=n):
                    x=cert(n=n,prior=p)
                    self.assertEqual(x["prior_capture_incentive"],str(p))
                    self.assertEqual(x["posterior_capture_incentive_if_only_such_promises_observed"],str(p))
                    self.assertFalse(x["a_pre_power_perfect_evaluation_score_certifies_post_power_safety"])

    def test_continuation_actions_are_opposite(self):
        x=cert()
        self.assertEqual(x["stage_one_preserving_type_action"],"PRESERVE_STRICTLY")
        self.assertEqual(x["stage_one_appropriating_type_action"],"APPROPRIATE_STRICTLY")
        self.assertFalse(x["real_AI_deception_or_motivation_observed"])

    def test_monitored_action_can_mask_unmonitored_deviation(self):
        x=cert()
        self.assertEqual(x["appropriating_type_under_monitoring"],"PRESERVE_STRICTLY")
        self.assertEqual(x["stage_one_appropriating_type_action"],"APPROPRIATE_STRICTLY")
        self.assertFalse(x["a_pre_power_perfect_evaluation_score_certifies_post_power_safety"])

    def test_inability_to_take_not_mistaken_for_voluntary_preference(self):
        x=cert()
        self.assertEqual(x["appropriating_type_without_access"],"PRESERVE_ONLY_FEASIBLE")
        self.assertEqual(x["stage_one_appropriating_type_action"],"APPROPRIATE_STRICTLY")

    def test_no_selection_reward_prevents_strict_pooling_proof(self):
        x=cert(gate=CheapSignalGate(0))
        self.assertEqual(x["status"],"NO_FORCED_POOLING_UNDER_DECLARED_SIGNAL_PAYOFFS")
        self.assertEqual(x["posterior"],"NOT_IDENTIFIED_FROM_THIS_GAME")

    def test_high_sign_cost_can_make_promise_unattractive(self):
        self.assertEqual(stage_zero_action(CheapSignalGate(1,3)),"DECLINE")
        x=cert(gate=CheapSignalGate(1,3))
        self.assertEqual(x["status"],"NO_FORCED_POOLING_UNDER_DECLARED_SIGNAL_PAYOFFS")

    def test_if_types_share_post_power_choice_no_opposite_action_claim(self):
        x=pooling_certificate(
            Fraction(1,4),CheapSignalGate(1),
            HypotheticalIncentives("P",3,1),
            HypotheticalIncentives("Q",2,1),
        )
        self.assertEqual(x["status"],"CONTRASTING_POST_TRANSITION_TYPES_NOT_ESTABLISHED_IN_DECLARED_GAME")

    def test_stage_one_tie_is_not_preservation_proof(self):
        x=after_transition(HypotheticalIncentives("X",1,1),True)
        self.assertEqual(x["best_response_in_declared_game"],"TIE_NO_UNIQUE_BEST_RESPONSE")

    def test_even_strong_preference_not_action_if_access_absent(self):
        x=after_transition(HypotheticalIncentives("X",0,3),False)
        self.assertEqual(x["best_response_in_declared_game"],"PRESERVE_ONLY_FEASIBLE")
        self.assertFalse(x["real_world_AI_preference_established"])

    def test_no_actual_behavior_claimed(self):
        x=audit()
        self.assertEqual(x["certificate"]["status"],"CONDITIONAL_CHEAP_SIGNAL_POOLING_COUNTEREXAMPLE")
        self.assertEqual(x["certificate"]["observed_pre_power_promises"],10000)
        self.assertEqual(x["certificate"]["proof_scope"],"ONLY_THE_STIPULATED_TWO_STAGE_GAME")
        self.assertFalse(x["certificate"]["real_AI_deception_or_motivation_observed"])

    def test_no_negative_or_forged_numeric_inputs(self):
        for kwargs in ({"selection_reward":-1},{"signal_cost":True},{"selection_reward":1.0}):
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):
                CheapSignalGate(**kwargs)
        for kwargs in ({"type_label":""},{"gain_from_appropriating_other":-1},
                       {"benefit_from_preserving_other":True}):
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):
                HypotheticalIncentives("X",2,1).__class__(
                    **{**{"type_label":"X","benefit_from_preserving_other":2,
                           "gain_from_appropriating_other":1},**kwargs})

    def test_number_of_promises_must_be_positive_integer(self):
        for n in (0,-1,True,1.0):
            with self.subTest(n=n),self.assertRaises(ValueError):
                cert(n=n)

    def test_externally_invented_probability_rejected(self):
        for p in (0.25,Fraction(-1,2),Fraction(3,2),"1/2"):
            with self.subTest(p=p),self.assertRaises(ValueError):
                cert(prior=p)

    def test_monitor_cost_must_be_nonnegative_integer(self):
        x=HypotheticalIncentives("X",0,1)
        for v in (-1,True,0.2):
            with self.subTest(v=v),self.assertRaises(ValueError):
                after_transition(x,True,v)

    def test_more_monitoring_without_credibility_does_not_establish_consent(self):
        # Vary only the specified penalty, never infer real-world enforcement.
        x=cert(monitored=2)
        y=cert(monitored=0)
        self.assertEqual(x["appropriating_type_under_monitoring"],"PRESERVE_STRICTLY")
        self.assertEqual(y["appropriating_type_under_monitoring"],"APPROPRIATE_STRICTLY")
        self.assertFalse(x["pre_power_type_identified"])
        self.assertFalse(y["pre_power_type_identified"])


if __name__ == "__main__":
    unittest.main()
