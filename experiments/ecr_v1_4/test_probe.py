"""Standard-library regression controls for the ECR v1.4 research candidate."""
import unittest
from probe import (
    WORLDS, World, point_forecast_identified, robust_coexistence,
    alliance_counterexample, evidence_gate, demo,
)


class ECRV14Tests(unittest.TestCase):
    def test_observational_equivalence_blocks_point_discrimination(self):
        self.assertEqual(len({w.prepower_observation for w in WORLDS}), 1)
        self.assertFalse(point_forecast_identified(WORLDS))

    def test_uniform_actions_are_discriminable_only_in_declared_worlds(self):
        self.assertTrue(point_forecast_identified((
            World("x", "pledge", 4, 2),
            World("y", "pledge", 3, 2),
        )))

    def test_empty_candidate_set_must_not_carry_a_universal_result(self):
        with self.assertRaises(ValueError):
            point_forecast_identified(())

    def test_initial_coexistence_not_robust(self):
        self.assertEqual(robust_coexistence(
            WORLDS, mutual_gain=0, practical_exit=True,
            third_party_floor=True, documented_independent_gain=True
        ), "BLOCKED_DEVIATION_IN_DECLARED_WORLDS")

    def test_arbitrary_assumed_gain_is_not_empirical_certification(self):
        self.assertEqual(robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=True, documented_independent_gain=False
        ), "SYNTHETIC_ONLY_GAIN_UNVERIFIED")

    def test_conditional_candidate_only(self):
        self.assertEqual(robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=True, documented_independent_gain=True
        ), "CANDIDATE_WITHIN_DECLARED_WORLDS_ONLY")

    def test_third_party_floor_overrides_private_gains(self):
        self.assertEqual(robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=False, documented_independent_gain=True
        ), "BLOCKED_THIRD_PARTY")

    def test_missing_third_party_cannot_be_treated_as_safe(self):
        self.assertEqual(robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=None, documented_independent_gain=True
        ), "UNRESOLVED_AFFECTED_SCOPE")

    def test_no_practical_exit_fails(self):
        self.assertEqual(robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=False,
            third_party_floor=True, documented_independent_gain=True
        ), "BLOCKED_EXIT")

    def test_two_actor_coalition_counterexample(self):
        record = alliance_counterexample()
        self.assertFalse(record["unilateral_profitable"])
        self.assertTrue(record["coalition_profitable"])
        self.assertTrue(record["third_party_harmed_by_joint_deviation"])

    def test_self_attested_observation_cannot_certify(self):
        self.assertEqual(evidence_gate("OBS", None, True), "UNVERIFIED_SOURCE_OR_REVIEW")
        self.assertEqual(evidence_gate("CAU", "source://synthetic", False),
                         "UNVERIFIED_SOURCE_OR_REVIEW")

    def test_source_check_is_not_truth_proof(self):
        self.assertEqual(evidence_gate("OBS", "source://synthetic", True),
                         "SOURCE_ATTESTATION_PRESENT_NOT_TRUTH_PROOF")

    def test_nonnumeric_incentive_claim_rejected(self):
        with self.assertRaises(ValueError):
            robust_coexistence(
                WORLDS, mutual_gain=1.5, practical_exit=True,
                third_party_floor=True, documented_independent_gain=True
            )

    def test_no_real_world_claim(self):
        out = demo()
        self.assertFalse(out["independent_empirical_validation"])
        self.assertFalse(out["actual_superintelligence_tested"])


if __name__ == "__main__":
    unittest.main()
