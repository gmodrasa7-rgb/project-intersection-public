"""Adversarial regression checks for narrow lexical abstention."""
import copy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from capability_lab import answerability_evolution as lab


class AnswerabilityTests(unittest.TestCase):
    def test_deterministic_and_existing_answers_preserved_on_promotion(self):
        first = lab.run()
        self.assertEqual(first, lab.run())
        self.assertEqual(first["independent_external_validation"], False)
        self.assertEqual(first["general_factual_grounding"], False)
        self.assertEqual(first["resource_budget"]["candidate_thresholds"], 4)
        if first["decision"] == "PROMOTE_SYNTHETIC_ABSTENTION_ONLY":
            self.assertGreater(
                first["candidate_development"]["correct"],
                first["baseline_development"]["correct"],
            )
            self.assertGreater(
                first["candidate_holdout"]["correct"],
                first["baseline_holdout"]["correct"],
            )
            self.assertEqual(first["holdout_supported_regressions"], [])

    def test_never_promote_when_search_has_no_alternative(self):
        with patch.object(lab, "THRESHOLDS", (0,)):
            self.assertEqual(lab.run()["decision"], "HOLD")

    def test_holdout_labels_not_used_to_select_threshold(self):
        original = lab.run()["selected_overlap_threshold"]
        contents = json.loads(lab.CASES.read_text(encoding="utf-8"))
        altered = copy.deepcopy(contents)
        altered["holdout_unknown"] = [
            "unobserved astronomy meteorite trajectory one",
            "unobserved astronomy meteorite trajectory two",
            "unobserved astronomy meteorite trajectory three",
        ]
        with TemporaryDirectory() as folder:
            path = Path(folder) / "cases.json"
            path.write_text(json.dumps(altered), encoding="utf-8")
            self.assertEqual(original, lab.run(path)["selected_overlap_threshold"])

    def test_unknown_vs_supported_and_no_overlap(self):
        docs, dev, holdout = lab.load_cases()
        self.assertTrue(all(c["expected"] is None for c in holdout[-5:]))
        self.assertEqual(
            lab.prediction(docs, "deepwater penguin astronomy orbit", 1), None
        )
        self.assertIsNotNone(
            lab.prediction(docs, "electricity sleep opportunity cost", 1)
        )
        with self.assertRaises(ValueError):
            lab.prediction(docs, "any", -1)

    def test_hard_negative_remains_visible_as_failure(self):
        # A topical unsupported question can receive a confident lexical match.
        # Keep this negative control rather than presenting a false universal solution.
        result = lab.run()
        self.assertLess(
            result["candidate_holdout"]["unsupported_correct"],
            result["candidate_holdout"]["unsupported_total"],
        )

    def test_invalid_split_raises(self):
        contents = json.loads(lab.CASES.read_text(encoding="utf-8"))
        contents["holdout_unknown"][0] = contents["development_unknown"][0]
        with TemporaryDirectory() as folder:
            path = Path(folder) / "cases.json"
            path.write_text(json.dumps(contents), encoding="utf-8")
            with self.assertRaises(ValueError):
                lab.load_cases(path)


if __name__ == "__main__":
    unittest.main()
