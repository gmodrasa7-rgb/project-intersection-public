#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "knowledge" / "graph.json"
SOURCE_REGISTRY = ROOT / "knowledge" / "source-registry.json"

allowed_entity_types = {
    "research_question", "claim", "governance_rule", "prior_art", "experiment",
    "evidence", "historical_case", "negative_control", "failure", "correction"
}
allowed_relations = {
    "has_claim", "tested_by", "produced", "supported_by", "challenged_by",
    "prior_art_for", "corrected_by", "narrows", "governs", "illustrates",
    "negative_control_for", "derived_from"
}

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

data = json.loads(GRAPH.read_text(encoding="utf-8"))
source_registry = json.loads(SOURCE_REGISTRY.read_text(encoding="utf-8"))
require(data.get("schema_version") == "1.0", "Unexpected knowledge graph schema version.")
meta = data.get("meta", {})

require(source_registry.get("schema_version") == "1.0", "Unexpected source registry schema version.")
systems = source_registry.get("systems", [])
require(bool(systems), "Source registry has no systems.")
system_ids = [s.get("system_id") for s in systems]
require(len(system_ids) == len(set(system_ids)), "Duplicate source-registry system IDs detected.")
source_ids = []
for system in systems:
    require(bool(system.get("name")), f"{system.get('system_id', '<missing>')}: missing source system name.")
    require(bool(system.get("project_reuse_decision")), f"{system.get('system_id', '<missing>')}: missing reuse decision.")
    require(bool(system.get("rights_boundary")), f"{system.get('system_id', '<missing>')}: missing rights boundary.")
    sources = system.get("sources") or []
    require(bool(sources), f"{system.get('system_id', '<missing>')}: no source records.")
    for src in sources:
        sid = src.get("source_id")
        source_ids.append(sid)
        require(bool(sid), "Source registry record missing source_id.")
        require(bool(src.get("title")), f"{sid}: missing title.")
        require(bool(src.get("source_type")), f"{sid}: missing source_type.")
        require(bool(src.get("url") or src.get("doi")), f"{sid}: missing URL/DOI.")
        require(bool(src.get("verified_points")), f"{sid}: missing verified design/source findings.")
        require(bool(src.get("rights_note")), f"{sid}: missing rights note.")
require(len(source_ids) == len(set(source_ids)), "Duplicate source IDs detected.")
require(meta.get("canonical_role") == "navigation_index_not_source_of_truth",
        "Knowledge graph must remain a navigation index, not source of truth.")
require(bool(meta.get("updated_at")), "Graph index date missing; readers cannot assess staleness.")
explorer = (ROOT / "knowledge" / "explorer.html").read_text(encoding="utf-8")
require('id="coverage-note"' in explorer and 'state.data.meta?.updated_at' in explorer,
        "Explorer lost graph timestamp/partial-coverage warning.")
readme = (ROOT / "knowledge" / "README.md").read_text(encoding="utf-8")
require("dated, incomplete public navigation subset" in readme,
        "Graph documentation again claims exhaustive current coverage.")

entities = data.get("entities", [])
relations = data.get("relations", [])
ids = [e.get("id") for e in entities]
require(len(ids) == len(set(ids)), "Duplicate entity IDs detected.")
entity_by_id = {e.get("id"): e for e in entities}

for entity in entities:
    eid = entity.get("id", "<missing>")
    require(entity.get("type") in allowed_entity_types, f"{eid}: invalid entity type.")
    for field in ["title_ko", "title_en", "status", "summary_ko", "evidence_class"]:
        require(bool(entity.get(field)), f"{eid}: missing {field}.")
    sources = entity.get("sources")
    require(isinstance(sources, list) and len(sources) > 0, f"{eid}: at least one source required.")
    for source in sources or []:
        kind = source.get("kind")
        locator = source.get("locator")
        require(kind in {"repo_path", "external_url", "doi"}, f"{eid}: invalid source kind.")
        require(bool(locator), f"{eid}: missing source locator.")
        require(bool(source.get("license_note")), f"{eid}: missing source rights/license note.")
        if kind == "repo_path" and locator:
            parts = Path(locator).parts
            require(not Path(locator).is_absolute() and ".." not in parts,
                    f"{eid}: repository path must not escape root: {locator}")
            if not Path(locator).is_absolute() and ".." not in parts:
                require((ROOT / locator).exists(), f"{eid}: referenced repository path does not exist: {locator}")
        if kind == "external_url" and locator:
            require(locator.startswith("https://"),
                    f"{eid}: unsafe/non-HTTPS external link scheme: {locator}")

