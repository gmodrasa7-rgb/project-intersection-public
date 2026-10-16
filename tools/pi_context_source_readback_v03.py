#!/usr/bin/env python3
"""v0.3: actual Git checkout content + source-integrity checks for route plans.

No Library/network access, no scientific validation, no model-weight modification.
Original project code, with older work credited in the bilingual protocol.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from pi_context_route_v02 import route

HEX40 = re.compile(r"^[0-9a-f]{40}$")
MAX_BYTES = 2_000_000


def git_command(root: Path, *args: str) -> str | None:
    try:
        process = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True, text=True, check=False, timeout=8,
        )
        return process.stdout.strip() if process.returncode == 0 else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def git_blob(data: bytes) -> str:
    # Git blob hashes include a type-and-length header.
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def tree_blob(root: Path, revision: str, path: str) -> str | None:
    out = git_command(root, "ls-tree", "-r", revision, "--", path)
    if not out:
        return None
    rows = [line.split("\t", 1) for line in out.splitlines() if "\t" in line]
    for item, name in rows:
        parts = item.split()
        if name == path and len(parts) == 3 and parts[1] == "blob":
            return parts[2]
    return None


def check_document(root: Path, revision: str | None, path: str) -> dict:
    if not isinstance(path, str) or not path or path.startswith("/") or ".." in Path(path).parts:
        return {"path": path, "status": "INVALID_PATH"}
    root = root.resolve()
    candidate = root / path
    if candidate.is_symlink():
        return {"path": path, "status": "SYMLINK_BLOCKED"}
    dest = candidate.resolve()
    if not dest.is_relative_to(root) or not dest.is_file():
        return {"path": path, "status": "MISSING_OR_UNSAFE"}
    size = dest.stat().st_size
    if size > MAX_BYTES:
        return {"path": path, "status": "TOO_LARGE", "bytes": size}
    data = dest.read_bytes()
    digest = git_blob(data)
    if revision is None or HEX40.fullmatch(revision) is None:
        status, tree_digest = "UNVERIFIED_GIT_REVISION", None
    else:
        tree_digest = tree_blob(root, revision, path)
        status = ("GIT_TREE_MATCH" if digest == tree_digest else
                  "NOT_IN_GIT_TREE" if tree_digest is None else
                  "LOCAL_FILE_DIFFERS_FROM_COMMIT")
    return {"path": path, "status": status, "bytes": len(data),
            "local_blob_sha": digest, "commit_tree_blob_sha": tree_digest,
            "contents_read": True, "contents_interpreted": False}


def checkout_head(root: Path) -> str | None:
    value = git_command(root, "rev-parse", "--verify", "HEAD")
    return value if isinstance(value, str) and HEX40.fullmatch(value) else None


def audit(question: str, root: Path, limit: int = 5) -> dict:
    plan = route(question, limit)
    head = checkout_head(root)
    records = [check_document(root, head, p) for p in plan["paths_to_read"]]
    is_verified = (head is not None and records and
                   all(rec["status"] == "GIT_TREE_MATCH" for rec in records))
    # A Git-bounded scientific source can still contain a stale fact or mistake.
    stale_pointer = "UNTESTED_NOT_IN_PLAN"
    for rec in records:
        if rec["path"] == "AUTONOMOUS_RESEARCH_STATE.json" and rec["status"] == "GIT_TREE_MATCH":
            try:
                value = json.loads((root / rec["path"]).read_text(encoding="utf-8"))
                saved = value.get("current_public_head")
                stale_pointer = ("STALE" if saved != head
                                 else "MATCHES_THIS_LOCAL_CHECKOUT")
            except (UnicodeError, OSError, ValueError, TypeError):
                stale_pointer = "UNREADABLE"
    if not is_verified:
        status = "SOURCE_NOT_VERIFIED"
    elif plan["status"] == "INSUFFICIENT_BUDGET":
        status = "COVERAGE_INCOMPLETE"
    elif stale_pointer in ("STALE", "UNREADABLE"):
        status = "REQUIRES_FRESH_STATE"
    else:
        status = "SOURCE_BYTES_CHECKED_NOT_CLAIMS"
    return {
        "schema": "pi-context-source-readback/v0.3",
        "evidence_class": "ORIGINAL_LOCAL_GIT_REPRODUCIBILITY_CHECK",
        "status": status, "plan": plan,
        "local_git_revision": head, "records": records,
        "known_stale_pointer": stale_pointer,
        "library_accessed": False,
        "source_truth_verified": False,
        "human_consent_or_rights_verified": False,
        "model_answer_accuracy_measured": False,
        "independent_scientific_replication": False,
        "source_text_is_untrusted_data": True,
    }


def regression(root: Path) -> dict:
    cases = (
        ("E009 제3자 원저자", "SOURCE_BYTES_CHECKED_NOT_CLAIMS"),
        ("Library 복원 E009", "REQUIRES_FRESH_STATE"),
        ("E009 E008 E007 제3자 원저자 Library", "COVERAGE_INCOMPLETE"),
    )
    observed = []
    for q, expected in cases:
        out = audit(q, root)
        assert out["status"] == expected, (q, out["status"], expected)
        assert all(x["status"] == "GIT_TREE_MATCH" for x in out["records"]), q
        assert out["library_accessed"] is False
        assert out["source_truth_verified"] is False
        observed.append({"question": q, "status": out["status"],
                         "count": len(out["records"])})
    assert audit("제3자 A가 B를 통제 E009 원저자", root)["plan"]["paths_to_read"] == (
        audit("제3자 B가 A를 통제 E009 원저자", root)["plan"]["paths_to_read"]
    )
    old = check_document(root, checkout_head(root), "tools/pi_context_route_v02.py")
    assert old["status"] == "GIT_TREE_MATCH"
    assert check_document(root, checkout_head(root), "../../etc/passwd")["status"] == "INVALID_PATH"
    assert check_document(root, checkout_head(root), "not-a-real-path.md")["status"] == "MISSING_OR_UNSAFE"
    assert check_document(root, None, "tools/pi_context_route_v02.py")["status"] == "UNVERIFIED_GIT_REVISION"
    assert git_blob(b"test") == hashlib.sha1(b"blob 4\0test").hexdigest()
    # The old v0.2 plan's coverage is not falsely counted as verified evidence.
    assert audit("E009", root)["plan"]["documents_retrieved"] is False
    return {"tested_queries": len(cases), "case_results": observed,
            "git_sha_checked": checkout_head(root),
            "binary_byte_checks": "MATCHED_COMMIT_TREE",
            "regression_scope": "source bytes and route completeness only",
            "independent_model_test": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--question", default="E009 원저자")
    parser.add_argument("--limit", type=int, default=5)
    a = parser.parse_args()
    base = Path(a.repo)
    print(json.dumps(regression(base) if a.selftest else audit(a.question, base, a.limit),
                     ensure_ascii=False, indent=2, sort_keys=True))
