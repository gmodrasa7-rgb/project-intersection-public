#!/usr/bin/env python3
"""PI-SIGNAL v0.1.0 — offline correlation of GitHub CI and Gmail notifications.

Scope: observable provider metadata only; no API/network, raw mail, secrets,
finances, automated mail actions, or permanent-repair claims.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

VERSION = "0.1.1"
FAIL_MAIL = re.compile(
    r"^\[[^\]]+\]\s+(?:PR\s+)?Run failed:\s+(.+?)\s+-\s+.+\s+\(([0-9a-fA-F]{7,40})\)$",
    flags=re.IGNORECASE,
)
SAFE_SHA = re.compile(r"^[a-f0-9]{7,40}$")


def _time(value):
    if not isinstance(value, str):
        raise ValueError("UNTRUSTED_RUN_TIME")
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError("missing timezone")
        return stamp.astimezone(timezone.utc)
    except ValueError as exc:
        raise ValueError("UNTRUSTED_RUN_TIME") from exc


def _run_records(source):
    if not isinstance(source, dict) or not isinstance(source.get("workflow_runs"), list):
        raise ValueError("INVALID_GITHUB_RUNS_PAYLOAD")
    seen = set()
    out = []
    for x in source["workflow_runs"]:
        if not isinstance(x, dict):
            raise ValueError("INVALID_GITHUB_RUN")
        try:
            rid = x["id"]
            name = x["name"]
            branch = x["head_branch"]
            sha = x["head_sha"].lower()
            conclusion = x.get("conclusion")
            timestamp = _time(x["created_at"])
        except (KeyError, AttributeError, TypeError) as exc:
            raise ValueError("MISSING_RUN_IDENTITY") from exc
        if (type(rid) is not int or rid <= 0 or rid in seen
                or not isinstance(name, str) or not name.strip() or len(name) > 200
                or not isinstance(branch, str) or not branch or len(branch) > 250
                or not SAFE_SHA.fullmatch(sha) or len(sha) != 40
                or conclusion not in (None, "success", "failure", "cancelled", "skipped",
                                      "timed_out", "action_required", "neutral", "stale")):
            raise ValueError("INVALID_RUN_IDENTITY")
        seen.add(rid)
        out.append({"id": rid, "workflow": name, "branch": branch,
                    "sha": sha, "conclusion": conclusion, "time": timestamp})
    return out


def _mail_signals(source):
    if not isinstance(source, dict) or not isinstance(source.get("emails"), list):
        raise ValueError("INVALID_GMAIL_SUMMARIES_PAYLOAD")
    out = {}
    for x in source["emails"]:
        if not isinstance(x, dict) or not isinstance(x.get("subject"), str):
            raise ValueError("INVALID_GMAIL_MESSAGE")
        match = FAIL_MAIL.match(x["subject"])
        if match:
            workflow, prefix = match.group(1), match.group(2).lower()
            # A notification is not an authoritative run state. Deduplicate by
            # workflow/commit prefix, never by arrival time or email ID.
            key = (workflow, prefix)
            out[key] = out.get(key, 0) + 1
    return out


def reconcile(github_runs, gmail_summaries):
    runs = _run_records(github_runs)
    alerts = _mail_signals(gmail_summaries)
    latest = {}
    for r in runs:
        key = (r["branch"], r["workflow"])
        if key not in latest or (r["time"], r["id"]) > (latest[key]["time"], latest[key]["id"]):
            latest[key] = r
    clusters = []
    counts = {"SUPERSEDED_BY_SUCCESS_IN_SAMPLE": 0,
              "FAILURE_OBSERVED_IN_SAMPLE": 0,
              "ALERT_CONFLICT_OR_RERUN_SUCCESS_IN_SAMPLE": 0,
              "NEWER_FAILURE_IN_SAMPLE": 0,
              "NEWER_NON_SUCCESS_IN_SAMPLE": 0,
              "AMBIGUOUS_RUN_MATCH": 0,
              "UNMATCHED_UNKNOWN": 0}
    for (workflow, prefix), notifications in sorted(alerts.items()):
        matched = [r for r in runs if r["workflow"] == workflow and r["sha"].startswith(prefix)]
        if not matched:
            verdict, chosen = "UNMATCHED_UNKNOWN", None
        elif len(matched) != 1:
            # Two distinct run IDs can share the exact same commit/workflow
            # (push and PR); never guess which notification describes which.
            verdict, chosen = "AMBIGUOUS_RUN_MATCH", None
        else:
            chosen = matched[0]
            newest = latest[(chosen["branch"], chosen["workflow"])]
            if newest["id"] == chosen["id"]:
                verdict = ("FAILURE_OBSERVED_IN_SAMPLE" if newest["conclusion"] == "failure"
                           else "ALERT_CONFLICT_OR_RERUN_SUCCESS_IN_SAMPLE"
                           if newest["conclusion"] == "success"
                           else "NEWER_NON_SUCCESS_IN_SAMPLE")
            elif newest["conclusion"] == "success":
                verdict = "SUPERSEDED_BY_SUCCESS_IN_SAMPLE"
            elif newest["conclusion"] == "failure":
                verdict = "NEWER_FAILURE_IN_SAMPLE"
            else:
                verdict = "NEWER_NON_SUCCESS_IN_SAMPLE"
        counts[verdict] += 1
        clusters.append({"workflow": workflow, "commit_prefix": prefix,
                         "notifications": notifications,
                         "run_id": chosen["id"] if chosen else None,
                         "branch": chosen["branch"] if chosen else None,
                         "verdict": verdict})
    return {"schema": VERSION, "basis": "GITHUB_RUNS_SNAPSHOT_NOT_EXHAUSTIVE",
            "email_notification_is_not_current_run_state": True,
            "later_success_does_not_prove_permanent_repair": True,
            "mail_signals": sum(alerts.values()), "unique_alert_clusters": len(clusters),
            "run_records_in_sample": len(runs), "counts": counts, "clusters": clusters}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github-runs", type=Path, required=True)
    parser.add_argument("--gmail-summaries", type=Path, required=True)
    args = parser.parse_args()
    result = reconcile(json.loads(args.github_runs.read_text(encoding="utf-8")),
                       json.loads(args.gmail_summaries.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
