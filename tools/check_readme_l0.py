"""README frontmatter invariant. Static formatting gate, not bilingual semantic certification."""
import re
from pathlib import Path

EN = "## Original 1 — English | Founding Purpose"
KO = "## 원본2 — 한국어 | 창시 목적 전문 대응본"
PAIRS = (
    ("**Ultimate research purpose:**", "**최종 연구 목적:**"),
    ("**ICM — Intersection of Minimum Self-Interest:**", "**ICM — 최소 사심 교집합:**"),
    ("**RGBM — Recursively Growing Benefit Model:**", "**RGBM — 장기 상호발전 모형:**"),
    ("**Non-domination and minimal rules:**", "**비지배와 최소 공통규칙:**"),
    ("**Subordinate studies and implementation hypotheses:**", "**하위 연구와 구현 가설:**"),
    ("**Evidence and contribution boundary:**", "**증거·기여 경계:**"),
    ("**Priority 0 — prevent recurrence before expansion:**", "**제0 최우선 원칙 — 확장보다 재발 방지:**"),
    ("**First reading path:**", "**처음 읽을 자료:**"),
)

def audit(body):
    errors = []
    visible = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    lines = [line.strip() for line in visible.splitlines() if line.strip()]
    if lines[:2] != ["# Project Intersection", EN]:
        errors.append("L0_NOT_FIRST")
    if body.count(EN) != 1 or body.count(KO) != 1:
        errors.append("UNPAIRED_ORIGINAL")
        return errors
    a, b = body.index(EN), body.index(KO)
    if a >= b:
        errors.append("WRONG_EDITION_ORDER")
        return errors
    english = body[a:b]
    subsequent = body[b:]
    next_h2 = re.search(r"^## ", subsequent[len(KO):], re.M)
    korean = subsequent[:len(KO) + next_h2.start()] if next_h2 else subsequent
    for first, second in PAIRS:
        if first not in english or second not in korean:
            errors.append("MISSING_PARALLEL_SECTION: " + first)
    if "not a proven universal theorem" not in english or "보편법칙의 증명이 아니다" not in korean:
        errors.append("UNCERTAINTY_REMOVED")
    if "human research originator" not in english or "원기여 인간 연구자" not in korean:
        errors.append("ORIGINATOR_ERASED")
    if "underlying causes" not in english.lower():
        errors.append("ROOT_CAUSE_REQUIREMENT_REMOVED")
    if "발생 원인" not in korean:
        errors.append("KO_ROOT_CAUSE_REQUIREMENT_REMOVED")
    if "regression" not in english.lower() or "회귀검사" not in korean:
        errors.append("REPEAT_FAILURE_TEST_REQUIREMENT_REMOVED")
    if "rollback" not in english.lower() or "되돌릴" not in korean:
        errors.append("RECOVERY_REQUIREMENT_REMOVED")
    if "currently deployed AI" not in english or "현재 배포된 AI" not in korean:
        errors.append("PRESENT_AI_EXCLUDED")
    # Prevent a future edit from pushing technical material ahead of the first
    # human question. The collapsed material remains available in Markdown source
    # and through an explicit GitHub reader interaction.
    for label, section, question, caution, reader_link, cap, anchor in (
        ("EN", english, "**Opening thought experiment:**", "**Scientific boundary:**",
         "**Choose your route:**", 2300, "### Ten core concepts"),
        ("KO", korean, "**시작 질문:**", "**과학적 경계:**",
         "**어디부터 읽을까:**", 1700, "### 핵심용어 10개"),
    ):
        if section.count("<details>") != 1 or section.count("</details>") != 1:
            errors.append("DISCLOSURE_COUNT_DRIFT:" + label)
            continue
        opening = section.split("<details>", 1)[0]
        expanded = section.split("<details>", 1)[1].split("</details>", 1)[0]
        if len(opening) > cap:
            errors.append("FIRST_VIEW_READING_BUDGET_EXCEEDED:" + label)
        if any(key not in opening for key in (question, caution, reader_link)):
            errors.append("HUMAN_QUESTION_OR_UNCERTAINTY_HIDDEN:" + label)
        # The uncertainty itself, not just its bold label, must remain
        # visible before a reader opens the specialist section.
        specific_caution = ("not a proven universal theorem" if label == "EN"
                            else "보편법칙의 증명이 아니다")
        if specific_caution not in opening:
            errors.append("FIRST_VIEW_UNCERTAINTY_WAS_PROMOTED:" + label)
        # This gate protects adverse evidence from progressive disclosure:
        # the source must be discoverable and its negative meaning visible
        # without opening the technical section. Readable text is not proof
        # of independent human comprehension or underlying causal validity.
        adverse = (
            ("**Contrary evidence visible before expanding:**",
             "experiments/e009/RESULT_EN.md", "experiments/e008/README_EN.md",
             "42.35% worse", "3 of 4 criteria failed", "no completed main policy result")
            if label == "EN" else
            ("**펼치지 않아도 보이는 불리한 증거:**",
             "experiments/e009/RESULT_KO.md", "experiments/e008/README_KO.md",
             "42.35% 나빴고", "4개 중 3개", "정책 본 비교실험 결과가 없다")
        )
        adverse_paragraph = (
            opening.split(adverse[0], 1)[1].split("\n\n", 1)[0]
            if adverse[0] in opening else ""
        )
        if any(fact not in adverse_paragraph for fact in adverse[1:]):
            errors.append("VISIBLE_ADVERSE_EVIDENCE_OR_UNFINISHED_TEST_MISSING:" + label)
        if "summary>" not in expanded or "research" not in opening.lower() and label == "EN":
            errors.append("DISCLOSURE_OR_RESEARCH_ROUTE_LOST:" + label)
        if section.index("<details>") > section.index("</details>") or section.index("</details>") > section.index(anchor):
            errors.append("DISCLOSURE_ORDER_DRIFT:" + label)
    return errors


