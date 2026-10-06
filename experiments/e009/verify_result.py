#!/usr/bin/env python3
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BENCH=ROOT/"benchmark.py"
RESULT=ROOT/"RESULT.json"
RECEIPT=ROOT/"EXECUTION_RECEIPT.json"

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

receipt=json.loads(RECEIPT.read_text(encoding="utf-8"))
expected=json.loads(RESULT.read_text(encoding="utf-8"))

bench_hash=sha256_bytes(BENCH.read_bytes())
if bench_hash != receipt["benchmark_sha256"]:
    raise SystemExit(f"benchmark SHA-256 drift: {bench_hash}")

with tempfile.TemporaryDirectory() as td:
    out=Path(td)/"result.json"
    subprocess.run([sys.executable,str(BENCH),"--execute","--out",str(out)],check=True)
    generated_bytes=out.read_bytes()
    generated=json.loads(generated_bytes)
    if generated != expected:
        raise SystemExit("re-executed E009 result does not match committed RESULT.json")
    raw_hash=sha256_bytes(generated_bytes)
    if raw_hash != receipt["generated_result_sha256"]:
        raise SystemExit(f"generated result byte hash drift: {raw_hash}")
    semantic=hashlib.sha256(json.dumps(generated,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")).hexdigest()
    if semantic != receipt["semantic_result_sha256"]:
        raise SystemExit(f"semantic result hash drift: {semantic}")

if expected["survival_criteria"]["project_v3_residual_survives"] is not False:
    raise SystemExit("negative E009 result was silently promoted")
if expected["status"]!="SYNTHETIC_PROJECT_RERUN_NOT_INDEPENDENT_VALIDATION":
    raise SystemExit("E009 evidence boundary drifted")
if receipt["independent_validation"] is not False:
    raise SystemExit("self-execution was mislabeled as independent validation")
if receipt["policy_or_threshold_changes_after_spec_merge"] is not False:
    raise SystemExit("execution receipt reports post-spec tuning")

print("E009 result reproduction passed: frozen benchmark reproduces committed negative synthetic result.")
