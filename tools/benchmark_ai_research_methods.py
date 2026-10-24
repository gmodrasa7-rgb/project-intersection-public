#!/usr/bin/env python3
"""Five-method-inspired PI operational baseline; never a benchmark of external AIs.

Runs existing, read-only checks on the current checkout and makes failures
visible.  Neither scientific replication nor independent blind evaluation.
Requires only Python 3.12 standard library.  Makes no network requests.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    ("literature_identity", ("tools/audit_prior_art_c01_c12_identity.py",)),
    ("source_traceability", ("tools/audit_claim_source_lock.py", "--self-test")),
    ("question_routing", ("tools/pi_context_route_v02.py", "--selftest")),
    ("failure_registry", ("tools/pi_flr_audit.py",)),
    ("whole_repo_unit_tests", ("-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py")),
    ("first_view_contract", ("tools/check_readme_l0.py",)),
    ("publication_manifest", ("tools/pi_rise_manifest_guard.py",)),
)


def command_for(arguments: tuple[str, ...]) -> list[str]:
    return [sys.executable, *arguments]


def result_summary(name: str, returncode: int, stdout: str, stderr: str) -> dict:
    """Interpret execution status without upgrading a structural pass to science."""
    message = (stdout + "\n" + stderr).strip()
    state = "PASS" if returncode == 0 else "FAIL"
    if "GITHUB_TOKEN_MISSING" in message:
        state = "BLOCKED_AUTH"
    record: dict = {"status": state, "returncode": returncode}
    if name == "literature_identity":
        m = re.search(r"records=(\d+), DOI=(\d+), alternative ID=(\d+), title-review pairs=(\d+)", message)
        if m:
            record.update(zip(("records", "doi_records", "alternative_id_records", "title_review_pairs"),
                              map(int, m.groups())))
    elif name == "source_traceability":
        m = re.search(r"negative controls: (\d+)/(\d+) detected", message)
        if m:
            record["preset_mutations_detected"] = int(m.group(1))
            record["preset_mutations_total"] = int(m.group(2))
    elif name == "question_routing" and state == "PASS":
        try:
            data = json.loads(stdout)
            for key in ("queries", "gold_family_instances", "legacy_family_covered",
                        "v02_family_covered", "v02_cases_explicitly_reporting_incompleteness"):
                record[key] = data[key]
            record["blind_validation"] = data["independent_blind_validation"]
            record["actual_retrieval"] = data["actual_library_retrieval"]
        except (ValueError, KeyError, TypeError):
            record["parse_error"] = "ROUTE_REPORT_UNREADABLE"
            record["status"] = "FAIL"
    elif name == "failure_registry" and state == "PASS":
        try:
            data = json.loads(stdout)
            record.update({key: data[key] for key in ("cases", "controls", "history_check", "boundary")})
        except (ValueError, KeyError, TypeError):
            record["parse_error"] = "FLR_REPORT_UNREADABLE"
            record["status"] = "FAIL"
    elif name == "whole_repo_unit_tests":
        count = re.search(r"Ran (\d+) tests", message)
        if count:
            record["tests_run"] = int(count.group(1))
        failures = re.search(r"FAILED \(([^)]+)\)", message)
        if failures:
            record["failure_summary"] = failures.group(1)
    if state != "PASS":
        record["diagnostic"] = " | ".join(message.splitlines()[-3:])[:500]
    return record


def benchmark(root: Path = ROOT) -> dict:
    checks = {}
    for name, arguments in CHECKS:
        completed = subprocess.run(command_for(arguments), cwd=root, text=True,
                                   capture_output=True, check=False, timeout=60)
        checks[name] = result_summary(name, completed.returncode,
                                      completed.stdout, completed.stderr)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root,
                            text=True, capture_output=True, check=False)
    return {
        "schema": "pi-ai-research-method-benchmark/v0.1",
        "commit": commit.stdout.strip() if commit.returncode == 0 else "UNKNOWN",
        "classification": "SAME_REPO_DETERMINISTIC_OPERATIONAL_PREFLIGHT_NOT_EXTERNAL_AI_COMPARISON",
        "overall": "PASS_ALL_SCOPED_CHECKS" if all(x["status"] == "PASS" for x in checks.values())
                   else "EXISTING_FAILURES_OR_BLOCKERS_VISIBLE",
        "checks": checks,
        "not_measured": ["external AI capability", "citation claim faithfulness",
                         "independent blind accuracy", "real-world coexistence",
                         "human research hours", "net cost savings", "recurrent failure reduction"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-only", action="store_true",
                        help="return zero while still printing all detected failures")
    args = parser.parse_args()
    data = benchmark()
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
    if data["overall"] != "PASS_ALL_SCOPED_CHECKS" and not args.report_only:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
