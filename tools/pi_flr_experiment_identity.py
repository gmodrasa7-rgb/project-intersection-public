#!/usr/bin/env python3
"""PI-FLR-C04: protect distinct E010 experiment lineages.

This audits PUBLIC canonical E010 metadata and status only; it cannot inspect
all GitHub history or certify scientific validity. External legacy PR #20
was checked separately at registration time.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = "experiments/e010/README_KO.md"
RESULT = "experiments/e010/RESULT.json"
MODEL = "one_shot_extraction_and_irreversible_execution_budget"
STATUS = "SELF_RUN_SYNTHETIC_FALSIFICATION_NOT_EMPIRICAL_VALIDATION"
REQUIRED_README = (
    "실험 ID 충돌 경고", "PR #20", "2026-10-12",
    "POSTHOC DESIGN", "NOT PRE-REGISTERED", "108개",
    "구성개념 불일치",
)
BLOCKED_LEGACY = "experiments/e010/benchmark.py"


class IdentityError(ValueError):
    pass


def audit_identity(result: dict, readme: str, legacy_executable_present: bool):
    if type(result) is not dict:
        raise IdentityError("E010_RESULT_NOT_OBJECT")
    if result.get("model") != MODEL:
        raise IdentityError("E010_IDENTITY_REPLACED_BY_OTHER_STUDY")
    if result.get("status") != STATUS:
        raise IdentityError("E010_EVIDENCE_GRADE_OR_PREREGISTRATION_PROMOTED")
    if type(result.get("grid_size")) is not int or result["grid_size"] != 108:
        raise IdentityError("E010_CANONICAL_SYNTHETIC_GRID_CHANGED")
    if type(readme) is not str or any(marker not in readme for marker in REQUIRED_README):
        raise IdentityError("E010_LEGACY_IDENTITY_COLLISION_DISCLOSURE_LOST")
    if legacy_executable_present:
        raise IdentityError("E010_BLOCKED_LEGACY_BENCHMARK_IMPORTED")
    return {"status":"PUBLIC_E010_IDENTITY_BOUNDARY_PASS",
            "canonical":"2026-10-12 exploratory self-run one-shot synthetic E010",
            "archived_pr20":"DISTINCT_BLOCKED_DESIGN_NOT_IMPORTED",
            "limitation":"NO_SCIENTIFIC_REPLICATION_OR_HISTORIC_PR_RUNTIME_ATTESTATION"}


def main():
    try:
        r=json.loads((ROOT/RESULT).read_text(encoding="utf-8"))
        readme=(ROOT/README).read_text(encoding="utf-8")
        output=audit_identity(r,readme,(ROOT/BLOCKED_LEGACY).exists())
        print(json.dumps(output,ensure_ascii=False,sort_keys=True))
    except (IdentityError, OSError, ValueError) as exc:
        raise SystemExit("PI_FLR_C04_FAIL:"+str(exc)) from None


if __name__=="__main__":
    main()
