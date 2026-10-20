"""PI-RISE-CUT synthetic fault-tree tests; no external or personal data."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pi_rise_cutset import COMPONENTS, evaluate, minimal_cuts, report


class CutsetTests(unittest.TestCase):
    def test_record_requires_both_archives_to_fail(self):
        self.assertEqual(minimal_cuts("research_record_readable"),
                         [["local_archive", "public_archive"]])

    def test_operation_has_four_single_point_failures_and_two_pairs(self):
        actual = {frozenset(v) for v in minimal_cuts("active_independent_research_possible")}
        expected = {
            frozenset(["human_availability"]),
            frozenset(["researcher_support"]),
            frozenset(["scientific_integrity"]),
            frozenset(["research_independence"]),
            frozenset(["local_compute", "remote_compute"]),
            frozenset(["local_archive", "public_archive"]),
        }
        self.assertEqual(actual, expected)

    def test_standalone_remote_compute_preserves_function(self):
        working = set(COMPONENTS) - {"local_compute"}
        self.assertTrue(evaluate(working)["active_independent_research_possible"])

    def test_standalone_public_archive_preserves_record(self):
        working = set(COMPONENTS) - {"local_archive"}
        self.assertTrue(evaluate(working)["research_record_readable"])

    def test_both_compute_unavailable_stops_active_operation_but_not_record(self):
        working = set(COMPONENTS) - {"local_compute", "remote_compute"}
        self.assertFalse(evaluate(working)["active_independent_research_possible"])
        self.assertTrue(evaluate(working)["research_record_readable"])

    def test_human_availability_is_not_equivalent_to_compute(self):
        working = set(COMPONENTS) - {"human_availability"}
        self.assertFalse(evaluate(working)["active_independent_research_possible"])

    def test_no_probability_or_validation_pretence(self):
        x = report()
        self.assertEqual(x["status"], "SYNTHETIC_FAULT_TREE_MODEL_ONLY")
        self.assertIn("NO_FAILURE_PROBABILITIES", x["limitations"])
        self.assertNotIn("real_failure_probability", x)

    def test_fail_closed_on_duplicates_and_complexity(self):
        with self.assertRaises(ValueError):
            minimal_cuts("research_record_readable", components=("local_archive",) * 2)
        with self.assertRaises(ValueError):
            minimal_cuts("research_record_readable", components=tuple(str(i) for i in range(13)))


if __name__ == "__main__":
    unittest.main()
