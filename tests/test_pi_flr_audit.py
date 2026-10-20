"""PI-FLR recursion/immutability/causal-regression mutation probes.

Synthetic mutations test prevention boundaries, not future incident probability.
"""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_flr_audit as flr
import pi_rise_manifest_guard as rise
import check_language_separation as language


class FLRValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads((ROOT / flr.REGISTRY_PATH).read_text(encoding="utf-8"))
        cls.workflow = (ROOT / flr.CI_PATH).read_text(encoding="utf-8")

    def case(self):
        return copy.deepcopy(self.record)

    def test_valid_initial_registry(self):
        out = flr.validate(self.record)
        self.assertEqual(out["version"], "0.1.0")
        self.assertEqual(out["cases"], 3)
        self.assertEqual(out["controls"], 3)

    def test_regression_original_naming_failure(self):
        """Original FLR-0001 unnamed ledger is rejected by the real language guard."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md"
            bad.parent.mkdir(parents=True)
            bad.write_text("# Original 1 — English\n## Original 2 — 한국어\n", encoding="utf-8")
            prev = language.ROOT
            try:
                language.ROOT = root
                errors = language.new_files_errors(["funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md"])
            finally:
                language.ROOT = prev
            self.assertTrue(any("ADDED_MARKDOWN_LACKS_LANGUAGE_EDITION" in x
                                for x in errors), errors)

    def test_regression_original_manifest_pointer(self):
        """Original FLR-0002 stale reference rejected by actual PI-RISE verifier."""
        d = json.loads((ROOT / rise.MANIFEST).read_text(encoding="utf-8"))
        d["ledger_ownership"]["institutional_grants_and_contracts"] = (
            "funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md")
        with self.assertRaisesRegex(rise.ManifestGuardError,
                                    "LEDGER_OWNERSHIP_NOT_CANONICAL"):
            rise.audit(d, ROOT)

    def test_regression_path_filtered_ci(self):
        """FLR-0003 known allowlist regression rejected by meta-workflow parser."""
        broken = self.workflow.replace("  pull_request:\n",
                                       "  pull_request:\n    paths:\n      - 'research/**'\n", 1)
        self.assertNotEqual(broken, self.workflow)
        with self.assertRaisesRegex(flr.FLRError, "CI_PATH_OR_BRANCH_FILTER"):
            flr.check_ci_contract(broken)

    def test_unfiltered_ci_contract(self):
        self.assertTrue(flr.check_ci_contract(self.workflow))

    def test_duplicate_case_rejected(self):
        x = self.case()
        x["cases"].append(copy.deepcopy(x["cases"][0]))
        with self.assertRaisesRegex(flr.FLRError, "INVALID_OR_DUPLICATE_CASE_ID"):
            flr.validate(x)

    def test_missing_control_rejected(self):
        x = self.case()
        x["cases"][1]["preventive_control_ids"] = ["FLR-C99"]
        with self.assertRaisesRegex(flr.FLRError, "MISSING_REFERENCED_CONTROL"):
            flr.validate(x)

    def test_event_sequence_tamper_rejected(self):
        x = self.case()
        x["cases"][0]["events"][2]["seq"] = 99
        with self.assertRaisesRegex(flr.FLRError, "EVENT_SEQUENCE"):
            flr.validate(x)

    def test_non_source_link_rejected(self):
        x = self.case()
        x["cases"][0]["events"][0]["evidence_url"] = "https://example.org/fake"
        with self.assertRaisesRegex(flr.FLRError, "UNTRUSTED_OR_UNGROUNDED_LINK_HOST"):
            flr.validate(x)

    def test_unproven_merge_rejected(self):
        x = self.case()
        x["cases"][0]["events"] = [e for e in x["cases"][0]["events"]
                                  if e["kind"] != "CI_PASS_OBSERVED"]
        for n, e in enumerate(x["cases"][0]["events"], 1):
            e["seq"] = n
        with self.assertRaisesRegex(flr.FLRError, "CLAIMED_MERGE_WITHOUT_REPAIR_OR_CI"):
            flr.validate(x)

    def test_undeclared_scientific_proof_rejected(self):
        x = self.case()
        x["classification"] = "PROVES_ALL_ERRORS_PREVENTED"
        with self.assertRaisesRegex(flr.FLRError, "PROOF_SCOPE_OVERCLAIM"):
            flr.validate(x)

    def test_case_deletion_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.1"
        newer["cases"] = newer["cases"][1:]
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CASE_DELETED"):
            flr.compare_history(newer, self.record)

    def test_case_metadata_rewrite_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.1"
        newer["cases"][0]["root_cause"] = "silently rewritten"
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CASE_METADATA_REWRITTEN"):
            flr.compare_history(newer, self.record)

    def test_event_erasal_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.1"
        newer["cases"][0]["events"][0]["note"] = "rewritten history"
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_EVIDENCE_REWRITTEN"):
            flr.compare_history(newer, self.record)

    def test_new_event_requires_version_bump(self):
        newer = self.case()
        fresh = dict(newer["cases"][0]["events"][-1])
        fresh.update(seq=len(newer["cases"][0]["events"])+1,
                     kind="LIMITATION_RECORDED",
                     note="Follow-up observation is still not evidence of permanent prevention.")
        newer["cases"][0]["events"].append(fresh)
        with self.assertRaisesRegex(flr.FLRError, "VERSION_BUMP_REQUIRED"):
            flr.compare_history(newer, self.record)
        newer["release_version"] = "0.1.1"
        self.assertTrue(flr.compare_history(newer, self.record))
        self.assertEqual(flr.validate(newer)["cases"], 3)

    def test_control_deletion_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.1"
        newer["control_registry"] = newer["control_registry"][1:]
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CONTROL_REMOVED"):
            flr.compare_history(newer, self.record)

    def test_version_only_update_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.1"
        with self.assertRaisesRegex(flr.FLRError, "EMPTY_VERSION_BUMP"):
            flr.compare_history(newer, self.record)

    def test_private_data_policy_fail_closed(self):
        x = self.case()
        x["release_rules"]["no_private_data"] = False
        with self.assertRaisesRegex(flr.FLRError, "PRIVATE_DATA_BOUNDARY"):
            flr.validate(x)


if __name__ == "__main__":
    unittest.main()
