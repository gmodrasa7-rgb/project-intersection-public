#!/usr/bin/env python3
"""Scope-limited publication ledger guard, NOT a scientific source replication.

Validates source-record identity, negative result retention, release boundaries,
and bilingual cross-reference. This is software integrity, not evidence that any
original paper's effect size, theory, or data has been independently reproduced.
"""
from copy import deepcopy
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"research/MER_EI_MOTIVE_SEPARATION_PRIOR_ART_2026-10-30.json"
EN=ROOT/"research/MER_EI_MOTIVE_SEPARATION_2026-10-30_EN.md"
KO=ROOT/"research/MER_EI_MOTIVE_SEPARATION_2026-10-30_KO.md"

EXPECTED={
    "DANA_CAIN_DAWES_2006", "DANA_WEBER_KUANG_2007",
    "DELLAVIGNA_LIST_MALMENDIER_2012","LAZEAR_MALMENDIER_WEBER_2012",
    "TONIN_VLASSOPOULOS_2013","KOBIS_ETAL_2025",
    "VONBIEBERSTEIN_FEESS_PACKHAM_2026","HUHOLT_SZECH_2026",
    "DONG_ZHENG_2026",
}


def valid(data):
    if data.get("schema")!="MER_EI_MOTIVE_SEPARATION_PRIOR_ART_V1":
        raise ValueError("SCHEMA_DRIFT")
    if data.get("new_R_numbered_hypotheses")!=0 or data.get("actual_RVD_empirical_replications")!=0:
        raise ValueError("FALSE_SCIENTIFIC_PROMOTION")
    if data.get("rvd_main_version")!="v0.7.0":
        raise ValueError("UNAUTHORIZED_RVD_VERSION_CHANGE")
    records=data.get("studies")
    if not isinstance(records,list) or len(records)!=9 or data.get("source_count")!=len(records):
        raise ValueError("SOURCE_COUNT_INCONSISTENT")
    ids=[x.get("id") for x in records]
    if len(ids)!=len(set(ids)) or set(ids)!=EXPECTED:
        raise ValueError("MISSING_DUPLICATE_OR_UNEXPECTED_LINEAGE")
    for src in records:
        if not src.get("result") or not src.get("nonclaim") or not src.get("source_scope"):
            raise ValueError("CAVEAT_OR_RESULT_REMOVED")
        u=urlparse(src.get("url",""))
        if u.scheme!="https" or not u.netloc or not src.get("title") or not src.get("authors"):
            raise ValueError("UNSOURCED_OR_MALFORMED_ORIGIN")
    by_id={x["id"]:x for x in records}
    negative=by_id["VONBIEBERSTEIN_FEESS_PACKHAM_2026"]["result"].lower()
    if not ("no evidence" in negative or "no increase" in negative):
        raise ValueError("NEGATIVE_DELEGATION_RESULT_ERASED")
    nature=by_id["KOBIS_ETAL_2025"]["result"].lower()
    if "not reliably request" not in nature and "did not reliably request" not in nature:
        raise ValueError("NATURE_NULL_PRINCIPAL_COMPARISON_ERASED")
    if "unethical" not in nature or "complied" not in nature:
        raise ValueError("NATURE_REQUEST_VS_EXECUTION_DISTINCTION_LOST")
    return True


def main():
    d=json.loads(PATH.read_text(encoding="utf-8"))
    assert valid(d)
    en=EN.read_text(encoding="utf-8")
    ko=KO.read_text(encoding="utf-8")
    if "<!-- PI-LANGUAGE: en -->" not in en or "<!-- PI-LANGUAGE: ko -->" not in ko:
        raise ValueError("LANGUAGE_MARKERS_MISSING")
    if EN.name not in ko or KO.name not in en:
        raise ValueError("RECIPROCAL_LINKS_MISSING")
    if "UNIDENTIFIED" not in ko or "non-identification" not in en.lower():
        raise ValueError("MOTIVE_BOUNDARY_LOST")
    if "no evidence" not in en.lower() or "증거를 찾지 못" not in ko:
        raise ValueError("COUNTEREVIDENCE_LOST_FROM_DOCS")
    # Mutation tests: each fault must be rejected. These are schema checks,
    # not invented human observations or authoritative paper verification.
    mutations=[]
    q=deepcopy(d);q["new_R_numbered_hypotheses"]=1;mutations.append(q)
    q=deepcopy(d);q["studies"]=q["studies"][:-1];mutations.append(q)
    q=deepcopy(d);q["studies"][0]["id"]=q["studies"][1]["id"];mutations.append(q)
    q=deepcopy(d);q["rvd_main_version"]="v0.8.0";mutations.append(q)
    q=deepcopy(d)
    for x in q["studies"]:
        if x["id"]=="VONBIEBERSTEIN_FEESS_PACKHAM_2026":
            x["result"]="Delegation increases dishonesty across all contexts."
    mutations.append(q)
    q=deepcopy(d)
    for x in q["studies"]:
        if x["id"]=="KOBIS_ETAL_2025":
            x["result"]="Machines always receive more dishonest instructions."
    mutations.append(q)
    for bad in mutations:
        try:
            valid(bad)
        except ValueError:
            continue
        raise AssertionError("MUTANT_ESCAPED_INTEGRITY_CHECK")
    print("PASS: 9 original-author identities, adverse evidence, EN/KO links and six negative mutations")
    print("SCOPE: software/source-ledger integrity only; no independent human or AI empirical validation")


if __name__=="__main__":
    main()
