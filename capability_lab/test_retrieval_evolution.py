"""Regression tests for the bounded capability-selection experiment."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from capability_lab import retrieval_evolution as lab


class EvolutionTests(unittest.TestCase):
    def test_splits_are_disjoint_and_documents_grounded(self):
        data = lab.load()
        dev = {x["question"] for x in data["development"]}
        hold = {x["question"] for x in data["holdout"]}
        self.assertFalse(dev & hold)
        ids = {x["id"] for x in data["documents"]}
        for task in data["development"] + data["holdout"]:
            self.assertIn(task["expected"], ids)
        self.assertEqual(len(ids), len(data["documents"]))

    def test_duplicate_ids_are_rejected(self):
        data = lab.load()
        altered = copy.deepcopy(data)
        altered["documents"][1]["id"] = altered["documents"][0]["id"]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "duplicate.json"
            p.write_text(json.dumps(altered), encoding="utf-8")
            with self.assertRaises(ValueError):
                lab.load(p)

    def test_public_saturated_holdout_cannot_certify_improvement(self):
        report = lab.run()
        self.assertTrue(report["holdout_saturated_at_baseline"])
        self.assertTrue(report["public_holdout_not_independent"])
        self.assertEqual(report["decision"], "HOLD")

    def test_bounded_and_repeatable(self):
        a, b = lab.run(), lab.run()
        self.assertEqual(a, b)
        self.assertEqual(a["resource_budget"]["strategy_count"], 4)
        self.assertEqual(a["independent_external_validation"], False)
        self.assertEqual(a["human_correction_required"], False)
        self.assertIn(a["decision"], {"PROMOTE_NARROW_RETRIEVAL", "HOLD"})

    def test_no_gain_must_hold(self):
        with patch.object(lab, "STRATEGIES", (lab.STRATEGIES[0],)):
            self.assertEqual(lab.run()["decision"], "HOLD")

    def test_holdout_changes_cannot_change_selection(self):
        data = lab.load()
        original = lab.run()["development_selected"]
        altered = copy.deepcopy(data)
        # Change holdout labels only; the development selection must be invariant.
        labels = [d["id"] for d in altered["documents"]]
        for t in altered["holdout"]:
            t["expected"] = labels[0]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "altered.json"
            p.write_text(json.dumps(altered), encoding="utf-8")
            self.assertEqual(lab.run(p)["development_selected"], original)

    def test_promotion_does_not_regress_holdout(self):
        report = lab.run()
        if report["decision"] == "PROMOTE_NARROW_RETRIEVAL":
            self.assertGreater(report["candidate_development"]["correct"],
                               report["baseline_development"]["correct"])
            self.assertGreater(report["candidate_holdout"]["correct"],
                               report["baseline_holdout"]["correct"])
            self.assertEqual(report["regressed_holdout_cases"], [])

    def test_length_and_tokenization_bounded(self):
        data = lab.load()
        for method in lab.STRATEGIES:
            first = lab.rankings(data["documents"], "verified delivery independent receipt", method)
            self.assertEqual(len(first), len(data["documents"]))
            self.assertEqual(set(first), {d["id"] for d in data["documents"]})


if __name__ == "__main__":
    unittest.main()
