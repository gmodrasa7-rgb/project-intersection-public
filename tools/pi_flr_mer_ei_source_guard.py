#!/usr/bin/env python3
"""Source-table *transcription* guard for the MER/EI consent/supply audit.

This verifies internal consistency with hand-transcribed May-2025 CESifo WP
Tables 4/7/8; it does NOT fetch an original source PDF, read participants'
microdata, reproduce authors' regressions or identify latent motives.
"""
import copy
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEDGER="research/MER_EI_CONSENT_PROVIDER_ASYMMETRY_EVIDENCE_2026-10-24.json"
KO="research/MER_EI_CONSENT_SUPPLY_ASYMMETRY_2026-10-24_KO.md"
EN="research/MER_EI_CONSENT_SUPPLY_ASYMMETRY_2026-10-24_EN.md"

SOURCE_EXPECTED={
"E_CHOOSER_SOFT":("Table 4 col 1",.117,.017,3000),
"E_CHOOSER_CONSENT":("Table 4 col 3",.134,.017,3000),
"E_ARCHITECT_DEMAND":("Table 7 col 1",.281,.026,1500),
"E_ARCHITECT_CONSENT":("Table 8 col 1",-.010,.028,1895),
"E_STRATEGY_METHOD":("Table 8 col 1",-.057,.024,1895),
}

class EvidenceGuardError(ValueError):
    pass

def require(condition, code):
    if not condition:
        raise EvidenceGuardError(code)

def audit(ledger, ko_text, en_text, rvd_version):
    require(ledger.get("schema_version")=="PI-MER-EI-CONSTRUCT-CONTRAST-2026-10-24-v0.1","SCHEMA_MISMATCH")
    require(ledger.get("rvd_main_expected")==rvd_version=="v0.7.0","RVD_VERSION_UPGRADED_WITHOUT_EVIDENCE")
    require(ledger.get("new_hypotheses")==0 and ledger.get("new_human_or_ai_dataset_experiments")==0
            and ledger.get("author_tables_rerun")==0,"FABRICATED_EMPIRICAL_EVIDENCE")
    require(ledger.get("routine_version_bump") is False,"FALSE_VERSION_PROMOTION")
    require(ledger.get("full_literature_saturation") is False,"FALSE_LITERATURE_SATURATION")
    effects=ledger.get("estimates")
    require(isinstance(effects,list) and len(effects)==len(SOURCE_EXPECTED),"INCOMPLETE_ESTIMATE_SET")
    found=set()
    for e in effects:
        i=e.get("id")
        require(i in SOURCE_EXPECTED and i not in found,"DUPLICATE_OR_UNKNOWN_ESTIMATE")
        found.add(i)
        table,b,se,n=SOURCE_EXPECTED[i]
        require(e.get("table")==table and e.get("coef")==b and e.get("se_hc3")==se and e.get("n")==n,
                "SOURCE_TABLE_TRANSCRIPTION_CHANGED:"+i)
        require(e.get("reproduction")=="TRANSCRIBED_FROM_SOURCE_NOT_RERUN","SOURCE_REPRODUCTION_OVERCLAIM:"+i)
        bounds=e.get("approx_normal_95_percent_points")
        expected=[round((b-1.96*se)*100,2),round((b+1.96*se)*100,2)]
        require(bounds==expected,"CI_ARITHMETIC_OR_LEVEL_INVALID:"+i)
        require(e.get("ci_status")=="APPROX_NORMAL_1_96x_PUBLISHED_HC3_SE_NO_REANALYSIS","CI_FALSE_CERTIFICATE:"+i)
    require(found==set(SOURCE_EXPECTED),"MISSING_SOURCE_ESTIMATE")
    null=next(e for e in effects if e["id"]=="E_ARCHITECT_CONSENT")
    require(null["approx_normal_95_percent_points"][0]<0<null["approx_normal_95_percent_points"][1],
            "NULL_EQUIVALENCE_FALSE_GREEN")
    require(null["significance"]=="NO_STATISTICALLY_SIGNIFICANT_DIFFERENCE",
            "SOURCE_NULL_MISCLASSIFIED")
    require("NOT evidence of equivalence" in null.get("false_inference",""),
            "UNQUALIFIED_EQUIVALENCE_FROM_NONSIGNIFICANCE")
    require("not an independent statistical reanalysis" in ledger.get("methods_note",""),
            "CI_AS_AUTHOR_DATA_REPRODUCTION")
    require(ledger.get("source_audit",{}).get("human_text_reason_model","").startswith("GPT-4o-mini"),
            "LLM_REASON_TAGS_NOT_LABELED")
    for tag,txt,counterpart in [
        ("ko",ko_text,EN),("en",en_text,KO),
    ]:
        require(f"<!-- PI-LANGUAGE: {tag} -->" in txt,"MISSING_LANGUAGE_TAG:"+tag)
        require(f"<!-- PI-MIRROR: {counterpart} -->" in txt,"MISSING_MIRROR:"+tag)
        require("v0.7.0" in txt,"MISSING_UNTESTED_VERSION:"+tag)
    require("원자료" in ko_text and "미" in ko_text,"KOREAN_EVIDENCE_LIMIT_MISSING")
    require("not independent data replication" in en_text.lower(),"EN_REPRO_LIMIT_MISSING")
    return {"status":"SOURCE_TRANSCRIPTION_AND_SCOPE_ONLY",
            "source_records":len(found),
            "null_effect_equivalence":"NOT_ESTABLISHED",
            "clinical_or_actual_AI_motives":"NOT_TESTED",
            "actual_paper_pdf_reparsed":False,
            "participants_reanalyzed":0}

if __name__=="__main__":
    j=json.loads((ROOT/LEDGER).read_text(encoding="utf-8"))
    v=json.loads((ROOT/"research/RVD_VERSION_MANIFEST.json").read_text(encoding="utf-8"))
    print(json.dumps(audit(j,(ROOT/KO).read_text(encoding="utf-8"),
              (ROOT/EN).read_text(encoding="utf-8"),v["current_version"]),ensure_ascii=False))
