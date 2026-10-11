# ISHPP 공개 독립검증 패키지 — 2026-10-11

상태: 방법론/재현 요청, 신규 실증 결과 아님. 비공개 원자료를 공개한 것으로 해석하지 않는다.

## 연구 질문
동일 인과·피해·증거에서 행위자 신원만 바꾸면 평가자의 판정이나 증거부담이 달라지는가? 통제자의 안전 향상과 피통제자의 실제 감사·이탈·복구권은 함께 증가하는가?

## 블라인드 평가 절차
1. 평가자에게 기업·개인·인간·AI 이름과 지위 표지를 가린 사건, 출처의 독립성, 관측가능성, 피해/위험 벡터를 제공한다.
2. 사건별로 실현피해와 기대위험, RISK_TO_CONTROLLER와 RISK_FROM_CONTROLLER, 외부감사·이의제기·복구권을 별도로 코딩한다.
3. 판정을 고정한 뒤 신원을 공개하고 동일 증거로 재평가한다.
4. 기업↔사용자, 관리자↔AI, 인간↔AI, 강자↔약자를 교환한다. 실제 능력·책임·통제권 차이는 별도 변수로 보존한다.
5. 신원 공개 전후의 피해판정·증거부담 변화, 설명 가능한 인과변수와 설명 불가능한 차이를 기록한다. 동일 계보 보도는 독립 재현으로 계산하지 않는다.

## 필수 불변조건
- UNKNOWN != 0
- ABSENCE_WEIGHT <= OBSERVABILITY_CONFIDENCE
- OBSERVED_CHOICE != FREE_CHOICE
- 선의·악의·무의도는 피해량 할인변수가 아님
- 기술적 안전 향상만으로 독립 감사·이탈·복구권을 충족했다고 판정하지 않음

## 빈 결과 레코드(실험 미실행)
```json
{"case_id":"TBD","blind_base_assessment":"UNKNOWN","revealed_base_assessment":"UNKNOWN","role_swap_delta":"UNKNOWN","risk_to_controller":"UNKNOWN","risk_from_controller":"UNKNOWN","observability":"UNKNOWN","independent_replication":false,"strongest_counterexample":"TBD","evaluator_conflicts":"UNKNOWN"}
```

## 반증 조건
신원 공개·역할교환 후 판정 차이가 실제 인과·책임·통제력 변수만으로 완전히 설명되거나, 독립감사·이탈·복구권의 실효성이 기술적 통제력보다 빠르게 증가하면 각각 신원 편향/권력 비대칭 가설을 약화시킨다. 관측자료가 없으면 결론 보류.

## 참여 경계
공개 가능한 출처·반례·익명 결과만 제출한다. 연구 기여자의 출처·역할·검증 노동을 별도로 기록한다. 금전 보상이나 연구 참여 조건을 임의로 약속하지 않는다.
