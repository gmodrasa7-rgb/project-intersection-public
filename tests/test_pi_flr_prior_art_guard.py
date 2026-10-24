"""Adversarial verification for PI-FLR prior-art transfer and case reuse."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import pi_flr_prior_art_guard as p


class PriorArtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/p.PATH).read_text(encoding="utf-8"))
        cls.cases=json.loads((ROOT/p.REGISTRY).read_text(encoding="utf-8"))
        cls.workflow=(ROOT/p.WORKFLOW).read_text(encoding="utf-8")

    def check(self,d):
        return p.validate(d,self.cases,self.workflow)

    def test_existing_transfer_valid_and_bounded(self):
        report=self.check(self.data)
        self.assertEqual(report["status"],"PRIOR_ART_MAPPING_VALID_NOT_FIELD_EFFECTIVENESS")
        self.assertEqual(report["mapped_cases"],len(self.cases["cases"]))
        self.assertEqual(report["effectiveness_verified"],0)

    def test_english_primary_must_be_first(self):
        d=copy.deepcopy(self.data);d["language_order"].reverse()
        with self.assertRaisesRegex(p.PriorArtError,"ENGLISH_PRIMARY"):
            self.check(d)

    def test_literature_not_declared_saturated(self):
        d=copy.deepcopy(self.data);d["saturation"]="COMPLETE"
        with self.assertRaisesRegex(p.PriorArtError,"FALSE_LITERATURE"):
            self.check(d)

    def test_correlated_support_is_not_two_independent_sources(self):
        d=copy.deepcopy(self.data)
        d["sources"][1]["lineage"]=d["sources"][0]["lineage"]
        d["principles"][0]["support"]=["S01","S02"]
        with self.assertRaisesRegex(p.PriorArtError,"CORRELATED_SOURCE_FAMILIES"):
            self.check(d)

    def test_counterevidence_cannot_be_removed(self):
        d=copy.deepcopy(self.data);d["principles"][0]["challenge"]=[]
        with self.assertRaisesRegex(p.PriorArtError,"SELF_CONFIRMATION"):
            self.check(d)

    def test_favorable_ai_model_scores_cannot_claim_field_impact(self):
        d=copy.deepcopy(self.data)
        d["principles"][0]["transfer_status"]="PROVEN_RECURSIVE_SELF_IMPROVEMENT"
        with self.assertRaisesRegex(p.PriorArtError,"ASSERTED_REAL_WORLD_EFFICACY"):
            self.check(d)

    def test_unobserved_recurrence_window_never_verifies_effectiveness(self):
        d=copy.deepcopy(self.data)
        d["effectiveness_by_case"][0]["status"]="FIELD_VERIFIED"
        with self.assertRaisesRegex(p.PriorArtError,"FIELD_EFFECTIVENESS_CANNOT_BE_ATTESTED"):
            self.check(d)

    def test_unobserved_unknown_not_zero(self):
        d=copy.deepcopy(self.data)
        d["efficiency"]["unknown_policy"]="Unknown history has zero failures."
        with self.assertRaisesRegex(p.PriorArtError,"UNKNOWN_OR_ABSENCE"):
            self.check(d)

    def test_private_raw_chat_boundary(self):
        d=copy.deepcopy(self.data)
        d["efficiency"]["privacy_boundary"]="Publish raw personal chats"
        with self.assertRaisesRegex(p.PriorArtError,"RAW_PERSONAL_CHATS"):
            self.check(d)

    def test_preflight_readme_replays_three_past_failures(self):
        route=p.preflight(self.data,["README.md"])["changed_paths"][0]
        self.assertEqual(route["past_cases"],["FLR-0005","FLR-0008","FLR-0009"])
        self.assertEqual(route["outcome"],"CHECKS_NOT_EXECUTED_BY_PREFLIGHT")

    def test_preflight_workflow_rechecks_global_visibility(self):
        route=p.preflight(self.data,[".github/workflows/pi-flr-integrity.yml"])["changed_paths"][0]
        self.assertIn("FLR-0003",route["past_cases"])
        self.assertIn("FLR-0009",route["past_cases"])

    def test_unmatched_path_not_falsely_certified(self):
        route=p.preflight(self.data,["random/unseen_file.txt"])["changed_paths"][0]
        self.assertEqual(route["known_risk_rules"],[])
        self.assertEqual(route["outcome"],"CHECKS_NOT_EXECUTED_BY_PREFLIGHT")

    def test_parent_case_orphan_cannot_be_silently_ignored(self):
        d=copy.deepcopy(self.data);d["principles"][-1]["cases"]=[]
        with self.assertRaisesRegex(p.PriorArtError,"UNKNOWN_OR_EMPTY_CASE_CROSSWALK"):
            self.check(d)

    def test_case_cannot_be_protected_by_unrelated_control(self):
        d=copy.deepcopy(self.data)
        d["preflight"][0]["controls"]=["FLR-C06"]
        with self.assertRaisesRegex(p.PriorArtError,"PREFLIGHT_HAS_NO_REAL_CASE_CONTROL"):
            self.check(d)

    def test_missing_control_execution_hook(self):
        broken=self.workflow.replace("python3 tools/pi_flr_prior_art_guard.py",
                                     "python3 tools/not_a_guard.py")
        with self.assertRaisesRegex(p.PriorArtError,"PRIOR_ART_REGRESSION_NOT_EXECUTED"):
            p.validate(self.data,self.cases,broken)

    def test_historic_source_cannot_be_rewritten_by_version(self):
        d=copy.deepcopy(self.data);d["version"]="0.3.2"
        d["sources"][0]["lesson"]="a different unsupported reading"
        with self.assertRaisesRegex(p.PriorArtError,"HISTORIC_TRANSFER_REWRITTEN"):
            p.compare_history(d,self.data)

    def test_append_only_new_observation_requires_version_bump(self):
        d=copy.deepcopy(self.data)
        d["improvement_observations"].append({
            "id":"OBS1","case_id":"FLR-0005","state":"UNVERIFIED",
            "receipt_url":"https://github.com/gmodrasa7-rgb/project-intersection-public/pull/345",
            "limitation":"No subsequent real-world recurrence monitoring available."})
        with self.assertRaisesRegex(p.PriorArtError,"UNVERSIONED_PRIOR_ART_CHANGE"):
            p.compare_history(d,self.data)
        d["version"]="0.3.2"
        self.assertTrue(p.compare_history(d,self.data))
        self.check(d)

    def test_fake_effectiveness_receipt_origin_rejected(self):
        d=copy.deepcopy(self.data)
        d["improvement_observations"].append({
            "id":"OBS2","case_id":"FLR-0009","state":"REPAIR_OBSERVED",
            "receipt_url":"https://example.invalid/fake",
            "limitation":"Self assertion, not independent verification."})
        with self.assertRaisesRegex(p.PriorArtError,"OBSERVATION_RECEIPT_UNTRUSTED"):
            self.check(d)


if __name__=="__main__":
    unittest.main()
