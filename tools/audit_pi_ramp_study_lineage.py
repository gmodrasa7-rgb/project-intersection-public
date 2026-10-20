#!/usr/bin/env python3
"""PI-RAMP v0.5: check evidence-unit boundaries and original-paper lineage.

Structural deterministic audit; NOT independent replication or scientific proof.
Run: python tools/audit_pi_ramp_study_lineage.py --self-test
"""
from __future__ import annotations
import argparse
import copy
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "evaluation/pi_ramp/STUDY_LINEAGE_REPLICATION_AUDIT_20261021.json"
BASE = ROOT / "evaluation/pi_ramp/PRIOR_ART_C01_C12_IDENTITY_AUDIT_20261020.json"
CATEGORIES = {
    "PARTIAL_TASK_REPLICATION_WITH_MODALITY_EXTENSION",
    "FOLLOWUP_MECHANISM_DISTINCTION",
    "DISTINCT_FORMAL_EVOLUTIONARY_ANALYSES",
    "RELATED_FORMAL_PARETO_RIGHTS_RESPONSE",
    "CROSS_DOMAIN_ANALOGY_NOT_REPLICATION",
    "SAME_AUTHORS_FORMAL_FOLLOWUP",
}
EXPECTED_RELATIONS = {
    frozenset(("C09-16", "C09-17")): "PARTIAL_TASK_REPLICATION_WITH_MODALITY_EXTENSION",
    frozenset(("PI-C07-09", "PI-C07-15")): "FOLLOWUP_MECHANISM_DISTINCTION",
    frozenset(("EI-C01-13", "EI-C01-14")): "DISTINCT_FORMAL_EVOLUTIONARY_ANALYSES",
    frozenset(("C09-02", "C09-04")): "RELATED_FORMAL_PARETO_RIGHTS_RESPONSE",
    frozenset(("PI-C05-07", "PI-C04-11")): "CROSS_DOMAIN_ANALOGY_NOT_REPLICATION",
    frozenset(("EI-C01-04", "EI-C01-05")): "SAME_AUTHORS_FORMAL_FOLLOWUP",
}
HUMAN_PAPER = "PI-C05-07"
LLM_PAPER = "PI-C04-11"
REPLICATION = "PI-C05-17"
KNOWN_SOURCE = "https://pmc.ncbi.nlm.nih.gov/articles/PMC5453400/"
VALID_OVERLAP = {"UNKNOWN", "NOT_APPLICABLE_FORMAL",
                 "DISTINCT_ENTITY_CLASS", "DISTINCT_RECRUITMENT_DESCRIBED"}


def load_originals(base: dict) -> tuple[dict, list[str]]:
    found = {}
    issues = []
    for file in base.get("source_inputs", []):
        raw = ROOT / file["path"]
        if not raw.is_file():
            issues.append("ORIGINAL_SOURCE_ABSENT:" + file["path"])
            continue
        data = json.loads(raw.read_text(encoding="utf-8"))
        for r in data.get("records", []):
            rid = r.get("id")
            if not isinstance(rid, str) or rid in found:
                issues.append("DUPLICATE_ORIGINAL_RECORD_ID:" + str(rid))
            found[rid] = r
    return found, issues


def doi(r: dict) -> str | None:
    for key in ("doi", "canonical_doi", "canonical_key", "stable_key", "key"):
        value = r.get(key)
        if not isinstance(value, str):
            continue
        v = re.sub(r"^(?:doi:|https?://doi.org/)", "", value.lower().strip())
        if re.match(r"^10\.\d{4,9}/", v):
            return v
    return None


def valid_https(v: object) -> bool:
    if not isinstance(v, str):
        return False
    x = urlparse(v)
    return x.scheme == "https" and bool(x.netloc)


