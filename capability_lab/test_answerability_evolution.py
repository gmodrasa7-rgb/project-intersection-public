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
        self.assertEqual(first["resource_budget"]["candidate_thresholds"], 5)
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

    def test_historical_hard_negative_fixed_outside_selected_benchmark(self):
        # This historical failure was previously an adversarial negative outside
        # both selection/dev and public holdout; do NOT count it as independent gain.
        docs, _, _ = lab.load_cases()
        unsupported = ("What exact number of hours did the contributor spend "
                       "on electricity sleep and equipment?")
        # Preserve the previous baseline failure for an auditable before/after.
        self.assertIsNotNone(lab.prediction(docs, unsupported, 0))
        self.assertIsNone(lab.prediction(docs, unsupported, 0.30))

    def test_numeric_precision_guard_needed_not_sufficient(self):
        # Topic-level lexical overlap cannot conjure an exact unmentioned number.
        self.assertFalse(lab.numeric_precision_has_any_evidence(
            "What exact amount did it cost?", "The cost was not recorded."))
        self.assertFalse(lab.numeric_precision_has_any_evidence(
            "How many hours were spent on repairs?", "The repair log has no hours."))
        self.assertFalse(lab.numeric_precision_has_any_evidence(
            "정확한 금액은 얼마인가?", "연구자 비용과 후원 상태는 미확인이다."))
        # A source containing digits passes only this necessary test, not
        # causal relevance, correct unit, verified provenance or factual truth.
        self.assertTrue(lab.numeric_precision_has_any_evidence(
            "What exact amount did it cost?", "2026 audit described the costs."))
        self.assertTrue(lab.numeric_precision_has_any_evidence(
            "What are the governance concerns?", "No quantitative measure here."))

    def test_numeric_precision_does_not_block_non_numeric_retrieval(self):
        docs, _, _ = lab.load_cases()
        self.assertIsNotNone(
            lab.prediction(docs, "electricity sleep opportunity cost", 1))
        self.assertIsNone(
            lab.prediction(docs, "How many hours were spent on electricity sleep and equipment?", 0.30))

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
