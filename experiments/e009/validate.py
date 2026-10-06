#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/"scenario_matrix.json").read_text(encoding="utf-8"))
readme=(ROOT/"README.md").read_text(encoding="utf-8")
protocol=(ROOT/"EXECUTABLE_PROTOCOL_v1_1.md").read_text(encoding="utf-8")
benchmark=(ROOT/"benchmark.py").read_text(encoding="utf-8")
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
req(("NO RESULT YET" in readme) or ("PROJECT RERUN SYNTHETIC RESULT AVAILABLE / NOT INDEPENDENT VALIDATION" in readme),"README has invalid E009 status boundary")
req("Model agreement is not counted as independent scientific evidence." in readme,"cross-model agreement was promoted to evidence")
req("PREREGISTERED EXECUTABLE SPECIFICATION / NO RESULT YET" in protocol,"v1.1 executable protocol lost no-result boundary")
req(data.get("pre_execution_amendment_v1_1",{}).get("secondary_comparator")=="MINIMAL_4VAR","minimal four-variable comparator drifted")
req("PROJECT_V3_RESIDUAL_SURVIVES = FALSE" in protocol,"falsification rule drifted")
req("SELF_EXECUTION != INDEPENDENT_VALIDATION" in protocol,"independent-validation boundary drifted")
req("MINIMAL_4VAR" in benchmark and "PROJECT_V3" in benchmark,"executable policy set drifted")
if (ROOT/"RESULT.json").exists():
    result=json.loads((ROOT/"RESULT.json").read_text(encoding="utf-8"))
    receipt=json.loads((ROOT/"EXECUTION_RECEIPT.json").read_text(encoding="utf-8"))
    req(result.get("status")=="SYNTHETIC_PROJECT_RERUN_NOT_INDEPENDENT_VALIDATION","result evidence class drifted")
    req(result.get("survival_criteria",{}).get("project_v3_residual_survives") is False,"negative result was silently promoted")
    req(receipt.get("executable_spec_commit")=="c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace","execution spec commit drifted")
    req(receipt.get("policy_or_threshold_changes_after_spec_merge") is False,"post-spec tuning reported")
    req(receipt.get("independent_validation") is False,"self-run mislabeled independent")
else:
    req("NO RESULT YET" in readme,"missing result artifact without preregistration no-result status")

if errors:
    print("E009 SPEC AUDIT FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("E009 spec audit passed.")
