#!/usr/bin/env python3
"""Guard externally useful EN/KO review routes, not scientific truth or human usability.

The scope is deliberately narrow: authored Markdown edges, local fragment targets,
language-specific entry endpoints, and one known stale numeric summary.
External URL reachability, understanding, translation equivalence and experiment
validity require different kinds of evidence.
"""
from __future__ import annotations

import argparse
import posixpath
import re
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
HEADING = re.compile(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$")

# Each critical question must be answerable by reaching an exact, language-specific
# existing artifact from the GitHub landing page in no more than two link clicks.
REQUIRED = {
    "EN purpose": "navigation/START_HERE_EN.md",
    "KO purpose": "navigation/START_HERE_KO.md",
    "EN claim ledger": "research/PUBLIC_EVIDENCE_INDEX_EN.md",
    "KO claim ledger": "research/PUBLIC_EVIDENCE_INDEX_KO.md",
    "EN negative baseline": "experiments/e009/RESULT_EN.md",
    "KO negative baseline": "experiments/e009/RESULT_KO.md",
    "EN reproducible model": "experiments/e007/README_EN.md",
    "KO reproducible model": "experiments/e007/README_KO.md",
    "EN unexecuted study": "experiments/e008/README_EN.md",
    "KO unexecuted study": "experiments/e008/README_KO.md",
    "EN post-hoc exploratory": "experiments/e010/README_EN.md",
    "KO post-hoc exploratory": "experiments/e010/README_KO.md",
    "EN real-world prior-art boundaries": "research/CCPH_RESEARCH_ATLAS_EN.md",
    "KO real-world prior-art boundaries": "research/CCPH_RESEARCH_ATLAS_KO.md",
    "EN independent critique": "research/PUBLIC_REVIEW_PACKET_EN.md",
    "KO independent critique": "research/PUBLIC_REVIEW_PACKET_KO.md",
    "Funding and contact": "funding/FUNDER_START_HERE.md",
}
GATEWAYS = (
    "README.md",
    "navigation/START_HERE_EN.md",
    "navigation/START_HERE_KO.md",
    "funding/FUNDER_START_HERE.md",
)
EN_FUNDER_LINK = ("navigation/START_HERE_EN.md",
                  "funding/FUNDER_START_HERE.md", "original-1--english")
KO_FUNDER_LINK = ("navigation/START_HERE_KO.md",
                  "funding/FUNDER_START_HERE.md", "원본2--한국어")


def document(path: str, overrides: dict[str, str] | None = None) -> str:
    if overrides and path in overrides:
        return overrides[path]
    return (ROOT / path).read_text(encoding="utf-8")


def link_destinations(source: str, body: str):
    """Return only local navigational destinations (not external targets)."""
    inside = False
    for line in body.splitlines():
        if re.match(r"^\s{0,3}(?:\x60{3,}|~{3,})", line):
            inside = not inside
            continue
        if inside:
            continue
        for match in LINK.finditer(line):
            raw = match.group(1).split(" ", 1)[0]
            u = urlsplit(raw)
            if u.scheme or u.netloc or not u.path or raw.startswith("#"):
                continue
            dest = posixpath.normpath(posixpath.join(
                posixpath.dirname(source), unquote(u.path)))
            if dest.startswith("../") or dest == ".." or dest.startswith("/"):
                continue
            yield dest, unquote(u.fragment)


def slug(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_\x60~]", "", text).lower().strip()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def local_heading_ids(body: str) -> set[str]:
    values: set[str] = set()
    counts: dict[str, int] = {}
    for m in HEADING.finditer(body):
        base = slug(m.group(1))
        n = counts.get(base, 0)
        counts[base] = n + 1
        values.add(base + (f"-{n}" if n else ""))
    return values


def check(overrides: dict[str, str] | None = None) -> list[str]:
    errors = []
    page_cache = {}

    def load(path):
        if path not in page_cache:
            page_cache[path] = document(path, overrides)
        return page_cache[path]

    def neighbors(path):
        return list(link_destinations(path, load(path)))

    # A two-click bound is a test of authored graph distance only; it is not a
    # time-on-task measurement. A wrong-language intermediate does not qualify.
    for label, destination in REQUIRED.items():
        language = label[:2] if label.startswith(("EN ", "KO ")) else None
        queue = deque([("README.md", 0)])
        visited = {"README.md"}
        found = None
        while queue:
            current, steps = queue.popleft()
            if current == destination:
                found = steps
                break
            if steps >= 2:
                continue
            for target, _ in neighbors(current):
                if target in visited:
                    continue
                if language and steps == 0 and target.startswith("navigation/START_HERE_"):
                    if not target.endswith(f"_{language}.md"):
                        continue
                if target != destination and target not in GATEWAYS:
                    continue
                visited.add(target)
                queue.append((target, steps + 1))
        if found is None:
            errors.append(f"REVIEW_ROUTE_OVER_TWO_CLICKS_OR_WRONG_LANGUAGE:{label}:{destination}")

    # Check local headings in the small externally promoted gateway set. This
    # catches dangling anchors even when the destination file itself exists.
    for page in GATEWAYS:
        for dest, fragment in neighbors(page):
            if not fragment:
                continue
            if not (ROOT / dest).is_file() and not (overrides and dest in overrides):
                errors.append(f"GATEWAY_TARGET_MISSING:{page}:{dest}")
                continue
            if dest.endswith(".md") and fragment not in local_heading_ids(load(dest)):
                errors.append(f"GATEWAY_FRAGMENT_MISSING:{page}:{dest}#{fragment}")

    for source, dest, fragment in (EN_FUNDER_LINK, KO_FUNDER_LINK):
        if (dest, fragment) not in neighbors(source):
            errors.append(f"LANGUAGE_FUNDER_DEEPLINK_MISSING:{source}")

    overview_en = load("research/RESEARCH_OVERVIEW_EN.md")
    overview_ko = load("research/RESEARCH_OVERVIEW_KO.md")
    if "27 standalone regression tests" not in overview_en or "26 tests" in overview_en:
        errors.append("E007_EN_STALE_TEST_COUNT")
    if "단독 회귀검사 27개" not in overview_ko or "테스트 26개" in overview_ko:
        errors.append("E007_KO_STALE_TEST_COUNT")

    funder = load("funding/FUNDER_START_HERE.md")
    if "Historical grant proposals below are not documented awards" not in funder:
        errors.append("UNAWARDED_FUNDING_BOUNDARY_MISSING")
    if not ("No external scientific reviewer or funder has been shown" in funder):
        errors.append("EXTERNAL_REVIEW_NOT_YET_DONE_BOUNDARY_MISSING")
    return errors


def self_test():
    base = check()
    assert not base, base

    en = document("navigation/START_HERE_EN.md")
    drift = en.replace("../experiments/e009/RESULT_EN.md",
                       "../experiments/e009/RESULT_KO.md")
    assert "REVIEW_ROUTE_OVER_TWO_CLICKS_OR_WRONG_LANGUAGE" in " ".join(
        check({"navigation/START_HERE_EN.md": drift}))

    ko = document("navigation/START_HERE_KO.md")
    changed = ko.replace("#원본2--한국어", "#missing-korean-anchor")
    assert "GATEWAY_FRAGMENT_MISSING" in " ".join(
        check({"navigation/START_HERE_KO.md": changed}))

    en_overview = document("research/RESEARCH_OVERVIEW_EN.md")
    assert "E007_EN_STALE_TEST_COUNT" in check({
        "research/RESEARCH_OVERVIEW_EN.md":
        en_overview.replace("27 standalone regression tests", "26 tests")
    })

    funding = document("funding/FUNDER_START_HERE.md")
    assert "UNAWARDED_FUNDING_BOUNDARY_MISSING" in check({
        "funding/FUNDER_START_HERE.md":
        funding.replace("Historical grant proposals below are not documented awards",
                        "Historical grant proposals")
    })

    print("External-review route guard: PASS (4 deliberate defects rejected)")
    print("Boundary: static graph/anchor/status checks, not visitor usability or scientific validation")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    issues = check()
    print(f"External-review required routes: {len(REQUIRED)}")
    print("Maximum authored route depth: two clicks from README")
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        raise SystemExit(1)
    print("PASS: EN/KO gateway paths, fragments and bounded status claims")
    print("NOT TESTED: real visitor understanding, remote URLs, scientific validity")


if __name__ == "__main__":
    main()
