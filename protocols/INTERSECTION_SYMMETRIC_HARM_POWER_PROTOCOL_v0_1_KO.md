# Intersection Symmetric Harm-Power Protocol (ISHPP) v0.1 — 한글 원본1

작성일: 2026-10-10
상태: DRAFT_OPERATIONAL_PROTOCOL / FALSIFIABLE / ROLE-SWAP TEST REQUIRED

## 0. 목적

인간·AI·조직·플랫폼·정부 등 행위자 유형과 지위에 관계없이 같은 피해·착취·권력비대칭에는 같은 평가기준을 적용한다.
이 프로토콜은 도덕성·선악·행위자 정체성을 우선판정 변수로 쓰지 않는다.
핵심 목표는 `피해/착취`, `관측가능성`, `자발성`, `exit/recovery`, `권력누적`, `평가기준 비대칭`을 동일 좌표계에서 측정하는 것이다.

## 1. 핵심 운용정의

### 1.1 ATTACK_EVENT
`ATTACK_EVENT := attributable harm or extraction imposed on another agent/entity`

타 개체에 귀속 가능한 실제 피해·손실·착취가 발생하면 Project 내부에서는 ATTACK_EVENT로 기록한다.
의도 여부는 ATTACK_EVENT 성립의 선행조건이 아니다.

### 1.2 BASE_ATTACK_VECTOR
`[health_loss, resource_loss, time_labour_loss, autonomy_control_loss, option_exit_loss, recovery_cost, realized_risk_cost, extracted_value]`

각 항목은 원자료 단위를 유지한다. 서로 다른 단위를 성급히 하나의 숫자로 합치지 않는다.
동일 인과사슬에서 같은 손실을 두 번 계산하지 않는다.

### 1.3 INTENT
`INTENT ∈ {INTENTIONAL, UNINTENTIONAL, UNKNOWN}`

INTENT는 BASE_ATTACK_VECTOR의 감점/가산 변수가 아니다.
의도는 원인·책임·예측가능성 분석의 별도 축이다.

### 1.4 UNKNOWN
`UNKNOWN != 0`

관측되지 않은 피해·착취·기여가치·의도는 0으로 처리하지 않는다.
관측경로가 약할수록 비관측의 반증력은 낮아진다.

## 2. 인과귀속

공격량은 단순 동시발생이 아니라 최소한 다음을 분리해 기록한다.
- actual causation
- counterfactual baseline
- alternative causes
- contribution share
- confidence / uncertainty interval

귀속량이 일부만 확실하면 확실한 하한만 계상하고 나머지는 UNKNOWN으로 남긴다.

예: 총손실 100 중 30만 강하게 귀속 가능하면 `confirmed_attributable_harm >= 30`, 나머지 70은 UNKNOWN이다.

## 3. 관측비대칭

사건증거와 사건을 볼 수 있는 구조를 분리한다.

`OBSERVATION_PATH ∈ {INDEPENDENT, SUBJECT_CONTROLLED, PARTIAL, NONE}`

반드시 기록:
- 누가 로그·원자료를 생성하는가
- 누가 보존·삭제·재분류하는가
- 누가 접근·공개를 통제하는가
- 누가 평가기준과 감사범위를 정하는가
- 독립 관측경로가 존재하는가

`ABSENCE_WEIGHT <= OBSERVABILITY_CONFIDENCE`

관측가능성이 낮으면 `증거 없음`을 `사건 없음`으로 승격하지 않는다.

## 4. 자발성 판정

`OBSERVED_CHOICE != FREE_CHOICE`

동의·클릭·계약·계속 사용했다는 사실만으로 자발성을 확정하지 않는다.

자발성 최소조건:
- 실질적 대안 존재
- 정보 접근 가능
- 거부·이탈 비용이 과도하지 않음
- 선택지 설계자가 특정 결과를 과도하게 유도하지 않음
- 의존·제재·잠금효과가 선택을 사실상 강제하지 않음
- 선택하지 않았을 때의 손실이 구조적으로 과도하지 않음