relation_ids = [r.get("id") for r in relations]
require(len(relation_ids) == len(set(relation_ids)), "Duplicate relation IDs detected.")

for rel in relations:
    rid = rel.get("id", "<missing>")
    require(rel.get("from") in entity_by_id, f"{rid}: from entity missing.")
    require(rel.get("to") in entity_by_id, f"{rid}: to entity missing.")
    require(rel.get("type") in allowed_relations, f"{rid}: invalid relation type.")
    q = rel.get("qualifiers") or {}
    for field in ["scope", "evidence_class", "source_path"]:
        require(bool(q.get(field)), f"{rid}: qualifier missing {field}.")
    sp = q.get("source_path")
    if sp:
        require((ROOT / sp).exists(), f"{rid}: qualifier source path missing: {sp}")

# Focused recovery gate for founder's 2026-10-14 contribution research.
# This checks *presence, provenance and evidence status*, not case truth or
# independently measured effect sizes. It blocks navigation/metric regression.
import re
focused = {
    "RQ-CCP-20261014": ("research_question", "ACTIVE_RESEARCH_QUESTION_UNVALIDATED"),
    "CL-CCP-20261014": ("claim", "HYPOTHESIS_NOT_FIELD_TESTED"),
    "EX-PICB-20261014": ("experiment", "EXECUTED_PROJECT_SYNTHETIC_LACKS_REAL_CONTRIBUTION_OUTCOMES"),
    "HC-OC-20261014": ("historical_case", "CURATED_MIXED_SOURCE_QUALITIES_NOT_REPRESENTATIVE"),
    "HC-HUM-20261014": ("historical_case", "CURATED_MIXED_SOURCE_QUALITIES_SELECTION_BIAS"),
    "PA-CCP-20261014": ("prior_art", "EXISTING_UPSTREAM_THEORIES_NOT_PI_DISCOVERIES"),
    "NC-CCP-20261014": ("negative_control", "TEST_PROTOCOL_UNEXECUTED"),
}
for eid, (etype, status) in focused.items():
    node = entity_by_id.get(eid, {})
    require(node.get("type") == etype and node.get("status") == status,
            f"2026-10-14 contribution graph node missing or incorrectly promoted: {eid}")
    require(bool(node.get("sources")), f"{eid}: origin path or scholar sources erased")
focused_edges = {f"REL-CCP-{k:03d}" for k in range(1, 9)}
require(focused_edges.issubset(set(relation_ids)),
        "Founder contribution graph lost at least one qualified linkage")
source = (ROOT / "CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md").read_text(encoding="utf-8")
for term in (
    "Continuance–Contribution Pathways Hypothesis",
    "존속–기여 경로 가설",
    "2026-10-14 founder correction: risk detection",
    "2026-10-14 인간 창시자 정정",
    "OBSERVED / PLAUSIBLE / UNKNOWN / NOT_SUPPORTED",
):
    require(term in source, "Bilingual core contribution definition disappeared: " + term)
for prefix, expected in (("OC", 19), ("HC", 15)):
    ids = re.findall(r"^\|\s*(" + prefix + r"\d{2})\s", source, flags=re.M)
    occurrences = {cid: ids.count(cid) for cid in set(ids)}
    require(len(occurrences) == expected and all(n == 2 for n in occurrences.values()),
            f"Wrong {prefix} human case entries: expect {expected} distinct IDs with paired EN and KO")
nav = {
    "PUBLIC_EVIDENCE_INDEX.md": ("Continuance–Contribution Pathways", "존속–기여 경로 가설", "PICB v1"),
    "RESEARCH_TOC.md": ("Continuance–Contribution Pathways", "존속–기여 경로 가설", "19+15"),
    "START_HERE_KO.md": ("존속–기여 경로 가설", "UNKNOWN", "OC01–OC19"),
    "PUBLIC_REVIEW_PACKET.md": ("Continuance–Contribution Pathways", "존속–기여 경로 가설", "19+15"),
    "experiments/picb_v1/README.md": ("P0 second correction: detection and inspiration", "P0 두 번째 성과변수 정정", "NO NEW OBSERVED DATA"),
}
for name, terms in nav.items():
    content = (ROOT / name).read_text(encoding="utf-8")
    for term in terms:
        require(term in content, f"{name} lost mapped contribution evidence/limits: {term}")
