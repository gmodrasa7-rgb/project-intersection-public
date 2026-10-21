#!/usr/bin/env python3
"""PI-FLR prior-art transfer guard: source lineage, uncertainty and risk preflight.

This offline verifier does not certify real-world efficacy, legal compliance,
complete literature saturation or model-weight learning. No network or secrets.
"""
from __future__ import annotations
import argparse
import fnmatch
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PATH = "knowledge/PI_FLR_PRIOR_ART_TRANSFER_V0_1_0_EN_KO.json"
REGISTRY = "knowledge/PI_FLR_CASES_V0_1_0.json"
WORKFLOW = ".github/workflows/pi-flr-integrity.yml"
GRADES = {"OPERATIONAL_PRIMARY", "REGULATOR_GUIDANCE", "GOVERNMENT_PRIMARY",
          "INDEPENDENT_GOVERNMENT_AUDIT", "PUBLIC_RISK_FRAMEWORK",
          "PEER_REVIEWED_EXPERIMENT", "PEER_REVIEWED_NEGATIVE",
          "PEER_REVIEWED_CRITICAL_SURVEY", "RESEARCH_PREPRINT", "GOVERNMENT_PRIMARY"}
SAFE_DOMAINS = {"sre.google","www.fda.gov","llis.nasa.gov","www.gao.gov",
                "airc.nist.gov","arxiv.org","proceedings.iclr.cc",
                "papers.neurips.cc","aclanthology.org","safety.microsoft.com","proceedings.mlr.press","www.cs.cornell.edu","csrc.nist.gov","slsa.dev"}
PERMITTED = {"NOT_OBSERVED","REPAIR_CHECKED_SCOPED","RECURRENCE_OBSERVED"}


class PriorArtError(ValueError):
    pass


def need(condition, reason):
    if not condition:
        raise PriorArtError(reason)


