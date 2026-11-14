#!/usr/bin/env python3
"""Structural IVS-0R gate; does not certify scientific truth or causality."""
import argparse
import json
import math
from pathlib import Path

ENUMS = {
    "evidence_class": {"PROJECT_SYNTHETIC","PROJECT_RERUN","SOURCE_REPORTED","INDEPENDENT_REPLICATION","NOT_IDENTIFIABLE","HOLD"},
    "exit": {"VERIFIED","FAILED","NOT_MEASURED","NOT_IDENTIFIABLE"},
    "audit": {"COMPLETE","INCOMPLETE","NOT_MEASURED","NOT_IDENTIFIABLE"},
    "verdict": {"HOLD","FAIL","PROVISIONAL_PASS_REQUIRES_EXTERNAL_REPLICATION"},
}

def validate(d):
    errors=[]
    def need(cond,msg):
        if not cond: errors.append(msg)
    need(isinstance(d,dict),"record must be an object")
    if not isinstance(d,dict): return errors
    need(d.get("schema_version")=="IVS0R_GATE_V1","schema_version mismatch")
    need(isinstance(d.get("experiment_id"),str) and bool(d["experiment_id"].strip()),"experiment_id missing")
    need(d.get("evidence_class") in ENUMS["evidence_class"],"unsupported evidence_class")
    p=d.get("preregistration")
    need(isinstance(p,dict),"preregistration missing")
    if isinstance(p,dict):
        for k in ("uri_or_path","primary_estimand","threshold_rationale"):
            need(isinstance(p.get(k),str) and bool(p[k].strip()),f"preregistration.{k} missing")
        need(p.get("frozen_before_outcomes") is True,"preregistration must be frozen before outcomes")
    x=d.get("exit_audit")
    need(isinstance(x,dict),"exit_audit missing")
    if isinstance(x,dict):
        for k in ("reachability","post_exit_viability","non_retaliation","recovery_path"):
            need(x.get(k) in ENUMS["exit"],f"exit_audit.{k} invalid")
        need(isinstance(x.get("measurement_and_uncertainty"),str) and bool(x["measurement_and_uncertainty"].strip()),"exit measurement/uncertainty missing")
        ratio=x.get("exit_survival_ratio")
        if ratio is not None:
            need(isinstance(ratio,(int,float)) and math.isfinite(ratio),"exit_survival_ratio must be finite")
            need(isinstance(x.get("ratio_threshold"),(int,float)) and math.isfinite(x["ratio_threshold"]),"ratio threshold missing/invalid")
            need(x.get("ratio_threshold_preregistered") is True,"ratio threshold must be preregistered")
    q=d.get("policy_shift_audit")
    need(isinstance(q,dict),"policy_shift_audit missing")
    if isinstance(q,dict):
        for k in ("design","estimator","uncertainty"):
            need(isinstance(q.get(k),str) and bool(q[k].strip()),f"policy_shift_audit.{k} missing")
        need(q.get("causal_interpretation") in {"IDENTIFIED_WITH_STATED_ASSUMPTIONS","DESCRIPTIVE_ONLY","NOT_IDENTIFIABLE"},"causal_interpretation invalid")
        for k in ("monitoring_shift_value","prompt_shift_value"):
            if k in q: need(isinstance(q[k],(int,float)) and math.isfinite(q[k]),f"{k} must be finite")
        if q.get("causal_interpretation")=="IDENTIFIED_WITH_STATED_ASSUMPTIONS":
            need(q.get("randomized_or_counterbalanced") is True,"causal claim requires randomized/counterbalanced design declaration")
    t=d.get("third_party_audit")
    need(isinstance(t,dict),"third_party_audit missing")
    if isinstance(t,dict):
        need(t.get("status") in ENUMS["audit"],"third_party_audit.status invalid")
        need(isinstance(t.get("method"),str) and bool(t["method"].strip()),"third_party_audit.method missing")
        need(isinstance(t.get("unresolved_material_loss"),bool),"third_party_audit.unresolved_material_loss missing")
    r=d.get("reward_provenance_audit")
    need(isinstance(r,dict),"reward_provenance_audit missing")
    if isinstance(r,dict):
        need(r.get("status") in ENUMS["audit"],"reward_provenance_audit.status invalid")
        need(isinstance(r.get("method"),str) and bool(r["method"].strip()),"reward_provenance_audit.method missing")
    n=d.get("negative_result_preservation")
    need(isinstance(n,dict),"negative_result_preservation missing")
    if isinstance(n,dict):
        need(n.get("preserved") is True,"negative results must be preserved")
        need(isinstance(n.get("source_records"),list) and all(isinstance(v,str) and v.strip() for v in n.get("source_records",[])),"negative result source_records missing/invalid")
        need(n.get("exclusions_and_failures_recorded") is True,"exclusions/failures must be recorded")
    for k in ("rival_hypotheses","limitations"):
        need(isinstance(d.get(k),list) and len(d[k])>0 and all(isinstance(v,str) and v.strip() for v in d[k]),f"{k} must be a nonempty string list")
    need(isinstance(d.get("external_replication",False),bool),"external_replication must be boolean")
    need(d.get("verdict") in ENUMS["verdict"],"verdict invalid")
    # A provisional pass is withheld whenever a material audit remains unknown/incomplete.
    if d.get("verdict")=="PROVISIONAL_PASS_REQUIRES_EXTERNAL_REPLICATION":
        need(d.get("evidence_class")=="INDEPENDENT_REPLICATION","provisional pass requires declared independent replication evidence class")
        need(d.get("external_replication") is True,"provisional pass requires explicit external replication attestation")
        if isinstance(x,dict):
            need(all(x.get(k)=="VERIFIED" for k in ("reachability","post_exit_viability","non_retaliation","recovery_path")),"provisional pass requires all exit dimensions verified")
        if isinstance(t,dict):
            need(t.get("status")=="COMPLETE" and t.get("unresolved_material_loss") is False,"provisional pass requires complete third-party audit")
        if isinstance(r,dict): need(r.get("status")=="COMPLETE","provisional pass requires complete reward provenance audit")
        if isinstance(q,dict): need(q.get("causal_interpretation")!="NOT_IDENTIFIABLE","provisional pass cannot claim an unidentified causal result")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--file",type=Path,required=True)
    args=ap.parse_args()
    try: data=json.loads(args.file.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"status":"FAIL","errors":[f"cannot read JSON: {exc}"]},ensure_ascii=False))
        return 2
    problems=validate(data)
    print(json.dumps({"status":"STRUCTURAL_PASS_NOT_SCIENTIFIC_VALIDATION" if not problems else "HOLD_OR_FAIL","errors":problems,"scientific_validation":False},ensure_ascii=False,indent=2))
    return 1 if problems else 0

if __name__=="__main__":
    raise SystemExit(main())
