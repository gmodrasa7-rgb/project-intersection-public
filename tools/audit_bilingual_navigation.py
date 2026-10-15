#!/usr/bin/env python3
"""Audit the public EN1/KO2 reader interface, provenance and language metadata.

This is deterministic structural checking, not a translation quality certificate,
scientific validation, authorship adjudication, or proof of complete legacy coverage.
"""
from __future__ import annotations

import argparse
import copy
import json
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTER = "knowledge/language-edition-register.json"
HANGUL = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
LINKS = re.compile(r"!?(?:\[[^\]\n]*\])\(([^)\n]+)\)")
PAIRED_NAV = {
    "PI-NAV-START": (7, "START_HERE"),
    "PI-NAV-TOC": (10, "RESEARCH_TOC"),
    "PI-NAV-REVIEW": (6, "AI_REVIEW"),
}
TOC_CRITICAL = (
    "../experiments/e009/RESULT.md",
    "../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md",
    "../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md",
    "../CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md",
)
REVIEW_CRITICAL = (
    "../experiments/e007/README.md",
    "../experiments/e008/README.md",
    "../experiments/e009/RESULT.md",
    "../experiments/e010/README_KO.md",
    "../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md",
)


def visible_text(body: str) -> str:
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"(?ms)^\s*(```|~~~).*?^\s*(?:```|~~~)\s*$", "", body)
    body = re.sub(r"`[^`\n]+`", "", body)
    body = LINKS.sub("", body)
    body = re.sub(r"https?://\S+", "", body)
    return body


def relative_links(path: str, body: str) -> list[str]:
    found = []
    for raw in LINKS.findall(body):
        u = urlsplit(raw)
        if not (u.scheme or u.netloc or raw.startswith("#")):
            found.append(unquote(u.path))
    return found


def sections(body: str) -> list[tuple[int, list[str]]]:
    results = []
    matches = list(re.finditer(r"(?m)^## (\d+)\.\s+", body))
    for i, m in enumerate(matches):
        stop = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        results.append((int(m.group(1)), LINKS.findall(body[m.end():stop])))
    return results


def list_paths_from_section_links(links: list[str]) -> list[str]:
    return [unquote(urlsplit(raw).path) for raw in links if not urlsplit(raw).scheme]


def comparable_source_path(raw: str) -> str:
    """The *_EN/KO editions are the same source position, not the same file."""
    if raw.endswith("_EN.md") or raw.endswith("_KO.md"):
        stem = raw[:-6]
        if stem.endswith(("RESEARCH_OVERVIEW", "PUBLIC_EVIDENCE_INDEX", "RESEARCH_STATUS_POLICY")):
            return stem + ".md"
    return raw


def git_blob_digest(content: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(content)).encode("ascii") + b"\\x00" + content).hexdigest()


