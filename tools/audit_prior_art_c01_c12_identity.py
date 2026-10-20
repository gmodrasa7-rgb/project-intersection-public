#!/usr/bin/env python3
"""Project Intersection C01-C12 primary-literature identity/contrast audit.

Pure standard library. The frozen manifest verifies source JSON Git blob identities,
233 bibliographic records, normalized identifier uniqueness, and six similar-title
pairs that require review rather than automatic merging. This is NOT a study-level
deduplication, research-quality, independent bibliographic, or saturation certificate.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "evaluation/pi_ramp/PRIOR_ART_C01_C12_IDENTITY_AUDIT_20261020.json"
STOP = set("the and with for from into experimental effects effect study evidence social original among versus human humans".split())
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
FIELDS = ("doi", "canonical_doi", "canonical_key", "stable_key", "key")
IDS = ("canonical_key", "stable_key", "key", "alternate_stable_identifier",
       "alternate_verified_id", "other_stable_id", "alternative_id", "alt_id")
REQUIRED_CYCLES = set(range(1, 13))
MAX_REASONABLE_PAIRS = 10000


def blob_hash(content: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(content)).encode("ascii")
                        + b"\0" + content).hexdigest()


def normalize(raw: object) -> str:
    if not isinstance(raw, str):
        return ""
    return re.sub(r"[.,;]+$", "", re.sub(r"^(?:doi:|https?://(?:dx\.)?doi\.org/)",
                                             "", raw.strip().lower()))


def doi(record: dict) -> str | None:
    for name in FIELDS:
        value = normalize(record.get(name))
        if DOI_RE.match(value):
            return value
    return None


def stable_id(record: dict) -> str | None:
    return next((v for field in IDS if (v := normalize(record.get(field)))), None)


def plain_title(value: str) -> str:
    a = unicodedata.normalize("NFKD", value).lower()
    return " ".join(re.findall(r"[\w]+", a, flags=re.UNICODE))


def keywords(value: str) -> set[str]:
    return set(w for w in re.sub(r"[^a-z0-9\s]", " ", value.lower()).split()
               if len(w) > 2 and w not in STOP)


def similarity(a: str, b: str) -> float:
    x, y = keywords(a), keywords(b)
    intersection = len(x & y)
    return intersection / (len(x | y) or 1)


def cycle(path: str) -> int | None:
    stem = Path(path).stem
    m = re.search(r"CYCLE(\d+)_2026-10-20$", stem)
    if m:
        return int(m.group(1))
    if stem.endswith("C08_A_2026-10-20"):
        return 8
    return None


def read_sources(manifest: dict) -> tuple[list[dict], list[str]]:
    errors = []
    rows = []
    sources = manifest.get("source_inputs", [])
    if len(sources) != 12 or {cycle(x.get("path", "")) for x in sources} != REQUIRED_CYCLES:
        errors.append("C01_C12_SOURCE_COVERAGE_MISMATCH")
    paths = [x.get("path", "") for x in sources]
    if len(set(paths)) != len(paths) or paths != sorted(paths):
        errors.append("SOURCE_PATH_DUPLICATE_OR_UNSORTED")
    for spec in sources:
        p = spec.get("path", "")
        target = ROOT / p
        if not p.startswith("research/PRIOR_ART_") or not p.endswith(".json") or ".." in Path(p).parts:
            errors.append("UNSAFE_SOURCE_PATH:" + p)
            continue
        if not target.is_file():
            errors.append("MISSING_SOURCE:" + p)
            continue
        raw = target.read_bytes()
        if blob_hash(raw) != spec.get("git_blob_sha"):
            errors.append("FROZEN_SOURCE_CHANGED:" + p)
        data = json.loads(raw)
        selected = data.get("records")
        if not isinstance(selected, list) or len(selected) != spec.get("records"):
            errors.append("SOURCE_RECORD_COUNT_DRIFT:" + p)
            continue
        for record in selected:
            if not isinstance(record, dict):
                errors.append("NON_OBJECT_RECORD:" + p)
                continue
            rows.append({**record, "_source": p})
    return rows, errors


def analyze(records: list[dict], manifest: dict) -> list[str]:
    errors = []
    if manifest.get("manifest_status") != "REPRODUCIBLE_METADATA_SNAPSHOT_NOT_STUDY_DEDUP_CERTIFICATION":
        errors.append("OVERCLAIMED_DEDUPLICATION")
    if manifest.get("counting_unit") != "CURATED_SOURCE_RECORD_NOT_UNIQUE_EXPERIMENT_OR_UNIQUE_STUDY":
        errors.append("MISLABELED_COUNTING_UNIT")
    if manifest.get("study_identity_verified_count") is not None:
        errors.append("UNSUPPORTED_STUDY_IDENTITY_CERTIFICATION")
    if manifest.get("file_count") != 12:
        errors.append("FILE_COUNT_WRONG")
    if len(records) != manifest.get("source_record_count"):
        errors.append("RECORD_COUNT_WRONG")
    all_doi = []
    title_groups = defaultdict(list)
    record_ids = {}
    for rec in records:
        rid = rec.get("id")
        if not isinstance(rid, str) or not rid.strip() or rid in record_ids:
            errors.append("MISSING_OR_DUPLICATE_SOURCE_RECORD_ID:" + str(rid))
        record_ids[rid] = rec
        if not rec.get("title") or not rec.get("year"):
            errors.append("MISSING_TITLE_OR_YEAR:" + str(rid))
        title_groups[plain_title(rec.get("title", ""))].append(rid)
        key = stable_id(rec)
        if not key:
            errors.append("MISSING_STABLE_IDENTIFIER:" + str(rid))
        candidates = [normalize(rec.get(name)) for name in FIELDS]
        dois = {value for value in candidates if DOI_RE.match(value)}
        if len(dois) > 1:
            errors.append("CONFLICTING_DOI_FIELDS:" + str(rid))
        for explicit in ("doi", "canonical_doi"):
            value = rec.get(explicit)
            if value is not None and not DOI_RE.match(normalize(value)):
                errors.append("INVALID_EXPLICIT_DOI:" + str(rid))
        if (value := doi(rec)):
            all_doi.append(value)
    duplicate_doi = len(all_doi) - len(set(all_doi))
    duplicate_titles = sum(len(v) - 1 for v in title_groups.values() if len(v) > 1)
    if duplicate_doi:
        errors.append("DOI_COLLISION_MANUAL_STUDY_REPORT_REVIEW_REQUIRED")
    if duplicate_titles:
        errors.append("EXACT_TITLE_COLLISION_REVIEW_REQUIRED")
    for label, actual in (
        ("doi_identified_records", len(all_doi)),
        ("non_doi_record_count", len(records)-len(all_doi)),
        ("unique_normalized_dois", len(set(all_doi))),
        ("exact_doi_collisions", duplicate_doi),
        ("duplicate_normalized_title_groups", duplicate_titles),
    ):
        if manifest.get(label) != actual:
            errors.append("METRIC_MISMATCH:" + label)
    candidates = []
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            score = similarity(a.get("title", ""), b.get("title", ""))
            if score >= 0.56:
                candidates.append((tuple(sorted((a["id"], b["id"]))), round(score, 6)))
    if len(candidates) > MAX_REASONABLE_PAIRS:
        errors.append("SIMILAR_TITLE_COMPARISON_UNBOUNDED")
    current = {identity: score for identity, score in candidates}
    expected = manifest.get("similar_title_review_candidates", [])
    saved = {}
    if not isinstance(expected, list):
        errors.append("CANDIDATE_LIST_NOT_ARRAY")
        expected = []
    for pair in expected:
        a, b = pair.get("a"), pair.get("b")
        identity = tuple(sorted((a, b)))
        if identity in saved:
            errors.append("DUPLICATE_CANDIDATE:" + str(identity))
        saved[identity] = pair.get("score")
        if a not in record_ids or b not in record_ids:
            errors.append("CANDIDATE_RECORD_MISSING:" + str(identity))
        if pair.get("auto_merge_authorized") is not False:
            errors.append("SILENT_SOURCE_COLLAPSE_FORBIDDEN:" + str(identity))
        if pair.get("same_study_confirmed") is not False:
            errors.append("STUDY_IDENTITY_NOT_VERIFIED:" + str(identity))
        if not isinstance(pair.get("provisional_relation"), str) or not pair["provisional_relation"]:
            errors.append("CANDIDATE_INTERPRETATION_MISSING:" + str(identity))
    if current != saved:
        errors.append("SIMILAR_TITLE_CANDIDATES_CHANGED_WITHOUT_REVIEW")
    pair = manifest.get("hard_negative_control", {})
    if pair.get("record_ids") != ["C09-16", "C09-17"] or not all(
        r in record_ids for r in ("C09-16", "C09-17")
    ):
        errors.append("C09_CONTRAST_LOST")
    elif {doi(record_ids[r]) for r in ("C09-16", "C09-17")} != {
        "10.1073/pnas.1408988111", "10.1073/pnas.1706693114"
    }:
        errors.append("C09_DISTINCT_ORIGINAL_PAPERS_FUSED")
    if pair.get("status") != "DISTINCT_PUBLICATIONS_WITH_DIFFERENT_DECISION_MODES__NOT_EXACT_REPLICATION":
        errors.append("C09_MODALITY_LIMIT_ERASED")
    if not manifest.get("known_limits") or not manifest.get("recommended_next_step"):
        errors.append("MISSING_HONEST_SCOPE_AND_FOLLOW_UP")
    return errors


def test_mutations(rows: list[dict], manifest: dict) -> int:
    if (errors := analyze(rows, manifest)):
        raise AssertionError("Baseline fails: " + str(errors))
    def edit(index: int, method):
        copied = copy.deepcopy(rows)
        method(copied[index])
        return copied

    mutants = []
    by = {r["id"]: i for i, r in enumerate(rows)}
    # Duplicate an existing DOI in another independently inventoried record.
    mutants.append(("duplicate_doi", edit(by["C09-17"], lambda r: r.update(
        {"doi": "10.1073/pnas.1408988111", "canonical_key": "doi:10.1073/pnas.1408988111"}))))
    mutants.append(("case_normalization_collision", edit(by["C09-17"], lambda r: r.update(
        {"doi": "10.1073/PNAS.1408988111", "canonical_key": "doi:10.1073/PNAS.1408988111"}))))
    mutants.append(("conflicting_doi_fields", edit(by["C09-17"], lambda r: r.update(
        {"doi": "10.0000/bad-crosswalk"}))))
    mutants.append(("distinct_modality_hidden", edit(by["C09-17"], lambda r: r.update(
        {"title": "Harm to others outweighs harm to self in moral decision making"}))))
    mutants.append(("missing_negative_control", [r for r in rows if r.get("id") != "C09-17"]))
    mutants.append(("missing_identifier", edit(by["C09-17"], lambda r: [
        r.pop(field, None) for field in FIELDS + IDS])))
    for label, records in mutants:
        if not analyze(records, manifest):
            raise AssertionError("MUTATION_NOT_DETECTED:" + label)
    for label, change in (
        ("invented_unique_studies", {"study_identity_verified_count": 233}),
        ("erase_uncertainty", {"manifest_status": "STUDY_DEDUP_FULLY_VERIFIED"}),
        ("inflate_record_count", {"source_record_count": 240}),
        ("collapse_contrast", {"hard_negative_control": {**manifest["hard_negative_control"],
                                                      "status": "ONE_STUDY"}}),
    ):
        copy_doc = copy.deepcopy(manifest)
        copy_doc.update(change)
        if not analyze(rows, copy_doc):
            raise AssertionError("MUTATION_NOT_DETECTED:" + label)
    copy_doc = copy.deepcopy(manifest)
    copy_doc["similar_title_review_candidates"][0]["auto_merge_authorized"] = True
    if not analyze(rows, copy_doc):
        raise AssertionError("MUTATION_NOT_DETECTED:unsafe_automatic_merge")
    return len(mutants) + 5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows, problems = read_sources(manifest)
    problems.extend(analyze(rows, manifest))
    if problems:
        for item in problems:
            print("PI_RAMP_IDENTITY_FAIL:", item)
        return 1
    print("PI-RAMP C01-C12 identity: STRUCTURAL PASS;"
          " records=%d, DOI=%d, alternative ID=%d, title-review pairs=%d"
          % (len(rows), manifest["doi_identified_records"],
             manifest["non_doi_record_count"],
             len(manifest["similar_title_review_candidates"])))
    if args.self_test:
        n = test_mutations(rows, manifest)
        print("PI-RAMP evidence identity adverse mutations rejected: %d/%d" % (n, n))
    print("LIMIT: no report-to-study deduplication, scientific replication,"
          " corpus-wide novelty or independent source-accuracy certification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
