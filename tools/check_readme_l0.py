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
      "disclosure_removed": text.replace("<details>", "<open-details>", 1),
      "hide_english_question": text.replace("**Opening thought experiment:**", "**Intro hidden:**", 1),
      "hide_korean_question": text.replace("**시작 질문:**", "**미확인 질문:**", 1),
      "wrong_disclosure_order": text.replace("</details>", "</details>\\n\\n<details>", 1),
    }
    for name, test in mutants.items():
        assert audit(test), "Mutation bypassed safeguard: " + name
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
    print("NOTE: static coverage is not scientific or translation semantic parity.")
