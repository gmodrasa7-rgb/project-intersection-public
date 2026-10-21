#!/usr/bin/env python3
"""Bounded provenance/status audit for PI-PACD-MIA. Structural only, not science."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = "research/PI_PACD_MIA_SOURCE_CROSSWALK_V0_1_0.json"
EN = "research/PI_PACD_MIA_V0_1_0_EN.md"
KO = "research/PI_PACD_MIA_V0_1_0_KO.md"
ALLOWED_STATUSES = {
    "BOUNDED_SOURCE_REPORT", "SOURCE_THEOREM_CONDITIONAL",
    "THEORETICAL_PRIOR_ART", "UNTESTED_RESEARCH_HYPOTHESIS",
    "OFFICIAL_CASE_RECORD_MIXED_PROCEDURAL_STATES",
    "REGULATOR_FINDINGS_AND_ONGOING_INTERVENTION"
}

class SourceAuditError(ValueError):
    pass

def require(test: bool, reason: str):
    if not test:
        raise SourceAuditError(reason)

def audit(data: dict, english: str, korean: str) -> dict:
    require(type(data) is dict and data.get("research_component") == "PI-PACD-MIA",
            "COMPONENT_MISMATCH")
    require(data.get("global_search_saturation") == "NOT_ESTABLISHED" and
            data.get("complete_fulltext_audit") == "NOT_COMPLETED" and
            data.get("novelty") == "NOT_ESTABLISHED",
            "UNSUPPORTED_LITERATURE_OR_NOVELTY_PROMOTION")
    sources, claims, mechanisms = data.get("sources"), data.get("claims"), data.get("mechanisms")
    require(all(isinstance(x, list) and x for x in (sources, claims, mechanisms)),
            "EMPTY_RESEARCH_INDEX")
    sid = [s.get("id") for s in sources]
    cid = [c.get("id") for c in claims]
    mid = [m.get("id") for m in mechanisms]
    require(len(sid) == len(set(sid)) and len(cid) == len(set(cid))
            and len(mid) == len(set(mid)), "DUPLICATE_IDS")
    require(all(re.fullmatch(r"MIA-S\d{2}", s) for s in sid), "BAD_SOURCE_ID")
    require(all(re.fullmatch(r"MIA-C\d{2}", c) for c in cid), "BAD_CLAIM_ID")
    require(all(s.get("url", "").startswith("https://") and
                s.get("type") and s.get("cautions") and s.get("supports") for s in sources),
            "SOURCE_WITHOUT_PROVENANCE_OR_LIMITS")
    for s in sources:
        require(all(c in cid for c in s["supports"]), "SOURCE_REFERENCES_UNKNOWN_CLAIM")
    for c in claims:
        require(c.get("status") in ALLOWED_STATUSES, "UNSUPPORTED_EVIDENCE_PROMOTION")
        require(c.get("sources_for"), "CLAIM_WITHOUT_SOURCE")
        require(all(s in sid for s in c["sources_for"] + c.get("rival_sources", [])),
                "CLAIM_REFERENCES_UNKNOWN_SOURCE")
        require(c.get("generalization") and c.get("statement"), "CLAIM_WITHOUT_SCOPE")
    for m in mechanisms:
        require(m.get("signature") and m.get("confound") and m.get("test"),
                "MECHANISM_WITHOUT_RIVAL_OR_INTERVENTION")
    cases = data.get("real_world_case_front")
    require(isinstance(cases, list) and len(cases) >= 2, "MISSING_REAL_CASE_BOUNDS")
    require(all(c.get("observed") and c.get("not_observed") and
                all(s in sid for s in c.get("evidence", [])) for c in cases),
            "REAL_CASE_WITHOUT_EVIDENCE_LIMITS")
    require(data.get("planned_protocol", {}).get("status") == "DESIGN_ONLY_NO_PI_MODEL_EXECUTION",
            "UNSUPPORTED_EXPERIMENT_STATUS")
    for document in (english, korean):
        for hypothesis in range(1, 8):
            require(f"MIA-H{hypothesis}" in document, "MISSING_PAIRED_HYPOTHESIS")
        for mechanism in range(1, 5):
            require(f"M{mechanism}" in document, "MISSING_MECHANISM")
        require("RealPage" in document and "CMA" in document,
                "CASE_NOT_LINKED_IN_PAIRED_DOCUMENT")
    return {
        "status": "PROVENANCE_STRUCTURE_PASS_NOT_INDEPENDENT_SCIENCE",
        "sources": len(sources),
        "claims": len(claims),
        "mechanisms": len(mechanisms),
        "official_case_fronts": len(cases),
        "model_trials": 0,
        "field_causal_studies_by_project": 0,
    }

def main():
    data = json.loads((ROOT / LEDGER).read_text(encoding="utf-8"))
    result = audit(data, (ROOT / EN).read_text(encoding="utf-8"),
                   (ROOT / KO).read_text(encoding="utf-8"))
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
