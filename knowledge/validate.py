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
            require((ROOT / locator).exists(), f"{eid}: referenced repository path does not exist: {locator}")

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

if errors:
    print("KNOWLEDGE GRAPH AUDIT FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Knowledge graph audit passed: {len(entities)} entities, {len(relations)} relations.")
