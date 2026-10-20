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
import pi_flr_experiment_identity as identity
import check_public_navigation as navigation


class FLRValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads((ROOT / flr.REGISTRY_PATH).read_text(encoding="utf-8"))
        cls.workflow = (ROOT / flr.CI_PATH).read_text(encoding="utf-8")

    def case(self):
        return copy.deepcopy(self.record)

    def test_valid_initial_registry(self):
        out = flr.validate(self.record)
        self.assertEqual(out["version"], "0.1.3")
        self.assertEqual(out["cases"], 7)
        self.assertEqual(out["controls"], 5)

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

    def test_regression_e010_identity_collision(self):
        """FLR-0004: different blocked inspection draft must never replace main E010."""
        current = json.loads((ROOT / identity.RESULT).read_text(encoding="utf-8"))
        source = (ROOT / identity.README).read_text(encoding="utf-8")
        self.assertEqual(identity.audit_identity(current, source, False)["status"],
                         "PUBLIC_E010_IDENTITY_BOUNDARY_PASS")
        old_study = copy.deepcopy(current)
        old_study["model"] = "dynamic_inspector_authority_safety_audit"
        with self.assertRaisesRegex(identity.IdentityError, "E010_IDENTITY_REPLACED"):
            identity.audit_identity(old_study, source, False)

    def test_e010_cannot_be_false_preregistered(self):
        current = json.loads((ROOT / identity.RESULT).read_text(encoding="utf-8"))
        source = (ROOT / identity.README).read_text(encoding="utf-8")
        current["status"] = "PREREGISTERED_EMPIRICALLY_VALIDATED"
        with self.assertRaisesRegex(identity.IdentityError, "E010_EVIDENCE_GRADE"):
            identity.audit_identity(current, source, False)

    def test_e010_colliding_lineage_notice_must_remain(self):
        current = json.loads((ROOT / identity.RESULT).read_text(encoding="utf-8"))
        source = (ROOT / identity.README).read_text(encoding="utf-8")
        with self.assertRaisesRegex(identity.IdentityError, "E010_LEGACY_IDENTITY_COLLISION"):
            identity.audit_identity(current, source.replace("실험 ID 충돌 경고", ""), False)

    def test_e010_blocked_legacy_executable_not_imported(self):
        current = json.loads((ROOT / identity.RESULT).read_text(encoding="utf-8"))
        source = (ROOT / identity.README).read_text(encoding="utf-8")
        with self.assertRaisesRegex(identity.IdentityError, "E010_BLOCKED_LEGACY_BENCHMARK"):
            identity.audit_identity(current, source, True)

    def test_mail_regression_manifest_hash_masking(self):
        """Reproduce FLR-0005: an existing artifact with stale SHA fails closed."""
        current = json.loads((ROOT / rise.MANIFEST).read_text(encoding="utf-8"))
        broken = copy.deepcopy(current)
        item = next(x for x in broken["artifacts"]
                    if x["path"] == "funding/README.md")
        item["git_blob_sha"] = "0" * 40
        with self.assertRaisesRegex(rise.ManifestGuardError, "STALE_GIT_BLOB_SHA"):
            rise.audit(broken, ROOT)

    def test_mail_regression_new_document_registration(self):
        """FLR-0006: removing the DC path from inventory is explicitly detectable."""
        r = json.loads((ROOT / "knowledge/language-edition-register.json")
                       .read_text(encoding="utf-8"))
        target = "operations/PI_RISE_DC_V0_1_0_EN_KO.md"
        paths = {e["path"] for e in r["inventory"]}
        self.assertIn(target, paths, "Current main's language register must include DC")
        simulated = paths - {target}
        self.assertNotIn(target, simulated)
        self.assertTrue((ROOT / target).is_file())

    def test_regression_missing_branch_link_target(self):
        """FLR-0007: the two documented RG-0 references must fail when a crosswalk is absent."""
        target = "research/PI_CORE_01_RG0_C10_CROSSWALK_V0_7_EN.md"
        srcs = ["research/PI_CORE_01_RG0_SIX_CASES_V0_7_EN.md",
                "research/PI_CORE_01_RG0_SPEC_V0_7_EN.md"]
        for source in srcs:
            line = "[C10 crosswalk](PI_CORE_01_RG0_C10_CROSSWALK_V0_7_EN.md)"
            errors = navigation.find_bad_links(
                source, line, exists=lambda path: path != target)
            self.assertEqual(errors, [(source, 1, target)])
            self.assertEqual(navigation.find_bad_links(
                source, line, exists=lambda path: path == target), [])

    def test_sha_drift_cannot_mask_duplicate_path(self):
        """FLR-0005: two independent corruptions must report the structural one first."""
        manifest = json.loads((ROOT / rise.MANIFEST).read_text(encoding="utf-8"))
        stale = copy.deepcopy(manifest)
        stale["artifacts"][0]["git_blob_sha"] = "0" * 40
        stale["artifacts"].append(copy.deepcopy(stale["artifacts"][-1]))
        with self.assertRaisesRegex(rise.ManifestGuardError,
                                    "DUPLICATE_OR_INVALID_PATH"):
            rise.audit(stale, ROOT)

    def test_sha_drift_cannot_mask_missing_required_artifact(self):
        manifest = json.loads((ROOT / rise.MANIFEST).read_text(encoding="utf-8"))
        broken = copy.deepcopy(manifest)
        broken["artifacts"][0]["git_blob_sha"] = "0" * 40
        broken["artifacts"] = [x for x in broken["artifacts"]
                               if x["path"] != "tests/test_pi_rise_manifest_guard.py"]
        with self.assertRaisesRegex(rise.ManifestGuardError,
                                    "MISSING_REQUIRED_ARTIFACTS"):
            rise.audit(broken, ROOT)

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
        newer["release_version"] = "0.1.4"
        newer["cases"] = newer["cases"][1:]
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CASE_DELETED"):
            flr.compare_history(newer, self.record)

    def test_case_metadata_rewrite_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.4"
        newer["cases"][0]["root_cause"] = "silently rewritten"
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CASE_METADATA_REWRITTEN"):
            flr.compare_history(newer, self.record)

    def test_event_erasal_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.4"
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
        newer["release_version"] = "0.1.4"
        self.assertTrue(flr.compare_history(newer, self.record))
        self.assertEqual(flr.validate(newer)["cases"], 7)

    def test_control_deletion_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.4"
        newer["control_registry"] = newer["control_registry"][1:]
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CONTROL_REMOVED"):
            flr.compare_history(newer, self.record)

    def test_version_only_update_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.1.4"
        with self.assertRaisesRegex(flr.FLRError, "EMPTY_VERSION_BUMP"):
            flr.compare_history(newer, self.record)

    def test_private_data_policy_fail_closed(self):
        x = self.case()
        x["release_rules"]["no_private_data"] = False
        with self.assertRaisesRegex(flr.FLRError, "PRIVATE_DATA_BOUNDARY"):
            flr.validate(x)


if __name__ == "__main__":
    unittest.main()
