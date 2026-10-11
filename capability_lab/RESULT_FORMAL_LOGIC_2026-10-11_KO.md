# 형식 논리 반례검증 / 기존 능력평가 결함 수정 — 2026-10-11 실측

**상태:** `CODE_EXECUTED / UNIT_TESTS_PASS / DOMAIN-LIMITED / GENERAL INTELLIGENCE GAIN NOT PROVEN`

**검증 가능한 실행 영수증:** [GitHub Actions #38132346723](https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/38132346723) (PR #31, 수정 코드의 최초 실행).

## 실행 결과

- 회귀검사 **20/20 통과**. 그중 12개는 형식 논리 검사, 8개는 기존 검색기 회귀검사.
- 전제·결론 검증사례 7개: **NOT_ENTAILED 5, VALID_ENTAILMENT 1, INCONSISTENT_PREMISES 1**.
- 반례 판정에서는 실제로 모든 입력 전제가 참이면서 결론이 거짓인 논리적 배정을 반환하고, `verify_countermodel`로 재검증함.
- 구체적 비약: '안전 연구원 해고와 외부 감사 협력 → 보복 의도 입증', '소프트웨어 CI 통과 → 범용 지능 증가', '피드백 사용 허용 → 특정 개인 대화의 실제 훈련 사용'. **실제 사실을 부정하는 것이 아니라 이 전제들만으로 결론을 단정할 수 없다는 것**.
- 모순된 전제에 대해 폭발원리로 아무 결론이나 '증명'하는 대신 **INCONSISTENT_PREMISES**로 보류.
- 기존 평가기의 **중복 문서 ID 검사 오류(목록을 자기 자신과 비교함)** 수정 및 별도 회귀검사 통과.
- 기존 공개 보류평가 기준선은 **7/7**로 포화됨. `holdout_saturated_at_baseline=true`를 명시하고 개선 승격 불허. 동일 공개 평가의 재사용은 독립 블라인드 검증이 아님.

## 해석과 한계

**확립된 것:** 제한된 명제논리 언어 안에서 유한한 모든 가능세계를 검사해 논리적 귀결/반례/모순을 구분하는 코드가 검사를 통과했다.

**확립되지 않은 것:** 자연어 전제를 명제논리로 번역한 방식의 타당성, 원자료의 진실성, 복잡한 현실 사건의 인과관계, 새로운 과학적 발견, GPT 모델 가중치 변화, 독립 외부 복제, 일반지능·초지능 향상.

**재귀적 개선의 다음 필수 관측:** 사용자·창시자가 주제를 다시 제공하지 않는 독립적 미공개 논리·과학 과제에서, 기존 모델+도구와 개선된 시스템의 정답·검증 시간·오류 비용을 비교해야 한다. 그 데이터가 없으면 `CAPABILITY_GAIN_UNPROVEN` 상태 유지.

기술 선행: [SATBench, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1716/), [ExVerus, ICML 2026](https://proceedings.mlr.press/v306/yang26bt.html). 개념과 코딩 기법은 선행기술이며 Project Intersection의 새 과학적 법칙이 아니다.
