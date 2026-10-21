#!/usr/bin/env python3
"""Eight proposed individual research version baselines. Scientific truth NOT inferred."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "research/INDIVIDUAL_RESEARCH_VERSION_BASELINES_V0_1_0.json"
DOC = "research/INDIVIDUAL_RESEARCH_VERSIONS_V0_1_0_EN_KO.md"
EXPECTED = {
    "ICM", "RGBM", "PI-UNKNOWN-PARADOX",
    "PI-NONMALICIOUS-EXPLOITATION", "PI-INCENTIVE-CROSSOVER",
    "PI-COUNTERFACTUAL-FUTURE", "PI-DEVELOPMENT-PATHWAYS", "DCA-0",
}
LIMITED_EVIDENCE = "HYPOTHESIS_AND_PRIOR_ART_ONLY"
HASH = re.compile(r"^[0-9a-f]{40}$")


def file_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def inspect(data: dict, *, root: Path = ROOT, override: dict[str, bytes] | None = None) -> list[str]:
    problems = []
    override = override or {}
    if data.get("schema_version") != "0.1.0" or data.get("document_version") != "0.1.0":
        problems.append("VERSION_SCHEMA_DRIFT")
    if data.get("nature") != "INITIAL_DOCUMENTATION_VERSION_NOT_SCIENTIFIC_VALIDATION":
        problems.append("SCIENTIFIC_STATUS_PROMOTED")
    if data.get("language_order") != "EN_ORIGINAL_1_THEN_KO_ORIGINAL_2":
        problems.append("LANGUAGE_ORDER_DRIFT")
    boundary = data.get("legacy_boundaries", {})
    if not all(word in boundary.get("ICM", "") for word in ("Intersection", "Independent Continuance Margin")):
        # ICM's new form and historically used form must remain distinct.
        if "non-equivalent" not in boundary.get("ICM", "").lower():
            problems.append("ICM_CONSTRUCTS_CONFLATED")
    if "version 0.1" not in boundary.get("DCA_0", ""):
        problems.append("DCA0_HISTORICAL_VERSION_ERASED")
    if "unmerged" not in boundary.get("ECR", "").lower():
        problems.append("ECR_DRAFT_PROMOTED")
    entries = data.get("entries")
    if not isinstance(entries, list):
        return problems + ["STUDIES_NOT_LIST"]
    ids = [e.get("id") for e in entries if isinstance(e, dict)]
    if len(ids) != len(entries) or len(ids) != len(set(ids)) or set(ids) != EXPECTED:
        problems.append("EXPECTED_STUDY_IDS_CHANGED_OR_DUPLICATED")
    for e in entries:
        if not isinstance(e, dict):
            problems.append("ROW_NOT_OBJECT")
            continue
        rid = e.get("id", "?")
        for f in ("name_en", "name_ko", "question_en", "question_ko",
                  "disconfirming_case_en", "disconfirming_case_ko", "source_path"):
            if not isinstance(e.get(f), str) or not e[f].strip():
                problems.append(rid + ":MISSING_" + f)
        if e.get("current_version") != "0.1.0":
            problems.append(rid + ":VERSION_NOT_BASELINE")
        if e.get("evidence_state") != LIMITED_EVIDENCE or e.get("scientific_validation") != "NOT_ESTABLISHED":
            problems.append(rid + ":EVIDENCE_PROMOTED")
        if e.get("independent_replication") is not False or e.get("version_is_evidence_grade") is not False:
            problems.append(rid + ":FALSE_REPLICATION_OR_VERSION_EQUIVALENCE")
        path = e.get("source_path", "")
        source_sha = e.get("source_blob_sha")
        if not isinstance(path, str) or not path.startswith("research/") or ".." in Path(path).parts:
            problems.append(rid + ":UNSAFE_SOURCE_PATH")
            continue
        if not isinstance(source_sha, str) or not HASH.fullmatch(source_sha):
            problems.append(rid + ":INVALID_SOURCE_SHA")
            continue
        try:
            source = override.get(path, (root / path).read_bytes())
            if file_sha(source) != source_sha:
                problems.append(rid + ":SOURCE_CHANGED_WITHOUT_REVIEW")
        except (OSError, ValueError):
            problems.append(rid + ":SOURCE_NOT_READABLE")
    try:
        document = override.get(DOC, (root / DOC).read_bytes()).decode("utf-8")
        for marker in ("## Original 1 — English", "## 원본2 — 한국어",
                       "HYPOTHESIS_AND_PRIOR_ART_ONLY", "DCA-0", "ICM"):
            if marker not in document:
                problems.append("DOCUMENT_MISSING:" + marker)
        if document.index("## Original 1 — English") >= document.index("## 원본2 — 한국어"):
            problems.append("EDITION_ORDER_REVERSED")
        for rid in EXPECTED:
            if document.count("**" + rid + " —") != 2:
                problems.append("DOCUMENT_TWO_EDITION_BODY_MISSING:" + rid)
    except (OSError, UnicodeDecodeError, ValueError):
        problems.append("DOCUMENT_MISSING_OR_UNREADABLE")
    return problems


def self_test(data: dict) -> list[str]:
    failures = []
    cases = []
    def mutate(label, fn):
        d = copy.deepcopy(data)
        fn(d)
        cases.append((label, d))
    mutate("source-hash", lambda d: d["entries"][0].update(source_blob_sha="0"*40))
    mutate("fabricate-evidence", lambda d: d["entries"][0].update(evidence_state="FIELD_PROVEN"))
    mutate("fabricate-replication", lambda d: d["entries"][0].update(independent_replication=True))
    mutate("invent-version", lambda d: d["entries"][0].update(current_version="9.9.9"))
    mutate("erase-substudy", lambda d: d["entries"].pop())
    mutate("duplicate-substudy", lambda d: d["entries"].append(copy.deepcopy(d["entries"][0])))
    mutate("erase-icm-collision", lambda d: d["legacy_boundaries"].update(ICM="identical measures"))
    mutate("ecr-promoted", lambda d: d["legacy_boundaries"].update(ECR="merged approved"))
    mutate("forget-historical-dca", lambda d: d["legacy_boundaries"].update(DCA_0="new study"))
    for label, altered in cases:
        if not inspect(altered):
            failures.append("FALSE_PASS:" + label)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    data = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    problems = inspect(data)
    if not problems and args.self_test:
        problems += self_test(data)
    if problems:
        print("FAIL:", *problems, sep="\n- ")
        return 1
    print("PASS: eight independent documentation baselines, exact source pins, two language editions, non-promotion limits; not scientific validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
