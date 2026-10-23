#!/usr/bin/env python3
"""PI-FLR watch: bounded, read-only failure and schedule-observability signals.

Failure step ≠ diagnosed root cause. Green after red ≠ proven remedy.
An hourly cron declaration ≠ an observed hourly execution cadence.
Never reads Gmail, downloads logs, changes issues/commits, or closes cases.
Only public numeric IDs, hash fingerprints and fixed allowlisted labels are exported.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPO = "gmodrasa7-rgb/project-intersection-public"
API = "https://api.github.com/repos/" + REPO
WATCH_NAME = "PI-FLR read-only failure signal watch"
SCHEDULE_DECLARED_MINUTES = 60
SCHEDULE_ATTENTION_THRESHOLD_MINUTES = 120
KNOWN = {
    "PI-RISE synthetic-only integrity": ("PI_RISE", ["FLR-0002", "FLR-0005"]),
    "Public English/Korean language separation": ("LANGUAGE", ["FLR-0001", "FLR-0006"]),
    "Public repository governance audit": ("GOVERNANCE", ["FLR-0007"]),
    "PI-FLR recursive failure learning integrity": ("PI_FLR", []),
}
FAIL = {"failure", "timed_out", "startup_failure", "action_required"}
MAX_RUNS = 160
MAX_FAILED_RUNS = 32
MAX_GROUP_EVIDENCE = 8
MAX_AGE_HOURS = 48
OUT = Path("pi_flr_watch_report.json")


class WatchError(ValueError):
    pass


def _require(condition, code):
    if not condition:
        raise WatchError(code)


def _utc(value):
    _require(isinstance(value, str), "RUN_TIMESTAMP_MISSING")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise WatchError("RUN_TIMESTAMP_INVALID") from None
    _require(dt.tzinfo is not None, "RUN_TIMESTAMP_TIMEZONE_MISSING")
    return dt.astimezone(timezone.utc)


def _number(value):
    _require(type(value) is int and value > 0, "INVALID_PUBLIC_GITHUB_ID")
    return value


def _signal(workflow_id, job_name, step_name, branch=""):
    # Never emit arbitrary job/step text: labels could carry secrets or PII.
    data = json.dumps([_number(workflow_id), str(job_name), str(step_name), str(branch)],
                      ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def _family(name):
    return KNOWN.get(name, ("OTHER_UNCLASSIFIED", []))


def schedule_observability(runs, *, now, limit_reached=False):
    """Report observed start gaps, not assumed missed cron triggers or their cause.

    A self-monitor cannot prove its own future liveness. The GitHub run-list
    sample may be truncated, and even a green watcher job says nothing about
    the intended number of schedule events that GitHub never created.
    """
    moment = _utc(now)
    cutoff = moment - timedelta(hours=MAX_AGE_HOURS)
    observed = []
    for run in runs:
        if not (run.get("name") == WATCH_NAME
                and run.get("event") == "schedule"
                and run.get("head_branch") == "main"):
            continue
        _number(run.get("id"))
        started = _utc(run.get("created_at"))
        _require(started <= moment + timedelta(minutes=5), "RUN_IN_FUTURE")
        if started >= cutoff:
            observed.append(started)
    observed.sort()
    gaps = [(b-a).total_seconds()/60 for a, b in zip(observed, observed[1:])]
    largest = round(max(gaps), 2) if gaps else None
    age = round(max(0, (moment-observed[-1]).total_seconds()/60), 2) if observed else None
    over_threshold = ((largest is not None and largest > SCHEDULE_ATTENTION_THRESHOLD_MINUTES)
                      or (age is not None and age > SCHEDULE_ATTENTION_THRESHOLD_MINUTES))
    if over_threshold:
        state = "OBSERVED_GAP_OR_STALENESS"
    elif limit_reached:
        state = "UNKNOWN_TRUNCATED_RUN_SAMPLE"
    elif len(observed) < 2:
        state = "UNKNOWN_INSUFFICIENT_SCHEDULE_RUNS"
    else:
        state = "NO_EXCESS_GAP_IN_BOUNDED_SAMPLE"
    return {
        "state": state,
        "declared_interval_minutes": SCHEDULE_DECLARED_MINUTES,
        "attention_threshold_minutes": SCHEDULE_ATTENTION_THRESHOLD_MINUTES,
        "sample_window_hours": MAX_AGE_HOURS,
        "observed_scheduled_run_count": len(observed),
        "latest_observed_start_utc": observed[-1].isoformat() if observed else None,
        "minutes_since_latest_observed_start": age,
        "largest_observed_interrun_gap_minutes": largest,
        "scheduler_cause": "UNKNOWN",
        "independent_heartbeat_verified": False,
        "no_guarantee_of_complete_execution_history": True,
    }


def build_report(runs, jobs_by_run, *, now, limit_reached=False):
    """Pure offline classifier: run metadata + failed step; no log/body access."""
    moment = _utc(now)
    cutoff = moment - timedelta(hours=MAX_AGE_HOURS)
    _require(isinstance(runs, list) and isinstance(jobs_by_run, dict),
             "BAD_INPUT_SHAPE")
    groups = {}
    seen_run_ids = set()
    relevant = []
    rejected_count = 0
    unseen_rerun_history = 0
    for run in runs:
        rid = _number(run.get("id"))
        _require(rid not in seen_run_ids, "DUPLICATE_RUN_ID")
        seen_run_ids.add(rid)
        ts = _utc(run.get("created_at"))
        if ts > moment + timedelta(minutes=5):
            raise WatchError("RUN_IN_FUTURE")
        if ts < cutoff:
            continue
        if run.get("status") != "completed":
            continue
        attempts = run.get("run_attempt", 1)
        _require(type(attempts) is int and attempts >= 1, "INVALID_RUN_ATTEMPT")
        unseen_rerun_history += max(0, attempts - 1)
        workflow_id = _number(run.get("workflow_id"))
        family, hints = _family(run.get("name"))
        relevant.append((run, ts, family, hints))
        if run.get("conclusion") not in FAIL:
            continue
        _require(rid in jobs_by_run, "MISSING_FAILED_RUN_JOB_DETAILS")
        jobs = jobs_by_run[rid]
        _require(isinstance(jobs, list), "INVALID_JOB_LIST")
        had_failed_step = False
        branch = run.get("head_branch")
        _require(isinstance(branch, str) and bool(branch),
                 "FAILURE_BRANCH_NOT_IDENTIFIABLE")
        fail_finished = _utc(run["updated_at"]) if run.get("updated_at") else None
        for job in jobs:
            if job.get("conclusion") not in FAIL:
                continue
            _number(job.get("id"))
            failures = [s for s in job.get("steps", [])
                        if s.get("conclusion") in FAIL]
            if not failures:
                failures = [{"name": "UNKNOWN_STEP"}]
            for step in failures:
                had_failed_step = True
                signature = _signal(workflow_id, job.get("name", ""),
                                    step.get("name", ""), branch)
                current = groups.setdefault(signature, {
                    "fingerprint_sha256": signature,
                    "workflow_family": family,
                    "root_cause_status": "UNKNOWN_NEEDS_JOB_LOG_AND_CAUSAL_REVIEW",
                    "suggested_related_cases_not_proven": hints,
                    "run_ids": [],
                    "last_failure_utc": "",
                    "subsequent_success_same_workflow_and_branch": False,
                    "_workflow_id": workflow_id,
                    "_branch": branch,
                    "_last_fail_dt": ts,
                    "_last_fail_finished": fail_finished,
                })
                if rid not in current["run_ids"]:
                    current["run_ids"].append(rid)
                if ts > current["_last_fail_dt"]:
                    current["_last_fail_dt"] = ts
                    current["last_failure_utc"] = ts.isoformat()
                    current["_branch"] = branch
                    current["_last_fail_finished"] = fail_finished
                elif not current["last_failure_utc"]:
                    current["last_failure_utc"] = ts.isoformat()
        if not had_failed_step:
            rejected_count += 1
            # A workflow-level failure without job details must remain visible.
            signature = _signal(workflow_id, "UNKNOWN_JOB",
                                "FAILED_RUN_WITHOUT_FAILED_JOB_DETAIL", branch)
            current = groups.setdefault(signature, {
                "fingerprint_sha256": signature,
                "workflow_family": family,
                "root_cause_status": "UNCLASSIFIED_FAILED_RUN_NEEDS_MANUAL_REVIEW",
                "suggested_related_cases_not_proven": hints,
                "run_ids": [],
                "last_failure_utc": ts.isoformat(),
                "subsequent_success_same_workflow_and_branch": False,
                "_workflow_id": workflow_id,
                "_branch": branch,
                "_last_fail_dt": ts,
                "_last_fail_finished": fail_finished,
            })
            if rid not in current["run_ids"]:
                current["run_ids"].append(rid)
            if ts > current["_last_fail_dt"]:
                current["_last_fail_dt"] = ts
                current["_last_fail_finished"] = fail_finished
                current["last_failure_utc"] = ts.isoformat()
    for group in groups.values():
        for run, ts, _, _ in relevant:
            if (run.get("conclusion") == "success"
                    and run.get("workflow_id") == group["_workflow_id"]
                    and run.get("head_branch") == group["_branch"]
                    and group["_last_fail_finished"] is not None
                    and run.get("run_started_at") is not None
                    and _utc(run["run_started_at"]) > group["_last_fail_finished"]):
                group["subsequent_success_same_workflow_and_branch"] = True
        group["run_count"] = len(group["run_ids"])
        # Dedup by actual run IDs, even if several jobs had same step signature.
        group["run_ids"].sort(reverse=True)
        group["evidence_run_urls"] = [
            f"https://github.com/{REPO}/actions/runs/{i}"
            for i in group["run_ids"][:MAX_GROUP_EVIDENCE]
        ]
        del group["_workflow_id"]
        del group["_branch"]
        del group["_last_fail_dt"]
        del group["_last_fail_finished"]
        group["resolution_status"] = "NOT_AUTOMATICALLY_CLOSED"
        group["subsequent_green_is_not_proof_of_repair"] = True

    public_groups = sorted(groups.values(),
                           key=lambda g: (-g["run_count"], g["fingerprint_sha256"]))
    return {
        "schema": "PI-FLR-WATCH/0.3.0",
        "scope": "RECENT_BOUNDED_GITHUB_ACTIONS_METADATA_ONLY",
        "repository": REPO,
        "window_hours": MAX_AGE_HOURS,
        "observed_at_utc": moment.isoformat(),
        "scanned_completed_runs": len(relevant),
        "failed_run_without_failed_job_step": rejected_count,
        "prior_attempts_not_inspected": unseen_rerun_history,
        "failure_fingerprint_count": len(public_groups),
        "observation_coverage": (
            "PARTIAL_LIMIT_REACHED" if limit_reached else
            "PARTIAL_PRIOR_RERUN_ATTEMPTS_UNINSPECTED" if unseen_rerun_history else
            "BOUNDED_WINDOW_NOT_FULL_REPOSITORY_HISTORY"),
        "no_emails_or_raw_logs_exported": True,
        "automatic_closure_enabled": False,
        "schedule_observability": schedule_observability(
            runs, now=now, limit_reached=limit_reached),
        "groups": public_groups,
    }


def validate_workflow_contract(text):
    _require("name: PI-FLR read-only failure signal watch" in text,
             "WATCH_WORKFLOW_NAME_MISSING")
    _require(re.search(r"(?m)^  schedule:\s*$", text) is not None
             and re.search(r"(?m)^    - cron: ['\"]17 \* \* \* \*['\"]", text) is not None,
             "WATCH_SCHEDULE_NOT_DECLARED")
    _require("workflow_dispatch:" in text, "WATCH_MANUAL_TRIGGER_MISSING")
    _require("  push:\n    branches: [main]" in text and
             "'tools/pi_flr_watch.py'" in text and
             "'tests/test_pi_flr_watch.py'" in text,
             "WATCH_MAIN_SMOKE_TRIGGER_MISSING")
    # Parse the actual top-level permissions block, not unrelated strings
    # or comments elsewhere. Every unrecognized or write-scoped key fails closed.
    _require(text.count("permissions:") == 1 and
             re.search(r"(?m)^[ ]{4,}permissions:", text) is None,
             "WATCH_NOT_READ_ONLY")
    permission_match = re.search(
        r"(?m)^permissions:[ \t]*\n((?:[ \t]+[^\n]*\n)*)", text)
    _require(permission_match is not None, "WATCH_NOT_READ_ONLY")
    perms = [line.strip() for line in permission_match.group(1).splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    _require(sorted(perms) == ["actions: read", "contents: read"],
             "WATCH_NOT_READ_ONLY")
    _require("if-no-files-found: error" in text,
             "WATCH_MISSING_RECEIPT_NOT_FATAL")
    _require("python3 -m unittest discover -s tests -p 'test_pi_flr_watch.py'" in text,
             "WATCH_SELF_TEST_MISSING")
    _require("python3 tools/pi_flr_watch.py" in text, "WATCH_SCAN_NOT_EXECUTED")
    return True


def _get_json(endpoint, token):
    _require(bool(token), "GITHUB_TOKEN_MISSING")
    _require(endpoint.startswith(API + "/"), "OUTSIDE_REPO_API")
    req = Request(endpoint, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + token,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "PI-FLR-ReadOnly-Watch/0.2.1",
    })
    try:
        with urlopen(req, timeout=20) as response:
            _require(response.status == 200, "GITHUB_API_NON_200")
            return json.loads(response.read(3_000_000).decode("utf-8"))
    except (HTTPError, URLError) as exc:
        # Deliberately do not print exception strings/headers: may contain URLs or secrets.
        raise WatchError("GITHUB_API_UNAVAILABLE_OR_ACCESS_DENIED") from None


def scan_github(token, *, now):
    collected = []
    reached = False
    cutoff = _utc(now) - timedelta(hours=MAX_AGE_HOURS)
    # Bounded pages and bounded job requests. No failed job logs ingested.
    for page in (1, 2):
        query = urlencode({"per_page": 100, "page": page})
        payload = _get_json(API + "/actions/runs?" + query, token)
        items = payload.get("workflow_runs")
        _require(type(items) is list, "GITHUB_RUNS_MALFORMED")
        for item in items:
            if len(collected) >= MAX_RUNS:
                reached = True
                break
            collected.append(item)
        if reached or len(items) < 100:
            break
    targets = [r for r in collected
               if _utc(r["created_at"]) >= cutoff
               and r.get("status") == "completed"
               and r.get("conclusion") in FAIL]
    if len(targets) > MAX_FAILED_RUNS:
        reached = True
        targets = targets[:MAX_FAILED_RUNS]
    job_lists = {}
    for run in targets:
        rid = _number(run["id"])
        response = _get_json(API + f"/actions/runs/{rid}/jobs?per_page=100", token)
        jobs = response.get("jobs")
        _require(isinstance(jobs, list), "FAILED_RUN_JOBS_NOT_READ")
        _require(response.get("total_count", len(jobs)) <= len(jobs),
                 "FAILED_RUN_JOBS_TRUNCATED")
        job_lists[rid] = jobs
    # If capped, exclude uninspected failures to avoid claiming they were checked.
    retained = [r for r in collected if r.get("conclusion") not in FAIL
                or r["id"] in job_lists]
    return build_report(retained, job_lists, now=now, limit_reached=reached)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", default=str(OUT))
    opts = p.parse_args()
    try:
        token = os.environ.get("GITHUB_TOKEN", "")
        now = datetime.now(timezone.utc).isoformat()
        report = scan_github(token, now=now)
        out = Path(opts.output)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
        print(json.dumps({k: v for k, v in report.items() if k != "groups"},
                         ensure_ascii=False, sort_keys=True))
        if report["schedule_observability"]["state"] == "OBSERVED_GAP_OR_STALENESS":
            print("::warning title=PI-FLR schedule observability::"
                  "Observed scheduled-run gap or stale start exceeds 120 minutes; "
                  "cause unknown, no independent heartbeat.")
        print("No automatic repair, case closure, private email export or root-cause inference.")
    except (WatchError, ValueError, OSError, KeyError, TypeError) as exc:
        print("PI_FLR_WATCH_FAIL:" + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
