#!/usr/bin/env python3
"""Public-language reading guard. Structural checks are not translation certification.

Hard-fail the current entry pair and README separation. Legacy files are inventoried,
not silently deleted or declared translated. New Markdown files can be checked in CI.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = "navigation/START_HERE_EN.md"
KO_PATH = "navigation/START_HERE_KO.md"
EN_README = "## Original 1 — English | Founding Purpose"
KO_README = "## 원본2 — 한국어 | 창시 목적 전문 대응본"
SECTIONS = ("purpose", "levels", "evidence", "ccph", "rights", "navigation", "limitations")
REQUIRED = (
    "../README.md",
    "../PUBLIC_EVIDENCE_INDEX.md",
    "../RESEARCH_TOC.md",
    "../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md",
    "../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md",
    "../experiments/e009/RESULT.md",
)
MD_LINK = re.compile(r"!?(?:\[[^\]\n]*\])\(([^)\n]+)\)")
SECTION = re.compile(r"<!-- PI-SECTION: ([a-z-]+) -->")
KOREAN = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
FENCED = re.compile(r"(?ms)^\s*```.*?^\s*```\s*$")


def human_text(body: str) -> str:
    """Remove non-prose paths and protected markup before checking language leakage."""
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = FENCED.sub("", body)
    body = re.sub(r"`[^`\n]+`", "", body)
    body = MD_LINK.sub(lambda m: m.group(0).split("](")[0] + "]", body)
    body = re.sub(r"https?://\S+", "", body)
    return body


def readme_errors(body: str) -> list[str]:
    errors = []
    if body.count(EN_README) != 1 or body.count(KO_README) != 1:
        return ["README_ORIGINAL_MARKERS_MISSING_OR_DUPLICATE"]
    a, b = body.index(EN_README), body.index(KO_README)
    if a >= b:
        return ["README_ORIGINAL_ORDER_REVERSED"]
    english = human_text(body[a:b])
    if KOREAN.search(english):
        errors.append("README_ENGLISH_SECTION_CONTAINS_KOREAN_PROSE")
    if "## Start here / 여기서 시작" in body:
        errors.append("README_LEGACY_MIXED_ROUTER_NOT_REMOVED")
    first_en = body.split(EN_README, 1)[1].split(KO_README, 1)[0]
    first_ko = body.split(KO_README, 1)[1]
    if "navigation/START_HERE_KO.md" not in first_en[:300]:
        errors.append("README_TOP_KOREAN_SWITCH_MISSING")
    if "navigation/START_HERE_EN.md" not in first_ko[:300]:
        errors.append("README_TOP_ENGLISH_SWITCH_MISSING")
    for link in ("navigation/START_HERE_EN.md", "navigation/START_HERE_KO.md"):
        if link not in body:
            errors.append("README_LANGUAGE_ROUTE_MISSING:" + link)
    return errors


def guide_errors(path: str, body: str, language: str) -> list[str]:
    errors = []
    mirror = KO_PATH if language == "en" else EN_PATH
    if f"<!-- PI-LANGUAGE: {language} -->" not in body:
        errors.append(f"{path}:LANGUAGE_DECLARATION_MISSING")
    if f"<!-- PI-MIRROR: {mirror} -->" not in body:
        errors.append(f"{path}:MIRROR_DECLARATION_MISSING")
    if SECTION.findall(body) != list(SECTIONS):
        errors.append(f"{path}:SECTIONS_MISSING_REORDERED_OR_DUPLICATED")
    if language == "en":
        if not body.startswith("# Start Here — Original 1: English"):
            errors.append(f"{path}:EN_FIRST_EDITION_LABEL_MISSING")
        if KOREAN.search(human_text(body)):
            errors.append(f"{path}:ENGLISH_PROSE_CONTAINS_KOREAN")
    else:
        if not body.startswith("# 공개자료실 시작 — 원본2: 한국어"):
            errors.append(f"{path}:KO_SECOND_EDITION_LABEL_MISSING")
        if len(KOREAN.findall(human_text(body))) < 100:
            errors.append(f"{path}:INSUFFICIENT_KOREAN_READING_CONTENT")
    links = set(MD_LINK.findall(body))
    for mandatory in REQUIRED:
        if mandatory not in links:
            errors.append(f"{path}:REQUIRED_ROUTE_MISSING:{mandatory}")
    if language == "en" and "START_HERE_KO.md" not in body:
        errors.append(f"{path}:COUNTERPART_NOT_DISCOVERABLE")
    if language == "ko" and "START_HERE_EN.md" not in body:
        errors.append(f"{path}:COUNTERPART_NOT_DISCOVERABLE")
    return errors


def local_link_errors(path: str, body: str) -> list[str]:
    failures = []
    parent = (ROOT / path).parent
    for raw in MD_LINK.findall(body):
        url = urlsplit(raw)
        if url.scheme or url.netloc or raw.startswith("#"):
            continue
        target = unquote(url.path)
        if target and not (parent / target).exists():
            failures.append(f"{path}:BROKEN_LINK:{target}")
    return failures


def edition_of(path: str) -> str:
    if path.endswith("_EN_KO.md") or path.endswith("_BILINGUAL.md"):
        return "dual"
    if path.endswith("_EN.md"):
        return "en"
    if path.endswith("_KO.md"):
        return "ko"
    return "unspecified"


def new_files_errors(paths: list[str]) -> list[str]:
    errors = []
    for name in paths:
        if not name.endswith(".md") or name.startswith(".github/"):
            continue
        # Existing legacy paths are not reclassified retroactively here.
        kind = edition_of(name)
        p = ROOT / name
        if not p.is_file():
            errors.append(f"ADDED_DOCUMENT_MISSING:{name}")
            continue
        body = p.read_text(encoding="utf-8")
        if kind in ("en", "ko"):
            if kind == "en":
                partner = name[:-6] + "_KO.md"
                if KOREAN.search(human_text(body)):
                    errors.append(f"ADDED_ENGLISH_DOCUMENT_HAS_KOREAN_PROSE:{name}")
            else:
                partner = name[:-6] + "_EN.md"
            if not (ROOT / partner).exists():
                errors.append(f"ADDED_DOCUMENT_MIRROR_MISSING:{name}:{partner}")
        elif kind == "dual":
            en_at = re.search(r"(?m)^#{1,3}\s+.*(?:Original\s*1|원본\s*1)", body, re.I)
            ko_at = re.search(r"(?m)^#{1,3}\s+.*(?:Original\s*2|원본\s*2)", body, re.I)
            if not en_at or not ko_at or en_at.start() >= ko_at.start():
                errors.append(f"ADDED_BILINGUAL_DOCUMENT_NOT_SEPARATED:{name}")
        elif not re.search(r"<!-- PI-LANGUAGE-EXEMPT: .+ -->", body):
            errors.append(f"ADDED_MARKDOWN_LACKS_LANGUAGE_EDITION_OR_JUSTIFIED_EXCEPTION:{name}")
    return errors


def legacy_inventory() -> str:
    files = list(ROOT.rglob("*.md"))
    buckets = {name: 0 for name in ("en", "ko", "dual", "unspecified")}
    mixed = []
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        buckets[edition_of(relative)] += 1
        body = human_text(path.read_text(encoding="utf-8"))
        if KOREAN.search(body) and len(re.findall(r"\b[A-Za-z]{4,}\b", body)) > 40:
            mixed.append(relative)
    # This deliberately includes technical terminology and references: REVIEW SIGNAL ONLY.
    return (f"Inventory: {len(files)} Markdown; naming en={buckets['en']}, "
            f"ko={buckets['ko']}, dual={buckets['dual']}, "
            f"unspecified={buckets['unspecified']}. "
            f"Possible mixed-script review candidates={len(mixed)} (heuristic, not defects). "
            f"Examples: {', '.join(mixed[:7])}")


def self_test(en: str, ko: str, readme: str) -> None:
    assert not guide_errors(EN_PATH, en, "en"), guide_errors(EN_PATH, en, "en")
    assert not guide_errors(KO_PATH, ko, "ko"), guide_errors(KO_PATH, ko, "ko")
    assert not readme_errors(readme), readme_errors(readme)
    mutations = [
        guide_errors(EN_PATH, en.replace("Original 1: English", "English", 1), "en"),
        guide_errors(EN_PATH, en.replace("## 4. CCPH", "## 4. 한국어 CCPH", 1), "en"),
        guide_errors(EN_PATH, en.replace("<!-- PI-SECTION: ccph -->", "", 1), "en"),
        guide_errors(KO_PATH, ko.replace("<!-- PI-MIRROR:", "<!-- MISSING:", 1), "ko"),
        guide_errors(KO_PATH, ko.replace("../experiments/e009/RESULT.md", "../none.md"), "ko"),
        readme_errors(readme.replace(KO_README, "## Korean version", 1)),
    ]
    assert all(mutations), "Mutation bypassed language guard"
    print(f"Language routing mutation regressions: {len(mutations)} / {len(mutations)} PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--added", nargs="*", default=[])
    args = parser.parse_args()
    en = (ROOT / EN_PATH).read_text(encoding="utf-8")
    ko = (ROOT / KO_PATH).read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    failures = (guide_errors(EN_PATH, en, "en") +
                guide_errors(KO_PATH, ko, "ko") +
                readme_errors(readme) +
                local_link_errors(EN_PATH, en) +
                local_link_errors(KO_PATH, ko) +
                new_files_errors(args.added))
    if failures:
        raise SystemExit("LANGUAGE AUDIT FAIL:\n" + "\n".join(failures))
    print("Language entry separation, mirrored structure and local links: PASS")
    print(legacy_inventory())
    if args.self_test:
        self_test(en, ko, readme)
    print("LIMIT: structural/script checks do not certify translation parity or scientific validity.")


if __name__ == "__main__":
    main()
