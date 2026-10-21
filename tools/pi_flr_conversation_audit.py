#!/usr/bin/env python3
"""PI-FLR conversation evidence ledger: bounded, append-only, falsifiable.

A transcript search is not a complete historical chat export. This validates
provenance labels and guards the distinction between partial CI and release readiness.
It does NOT call models, connect to private chats, or prove causal mechanisms.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LEDGER = "knowledge/PI_FLR_CONVERSATION_AUDIT_V0_1_0_EN_KO.json"
REGISTRY = "knowledge/PI_FLR_CASES_V0_1_0.json"
RECORD_FIELDS = {"id", "family", "evidence_class", "title_en", "title_ko",
                 "observation", "causal_hypothesis", "competing_explanation",
                 "preventive_test", "linked_flr", "public_evidence"}
EVIDENCE_CLASSES = {"GITHUB_LOG_CONFIRMED", "PUBLIC_CASE_DOCUMENTED",
                    "CONVERSATION_SUMMARY_REPORTED", "HYPOTHESIS_ONLY"}
RELEASE_OK = {"success"}
RELEASE_BAD = {"failure", "cancelled", "timed_out", "startup_failure",
               "action_required", "skipped", "neutral"}
RELEASE_PENDING = {"queued", "in_progress", "requested", "waiting", "pending"}
REGISTRY_RE = re.compile(r"^FLR-\d{4}$")
RECORD_RE = re.compile(r"^FLC-\d{3}$")
PRIVATE_PATTERN = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|(?:sk-|ghp_)[A-Za-z0-9]{12,}")


class ConversationAuditError(ValueError):
    pass


def require(condition, code):
    if not condition:
        raise ConversationAuditError(code)


def validate_release_matrix(runs, expected):
    """Never infer full readiness from a single green check or a merged PR."""
    require(isinstance(runs, list) and isinstance(expected, list)
            and bool(expected) and len(expected) == len(set(expected)),
            "RELEASE_MATRIX_INPUT_INVALID")
    require(all(isinstance(x, dict) and set(x) == {"name", "conclusion"}
                and isinstance(x["name"], str) and isinstance(x["conclusion"], str)
                for x in runs), "RELEASE_MATRIX_ROW_INVALID")
    names = [x["name"] for x in runs]
    require(len(names) == len(set(names)), "DUPLICATE_WORKFLOW_RESULT")
    require(all(x["conclusion"] in RELEASE_OK | RELEASE_BAD | RELEASE_PENDING
                for x in runs), "UNKNOWN_WORKFLOW_CONCLUSION")
    missing = sorted(set(expected) - set(names))
    failed = sorted(x["name"] for x in runs if x["conclusion"] in RELEASE_BAD)
    pending = sorted(x["name"] for x in runs if x["conclusion"] in RELEASE_PENDING)
    extra = sorted(set(names) - set(expected))
    require(not extra, "UNDECLARED_WORKFLOW_RESULT")
    status = ("BLOCKED_FAILED" if failed else
              "INCOMPLETE_UNOBSERVED" if missing else
              "INCOMPLETE_PENDING" if pending else "SCOPED_ALL_PASS")
    return {"status": status, "ready": status == "SCOPED_ALL_PASS",
            "missing": missing, "failed": failed, "pending": pending,
            "scope": "DECLARED_WORKFLOW_SET_ONLY_NOT_BRANCH_PROTECTION"}


def validate(data, registry):
    required = {"registry_id", "schema_version", "release_version", "as_of",
                "title_en", "title_ko", "language_order", "status", "coverage",
                "evidence_policy", "overview_en", "overview_ko",
                "records", "next_cycle"}
    require(type(data) is dict and set(data) == required, "LEDGER_SCHEMA_DRIFT")
    require(data["registry_id"] == "PI-FLR-CONVERSATION-AUDIT"
            and data["schema_version"] == "0.1.0", "LEDGER_IDENTITY_CHANGED")
    require(data["language_order"] == ["English primary", "Korean secondary"],
            "ENGLISH_FIRST_RULE_VIOLATED")
    require(data["status"] == "PARTIAL_ACCESS_NOT_ALL_CHAT_TRANSCRIPTS",
            "FALSE_FULL_CHAT_AUDIT_CLAIM")
    require(data["coverage"]["denominator"] == "UNKNOWN_ALL_CHATS_UNAVAILABLE"
            and data["coverage"]["missing_records_not_zero"] is True
            and data["coverage"]["not_verified"], "UNKNOWN_HISTORY_WAS_ERASED")
    require(data["coverage"]["personally_identifying_or_private_financial_information"]
            == "EXCLUDED", "PRIVATE_INFORMATION_EXPOSURE_CONTRACT")
    require(re.fullmatch(r"\d+\.\d+\.\d+", data["release_version"]) is not None,
            "INVALID_RELEASE_VERSION")
    require(data["as_of"] >= "2026-10-22", "STALE_LEDGER_AS_OF")
    require(type(registry) is dict and registry.get("registry_id") == "PI-FLR",
            "PARENT_FLR_MISSING")
    known = {case["id"] for case in registry["cases"]}
    ids = set()
    for r in data["records"]:
        require(type(r) is dict and set(r) == RECORD_FIELDS, "PATTERN_FIELDS_INVALID")
        require(type(r["id"]) is str and RECORD_RE.fullmatch(r["id"])
                and r["id"] not in ids, "INVALID_OR_DUPLICATE_PATTERN_ID")
        ids.add(r["id"])
        require(r["evidence_class"] in EVIDENCE_CLASSES,
                "INCORRECT_EVIDENCE_GRADE")
        for k in ("family", "title_en", "title_ko", "observation",
                  "causal_hypothesis", "competing_explanation", "preventive_test"):
            require(type(r[k]) is str and len(r[k]) >= 8,
                    "INSUFFICIENT_PATTERN_FIELD:" + k)
        require(type(r["public_evidence"]) is list and bool(r["public_evidence"]),
                "MISSING_PUBLIC_PROVENANCE")
        for url in r["public_evidence"]:
            parts = urlsplit(url)
            require(parts.scheme == "https" and parts.netloc == "github.com"
                    and parts.path.startswith(
                        "/gmodrasa7-rgb/project-intersection-public/"),
                    "UNVERIFIED_EXTERNAL_EVIDENCE_DOMAIN")
        require(type(r["linked_flr"]) is list and
                set(r["linked_flr"]) <= known and
                len(r["linked_flr"]) == len(set(r["linked_flr"])),
                "INVALID_CANONICAL_FLR_CROSSWALK")
        if r["evidence_class"] == "GITHUB_LOG_CONFIRMED":
            require(any("/actions/runs/" in url for url in r["public_evidence"]),
                    "LOG_CONFIRMED_WITHOUT_A_RUN_RECEIPT")
        if r["evidence_class"] == "CONVERSATION_SUMMARY_REPORTED":
            require("summary" in data["evidence_policy"][
                        "CONVERSATION_SUMMARY_REPORTED"].lower(),
                    "CONVERSATION_MEMORY_FALSELY_CERTIFIED")
    require(ids, "EMPTY_CONVERSATION_AUDIT")
    require(list(data["evidence_policy"]) == [
        "GITHUB_LOG_CONFIRMED", "PUBLIC_CASE_DOCUMENTED",
        "CONVERSATION_SUMMARY_REPORTED", "HYPOTHESIS_ONLY", "absence",
        "append_only"], "EVIDENCE_POLICY_MUTATED")
    require("OBSERVE" in data["next_cycle"]["sequence"]
            and "REOPEN_IF_RECURRENT" in data["next_cycle"]["sequence"]
            and "DEDUP_WITH_FLR_AND_F_R" in data["next_cycle"]["sequence"],
            "RECURSIVE_LOOP_OR_DEDUP_MISSING")
    public = json.dumps(data, ensure_ascii=False)
    require(PRIVATE_PATTERN.search(public) is None, "PRIVATE_IDENTIFIER_IN_PUBLIC_LEDGER")
    return {"status": "BOUNDED_AUDIT_VALID_NOT_EXHAUSTIVE",
            "patterns": len(ids), "parent_flr_cases": len(known),
            "unobserved_history": "UNKNOWN"}


def compare_history(new, old):
    require(old.get("registry_id") == "PI-FLR-CONVERSATION-AUDIT",
            "INVALID_HISTORICAL_BASELINE")
    past = {r["id"]: r for r in old["records"]}
    present = {r["id"]: r for r in new["records"]}
    require(set(past) <= set(present), "HISTORICAL_PATTERN_DELETED")
    for key, before in past.items():
        require(present[key] == before, "HISTORICAL_PATTERN_MUTATED:" + key)
    require(new["coverage"]["denominator"] == old["coverage"]["denominator"],
            "UNKNOWN_CHAT_DENOMINATOR_SILENTLY_REWRITTEN")
    if new["release_version"] == old["release_version"]:
        require(new == old, "UNVERSIONED_AUDIT_CHANGE")
    else:
        require(tuple(map(int, new["release_version"].split("."))) >
                tuple(map(int, old["release_version"].split("."))),
                "NON_MONOTONIC_AUDIT_VERSION")
        require(new["records"] != old["records"] or
                new["next_cycle"] != old["next_cycle"],
                "EMPTY_AUDIT_VERSION_BUMP")
    return True


def baseline_from_git(commit):
    if not commit or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        return None
    p = subprocess.run(["git", "show", commit + ":" + LEDGER],
                       cwd=ROOT, capture_output=True, text=True, check=False)
    if p.returncode:
        return None  # file introduced on this branch: no historical baseline
    return json.loads(p.stdout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-commit", default="")
    args = parser.parse_args()
    try:
        data = json.loads((ROOT / LEDGER).read_text(encoding="utf-8"))
        registry = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
        report = validate(data, registry)
        old = baseline_from_git(args.baseline_commit)
        if old is not None:
            compare_history(data, old)
            report["historical_integrity"] = "APPEND_ONLY_VERIFIED"
        else:
            report["historical_integrity"] = "BASELINE_ABSENT_OR_UNVERIFIED"
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise SystemExit("PI_FLR_CONVERSATION_AUDIT_FAIL:" + str(e)) from None


if __name__ == "__main__":
    main()
