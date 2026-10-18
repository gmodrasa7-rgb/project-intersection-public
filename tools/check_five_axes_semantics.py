#!/usr/bin/env python3
"""Bounded IVS-0R text/provenance regression for the provisional five axes.

This is NOT empirical validation, semantic translation certification, or a
guarantee that any model or cited source is scientifically correct.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = "research/TERMINOLOGY_FIVE_AXES_V0_1_EN.md"
KO = "research/TERMINOLOGY_FIVE_AXES_V0_1_KO.md"
REGISTER = "knowledge/language-edition-register.json"
NAV_EN = "navigation/START_HERE_EN.md"
NAV_KO = "navigation/START_HERE_KO.md"
PAIR_ID = "PI-RESEARCH-FIVE-AXES-V01"

COMMON = (
    "VC", "EI", "MER", "ECR", "IVS-0R", "ICM", "RGBM", "CCPH",
    "E007", "E008", "E009", "E010", "42.35%",
    "ds004128", "OSF", "OpenNeuro", "43", "32", "D0", "D4",
    "PR #211", "PR #212", "PR #213",
)
REQUIRED = {
    EN: (
        "MER — Mind–Experience–Response",
        "ECR — Entity–Constituency–Relation",
        "behavioral data",  # checked via source-location paragraph below
        "43 consented participants",
        "1 excluded for imaging artifacts",
        "10 for excessive motion",
        "NOT empirical validation",
        "independent",
        "not an intervention on coercion",
        "OSF page/file manifest was not accessible",
        "data were not downloaded or reanalyzed",
    ),
    KO: (
        "MER — Mind–Experience–Response",
        "ECR — Entity–Constituency–Relation",
        "실제 **행동자료의 별도 위치",
        "동의 참가자 43명",
        "영상 결함 1명",
        "과도한 움직임 10명",
        "현실 실증 아님",
        "독립",
        "강압·이탈권·지속 권력반전",
        "OSF 페이지와 개별 파일 목록을 직접 열지 못했음",
        "원자료 다운로드·재분석 미실행",
    ),
}


def inspect(bodies: dict[str, str], reg: dict) -> list[str]:
    problems: list[str] = []
    for p in (EN, KO):
        content = bodies[p]
        lang = "en" if p == EN else "ko"
        other = KO if p == EN else EN
        for t in (f"<!-- PI-LANGUAGE: {lang} -->",
                  f"<!-- PI-MIRROR: {other} -->"):
            if t not in content:
                problems.append(f"{p}: MISSING_METADATA: {t}")
        for keyword in COMMON + REQUIRED[p]:
            if keyword not in content:
                problems.append(f"{p}: REQUIRED_BOUNDARY_ABSENT: {keyword}")
        found = [int(m.group(1)) for m in
                 re.finditer(r"(?m)^## (\d+)\.", content)]
        if found != list(range(8)):
            problems.append(f"{p}: SECTION_SEQUENCE_DRIFT: {found}")
        if "http" not in content:
            problems.append(f"{p}: REFERENCES_MISSING")

    pairs = [r for r in reg.get("pair_catalog", [])
             if r.get("id") == PAIR_ID]
    if len(pairs) != 1:
        problems.append("REGISTER: PAIR_ID_MISSING_OR_DUPLICATE")
    else:
        p = pairs[0]
        if (p.get("original_1_english") != EN or
            p.get("original_2_korean") != KO or
            p.get("meaning_review_status") != "NOT_INDEPENDENTLY_VERIFIED"):
            problems.append("REGISTER: PAIR_OR_REVIEW_STATUS_DRIFT")

    inventory = {r.get("path"): r for r in reg.get("inventory", [])}
    for path, counterpart in ((EN, KO), (KO, EN)):
        row = inventory.get(path)
        if (not row or row.get("counterpart_path") != counterpart
            or row.get("content_equivalence") != "NOT_REVIEWED"):
            problems.append(f"REGISTER: EDITION_UNREGISTERED_OR_OVERCLAIMED: {path}")
    if reg.get("metrics", {}).get("markdown_total") != len(reg.get("inventory", [])):
        problems.append("REGISTER: INVENTORY_COUNT_DRIFT")
    if f"../{EN}" not in bodies[NAV_EN]:
        problems.append("NAV: EN_ROUTE_MISSING")
    if f"../{KO}" not in bodies[NAV_KO]:
        problems.append("NAV: KO_ROUTE_MISSING")
    return problems


def run_self_tests(bodies: dict[str, str], reg: dict) -> int:
    checks = [
        ("remove-english-osf-evidence", EN, "OSF", ""),
        ("remove-korean-osf-evidence", KO, "OSF", ""),
        ("erase-negative-result", EN, "42.35%", ""),
        ("erase-selection-denominator", KO, "동의 참가자 43명", "참가자 다수"),
        ("erase-llm-mind-distinction", EN, "MER — Mind–Experience–Response", "MER"),
        ("erase-ecr-origin", KO, "ECR — Entity–Constituency–Relation", "ECR"),
        ("erase-korean-scientific-scope", KO, "현실 실증 아님", "연구"),
        ("erase-english-osf-block", EN, "OSF page/file manifest was not accessible", "files verified"),
        ("erase-section", EN, "## 7.", "## X."),
        ("erase-provenance", KO, "<!-- PI-LANGUAGE: ko -->", ""),
    ]
    for name, path, before, after in checks:
        assert before in bodies[path], f"Bad self-test fixture: {name}"
        changed = dict(bodies)
        changed[path] = changed[path].replace(before, after, 1)
        assert inspect(changed, reg), f"FALSE PASS: {name}"
    changed_reg = json.loads(json.dumps(reg))
    changed_reg["pair_catalog"] = [
        r for r in changed_reg["pair_catalog"] if r.get("id") != PAIR_ID
    ]
    assert inspect(bodies, changed_reg), "FALSE PASS: removed paired provenance"
    changed_reg = json.loads(json.dumps(reg))
    changed_reg["metrics"]["markdown_total"] -= 1
    assert inspect(bodies, changed_reg), "FALSE PASS: inventory count"
    print(f"IVS-0R negative controls: {len(checks)+2}/{len(checks)+2} detected")
    return len(checks) + 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    bodies = {p: (ROOT / p).read_text(encoding="utf-8")
              for p in (EN, KO, NAV_EN, NAV_KO)}
    reg = json.loads((ROOT / REGISTER).read_text(encoding="utf-8"))
    problems = inspect(bodies, reg)
    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    if args.self_test:
        run_self_tests(bodies, reg)
    print("PASS: provisional terminology, source-location caveat, bilingual route"
          " and provenance preserved. NOT scientific or translation validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
