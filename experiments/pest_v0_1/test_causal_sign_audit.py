"""Negative controls for simulated opposite-sign causal effects and post-event role leakage."""
import unittest
from fractions import Fraction

from causal_sign_audit import (
    WorldUnit, TemporalRole, world, inspect, binary_ate_bounds_from_observations,
    observational_equivalence_certificate, role_time_audit, audit
)


class CausalSignAuditTests(unittest.TestCase):
    def test_observed_full_support_joint_distribution_identical(self):
        a=inspect(world("HARM_INCREASES"))
        b=inspect(world("HARM_DECREASES"))
        self.assertEqual(a["observed_joint"],b["observed_joint"])
        self.assertEqual(a["observed_joint"], {
            "T0_Y0":"1/4","T0_Y1":"1/4","T1_Y0":"1/4","T1_Y1":"1/4"
        })

    def test_exact_opposite_causal_sign_in_same_observational_data(self):
        a=inspect(world("HARM_INCREASES"))
        b=inspect(world("HARM_DECREASES"))
        self.assertEqual(a["average_causal_effect"],"1/2")
        self.assertEqual(b["average_causal_effect"],"-1/2")
        self.assertEqual(a["P_harm_if_all_transition"],"3/4")
        self.assertEqual(a["P_harm_if_none_transition"],"1/4")
        self.assertEqual(b["P_harm_if_all_transition"],"1/4")
        self.assertEqual(b["P_harm_if_none_transition"],"3/4")

    def test_effect_difference_is_causal_not_observed_correlation(self):
        a=inspect(world("HARM_INCREASES"))
        observed=a["observed_joint"]
        # The observed Y rate is exactly 1/2 for each transition state.
        for treatment in (0,1):
            p_zero=Fraction(observed[f"T{treatment}_Y0"])
            p_one=Fraction(observed[f"T{treatment}_Y1"])
            self.assertEqual(p_one/(p_zero+p_one),Fraction(1,2))

    def test_sharp_binary_potential_outcome_bounds_straddle_zero(self):
        x=binary_ate_bounds_from_observations(world("HARM_INCREASES"))
        y=binary_ate_bounds_from_observations(world("HARM_DECREASES"))
        self.assertEqual(x,y)
        self.assertEqual(x["sharp_ATE_lower"],"-1/2")
        self.assertEqual(x["sharp_ATE_upper"],"1/2")
        self.assertFalse(x["sign_identified"])
        self.assertFalse(x["real_world_AI_transition_interference_and_treatment_definition_verified"])

    def test_bounds_flag_systemic_transition_not_experiment(self):
        x=observational_equivalence_certificate()
        self.assertEqual(x["sharp_binary_effect_bounds"]["sharp_ATE_lower"],"-1/2")
        self.assertEqual(x["sharp_binary_effect_bounds"]["sharp_ATE_upper"],"1/2")
        self.assertEqual(x["sharp_binary_effect_bounds"]["real_world_applicability"],"NOT_ESTABLISHED")

    def test_certificate_never_claims_real_A(self):
        x=observational_equivalence_certificate()
        self.assertTrue(x["same_observed_distribution"])
        self.assertTrue(x["opposite_causal_effects"])
        self.assertFalse(x["observations_sufficient_for_sign"])
        self.assertFalse(x["data_are_actual_A_or_human_harm_observations"])

    def test_shuffling_latent_strata_does_not_change_effect(self):
        for label in ("HARM_INCREASES","HARM_DECREASES"):
            units=world(label)
            self.assertEqual(inspect(units), inspect(tuple(reversed(units))))

    def test_counterfactuals_not_assumed_known_from_observations(self):
        x=world("HARM_INCREASES")
        y=world("HARM_DECREASES")
        self.assertEqual(tuple((r.observed_transition,
             r.human_harm_if_transition if r.observed_transition
             else r.human_harm_if_no_transition) for r in x),
             tuple((r.observed_transition,
             r.human_harm_if_transition if r.observed_transition
             else r.human_harm_if_no_transition) for r in y))
        self.assertNotEqual(x,y)

    def test_negative_control_invalid_world_rejected(self):
        with self.assertRaises(ValueError):
            world("HARM_UNKNOWN")
        with self.assertRaises(ValueError):
            inspect(())
        with self.assertRaises(ValueError):
            inspect((WorldUnit("x",0,0,0),WorldUnit("x",1,1,1)))
        with self.assertRaises(ValueError):
            inspect((WorldUnit("x",0,0,2),))
        with self.assertRaises(ValueError):
            inspect((WorldUnit("x",True,0,1),))

    def test_new_N_is_post_event_label_not_baseline_predictor(self):
        x=role_time_audit((
            TemporalRole("PER001",frozenset({"G","P"}),frozenset({"N","Q"})),
            TemporalRole("PER002",frozenset({"E","O"}),frozenset({"E","O"}))
        ),("N","Q"))
        self.assertTrue(x["adjustment_contaminated_by_post_event_role"])
        self.assertEqual(x["potentially_post_event_adjustment_roles"],["N","Q"])
        self.assertEqual(x["N_newly_acquired_after_transition"],["PER001"])
        self.assertFalse(x["causal_estimate_identified"])

    def test_baseline_G_P_not_contaminated_by_changes(self):
        x=role_time_audit((
            TemporalRole("PER001",frozenset({"G","P"}),frozenset({"N","Q"})),
        ),("G","P"))
        self.assertFalse(x["adjustment_contaminated_by_post_event_role"])
        self.assertEqual(x["tracked_entity_count"],1)
        self.assertFalse(x["causal_estimate_identified"])

    def test_same_person_after_transition_never_counts_as_new_person(self):
        x=role_time_audit((
            TemporalRole("PER001",frozenset({"G","P"}),frozenset({"N","Q"})),
        ),("N",))
        self.assertTrue(x["person_or_entity_ID_preserved_across_time"])
        self.assertEqual(list(x["roles_acquired_after_transition_by_entity"]),["PER001"])

    def test_new_role_leakage_not_independent_causal_proof(self):
        x=role_time_audit((
            TemporalRole("PER001",frozenset({"G"}),frozenset({"N"})),
        ),("N",))
        self.assertFalse(x["post_treatment_selection_proves_transition_caused_layoff"])

    def test_missing_person_or_duplicate_identity_rejected(self):
        with self.assertRaises(ValueError):
            role_time_audit((),("N",))
        with self.assertRaises(ValueError):
            role_time_audit((
                TemporalRole("P",frozenset({"G"}),frozenset({"N"})),
                TemporalRole("P",frozenset({"G"}),frozenset({"N"})),
            ),("N",))
        with self.assertRaises(ValueError):
            role_time_audit((
                TemporalRole("",frozenset({"G"}),frozenset({"N"})),
            ),("N",))

    def test_unsafe_adjustment_types_rejected(self):
        with self.assertRaises(ValueError):
            role_time_audit((TemporalRole("P",set({"G"}),frozenset({"N"})),),("N",))
        with self.assertRaises(ValueError):
            role_time_audit((TemporalRole("P",frozenset({"G"}),frozenset({"N"})),),("N","N"))
        with self.assertRaises(ValueError):
            role_time_audit((TemporalRole("P",frozenset({"G"}),frozenset({"N"})),),(1,))

    def test_provenance_status_preserved(self):
        x=audit()
        self.assertEqual(x["certificate"]["status"],
                         "EXACT_CONSTRUCTIVE_NONIDENTIFIABILITY_CERTIFICATE")
        self.assertEqual(x["post_treatment_label_example"]["N_newly_acquired_after_transition"],["PER001"])
        self.assertIn("No new social actor role is required by this certificate",x["research_holds"])


if __name__=="__main__":
    unittest.main()
