#!/usr/bin/env python3
"""PI-ACCESS: static task-navigation accessibility regression, not a WCAG certification.

Checks source files, task destinations, text navigation, bilingual pairing,
visible adverse evidence and known privacy/verification limits. No network.
"""
from __future__ import annotations
import argparse
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EN = "navigation/ACCESS_MAP_EN.md"
KO = "navigation/ACCESS_MAP_KO.md"
POLICY = ".github/ACCESSIBILITY.md"
README = "README.md"
EN_START = "navigation/START_HERE_EN.md"
KO_START = "navigation/START_HERE_KO.md"
LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
H = re.compile(r"(?m)^(#{1,6})\s+(.+)\s*$")
TASK_TARGETS = {
    "START_HERE": ("navigation/START_HERE_EN.md", "navigation/START_HERE_KO.md"),
    "PROGRAM": ("navigation/RESEARCH_PROGRAM_EN.md", "navigation/RESEARCH_PROGRAM_KO.md"),
    "EVIDENCE": ("research/PUBLIC_EVIDENCE_INDEX_EN.md", "research/PUBLIC_EVIDENCE_INDEX_KO.md"),
    "ADVERSE": ("experiments/e009/RESULT_EN.md", "experiments/e009/RESULT_KO.md"),
    "REPRO": ("experiments/e007/README_EN.md", "experiments/e007/README_KO.md"),
    "NOT_EXECUTED": ("experiments/e008/README_EN.md", "experiments/e008/README_KO.md"),
    "POSTHOC": ("experiments/e010/README_EN.md", "experiments/e010/README_KO.md"),
    "CRITIQUE": ("research/PUBLIC_REVIEW_PACKET_EN.md", "research/PUBLIC_REVIEW_PACKET_KO.md"),
    "VERSIONS": ("navigation/RESEARCH_VERSIONS_EN_KO.md", "navigation/RESEARCH_VERSIONS_EN_KO.md"),
    "CONTENTS": ("navigation/RESEARCH_TOC_EN.md", "navigation/RESEARCH_TOC_KO.md"),
    "FUND": ("funding/FUNDER_START_HERE.md", "funding/FUNDER_START_HERE.md"),
    "CORRECTION": (POLICY, POLICY),
}


def read(path: str, overrides: dict[str, str] | None = None) -> str:
    return overrides[path] if overrides and path in overrides else (ROOT / path).read_text(encoding="utf-8")


def local_links(path: str, body: str) -> list[tuple[str, str, str]]:
    output = []
    fenced = False
    for line in body.splitlines():
        if re.match(r"^\s{0,3}(?:\x60{3,}|~{3,})", line):
            fenced = not fenced
            continue
        if fenced:
            continue
        for title, raw in LINK.findall(line):
            target = urlsplit(raw.strip())
            if target.scheme or target.netloc:
                continue
            if not target.path:
                continue
            p = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(target.path)))
            output.append((title, p, target.fragment))
    return output


