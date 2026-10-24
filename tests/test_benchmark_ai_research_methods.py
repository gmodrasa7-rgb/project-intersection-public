"""Tests for report parsing: no repository state or real external service is mutated."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "tools/benchmark_ai_research_methods.py"
SPEC = importlib.util.spec_from_file_location("pi_method_benchmark", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BenchmarkParsingTests(unittest.TestCase):
    def test_existing_failure_not_turned_into_pass(self):
        entry = MODULE.result_summary("first_view_contract", 1,
                                      "README / Priority-0 guard FAIL: L0_NOT_FIRST", "")
        self.assertEqual("FAIL", entry["status"])

    def test_missing_auth_not_counted_as_failed_science(self):
        entry = MODULE.result_summary("watcher", 1, "PI_FLR_WATCH_FAIL:GITHUB_TOKEN_MISSING", "")
        self.assertEqual("BLOCKED_AUTH", entry["status"])

    def test_negative_controls_are_counted_only_as_preset(self):
        entry = MODULE.result_summary("source_traceability", 0,
                                      "Source-to-bilingual integrity negative controls: 6/6 detected", "")
        self.assertEqual(6, entry["preset_mutations_detected"])
        self.assertNotIn("blind_accuracy", entry)

    def test_routing_rejects_broken_report(self):
        entry = MODULE.result_summary("question_routing", 0, "not json", "")
        self.assertEqual("FAIL", entry["status"])


if __name__ == "__main__":
    unittest.main()
