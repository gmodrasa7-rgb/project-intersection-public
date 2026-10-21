#!/usr/bin/env python3
"""24-study priority metadata integrity. Ranking is a plan, never scientific evidence."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = "research/INDIVIDUAL_RESEARCH_PRIORITY_VERSION_MATRIX_V0_1_0.json"
DOC = "research/INDIVIDUAL_RESEARCH_PRIORITY_VERSION_MATRIX_V0_1_0_EN_KO.md"
BASELINE = "research/INDIVIDUAL_RESEARCH_VERSION_BASELINES_V0_1_0.json"
VERSION = re.compile(r"^v(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){1,2}$")
HEX = re.compile(r"^[0-9a-f]{40}$")
BASELINE_IDS = {"ICM", "RGBM", "PI-UNKNOWN-PARADOX",
                "PI-NONMALICIOUS-EXPLOITATION", "PI-INCENTIVE-CROSSOVER",
                "PI-COUNTERFACTUAL-FUTURE", "PI-DEVELOPMENT-PATHWAYS", "DCA-0"}
SPECIAL = {"ECR", "OCP"}


def git_sha(content: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def check(obj: dict, *, root: Path = ROOT,
          override: dict[str, bytes] | None = None) -> list[str]:
    override = override or {}
    errors = []

    def read(p: str) -> bytes:
        return override[p] if p in override else (root / p).read_bytes()

    if obj.get("schema_version") != "pi-individual-research-priority/v0.1.0":
        errors.append("SCHEMA_MISMATCH")
    if obj.get("matrix_version") != "0.1.0":
        errors.append("MATRIX_RELEASE_DRIFT")
    policy = obj.get("priority_policy", {})
    if (policy.get("semantic_version_remains_unchanged") is not True
            or policy.get("priority_is_not_semver") is not True
            or policy.get("scores_status") != "INTERNAL_EXPLICIT_EDITORIAL_PRIORITIZATION_NOT_EXPERT_CONSENSUS"):
        errors.append("PLANNING_AND_SCIENTIFIC_VERSION_CONFLATION")
    if obj.get("status") != "PROPOSED_IN_STACKED_PR_346":
        errors.append("UNMERGED_PRIORITY_MATRIX_MARKED_RELEASED")
    if "private" not in obj.get("special_cases", {}).get("OCP", "").lower():
        errors.append("PRIVATE_SOURCE_BOUNDARY_ERASED")

    rows = obj.get("entries")
    if not isinstance(rows, list):
        return errors + ["ENTRIES_NOT_LIST"]
    if len(rows) != 24:
        errors.append("STUDY_COUNT_NOT_24")
    ranks = [e.get("priority_rank") for e in rows if isinstance(e, dict)]
    ids = [e.get("id") for e in rows if isinstance(e, dict)]
    if ranks != list(range(1, 25)):
        errors.append("PRIORITY_RANKS_NOT_1_THROUGH_24")
    if len(set(ids)) != 24 or len(ids) != 24:
        errors.append("DUPLICATE_OR_MISSING_STUDY")
    if set(ids) & {"VC", "IVS-0R", "PI-RAMP", "PI-FLR", "PI-RISE", "E009"}:
        errors.append("PURPOSE_OR_MANAGEMENT_RECLASSIFIED_AS_STUDY")

    try:
        first = json.loads(read(BASELINE))
        initial = {x["id"]: x for x in first["entries"]}
        if set(initial) != BASELINE_IDS:
            errors.append("INITIAL_BASELINE_IDENTITIES_CHANGED")
    except (OSError, ValueError, KeyError, TypeError):
        initial = {}
        errors.append("INITIAL_VERSION_BASELINE_MISSING")

    try:
        doc = read(DOC).decode("utf-8")
        if doc.index("## Original 1 — English") > doc.index("## 원본2 — 한국어"):
            errors.append("EN_KO_ORDER_REVERSED")
        if "priority does not mean correctness" not in doc.lower():
            errors.append("NO_PRIORITY_UNCERTAINTY")
        if "임의" not in doc and "계획" not in doc:
            errors.append("KOREAN_JUDGMENT_WARNING_REMOVED")
    except (OSError, UnicodeError, ValueError):
        doc = ""
        errors.append("VERSION_MATRIX_DOCUMENT_MISSING")

    for e in rows:
        if not isinstance(e, dict):
            errors.append("ROW_NOT_OBJECT")
            continue
        rid = e.get("id", "")
        r = e.get("priority_rank")
        expected_band = "P0" if isinstance(r, int) and r <= 5 else (
            "P1" if isinstance(r, int) and r <= 13 else (
            "P2" if isinstance(r, int) and r <= 20 else "P3"))
        if e.get("priority_band") != expected_band:
            errors.append(rid + ":WRONG_PRIORITY_BAND")
        n, d = e.get("necessity"), e.get("difficulty")
        if not all(type(v) is int and 1 <= v <= 5 for v in (n, d)):
            errors.append(rid + ":OUT_OF_RANGE_N_OR_D")
        version = e.get("version_label")
        if not isinstance(version, str) or not VERSION.fullmatch(version):
            errors.append(rid + ":VERSION_LABEL_MALFORMED")
            continue
        want = f"{version} | {expected_band} | N{n}/5 | D{d}/5"
        if e.get("display") != want:
            errors.append(rid + ":VERSION_PLANNING_DISPLAY_DRIFT")
        if not all(isinstance(e.get(key), str) and e[key]
                   for key in ("name_en", "name_ko", "rationale_ko",
                               "next_verification_step_en", "version_provenance")):
            errors.append(rid + ":DESCRIPTION_MISSING")
        if e.get("evidence_grade_independently_established") is not False:
            errors.append(rid + ":FALSE_SCIENCE_PROMOTION")
        if doc.count("| **" + rid + " —") != 2:
            errors.append(rid + ":BILINGUAL_DOC_ENTRY_MISSING")
        if rid in initial:
            base = initial[rid]
            if not (base.get("current_version") == version.lstrip("v")
                    and base.get("priority_rank") == r
                    and base.get("priority_band") == expected_band
                    and base.get("necessity") == n
                    and base.get("difficulty") == d
                    and base.get("version_priority_display") == want):
                errors.append(rid + ":INITIAL_BASELINE_PRIORITY_MISMATCH")
        path, sha = e.get("public_source_path"), e.get("public_source_blob_sha")
        if rid == "ECR":
            if (version != "v1.4" or e.get("version_provenance") != "OPEN_UNMERGED_DRAFT_PR_211"
                    or path is not None or sha is not None):
                errors.append("ECR_DRAFT_CONFUSED_WITH_MAIN")
        elif rid == "OCP":
            if (version != "v0.15" or e.get("version_provenance") != "PRIVATE_VERIFIED_HISTORICAL_REFERENCE"
                    or path is not None or sha is not None):
                errors.append("OCP_PRIVATE_SOURCE_LEAK_OR_FALSE_RELEASE")
        elif rid in initial:
            if (e.get("version_provenance") != "PROPOSED_IN_STACKED_PR_346"
                    or path != initial[rid].get("source_path")
                    or sha != initial[rid].get("source_blob_sha")):
                errors.append(rid + ":ORIGINAL_BASELINE_SOURCE_OR_DRAFT_STATE_DRIFT")
        else:
            if e.get("version_provenance") != "PUBLIC_MAIN_SOURCE_VERIFIED":
                errors.append(rid + ":MAIN_RELEASE_STATUS_DRIFT")
        if rid not in SPECIAL:
            if (not isinstance(path, str) or not path.startswith("research/")
                    or ".." in Path(path).parts or not isinstance(sha, str) or not HEX.fullmatch(sha)):
                errors.append(rid + ":UNSAFE_OR_UNPINNED_PUBLIC_SOURCE")
                continue
            try:
                if git_sha(read(path)) != sha:
                    errors.append(rid + ":ORIGINAL_SOURCE_CHANGED_UNREVIEWED")
            except (OSError, ValueError):
                errors.append(rid + ":SOURCE_FILE_MISSING")
    return errors


def self_test(obj):
    scenarios = []
    def mutate(label, fn):
        item = copy.deepcopy(obj)
        fn(item)
        scenarios.append((label, item))
    mutate("rank-duplicate", lambda x: x["entries"][1].update(priority_rank=1))
    mutate("need-overflow", lambda x: x["entries"][0].update(necessity=7))
    mutate("difficulty-drift", lambda x: x["entries"][0].update(difficulty=1))
    mutate("version-promoted", lambda x: x["entries"][0].update(version_label="v9.0.0"))
    mutate("hidden-null-evidence", lambda x: x["entries"][0].update(evidence_grade_independently_established=True))
    mutate("ecr-draft-promoted", lambda x: x["entries"][2].update(version_provenance="PUBLIC_MAIN_SOURCE_VERIFIED"))
    mutate("ocp-path-leak", lambda x: x["entries"][-1].update(public_source_path="private/secret.md"))
    mutate("edit-public-sha", lambda x: x["entries"][0].update(public_source_blob_sha="0"*40))
    mutate("drop-24th-study", lambda x: x["entries"].pop())
    mutate("research-success-by-priority", lambda x: x["priority_policy"].update(priority_is_not_semver=False))
    errors = [label for label, item in scenarios if not check(item)]
    return ["FALSE_PASS:" + label for label in errors]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    data = json.loads((ROOT / MATRIX).read_text(encoding="utf-8"))
    problems = check(data)
    if not problems and args.self_test:
        problems.extend(self_test(data))
    if problems:
        print("FAIL priority metadata:\n- " + "\n- ".join(problems))
        return 1
    print("PASS: 24 bounded version/priorities, 8 original baselines, public source hashes, EN/KO parity and negative controls; scientific results UNVERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