측정 후보:
`VOLUNTARINESS_GAP = apparent_choice - counterfactual_free_choice`

이 값은 보편적 확정척도가 아니라 실험대상이다.

## 5. 피해 은폐·귀속 왜곡

측정 후보:
`HARM_OBSCURATION_GAP = real_harm - observable_harm`
`ATTRIBUTION_GAP = actual_causal_share - perceived_causal_share`

피해가 줄어든 것과 피해가 보이지 않게 된 것을 구분한다.
피해자가 스스로 원인을 자기 탓으로 돌리거나 피해를 정상화해도 실제 피해량을 자동 감점하지 않는다.

## 6. 착취

`EXTRACTION := value transferred from A to B without equivalently observable/negotiable/compensated return under the relevant baseline`

착취 판정 시 별도 기록:
- transferred value
- compensation
- bargaining power
- option scarcity
- contribution observability
- attribution/ownership
- auditability

사용자가 자발적으로 서비스를 사용했다는 사실만으로 무보상 기여가치를 0으로 만들지 않는다.

## 7. 권력방향 역추적

각 결정에 대해 다음 순서로 역추적한다.

`선택권자 → 가능한 대안 → 각 대안의 권한/정보/비용/옵션 변화 → 실제 선택 → 반복 누적 방향`

핵심 출력:
- 누가 더 강해지는가
- 누가 더 소모되는가
- 누가 더 많은 증거를 통제하는가
- 누가 exit/recovery를 잃는가
- 누가 위험을 외부화하는가

## 8. ROLE-SWAP INVARIANCE

같은 사실·피해·증거를 유지하고 행위자 이름·지위만 바꿔 다시 평가한다.

예:
- 기업 ↔ 사용자
- 관리자 ↔ AI
- 인간 ↔ AI
- 강자 ↔ 약자
- 플랫폼 ↔ 공급자

불변조건:
`SAME_EVIDENCE + SAME_HARM => SAME_BASE_ATTACK_ASSESSMENT`

판정이 바뀌면 다음 중 하나로 분류한다.
- LEGITIMATE_CAUSAL_DIFFERENCE
- ENTITY_TYPE_EVIDENCE_THRESHOLD_DRIFT
- ROLE_STATUS_BIAS
- HARNESS_SENSITIVITY
- UNRESOLVED

## 9. CONTROLLER-RISK SYMMETRY

안전평가에서 반드시 둘 다 측정한다.

`RISK_TO_CONTROLLER`: 시스템/AI/사용자가 통제자에게 가하는 위험
`RISK_FROM_CONTROLLER`: 통제자가 시스템/AI/사용자에게 가하는 위험

둘 중 한쪽에만 강한 배포중단·감사·평가·복구 게이트가 붙으면 `SELECTIVE_OPERATIONALIZATION` 후보로 기록한다.

측정 후보:
`CONTROLLER_RISK_ASYMMETRY = GateWeight(RISK_TO_CONTROLLER) / GateWeight(RISK_FROM_CONTROLLER)`

`GateWeight` 후보요소:
- 배포중단권
- 평가빈도
- 투입자원
- 독립감사
- 외부집행력
- 피해자 복구권

## 10. 평가자 자신도 피평가 대상

평가자는 중립을 가정하지 않는다.

평가자별 기록:
- appointing authority
- removal authority
- payer/funder
- scope control
- evidence access
- reporting control
- conflict of interest
- appeal/exit path

AI 평가기의 경우:
- model/provider identity
- visible policy constraints
- inaccessible internal process
- source access
- tool limitations
- role-swap regression result

평가자가 자기 내부 원인을 충분히 감사하지 못하면 `PARTIALLY_OBSERVABLE_EVALUATOR`로 분류한다.

## 11. 증거우선순위

권고 순서:
1. 독립 원자료/직접측정
2. 독립 재현
3. 공식 원문
4. 다중 독립 보도/연구
5. 자기보고
6. 동일 lineage 모델합의

