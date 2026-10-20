"""Negative mutation regressions for PI-RISE canonical reference and SHA gate."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_rise_manifest_guard as mod


class PublicationManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((ROOT / mod.MANIFEST).read_text(encoding="utf-8"))

    def test_live_manifest_passes_structure_and_all_blob_sha(self):
        result = mod.audit(self.source, ROOT)
        self.assertEqual(result["status"], "PUBLIC_REFERENCE_AND_GIT_BLOB_INTEGRITY_PASS")
        self.assertGreaterEqual(result["tracked_artifact_count"], 13)

    def test_original_regression_old_ledger_name_rejected(self):
        d = copy.deepcopy(self.source)
        d["ledger_ownership"]["institutional_grants_and_contracts"] = (
            "funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md")
        with self.assertRaisesRegex(mod.ManifestGuardError, "LEDGER_OWNERSHIP_NOT_CANONICAL"):
            mod.audit(d, ROOT)

    def test_other_existing_file_is_not_accepted_as_ledger(self):
        d = copy.deepcopy(self.source)
        d["ledger_ownership"]["institutional_grants_and_contracts"] = "README.md"
        with self.assertRaises(mod.ManifestGuardError):
            mod.audit(d, ROOT)

    def test_tracked_missing_file_ref_fails(self):
        d = copy.deepcopy(self.source)
        d["artifacts"][0]["path"] = "operations/NO_SUCH_RELEASE_EN_KO.md"
        with self.assertRaisesRegex(mod.ManifestGuardError, "MISSING_FILE"):
            mod.audit(d, ROOT)

    def test_blob_content_drift_fails_even_when_file_exists(self):
        d = copy.deepcopy(self.source)
        d["artifacts"][0]["git_blob_sha"] = "0" * 40
        with self.assertRaisesRegex(mod.ManifestGuardError, "STALE_GIT_BLOB_SHA"):
            mod.audit(d, ROOT)

    def test_missing_required_artifact_fails(self):
        d = copy.deepcopy(self.source)
        d["artifacts"] = [x for x in d["artifacts"]
                          if x["path"] != "tools/pi_rise_manifest_guard.py"]
        with self.assertRaisesRegex(mod.ManifestGuardError, "MISSING_REQUIRED_ARTIFACTS"):
            mod.audit(d, ROOT)

    def test_duplicate_blob_record_fails(self):
        d = copy.deepcopy(self.source)
        d["artifacts"].append(copy.deepcopy(d["artifacts"][0]))
        with self.assertRaisesRegex(mod.ManifestGuardError, "DUPLICATE_OR_INVALID_PATH"):
            mod.audit(d, ROOT)

    def test_relative_escape_fails(self):
        d = copy.deepcopy(self.source)
        d["artifacts"][0]["path"] = "../secret.md"
        with self.assertRaisesRegex(mod.ManifestGuardError, "UNSAFE_PATH"):
            mod.audit(d, ROOT)

    def test_invalid_hex_fails(self):
        d = copy.deepcopy(self.source)
        d["artifacts"][0]["git_blob_sha"] = "not-a-hash"
        with self.assertRaisesRegex(mod.ManifestGuardError, "INVALID_SHA"):
            mod.audit(d, ROOT)

    def test_false_receipt_claim_cannot_enter_manifest(self):
        d = copy.deepcopy(self.source)
        d["verified_financial_receipts_from_this_release"] = True
        with self.assertRaisesRegex(mod.ManifestGuardError, "UNSUPPORTED_ATTESTATION"):
            mod.audit(d, ROOT)

    def test_candidate_release_cannot_silently_replace_main(self):
        d = copy.deepcopy(self.source)
        d["release_state"] = "BRANCH_CANDIDATE_UNTIL_PR_MERGED"
        with self.assertRaisesRegex(mod.ManifestGuardError, "RELEASE_STATUS_UNVERIFIED"):
            mod.audit(d, ROOT)

    def test_wrong_pipeline_ledger_pointer_rejected(self):
        d = copy.deepcopy(self.source)
        d["ledger_ownership"]["public_application_pipeline"] = "README.md"
        with self.assertRaisesRegex(mod.ManifestGuardError, "LEDGER_OWNERSHIP_NOT_CANONICAL"):
            mod.audit(d, ROOT)

    def test_known_git_blob_hash_vector(self):
        self.assertEqual(mod.git_blob_sha(b"hello\n"),
                         "ce013625030ba8dba906f756967f9e9ca394464a")


if __name__ == "__main__":
    unittest.main()
