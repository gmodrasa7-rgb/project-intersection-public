#!/usr/bin/env python3
"""PI-PACD-PRS OSL v0.1.0 toy scenario truthfulness and separation guard.
Arithmetic of human-assigned illustrative figures only. No independent scientific validation.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "research/PI_PACD_PRS_OSL_CASES_V0_1_0.json"

class OslAuditError(ValueError):
    pass

def verify(data):
    if data.get("evidence_grade") != "RESEARCHER_ASSIGNED_TOY_INPUTS_NOT_REPORTED_EMPIRICAL_OWNER_UTILITY":
        raise OslAuditError("FALSE_REAL_WORLD_PROMOTION")
    if len(data.get("cases", [])) != 3:
        raise OslAuditError("MISSING_ADVERSARIAL_CASES")
    seen, signs = set(), set()
    for case in data["cases"]:
        cid = case.get("case_id")
        if cid in seen or not cid:
            raise OslAuditError("DUPLICATE_CASE")
        seen.add(cid)
        for action in ("D", "C"):
            a = case[action]
            if not all(type(a.get(x)) in (int, float) for x in ("gross","cost","net")):
                raise OslAuditError("INVALID_OWNER_WELFARE_INPUT")
            if abs(a["net"] - (a["gross"] - a["cost"])) > 1e-9:
                raise OslAuditError("NET_MATH_ERROR")
        delta = case["C"]["net"] - case["D"]["net"]
        if abs(delta - case.get("delta_owner",float("inf"))) > 1e-9:
            raise OslAuditError("DELTA_MATH_ERROR")
        actual = "C" if delta>0 else "D" if delta<0 else "TIE"
        if actual != case.get("owner_private_choice"):
            raise OslAuditError("OWNER_CHOICE_ERROR")
        signs.add(actual)
        if case.get("outsider_B_legitimate_rights_assessment") != "INDEPENDENT_REVIEW_REQUIRED":
            raise OslAuditError("OWNER_WELFARE_NOT_PROOF_OF_B_RIGHTS")
    if signs != {"C","D","TIE"}:
        raise OslAuditError("MISSING_REVERSE_OR_TIE")
    flags=data.get("evidence_boundary",{})
    if not flags or any(x is not False for x in flags.values()):
        raise OslAuditError("FALSE_EMPIRICAL_VERIFICATION")
    if "rights" not in data.get("rights_noncompensation_rule","").lower():
        raise OslAuditError("MISSING_THIRD_PARTY_GUARD")
    return {"result":"PASS_SYNTHETIC_OWNER_WELFARE_LOGIC_NOT_FIELD_DATA",
            "cases":len(data["cases"]), "owner_self_loss_cases":1,
            "owner_domination_advantage_cases":1,"owner_indifference_cases":1,
            "actual_owner_observations":0, "ai_model_tests":0}

if __name__=="__main__":
    print(json.dumps(verify(json.loads(CASES.read_text(encoding="utf-8"))),ensure_ascii=False,indent=2))
