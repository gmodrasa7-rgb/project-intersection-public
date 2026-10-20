#!/usr/bin/env python3
"""PI research-version registry: bounded configuration/provenance guard.

THIS CHECKS FILE/PR STATE, NOT SCIENTIFIC TRUTH, MODEL MOTIVES, OR INDEPENDENT REPLICATION.
No third-party dependencies. Network checks are explicit; unavailable => UNVERIFIED, never PASS.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "gmodrasa7-rgb/project-intersection-public"
MANIFEST = "research/RESEARCH_VERSION_REGISTRY.json"
GUIDE = "navigation/RESEARCH_VERSIONS_EN_KO.md"
README = "README.md"
IDS = {"PI", "VC", "MER", "EI", "ECR", "IVS-0R", "ICM", "RGBM",
       "CCPH", "RVD", "PI-RAMP", "PI-ROADMAP", "DCA-0",
       "E007", "E008", "E009", "E010", "C13"}
VERSION = re.compile(r"^(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)$")
STATES = {"MAIN", "MAIN_WITH_UNMERGED_PROPOSAL", "PROPOSAL_ONLY"}
FIXED_EVIDENCE = {
    "RVD": "CONCEPTUAL_HYPOTHESIS_UNTESTED",
    "PI-RAMP": "PILOT_NO_READER_EFFECT_MEASUREMENT",
    "E008": "NO_MAIN_POLICY_RESULT",
    "E009": "SYNTHETIC_NEGATIVE_RESULT",
    "E010": "EXPLORATORY_POSTHOC",
}
CANDIDATES = {"ECR": (211, "1.4"), "C13": (248, None)}
VERSIONED_SOURCES = {
    "RVD": "research/RVD_VERSION_MANIFEST.json",
    "PI-RAMP": "protocols/PI_RAMP_V0_3_KO.md",
    "PI-ROADMAP": "research/PI_ROADMAP_OPERATIONAL_GATES_V0_2_3_EN_KO.md",
}

def blob_sha(content: bytes) -> str:
    return hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()

def local_file(root: Path, path: str) -> bytes:
    p = (root / path).resolve()
    if not p.is_relative_to(root.resolve()):
        raise ValueError("Path escapes repository root")
    return p.read_bytes()

def check_local(record: dict, root: Path = ROOT, override: dict[str, bytes] | None = None) -> list[str]:
    problems: list[str] = []
    override = override or {}
    def read(path: str) -> bytes:
        return override[path] if path in override else local_file(root, path)
    if record.get("schema_version") != "0.2.0" or record.get("registry_document_version") != "0.2.0":
        problems.append("SCHEMA_VERSION_NOT_0.2.0")
    if record.get("snapshot_kind") != "CURATED_CURRENT_STATUS_NOT_A_RELEASE_TAG":
        problems.append("SNAPSHOT_SCOPE_NOT_EXPLICIT")
    rows = record.get("entries")
    if not isinstance(rows, list):
        return problems + ["ENTRIES_MISSING"]
    ids = [e.get("id") for e in rows if isinstance(e, dict)]
    if len(ids) != len(set(ids)) or set(ids) != IDS:
        problems.append("RESEARCH_ID_DUPLICATION_OR_LOSS")
    for e in rows:
        if not isinstance(e, dict):
            problems.append("ROW_NOT_OBJECT")
            continue
        rid = e.get("id", "UNKNOWN")
        if not all(isinstance(e.get(x), str) and e.get(x).strip()
                   for x in ("title", "what", "how", "source", "evidence_state")):
            problems.append(f"{rid}: INCOMPLETE_WHY_WHAT_HOW_SOURCE_OR_EVIDENCE")
        if e.get("publication_state") not in STATES:
            problems.append(f"{rid}: INVALID_PUBLICATION_STATE")
        ver = e.get("current_version")
        if ver != "UNASSIGNED" and (not isinstance(ver, str) or not VERSION.fullmatch(ver)):
            problems.append(f"{rid}: CURRENT_VERSION_FORMAT")
        candidate = e.get("candidate_version")
        if candidate is not None and (not isinstance(candidate, str) or not VERSION.fullmatch(candidate)):
            problems.append(f"{rid}: CANDIDATE_VERSION_FORMAT")
        pr = e.get("candidate_pr")
        if rid in CANDIDATES:
            expected_pr, expected_ver = CANDIDATES[rid]
            if pr != expected_pr or candidate != expected_ver:
                problems.append(f"{rid}: REQUIRED_UNMERGED_PR_NOT_REGISTERED")
            if e.get("publication_state") != ("PROPOSAL_ONLY" if rid == "C13" else "MAIN_WITH_UNMERGED_PROPOSAL"):
                problems.append(f"{rid}: PROPOSAL_PROMOTED_OR_MISCLASSIFIED")
        elif pr is not None or candidate is not None:
            problems.append(f"{rid}: UNEXPECTED_UNVERIFIED_PROPOSAL")
        if e.get("publication_state") == "PROPOSAL_ONLY" and ver != "UNASSIGNED":
            problems.append(f"{rid}: UNMERGED_AS_CURRENT")
        src = e.get("source")
        if not isinstance(src, str):
            problems.append(f"{rid}: INVALID_SOURCE")
            continue
        if src.startswith("https://"):
            expected = f"https://github.com/{REPO}/pull/{pr}"
            if rid != "C13" or src != expected:
                problems.append(f"{rid}: EXTERNAL_OR_UNBOUND_SOURCE")
        else:
            try:
                read(src)
            except (OSError, ValueError):
                problems.append(f"{rid}: SOURCE_PATH_MISSING_OR_ESCAPED")
        declared_sha = e.get("current_source_blob_sha")
        if rid in VERSIONED_SOURCES:
            if src != VERSIONED_SOURCES[rid] or ver == "UNASSIGNED":
                problems.append(f"{rid}: VERSION_NOT_ANCHORED_TO_CANONICAL_SOURCE")
            if not isinstance(declared_sha, str) or not re.fullmatch("[a-f0-9]{40}", declared_sha):
                problems.append(f"{rid}: SOURCE_BLOB_SHA_MISSING")
            else:
                try:
                    content = read(src)
                    if blob_sha(content) != declared_sha:
                        problems.append(f"{rid}: CANONICAL_SOURCE_CHANGED_SINCE_ATTESTATION")
                    if rid == "RVD":
                        source_ver = json.loads(content).get("current_version", "").lstrip("v")
                        if source_ver != ver:
                            problems.append("RVD: MANIFEST_VERSION_MISMATCH")
                    else:
                        name = "PI-RAMP" if rid == "PI-RAMP" else "Research Roadmap"
                        if not re.search(r"\bv" + re.escape(ver) + r"\b", content.decode("utf-8")[:1300], re.I):
                            problems.append(f"{rid}: VERSION_NOT_IN_SOURCE_HEADER")
                except (OSError, ValueError, UnicodeDecodeError, json.JSONDecodeError):
                    problems.append(f"{rid}: CANONICAL_SOURCE_UNREADABLE")
        elif declared_sha is not None:
            problems.append(f"{rid}: UNSUPPORTED_SHA_ANCHOR")
        if rid in FIXED_EVIDENCE and e.get("evidence_state") != FIXED_EVIDENCE[rid]:
            problems.append(f"{rid}: EVIDENCE_BOUNDARY_CHANGED_WITHOUT_REVIEW")
    try:
        guide = read(GUIDE).decode("utf-8")
        readme = read(README).decode("utf-8")
        for tag in ("Original 1 — English", "원본2 — 한국어", "### Temporal failure", "### 시간차 오류"):
            if tag not in guide:
                problems.append(f"GUIDE: MISSING_{tag}")
        if readme.count("navigation/RESEARCH_VERSIONS_EN_KO.md") != 2:
            problems.append("README: TWO_LANGUAGE_ROUTES_REQUIRED")
        for rid in ("RVD", "PI-RAMP", "ECR", "E008", "E009"):
            lines = [line for line in guide.splitlines() if line.startswith("| " + rid + " |")]
            if len(lines) != 2:
                problems.append(f"GUIDE: EN_KO_ROW_MISSING_{rid}")
                continue
            row = next((e for e in rows if e.get("id") == rid), None)
            if row and row["current_version"] != "UNASSIGNED" and not all(
                "v" + row["current_version"] in line for line in lines
            ):
                problems.append(f"GUIDE: MAIN_VERSION_DRIFT_{rid}")
        if "42.35%" not in guide or "3 of 4" not in guide or "3개" not in guide:
            problems.append("GUIDE: NEGATIVE_RESULT_HIDDEN")
        if "no completed main-policy comparison" not in guide.lower() and "no completed main" not in guide.lower():
            problems.append("GUIDE: E008_SCOPE_HIDDEN_EN")
        if "본비교 실험 결과 없음" not in guide and "본 비교실험 결과 없음" not in guide:
            problems.append("GUIDE: E008_SCOPE_HIDDEN_KO")
    except (OSError, ValueError, UnicodeDecodeError):
        problems.append("GUIDE_OR_README_MISSING")
    return problems

def check_remote(record: dict, request_json) -> list[str]:
    problems: list[str] = []
    for e in record["entries"]:
        rid = e["id"]
        if e.get("candidate_pr") is not None:
            pr = int(e["candidate_pr"])
            p = request_json(f"https://api.github.com/repos/{REPO}/pulls/{pr}")
            if p.get("state") != "open" or p.get("merged_at") is not None:
                problems.append(f"{rid}: CANDIDATE_PR_CLOSED_OR_MERGED")
        if e.get("current_source_blob_sha") is not None:
            path = urllib.parse.quote(e["source"], safe="/")
            c = request_json(f"https://api.github.com/repos/{REPO}/contents/{path}?ref=main")
            if c.get("sha") != e["current_source_blob_sha"]:
                problems.append(f"{rid}: LIVE_MAIN_BLOB_CHANGED")
    return problems

def github_json(url: str) -> dict:
    if not url.startswith(f"https://api.github.com/repos/{REPO}/"):
        raise RuntimeError("Unexpected API origin/path")
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "pi-research-version-guard/0.2",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.load(response)

def self_test(record: dict) -> int:
    baseline = check_local(record)
    if baseline:
        print("BASELINE FAIL: " + " / ".join(baseline))
        return 1
    mutations = []
    def case(name, mutate):
        obj = deepcopy(record)
        mutate(obj)
        mutations.append((name, obj, {}))
    def row(data, rid):
        return next(x for x in data["entries"] if x["id"] == rid)
    case("duplicate-actor", lambda d: d["entries"].append(deepcopy(d["entries"][0])))
    case("erase-VC", lambda d: d["entries"].remove(row(d,"VC")))
    case("invent-RVD-version", lambda d: row(d,"RVD").update(current_version="9.9.9"))
    case("downgrade-RAMP-number", lambda d: row(d,"PI-RAMP").update(current_version="0.2.0"))
    case("invent-version-without-source", lambda d: row(d,"VC").update(current_version="1.0.0"))
    case("corrupt-source-SHA", lambda d: row(d,"RVD").update(current_source_blob_sha="0"*40))
    case("erase-source-SHA", lambda d: row(d,"PI-RAMP").update(current_source_blob_sha=None))
    case("ECR-promoted-without-merge", lambda d: row(d,"ECR").update(publication_state="MAIN"))
    case("lose-C13-PR", lambda d: row(d,"C13").update(candidate_pr=None))
    case("restore-RVD-as-unmerged", lambda d: row(d,"RVD").update(candidate_version="0.1.0",candidate_pr=245))
    case("E008-fabricated-result", lambda d: row(d,"E008").update(evidence_state="FIELD_SUCCESS"))
    case("E009-negative-erased", lambda d: row(d,"E009").update(evidence_state="SUPPORTED"))
    case("E010-posthoc-as-confirmatory", lambda d: row(d,"E010").update(evidence_state="CONFIRMED"))
    case("escape-source-path", lambda d: row(d,"VC").update(source="../private.json"))
    case("invent-schema-version", lambda d: d.update(schema_version="1.0.0"))
    for name, obj, extra in mutations:
        faults = check_local(obj, override=extra)
        if not faults:
            print("FALSE PASS: " + name)
            return 1
    bad_guide = local_file(ROOT, GUIDE).decode("utf-8").replace("42.35%", "success!")
    if not check_local(record, override={GUIDE: bad_guide.encode()}):
        print("FALSE PASS: negative-evidence-redaction")
        return 1
    fake = lambda url: {"state":"closed", "merged_at":"2026-10-20T14:02:53Z"} if "/pulls/" in url else {"sha":"0"*40}
    r = check_remote(record, fake)
    if not any("CANDIDATE_PR_CLOSED" in x for x in r) or not any("LIVE_MAIN_BLOB_CHANGED" in x for x in r):
        print("FALSE PASS: simulated time/race mutation")
        return 1
    print(f"PASS: 18 negative controls detected (16 local including guide redaction + 2 remote classes)")
    return 0

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--remote", action="store_true")
    args = ap.parse_args()
    try:
        manifest = json.loads(local_file(ROOT, MANIFEST))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"UNVERIFIED: manifest unreadable: {exc}")
        return 2
    problems = check_local(manifest)
    if problems:
        print("FAIL: configuration/provenance mismatches:\n- " + "\n- ".join(problems))
        return 1
    if args.self_test:
        return self_test(manifest)
    if args.remote:
        try:
            drift = check_remote(manifest, github_json)
        except (OSError, ValueError, urllib.error.URLError, TimeoutError, RuntimeError, KeyError) as exc:
            print(f"UNVERIFIED: GitHub source state unavailable: {type(exc).__name__}: {exc}")
            return 2
        if drift:
            print("FAIL: live GitHub drift:\n- " + "\n- ".join(drift))
            return 1
        print("PASS: time-scoped GitHub version/proposal-status checks; scientific claims UNVERIFIED")
        return 0
    print("PASS: local version/provenance consistency; not scientific validation")
    return 0

if __name__ == "__main__":
    sys.exit(main())
