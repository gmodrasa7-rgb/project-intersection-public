"""Offline PI-FLR watch adversarial regression: network-free synthetic GitHub fixtures."""
import copy
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_flr_watch as watch

NOW = "2026-10-21T00:00:00Z"


def run(n, *, name="PI-RISE synthetic-only integrity", conclusion="failure",
        created_at="2026-10-20T18:00:00Z", branch="main", workflow_id=13):
    started = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    finished = started + timedelta(minutes=2)
    return {"id": n, "name": name, "conclusion": conclusion, "created_at": created_at,
            "run_started_at": started.isoformat(), "updated_at": finished.isoformat(),
            "status": "completed", "workflow_id": workflow_id, "head_branch": branch}


def job(n, *, step="Unit regression tests", conclusion="failure"):
    return {"id": n, "name": "synthetic-check", "conclusion": conclusion,
            "steps": [{"name": step, "conclusion": conclusion}]}


class WatchTests(unittest.TestCase):
    def test_clean_empty_window_is_no_failure_not_assured_completeness(self):
        out = watch.build_report([], {}, now=NOW)
        self.assertEqual(out["failure_fingerprint_count"], 0)
        self.assertFalse(out["automatic_closure_enabled"])
        self.assertEqual(out["observation_coverage"],
                         "BOUNDED_WINDOW_NOT_FULL_REPOSITORY_HISTORY")

    def test_repeated_failures_cluster_without_duplicate_incident(self):
        r = [run(101), run(102)]
        j = {101:[job(501)], 102:[job(502)]}
        out = watch.build_report(r, j, now=NOW)
        self.assertEqual(out["failure_fingerprint_count"], 1)
        self.assertEqual(out["groups"][0]["run_count"], 2)
        self.assertEqual(out["groups"][0]["run_ids"], [102, 101])
        self.assertEqual(out["groups"][0]["root_cause_status"],
                         "UNKNOWN_NEEDS_JOB_LOG_AND_CAUSAL_REVIEW")

    def test_different_failure_step_separates_clusters(self):
        r = [run(101), run(102)]
        j = {101:[job(501,step="Step A")], 102:[job(502,step="Step B")]}
        self.assertEqual(watch.build_report(r,j,now=NOW)["failure_fingerprint_count"],2)

    def test_multiple_identical_failed_jobs_same_run_count_once(self):
        r = [run(101)]
        j = {101:[job(501),job(502)]}
        out=watch.build_report(r,j,now=NOW)
        self.assertEqual(out["groups"][0]["run_count"],1)

    def test_distinct_branches_never_merged_as_one_failure_signal(self):
        runs = [run(101, branch="main"), run(102, branch="research/new-experiment")]
        jobs = {101:[job(501)], 102:[job(502)]}
        result = watch.build_report(runs, jobs, now=NOW)
        self.assertEqual(result["failure_fingerprint_count"], 2)

    def test_success_started_before_failure_completed_is_not_recovery(self):
        first = run(101, created_at="2026-10-20T18:00:00Z")
        next_run = run(102, conclusion="success",
                       created_at="2026-10-20T18:01:00Z")
        result = watch.build_report([first, next_run], {101:[job(501)]}, now=NOW)
        self.assertFalse(result["groups"][0][
            "subsequent_success_same_workflow_and_branch"])

    def test_missing_failure_completion_time_cannot_prove_recovery(self):
        failed = run(101)
        failed.pop("updated_at")
        later = run(102, conclusion="success",
                    created_at="2026-10-20T21:00:00Z")
        result = watch.build_report([failed, later], {101:[job(501)]}, now=NOW)
        self.assertFalse(result["groups"][0][
            "subsequent_success_same_workflow_and_branch"])

    def test_branch_names_not_exposed(self):
        secret = "private-branch-account-123"
        result = watch.build_report([run(101, branch=secret)],
                                    {101:[job(501)]}, now=NOW)
        import json
        self.assertNotIn(secret, json.dumps(result))

    def test_action_required_without_job_still_visible(self):
        candidate = run(101, conclusion="action_required")
        result = watch.build_report([candidate], {101:[]}, now=NOW)
        self.assertEqual(result["failure_fingerprint_count"], 1)
        self.assertEqual(result["groups"][0]["resolution_status"],
                         "NOT_AUTOMATICALLY_CLOSED")

    def test_startup_failure_without_job_still_visible(self):
        candidate = run(101, conclusion="startup_failure")
        result = watch.build_report([candidate], {101:[]}, now=NOW)
        self.assertEqual(result["failure_fingerprint_count"], 1)

    def test_report_without_failed_job_is_not_clean(self):
        result = watch.build_report([run(101)], {101:[]}, now=NOW)
        self.assertGreater(result["failure_fingerprint_count"], 0)

    def test_success_after_failure_does_not_mark_case_closed(self):
        r = [run(101),run(102,conclusion="success",
             created_at="2026-10-20T21:00:00Z")]
        out=watch.build_report(r,{101:[job(501)]},now=NOW)
        self.assertTrue(out["groups"][0]["subsequent_success_same_workflow_and_branch"])
        self.assertEqual(out["groups"][0]["resolution_status"],
                         "NOT_AUTOMATICALLY_CLOSED")

    def test_different_branch_success_cannot_imply_recovery(self):
        r = [run(101),run(102,conclusion="success", branch="fix-other",
             created_at="2026-10-20T21:00:00Z")]
        out=watch.build_report(r,{101:[job(501)]},now=NOW)
        self.assertFalse(out["groups"][0]["subsequent_success_same_workflow_and_branch"])

    def test_success_before_failure_cannot_imply_recovery(self):
        r = [run(101),run(102,conclusion="success",
             created_at="2026-10-20T16:00:00Z")]
        out=watch.build_report(r,{101:[job(501)]},now=NOW)
        self.assertFalse(out["groups"][0]["subsequent_success_same_workflow_and_branch"])

    def test_old_run_outside_window_excluded(self):
        old=run(101,created_at="2026-10-16T18:00:00Z")
        self.assertEqual(watch.build_report([old],{},now=NOW)["failure_fingerprint_count"],0)

    def test_in_progress_excluded_without_unknown_assurance(self):
        r=run(101)
        r["status"]="in_progress"
        self.assertEqual(watch.build_report([r],{},now=NOW)["failure_fingerprint_count"],0)

    def test_missing_job_details_fail_closed(self):
        with self.assertRaisesRegex(watch.WatchError,"MISSING_FAILED_RUN_JOB_DETAILS"):
            watch.build_report([run(101)],{},now=NOW)

    def test_duplicate_run_fails_closed(self):
        with self.assertRaisesRegex(watch.WatchError,"DUPLICATE_RUN_ID"):
            watch.build_report([run(101),run(101)],{101:[job(501)]},now=NOW)

    def test_future_run_fails_closed(self):
        with self.assertRaisesRegex(watch.WatchError,"RUN_IN_FUTURE"):
            watch.build_report([run(101,created_at="2026-10-22T06:00:00Z")],
                               {},now=NOW)

    def test_empty_failed_job_list_reported_not_fabricated_cause(self):
        out=watch.build_report([run(101)],{101:[]},now=NOW)
        self.assertEqual(out["failed_run_without_failed_job_step"],1)
        self.assertEqual(out["failure_fingerprint_count"],1)
        self.assertEqual(out["groups"][0]["root_cause_status"],
                         "UNCLASSIFIED_FAILED_RUN_NEEDS_MANUAL_REVIEW")

    def test_job_without_step_produces_unknown_step_fingerprint(self):
        j=job(501);j["steps"]=[]
        out=watch.build_report([run(101)],{101:[j]},now=NOW)
        self.assertEqual(out["failure_fingerprint_count"],1)
        self.assertEqual(out["groups"][0]["root_cause_status"],
                         "UNKNOWN_NEEDS_JOB_LOG_AND_CAUSAL_REVIEW")

    def test_avoid_raw_label_and_personal_data_exposure(self):
        secret="internal@example.invalid token ABCDE1234"
        sensitive_job=job(501,step=secret)
        sensitive_job["name"]=secret
        out=watch.build_report([run(101)],{101:[sensitive_job]},now=NOW)
        import json
        raw=json.dumps(out,ensure_ascii=False)
        self.assertNotIn(secret, raw)
        self.assertNotIn("example.invalid", raw)

    def test_reproducible_fingerprints(self):
        f=watch._signal(13,"same job","step")
        self.assertEqual(f,watch._signal(13,"same job","step"))
        self.assertNotEqual(f,watch._signal(13,"same job","different"))

    def test_partial_scan_marker(self):
        out=watch.build_report([],{ },now=NOW,limit_reached=True)
        self.assertEqual(out["observation_coverage"],"PARTIAL_LIMIT_REACHED")

    def test_fail_closed_when_github_credentials_missing(self):
        with self.assertRaisesRegex(watch.WatchError,"GITHUB_TOKEN_MISSING"):
            watch._get_json(watch.API+"/actions/runs","")

    def test_network_access_scoped_to_github_repo(self):
        with self.assertRaisesRegex(watch.WatchError,"OUTSIDE_REPO_API"):
            watch._get_json("https://other-site.invalid/actions","secret")

    def test_offline_scan_api_errors_do_not_fabricate_empty_report(self):
        with patch.object(watch,"_get_json",side_effect=watch.WatchError("API_OFFLINE")):
            with self.assertRaisesRegex(watch.WatchError,"API_OFFLINE"):
                watch.scan_github("dummy",now=NOW)

    def test_bounded_scan_ignores_cancelled_and_records_failed_run(self):
        failed=run(101)
        cancelled=run(102,conclusion="cancelled")
        with patch.object(watch,"_get_json",side_effect=[
            {"workflow_runs":[failed,cancelled]},
            {"jobs":[job(501)],"total_count":1},
        ]):
            out=watch.scan_github("dummy",now=NOW)
        self.assertEqual(out["scanned_completed_runs"],2)
        self.assertEqual(out["failure_fingerprint_count"],1)

    def test_truncated_job_pages_do_not_silently_pass(self):
        with patch.object(watch,"_get_json",side_effect=[
            {"workflow_runs":[run(101)]},
            {"jobs":[job(501)],"total_count":2},
        ]):
            with self.assertRaisesRegex(watch.WatchError,"FAILED_RUN_JOBS_TRUNCATED"):
                watch.scan_github("dummy",now=NOW)

    def test_watch_workflow_is_read_only_and_hourly(self):
        raw=(ROOT/".github/workflows/pi-flr-watch.yml").read_text(encoding="utf-8")
        self.assertTrue(watch.validate_workflow_contract(raw))
        tampered=raw.replace("actions: read","actions: write")
        with self.assertRaisesRegex(watch.WatchError,"WATCH_NOT_READ_ONLY"):
            watch.validate_workflow_contract(tampered)

    def test_additional_permission_scope_rejected(self):
        raw=(ROOT/".github/workflows/pi-flr-watch.yml").read_text(encoding="utf-8")
        mutated=raw.replace("  actions: read", "  actions: read\n  pull-requests: write")
        with self.assertRaisesRegex(watch.WatchError,"WATCH_NOT_READ_ONLY"):
            watch.validate_workflow_contract(mutated)

    def test_job_level_permission_override_rejected(self):
        raw=(ROOT/".github/workflows/pi-flr-watch.yml").read_text(encoding="utf-8")
        mutated=raw.replace("    runs-on: ubuntu-latest",
                            "    permissions: write-all\n    runs-on: ubuntu-latest")
        with self.assertRaisesRegex(watch.WatchError,"WATCH_NOT_READ_ONLY"):
            watch.validate_workflow_contract(mutated)

    def test_missing_artifact_must_fail_schedule(self):
        raw=(ROOT/".github/workflows/pi-flr-watch.yml").read_text(encoding="utf-8")
        mutated=raw.replace("if-no-files-found: error", "if-no-files-found: warn")
        with self.assertRaisesRegex(watch.WatchError,"WATCH_MISSING_RECEIPT_NOT_FATAL"):
            watch.validate_workflow_contract(mutated)

    def test_disable_watcher_schedule_detected(self):
        raw=(ROOT/".github/workflows/pi-flr-watch.yml").read_text(encoding="utf-8")
        with self.assertRaisesRegex(watch.WatchError,"WATCH_SCHEDULE_NOT_DECLARED"):
            watch.validate_workflow_contract(raw.replace("17 * * * *","0 0 * * *"))

    def test_watch_only_public_evidence_links(self):
        out=watch.build_report([run(101)],{101:[job(501)]},now=NOW)
        self.assertEqual(out["groups"][0]["evidence_run_urls"][0],
                         "https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/101")


if __name__=="__main__":
    unittest.main()
