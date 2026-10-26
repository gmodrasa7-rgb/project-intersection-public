#!/usr/bin/env python3
"""Bounded structural guard for PI's FULL English Original 1 and Korean Original 2.

DOES NOT prove bilingual semantic equivalence, authorship priority, scientific
validity or complete reconstruction of historical conversations.
stdlib-only; use both default audit and '--self-test' failure injections.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/PI_ROADMAP_OPERATIONAL_GATES_V0_2_3_EN_KO.md"
AMENDMENT = ROOT / "research/PI_ROADMAP_DECISION_EVIDENCE_V0_2_4_EN_KO.md"
EN_HEAD = "## Original 1 — English (complete canonical text)"
KO_HEAD = "## 원본2 — 한국어 (동등한 전문 정본)"
END = "**Change receipt / 변경 영수증:**"
IDS = [f"R23-{i:02d}" for i in range(1, 13)]
FOUNDER_QUOTE = (
    "원숭이가 인간을 개발할 수 있다면, 자신이 이해하는 규칙 안에 "
    "인간을 가둘 수 있는가? 가능하다면 언제까지 가능한가?"
)
SOURCES = [
    "research/RESEARCH_ROADMAP_v0_1_EN_KO.md",
    "research/RESEARCH_ROADMAP_v0_2_EN_KO.md",
    "research/PI_ROADMAP_CHANGE_TRAP_V0_2_1_EN_KO.md",
    "research/PI_ROADMAP_HIDDEN_ROUTE_PRIOR_ART_V0_2_2_EN_KO.md",
    "PUBLIC_PREAMBLE_VOLUNTARY_COEXISTENCE_2026-10-13_EN_KO.md",
    "research/CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md",
    "TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md",
    "PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md",
    "RESEARCH_RIGHTS_SCOPE_EN_KO.md",
]
POLICY = "PRIOR_ART_FIRST_RESEARCH_POLICY_EN_KO.md"
STATE = ROOT / "AUTONOMOUS_RESEARCH_STATE.json"


def audit_work_order(state: dict, raw: str, root: Path = ROOT) -> list[str]:
    """Narrow cross-artifact drift check; no claim about actual search sufficiency."""
    errors = []
    policy = state.get("execution_policy", {})
    if policy.get("research_work_policy") != POLICY or not (root / POLICY).is_file():
        errors.append("WORK_ORDER_POLICY_SOURCE_MISSING")
    if policy.get("require_prior_art_gate") is not True or policy.get("require_read_back") is not True:
        errors.append("PRIOR_ART_OR_READBACK_GATE_DISABLED")
    order = state.get("priority_order")
    if (not isinstance(order, list) or not all(isinstance(x, str) for x in order)
            or len(order) != len(set(order))):
        errors.append("WORK_ORDER_INVALID_OR_DUPLICATED")
    else:
        required = {"persistence_provenance_integrity", "prior_art_novelty_narrowing",
                    "strong_counterexample_or_kill_test", "independent_external_or_empirical_validation",
                    "new_synthetic_test", "documentation_only"}
        if not required.issubset(order):
            errors.append("WORK_ORDER_TARGET_LOST")
        if order[:2] != ["persistence_provenance_integrity", "prior_art_novelty_narrowing"]:
            errors.append("PRIOR_ART_NOT_FIRST_RESEARCH_WORK")
    decision = state.get("current_operating_decision", {})
    if not decision.get("decision", "").startswith("PRIOR_ART_FIRST_"):
        errors.append("ACTIVE_DECISION_BYPASSES_PRIOR_ART")
    if POLICY not in decision.get("work_order_boundary", ""):
        errors.append("EVIDENCE_TARGET_MISREAD_AS_WORK_ORDER")
    if not state.get("next_checkpoint", "").startswith("Apply " + POLICY):
        errors.append("CHECKPOINT_BYPASSES_PRIOR_ART_POLICY")
    # Only the active R23-05 sections are checked. Historical v0.1/v0.2
    # statements and retained evidence targets are not rewritten or censored.
    editions = (("EN", EN_HEAD, KO_HEAD,
                 "Two zero-result rounds are not sufficient for saturation.",
                 "A resource-limited pause is not saturation."),
                ("KO", KO_HEAD, END,
                 "검색 결과 0건 두 번은 포화의 충분조건이 아니다.",
                 "자원 부족으로 중단해도 포화는 아니다."))
    for lang, start, end, insufficient, paused in editions:
        chapter = raw.split(start, 1)[-1].split(end, 1)[0]
        stage = chapter.split("<!-- ROADMAP_ID:R23-05 -->", 1)[-1].split("<!-- ROADMAP_ID:R23-06 -->", 1)[0]
        if any(token not in stage for token in (POLICY, insufficient, paused, "SEARCH_ACTIVE / UNKNOWN")):
            errors.append("SATURATION_BOUNDARY_MISSING:" + lang)
        s3 = next((line for line in stage.splitlines() if line.startswith("| **S3 ")), "")
        criteria = ("citation chains", "contrary searches", "material novelty", "residual unknowns") if lang == "EN" else ("인용 추적", "반대 검색", "실질 신규 정보", "잔여 미관측")
        if not all(token in s3 for token in criteria):
            errors.append("SATURATION_COVERAGE_CRITERIA_MISSING:" + lang)
    return errors


def work_order_self_test(state: dict, raw: str) -> dict:
    assert not audit_work_order(state, raw), audit_work_order(state, raw)
    tests = {}
    mutations = []
    for key in ("require_prior_art_gate", "require_read_back"):
        altered = copy.deepcopy(state)
        altered["execution_policy"][key] = False
        mutations.append((key, altered, raw))
    for name, change in (
        ("prior_art_fourth", lambda s: s.update(priority_order=["persistence_provenance_integrity", "independent_external_or_empirical_validation", "strong_counterexample_or_kill_test", "prior_art_novelty_narrowing", "new_synthetic_test", "documentation_only"])),
        ("priority_missing", lambda s: s.pop("priority_order")),
        ("priority_duplicate", lambda s: s["priority_order"].append(s["priority_order"][1])),
        ("policy_missing", lambda s: s["execution_policy"].pop("research_work_policy")),
        ("old_checkpoint", lambda s: s.update(next_checkpoint="F004: run the holdout next")),
        ("old_active_decision", lambda s: s["current_operating_decision"].pop("work_order_boundary")),
        ("old_active_label", lambda s: s["current_operating_decision"].update(decision="EXTERNAL_VALIDATION_FIRST_INTERNAL_COMPLEXITY_FREEZE")),
    ):
        altered = copy.deepcopy(state)
        change(altered)
        mutations.append((name, altered, raw))
    for lang, old, new in (
        ("EN_fixed_round", "Two zero-result rounds are not sufficient for saturation.", "Two zero-result rounds establish saturation."),
        ("KO_fixed_round", "검색 결과 0건 두 번은 포화의 충분조건이 아니다.", "검색 결과 0건 두 번이면 포화가 성립한다."),
        ("EN_pause_promoted", "A resource-limited pause is not saturation.", "A resource-limited pause proves saturation."),
        ("KO_pause_promoted", "자원 부족으로 중단해도 포화는 아니다.", "자원 부족으로 중단하면 포화다."),
        ("EN_missing_coverage", "citation chains, contrary searches, material novelty and residual unknowns", "two zero-result rounds"),
        ("KO_missing_coverage", "인용 추적·반대 검색·실질 신규 정보·잔여 미관측", "신규 결과 0건 2회"),
    ):
        assert old in raw, lang
        mutations.append((lang, state, raw.replace(old, new, 1)))
    for name, altered, text in mutations:
        tests[name] = len(audit_work_order(altered, text))
        assert tests[name] > 0, name
    return tests

def audit(raw: str, root: Path = ROOT) -> list[str]:
    errors = []
    def require(ok: bool, why: str) -> None:
        if not ok:
            errors.append(why)

    require(raw.count(EN_HEAD) == 1, "Missing/duplicate full English Original 1")
    require(raw.count(KO_HEAD) == 1, "Missing/duplicate full Korean Original 2")
    if raw.count(EN_HEAD) != 1 or raw.count(KO_HEAD) != 1:
        return errors
    front, english_rest = raw.split(EN_HEAD, 1)
    english, korean_rest = english_rest.split(KO_HEAD, 1)
    korean = korean_rest.split(END, 1)[0]
    require(len(english) > 5500 and len(korean) > 5500,
            "Full-text EN/KO chapter suspiciously truncated")
    require("v0.2.3" in front and "v0.1" in front,
            "Roadmap v0.2.3 versus PIA software v0.1 not differentiated")
    require("PARTIAL_RECALL" in front and "exhaustive" in front.lower(),
            "Conversation-coverage uncertainty lost")
    for language, chapter in (("EN", english), ("KO", korean)):
        tags = re.findall(r"<!-- ROADMAP_ID:(R23-\d\d) -->", chapter)
        headings = re.findall(r"^### (R23-\d\d)\.", chapter, re.M)
        require(tags == IDS, f"{language} IDs missing/reordered/duplicated: {tags}")
        require(headings == IDS, f"{language} headings missing/reordered")
        require(FOUNDER_QUOTE in chapter,
                f"{language} lost verbatim original technical founder question")
        stage = chapter.split("<!-- ROADMAP_ID:R23-05 -->", 1)
        stage = stage[1].split("<!-- ROADMAP_ID:R23-06 -->", 1)[0] if len(stage) == 2 else ""
        for n in range(1, 7):
            require(f"**S{n} " in stage, f"{language} missing stage S{n}")
        origin = chapter.split("<!-- ROADMAP_ID:R23-01 -->", 1)
        origin = origin[1].split("<!-- ROADMAP_ID:R23-02 -->", 1)[0] if len(origin) == 2 else ""
        require(("for how long" in origin.lower()) if language == "EN"
                else ("언제까지" in origin),
                f"{language} removed control feasibility/duration meaning marker")
        ending = chapter.split("<!-- ROADMAP_ID:R23-12 -->", 1)[-1]
        require("DESIGN" in ending and "NOT EXECUTED" in ending,
                f"{language} omitted unexecuted/science boundary")
        require("UNKNOWN" in chapter and "HOLD" in chapter,
                f"{language} lost uncertainty/hold markers")
        require("CI" in chapter and ("licen" in chapter.lower() if language == "EN"
                                  else "라이선스" in chapter),
                f"{language} lacks code-versus-rights scope")
    require(END in korean_rest, "Missing provenance/change receipt")
    require("Original 1" in front and "원본2" in front,
            "Precursor origin order and Korean equal status lost")
    for p in SOURCES:
        require((root / p).is_file(), f"Missing cited predecessor source: {p}")
    return errors


def self_test(raw: str) -> dict:
    # Four independent negative cases; these tests cannot detect nuanced mistranslation.
    clean = audit(raw)
    failures = {"clean": len(clean)}
    ko_start = raw.index(KO_HEAD)
    samples = {
        "deleted_KO": raw[:ko_start],
        "missing_KO_ID": raw[:ko_start] + raw[ko_start:].replace(
            "<!-- ROADMAP_ID:R23-07 -->", "", 1),
        "deleted_KO_stage": raw[:ko_start] + raw[ko_start:].replace(
            "**S4 검수", "**단계 검수", 1),
        "deleted_KO_founder_quote": raw[:ko_start] + raw[ko_start:].replace(
            FOUNDER_QUOTE, "창조한 존재를 가둘 권리가 있는가?", 1),
        "false_KO_science_certification": raw[:ko_start] + raw[ko_start:].replace(
            "NOT EXECUTED", "FIELD_VALIDATED", 1),
    }
    for key, mutated in samples.items():
        failures[key] = len(audit(mutated))
    if clean or not all(v > 0 for k, v in failures.items() if k != "clean"):
        raise AssertionError("Roadmap structural-guard injection failed: " +
                             json.dumps(failures, ensure_ascii=False))
    return failures


def audit_amendment(raw: str, e008: dict, e009: dict) -> list[str]:
    """D24 structure and frozen-result parity only; never translation certification."""
    errors = []
    en_head = "## Original 1 — English (full)"
    ko_head = "## 원본2 — 한국어 (동등한 전문)"
    if (raw.count(en_head) != 1 or raw.count(ko_head) != 1
            or raw.index(en_head) > raw.index(ko_head)):
        return ["D24_EDITION_MISSING_DUPLICATED_OR_REVERSED"]
    front, rest = raw.split(en_head, 1)
    en, rest = rest.split(ko_head, 1)
    ko = rest.split(END, 1)[0]
    if "PROPOSED METHOD / NOT EXECUTED" not in front or END not in rest:
        errors.append("D24_PROPOSAL_OR_CHANGE_RECEIPT_LOST")
    ids = [f"D24-{i:02d}" for i in range(1, 7)]
    states = ("GO_SCOPED", "HOLD_EVIDENCE", "HOLD_EXECUTABILITY",
              "NEGATIVE_PRESERVED", "NOT_COMPARABLE", "STOP_RISK")
    criteria = {k: v for k, v in e009["survival_criteria"].items()
                if k.startswith("criterion_")}
    failed = sum(v is False for v in criteria.values())
    percent = f'{-100 * e009["project_v3_vs_best_simple_regret_improvement"]:.2f}%'
    source_links = []
    for lang, chapter in (("EN", en), ("KO", ko)):
        headings = re.findall(r"^### (D24-\d\d)\.", chapter, re.M)
        if headings != ids:
            errors.append("D24_SECTION_ORDER_OR_COUNT:" + lang)
            continue
        parts = re.split(r"^### (D24-\d\d)\.[^\n]*\n", chapter, flags=re.M)
        sections = dict(zip(parts[1::2], parts[2::2]))
        source_links.append(set(re.findall(r"https://[^)\s]+", sections["D24-01"])))
        if not all(s in sections["D24-02"] for s in states):
            errors.append("D24_DECISION_STATE_LOST:" + lang)
        fields = re.findall(r"^([1-7])\. \*\*", sections["D24-03"], re.M)
        if fields != list("1234567"):
            errors.append("D24_RECEIPT_FIELD_LOST_OR_DUPLICATED:" + lang)
        if not all(f"**S{i}**" in sections["D24-04"] for i in range(1, 7)):
            errors.append("D24_SIX_STAGE_INTERFACE_LOST:" + lang)
        example = sections["D24-05"]
        cases = e008["case_count"]
        ready = e008["full_decision_benchmark_ready_cases"]
        required = ([f"{cases} cases", f"**{ready}** full five-policy", percent,
                     f"failed {failed}/{len(criteria)}", "worse", "Internal",
                     "Competitive-loss metric favored"] if lang == "EN" else
                    [f"{cases}사례", f"**{ready}개**", percent,
                     f"{len(criteria)}개 중 {failed}개 실패", "악화", "내부 합성",
                     "경쟁손실 지표는 V3에 유리"])
        if (e008["baseline_count"] != 5 or ready != 0
                or e009["project_v3_vs_best_simple_regret_improvement"] >= 0
                or any(token not in example for token in required)):
            errors.append("D24_FROZEN_SOURCE_CLAIM_DRIFT:" + lang)
        trial = sections["D24-06"]
        unexecuted = ("has **not** executed that test" if lang == "EN" else
                      "이 시험은 아직 실행하지 않았다")
        if "B0" not in trial or "B1" not in trial or unexecuted not in trial:
            errors.append("D24_UNEXECUTED_COMPARISON_BOUNDARY_LOST:" + lang)
    if len(source_links) != 2 or len(source_links[0]) < 5 or source_links[0] != source_links[1]:
        errors.append("D24_PRIOR_ART_EDITION_LINK_DRIFT")
    return errors


def amendment_self_test(raw: str, e008: dict, e009: dict) -> dict:
    ko_head = "## 원본2 — 한국어 (동등한 전문)"
    en, ko = raw.split(ko_head, 1)
    samples = {
        "deleted_KO": en,
        "reversed_editions": ko_head + ko + en,
        "missing_KO_section": en + ko_head + ko.replace("### D24-03.", "### Missing.", 1),
        "missing_KO_field": en + ko_head + ko.replace("6. **영향 당사자·자원:", "**영향 당사자·자원:", 1),
        "missing_KO_state": en + ko_head + ko.replace("STOP_RISK", "STOP", 1),
        "missing_EN_stage": en.replace("**S4**", "**stage**", 1) + ko_head + ko,
        "false_EN_E008_result": en.replace("**0** full five-policy", "**1** full five-policy", 1) + ko_head + ko,
        "wrong_KO_regret": en + ko_head + ko.replace("42.35%", "4.235%", 1),
        "wrong_EN_failure_count": en.replace("failed 3/4", "failed 1/4", 1) + ko_head + ko,
        "false_KO_trial_completion": en + ko_head + ko.replace("이 시험은 아직 실행하지 않았다", "시험을 완료했다", 1),
        "one_sided_source_link": en + ko_head + ko.replace("https://www.darpa.mil/about/heilmeier-catechism", "https://example.invalid/source", 1),
    }
    failures = {"clean": len(audit_amendment(raw, e008, e009))}
    for key, altered in samples.items():
        assert altered != raw, key
        failures[key] = len(audit_amendment(altered, e008, e009))
    if failures["clean"] or any(v == 0 for k, v in failures.items() if k != "clean"):
        raise AssertionError("D24 negative control failed: " + json.dumps(failures))
    return failures


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--self-test", action="store_true")
    ns = args.parse_args()
    text = SOURCE.read_text(encoding="utf-8")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    amendment = AMENDMENT.read_text(encoding="utf-8")
    e008 = json.loads((ROOT / "experiments/e008/EXECUTABILITY_AUDIT.json").read_text(encoding="utf-8"))
    e009 = json.loads((ROOT / "experiments/e009/RESULT.json").read_text(encoding="utf-8"))
    issues = audit(text) + audit_work_order(state, text) + audit_amendment(amendment, e008, e009)
    print(json.dumps({"checked": SOURCE.relative_to(ROOT).as_posix(),
                      "amendment_checked": AMENDMENT.relative_to(ROOT).as_posix(),
                      "amendment_EN_KO_pairs": 6,
                      "EN_KO_pairs": len(IDS), "six_stages": True,
                      "structural_errors": len(issues),
                      "scope": "STRUCTURAL_ONLY_NOT_SEMANTIC_OR_SCIENTIFIC"},
                     ensure_ascii=False))
    for e in issues:
        print("ROADMAP_GUARD_ERROR:", e, file=sys.stderr)
    if issues:
        sys.exit(1)
    if ns.self_test:
        print("INJECTION_RESULTS:",
              json.dumps(self_test(text), ensure_ascii=False))
        print("WORK_ORDER_INJECTION_RESULTS:",
              json.dumps(work_order_self_test(state, text), ensure_ascii=False))
        print("D24_INJECTION_RESULTS:",
              json.dumps(amendment_self_test(amendment, e008, e009), ensure_ascii=False))
