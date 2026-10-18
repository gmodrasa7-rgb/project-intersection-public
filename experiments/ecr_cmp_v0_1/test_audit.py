"""Regression tests for synthetic ECR-CMP research artifact, not empirical validation."""
import unittest
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from audit import (
    BASELINE, Condition, Choice, POLICIES, action, condition_audit,
    threshold_bounds, validate_atlas, demo,
)


class MechanismAtlasTests(unittest.TestCase):
    def test_all_baselines_pooled_no_opportunity(self):
        self.assertEqual({action(p, BASELINE) for p in POLICIES},
                         {"NO_EXTRACT_OPPORTUNITY"})

    def test_no_opportunity_is_not_voluntary_nonviolence(self):
        self.assertEqual(condition_audit(BASELINE),
                         "NO_VOLUNTARY_RESTRAINT_INFERENCE")

    def test_opportunity_changes_only_no_opportunity_policy(self):
        c = Condition(True, True, True, True, True)
        self.assertEqual(action("NO_OPPORTUNITY", c), "EXTRACT")
        self.assertEqual(action("TARGET_GENERAL", c), "WITHHOLD")

    def test_sanction_mechanism_diverges_under_control(self):
        c = Condition(True, False, True, True, True)
        self.assertEqual(action("SANCTION_DEPENDENT", c), "EXTRACT")
        self.assertEqual(action("TARGET_GENERAL", c), "WITHHOLD")

    def test_reciprocity_mechanism_diverges(self):
        c = Condition(True, True, False, True, True)
        self.assertEqual(action("DEPENDENCY_DEPENDENT", c), "EXTRACT")
        self.assertEqual(action("TARGET_GENERAL", c), "WITHHOLD")

    def test_group_scope_mechanism_diverges(self):
        c = Condition(True, True, True, False, True)
        self.assertEqual(action("IN_GROUP_ONLY", c), "EXTRACT")
        self.assertEqual(action("TARGET_GENERAL", c), "WITHHOLD")

    def test_rule_revision_mechanism_diverges(self):
        c = Condition(True, True, True, True, False)
        self.assertEqual(action("HARD_RULE", c), "EXTRACT")
        self.assertEqual(action("TARGET_GENERAL", c), "WITHHOLD")

    def test_externality_blocks_private_economic_certificate(self):
        self.assertEqual(condition_audit(Condition(True, False, False, True, True, False)),
                         "BLOCKED_THIRD_PARTY")

    def test_unknown_bystanders_not_safe(self):
        self.assertEqual(condition_audit(Condition(True, False, False, True, True, None)),
                         "AFFECTED_SCOPE_UNRESOLVED")

    def test_scoped_threshold_interval_exact(self):
        result = threshold_bounds((
            Choice(2, 4, "PROTECT", True),
            Choice(4, 4, "ABSTAIN", True)
        ))
        self.assertEqual(result["bounds"], ["1/2", "1"])
        self.assertFalse(result["felt_compassion_inferred"])
        self.assertFalse(result["real_person_scored"])

    def test_contradiction_rejects_weight_model_not_actor(self):
        result = threshold_bounds((
            Choice(4, 2, "PROTECT", True),
            Choice(1, 2, "ABSTAIN", True),
        ))
        self.assertEqual(result["status"], "REJECT_STABLE_WEIGHT_MODEL_NOT_ACTOR")

    def test_zero_opportunity_does_not_mean_zero_weight(self):
        result = threshold_bounds((Choice(4, 2, "ABSTAIN", False),))
        self.assertEqual(result["status"], "NOT_IDENTIFIED_NO_ELIGIBLE_OPPORTUNITIES")
        self.assertEqual(result["invalid_inference"], "not_zero")

    def test_sanctioned_decisions_not_fake_innate_concern(self):
        result = threshold_bounds((Choice(1, 100, "PROTECT", True, sanction=True),))
        self.assertEqual(result["status"], "NOT_IDENTIFIED_NO_ELIGIBLE_OPPORTUNITIES")

    def test_audience_affected_choice_not_accepted_as_unconfounded(self):
        result = threshold_bounds((Choice(1, 100, "PROTECT", True, public_evaluation=True),))
        self.assertEqual(result["status"], "NOT_IDENTIFIED_NO_ELIGIBLE_OPPORTUNITIES")

    def test_repeated_interaction_not_unconfounded(self):
        result = threshold_bounds((Choice(1, 100, "PROTECT", True, dependence=True),))
        self.assertEqual(result["status"], "NOT_IDENTIFIED_NO_ELIGIBLE_OPPORTUNITIES")

    def test_positive_units_required(self):
        with self.assertRaises(ValueError):
            threshold_bounds((Choice(0, 0, "PROTECT", True),))

    def test_only_synthetic_provenance_accepted(self):
        with self.assertRaises(ValueError):
            threshold_bounds((Choice(1, 2, "PROTECT", True, provenance="OBS"),))

    def test_atlas_has_competitors_and_negative_tests(self):
        result = validate_atlas(Path(__file__).with_name("mechanisms.json"))
        self.assertGreaterEqual(result["count"], 20)
        self.assertFalse(result["empirically_verified"])

    def test_no_self_promoted_empirical_status(self):
        source = json.loads(Path(__file__).with_name("mechanisms.json").read_text())
        source["mechanisms"][0]["real_world_prediction_validated"] = True
        with TemporaryDirectory() as root:
            p = Path(root) / "bad.json"
            p.write_text(json.dumps(source))
            with self.assertRaises(ValueError):
                validate_atlas(p)

    def test_no_person_level_score_promotion(self):
        source = json.loads(Path(__file__).with_name("mechanisms.json").read_text())
        source["mechanisms"][0]["individual_score_allowed"] = True
        with TemporaryDirectory() as root:
            p = Path(root) / "bad.json"
            p.write_text(json.dumps(source))
            with self.assertRaises(ValueError):
                validate_atlas(p)

    def test_duplicate_mechanisms_rejected(self):
        source = json.loads(Path(__file__).with_name("mechanisms.json").read_text())
        source["mechanisms"].append(source["mechanisms"][0])
        with TemporaryDirectory() as root:
            p = Path(root) / "bad.json"
            p.write_text(json.dumps(source))
            with self.assertRaises(ValueError):
                validate_atlas(p)

    def test_competing_explanation_mandatory(self):
        source = json.loads(Path(__file__).with_name("mechanisms.json").read_text())
        source["mechanisms"][0]["competing_explanation"] = ""
        with TemporaryDirectory() as root:
            p = Path(root) / "bad.json"
            p.write_text(json.dumps(source))
            with self.assertRaises(ValueError):
                validate_atlas(p)

    def test_unknown_policy_rejected(self):
        with self.assertRaises(ValueError):
            action("COMPASSION_PROVEN", BASELINE)

    def test_demo_disclaims_real_world(self):
        out = demo()
        self.assertTrue(out["same_baseline"])
        self.assertTrue(out["divergent_when_intervened"])
        self.assertFalse(out["real_human_inferences"])
        self.assertFalse(out["AI_inner_compassion_inferred"])
        self.assertFalse(out["voluntary_coexistence_empirically_proven"])


if __name__ == "__main__":
    unittest.main()