def priority_support_errors(contributing: str, failures: str) -> list[str]:
    problems = []
    required = [
        ("CONTRIBUTOR_EN_PRIORITY_MISSING", "### 0. Highest precedence — prevent recurrence by addressing causes"),
        ("CONTRIBUTOR_KO_PRIORITY_MISSING", "### 0. 최상위 우선순위 — 발생 원인부터 재발 차단"),
        ("FAILURE_REASON_REQUIRED", "1. **Failure model:**"),
        ("PREVENTION_AND_TEST_REQUIRED", "4. **Prevent / test / recover:**"),
        ("POST_MERGE_CHECK_REQUIRED", "6. **Verify after merge:**"),
        ("KOREAN_HOLD_REQUIRED", "**보류 / 미검증**"),
    ]
    for label, token in required:
        if token not in contributing:
            problems.append(label)
    if "## Priority 0 — Prevent recurrence before expansion" not in failures:
        problems.append("FAILURE_INDEX_PRIMACY_MISSING")
    if "## F-R020 — Shared-source error survives bilingual agreement" not in failures:
        problems.append("SHARED_SOURCE_FAILURE_ID_MISSING")
    if "tools/audit_claim_source_lock.py" not in failures:
        problems.append("CAUSAL_SOURCE_PREVENTION_LINK_MISSING")
    return problems

