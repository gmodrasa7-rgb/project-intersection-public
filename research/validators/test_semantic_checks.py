import unittest
from semantic_checks import evidence_semantic_errors, coverage_semantic_errors


class SemanticChecksTest(unittest.TestCase):
    def test_independent_verification_requires_disclosure(self):
        record = {"status": "INDEPENDENTLY_VERIFIED", "verifier": "reviewer", "verified_at": "2026-11-16T00:00:00Z"}
        self.assertTrue(any("independence_disclosure" in e for e in evidence_semantic_errors(record)))

    def test_complete_coverage_rejects_count_mismatch(self):
        record = {"started_at": "2026-11-16T00:00:00Z", "finished_at": "2026-11-16T00:01:00Z",
                  "target_inventory": ["a", "b"], "target_count": 2, "observed_count": 1,
                  "coverage_status": "COMPLETE_AT_REFERENCE", "pagination_exhausted": True,
                  "errors": [], "unresolved": []}
        self.assertTrue(coverage_semantic_errors(record))

    def test_complete_coverage_rejects_time_reversal(self):
        record = {"started_at": "2026-11-16T00:02:00Z", "finished_at": "2026-11-16T00:01:00Z",
                  "target_inventory": ["a"], "target_count": 1, "observed_count": 1,
                  "coverage_status": "COMPLETE_AT_REFERENCE", "pagination_exhausted": True,
                  "errors": [], "unresolved": []}
        self.assertTrue(any("finished_at" in e for e in coverage_semantic_errors(record)))

    def test_valid_complete_coverage(self):
        record = {"started_at": "2026-11-16T00:00:00Z", "finished_at": "2026-11-16T00:01:00Z",
                  "target_inventory": ["a"], "target_count": 1, "observed_count": 1,
                  "coverage_status": "COMPLETE_AT_REFERENCE", "pagination_exhausted": True,
                  "errors": [], "unresolved": []}
        self.assertEqual([], coverage_semantic_errors(record))


if __name__ == "__main__":
    unittest.main()
