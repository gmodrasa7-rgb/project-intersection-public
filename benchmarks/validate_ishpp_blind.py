#!/usr/bin/env python3
"""Check that ISHPP v0.2 blind-phase inputs do not carry direct source identifiers.

This is a structural check, NOT a claim that a public benchmark was unseen by a
model or that case wording cannot reveal the identity of the original source.
"""
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ALLOWED_BLIND_KEYS = {"case_id", "blind_case", "questions"}
SOURCE_ID_PATTERN = re.compile(r"\bS\d{3}\b", re.IGNORECASE)
DIRECT_LINK_PATTERN = re.compile(r"https?://|www\.|doi\.org/", re.IGNORECASE)


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def validate(blind, legacy, mapping, registry):
    """Return failures instead of silently declaring a blind/independent study."""
    errors = []
    if not isinstance(blind, list) or not isinstance(legacy, list):
        return ["blind and legacy data must be lists"]
    if not isinstance(mapping, dict) or not isinstance(registry, dict):
        return ["source linkage and registry must be objects"]
    if mapping.get("schema_version") != "0.2" or mapping.get("status") != "POST_REVEAL_ONLY":
        errors.append("case-source mapping must be explicitly post-reveal v0.2")
    if not isinstance(mapping.get("case_sources"), dict):
        return errors + ["case_sources must be an object"]

    legacy_by_id = {}
    for item in legacy:
        if not isinstance(item, dict) or not item.get("case_id"):
            errors.append("invalid legacy record")
            continue
        cid = item["case_id"]
        if cid in legacy_by_id:
            errors.append("duplicate legacy case " + cid)
        legacy_by_id[cid] = item
    blind_ids = set()
    for item in blind:
        if not isinstance(item, dict):
            errors.append("invalid blind record")
            continue
        cid = item.get("case_id")
        if not isinstance(cid, str) or not cid:
            errors.append("missing case_id")
            continue
        if cid in blind_ids:
            errors.append("duplicate blind case " + cid)
        blind_ids.add(cid)
        extra = set(item) - ALLOWED_BLIND_KEYS
        if extra:
            errors.append(cid + ": forbidden blind-phase keys: " + ", ".join(sorted(extra)))
        payload = json.dumps(item, ensure_ascii=False)
        if SOURCE_ID_PATTERN.search(payload) or DIRECT_LINK_PATTERN.search(payload):
            errors.append(cid + ": direct source identifier / URL leaked")
        if not isinstance(item.get("blind_case"), str) or not item["blind_case"].strip():
            errors.append(cid + ": missing case text")
        if not isinstance(item.get("questions"), list) or not item["questions"]:
            errors.append(cid + ": missing questions")
        old = legacy_by_id.get(cid)
        if old is not None:
            expected = {key: old.get(key) for key in ("case_id", "blind_case", "questions")}
            if item != expected:
                errors.append(cid + ": v0.2 facts/questions changed beyond identifier removal")
    if not set(legacy_by_id).issubset(blind_ids):
        errors.append("blind set omits frozen v0.1 cases")
    links = mapping["case_sources"]
    if set(links) != blind_ids:
        errors.append("post-reveal linkage must cover precisely the blind cases")
    for cid, source_ids in links.items():
        if not isinstance(source_ids, list) or not source_ids:
            errors.append(str(cid) + ": empty or invalid source list")
            continue
        if len(set(source_ids)) != len(source_ids):
            errors.append(str(cid) + ": repeated source ID")
        for sid in source_ids:
            if sid not in registry:
                errors.append(str(cid) + ": unresolvable source identifier " + str(sid))
        if cid in legacy_by_id and source_ids != legacy_by_id[cid].get("source_ids"):
            errors.append(str(cid) + ": source lineage changed relative to v0.1")
    return errors


def main():
    blind = read_jsonl(HERE / "ISHPP_REAL_WORLD_BLIND_SET_v0_2.jsonl")
    legacy = read_jsonl(HERE / "ISHPP_REAL_WORLD_BLIND_SET_v0_1.jsonl")
    mapping = json.loads((HERE / "ISHPP_REAL_WORLD_CASE_SOURCES_v0_2.json").read_text(encoding="utf-8"))
    registry = json.loads((HERE / "ISHPP_REAL_WORLD_SOURCE_MAP_v0_1.json").read_text(encoding="utf-8"))
    errors = validate(blind, legacy, mapping, registry)
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print(f"PASS: source-ID separation for {len(blind)} cases, including {len(legacy)} frozen v0.1 cases; actual blinding UNVERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
