#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
POLICY=ROOT/"continuity"/"handoff-policy.json"
SCHEMA=ROOT/"continuity"/"handoff-receipt-schema-v1.json"
errors=[]

def req(v,m):
    if not v: errors.append(m)

p=json.loads(POLICY.read_text(encoding="utf-8"))
s=json.loads(SCHEMA.read_text(encoding="utf-8"))

req(p.get("schema_version")=="1.0","handoff policy schema drifted")
req(p.get("role")=="transaction_provenance_not_third_canonical","handoff layer was promoted into a third canonical store")
g=p.get("guards",{})
for k in ["public_push_is_success","github_change_is_local_truth","local_access_is_publication_authority","staging_is_canonical","receipts_are_scientific_validation"]:
    req(g.get(k) is False,f"guard must remain false: {k}")
req(g.get("previous_canonical_unchanged_on_failure") is True,"failure may mutate previous canonical")
req(g.get("source_authority_over_distillation") is True,"source authority over distillation lost")
req("QUARANTINED" in p.get("states",[]),"quarantine state missing")
req("ROLLBACK_REQUIRED" in p.get("states",[]),"rollback state missing")

required=set(s.get("required",[]))
for field in p.get("required_receipt_fields",[]):
    req(field in required,f"policy-required receipt field absent from JSON schema: {field}")

protocol=(ROOT/"continuity"/"GITHUB_LOCAL_HANDOFF_PROTOCOL.md").read_text(encoding="utf-8")
for phrase in [
    "PUBLIC_PUSH != SUCCESS",
    "LOCAL_ACCESS != PUBLICATION_AUTHORITY",
    "transaction / provenance layer",
    "QUARANTINED / UNRESOLVED",
]:
    req(phrase in protocol,f"protocol lost required boundary: {phrase}")

if errors:
    print("HANDOFF PROTOCOL AUDIT FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("Handoff protocol audit passed.")
