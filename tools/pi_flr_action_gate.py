#!/usr/bin/env python3
"""PI-FLR cross-industry action gate: checks design claims, not field efficacy.

Pure offline validation. No personal data collection or independent attestation.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ACTION = "knowledge/PI_FLR_ACTION_EFFECTIVENESS_V0_1_0_KO.json"
REGISTRY = "knowledge/PI_FLR_CASES_V0_1_0.json"
WORKFLOW = ".github/workflows/pi-flr-integrity.yml"
DOMAINS = {"www.ihi.org", "sre.google", "www.fda.gov", "asrs.arc.nasa.gov",
           "airc.nist.gov"}
CLASSES = {"AUTOMATED_BLOCKING_GUARD", "AUTOMATED_DETECTION_ONLY",
           "HUMAN_PROCEDURE", "NOT_CLASSIFIED"}
SOURCE_FIELDS = {"id", "family", "grade", "url", "transfer", "limitation"}
ACTION_FIELDS = {"id", "case_id", "control_id", "priority", "action_class",
                 "status", "target_failure_ko", "competing_explanation_ko",
                 "eligible_denominator_ko", "recurrence_numerator_ko",
                 "adverse_effects_ko", "rollback_ko"}
OBS_FIELDS = {"id", "action_id", "status", "window", "eligible", "recurrences",
              "false_blocks", "human_review_minutes", "evidence_urls", "limitation"}


class ActionError(ValueError):
    pass


def require(ok, code):
    if not ok:
        raise ActionError(code)


def _version(value):
    require(isinstance(value, str) and re.fullmatch(r"\d+\.\d+\.\d+", value),
            "INVALID_VERSION")
    return tuple(map(int, value.split(".")))


def _trusted_url(url, domains):
    require(isinstance(url, str), "INVALID_URL")
    parts = urlsplit(url)
    return parts.scheme == "https" and parts.hostname in domains and not parts.username



def _verified_github_run(url, window):
    """Check source existence at GitHub; NEVER certify denominator or field efficacy.

    Fail closed for 403, 404, 429, malformed payload and outages. These states
    mean NOT_VERIFIED, not 'run absent'. Fixed host, repository and numeric ID
    prevent observation URLs from becoming arbitrary network fetch targets.
    """
    parts = urlsplit(url)
    match = re.fullmatch(
        r"/gmodrasa7-rgb/project-intersection-public/actions/runs/([1-9][0-9]*)",
        parts.path)
    if not (parts.scheme == "https" and parts.netloc == "github.com" and
            not parts.query and not parts.fragment and match and
            isinstance(window, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}", window)):
        return False
    run_id = int(match.group(1))
    endpoint = ("https://api.github.com/repos/gmodrasa7-rgb/"
                "project-intersection-public/actions/runs/" + str(run_id))
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "User-Agent": "PI-FLR-Receipt-Check/0.1"}
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        with urlopen(Request(endpoint, headers=headers), timeout=10) as response:
            if response.status != 200:
                return False
            payload = json.loads(response.read(160000).decode("utf-8"))
    except (OSError, ValueError, TypeError, UnicodeError):
        return False
    return (type(payload) is dict and payload.get("id") == run_id and
            isinstance(payload.get("repository"), dict) and
            payload["repository"].get("full_name") ==
            "gmodrasa7-rgb/project-intersection-public" and
            payload.get("html_url") == url and
            payload.get("status") == "completed" and
            isinstance(payload.get("created_at"), str) and
            payload["created_at"].startswith(window + "-"))

def validate(data, registry, workflow, root=ROOT):
    require(set(data) == {"registry_id", "schema_version", "release_version",
                          "as_of", "classification", "language_order",
                          "privacy_policy", "source_limit", "sources", "intersection",
                          "pilot_actions", "observations", "status_policy"},
            "ACTION_SCHEMA_DRIFT")
    require(data["registry_id"] == "PI-FLR-ACTION-EFFECTIVENESS" and
            data["schema_version"] == "0.1.0", "ACTION_IDENTITY_CHANGED")
    _version(data["release_version"])
    require(data["language_order"] == ["English primary", "Korean secondary"] and
            data["classification"] == "CROSS_INDUSTRY_DESIGN_TRANSFER_NOT_FIELD_EFFECTIVENESS",
            "UNSUPPORTED_EFFICACY_OR_LANGUAGE_CLAIM")
    require("원문 개인대화" in data["privacy_policy"] and
            "아니다" in data["source_limit"], "PRIVACY_OR_SOURCE_LIMIT_MISSING")
    require(registry.get("registry_id") == "PI-FLR", "PARENT_REGISTRY_MISSING")
    sources = {}
    families = set()
    require(len(data["sources"]) >= 4, "PRIOR_ART_TOO_NARROW")
    for source in data["sources"]:
        require(set(source) == SOURCE_FIELDS, "SOURCE_FIELDS_INVALID")
        require(re.fullmatch(r"A\d{2}", source["id"]) and
                source["id"] not in sources, "DUPLICATE_OR_INVALID_SOURCE")
        require(_trusted_url(source["url"], DOMAINS), "UNTRUSTED_SOURCE_URL")
        require(len(source["family"]) >= 4 and len(source["limitation"]) >= 25
                and len(source["transfer"]) >= 20, "SOURCE_LIMITATION_MISSING")
        sources[source["id"]] = source
        families.add(source["family"])
    require(len(families) >= 4, "CORRELATED_PRIOR_ART_FAMILIES")
    intersection_ids = set()
    require(len(data["intersection"]) >= 3, "INTERSECTION_MISSING")
    for item in data["intersection"]:
        require(set(item) == {"id", "sources", "rule_ko", "counterexample_ko"},
                "INTERSECTION_SCHEMA_DRIFT")
        require(item["id"] not in intersection_ids, "DUPLICATE_INTERSECTION")
        intersection_ids.add(item["id"])
        require(len(set(item["sources"])) == len(item["sources"]) and
                set(item["sources"]) <= sources.keys() and
                len({sources[s]["family"] for s in item["sources"]}) >= 2,
                "INTERSECTION_NOT_INDEPENDENT")
        require(len(item["rule_ko"]) >= 30 and
                len(item["counterexample_ko"]) >= 25,
                "INTERSECTION_COUNTEREXAMPLE_LOST")
    cases = {x["id"]: x for x in registry["cases"]}
    controls = {x["id"]: x for x in registry["control_registry"]}
    action_ids = set()
    mapped_cases = set()
    for item in data["pilot_actions"]:
        require(set(item) == ACTION_FIELDS, "PILOT_SCHEMA_DRIFT")
        require(re.fullmatch(r"FLR-A\d{3}", item["id"]) and
                item["id"] not in action_ids, "INVALID_OR_DUPLICATE_ACTION")
        action_ids.add(item["id"])
        require(item["case_id"] in cases and item["control_id"] in controls and
                item["control_id"] in cases[item["case_id"]]["preventive_control_ids"],
                "ACTION_ORPHAN_OR_INCORRECT_CONTROL")
        mapped_cases.add(item["case_id"])
        require(item["action_class"] in CLASSES and item["priority"] in {"P0", "P1"}
                and item["status"] == "CONTROL_MAPPED_EFFECT_NOT_OBSERVED",
                "ACTION_CLASS_OR_EFFICACY_OVERCLAIM")
        for key in ("target_failure_ko", "competing_explanation_ko",
                    "eligible_denominator_ko", "recurrence_numerator_ko", "rollback_ko"):
            require(isinstance(item[key], str) and len(item[key]) >= 20,
                    "ACTION_NOT_TESTABLE:" + key)
        require(len(item["adverse_effects_ko"]) >= 2 and
                all(len(x) >= 10 for x in item["adverse_effects_ko"]),
                "ADVERSE_EFFECTS_NOT_MAPPED")
        control = controls[item["control_id"]]
        detector = control["detector"].split("::", 1)[0].split(";", 1)[0]
        require(detector.startswith("tools/") and (root / detector).is_file() and
                control["workflow"] == WORKFLOW,
                "CLAIMED_CONTROL_NOT_PRESENT_IN_REPOSITORY")
    require({"FLR-0009", "FLR-0010"} <= mapped_cases,
            "P0_FALSE_GREEN_PILOTS_REMOVED")
    observations = set()
    for obs in data["observations"]:
        require(set(obs) == OBS_FIELDS, "OBSERVATION_SCHEMA_DRIFT")
        require(obs["id"] not in observations and
                re.fullmatch(r"FLR-O\d{4}", obs["id"]),
                "OBSERVATION_DUPLICATE_OR_INVALID")
        observations.add(obs["id"])
        require(obs["action_id"] in action_ids and
                obs["status"] == "OBSERVED_NOT_EFFECTIVENESS_CERTIFIED" and
                len(obs["limitation"]) >= 20, "FALSE_FIELD_VERIFICATION")
        require(obs["window"] != "UNOBSERVED" and
                isinstance(obs["eligible"], int) and not isinstance(obs["eligible"], bool) and
                obs["eligible"] > 0 and
                isinstance(obs["recurrences"], int) and not isinstance(obs["recurrences"], bool) and
                0 <= obs["recurrences"] <= obs["eligible"],
                "MISSING_EXPOSURE_DENOMINATOR")
        for metric in ("false_blocks", "human_review_minutes"):
            require(obs[metric] is None or
                    (type(obs[metric]) is int and obs[metric] >= 0),
                    "INVALID_OR_INVENTED_SIDE_EFFECT_METRIC")
        require(obs["evidence_urls"] and all(_trusted_url(x, {"github.com"}) and
                urlsplit(x).path.startswith("/gmodrasa7-rgb/project-intersection-public/")
                for x in obs["evidence_urls"]), "UNVERIFIABLE_OBSERVATION_RECEIPT")
        for url in obs["evidence_urls"]:
            require(_verified_github_run(url, obs["window"]),
                    "OBSERVED_RECEIPT_REMOTE_UNVERIFIED_NOT_ABSENT")
    policy = data["status_policy"]
    require(policy == {"other_cases": "UNTRIAGED_NOT_ZERO",
                       "no_exposure": "UNKNOWN_NOT_ZERO",
                       "independent_effectiveness": "NOT_OBSERVED",
                       "recurrence_window": "UNOBSERVED",
                       "near_miss_channel": "NOT_IMPLEMENTED_NO_CONFIDENTIALITY_PROMISE",
                       "field_effectiveness_certified": False,
                       "human_burden_reduction_certified": False},
            "MISSINGNESS_OR_EFFECTIVENESS_FALSE_CERTIFICATION")
    require("test_pi_flr_action_gate.py" in workflow and
            "python3 tools/pi_flr_action_gate.py" in workflow,
            "ACTION_GUARD_NOT_EXECUTED_BY_CI")
    return {"status": "DESIGN_TRANSFER_ONLY_NOT_FIELD_VERIFIED",
            "source_families": len(families), "intersections": len(intersection_ids),
            "pilot_actions": len(action_ids),
            "untriaged_case_count": len(cases.keys() - mapped_cases),
            "observations": len(observations), "field_effectiveness_verified": 0}


def compare_history(current, old):
    require(old["registry_id"] == "PI-FLR-ACTION-EFFECTIVENESS",
            "INVALID_ACTION_BASELINE")
    for key in ("sources", "intersection", "pilot_actions", "observations"):
        require(current[key][:len(old[key])] == old[key],
                "ACTION_HISTORY_REWRITTEN:" + key)
    require(_version(current["release_version"]) >= _version(old["release_version"]),
            "ACTION_VERSION_REGRESSION")
    if current != old:
        require(_version(current["release_version"]) > _version(old["release_version"]),
                "UNVERSIONED_ACTION_CHANGE")
    else:
        require(current["release_version"] == old["release_version"],
                "EMPTY_ACTION_VERSION_BUMP")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-commit", default="")
    args = parser.parse_args()
    try:
        data = json.loads((ROOT / ACTION).read_text(encoding="utf-8"))
        parent = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
        workflow = (ROOT / WORKFLOW).read_text(encoding="utf-8")
        report = validate(data, parent, workflow)
        report["history"] = "BASELINE_UNOBSERVED_NEW_FILE"
        if re.fullmatch(r"[0-9a-fA-F]{40}", args.baseline_commit):
            old = subprocess.run(["git", "show", args.baseline_commit + ":" + ACTION],
                                 cwd=ROOT, capture_output=True, text=True, check=False)
            if old.returncode == 0:
                compare_history(data, json.loads(old.stdout))
                report["history"] = "APPEND_ONLY_VERIFIED"
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit("PI_FLR_ACTION_GATE_FAIL:" + str(exc)) from None


if __name__ == "__main__":
    main()