def find_errors(overrides: dict[str, str] | None = None) -> list[str]:
    issues = []
    en = read(EN, overrides)
    ko = read(KO, overrides)
    r = read(README, overrides)
    policy = read(POLICY, overrides)
    for lang, filename, opposite, body in (
        ("en", EN, KO, en), ("ko", KO, EN, ko)
    ):
        if f"<!-- PI-LANGUAGE: {lang} -->" not in body:
            issues.append("LANGUAGE_DECLARATION_MISSING:" + lang)
        if f"<!-- PI-MIRROR: {opposite} -->" not in body:
            issues.append("MIRROR_MISSING:" + lang)
        links = local_links(filename, body)
        link_paths = {target for _, target, _ in links}
        if opposite not in link_paths or POLICY not in link_paths or README not in link_paths:
            issues.append("RECIPROCAL_NAV_MISSING:" + lang)
        headings = [(len(m.group(1)), m.group(2)) for m in H.finditer(body)]
        if not headings or headings[0][0] != 1 or sum(level == 1 for level, _ in headings) != 1:
            issues.append("H1_STRUCTURE:" + lang)
        if any(b-a > 1 for (a, _), (b, _) in zip(headings, headings[1:])):
            issues.append("SKIPPED_HEADING_LEVEL:" + lang)
        if re.search(r"(?i)\[(?:click here|here|more|여기|클릭|자세히)\]\(", body):
            issues.append("AMBIGUOUS_LINK_TEXT:" + lang)
        for name, paths in TASK_TARGETS.items():
            wanted = paths[0 if lang == "en" else 1]
            if wanted not in link_paths:
                issues.append("MISSING_TASK_ROUTE:" + lang + ":" + name)
        if not any(token in body for token in ("not independent", "독립적", "NOT_REVIEWED")):
            issues.append("VERIFICATION_LIMIT_NOT_DISCLOSED:" + lang)
        for title, destination, fragment in links:
            if destination.startswith("../") or not (ROOT / destination).is_file():
                issues.append("BROKEN_LOCAL_LINK:" + lang + ":" + destination)
            if len(title.strip()) < 6:
                issues.append("NONDESCRIPTIVE_LABEL:" + lang + ":" + title)
            # Only detect fragments for paths explicitly in the user-visible role map.
            if fragment and destination.startswith("funding/") and (
                ("original-1--english" not in fragment and "원본2--한국어" not in fragment)):
                issues.append("FUNDING_FRAGMENT_DRIFT:" + lang)
    for filename, linkname in ((README, "ROOT"), (EN_START, "START_EN"), (KO_START, "START_KO")):
        targets = {dest for _, dest, _ in local_links(filename, read(filename, overrides))}
        wanted = (
            {EN, KO} if filename == README
            else {EN} if filename == EN_START else {KO}
        )
        if not wanted.issubset(targets):
            issues.append("READER_DISCOVERY_MISSING:" + linkname)
    # Founder's two language originals and negative-result disclosure must remain visible.
    if r.index("## Original 1 — English | Founding Purpose") >= r.index("## 원본2 — 한국어 | 창시 목적 전문 대응본"):
        issues.append("FOUNDING_LANGUAGE_ORDER_DRIFT")
    en_open = r.split("## Original 1 — English | Founding Purpose", 1)[1].split("<details>", 1)[0]
    ko_open = r.split("## 원본2 — 한국어 | 창시 목적 전문 대응본", 1)[1].split("<details>", 1)[0]
    for lang, opening, negative_path in (
        ("en", en_open, "experiments/e009/RESULT_EN.md"),
        ("ko", ko_open, "experiments/e009/RESULT_KO.md")):
        if negative_path not in opening:
            issues.append("NEGATIVE_EVIDENCE_HIDDEN:" + lang)
    if "## Original 1 — English" not in policy or "## 원본2 — 한국어" not in policy:
        issues.append("ACCESSIBILITY_EDITION_ORDER_MISSING")
    if not all(term in policy for term in ("issues/new", "개인", "private", "not", "아님")):
        issues.append("PRIVACY_REPORTING_AND_LIMITS_MISSING")
    return sorted(set(issues))


def self_test():
    assert not find_errors(), find_errors()
    base = {p: read(p) for p in (EN, KO, README, POLICY, EN_START, KO_START)}
    mutations = [
        ({EN: base[EN].replace("<!-- PI-MIRROR:", "<!-- bad:", 1)}, "MIRROR_MISSING"),
        ({KO: base[KO].replace("(../experiments/e009/RESULT_KO.md)", "(../experiments/e000/RESULT_KO.md)", 1)}, "MISSING_TASK_ROUTE"),
        ({EN: base[EN].replace("[E008 unexecuted main study]", "[click here]", 1)}, "AMBIGUOUS_LINK_TEXT"),
        ({EN: base[EN].replace("## Choose one task, not a folder", "#### Choose one task, not a folder", 1)}, "SKIPPED_HEADING_LEVEL"),
        ({README: base[README].replace("(navigation/ACCESS_MAP_KO.md)", "(navigation/MISSING_KO.md)", 1)}, "READER_DISCOVERY_MISSING"),
        ({EN_START: base[EN_START].replace("(ACCESS_MAP_EN.md)", "(BAD_MAP_EN.md)", 1)}, "READER_DISCOVERY_MISSING"),
        ({POLICY: base[POLICY].replace("issues/new", "contact-private", 2)}, "PRIVACY_REPORTING_AND_LIMITS_MISSING"),
        ({EN: base[EN].replace("[English claim-by-claim public evidence index]", "[x]", 1)}, "NONDESCRIPTIVE_LABEL"),
        ({KO: base[KO].replace("<!-- PI-LANGUAGE: ko -->", "<!-- PI-LANGUAGE: xx -->", 1)}, "LANGUAGE_DECLARATION_MISSING"),
        # Mutate the checked detailed opening, not the earlier founding preface.
        ({README: base[README].replace(
            "**Contrary evidence visible before expanding:** [E009](experiments/e009/RESULT_EN.md)",
            "**Contrary evidence visible before expanding:** [E009](experiments/e009/BAD.md)", 1)},
         "NEGATIVE_EVIDENCE_HIDDEN"),
    ]
    for overrides, expected in mutations:
        issues = find_errors(overrides)
        assert any(expected in x for x in issues), (expected, issues)
    print("PI-ACCESS static navigation and 10 adversarial mutations: PASS")
    print("LIMIT: link/heading tests cannot certify screen-reader use, translation parity or science.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    opts = parser.parse_args()
    problems = find_errors()
    if problems:
        raise SystemExit("PI_ACCESS_FAIL:\n" + "\n".join(problems))
    if opts.self_test:
        self_test()
    else:
        print("PI-ACCESS static navigation: PASS (usability not certified)")
