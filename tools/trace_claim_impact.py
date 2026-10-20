#!/usr/bin/env python3
"""PI-CIG v0.1: bounded claim impact graph; provenance != scientific proof.

Source content/claim changes require review, NOT automatic falsification.
Review propagation is only along declared edges, and incompleteness is explicit.
stdlib-only, Python 3.11+. No network, no model-generated classifications.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "knowledge/claim-impact-overlay-v0_1.json"
VERSION_REGISTRY = "research/RESEARCH_VERSION_REGISTRY.json"
SHA = re.compile(r"^[0-9a-f]{40}$")
SCOPED = {"scoped_source", "limitation_boundary", "version_and_evidence_boundary",
          "original_source_crosswalk", "competing_mechanisms", "reassessment_dependency"}
EXPECTED_CLAIMS = {
    "CL-E008-GAP": "NO_MAIN_RESULT",
    "CL-E009-NEG": "SYNTHETIC_NEGATIVE",
    "CL-DCA1-TRANSFER": "TOY_COUNTEREXAMPLE_ONLY",
    "CL-RVD-ORIGINAL": "FORMAL_COUNTEREXAMPLE_ONLY",
    "CL-RVD-MOTIVE": "MECHANISM_UNIDENTIFIED",
    "CL-VC-HARD": "UNRESOLVED",
    "CL-RAMP-EFFECT": "EFFECT_UNMEASURED",
}
EXPECTED_VERSIONS = {"RVD": "0.2.0", "PI-RAMP": "0.4.0", "DCA-1": "0.2.0"}
REQUIRED_SOURCE_PATHS = {
    "experiments/e008/EXECUTABILITY_AUDIT.json",
    "experiments/e009/RESULT.json",
    "experiments/dca1/RESULT.json",
    "research/RVD_VERSION_MANIFEST.json",
    "protocols/PI_RAMP_V0_4_EN_KO.md",
}

def read(path, override=None):
    if override and path in override:
        return override[path]
    p = (ROOT / path).resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError("source escapes root")
    return p.read_bytes()

def sha_bytes(value: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(value)).encode() + b"\0" + value).hexdigest()

def pointer(obj, path):
    current = obj
    for k in path.split("."):
        current = current[k]
    return current

def impact(graph, changed_paths):
    """Return exact shortest declared paths; no inference about missing graph edges."""
    source_by_path = {s["path"]: s["id"] for s in graph["sources"]}
    adjacency = {}
    for e in graph["edges"]:
        adjacency.setdefault(e["from"], []).append((e["to"], e["relation"]))
    found = {}
    changed_paths = sorted(set(changed_paths))
    for path in changed_paths:
        if path not in source_by_path:
            continue
        origin = source_by_path[path]
        q = deque([(origin, [origin])])
        visited = {origin}
        while q:
            node, chain = q.popleft()
            for other, relation in sorted(adjacency.get(node, [])):
                if other in visited:
                    continue
                visited.add(other)
                newchain = chain + [other]
                if other.startswith("CL-"):
                    found.setdefault(other, []).append({
                        "changed_source": path, "dependency_chain": newchain,
                        "decision": "REVIEW_REQUIRED_NOT_AUTO_FALSIFIED"
                    })
                q.append((other, newchain))
    return {
        "scope": graph["scope"],
        "changed_paths": changed_paths,
        "unmapped_changes": sorted(set(changed_paths) - set(source_by_path)),
        "affected_claims": {k: found[k] for k in sorted(found)},
        "scientific_verdict": "NOT_INFERRED",
        "coverage": "BOUNDED_OVERLAY_NOT_EXHAUSTIVE"
    }

def inspect(data, source_override=None, registry_override=None):
    errs = []
    if data.get("schema") != "pi-claim-impact-overlay/v0.1.0":
        errs.append("SCHEMA_MISMATCH")
    if data.get("scope") != "SELECTED_MAIN_ONLY_NOT_COMPLETE_CLAIM_INVENTORY":
        errs.append("INCOMPLETE_SCOPE_HIDDEN")
    if data.get("upstream_graph") != "knowledge/graph.json":
        errs.append("UPSTREAM_GRAPH_PATH_DRIFT")
    sources, claims, edges = data.get("sources"), data.get("claims"), data.get("edges")
    if not all(isinstance(v, list) for v in (sources, claims, edges)):
        return errs + ["GRAPH_ARRAY_MISSING"]
    sid, cid, eid = [x.get("id") for x in sources], [x.get("id") for x in claims], [x.get("id") for x in edges]
    if (len(set(sid)) != len(sid) or len(set(cid)) != len(cid) or len(set(eid)) != len(eid)
        or set(sid).intersection(cid)):
        errs.append("DUPLICATE_NODE_OR_EDGE_ID")
    if len(sources) != 8 or set(cid) != set(EXPECTED_CLAIMS):
        errs.append("BASELINE_COVERAGE_CHANGED_REQUIRE_NEW_METHOD_VERSION")
    if not REQUIRED_SOURCE_PATHS.issubset({s.get("path") for s in sources}):
        errs.append("CRITICAL_SOURCE_OMITTED")
    for c in claims:
        k = c.get("id")
        if c.get("status") != EXPECTED_CLAIMS.get(k):
            errs.append(f"{k}: SCIENTIFIC_STATUS_ESCALATED_OR_LOST")
        for prop in ("title_ko", "title_en", "scope", "action"):
            if not isinstance(c.get(prop), str) or not c[prop].strip():
                errs.append(f"{k}: CLAIM_CONTEXT_MISSING_{prop}")
        if "FIELD_VALIDATED" in c.get("status", "") or "INDEPENDENTLY_VERIFIED" in c.get("status", ""):
            errs.append(f"{k}: UNSUPPORTED_VERIFICATION_CLAIM")
    path_set = set()
    for s in sources:
        ident = s.get("id", "UNKNOWN")
        path = s.get("path")
        if not isinstance(path, str) or path.startswith("/") or ".." in Path(path).parts:
            errs.append(f"{ident}: SOURCE_PATH_INVALID")
            continue
        if path in path_set:
            errs.append("DUPLICATE_SOURCE_PATH")
        path_set.add(path)
        try:
            content = read(path, source_override)
        except (OSError, ValueError):
            errs.append(f"{ident}: SOURCE_UNREADABLE")
            continue
        expected = s.get("sha")
        if not isinstance(expected, str) or not SHA.fullmatch(expected):
            errs.append(f"{ident}: MISSING_SOURCE_SHA")
        elif sha_bytes(content) != expected:
            errs.append(f"{ident}: SOURCE_CONTENT_CHANGED_REVIEW_REQUIRED")
        p = s.get("probe", {})
        try:
            kind = p["kind"]
            if kind == "json_exact":
                actual = pointer(json.loads(content), p["field"])
                # bool compares must not silently pass as int 0 / 1.
                if type(actual) is not type(p["expected"]) or actual != p["expected"]:
                    errs.append(f"{ident}: CRITICAL_EVIDENCE_OR_STATUS_DRIFT")
            elif kind == "contains":
                if p.get("value", "") not in content.decode("utf-8"):
                    errs.append(f"{ident}: CRITICAL_CAVEAT_REMOVED")
            else:
                errs.append(f"{ident}: UNKNOWN_PROBE")
        except (ValueError, UnicodeError, KeyError, TypeError, AttributeError):
            errs.append(f"{ident}: ASSERTION_UNREADABLE")
        if not isinstance(s.get("caveat"), str) or not s["caveat"].strip():
            errs.append(f"{ident}: LIMITATION_ERASED")
    all_nodes = set(sid) | set(cid)
    adj = {node: [] for node in all_nodes}
    incoming = {node: 0 for node in all_nodes}
    for e in edges:
        a, b = e.get("from"), e.get("to")
        if a not in all_nodes or b not in all_nodes or b not in cid:
            errs.append(f"{e.get('id')}: DANGLING_OR_WRONG_DIRECTION_EDGE")
            continue
        if e.get("relation") not in SCOPED:
            errs.append(f"{e.get('id')}: UNKNOWN_EDGE_SEMANTICS")
        if "NOT" not in e.get("meaning", ""):
            errs.append(f"{e.get('id')}: NO_NONINFERENCE_BOUNDARY")
        adj[a].append(b)
        incoming[b] += 1
    start = sorted(n for n, d in incoming.items() if d == 0)
    nseen = 0
    while start:
        a = start.pop()
        nseen += 1
        for b in adj[a]:
            incoming[b] -= 1
            if incoming[b] == 0:
                start.append(b)
    if nseen != len(all_nodes):
        errs.append("CYCLE_CANNOT_DETERMINE_DEPENDENCY_ORDER")
    for c in cid:
        if not any(e.get("to") == c for e in edges):
            errs.append(f"{c}: CLAIM_HAS_NO_REVIEW_INPUT")
    for s in sid:
        if not any(e.get("from") == s for e in edges):
            errs.append(f"{s}: UNUSED_EVIDENCE_SOURCE")
    if data.get("version_registry") != VERSION_REGISTRY:
        errs.append("VERSION_REGISTRY_UNLINKED")
    try:
        reg = json.loads(registry_override) if registry_override else json.loads(read(VERSION_REGISTRY))
        versions = {x["id"]: x["current_version"] for x in reg["entries"]}
        for k, v in EXPECTED_VERSIONS.items():
            if versions.get(k) != v:
                errs.append(f"{k}: VERSION_REGISTRY_SCIENTIFIC_SCOPE_REVIEW_REQUIRED")
    except (KeyError, ValueError, OSError, TypeError):
        errs.append("VERSION_REGISTRY_UNREADABLE")
    return errs

def self_test(data):
    if inspect(data):
        print("BASELINE_FAIL " + " | ".join(inspect(data)))
        return 1
    trials = []
    def mutate(name, modify, overrides=None):
        graph = copy.deepcopy(data)
        modify(graph)
        trials.append((name, graph, overrides))
    mutate("erase-E009-negative", lambda x: next(c for c in x["claims"] if c["id"] == "CL-E009-NEG").update(status="SUPPORTED_FIELD"))
    mutate("promote-E008-no-result", lambda x: next(c for c in x["claims"] if c["id"] == "CL-E008-GAP").update(status="MAIN_POLICY_SUCCESS"))
    mutate("promote-RVD-motive", lambda x: next(c for c in x["claims"] if c["id"] == "CL-RVD-MOTIVE").update(status="AI_SENTIENCE_PROVEN"))
    mutate("hide-coverage-limit", lambda x: x.update(scope="COMPLETE_RESEARCH_AUDIT"))
    mutate("erase-hard-case", lambda x: x["claims"].remove(next(c for c in x["claims"] if c["id"] == "CL-VC-HARD")))
    mutate("duplicate-claim", lambda x: x["claims"].append(copy.deepcopy(x["claims"][0])))
    mutate("remove-E009-source", lambda x: x["sources"].remove(next(s for s in x["sources"] if s["id"] == "SRC-E009-RESULT")))
    mutate("path-traversal", lambda x: x["sources"][0].update(path="../secret.json"))
    mutate("tamper-blob-lock", lambda x: x["sources"][0].update(sha="0"*40))
    mutate("create-dangling-edge", lambda x: x["edges"][0].update(to="CL-NOT-FOUND"))
    mutate("create-cycle", lambda x: x["edges"].append({"id":"EDGE-999","from":"CL-VC-HARD","to":"CL-RVD-MOTIVE","relation":"reassessment_dependency","meaning":"NOT proof"}))
    mutate("erase-source-limitation", lambda x: x["sources"][0].update(caveat=""))
    mutate("introduce-unscoped-relation", lambda x: x["edges"][0].update(relation="causally_proves"))
    mutate("destroy-edge-direction", lambda x: x["edges"][0].update(to="SRC-E009-RESULT"))
    bad = {data["sources"][0]["path"]: b'{"full_decision_benchmark_ready_cases":1}'}
    mutate("fabricate-E008-result", lambda x: None, bad)
    bad = {next(s["path"] for s in data["sources"] if s["id"] == "SRC-E009-RESULT"): b'{"project_v3_vs_best_simple_regret_improvement":0.42348132449545167}'}
    mutate("reverse-E009-result", lambda x: None, bad)
    bad = {next(s["path"] for s in data["sources"] if s["id"] == "SRC-DCA1-RESULT"): b'{"empirical":true}'}
    mutate("mislabel-toy-as-field", lambda x: None, bad)
    for name, graph, overrides in trials:
        if not inspect(graph, overrides):
            print("FALSE_PASS " + name)
            return 1
    sample = impact(data, ["experiments/e009/RESULT.json"])
    expected = {"CL-E009-NEG", "CL-VC-HARD"}
    if set(sample["affected_claims"]) != expected or sample["scientific_verdict"] != "NOT_INFERRED":
        print("FALSE_PASS E009 impact chain")
        return 1
    sample = impact(data, ["research/RVD_CYCLE02_SOURCE_REGISTER_2026-10-20.json"])
    if set(sample["affected_claims"]) != {"CL-RVD-MOTIVE", "CL-VC-HARD"}:
        print("FALSE_PASS RVD lineage chain")
        return 1
    sample = impact(data, ["unregistered/project-paper.md"])
    if sample["affected_claims"] or not sample["unmapped_changes"]:
        print("FALSE_PASS unknown source scope")
        return 1
    print(f"PASS: {len(trials)} injected corruptions + 3 exact impact/unknown-scope checks")
    return 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--changed", action="append", default=[])
    parser.add_argument("--changed-base", help="git revision for changed-path report")
    args = parser.parse_args()
    try:
        data = json.loads(read(MANIFEST))
    except (OSError, ValueError) as exc:
        print("UNVERIFIED graph manifest: " + str(exc))
        return 2
    issues = inspect(data)
    if issues:
        print("HOLD_FOR_REVIEW:\n- " + "\n- ".join(issues))
        return 1
    if args.self_test:
        return self_test(data)
    paths = list(args.changed)
    if args.changed_base:
        try:
            r = subprocess.run(["git", "diff", "--name-only", "--diff-filter=ACDMRT",
                                args.changed_base, "HEAD", "--"],
                               cwd=ROOT, capture_output=True, text=True, check=True, timeout=20)
            paths.extend(x.strip() for x in r.stdout.splitlines() if x.strip())
        except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            print("UNVERIFIED git history / diff unavailable: " + str(exc))
            return 2
    if paths:
        print(json.dumps(impact(data, paths), ensure_ascii=False, indent=2))
    else:
        print("PASS: bounded claim-source contract; no inference about scientific truth")
    return 0

if __name__ == "__main__":
    sys.exit(main())
