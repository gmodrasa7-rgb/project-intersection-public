#!/usr/bin/env python3
"""PI-FLR v0.1.0: public recursive failure-learning registry verifier.

No network, private records, finance certification, or scientific validation.
Built-in append-only baseline comparator makes changes auditable on each PR.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = "knowledge/PI_FLR_CASES_V0_1_0.json"
CI_PATH = ".github/workflows/pi-flr-integrity.yml"
VALID_CATEGORIES = {"PUBLICATION_CONTRACT", "REFERENCE_INTEGRITY", "GUARD_COVERAGE",
                    "DATA_INTEGRITY", "EVIDENCE_DRIFT", "ACCESS_CONTROL",
                    "REPRODUCIBILITY", "OTHER"}
VALID_EVENTS = {"FAILURE_OBSERVED", "ROOT_CAUSE_REVIEWED", "REPAIR_APPLIED",
                "CI_PASS_OBSERVED", "FIX_MERGED", "LIMITATION_RECORDED",
                "RECURRENCE_OBSERVED"}
CASE_FIELDS = {"id", "title_ko", "title_en", "category", "root_cause",
               "trigger", "observable", "impact", "counterfactual", "repair",
               "preventive_control_ids", "regression_test", "limitations", "events"}
EVENT_FIELDS = {"seq", "date", "kind", "evidence_url", "note"}
CONTROL_FIELDS = {"id", "title", "detector", "workflow", "mutation_test"}
VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
ISO_DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CASE_ID = re.compile(r"^FLR-\d{4}$")
CONTROL_ID = re.compile(r"^FLR-C\d{2,3}$")
TEST_ID = re.compile(r"^test_[a-z0-9_]+$")


class FLRError(ValueError):
    pass


def require(ok, reason):
    if not ok:
        raise FLRError(reason)


def version_tuple(v):
    require(isinstance(v, str) and VERSION.fullmatch(v) is not None,
            "INVALID_SEMVER")
    return tuple(int(x) for x in v.split("."))


def check_ci_contract(text):
    """Reject regressions that suppress the global FLR audit on ordinary PRs."""
    require(isinstance(text, str) and text.startswith("name: PI-FLR"),
            "INVALID_CI_WORKFLOW")
    match = re.search(r"^on:[ \t]*\n(.*?)(?=^[^\s#]|\Z)", text, flags=re.S | re.M)
    require(match is not None, "CI_TRIGGERS_NOT_DECLARED")
    triggers = match.group(1)
    require(re.search(r"(?m)^  pull_request:\s*$", triggers) is not None,
            "CI_MISSING_UNFILTERED_PULL_REQUEST")
    require(re.search(r"(?m)^  push:\s*$", triggers) is not None and
            re.search(r"(?m)^    branches: \[main\]\s*$", triggers) is not None,
            "CI_MISSING_MAIN_PUSH")
    require("paths:" not in triggers and "paths-ignore:" not in triggers and
            "branches-ignore:" not in triggers, "CI_PATH_OR_BRANCH_FILTER_REINTRODUCED")
    require("python3 -m unittest discover -s tests -p 'test_pi_flr_audit.py'" in text,
            "CI_MUTATION_TESTS_NOT_EXECUTED")
    require("python3 tools/pi_flr_audit.py" in text and "--baseline-commit" in text,
            "CI_HISTORY_AUDIT_NOT_EXECUTED")
    require("python3 tools/pi_flr_experiment_identity.py" in text,
            "CI_IDENTITY_GUARD_NOT_EXECUTED")
    require("python3 tools/check_public_navigation.py --strict-all" in text,
            "CI_WHOLE_REPOSITORY_LINK_GUARD_NOT_EXECUTED")
    return True


def validate(data, root=ROOT, ci_text=None):
    require(type(data) is dict, "REGISTRY_NOT_OBJECT")
    required = {"registry_id", "schema_version", "release_version", "as_of",
                "korean_name", "english_name", "parent_protocol", "classification",
                "release_rules", "stages", "control_registry", "cases",
                "improvement_protocol"}
    require(set(data) == required, "ROOT_SCHEMA_MISMATCH")
    require(data["registry_id"] == "PI-FLR" and data["parent_protocol"] == "PI-RAMP",
            "REGISTRY_IDENTITY_MISMATCH")
    require(data["schema_version"] == "0.1.0", "UNSUPPORTED_SCHEMA_VERSION")
    version_tuple(data["release_version"])
    require(ISO_DAY.fullmatch(data["as_of"]) is not None, "INVALID_DATE")
    require(data["classification"] == "PUBLIC_OPERATIONAL_EVIDENCE_NOT_SCIENTIFIC_PROOF",
            "PROOF_SCOPE_OVERCLAIM")
    policy = data["release_rules"]
    require(type(policy) is dict and all(k in policy for k in
            ("patch", "minor", "major", "history", "closed_means", "no_private_data")),
            "VERSION_POLICY_MISSING")
    require(policy["no_private_data"] is True, "PRIVATE_DATA_BOUNDARY_DISABLED")
    require(type(data["stages"]) is list and len(data["stages"]) == len(VALID_EVENTS)
            and set(data["stages"]) == VALID_EVENTS,
            "EVENT_DICTIONARY_DRIFT")
    require(type(data["improvement_protocol"]) is dict
            and len(data["improvement_protocol"].get("cycle", [])) >= 7
            and "anti_proxy" in data["improvement_protocol"],
            "RECURSIVE_LEARNING_CONTRACT_MISSING")

    controls = data["control_registry"]
    require(type(controls) is list and len(controls) > 0, "MISSING_CONTROLS")
    control_ids = set()
    test_body = (root / "tests/test_pi_flr_audit.py").read_text(encoding="utf-8")
    for c in controls:
        require(type(c) is dict and set(c) == CONTROL_FIELDS, "INVALID_CONTROL_SCHEMA")
        cid = c["id"]
        require(type(cid) is str and CONTROL_ID.fullmatch(cid) and cid not in control_ids,
                "INVALID_OR_DUPLICATE_CONTROL_ID")
        control_ids.add(cid)
        require(type(c["title"]) is str and bool(c["title"].strip()), "EMPTY_CONTROL_TITLE")
        for k in ("detector", "workflow"):
            require(type(c[k]) is str and len(c[k]) >= 8, "INVALID_CONTROL_REFERENCE")
        method = c["mutation_test"]
        require(type(method) is str and TEST_ID.fullmatch(method)
                and ("def " + method + "(") in test_body,
                "CONTROL_MUTATION_TEST_MISSING:" + str(method))
    cases = data["cases"]
    require(type(cases) is list and bool(cases), "MISSING_CASES")
    ids = set()
    for case in cases:
        require(type(case) is dict and set(case) == CASE_FIELDS, "INVALID_CASE_SCHEMA")
        identifier = case["id"]
        require(type(identifier) is str and CASE_ID.fullmatch(identifier)
                and identifier not in ids, "INVALID_OR_DUPLICATE_CASE_ID")
        ids.add(identifier)
        require(case["category"] in VALID_CATEGORIES, "INVALID_FAILURE_CATEGORY")
        for key in CASE_FIELDS - {"events", "preventive_control_ids", "limitations",
                                  "category", "regression_test", "id"}:
            require(type(case[key]) is str and bool(case[key].strip()),
                    "CASE_FIELD_EMPTY:" + key)
        require(type(case["limitations"]) is list and len(case["limitations"]) > 0
                and all(type(x) is str and x.strip() for x in case["limitations"]),
                "FAILURE_LIMITATIONS_NOT_PRESERVED")
        refs = case["preventive_control_ids"]
        require(type(refs) is list and bool(refs) and len(set(refs)) == len(refs)
                and set(refs) <= control_ids, "MISSING_REFERENCED_CONTROL")
        method = case["regression_test"]
        require(type(method) is str and TEST_ID.fullmatch(method)
                and ("def " + method + "(") in test_body,
                "CASE_MUTATION_TEST_MISSING")
        ev = case["events"]
        require(type(ev) is list and len(ev) >= 2, "EVENT_HISTORY_TOO_SHORT")
        kinds = []
        for num, e in enumerate(ev, 1):
            require(type(e) is dict and set(e) == EVENT_FIELDS
                    and type(e["seq"]) is int and e["seq"] == num,
                    "EVENT_SEQUENCE_OR_SCHEMA_INVALID:" + identifier)
            require(type(e["date"]) is str and ISO_DAY.fullmatch(e["date"]) is not None
                    and e["date"] <= data["as_of"], "INVALID_EVENT_DATE:" + identifier)
            require(e["kind"] in VALID_EVENTS, "INVALID_EVENT_KIND:" + identifier)
            require(type(e["note"]) is str and 10 <= len(e["note"]) <= 1000,
                    "INVALID_EVENT_NOTE:" + identifier)
            link = e["evidence_url"]
            require(type(link) is str and urlsplit(link).scheme == "https"
                    and urlsplit(link).netloc == "github.com"
                    and urlsplit(link).path.startswith(
                        "/gmodrasa7-rgb/project-intersection-public/"),
                    "UNTRUSTED_OR_UNGROUNDED_LINK_HOST:" + identifier)
            kinds.append(e["kind"])
        require(kinds[0] == "FAILURE_OBSERVED", "CASE_MISSING_FAILURE_EVIDENCE")
        require("ROOT_CAUSE_REVIEWED" in kinds and
                kinds.index("FAILURE_OBSERVED") < kinds.index("ROOT_CAUSE_REVIEWED"),
                "CASE_ROOT_CAUSE_NOT_REVIEWED")
        if "FIX_MERGED" in kinds:
            require("REPAIR_APPLIED" in kinds and
                    "CI_PASS_OBSERVED" in kinds, "CLAIMED_MERGE_WITHOUT_REPAIR_OR_CI")
    check_ci_contract(ci_text if ci_text is not None
                      else (root / CI_PATH).read_text(encoding="utf-8"))
    return {"result":"PI_FLR_STRUCTURAL_AND_HISTORY_READY",
            "version":data["release_version"],"cases":len(ids),
            "controls":len(control_ids),
            "boundary":"NO_ZERO_RECURRENCE_OR_REAL_WORLD_VERIFICATION"}


def compare_history(now, old):
    """Old case claims and prior event records must remain exact prefixes."""
    require(type(old) is dict and old.get("registry_id") == "PI-FLR",
            "INVALID_BASELINE_REGISTRY")
    before_version = version_tuple(old.get("release_version"))
    after_version = version_tuple(now.get("release_version"))
    oldcases = {c["id"]: c for c in old.get("cases", [])}
    newcases = {c["id"]: c for c in now["cases"]}
    require(set(oldcases) <= set(newcases), "HISTORICAL_CASE_DELETED")
    for key, prev in oldcases.items():
        curr = newcases[key]
        require({k:v for k,v in curr.items() if k!="events"} ==
                {k:v for k,v in prev.items() if k!="events"},
                "HISTORICAL_CASE_METADATA_REWRITTEN:"+key)
        require(curr["events"][:len(prev["events"])] == prev["events"],
                "HISTORICAL_EVIDENCE_REWRITTEN:"+key)
    prior_controls = {c["id"]:c for c in old.get("control_registry", [])}
    next_controls = {c["id"]:c for c in now["control_registry"]}
    require(set(prior_controls) <= set(next_controls), "HISTORICAL_CONTROL_REMOVED")
    for key, old_ctrl in prior_controls.items():
        require(old_ctrl == next_controls[key], "HISTORICAL_CONTROL_REWRITTEN:"+key)
    changed_payload = {k:v for k,v in now.items() if k != "release_version"} != (
        {k:v for k,v in old.items() if k != "release_version"})
    if changed_payload:
        require(after_version > before_version, "VERSION_BUMP_REQUIRED_FOR_REGISTRY_CHANGE")
    else:
        require(after_version == before_version, "EMPTY_VERSION_BUMP")
    return True


def baseline_from_git(commit, root=ROOT):
    if not commit or commit == "0"*40:
        return None
    require(re.fullmatch(r"[0-9a-fA-F]{7,40}", commit) is not None,
            "INVALID_BASELINE_SHA")
    result = subprocess.run(["git", "show", commit + ":" + REGISTRY_PATH],
                            cwd=root, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        # Distinguish an initial registry addition from missing commit, not silent success.
        verify = subprocess.run(["git", "cat-file", "-e", commit + "^{commit}"],
                                cwd=root, capture_output=True, check=False)
        require(verify.returncode == 0, "BASELINE_COMMIT_NOT_FETCHED")
        return None
    return json.loads(result.stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline-commit", default="")
    a = ap.parse_args()
    try:
        obj = json.loads((ROOT / REGISTRY_PATH).read_text(encoding="utf-8"))
        result = validate(obj)
        old = baseline_from_git(a.baseline_commit)
        if old is not None:
            compare_history(obj, old)
            result["history_check"] = "APPEND_ONLY_AND_VERSION_BUMP_VALID"
        else:
            result["history_check"] = "BASELINE_NOT_AVAILABLE_OR_FIRST_PUBLICATION"
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    except (FLRError, ValueError, OSError, KeyError, TypeError) as exc:
        raise SystemExit("PI_FLR_AUDIT_FAIL:" + str(exc)) from None


if __name__ == "__main__":
    main()
