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
import pi_flr_watch as watch
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
        self.assertEqual(out["version"], "0.5.0")
        self.assertEqual(out["cases"], 9)
        self.assertEqual(out["controls"], 11)

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

    def test_meta_link_guard_cannot_be_silently_removed(self):
        """The CI contract rejects removal of repository-wide link verification."""
        broken = self.workflow.replace(
            "python3 tools/check_public_navigation.py --strict-all",
            "python3 tools/check_public_navigation.py --strict-core")
        self.assertNotEqual(broken, self.workflow)
        with self.assertRaisesRegex(flr.FLRError, "CI_WHOLE_REPOSITORY_LINK_GUARD"):
            flr.check_ci_contract(broken)

    def test_report_unknown_failures_never_disappear(self):
        """C07 cannot hide a failed run solely because no job details exist."""
        observed = {
            "id": 901, "name": "Public repository governance audit",
            "workflow_id": 31, "head_branch": "main",
            "status": "completed", "conclusion": "failure",
            "created_at": "2026-10-20T17:00:00Z",
            "updated_at": "2026-10-20T17:05:00Z",
            "run_attempt": 1,
        }
        record = watch.build_report([observed], {901: []},
                                    now="2026-10-21T00:00:00Z")
        self.assertEqual(record["failed_run_without_failed_job_step"], 1)
        self.assertEqual(record["failure_fingerprint_count"], 1)
        self.assertEqual(record["groups"][0]["resolution_status"],
                         "NOT_AUTOMATICALLY_CLOSED")

    def test_watch_deduplicates_distinct_runs(self):
        """FLR-C06: same failure step on distinct runs is one signal cluster, not a proven cause."""
        runs = [
            {"id": 101, "name": "PI-RISE synthetic-only integrity",
             "workflow_id": 13, "head_branch": "main", "status": "completed",
             "conclusion": "failure", "created_at": "2026-10-20T18:00:00Z"},
            {"id": 102, "name": "PI-RISE synthetic-only integrity",
             "workflow_id": 13, "head_branch": "main", "status": "completed",
             "conclusion": "failure", "created_at": "2026-10-20T19:00:00Z"},
        ]
        jobs = {i: [{"id": 500+i, "name": "synthetic-check", "conclusion": "failure",
                     "steps": [{"name": "Unit regression tests", "conclusion": "failure"}]}]
                for i in (101, 102)}
        result = watch.build_report(runs, jobs, now="2026-10-21T00:00:00Z")
        self.assertEqual(result["failure_fingerprint_count"], 1)
        self.assertEqual(result["groups"][0]["run_count"], 2)
        self.assertEqual(result["groups"][0]["resolution_status"],
                         "NOT_AUTOMATICALLY_CLOSED")

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
        newer["release_version"] = "0.5.1"
        newer["cases"] = newer["cases"][1:]
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CASE_DELETED"):
            flr.compare_history(newer, self.record)

    def test_case_metadata_rewrite_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.5.1"
        newer["cases"][0]["root_cause"] = "silently rewritten"
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CASE_METADATA_REWRITTEN"):
            flr.compare_history(newer, self.record)

    def test_event_erasal_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.5.1"
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
        newer["release_version"] = "0.5.1"
        self.assertTrue(flr.compare_history(newer, self.record))
        self.assertEqual(flr.validate(newer)["cases"], 9)

    def test_control_deletion_against_prior_version_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.5.1"
        newer["control_registry"] = newer["control_registry"][1:]
        with self.assertRaisesRegex(flr.FLRError, "HISTORICAL_CONTROL_REMOVED"):
            flr.compare_history(newer, self.record)

    def test_version_only_update_rejected(self):
        newer = self.case()
        newer["release_version"] = "0.5.1"
        with self.assertRaisesRegex(flr.FLRError, "EMPTY_VERSION_BUMP"):
            flr.compare_history(newer, self.record)

    def test_private_data_policy_fail_closed(self):
        x = self.case()
        x["release_rules"]["no_private_data"] = False
        with self.assertRaisesRegex(flr.FLRError, "PRIVATE_DATA_BOUNDARY"):
            flr.validate(x)


    def test_regression_english_first_english_only(self):
        """FLR-0008: real README language detector rejects Hangul in EN founding purpose."""
        sample = (
            "# Project Intersection\n"
            "## English — Primary\n"
            + language.EN_README + "\n"
            + "[Korean](navigation/START_HERE_KO.md) 한국어 본문 유입\n"
            + "## 한국어 — Secondary\n"
            + language.KO_README + "\n"
            + "[English](navigation/START_HERE_EN.md)\n"
        )
        self.assertIn("README_ENGLISH_SECTION_CONTAINS_KOREAN_PROSE",
                      language.readme_errors(sample))

    def test_regression_partial_green_is_not_global_release(self):
        """FLR-0009: one green README checker cannot close the failed PI-RISE job."""
        import pi_flr_conversation_audit as conversation
        expected = ["README English-first language order",
                    "PI-RISE synthetic-only integrity"]
        results = [{"name": expected[0], "conclusion": "success"},
                   {"name": expected[1], "conclusion": "failure"}]
        report = conversation.validate_release_matrix(results, expected)
        self.assertFalse(report["ready"])
        self.assertEqual(report["status"], "BLOCKED_FAILED")
        self.assertEqual(report["failed"], [expected[1]])


    def test_regression_prior_art_independence_and_preflight(self):
        """C10: duplicate source lineages must not count as independent evidence."""
        import pi_flr_prior_art_guard as pa
        d=json.loads((ROOT/pa.PATH).read_text(encoding="utf-8"))
        report=pa.preflight(d,["README.md"])
        self.assertIn("FLR-0008",report["changed_paths"][0]["past_cases"])
        self.assertEqual(report["changed_paths"][0]["outcome"],
                         "CHECKS_NOT_EXECUTED_BY_PREFLIGHT")
        bad=copy.deepcopy(d)
        bad["principles"][0]["challenge"]=[]
        with self.assertRaisesRegex(pa.PriorArtError,"SELF_CONFIRMATION"):
            pa.validate(bad,self.record,(ROOT/pa.WORKFLOW).read_text(encoding="utf-8"))



    def test_regression_replay_executes_prior_case_checks(self):
        """FLR-C11 rejects a missing executable check and preserves failures."""
        import pi_flr_replay_gate as replay
        from types import SimpleNamespace
        data=json.loads((ROOT/replay.TRANSFER_PATH).read_text(encoding="utf-8"))
        plan=replay.planned_replay(data,["README.md"])
        self.assertEqual(set(plan["check_ids"]),
                         {"README_L0","LANGUAGE","RISE_MANIFEST"})
        def forced_failure(command, **kwargs):
            return SimpleNamespace(returncode=1 if
                                   "tools/pi_rise_manifest_guard.py" in command else 0)
        observed=replay.execute(plan,run=forced_failure)
        self.assertEqual(observed["status"],"BLOCKED_FAILED")
        self.assertEqual(observed["failed_checks"],["RISE_MANIFEST"])
        with self.assertRaisesRegex(replay.ReplayError,"BASELINE_COMMIT_NOT_OBSERVED"):
            replay.git_changed_paths("")



if __name__ == "__main__":
    unittest.main()
