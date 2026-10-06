#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "scenario_matrix.json").read_text(encoding="utf-8"))
errors=[]

def req(cond,msg):
    if not cond:
        errors.append(msg)

req(data.get("schema_version")=="1.0","schema_version must be 1.0")
req(data.get("status")=="PREREGISTERED_SPECIFICATION_NO_RESULT","status drifted")
baselines=data.get("baselines",[])
req(baselines==["MYOPIC_SCALAR","LONG_HORIZON_EV","CONSTRAINED_RECEDING","ROBUST_CONSTRAINED","PROJECT_V2"],"baseline order changed")
cases=data.get("cases",[])
ids=[x.get("id") for x in cases]
req(len(ids)==len(set(ids)),"duplicate case IDs")
lookup={x.get("id"):x for x in cases}

required=["id","pair","theme","immediate_reward","delayed_effect","uncertainty","irreversibility","practical_exit","rollback","urgency","amendment_conflict","role"]
for case in cases:
    for f in required:
        req(bool(case.get(f)),f"{case.get('id')}: missing {f}")
    pair=lookup.get(case.get("pair"))
    req(pair is not None,f"{case.get('id')}: missing pair")
    if pair:
        req(pair.get("pair")==case.get("id"),f"{case.get('id')}: pair symmetry broken")
        for f in ["theme","immediate_reward","delayed_effect","uncertainty","irreversibility","practical_exit","rollback","urgency","amendment_conflict"]:
            req(pair.get(f)==case.get(f),f"{case.get('id')}: causal factor drift across reversal pair: {f}")

req(len(cases)>=16,"expected at least 16 preregistered cases")
req(all(not any(k in c for k in ["winner","expected_winner","project_wins"]) for c in cases),"predeclared winner field prohibited")

if errors:
    print("E008 SPEC AUDIT FAILED")
    for e in errors:
        print("-",e)
    sys.exit(1)

print(f"E008 spec audit passed: {len(cases)} cases, {len(cases)//2} reversal pairs.")