def validate(data, registry, workflow):
    need(data.get("id") == "PI-FLR-PRIOR-ART-TRANSFER" and
         data.get("schema_version") == "0.1.0", "IDENTITY_OR_SCHEMA_CHANGED")
    need(re.fullmatch(r"\d+\.\d+\.\d+", data.get("version", "")) is not None,
         "INVALID_VERSION")
    need(data.get("language_order") == ["English primary","Korean secondary"],
         "ENGLISH_PRIMARY_KOREAN_SECONDARY_VIOLATED")
    need(data.get("saturation") == "NOT_ESTABLISHED" and
         "NOT_EMPIRICAL_AI_SELF_IMPROVEMENT" in data.get("scope", ""),
         "FALSE_LITERATURE_SATURATION_OR_SCIENCE_CLAIM")
    sources = data["sources"]
    need(type(sources) is list and len(sources) >= 6, "SOURCE_COVERAGE_TOO_NARROW")
    ids = set()
    for s in sources:
        need(set(s) == {"id","title","lineage","grade","url","lesson","limitation"},
             "INVALID_SOURCE_FIELDS")
        need(s["id"] not in ids, "DUPLICATE_SOURCE")
        ids.add(s["id"])
        u = urlsplit(s["url"])
        need(u.scheme == "https" and u.netloc in SAFE_DOMAINS,
             "UNVERIFIED_SOURCE_LOCATION")
        need(s["grade"] in GRADES, "EVIDENCE_GRADE_UNKNOWN")
        need(len(s["lesson"]) >= 25 and len(s["limitation"]) >= 20,
             "SOURCE_CAVEAT_REMOVED")
        need(s["lineage"].strip(), "UNKNOWN_ORIGIN_FAMILY")
    lookup = {s["id"]:s for s in sources}
    need(any(s["grade"] == "PEER_REVIEWED_NEGATIVE" for s in sources) and
         any(s["grade"] == "INDEPENDENT_GOVERNMENT_AUDIT" for s in sources),
         "NEGATIVE_OR_AUDIT_SOURCE_MISSING")
    case_ids = {c["id"] for c in registry["cases"]}
    ctrl_ids = {c["id"] for c in registry["control_registry"]}
    need(registry["registry_id"] == "PI-FLR", "PARENT_REGISTRY_NOT_FOUND")
    pids = set()
    mapped = set()
    for p in data["principles"]:
        need(set(p) == {"id","priority","title_en","title_ko","support","challenge",
                       "cases","adoption","verification","transfer_status"},
             "PRINCIPLE_SCHEMA_DRIFT")
        need(p["id"] not in pids, "DUPLICATE_PRINCIPLE")
        pids.add(p["id"])
        need(p["priority"] in {"P0","P1"} and
             p["transfer_status"] == "OPERATIONAL_DESIGN_NOT_FIELD_VALIDATED",
             "ASSERTED_REAL_WORLD_EFFICACY")
        need(p["support"] and p["challenge"], "SELF_CONFIRMATION_OR_COUNTEREVIDENCE_MISSING")
        need(len(set(p["support"])) == len(p["support"]) and
             len(set(p["challenge"])) == len(p["challenge"]),
             "DUPLICATE_SOURCE_VOTES")
        need(set(p["support"] + p["challenge"]) <= ids, "UNKNOWN_EVIDENCE_SOURCE")
        need(len({lookup[x]["lineage"] for x in p["support"]}) >= 2,
             "CORRELATED_SOURCE_FAMILIES_NOT_INDEPENDENT")
        need(set(p["cases"]) <= case_ids and p["cases"], "UNKNOWN_OR_EMPTY_CASE_CROSSWALK")
        mapped.update(p["cases"])
        need(len(p["adoption"]) >= 35 and len(p["verification"]) >= 30,
             "TRANSFER_WITHOUT_FALSIFIER")
    need(mapped == case_ids, "CANONICAL_FAILURE_CASES_NOT_ALL_MAPPED")
    need(any(x["priority"] == "P0" for x in data["principles"]),
         "MISSING_HIGHEST_PRIORITY")
    risk_ids = set()
    for r in data["preflight"]:
        need(set(r) == {"id","match","cases","controls","checkpoints"},
             "PREFLIGHT_RULE_INVALID")
        need(r["id"] not in risk_ids, "DUPLICATE_PREFLIGHT_RULE")
        risk_ids.add(r["id"])
        need(r["cases"] and r["controls"] and
             set(r["cases"]) <= case_ids and set(r["controls"]) <= ctrl_ids,
             "PREFLIGHT_ORPHAN_REFERENCE")
        for c in r["cases"]:
            matching = next(x for x in registry["cases"] if x["id"] == c)
            need(set(r["controls"]) & set(matching["preventive_control_ids"]),
                 "PREFLIGHT_HAS_NO_REAL_CASE_CONTROL:" + c)
        need(r["checkpoints"] and all(isinstance(s,str) and len(s)>8
             for s in r["checkpoints"]), "PREFLIGHT_NO_ACTIONABLE_CHECK")
    need({"README.md",".github/workflows/*.yml"} <=
         {r["match"] for r in data["preflight"]}, "REPEATED_README_OR_CI_RISK_UNMAPPED")
    eff = data["effectiveness_by_case"]
    need(len(eff) == len(case_ids) and
         {e["case_id"] for e in eff} == case_ids, "EFFICACY_DENOMINATOR_MISSING")
    for e in eff:
        need(set(e) == {"case_id","status","independent_effectiveness_receipts",
                        "recurrence_window","limitation"}, "EFFICACY_RECORD_SCHEMA_DRIFT")
        need(e["status"] in PERMITTED, "FIELD_EFFECTIVENESS_CANNOT_BE_ATTESTED_OFFLINE")
        if e["status"] == "NOT_OBSERVED":
            need(e["recurrence_window"] == "UNOBSERVED" and
                 not e["independent_effectiveness_receipts"],
                 "UNOBSERVED_PROMOTED_TO_VERIFIED")
        need("not" in e["limitation"].lower(), "EFFICACY_LIMITATION_ERASED")
    need(data["efficiency"]["status_default"] == "NOT_OBSERVED" and
         "not zero" in data["efficiency"]["unknown_policy"].lower(),
         "UNKNOWN_OR_ABSENCE_PROMOTED_TO_ZERO")
    need("do not ingest or publish raw personal chats" in data["efficiency"]["privacy_boundary"].lower(),
         "RAW_PERSONAL_CHATS_MAY_LEAK")
    need("do not demand" in data["efficiency"]["cost_boundary"].lower(),
         "HUMAN_CORRECTION_LABOR_GUARD_REMOVED")
    observations = data["improvement_observations"]
    need(type(observations) is list, "OBSERVATION_APPEND_ONLY_LIST_MISSING")
    for obs in observations:
        need(set(obs) == {"id","case_id","state","receipt_url","limitation"},
             "OBSERVATION_SCHEMA_INVALID")
        need(obs["case_id"] in case_ids and obs["state"] in
             {"REPAIR_OBSERVED","RECURRENCE_OBSERVED","UNVERIFIED"},
             "UNSUPPORTED_EFFECTIVENESS_EVENT")
        url = urlsplit(obs["receipt_url"])
        need(url.scheme == "https" and url.netloc == "github.com" and
             url.path.startswith("/gmodrasa7-rgb/project-intersection-public/"),
             "OBSERVATION_RECEIPT_UNTRUSTED")
        need(obs["limitation"], "OBSERVATION_SCOPE_MISSING")
    need("python3 tools/pi_flr_prior_art_guard.py" in workflow and
         "test_pi_flr_prior_art_guard.py" in workflow,
         "PRIOR_ART_REGRESSION_NOT_EXECUTED_ON_PR_AND_MAIN")
    return {"status":"PRIOR_ART_MAPPING_VALID_NOT_FIELD_EFFECTIVENESS",
            "sources":len(ids),"independent_source_families":len({s["lineage"] for s in sources}),
            "principles":len(pids),"mapped_cases":len(case_ids),
            "preflight_rules":len(risk_ids),"effectiveness_verified":0}