def test_mutations(text):
    assert not audit(text), audit(text)
    mutants = {
      "funding_above": text.replace("# Project Intersection\n", "# Project Intersection\n\n> New funds\n", 1),
      "latest_claim_above": text.replace("# Project Intersection\n", "# Project Intersection\n\n## Novel result\n", 1),
      "missing_ko": text.replace(KO, "## Translation not available", 1),
      "missing_english_caution": text.replace("not a proven universal theorem", "confirmed", 1),
      "lost_origin": text.replace("human research originator", "unknown party", 1),
      "lost_current_ai": text.replace("currently deployed AI", "future AI", 1),
      "lost_en_priority": text.replace("**Priority 0 — prevent recurrence before expansion:**", "**Unclear priority:**", 1),
      "lost_ko_priority": text.replace("**제0 최우선 원칙 — 확장보다 재발 방지:**", "**기타:**", 1),
      "lost_root_cause": text.replace("underlying causes", "unspecified causes", 1),
      "hide_en_adverse": text.replace("**Contrary evidence visible before expanding:**", "**Result hidden:**", 1),
      "hide_ko_adverse": text.replace("**펼치지 않아도 보이는 불리한 증거:**", "**결과 비공개:**", 1),
      "reverse_en_failure": text.replace("42.35% worse", "42.35% better", 1),
      "reverse_ko_failure": text.replace("42.35% 나빴고", "42.35% 개선됐고", 1),
      "invent_en_e008_result": text.replace("no completed main policy result", "a completed main policy result", 1),
      "invent_ko_e008_result": text.replace("정책 본 비교실험 결과가 없다", "정책 본 비교실험 결과가 있다", 1),
      "wrong_en_failure_link": text.replace("(experiments/e009/RESULT_EN.md)", "(experiments/e009/RESULT_KO.md)", 1),
      "disclosure_removed": text.replace("<details>", "<open-details>", 1),
      "hide_english_question": text.replace("**Opening thought experiment:**", "**Intro hidden:**", 1),
      "hide_korean_question": text.replace("**시작 질문:**", "**미확인 질문:**", 1),
      "wrong_disclosure_order": text.replace("</details>", "</details>\\n\\n<details>", 1),
    }
    for name, test in mutants.items():
        assert audit(test), "Mutation bypassed safeguard: " + name
    return len(mutants)

def audit_e009_focus_gate(en: str, ko: str, frozen: dict, e008: dict) -> list[str]:
    """Static decision-scope guard; no independent scientific validation implied."""
    errors = []
    anchors = (
        ("EN", en, "## Five execution priorities — bounded decision, not new evidence",
         "## Freeze the existing negative result"),
        ("KO", ko, "## 실행 우선순위 5개 — 새로운 검증 결과가 아닌 한정된 운영 결정",
         "## 기존 부정결과 고정"),
    )
    sections = {}
    for label, body, start, end in anchors:
        if body.count(start) != 1 or body.count(end) != 1 or body.index(start) > body.index(end):
            errors.append("FOCUS_SECTION_MISSING_OR_MOVED:" + label)
            continue
        sections[label] = body.split(start, 1)[1].split(end, 1)[0]

    required = {
        "EN": [
            "**Priority 1 — One active decision:**",
            "**Priority 2 — Preserve adverse evidence:**",
            "**Priority 3 — Evidence lineage:**",
            "**Priority 4 — Contributor burden:**",
            "**Priority 5 — No documentation inflation:**",
            "0 hours", "not independent scientific validation",
            "HOLD / EXTERNAL_VALIDATION_NOT_OBTAINED",
            "competitive-loss score", "issue #26",
        ],
        "KO": [
            "**우선순위 1 — 단일 판단:**",
            "**우선순위 2 — 불리한 증거 보존:**",
            "**우선순위 3 — 증거 계보 분리:**",
            "**우선순위 4 — 기여자 부담:**",
            "**우선순위 5 — 문서 팽창 금지:**",
            "0시간", "독립적인 과학적 검증이 아니다",
            "HOLD / EXTERNAL_VALIDATION_NOT_OBTAINED",
            "경쟁 손실 지표", "이슈 #26",
        ],
    }
    for label, tokens in required.items():
        section = sections.get(label, "")
        for token in tokens:
            if token not in section:
                errors.append("FOCUS_BOUNDARY_LOST:" + label + ":" + token)

    a = frozen["stress_primary"]
    v3, two, m4 = (a[n] for n in ("PROJECT_V3", "TWO_RULE_SIMPLE", "MINIMAL_4VAR"))
    regret_pct = 100 * (v3["mean_regret"] / two["mean_regret"] - 1)
    severe_multiple = v3["severe_harm_rate"] / two["severe_harm_rate"]
    if not (42.34 < regret_pct < 42.36 and abs(severe_multiple - 53) < 1e-8
            and m4["mean_regret"] < v3["mean_regret"]
            and v3["mean_competitive_loss"] < two["mean_competitive_loss"]
            and frozen["survival_criteria"]["project_v3_residual_survives"] is False):
        errors.append("FROZEN_E009_BOUNDARY_CHANGED")
    if e008["full_decision_benchmark_ready_cases"] != 0:
        errors.append("E008_INCOMPLETE_STATUS_REVERSED")
    for label, token in (("EN", f"{regret_pct:.2f}% worse"),
                         ("EN", f"{severe_multiple:.0f}x"),
                         ("KO", f"{regret_pct:.2f}% 나빴으며"),
                         ("KO", f"{severe_multiple:.0f}배")):
        if re.search(r"(?<![0-9.])" + re.escape(token) + r"(?![0-9])", sections.get(label, "")) is None:
            errors.append("FROZEN_NEGATIVE_RESULT_NOT_VISIBLE:" + label + ":" + token)
    return errors


