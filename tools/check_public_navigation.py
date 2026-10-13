#!/usr/bin/env python3
"""Deterministic repository-local Markdown link integrity and landing clutter budget.

Only checks existing local files/directories, not remote websites or fragment
anchors. No network, third-party dependency, or scientific verification claim.
Do not use this to delete historical source, failure or contribution records.
"""
from __future__ import annotations

import argparse
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_ROOT_FILES = 60  # 2026-10-13 baseline, do not expand top-level clutter.
CORE = (
    "README.md",
    "RESEARCH_TOC.md",
    "START_HERE_KO.md",
    "PUBLIC_EVIDENCE_INDEX.md",
    "PUBLIC_REVIEW_PACKET.md",
    "AI_REVIEW_START_HERE.md",
    "RESEARCH_OVERVIEW.md",
    "RESEARCH_STATUS_POLICY.md",
    "CONTRIBUTING.md",
    "START_HERE_EVIDENCE_FUNDING_BILINGUAL.md",
)
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
FENCE = re.compile(r"^\s{0,3}(\x60{3,}|~{3,})")


def iter_live_lines(body: str):
    active = None
    for lineno, line in enumerate(body.splitlines(), 1):
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if active is None:
                active = marker[0]
            elif marker[0] == active:
                active = None
            continue
        if active is None:
            yield lineno, line


def local_target(source: str, destination: str):
    """Return repo-relative target or None for fragment/external links."""
    raw = destination.strip()
    if raw.startswith("<"):
        end = raw.find(">")
        raw = raw[1:end] if end != -1 else raw
    else:
        raw = raw.split()[0] if raw else ""
    if not raw or raw.startswith("#") or raw.startswith("//"):
        return None
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc:
        return None
    candidate = unquote(parsed.path)
    if not candidate:
        return None
    if candidate.startswith("/"):
        return "!ABSOLUTE-LOCAL:" + candidate
    joined = posixpath.normpath(posixpath.join(posixpath.dirname(source), candidate))
    if joined == ".." or joined.startswith("../"):
        return "!ESCAPE:" + joined
    return joined


def find_bad_links(source: str, body: str, exists):
    bad = []
    for lineno, line in iter_live_lines(body):
        for match in LINK.finditer(line):
            target = local_target(source, match.group(1))
            if target is not None and (target.startswith("!") or not exists(target)):
                bad.append((source, lineno, target))
    return bad


def scan(paths):
    all_paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if ".git" not in p.parts}
    exists = lambda p: p in all_paths
    failures = []
    for path in paths:
        full = ROOT / path
        if not full.is_file():
            failures.append((path, 0, "!SOURCE-MISSING"))
        elif path.endswith(".md"):
            failures.extend(find_bad_links(path, full.read_text(encoding="utf-8"), exists))
    return failures


def self_test():
    exists = lambda x: x in {"README.md", "research/a.md", "research/examples"}
    assert local_target("research/a.md", "../README.md#purpose") == "README.md"
    assert local_target("README.md", "https://example.org/a.md") is None
    assert local_target("README.md", "#a-section") is None
    assert local_target("research/a.md", "examples") == "research/examples"
    assert local_target("README.md", "../outside.md").startswith("!ESCAPE:")
    assert find_bad_links("README.md", "[ok](README.md) [bad](missing.md)", exists) == [
        ("README.md", 1, "missing.md")]
    assert find_bad_links("README.md", "~~~md\n[example](ghost.md)\n~~~\n[ok](README.md)", exists) == []
    assert find_bad_links("research/a.md", "[relative](../README.md)", exists) == []
    print("Navigation local-link unit regressions: PASS")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--strict-core", action="store_true")
    group.add_argument("--strict-all", action="store_true")
    group.add_argument("--report-all", action="store_true")
    group.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return

    root_files = sorted(p.name for p in ROOT.iterdir() if p.is_file() and p.name != ".git")
    print(f"Top-level files: {len(root_files)} (baseline maximum {MAX_ROOT_FILES})")
    if args.strict_core:
        paths = CORE
    else:
        paths = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.md")
                       if ".git" not in p.parts)
    failures = scan(paths)
    print(f"Markdown file scope: {len(paths)}; unresolved local links: {len(failures)}")
    for src, lineno, target in failures[:80]:
        print(f"  {src}:{lineno}: {target}")
    if len(failures) > 80:
        print(f"  ... and {len(failures)-80} more")
    if args.report_all:
        print("REPORT ONLY: findings require source-level review; no automatic deletion.")
        return
    if len(root_files) > MAX_ROOT_FILES:
        raise SystemExit("FAIL: root clutter increased; put new material under an existing domain directory.")
    if failures:
        raise SystemExit("FAIL: local link integrity regression")
    print("Public navigation integrity and root clutter budget: PASS")


if __name__ == "__main__":
    main()
