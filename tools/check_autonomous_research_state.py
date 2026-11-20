#!/usr/bin/env python3
"""Validate the public autonomous-research continuation pointer.

This checks repository-state integrity only. It does not certify research claims,
scientific validity, or external replication.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "AUTONOMOUS_RESEARCH_STATE.json"
EXPECTED_REPOSITORY = "gmodrasa7-rgb/project-intersection-public"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


class StateError(ValueError):
    pass


def git(args: list[str], *, run=subprocess.run) -> subprocess.CompletedProcess:
    return run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False)


def validate_state(data: object, *, run=subprocess.run) -> dict:
    if not isinstance(data, dict):
        raise StateError("STATE_NOT_OBJECT")
    if data.get("schema_version") != "1.1":
        raise StateError("STATE_SCHEMA_VERSION_UNSUPPORTED")
    if data.get("status") != "ACTIVE_CONTINUITY":
        raise StateError("STATE_STATUS_UNEXPECTED")
    if data.get("public_repository") != EXPECTED_REPOSITORY:
        raise StateError("STATE_REPOSITORY_MISMATCH")

    pointer = data.get("current_public_head")
    if not isinstance(pointer, str) or not SHA40.fullmatch(pointer):
        raise StateError("CURRENT_PUBLIC_HEAD_INVALID")
    boundary = data.get("canonical_boundary")
    if not isinstance(boundary, str) or not boundary.strip():
        raise StateError("CANONICAL_BOUNDARY_MISSING")
    updated = data.get("updated_at")
    if not isinstance(updated, str):
        raise StateError("UPDATED_AT_MISSING")
    try:
        datetime.fromisoformat(updated.replace("Z", "+00:00"))
    except ValueError as exc:
        raise StateError("UPDATED_AT_INVALID") from exc
    policy = data.get("execution_policy")
    if not isinstance(policy, dict) or not policy:
        raise StateError("EXECUTION_POLICY_MISSING")

    exists = git(["cat-file", "-e", pointer + "^{commit}"], run=run)
    if exists.returncode != 0:
        raise StateError("CURRENT_PUBLIC_HEAD_NOT_AVAILABLE_AS_COMMIT")
    head = git(["rev-parse", "HEAD"], run=run)
    if head.returncode != 0 or not SHA40.fullmatch(head.stdout.strip()):
        raise StateError("CHECKED_OUT_HEAD_NOT_OBSERVED")
    ancestor = git(["merge-base", "--is-ancestor", pointer, "HEAD"], run=run)
    if ancestor.returncode != 0:
        raise StateError("CURRENT_PUBLIC_HEAD_NOT_ANCESTOR_OF_CHECKOUT")
    distance = git(["rev-list", "--count", pointer + "..HEAD"], run=run)
    if distance.returncode != 0 or not distance.stdout.strip().isdigit():
        raise StateError("POINTER_DISTANCE_NOT_OBSERVED")

    return {
        "status": "PASS",
        "scope": "PUBLIC_CONTINUITY_POINTER_INTEGRITY_ONLY",
        "schema_version": data["schema_version"],
        "current_public_head": pointer,
        "checked_out_head": head.stdout.strip(),
        "commits_after_pointer_in_checkout": int(distance.stdout.strip()),
        "scientific_validity_certified": False,
        "external_replication_certified": False,
    }


def main() -> int:
    try:
        data = json.loads(STATE.read_text(encoding="utf-8"))
        result = validate_state(data)
    except (OSError, json.JSONDecodeError, StateError) as exc:
        print(json.dumps({"status": "FAIL", "error_code": str(exc).splitlines()[0][:160]},
                         ensure_ascii=False, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