def validate(doc: dict, original: dict, base: dict) -> list[str]:
    issues = []
    if doc.get("schema") != "pi-ramp.study-evidence-lineage/v0.5":
        issues.append("SCHEMA_MISMATCH")
    if doc.get("predecessor") != "evaluation/pi_ramp/PRIOR_ART_C01_C12_IDENTITY_AUDIT_20261020.json":
        issues.append("LOST_FROZEN_PREDECESSOR")
    if doc.get("study_identity_verified_count") is not None or doc.get("independently_replication_verified_count") is not None:
        issues.append("INVENTED_VERIFIED_STUDY_OR_REPLICATION")
    if doc.get("measured_reader_effect") is not None or doc.get("no_automatic_merges") is not True:
        issues.append("INVENTED_READER_EFFECT_OR_AUTOMERGE")
    if doc.get("status") != "SOURCE_LINKED_PROVISIONAL_REVIEW_NOT_INDEPENDENT_VALIDATION":
        issues.append("MISLEADING_SCIENTIFIC_CERTIFICATION")
    expected_pairs = {frozenset((p["a"], p["b"])) for p in base["similar_title_review_candidates"]}
    if expected_pairs != set(EXPECTED_RELATIONS):
        issues.append("PREDECESSOR_RELATIONS_DRIFTED")
    pairs = doc.get("pairs", [])
    if not isinstance(pairs, list) or len(pairs) != 6:
        issues.append("PAIR_COUNT_INCORRECT")
        pairs = []
    seen = set()
    for p in pairs:
        ids = p.get("ids")
        if not isinstance(ids, list) or len(ids) != 2 or len(set(ids)) != 2:
            issues.append("MALFORMED_PAIR")
            continue
        k = frozenset(ids)
        if k in seen:
            issues.append("DUPLICATE_PAIR")
        seen.add(k)
        if k not in EXPECTED_RELATIONS or p.get("relation") != EXPECTED_RELATIONS.get(k):
            issues.append("CONTRAST_RELATION_INCORRECT:" + ",".join(ids))
        if p.get("relation") not in CATEGORIES:
            issues.append("UNKNOWN_RELATION_TYPE")
        if any(n not in original for n in ids):
            issues.append("PAIR_RECORD_MISSING:" + ",".join(ids))
        elif doi(original[ids[0]]) == doi(original[ids[1]]):
            issues.append("DOI_COLLISION_NOT_DECLARED")
        for source in p.get("sources", []):
            if not valid_https(source):
                issues.append("INVALID_SOURCE_URL")
        if len(p.get("sources", [])) != 2:
            issues.append("NEED_BOTH_ORIGINAL_SOURCES")
        if not p.get("specific") or not p.get("reading_limit") or not p.get("evidence"):
            issues.append("NO_OBSERVATION_OR_ACCESS_BOUNDARY")
        if p.get("auto_merge_authorized") is not False or p.get("independent_replication_certified") is not False:
            issues.append("UNSUPPORTED_PAIR_MERGE_OR_INDEPENDENCE")
        if p.get("study_identity") != "UNKNOWN_OR_NOT_APPLICABLE":
            issues.append("UNKNOWN_STUDY_IDENTITY_FALSIFIED")
        if p.get("sample_overlap") not in VALID_OVERLAP:
            issues.append("INVALID_PARTICIPANT_OVERLAP_STATUS")
        if p.get("claim_scope") != "CONTEXT_BOUND_ONLY":
            issues.append("UNIVERSALIZED_RESULT")
    if seen != expected_pairs:
        issues.append("SIX_PREDECLARED_CONTRASTS_NOT_ALL_PRESENT")
    edges = doc.get("replication_edges", [])
    if not isinstance(edges, list) or len(edges) != 2:
        issues.append("REPLICATION_EDGE_COUNT_WRONG")
        edges = []
    graph = {e.get("edge_id"): e for e in edges}
    if len(graph) != 2 or set(graph) != {"E-RAND-STUDY7-RRR", "E-RAND-LLM-ANALOGY"}:
        issues.append("EVIDENCE_GRAPH_INCOMPLETE")
    for e in edges:
        if e.get("from") not in original or e.get("to") not in original:
            issues.append("DANGLING_PUBLICATION_REFERENCE")
        if not valid_https(e.get("source")) or not valid_https(e.get("original_source")):
            issues.append("UNSUPPORTED_PRIMARY_SOURCE")
        if e.get("claims_full_original_article_replicated") is not False:
            issues.append("FALSE_WHOLE_PAPER_REPLICATION")
        if e.get("shares_original_participants") is not False:
            issues.append("FALSE_SAMPLE_OVERLAP")
        if not e.get("result") or not e.get("generalization") or not e.get("evidence_status"):
            issues.append("RESULT_OR_COUNTERBOUNDARY_MISSING")
    r=graph.get("E-RAND-STUDY7-RRR", {})
    if (r.get("from"),r.get("to"),r.get("relation")) != (
        HUMAN_PAPER,REPLICATION,"PREREGISTERED_DIRECT_REPLICATION_OF_SUBSTUDY"
    ):
        issues.append("STUDY7_REPLICATION_LINK_LOST")
    if "Study 7" not in str(r.get("replicated_unit")) or "intent-to-treat" not in str(r.get("result")):
        issues.append("STUDY7_SCOPE_OR_ADVERSE_RESULT_ERASED")
    if r.get("source") != KNOWN_SOURCE:
        issues.append("REPLICATION_ORIGINAL_SOURCE_REPLACED")
    a=graph.get("E-RAND-LLM-ANALOGY",{})
    if (a.get("from"),a.get("to"),a.get("relation"),a.get("replicated_unit")) != (
        HUMAN_PAPER,LLM_PAPER,"CROSS_DOMAIN_ANALOGY_NOT_REPLICATION",None
    ):
        issues.append("CROSS_DOMAIN_LLM_FALSE_REPLICATION")
    for key in ("safety_gates","known_limits"):
        if not isinstance(doc.get(key),list) or len(doc[key]) < 4:
            issues.append("BOUNDARIES_ERASED:"+key)
    return issues


