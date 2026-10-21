"""Offline PI-SIGNAL regression checks; synthetic inputs only."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_signal_reconcile as signal


def run(i, workflow="PI-RISE synthetic-only integrity", branch="ops/test", sha="a", conclusion="failure", time="2026-10-20T19:00:00Z"):
    return {"id": i, "name": workflow, "head_branch": branch,
            "head_sha": sha * 40, "conclusion": conclusion, "created_at": time}


def alert(workflow="PI-RISE synthetic-only integrity", sha="a", prefix="Run failed:"):
    return {"subject": f"[owner/repo] {prefix} {workflow} - ops/test ({sha * 7})"}


class SignalTests(unittest.TestCase):
    def check(self, runs, emails):
        return signal.reconcile({"workflow_runs": runs}, {"emails": emails})

    def test_old_failure_followed_by_green_same_branch_workflow(self):
        x = self.check([run(1), run(2, sha="b", conclusion="success", time="2026-10-20T19:01:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "SUPERSEDED_BY_SUCCESS_IN_SAMPLE")
        self.assertTrue(x["later_success_does_not_prove_permanent_repair"])

    def test_success_on_another_branch_cannot_clear_failure(self):
        x = self.check([run(1), run(2, branch="main", sha="b", conclusion="success", time="2026-10-20T19:01:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "FAILURE_OBSERVED_IN_SAMPLE")

    def test_success_on_another_workflow_cannot_clear_failure(self):
        x = self.check([run(1), run(2, workflow="Public repository governance audit", sha="b", conclusion="success", time="2026-10-20T19:01:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "FAILURE_OBSERVED_IN_SAMPLE")

    def test_same_commit_two_distinct_runs_ambiguous(self):
        x = self.check([run(1), run(2, time="2026-10-20T19:01:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "AMBIGUOUS_RUN_MATCH")
        self.assertIsNone(x["clusters"][0]["run_id"])

    def test_email_duplicates_compress_without_false_independent_evidence(self):
        x = self.check([run(1)], [alert(), alert(), alert()])
        self.assertEqual(x["mail_signals"], 3)
        self.assertEqual(x["unique_alert_clusters"], 1)
        self.assertEqual(x["clusters"][0]["notifications"], 3)

    def test_pr_title_is_not_confused_with_branch_name(self):
        email = alert(prefix="PR run failed:")
        email["subject"] = email["subject"].replace("ops/test", "PI-RISE changeset - funding guard")
        x = self.check([run(1)], [email])
        self.assertEqual(x["clusters"][0]["run_id"], 1)

    def test_sample_has_no_matching_run(self):
        x = self.check([], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "UNMATCHED_UNKNOWN")

    def test_newer_pending_not_success(self):
        x = self.check([run(1), run(2, sha="b", conclusion=None, time="2026-10-20T19:01:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "NEWER_NON_SUCCESS_IN_SAMPLE")

    def test_irrelevant_mail_not_parsed_as_ci_alert(self):
        x = self.check([], [{"subject": "Funding approval: action required"}])
        self.assertEqual(x["unique_alert_clusters"], 0)

    def test_timestamps_compared_as_aware_utc(self):
        x = self.check([run(1, time="2026-10-20T20:00:00+01:00"),run(2, sha="b", conclusion="success", time="2026-10-20T19:30:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "SUPERSEDED_BY_SUCCESS_IN_SAMPLE")

    def test_reject_duplicate_run_ids(self):
        with self.assertRaisesRegex(ValueError, "INVALID_RUN_IDENTITY"):
            self.check([run(1), run(1, sha="b")], [alert()])

    def test_reject_missing_time_zone(self):
        with self.assertRaisesRegex(ValueError, "UNTRUSTED_RUN_TIME"):
            self.check([run(1,time="2026-10-20T19:00:00")], [alert()])

    def test_reject_invalid_sha(self):
        with self.assertRaisesRegex(ValueError, "INVALID_RUN_IDENTITY"):
            self.check([run(1, sha="z")], [alert()])

    def test_rerun_same_id_now_success_requires_conflict_boundary(self):
        x = self.check([run(1, conclusion="success")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"],
                         "ALERT_CONFLICT_OR_RERUN_SUCCESS_IN_SAMPLE")

    def test_newer_failure_is_not_treated_as_original_failure(self):
        x = self.check([run(1), run(2, sha="b", conclusion="failure", time="2026-10-20T19:01:00Z")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "NEWER_FAILURE_IN_SAMPLE")

    def test_same_time_uses_run_id_tiebreaker(self):
        x = self.check([run(1), run(2, sha="b", conclusion="success")], [alert()])
        self.assertEqual(x["clusters"][0]["verdict"], "SUPERSEDED_BY_SUCCESS_IN_SAMPLE")

if __name__ == "__main__":
    unittest.main()