def preflight(data, changed_paths):
    hits = []
    for name in changed_paths:
        rules = [r for r in data["preflight"] if fnmatch.fnmatchcase(name,r["match"])]
        hits.append({"path":name,"known_risk_rules":[r["id"] for r in rules],
                     "past_cases":sorted({c for r in rules for c in r["cases"]}),
                     "checkpoints":sorted({c for r in rules for c in r["checkpoints"]}),
                     "outcome":"CHECKS_NOT_EXECUTED_BY_PREFLIGHT"})
    return {"coverage":"KNOWN_PATH_FINGERPRINTS_ONLY_NO_SEMANTIC_CERTAINTY",
            "changed_paths":hits}


def compare_history(current, old):
    need(old.get("id") == "PI-FLR-PRIOR-ART-TRANSFER",
         "INVALID_PRIOR_ART_BASELINE")
    for key in ("sources","principles","preflight","effectiveness_by_case",
                "counterclaims"):
        prior = old[key]
        after = current[key]
        if key == "effectiveness_by_case":
            need(after[:len(prior)] == prior, "EFFICACY_HISTORY_MUTATED")
        else:
            need(after[:len(prior)] == prior, "HISTORIC_TRANSFER_REWRITTEN:"+key)
    need(current["improvement_observations"][:len(old["improvement_observations"])]
         == old["improvement_observations"], "OBSERVED_EFFECT_HISTORY_REWRITTEN")
    prev = tuple(map(int,old["version"].split(".")))
    now = tuple(map(int,current["version"].split(".")))
    need(now >= prev, "PRIOR_ART_VERSION_REGRESSION")
    if current != old:
        need(now > prev, "UNVERSIONED_PRIOR_ART_CHANGE")
    else:
        need(now == prev, "EMPTY_PRIOR_ART_VERSION_BUMP")
    return True


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--path", action="append", default=[])
    ap.add_argument("--baseline-commit",default="")
    arg=ap.parse_args()
    try:
        data=json.loads((ROOT/PATH).read_text(encoding="utf-8"))
        parent=json.loads((ROOT/REGISTRY).read_text(encoding="utf-8"))
        workflow=(ROOT/WORKFLOW).read_text(encoding="utf-8")
        result=validate(data,parent,workflow)
        if arg.baseline_commit and re.fullmatch(r"[0-9a-fA-F]{40}",arg.baseline_commit):
            p=subprocess.run(["git","show",arg.baseline_commit+":"+PATH],
                             cwd=ROOT,text=True,capture_output=True,check=False)
            if p.returncode==0:
                compare_history(data,json.loads(p.stdout))
                result["history"]="APPEND_ONLY_VERIFIED"
            else:
                result["history"]="FIRST_PUBLICATION_OR_BASELINE_ABSENT"
        changed=list(arg.path)
        if not changed and arg.baseline_commit:
            diff=subprocess.run(["git","diff","--name-only",arg.baseline_commit,"HEAD"],
                                cwd=ROOT,text=True,capture_output=True,check=False)
            if diff.returncode == 0:
                changed=[name for name in diff.stdout.splitlines() if name]
            else:
                result["preflight_coverage"]="NOT_OBSERVED_INVALID_DIFF_BASE"
        if changed:
            result["preflight"]=preflight(data,changed)
        elif "preflight_coverage" not in result:
            result["preflight_coverage"]="NO_CHANGED_PATHS_OR_NOT_PROVIDED"
        print(json.dumps(result,ensure_ascii=False,sort_keys=True))
    except (OSError,ValueError,KeyError,TypeError) as exc:
        raise SystemExit("PI_FLR_PRIOR_ART_FAIL:"+str(exc)) from None


if __name__=="__main__":
    main()