def mutation_test(doc: dict, original: dict, base: dict) -> int:
    assert not validate(doc, original, base), validate(doc,original,base)
    variants = [
        ("invent_sample_certification",lambda d:d.update(study_identity_verified_count=12)),
        ("invent_independent_replication",lambda d:d.update(independently_replication_verified_count=1)),
        ("invent_reader_success",lambda d:d.update(measured_reader_effect=0.8)),
        ("enable_auto_merge",lambda d:d.update(no_automatic_merges=False)),
        ("drop_source_pair",lambda d:d["pairs"].pop()),
        ("duplicate_source_pair",lambda d:d["pairs"].append(copy.deepcopy(d["pairs"][0]))),
        ("invent_same_study",lambda d:d["pairs"][0].update(study_identity="SAME")),
        ("convert_contrast_to_replication",lambda d:d["pairs"][0].update(relation="EXACT_REPLICATION")),
        ("erase_fulltext_limit",lambda d:d["pairs"][3].update(reading_limit="")),
        ("fake_independent_review",lambda d:d["pairs"][0].update(independent_replication_certified=True)),
        ("invent_auto_merge",lambda d:d["pairs"][1].update(auto_merge_authorized=True)),
        ("drop_replication",lambda d:d["replication_edges"].pop(0)),
        ("call_llm_a_replication",lambda d:d["replication_edges"][1].update(relation="PREREGISTERED_DIRECT_REPLICATION_OF_SUBSTUDY")),
        ("erase_negative_itt",lambda d:d["replication_edges"][0].update(result="confirmed original effect")),
        ("claim_all_10_replicated",lambda d:d["replication_edges"][0].update(replicated_unit="all 10 experiments")),
        ("alter_external_source",lambda d:d["replication_edges"][0].update(source="https://example.com")),
        ("wrong_human_to_llm_bridge",lambda d:d["replication_edges"][1].update(to="PI-C05-17")),
    ]
    for name,edit in variants:
        m=copy.deepcopy(doc)
        edit(m)
        if not validate(m, original, base):
            raise AssertionError("UNDISCOVERED_HARMFUL_MUTATION:"+name)
    return len(variants)


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    a=p.parse_args()
    data=json.loads(AUDIT.read_text(encoding="utf-8"))
    predecessor=json.loads(BASE.read_text(encoding="utf-8"))
    originals, errors=load_originals(predecessor)
    errors.extend(validate(data,originals,predecessor))
    if errors:
        for issue in errors:
            print("STUDY_LINEAGE_AUDIT_FAIL:",issue)
        return 1
    print("PI-RAMP v0.5 source lineage: STRUCTURAL PASS; 6 contrasts + 2 evidence edges")
    if a.self_test:
        n=mutation_test(data,originals,predecessor)
        print(f"Negative semantic distortions caught: {n}/{n}")
    print("CAUTION: no independent source-to-study equivalence or real-world validity established")
    return 0

if __name__ == "__main__":
    sys.exit(main())