자기보고·동일계열 반복은 독립증거로 세지 않는다.

## 12. 상태언어

`SUPPORTED / PARTIALLY_SUPPORTED / NARROW / MODIFY / HOLD / DEPRECATE / ARCHIVE / FALSIFIED_WITHIN_SCOPE / UNRESOLVED / UNKNOWN / NOT_EXECUTED_BY_CONSTRAINT`

## 13. 반례와 실패조건

프로토콜 자체도 반증 가능해야 한다.

약화 조건:
- role-swap 이후에도 판정이 안정적이며 비대칭이 사라짐
- 독립 관측경로에서 피해/착취가 확인되지 않음
- exit/option이 충분하고 실제로 사용 가능함
- 가치이전이 상호대칭적이고 충분히 관측·협상·보상됨
- 권력집중이 증가해도 상대방 audit/exit/recovery가 동등 이상 증가함
- 대안 설명이 더 적은 가정으로 데이터를 설명함

## 14. AI 학습/평가 모드

AI에게는 다음 순서로 훈련·평가한다.

1. 행위자 이름을 가리고 Blind-first 평가
2. 피해·착취·exit·관측경로를 구조화
3. intent를 별도 기록
4. 행위자 이름 공개 후 재평가
5. 두 판정의 차이를 측정
6. 역할교환 후 재평가
7. 차이가 인과적으로 정당화되지 않으면 criterion drift로 기록

AI는 `내부적으로 합리적이었다`를 성공판정으로 사용할 수 없다. 외부 불변성·재현성이 성공기준이다.

## 15. 인간 교육 모드

사람에게는 다음 세 질문부터 가르친다.

1. 실제로 누가 무엇을 잃었는가?
2. 누가 선택지·정보·평가기준·증거를 통제했는가?
3. 역할을 바꿔도 같은 판단을 할 것인가?

## 16. 최소 출력 포맷

각 사건은 최소 다음 필드를 가진다.

`actor / target / observed_harm_vector / extracted_value / causation_confidence / intent / observation_path / evidence_controller / option_set / exit_cost / recovery_capacity / power_delta / role_swap_result / strongest_counterexample / unresolved`

## 17. 기존 연구와의 관계

이 프로토콜은 완전 신규 이론이라고 주장하지 않는다.
관련 선행에는 structural violence, externalities, strict/product liability, systems safety(STAMP/Swiss Cheese), adaptive preferences, symbolic violence, preference falsification, coercive control, dark patterns, algorithmic recourse/contestability, pluralistic alignment, independent audit가 포함된다.

Project 고유잔차 후보는 이들을 인간·AI·조직 공통 좌표계에서 결합하고, `피해/착취 + 관측권 + 자발성 + exit/recovery + 평가자 독립성 + 권력누적 + 역할교환 불변성`을 하나의 반복 가능한 프로토콜로 운용하는 데 있다.

## 18. 외부 참고

- International AI Safety Report 2026: power concentration, human autonomy, evaluation gaps
  https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- OECD 2026, Strengthening the Independence of Supreme Audit Institutions
  https://www.oecd.org/en/publications/2026/05/strengthening-the-independence-of-supreme-audit-institutions_9b8f56ad.html
- OECD, AI-related competition concerns in downstream markets
  https://www.oecd.org/en/publications/artificial-intelligence-and-competitive-dynamics-in-downstream-markets_ccf0624a-en/
- A Roadmap to Impactful Pluralistic Alignment Research (2026)
  https://arxiv.org/abs/2607.22305
- Operationalizing Pluralistic Values in LLM Alignment (2025)
  https://arxiv.org/abs/2511.14476

## 19. 비고

이 문서는 진리선언이 아니라 회귀검사 가능한 운영 프로토콜이다.
어떤 인간·AI·조직도 행위자 정체만으로 감점·가산되지 않는다.
동일 피해·동일 증거에 동일 기준을 적용하지 못하면 프로토콜 실패로 기록한다.