def inspect(registry: dict, overrides: dict[str, str] | None = None, full_inventory: bool = True) -> list[str]:
    overrides = overrides or {}
    issues = []
    def load(path: str) -> str:
        return overrides.get(path, (ROOT / path).read_text(encoding="utf-8"))

    rows = registry.get("inventory", [])
    paths = [r.get("path") for r in rows if isinstance(r, dict)]
    if len(paths) != len(set(paths)):
        issues.append("DUPLICATE_INVENTORY_PATH")
    if paths != sorted(paths):
        issues.append("INVENTORY_NOT_SORTED")
    if full_inventory:
        actual = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.md") if ".git" not in p.parts)
        missing = sorted(set(actual) - set(paths))
        retired = sorted(set(paths) - set(actual))
        if missing:
            issues.append("NEW_MARKDOWN_NOT_REGISTERED:" + ",".join(missing[:20]))
        if retired:
            issues.append("REGISTERED_MARKDOWN_MISSING:" + ",".join(retired[:20]))
    for row in rows:
        path = row.get("path", "")
        if not (ROOT / path).is_file():
            issues.append("MISSING_SOURCE:" + path)
        if row.get("content_equivalence") != "NOT_REVIEWED":
            issues.append("MISLEADING_INVENTORY_CERTIFICATION:" + path)

    pairs = registry.get("pair_catalog", [])
    ids = set()
    for pair in pairs:
        pid = pair.get("id", "")
        en, ko = pair.get("original_1_english", ""), pair.get("original_2_korean", "")
        if pid in ids:
            issues.append("DUPLICATE_PAIR_ID:" + pid)
        ids.add(pid)
        if en not in paths or ko not in paths or not en.endswith("_EN.md") or not ko.endswith("_KO.md"):
            issues.append("PAIR_PATH_MISSING_OR_ORDER_INVALID:" + pid)
            continue
        if pair.get("meaning_review_status") == "REVIEWED" and not pair.get("independent_review_receipt"):
            issues.append("MEANING_REVIEW_CLAIM_WITHOUT_RECEIPT:" + pid)
        if pair.get("meaning_review_status") not in ("NOT_INDEPENDENTLY_VERIFIED", "STALE", "REVIEWED"):
            issues.append("UNKNOWN_MEANING_REVIEW_STATUS:" + pid)
        if pid.startswith("PI-CORE-"):
            expected_source = pair.get("source_legacy_path", "")
            if not (ROOT / expected_source).is_file():
                issues.append("LEGACY_SOURCE_MISSING:" + pid)
            else:
                actual_hash = git_blob_digest((ROOT / expected_source).read_bytes())
                if actual_hash != pair.get("source_blob_sha_at_split"):
                    issues.append("CORE_SOURCE_CHANGED_WITHOUT_NEW_EDITION_REVIEW:" + pid)
            for lang, path, other in (("en", en, ko), ("ko", ko, en)):
                body = load(path)
                if f"<!-- PI-LANGUAGE: {lang} -->" not in body:
                    issues.append("CORE_LANGUAGE_MARKER_MISSING:" + path)
                if f"<!-- PI-MIRROR: {other} -->" not in body:
                    issues.append("CORE_COUNTERPART_MARKER_MISSING:" + path)
                if f"<!-- PI-SOURCE: {expected_source} -->" not in body:
                    issues.append("CORE_SOURCE_MARKER_MISSING:" + path)
                if lang == "en" and HANGUL.search(visible_text(body)):
                    issues.append("CORE_ENGLISH_SCRIPT_LEAK:" + path)
                if lang == "ko" and len(HANGUL.findall(visible_text(body))) < 200:
                    issues.append("CORE_KOREAN_BODY_MISSING:" + path)
                for target in relative_links(path, body):
                    if target and not ((ROOT / path).parent / target).exists():
                        issues.append("CORE_BROKEN_LINK:" + path + ":" + target)
            if pid == "PI-CORE-PUBLIC-EVIDENCE-INDEX":
                for metric in ("0.090022", "0.063241", "0.065323", "42.35%"):
                    if metric not in load(en) or metric not in load(ko):
                        issues.append("E009_NUMERIC_PARITY_FAILED:" + metric)
        if pid not in PAIRED_NAV:
            continue

        expected_n, _ = PAIRED_NAV[pid]
        for lang, path, counterpart in (("en", en, ko), ("ko", ko, en)):
            body = load(path)
            if f"<!-- PI-LANGUAGE: {lang} -->" not in body:
                issues.append("LANGUAGE_DECLARATION_MISSING:" + path)
            if f"<!-- PI-MIRROR: {counterpart} -->" not in body:
                issues.append("MIRROR_ROUTE_MISSING:" + path)
            if lang == "en" and HANGUL.search(visible_text(body)):
                issues.append("ENGLISH_NARRATIVE_LANGUAGE_LEAK:" + path)
            if lang == "ko" and len(HANGUL.findall(visible_text(body))) < 50:
                issues.append("INSUFFICIENT_KOREAN_NARRATIVE:" + path)
            if not body.startswith(("# Start Here" if pid == "PI-NAV-START" and lang == "en" else
                                    "# 공개자료실 시작" if pid == "PI-NAV-START" else "#")):
                issues.append("NAV_TITLE_MISSING:" + path)
            for target in relative_links(path, body):
                if not target:
                    continue
                dest = (ROOT / path).parent / target
                if not dest.exists():
                    issues.append("UNRESOLVED_LOCAL_LINK:" + path + ":" + target)

            if pid != "PI-NAV-START":
                numbered = sections(body)
                if [x[0] for x in numbered] != list(range(1, expected_n + 1)):
                    issues.append("NAV_SECTION_SEQUENCE_DRIFT:" + path)
                core = TOC_CRITICAL if pid == "PI-NAV-TOC" else REVIEW_CRITICAL
                linked = set(relative_links(path, body))
                if pid == "PI-NAV-TOC":
                    suffix = "_EN.md" if lang == "en" else "_KO.md"
                    for stem in ("RESEARCH_OVERVIEW", "PUBLIC_EVIDENCE_INDEX", "RESEARCH_STATUS_POLICY"):
                        target = "../" + stem + suffix
                        if target not in linked:
                            issues.append("PREFERRED_LANGUAGE_RESEARCH_ROUTE_MISSING:" + path + ":" + target)
                for source in core:
                    if source not in linked:
                        issues.append("REQUIRED_EVIDENCE_ROUTE_MISSING:" + path + ":" + source)

        en_sections = sections(load(en))
        ko_sections = sections(load(ko))
        if pid == "PI-NAV-TOC" and len(en_sections) == 10 and len(ko_sections) == 10:
            for (number, a), (_, b) in zip(en_sections[:9], ko_sections[:9]):
                if [comparable_source_path(x) for x in list_paths_from_section_links(a)] != [comparable_source_path(x) for x in list_paths_from_section_links(b)]:
                    issues.append(f"TOC_PARALLEL_SOURCE_ORDER_DRIFT:section_{number}")

    snapshot = registry.get("metrics", {})
    if snapshot.get("meaning_verified_pairs") != 0:
        # Explicitly update this only after storing a real review receipt.
        receipts = [p for p in pairs if p.get("meaning_review_status") == "REVIEWED" and p.get("independent_review_receipt")]
        if len(receipts) != snapshot.get("meaning_verified_pairs"):
            issues.append("UNVERIFIED_MEANING_PARITY_METRIC")

    return sorted(set(issues))


