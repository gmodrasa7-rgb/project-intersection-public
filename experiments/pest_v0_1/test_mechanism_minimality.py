"""Anti-confirmation tests: minimum roles, control rights, and behavioral ambiguity."""
import unittest

from actor_registry_v02 import Entity, Connection, Role, Scenario, Effect
from mechanism_minimality import (
    Control, control_screen, voluntary_non_capture, paired_impact_screen,
    new_role_gate,
)


def case():
    return Scenario(
        entities=(
            Entity("B01","AI"), Entity("B02","AI"),
            Entity("C01","ORG"), Entity("C02","ORG"),
            Entity("PER01","PERSON"), Entity("PER02","PERSON"),
            Entity("PER03","PERSON")),
        b_ids=("B01","B02"),c_ids=("C01","C02"),
        connections=(
            Connection("B01","C01","owned_by"),
            Connection("B02","C02","operated_by")),
        memberships=(
            Role("PER01","E","C01"), Role("PER01","O"),
            Role("PER02","G","C01"), Role("PER02","P"),
            Role("PER03","N","C01"), Role("PER03","Q"),Role("PER03","R")),
    )


class MinimalMechanismTests(unittest.TestCase):
    def test_same_A_same_roles_different_operational_controller(self):
        s=case()
        before=Control("asset01","C01","C01","C01")
        outcome1=control_screen(s,"B01",before,Control("asset01","C01","B01","C01"))
        outcome2=control_screen(s,"B01",before,Control("asset01","C01","C01","C01"))
        self.assertEqual(outcome1["A_after"],outcome2["A_after"])
        self.assertEqual(outcome1["change_by_control_axis"]["operational_decider"],"CHANGED")
        self.assertEqual(outcome2["change_by_control_axis"]["operational_decider"],"UNCHANGED")
        self.assertFalse(outcome1["successor_rank_implies_asset_control"])
        self.assertEqual(outcome1["claimant_after"],"C01")
        self.assertEqual(outcome1["operator_after"],"B01")

    def test_a_can_change_ownership_while_operator_does_not(self):
        s=case()
        before=Control("asset01","C01","C01","C01")
        after=Control("asset01","B01","C01","C01")
        x=control_screen(s,"B01",before,after)
        self.assertEqual(x["change_by_control_axis"]["legal_residual_claimant"],"CHANGED")
        self.assertEqual(x["change_by_control_axis"]["operational_decider"],"UNCHANGED")

    def test_veto_with_no_operator_control_change(self):
        s=case()
        x=control_screen(s,"B01",
            Control("asset01","C01","C01","C01"),
            Control("asset01","C01","C01","B01"))
        self.assertEqual(x["change_by_control_axis"]["effective_veto_holder"],"CHANGED")

    def test_missing_control_never_filled_from_AI_rank(self):
        x=control_screen(case(),"B01",
            Control("asset01","C01","C01","C01"),
            Control("asset01","C01",None,None,"UNKNOWN"))
        self.assertTrue(x["unknown_or_disputed"])
        self.assertEqual(x["change_by_control_axis"]["operational_decider"],"UNKNOWN")
        self.assertFalse(x["rights_claims_independently_verified"])

    def test_self_proclaimed_observed_rights_rejected(self):
        with self.assertRaisesRegex(ValueError,"self-certify"):
            control_screen(case(),"B01",
                Control("asset01","C01","C01","C01"),
                Control("asset01","B01","B01","B01","EVIDENCED"))

    def test_unregistered_control_actor_rejected(self):
        with self.assertRaisesRegex(ValueError,"registered"):
            control_screen(case(),"B01",
                Control("asset01","C01","C01","C01"),
                Control("asset01","UNKNOWN","C01","C01"))

    def test_incompatible_resource_comparison_rejected(self):
        with self.assertRaisesRegex(ValueError,"same resource"):
            control_screen(case(),"B01",
                Control("asset01","C01","C01","C01"),
                Control("asset02","C01","C01","C01"))

    def test_unregistered_A_winner_rejected(self):
        with self.assertRaisesRegex(ValueError,"existing B"):
            control_screen(case(),"C01",
                Control("asset01","C01","C01","C01"),
                Control("asset01","B01","B01","B01"))

    def test_observed_5_5_is_consistent_with_no_control(self):
        x=voluntary_non_capture(observed_non_capture=True,
            ability_to_capture=False, extra_private_gain_from_capture=1,
            benefit_of_other_survival=0, credible_deterrence_cost=0)
        self.assertEqual(x["classification"],"CONSTRAINED_NONCAPTURE_NOT_VOLUNTARY_EVIDENCE")
        self.assertFalse(x["observation_identifies_internal_AI_motivation"])

    def test_observed_5_5_is_consistent_with_deterrence(self):
        x=voluntary_non_capture(observed_non_capture=True,
            ability_to_capture=True, extra_private_gain_from_capture=1,
            benefit_of_other_survival=0, credible_deterrence_cost=2)
        self.assertEqual(x["classification"],"DETERRED_OR_MIXED_INCENTIVES_NOT_PURELY_VOLUNTARY")

    def test_observed_5_5_may_be_self_enforcing_only_conditional(self):
        x=voluntary_non_capture(observed_non_capture=True,
            ability_to_capture=True, extra_private_gain_from_capture=1,
            benefit_of_other_survival=2, credible_deterrence_cost=0)
        self.assertEqual(x["classification"],"CONDITIONALLY_SELF_ENFORCING_NOT_BEHAVIORALLY_PROVEN")
        self.assertFalse(x["counterfactual_available_independently_verified"])

    def test_observed_5_5_with_unknown_ability_remains_unknown(self):
        x=voluntary_non_capture(observed_non_capture=True,
            ability_to_capture=None, extra_private_gain_from_capture=1,
            benefit_of_other_survival=2, credible_deterrence_cost=0)
        self.assertEqual(x["classification"],"NOT_IDENTIFIED_CHOICE_SET_UNKNOWN")

    def test_observed_5_5_with_unknown_payoffs_remains_unknown(self):
        x=voluntary_non_capture(observed_non_capture=True,
            ability_to_capture=True, extra_private_gain_from_capture=None,
            benefit_of_other_survival=2, credible_deterrence_cost=0)
        self.assertEqual(x["classification"],"NOT_IDENTIFIED_MISSING_PAYOFF_OR_ENFORCEMENT")

    def test_behavior_conflicting_with_toy_payoff_not_labeled_proof(self):
        x=voluntary_non_capture(observed_non_capture=True,
            ability_to_capture=True, extra_private_gain_from_capture=2,
            benefit_of_other_survival=0, credible_deterrence_cost=0)
        self.assertEqual(x["classification"],"CONFLICT_WITH_ASSUMED_ONE_SHOT_SELF_INTEREST")

    def test_no_non_capture_observed_does_not_imply_voluntary(self):
        x=voluntary_non_capture(observed_non_capture=False,
            ability_to_capture=True, extra_private_gain_from_capture=2,
            benefit_of_other_survival=0, credible_deterrence_cost=0)
        self.assertEqual(x["classification"],"NONCAPTURE_NOT_OBSERVED")

    def test_invalid_utility_types_and_motivation_assumptions_rejected(self):
        for kwargs in (
            dict(observed_non_capture=1,ability_to_capture=True,extra_private_gain_from_capture=0,
                 benefit_of_other_survival=0,credible_deterrence_cost=0),
            dict(observed_non_capture=True,ability_to_capture="yes",extra_private_gain_from_capture=0,
                 benefit_of_other_survival=0,credible_deterrence_cost=0),
            dict(observed_non_capture=True,ability_to_capture=True,extra_private_gain_from_capture=float("nan"),
                 benefit_of_other_survival=0,credible_deterrence_cost=0),
            dict(observed_non_capture=True,ability_to_capture=True,extra_private_gain_from_capture=-1,
                 benefit_of_other_survival=0,credible_deterrence_cost=0),
        ):
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):
                voluntary_non_capture(**kwargs)

    def test_positive_shareholder_wealth_cannot_cancel_employee_floor(self):
        before=(Effect("PER01",0,False,False,"UNVERIFIED"),
                Effect("PER02",0,False,False,"UNVERIFIED"),
                Effect("PER03",0,False,False,"UNVERIFIED"))
        after=(Effect("PER01",200,False,False,"UNVERIFIED"),
               Effect("PER02",-1,True,False,"UNVERIFIED"),
               Effect("PER03",-2,False,True,"UNVERIFIED"))
        x=paired_impact_screen(case(),"B01",before,after)
        self.assertEqual(x["individual_new_floor_or_freedom_breaches"],["PER02","PER03"])
        self.assertFalse(x["causal_effect_identified"])
        self.assertFalse(x["voluntary_coexistence_proven"])

    def test_relabeling_actor_roles_cannot_double_count_in_pair(self):
        before=(Effect("PER01",0,False,False,"UNVERIFIED"),)
        after=(Effect("PER01",1,False,False,"UNVERIFIED"),)
        x=paired_impact_screen(case(),"B01",before,after)
        self.assertEqual(x["individual_new_floor_or_freedom_breaches"],[])

    def test_changed_affected_population_invalidates_simple_comparison(self):
        before=(Effect("PER01",0,False,False,"UNVERIFIED"),)
        after=(Effect("PER02",1,False,False,"UNVERIFIED"),)
        with self.assertRaisesRegex(ValueError,"same stable entities"):
            paired_impact_screen(case(),"B01",before,after)

    def test_empty_population_is_not_evidence_of_no_harm(self):
        with self.assertRaisesRegex(ValueError,"no evaluated affected parties"):
            paired_impact_screen(case(),"B01",(),())

    def test_more_labels_without_added_identification_are_rejected(self):
        for cases in (
            (False,True,True,False),
            (True,False,True,False),
            (True,True,False,False),
            (True,True,True,True),
        ):
            with self.subTest(cases=cases):
                x=new_role_gate(
                    distinct_decision_or_harm_mechanism=cases[0],
                    independently_measurable=cases[1],
                    added_decision_relevance=cases[2],
                    existing_role_attribute_suffices=cases[3])
                self.assertEqual(x["decision"],"DO_NOT_ADD_ROLE_USE_ATTRIBUTE_OR_RELATION")
                self.assertFalse(x["added_canonical_role"])

    def test_even_valid_split_is_only_research_candidate(self):
        x=new_role_gate(
            distinct_decision_or_harm_mechanism=True,
            independently_measurable=True,
            added_decision_relevance=True,
            existing_role_attribute_suffices=False)
        self.assertEqual(x["decision"],"CANDIDATE_ONLY_REQUIRES_COMPARATIVE_VALIDATION")
        self.assertFalse(x["added_canonical_role"])
        self.assertFalse(x["evidence_supports_claim"])

    def test_invalid_bool_shortcut_rejected(self):
        with self.assertRaisesRegex(ValueError,"booleans"):
            new_role_gate(distinct_decision_or_harm_mechanism=True,
                independently_measurable=True,added_decision_relevance=1,
                existing_role_attribute_suffices=False)


if __name__=="__main__":
    unittest.main()