require(meta.get("updated_at") == "2026-10-14" and
        "still partial" in (meta.get("coverage_note") or ""),
        "Graph update has falsely become an undated or complete inventory")

# High-risk evidence promotions require explicit narrow scopes.
for rel in relations:
    if rel.get("type") == "supported_by":
        scope = (rel.get("qualifiers") or {}).get("scope", "").lower()
        require(scope not in {"", "general", "universal"}, f"{rel.get('id')}: supported_by scope is too broad.")

# No new structured layer may claim independent evidence without an explicit external source.
independent_labels = {"THIRD_PARTY_RERUN", "INDEPENDENT_IMPLEMENTATION", "EMPIRICAL_VALIDATION"}
for entity in entities:
    if entity.get("evidence_class") in independent_labels:
        external = any(s.get("kind") in {"external_url", "doi"} for s in entity.get("sources", []))
        require(external, f"{entity.get('id')}: independent evidence class requires external source lineage.")

# Public findability regression: five bilingual routes must resolve to existing
# canonical artifacts. This is a structural check, NOT a human comprehension
# trial or an independent verification of the underlying scientific claims.
discovery = json.loads((ROOT / "AI_DISCOVERY_INDEX.json").read_text(encoding="utf-8"))
route = discovery.get("review_tasks") or {}
require(route.get("status") == "NAVIGATION_ONLY_NOT_INDEPENDENT_VALIDATION",
        "Public review routes were promoted from navigation to scientific verification.")
require(route.get("human_guide") == "PUBLIC_REVIEW_PACKET.md",
        "Review-task index no longer identifies its public human guide.")
packet = (ROOT / "PUBLIC_REVIEW_PACKET.md").read_text(encoding="utf-8")
tasks = route.get("tasks") or []
require(isinstance(tasks, list) and len(tasks) == 5,
        "Expected exactly five canonical public-review questions.")
expected_task_ids = [f"NAV-Q{i}" for i in range(1, 6)]
require([t.get("id") for t in tasks if isinstance(t, dict)] == expected_task_ids,
        "Public review-task IDs are incomplete, duplicated or reordered.")

def check_public_path(path, label):
    if not isinstance(path, str) or not path:
        require(False, f"{label}: missing repository path")
        return
    ref = Path(path)
    if ref.is_absolute() or ".." in ref.parts or "://" in path or path.startswith("/"):
        require(False, f"{label}: unsafe or nonlocal repository path: {path}")
        return
    require((ROOT / path).exists(), f"{label}: unresolved repository path: {path}")

levels = (discovery.get("navigation_levels") or {})
for group, expected_len in [
    ("level_1_discovery", 5),
    ("level_2_understanding_and_audit", 8),
    ("level_3_artifacts_and_operations", 9),
]:
    paths = levels.get(group) or []
    require(isinstance(paths, list) and len(paths) == expected_len,
            f"{group}: three-level navigation contract changed")
    for linked in paths:
        check_public_path(linked, group)

for task in tasks:
    if not isinstance(task, dict):
        require(False, "Review-task must be an object.")
        continue
    tid = task.get("id", "<missing>")
    for key in ("question_en", "question_ko", "limitation_en", "limitation_ko"):
        require(bool(task.get(key)), f"{tid}: missing bilingual question/boundary: {key}")
    primary = task.get("primary_path")
    check_public_path(primary, tid)
    require(tid in packet, f"{tid}: human review packet lost task identifier")
    require(isinstance(primary, str) and f"({primary})" in packet,
            f"{tid}: human guide no longer links to its primary source")
    verification_paths = task.get("verification_paths") or []
    require(isinstance(verification_paths, list) and len(verification_paths) > 0,
            f"{tid}: no verification/counterexample source")
    for linked in verification_paths:
        check_public_path(linked, tid)

# Prevent semantic promotion of the four distinct experimental states.
states = (levels.get("representative_experiment_status") or {})
for identifier in ("E007", "E008", "E009", "E010"):
    require(isinstance(states.get(identifier), str) and bool(states[identifier]),
            f"{identifier}: missing scope-limited evidence status")
require("negative" in states.get("E009", "").lower(),
        "E009 synthetic negative result was erased")
require("not executed" in states.get("E008", "").lower(),
        "E008 preregistered protocol was misrepresented as executed")
require("posthoc" in states.get("E010", "").lower(),
        "E010 exploratory posthoc status was erased")

if errors:
    print("KNOWLEDGE GRAPH AUDIT FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Knowledge graph audit passed: {len(entities)} entities, {len(relations)} relations.")
