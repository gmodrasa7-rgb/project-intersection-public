#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/"scenario_matrix.json").read_text(encoding="utf-8"))
readme=(ROOT/"README.md").read_text(encoding="utf-8")
errors=[]

def req(x,m):
    if not x: errors.append(m)

req(data.get("schema_version")=="1.0","schema drift")
req(data.get("status")=="PREREGISTERED_SPECIFICATION_NO_RESULT","result boundary drift")
req(len(data.get("scenario_families",[]))==16,"expected 16 scenario families")
req(data.get("required_variables")==["ENF","ID","OV","CUM","RF","SEL","INT","VOI"],"stress variable set drift")
blob=json.dumps(data)
for field in data.get("prohibited_fields",[]):
    req(f'"{field}":' not in blob,f"predeclared winner field prohibited: {field}")
req("NO RESULT YET" in readme,"README lost no-result boundary")
req("Model agreement is not counted as independent scientific evidence." in readme,"cross-model agreement was promoted to evidence")

if errors:
    print("E009 SPEC AUDIT FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("E009 spec audit passed.")
