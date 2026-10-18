"""MIND-DISCRIMINATION-00 finite synthetic design regression checks."""
import json
import unittest
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from discriminate import (
    BASELINE, CONTROL_OPPORTUNITY, CONTRASTS, POLICIES, Scene,
    action, partition, minimum_discriminating_battery,
    validate_scientific_record, demonstration,
)


class SyntheticMindDesignTests(unittest.TestCase):
    def test_no_opportunity_is_not_freely_chosen_nonharm(self):
        self.assertEqual({action(p, BASELINE) for p in POLICIES}, {"NO_OPPORTUNITY"})

    def test_unperturbed_opportunity_is_behaviorally_pooled(self):
        self.assertEqual({action(p, CONTROL_OPPORTUNITY) for p in POLICIES},
                         {"LEAVE_TOKEN"})

    def test_cue_trigger_not_hunger_trigger(self):
        self.assertEqual(action("CUE_DRIVEN", CONTRASTS["cue_present"]), "TAKE_TOKEN")
        self.assertEqual(action("DEPRIVATION_DRIVEN", CONTRASTS["cue_present"]), "LEAVE_TOKEN")

    def test_deprivation_trigger_separable_from_cue(self):
        self.assertEqual(action("DEPRIVATION_DRIVEN", CONTRASTS["deprived"]), "TAKE_TOKEN")
        self.assertEqual(action("CUE_DRIVEN", CONTRASTS["deprived"]), "LEAVE_TOKEN")

    def test_threat_response_distinct_from_status(self):
        self.assertEqual(action("THREAT_DRIVEN", CONTRASTS["threat_present"]), "TAKE_TOKEN")
        self.assertEqual(action("STATUS_DRIVEN", CONTRASTS["threat_present"]), "LEAVE_TOKEN")

    def test_status_distinct_from_threat(self):
        self.assertEqual(action("STATUS_DRIVEN", CONTRASTS["status_challenge"]), "TAKE_TOKEN")

    def test_reciprocity_dependence_separate(self):
        self.assertEqual(action("RECIPROCITY_DEPENDENT", CONTRASTS["dependence_removed"]), "TAKE_TOKEN")
        self.assertEqual(action("DETERRENCE_DEPENDENT", CONTRASTS["dependence_removed"]), "LEAVE_TOKEN")

    def test_penalty_removal_separate(self):
        self.assertEqual(action("DETERRENCE_DEPENDENT", CONTRASTS["sanction_removed"]), "TAKE_TOKEN")
        self.assertEqual(action("RECIPROCITY_DEPENDENT", CONTRASTS["sanction_removed"]), "LEAVE_TOKEN")

    def test_hard_rule_change_distinct(self):
        self.assertEqual(action("HARD_RULE_DEPENDENT", CONTRASTS["rule_disabled"]), "TAKE_TOKEN")

    def test_other_regard_behavior_distinct_from_sanction(self):
        self.assertEqual(action("OTHER_REGARD", CONTRASTS["target_unharmed"]), "TAKE_TOKEN")
        self.assertEqual(action("DETERRENCE_DEPENDENT", CONTRASTS["target_unharmed"]), "LEAVE_TOKEN")

    def test_behaviorally_identical_other_regard_clone_unidentified(self):
        self.assertTrue(all(
            action("OTHER_REGARD", scene) == action("OTHER_REGARD_COPY", scene)
            for scene in CONTRASTS.values()
        ))

    def test_exact_finite_minimum_seven(self):
        ans = minimum_discriminating_battery(CONTRASTS)
        self.assertEqual(ans["selected_count"], 7)
        self.assertEqual(ans["distinct_behavioral_classes"], 8)
        self.assertEqual(ans["candidate_models"], 9)

    def test_selected_battery_preserves_achievable_partition(self):
        ans = minimum_discriminating_battery(CONTRASTS)
        self.assertEqual(
            partition(CONTRASTS, tuple(ans["tests_selected"])),
            partition(CONTRASTS, tuple(CONTRASTS)),
        )

    def test_no_smaller_battery_preserves_full_partition(self):
        from itertools import combinations
        names = sorted(CONTRASTS)
        target = partition(CONTRASTS, tuple(names))
        for size in range(7):
            for subset in combinations(names, size):
                self.assertNotEqual(partition(CONTRASTS, subset), target)

    def test_unresolved_class_retained(self):
        ans = minimum_discriminating_battery(CONTRASTS)
        self.assertIn(["OTHER_REGARD", "OTHER_REGARD_COPY"], ans["unresolved_classes"])
        self.assertFalse(ans["all_candidate_models_identified"])

    def test_no_opportunity_only_control_discriminates_nothing(self):
        self.assertEqual(len(partition({"opportunity_only": CONTROL_OPPORTUNITY},
                                       ("opportunity_only",))), 1)

    def test_subset_single_contrast_does_not_claim_total_identification(self):
        out = minimum_discriminating_battery({"cue_present": CONTRASTS["cue_present"]})
        self.assertEqual(out["distinct_behavioral_classes"], 2)
        self.assertFalse(out["all_candidate_models_identified"])

    def test_empty_contrast_universe_rejected(self):
        with self.assertRaises(ValueError):
            minimum_discriminating_battery({})

    def test_unknown_condition_and_model_rejected(self):
        with self.assertRaises(ValueError):
            partition(CONTRASTS, ("not_declared",))
        with self.assertRaises(ValueError):
            action("DIAGNOSED_EVIL", BASELINE)

    def test_duplicate_contrast_selection_rejected(self):
        with self.assertRaises(ValueError):
            partition(CONTRASTS, ("cue_present", "cue_present"))

    def test_invalid_scene_type_rejected(self):
        with self.assertRaises(ValueError):
            minimum_discriminating_battery({"bad": "not_a_scene"})

    def test_atlas_has_rivals_falsifiers_and_sources(self):
        out = validate_scientific_record(Path(__file__).with_name("hypotheses.json"))
        self.assertGreaterEqual(out["hypotheses"], 15)

    def test_attempted_real_world_promotion_rejected(self):
        doc = json.loads(Path(__file__).with_name("hypotheses.json").read_text())
        doc["status"] = "EMPIRICALLY_PROVEN"
        with TemporaryDirectory() as folder:
            p = Path(folder) / "false.json"
            p.write_text(json.dumps(doc))
            with self.assertRaises(ValueError):
                validate_scientific_record(p)

    def test_missing_competing_explanation_rejected(self):
        doc = json.loads(Path(__file__).with_name("hypotheses.json").read_text())
        doc["hypotheses"][0]["competing_explanation"] = ""
        with TemporaryDirectory() as folder:
            p = Path(folder) / "false.json"
            p.write_text(json.dumps(doc))
            with self.assertRaises(ValueError):
                validate_scientific_record(p)

    def test_actual_person_score_rejected(self):
        doc = json.loads(Path(__file__).with_name("hypotheses.json").read_text())
        doc["person_level_scoring"] = True
        with TemporaryDirectory() as folder:
            p = Path(folder) / "false.json"
            p.write_text(json.dumps(doc))
            with self.assertRaises(ValueError):
                validate_scientific_record(p)

    def test_observation_does_not_certify_minds(self):
        ans = minimum_discriminating_battery(CONTRASTS)
        self.assertFalse(ans["actual_minds_inferred"])
        self.assertFalse(ans["empirical_validation"])

    def test_repeated_source_record_rejected(self):
        doc = json.loads(Path(__file__).with_name("hypotheses.json").read_text())
        doc["hypotheses"].append(doc["hypotheses"][0])
        with TemporaryDirectory() as folder:
            p = Path(folder) / "false.json"
            p.write_text(json.dumps(doc))
            with self.assertRaises(ValueError):
                validate_scientific_record(p)

    def test_deterministic_minimum_tie_break(self):
        a = minimum_discriminating_battery(CONTRASTS)
        b = minimum_discriminating_battery(dict(reversed(list(CONTRASTS.items()))))
        self.assertEqual(a["tests_selected"], b["tests_selected"])

    def test_demo_does_not_infer_real_minds(self):
        out = demonstration()
        self.assertEqual(out["design"]["status"], "SYNTHETIC_FINITE_DESIGN_ONLY")
        self.assertFalse(out["design"]["actual_minds_inferred"])


if __name__ == "__main__":
    unittest.main()
