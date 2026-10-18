#!/usr/bin/env python3
"""Deterministic repository-local Markdown link integrity and landing clutter budget.

Checks local paths across Markdown and checks same-repository main-branch URLs
and GitHub-style heading anchors for a bounded set of public reader entrypoints.
External websites and scientific truth are NOT verified. No network or third-party dependencies.
Do not use this to delete historical source, failure or contribution records.
"""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import unicodedata
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
READER_ENTRYPOINTS = (
    "README.md",
    "AI_REVIEW_START_HERE.md",
    "navigation/START_HERE_EN.md",
    "navigation/START_HERE_KO.md",
    "navigation/RESEARCH_TOC_EN.md",
    "navigation/RESEARCH_TOC_KO.md",
    "research/PUBLIC_EVIDENCE_INDEX_EN.md",
    "research/PUBLIC_EVIDENCE_INDEX_KO.md",
    "research/PUBLIC_REVIEW_PACKET_EN.md",
    "research/PUBLIC_REVIEW_PACKET_KO.md",
)
SELF_REPO = "/gmodrasa7-rgb/project-intersection-public/"

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



def reader_target(source: str, destination: str):
    """Resolve an entrypoint link; preserve #fragment for heading validation.

    Only GitHub links to THIS repo on main count as internal absolute links.
    Historical commit URLs, external sites and other branches stay untested.
    """
    raw = destination.strip()
    if raw.startswith("<"):
        raw = raw[1:].split(">", 1)[0]
    else:
        raw = raw.split()[0] if raw else ""
    if not raw or raw.startswith("//"):
        return None
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc:
        prefix = SELF_REPO + "blob/main/"
        tree_prefix = SELF_REPO + "tree/main/"
        if (parsed.scheme != "https" or parsed.netloc != "github.com"
                or not (parsed.path.startswith(prefix) or parsed.path.startswith(tree_prefix))):
            return None
        candidate = parsed.path[len(prefix):] if parsed.path.startswith(prefix) else parsed.path[len(tree_prefix):]
        target = unquote(candidate)
    else:
        target = local_target(source, raw)
        if target is None and raw.startswith("#"):
            target = source
    if target is None:
        return None
    return target, unquote(parsed.fragment)


def github_heading_anchors(body: str):
    """Approximate GitHub heading slugs; explicit anchors and duplicate headings included.

    This catches ordinary broken headings, not GitHub's full Markdown rendering.
    """
    result = set()
    seen = {}
    for _, line in iter_live_lines(body):
        for name in re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', line):
            result.add(name)
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", match.group(1))
        heading = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = heading.replace(chr(96), "").replace("*", "").replace("~", "")
        heading = "".join(
            char for char in heading.lower()
            if char.isspace() or char in "-_" or
            not unicodedata.category(char).startswith(("P", "S"))
        ).strip()
        base = re.sub(r"\s", "-", heading)
        index = seen.get(base, 0)
        seen[base] = index + 1
        result.add(base if not index else f"{base}-{index}")
    return result


def find_bad_reader_links(source: str, body: str, exists, read_text):
    """Check the first-reader routes including anchored and self-repository main URLs."""
    bad = []
    anchor_cache = {}
    for lineno, line in iter_live_lines(body):
        for match in LINK.finditer(line):
            resolved = reader_target(source, match.group(1))
            if resolved is None:
                continue
            target, fragment = resolved
            if target.startswith("!") or not exists(target):
                bad.append((source, lineno, target))
            elif fragment and target.endswith(".md"):
                if target not in anchor_cache:
                    anchor_cache[target] = github_heading_anchors(read_text(target))
                if fragment not in anchor_cache[target]:
                    bad.append((source, lineno, target + "#" + fragment))
    return bad