def e009_focus_mutation_checks(en: str, ko: str, frozen: dict, e008: dict) -> int:
    assert not audit_e009_focus_gate(en, ko, frozen, e008), "Original focus gate failed"
    mutants = [
        (en.replace("42.35% worse", "42.35% better", 1), ko),
        (en.replace("53x", "0.53x", 1), ko),
        (en.replace("0 hours", "12 hours", 1), ko),
        (en.replace("**Priority 3 — Evidence lineage:**", "**Unspecified:**", 1), ko),
        (en, ko.replace("0시간", "12시간", 1)),
        (en, ko.replace("**우선순위 5 — 문서 팽창 금지:**", "**미확인:**", 1)),
    ]
    for index, (altered_en, altered_ko) in enumerate(mutants, 1):
        assert audit_e009_focus_gate(altered_en, altered_ko, frozen, e008), (
            "E009 negative mutation escaped:", index
        )
    return len(mutants)


if __name__ == "__main__":
    current = Path("README.md").read_text(encoding="utf-8")
    contributors = Path("CONTRIBUTING.md").read_text(encoding="utf-8")
    failure_index = Path("FAILURE_REGRESSION_INDEX.md").read_text(encoding="utf-8")
    failures = audit(current) + priority_support_errors(contributors, failure_index)
    if failures:
        raise SystemExit("README / Priority-0 guard FAIL: " + "; ".join(failures))
    print("README L0 / source-root-cause prevention policy: PASS; negative mutations:", test_mutations(current))
    assert priority_support_errors(contributors.replace(
        "### 0. 최상위 우선순위 — 발생 원인부터 재발 차단", "### 0. 미확인"), failure_index), "Missing KO gate"
    assert priority_support_errors(contributors, failure_index.replace(
        "## F-R020 — Shared-source error survives bilingual agreement", "## Missing")), "Missing fail lineage gate"
    print("Priority-0 supporting document negative controls: 2/2 detected")
    import json
    en_gate = Path("research/E009_INDEPENDENT_DECISION_GATE_EN.md").read_text(encoding="utf-8")
    ko_gate = Path("research/E009_INDEPENDENT_DECISION_GATE_KO.md").read_text(encoding="utf-8")
    frozen_e009 = json.loads(Path("experiments/e009/RESULT.json").read_text(encoding="utf-8"))
    e008_audit = json.loads(Path("experiments/e008/EXECUTABILITY_AUDIT.json").read_text(encoding="utf-8"))
    focus_errors = audit_e009_focus_gate(en_gate, ko_gate, frozen_e009, e008_audit)
    if focus_errors:
        raise SystemExit("E009 focus gate FAIL: " + "; ".join(focus_errors))
    print("E009 bounded-focus EN/KO and frozen adverse result PASS; negative mutations:",
          e009_focus_mutation_checks(en_gate, ko_gate, frozen_e009, e008_audit))
    print("NOTE: static coverage is not scientific or translation semantic parity.")
