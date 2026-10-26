#!/usr/bin/env python3
"""PI-FLR C11: executable, bounded replay of known regression guards.

Prior-art preflight alone returns a suggestion, never proof that a check ran.
This CI gate invokes an allowlisted set of actual checks for changed path families.
No self-certified field effectiveness or proof of future nonrecurrence.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

from pi_flr_prior_art_guard import PATH as TRANSFER_PATH, preflight, PriorArtError

ROOT=Path(__file__).resolve().parents[1]
RECEIPT="pi_flr_replay_receipt.json"
# Hardcode commands here, not in agent-editable literature metadata. Never use shell=True.
COMMANDS={
    "README_L0":["python3","tools/check_readme_l0.py"],
    "LANGUAGE":["python3","tools/check_language_separation.py","--self-test"],
    "RISE_MANIFEST":["python3","tools/pi_rise_manifest_guard.py"],
    "E010_LINEAGE":["python3","tools/pi_flr_experiment_identity.py"],
    "NAV_LINKS":["python3","tools/check_public_navigation.py","--strict-all"],
    "BILINGUAL_INVENTORY":["python3","tools/audit_bilingual_navigation.py","--self-test"],
    "ROADMAP_BILINGUAL":["python3","tools/check_roadmap_bilingual_gate.py","--self-test"],
    "PI_ACCESS":["python3","tools/audit_pi_access.py","--self-test"],
    "FLR_META":["python3","tools/pi_flr_audit.py"],
    "FLR_MUTANTS":["python3","-m","unittest","discover","-s","tests","-p","test_pi_flr_replay_gate.py"],
    "FLR_ALL_TESTS":["python3","-m","unittest","discover","-s","tests","-p","test_pi_flr_*.py"],
}
# Match rule identifiers declared in the versioned data. These checks do real work.
RULE_CHECKS={
    "R01":("README_L0","LANGUAGE","RISE_MANIFEST"),
    "R02":("RISE_MANIFEST",),
    "R03":("E010_LINEAGE",),
    "R04":("NAV_LINKS",),
    "R05":("FLR_META","FLR_MUTANTS"),
    "R06":("FLR_META","FLR_MUTANTS"),
    "R07":("FLR_META","FLR_ALL_TESTS"),
    "R08":("FLR_META","FLR_ALL_TESTS"),
    "R09":("FLR_META","FLR_ALL_TESTS"),
    "R10":("BILINGUAL_INVENTORY","RISE_MANIFEST"),
}


# Precise, reviewed checks for existing material paths not represented in the
# historical failure taxonomy. Unlisted material changes still block promotion.
DIRECT_PATH_CHECKS = {
    "tools/check_roadmap_bilingual_gate.py": ("ROADMAP_BILINGUAL",),
    "research/PI_ROADMAP_DECISION_EVIDENCE_V0_2_4_EN_KO.md": ("ROADMAP_BILINGUAL",),
    "tools/audit_pi_access.py": ("PI_ACCESS", "NAV_LINKS"),
    "tools/check_readme_l0.py": ("README_L0",),
    ".github/workflows/public-repository-audit.yml": ("README_L0", "NAV_LINKS", "FLR_ALL_TESTS"),
}


class ReplayError(ValueError):
    pass


def require(ok, reason):
    if not ok:
        raise ReplayError(reason)


def git_changed_paths(baseline, root=ROOT, run=subprocess.run):
    """Inventory both sides of renames and deletions with NUL-safe Git parsing."""
    require(isinstance(baseline,str) and re.fullmatch(r"[0-9a-fA-F]{40}",baseline),
            "BASELINE_COMMIT_NOT_OBSERVED")
    ref=run(["git","rev-parse","--verify",baseline+"^{commit}"],
            cwd=root,capture_output=True,text=True,check=False)
    require(ref.returncode==0,"BASELINE_COMMIT_NOT_ACCESSIBLE")
    diff=run(["git","diff","--name-status","-z","--find-renames",baseline,"HEAD"],
             cwd=root,capture_output=True,text=True,check=False)
    require(diff.returncode==0,"CHANGED_PATHS_NOT_OBSERVED")
    raw=diff.stdout
    require(isinstance(raw,str) and (not raw or raw.endswith("\0")),
            "DIFF_FORMAT_INVALID")
    fields=raw.split("\0")[:-1] if raw else []
    names=[]
    i=0
    while i<len(fields):
        status=fields[i]
        i+=1
        need_two=status.startswith(("R","C"))
        require(status in {"M","A","D","T"} or
                (need_two and status[1:].isdigit()),
                "UNSUPPORTED_GIT_STATUS:"+status)
        count=2 if need_two else 1
        require(i+count<=len(fields),"DIFF_RECORD_TRUNCATED")
        paths=fields[i:i+count]
        require(all(p and not p.startswith("/") and "\0" not in p
                    for p in paths), "DIFF_PATH_INVALID")
        names.extend(paths)
        i+=count
    return sorted(set(names))


def is_material_unmapped_path(path):
    """Conservative materiality; unknown artifacts alone are not proof of safety."""
    import posixpath
    ext=posixpath.splitext(path.lower())[1]
    return (ext in {".py",".json",".jsonl",".md",".yml",".yaml",
                    ".js",".ts",".toml",".sh",".csv",".lock",".ipynb"}
            or path.startswith((".github/","tools/","tests/","experiments/"))
            or posixpath.basename(path) in {"Dockerfile","Makefile","requirements.txt"})


def planned_replay(data, paths):
    require(isinstance(paths,list) and all(isinstance(x,str) and x for x in paths),
            "PATHS_INVALID")
    observed=preflight(data,sorted(set(paths)))["changed_paths"]
    rules={r["id"] for r in data["preflight"]}
    require(rules==set(RULE_CHECKS),"RULE_AND_EXECUTOR_DRIFT")
    checks=set()
    relevant=set()
    unmapped_material=[]
    for entry in observed:
        rr=set(entry["known_risk_rules"])
        direct = DIRECT_PATH_CHECKS.get(entry["path"], ())
        if rr:
            require(rr<=set(RULE_CHECKS),"KNOWN_RISK_WITHOUT_EXECUTABLE_CHECK")
            for r in rr:
                checks.update(RULE_CHECKS[r])
        if direct:
            checks.update(direct)
        if rr or direct:
            relevant.add(entry["path"])
        elif is_material_unmapped_path(entry["path"]):
            unmapped_material.append(entry["path"])
        require(entry["outcome"]=="CHECKS_NOT_EXECUTED_BY_PREFLIGHT",
                "PREFLIGHT_FALSELY_CERTIFIED_EXECUTION")
    require(checks<=set(COMMANDS),"UNTRUSTED_OR_MISSING_COMMAND")
    return {"changed_paths":len(observed),
            "matched_paths":sorted(relevant),
            "check_ids":sorted(checks),
            "unmatched_path_count":len(observed)-len(relevant),
            "unmapped_material_paths":sorted(unmapped_material),
            "coverage":"MATERIAL_UNMAPPED_BLOCKS_SCOPE_PASS"}


def execute(plan, root=ROOT, run=subprocess.run):
    receipts=[]
    for label in plan["check_ids"]:
        require(label in COMMANDS,"UNALLOWLISTED_CHECK:"+str(label))
        cmd=COMMANDS[label]
        result=run(cmd,cwd=root,capture_output=True,text=True,check=False)
        receipts.append({"check_id":label,
                         "status":"PASS" if result.returncode==0 else "FAIL",
                         "exit_code":int(result.returncode)})
    fail=[x["check_id"] for x in receipts if x["status"]!="PASS"]
    status=("BLOCKED_FAILED" if fail else
            "BLOCKED_UNMAPPED_MATERIAL" if plan.get("unmapped_material_paths") else
            "NO_KNOWN_RISK_MATCHED" if not receipts else
            "SCOPED_REPLAY_PASS")
    return {"status":status,"executed":receipts,"failed_checks":fail,
            "scope":"ACTUAL_ALLOWLISTED_SUBPROCESS_RESULTS_NOT_FIELD_EFFECTIVENESS"}


def verify_contract(data, workflow):
    require("python3 tools/pi_flr_replay_gate.py --baseline-commit \"$BASE\"" in workflow,
            "CI_REPLAY_INVOCATION_MISSING")
    require("path: pi_flr_replay_receipt.json" in workflow and
            "if-no-files-found: error" in workflow,
            "REPLAY_RECEIPT_NOT_PERSISTED_FAIL_CLOSED")
    require("test_pi_flr_replay_gate.py" in workflow,
            "REPLAY_NEGATIVE_MUTATIONS_NOT_RUN")
    require(data.get("saturation")=="NOT_ESTABLISHED",
            "LITERATURE_SATURATION_FALSELY_CLOSED")
    return True


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--baseline-commit",default="")
    ap.add_argument("--path",action="append",default=[])
    ap.add_argument("--output",default=RECEIPT)
    args=ap.parse_args()
    receipt={"status":"BLOCKED_UNCONFIRMED","coverage":"NOT_OBSERVED",
             "error_code":"NO_EXECUTION","source_version":"PI-FLR-v0.6.0"}
    exit_bad=True
    try:
        raw=json.loads((ROOT/TRANSFER_PATH).read_text(encoding="utf-8"))
        wf=(ROOT/".github/workflows/pi-flr-integrity.yml").read_text(encoding="utf-8")
        verify_contract(raw,wf)
        # Explicit paths support local manual smoke tests. CI must pass a real baseline.
        paths=list(args.path)
        if not paths:
            paths=git_changed_paths(args.baseline_commit)
        plan=planned_replay(raw,paths)
        result=execute(plan)
        head=subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,
                            capture_output=True,text=True,check=False)
        receipt={**result,**plan,"head_commit":head.stdout.strip() if
                 head.returncode==0 else "UNKNOWN",
                 "baseline_commit":args.baseline_commit or "EXPLICIT_PATH_SMOKE",
                 "status":result["status"],
                 "no_future_recurrence_proof":True}
        exit_bad=result["status"] in {"BLOCKED_FAILED","BLOCKED_UNMAPPED_MATERIAL"}
    except (OSError,ValueError,TypeError,KeyError,PriorArtError) as e:
        # Keep a receipt even for a malformed baseline or policy failure.
        receipt["error_code"]=str(e).splitlines()[0][:180]
        receipt["status"]="BLOCKED_UNCONFIRMED"
        exit_bad=True
    target=Path(args.output)
    target.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt,ensure_ascii=False,sort_keys=True))
    if exit_bad:
        raise SystemExit(1)


if __name__=="__main__":
    main()