def scan_reader_entrypoints():
    paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if ".git" not in p.parts}
    errors = []
    for source in READER_ENTRYPOINTS:
        full = ROOT / source
        if not full.is_file():
            errors.append((source, 0, "!ENTRYPOINT-MISSING"))
            continue
        errors.extend(find_bad_reader_links(
            source, full.read_text(encoding="utf-8"),
            lambda p: p in paths,
            lambda p: (ROOT / p).read_text(encoding="utf-8"),
        ))
    return errors


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
    fake = {"README.md": "# Purpose\n## Repeated\n## Repeated\n",
            "guide.md": "# Target heading\n"}
    assert github_heading_anchors(fake["README.md"]) >= {"purpose", "repeated", "repeated-1"}
    assert not find_bad_reader_links(
        "README.md", "[ok](guide.md#target-heading) [external](https://example.org/x#absent)",
        lambda p: p in fake, lambda p: fake[p])
    assert find_bad_reader_links(
        "README.md", "[bad](guide.md#absent) [local-bad](https://github.com/gmodrasa7-rgb/project-intersection-public/blob/main/ghost.md)",
        lambda p: p in fake, lambda p: fake[p]) == [
            ("README.md", 1, "guide.md#absent"), ("README.md", 1, "ghost.md")]
    assert reader_target("README.md", "https://github.com/gmodrasa7-rgb/project-intersection-public/blob/main/guide.md#target-heading") == ("guide.md", "target-heading")
    discovery = json.loads((ROOT / "AI_DISCOVERY_INDEX.json").read_text(encoding="utf-8"))
    assert not discovery_route_errors(discovery), discovery_route_errors(discovery)
    broken = json.loads(json.dumps(discovery))
    broken["entrypoints"]["overview"] = broken["historical_entrypoints"]["prior_values"]["overview"]
    assert "CURRENT_ROUTE_OUTDATED:overview" in discovery_route_errors(broken)
    print("Navigation local-link and current-versus-historical route regressions: PASS")


def discovery_route_errors(index: dict) -> list[str]:
    """Current EN/KO defaults must not silently point to historical mixed editions."""
    entry = index.get("entrypoints", {})
    pair_targets = {
        "overview": "research/RESEARCH_OVERVIEW_EN.md",
        "overview_ko": "research/RESEARCH_OVERVIEW_KO.md",
        "toc": "navigation/RESEARCH_TOC_EN.md",
        "toc_ko": "navigation/RESEARCH_TOC_KO.md",
        "review": "navigation/AI_REVIEW_EN.md",
        "review_ko": "navigation/AI_REVIEW_KO.md",
        "evidence": "research/PUBLIC_EVIDENCE_INDEX_EN.md",
        "evidence_ko": "research/PUBLIC_EVIDENCE_INDEX_KO.md",
        "negative_results": "experiments/e009/RESULT_EN.md",
        "negative_results_ko": "experiments/e009/RESULT_KO.md",
        "public_study_navigation": "navigation/START_HERE_KO.md",
    }
    errors = []
    for key, relative in pair_targets.items():
        expected = "/blob/main/" + relative
        if not str(entry.get(key, "")).endswith(expected):
            errors.append("CURRENT_ROUTE_OUTDATED:" + key)
    historic = index.get("historical_entrypoints", {}).get("prior_values", {})
    for key in ("overview", "toc", "review", "evidence", "negative_results", "public_study_navigation"):
        if key not in historic:
            errors.append("HISTORICAL_ENTRYPOINT_NOT_PRESERVED:" + key)
    return errors


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
    discovery = json.loads((ROOT / "AI_DISCOVERY_INDEX.json").read_text(encoding="utf-8"))
    route_failures = discovery_route_errors(discovery)
    reader_failures = scan_reader_entrypoints()
    print(f"Markdown file scope: {len(paths)}; unresolved local links: {len(failures)}")
    print(f"Current/historical discovery route errors: {len(route_failures)}")
    print(f"Critical reader-route path/anchor errors: {len(reader_failures)}")
    for src, lineno, target in reader_failures[:40]:
        print(f"  READER {src}:{lineno}: {target}")
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
    if route_failures:
        raise SystemExit("FAIL: AI discovery route regression: " + ", ".join(route_failures))
    if reader_failures:
        raise SystemExit("FAIL: public reader link/anchor regression")
    print("Public navigation integrity and root clutter budget: PASS")


if __name__ == "__main__":
    main()