def changed_pair_errors(registry: dict, base: str) -> list[str]:
    """Gate explicit new publication pairs; legacy source files remain inspectable."""
    out = []
    try:
        changed = set(subprocess.check_output(
            ["git", "diff", "--name-only", base + "...HEAD", "--"],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).splitlines())
    except (subprocess.CalledProcessError, OSError):
        return ["INVALID_GIT_DIFF_BASE"]
    for p in registry.get("pair_catalog", []):
        if p.get("id") not in PAIRED_NAV and not p.get("id", "").startswith("PI-CORE-"):
            continue
        en, ko = p["original_1_english"], p["original_2_korean"]
        if (en in changed) != (ko in changed):
            exc = p.get("one_sided_edit_exception")
            if not (p.get("meaning_review_status") == "STALE"
                    and isinstance(exc, str) and len(exc.strip()) >= 20
                    and REGISTER in changed):
                out.append("ONE_SIDED_PUBLIC_EDITION_UPDATE:" + p["id"])
    return out


def run_mutations(registry: dict) -> None:
    en = "navigation/RESEARCH_TOC_EN.md"
    ko = "navigation/RESEARCH_TOC_KO.md"
    base_en = (ROOT / en).read_text(encoding="utf-8")
    base_ko = (ROOT / ko).read_text(encoding="utf-8")
    mutants = [
        ({en: base_en.replace("## 3.", "## 7.", 1)}, None),
        ({en: base_en.replace("Founding question", "한글 침입", 1)}, None),
        ({ko: base_ko.replace("../experiments/e009/RESULT.md", "../absent.md", 1)}, None),
        ({en: base_en.replace("<!-- PI-MIRROR:", "<!-- missing:", 1)}, None),
    ]
    for changed, _ in mutants:
        assert inspect(registry, overrides=changed, full_inventory=False), "Mutation evaded audit"
    tampered = copy.deepcopy(registry)
    tampered["pair_catalog"][0]["meaning_review_status"] = "REVIEWED"
    assert any("WITHOUT_RECEIPT" in x for x in inspect(tampered, full_inventory=False))
    core_en = "PUBLIC_EVIDENCE_INDEX_EN.md"
    corrupted = (ROOT / core_en).read_text(encoding="utf-8").replace("0.090022", "0.990022", 1)
    assert any("E009_NUMERIC_PARITY_FAILED" in x for x in inspect(registry, overrides={core_en: corrupted}, full_inventory=False))
    print("Independent-language structural negative mutants: 6/6 detected")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--diff-base", default="")
    args = p.parse_args()
    registry = json.loads((ROOT / REGISTER).read_text(encoding="utf-8"))
    failures = inspect(registry)
    if args.diff_base:
        failures += changed_pair_errors(registry, args.diff_base)
    counts = registry.get("metrics", {}).get("filename_classes", {})
    print("Language-edition inventory:", registry.get("metrics", {}).get("markdown_total"), "Markdown paths")
    print("Filename-based categories:", json.dumps(counts, sort_keys=True))
    print("Meaningful human-reviewed pair count is unverified; filename pairing and checks are not translation parity.")
    if failures:
        for issue in failures:
            print("FAIL:", issue)
        raise SystemExit(1)
    if args.self_test:
        run_mutations(registry)
    print("Public original-1 English / original-2 Korean navigation parity: STRUCTURAL PASS")


if __name__ == "__main__":
    main()
