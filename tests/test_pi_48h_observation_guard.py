#!/usr/bin/env python3
"""Adversarial failure checks; no independent science validation."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_48h_observation_guard as guard

DATA = ROOT / "research" / "PI_48H_OBSERVATION_EVIDENCE_V0_1_0.json"

class ObservationBoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads(DATA.read_text(encoding="utf-8"))

    def altered(self):
        return copy.deepcopy(self.baseline)

    def reject(self, change):
        doc = self.altered()
        change(doc)
        self.assertTrue(guard.errors(doc), msg="unjustified promotion went undetected")

    def test_baseline(self):
        self.assertEqual([], guard.errors(self.baseline))
        self.assertEqual(9, len(self.baseline["records"]))

    def test_unauthorized_empirical_success(self):
        self.reject(lambda d: d["records"][0].update(real_world_effect_established=True))

    def test_independent_replication_forgery(self):
        self.reject(lambda d: d["records"][2].update(external_independent_reproduction=True))

    def test_missing_axis(self):
        self.reject(lambda d: d["records"][3]["axes"].pop("meta_consent"))

    def test_inferred_motivation(self):
        self.reject(lambda d: d["records"][3]["axes"]["motive_identifiability"].update(status="SOURCE_REPORTED"))

    def test_synthetic_to_real_promotion(self):
        self.reject(lambda d: d["records"][4]["axes"]["action_respect"].update(status="SOURCE_REPORTED"))

    def test_missing_reference(self):
        self.reject(lambda d: d["records"][5].update(source_paths=["research/no-such-research.md"]))

    def test_escaped_path(self):
        self.reject(lambda d: d["records"][0].update(source_paths=["../../P-CHRONICLE/private.md"]))

    def test_unsupported_status(self):
        self.reject(lambda d: d["records"][3]["axes"]["motive_identifiability"].update(status="PROVEN"))

    def test_duplicate_record(self):
        self.reject(lambda d: d["records"].append(copy.deepcopy(d["records"][0])))

    def test_saturation_promotion(self):
        self.reject(lambda d: d.update(literature_saturation="SATURATED"))

    def test_unfounded_global_coexistence_score(self):
        self.reject(lambda d: d["records"][1].update(overall_coexistence_score=1))

    def test_missing_rival_explanations(self):
        self.reject(lambda d: d["records"][2].update(rival_explanations=[]))

    def test_wrong_url(self):
        self.reject(lambda d: d["records"][2].update(original_sources=["file:///private"]))

    def test_toy_assumptions_as_external_empirical(self):
        self.reject(lambda d: d["records"][6]["axes"]["credible_exit"].update(status="TOY_ASSUMED"))

if __name__ == "__main__":
    unittest.main()
