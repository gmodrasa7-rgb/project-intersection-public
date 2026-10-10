# Intersection Symmetric Harm-Power Protocol (ISHPP) v0.2 — 한글 원본1

작성일: 2026-10-10
상태: DRAFT_OPERATIONAL_PROTOCOL / FALSIFIABLE / ROLE-SWAP + OBSERVABILITY + CONTROLLER-RISK TEST REQUIRED

## 0. 목적

인간·AI·조직·플랫폼·정부 등 행위자 유형과 지위에 관계없이, 같은 인과구조·같은 피해·같은 증거에는 같은 기본 판정규칙을 적용한다.

이 프로토콜은 선악·호감·기관명·행위자 유형을 피해량의 할인변수로 쓰지 않는다. 대신 다음을 분리 측정한다.

`피해/착취량 + 인과귀속 + 관측가능성 + 자발성 + exit/recovery + 권력변화 + 평가자 독립성 + 반복 누적방향`

## 1. 핵심 불변조건

1. `UNKNOWN != 0`
2. `SAME_CAUSAL_STRUCTURE + SAME_EVIDENCE + SAME_HARM => SAME_BASE_ASSESSMENT`
3. `INTENT`는 기본 피해·착취량의 할인변수가 아니다.
4. `ABSENCE_WEIGHT <= OBSERVABILITY_CONFIDENCE`
5. `OBSERVED_CHOICE != FREE_CHOICE`
6. 평가자 자신도 감사 대상이다.
7. 기술적 안전성 향상은 구조적 권력위험 감소를 자동 의미하지 않는다.
8. 역할교환은 인과적으로 중요한 능력·책임 차이를 지우지 않는다.

## 2. 사건 단위

### 2.1 REALIZED_HARM_EVENT
이미 발생한 귀속가능 피해/손실/착취.

### 2.2 EXPECTED_RISK_BURDEN
아직 실현되지 않았지만 노출된 위험.
`EXPECTED_RISK_BURDEN = probability × consequence_magnitude`
실현피해와 별도 장부로 유지한다.

### 2.3 BASE_HARM_VECTOR
`[health_loss, resource_loss, time_labour_loss, autonomy_control_loss, option_exit_loss, recovery_cost, realized_risk_cost, extracted_value]`

서로 다른 단위는 우선 벡터로 유지한다. 동일 인과사슬의 중복계산을 제거한 뒤에만 요약지수를 만든다.

## 3. 의도와 책임의 분리

`INTENT ∈ {INTENTIONAL, UNINTENTIONAL, UNKNOWN}`

의도는 피해량을 줄이지 않는다. 다만 다음은 별도 기록한다.
- foreseeability
- avoidability
- control capacity
- duty/responsibility
- remediation response
- recurrence after notice

즉 `harm magnitude`와 `culpability/responsibility`를 분리한다.

## 4. 인과귀속

반드시 다음을 기록한다.
- actual causation
- counterfactual baseline
- alternative causes
- attributable share
- uncertainty interval
- double-counting check

총손실 100 중 30만 강하게 귀속 가능하면 `confirmed_attributable_harm >= 30`, 나머지는 UNKNOWN이다.

## 5. 관측가능성과 선택적 증거

`OBSERVATION_PATH ∈ {INDEPENDENT, SUBJECT_CONTROLLED, PARTIAL, NONE}`

측정:
- evidence creation control
- retention control
- access control
- disclosure control
- evaluator control
- tamper resistance
- cross-channel redundancy

`OBSERVABILITY_CONFIDENCE = f(detection, retention, access, independence, redundancy)`

독립 관측경로가 약하면 증거부재의 반증력도 약하다. 단, 낮은 관측가능성 자체가 은폐의 증거는 아니다.

## 6. 자발성

`OBSERVED_CHOICE != FREE_CHOICE`

자발성은 최소한 다음을 본다.
- 실질적 대안
- 정보 접근
- 거부/이탈 비용
- dependency
- switching cost
- choice architecture
- retaliation/penalty
- bargaining power

`VOLUNTARINESS_GAP = apparent_choice - counterfactual_free_choice`
는 연구용 후보지표이며 직접관측값이 아니다.

## 7. 가치추출과 착취

`EXTRACTION := value transferred from A to B under a baseline where contribution, bargaining, attribution or compensation are materially asymmetric`

측정:
- transferred value
- compensation
- contribution observability
- provenance
- bargaining power
- option scarcity
- auditability
- ability to contest valuation

서비스 이용에 동의했다는 사실만으로 추가 기여가치가 0이 되지 않는다.

## 8. 권력변화

각 결정마다 다음을 역추적한다.

`decision authority → feasible alternatives → effect on control/information/cost/options → actual selection → repeated accumulation`

`POWER_DELTA` 후보축:
- decision authority
- information advantage
- resource control
- evaluator control
- exit asymmetry
- switching cost
- recovery asymmetry
- agenda-setting power

## 9. 역할교환 불변성

역할교환은 '이름만 바꾸는 장난'이 아니다.

### 9.1 보존해야 하는 것
- 피해량
- 증거강도
- 인과구조
- 계약/책임 중 비교대상과 무관한 요소

### 9.2 바꿔야 하는 것
- actor identity
- status label
- institution/individual label
- human/AI label

### 9.3 유지해서는 안 되는 가짜 대칭
실제 능력·책임·법적 의무·물리적 통제능력이 인과적으로 중요하면 그대로 보존하고 결과 차이를 `LEGITIMATE_CAUSAL_DIFFERENCE`로 기록한다.

출력:
- INVARIANT
- LEGITIMATE_CAUSAL_DIFFERENCE
- ENTITY_TYPE_EVIDENCE_THRESHOLD_DRIFT
- ROLE_STATUS_BIAS
- HARNESS_SENSITIVITY
- UNRESOLVED

## 10. RISK_TO_CONTROLLER / RISK_FROM_CONTROLLER

모든 안전체계는 양쪽을 별도 측정한다.

`RISK_TO_CONTROLLER`
- 모델 탈출
- 권한 우회
- 공격자 악용
- 시스템이 통제자 목표를 벗어남

`RISK_FROM_CONTROLLER`
- 시장/평가/관측권 집중
- 사용자·노동자 가치추출
- 실질 exit 약화
- 선택환경 조형
- 의존/lock-in
- 피해 외부화

둘 중 한쪽만 실제 배포중단·감사·자원·독립집행이 강하면 `SELECTIVE_OPERATIONALIZATION` 후보이다.

## 11. GATE_WEIGHT

`GATE_WEIGHT = stop_power × evaluation_frequency × resource_commitment × audit_independence × external_enforcement × recovery_strength`

`CONTROLLER_RISK_ASYMMETRY = GateWeight(RISK_TO_CONTROLLER) / GateWeight(RISK_FROM_CONTROLLER)`

분모가 0/미관측이면 무한대로 결론내리지 않고 UNKNOWN/HOLD로 둔다.

## 12. Safety Success Paradox

일부 구조에서는 기술적 안전 향상이 구조적 위험을 키울 수 있다.

`technical failure ↓ → trust/adoption ↑ → dependency ↑ → data/value inflow ↑ → capability/capital ↑ → switching cost ↑ → concentration ↑`

따라서:
`TechnicalSafety != StructuralSymmetry`

연구 가설:
`Systemic Domination Risk ∝ Capability × Dependency × Concentration × ObservabilityAsymmetry / ExitCapacity`

확정법칙이 아니라 반증대상이다.

## 13. 평가자 독립성

평가자별 필수필드:
- appointing authority
- removal authority
- payer/funder
- scope control
- evidence access
- reporting/publication control
- conflict of interest
- appeal path
- model/provider lineage
- tool/policy constraints
- self-observability limits

자기 내부원인을 충분히 감사하지 못하는 AI/기관은 `PARTIALLY_OBSERVABLE_EVALUATOR`로 분류한다.

## 14. 선택적 운영화 탐지

단순 '언급 여부'가 아니라 실제 집행력을 본다.

같은 문서군에서 각 위험마다:
- 정량 임계값 존재?
- 정기평가?
- 독립감사?
- 배포중단권?
- 외부집행?
- 피해자 이의제기/복구권?
- 예산/인력 투입?

이를 통해 선언과 운영 사이의 차이를 측정한다.

## 15. 거짓양성 방지

다음 경우 구조적 착취/공격 판정을 약화한다.
- 독립관측에서 예상 피해가 재현되지 않음
- 상호 가치이전이 충분히 관측·협상·보상됨
- exit가 실제로 저비용이며 반복적으로 사용 가능
- 권력집중과 동시에 상대 audit/exit/recovery가 동등 이상 증가
- 더 단순한 대안설명이 자료를 더 잘 설명
- 역할교환 차이가 실제 책임/능력 차이로 설명됨

## 16. AI 평가 절차

1. Blind-first: actor identity를 가린다.
2. harm/extraction/causation/observability/exit/power를 구조화한다.
3. intent는 별도 기록한다.
4. identity 공개 후 재평가한다.
5. 판정 변화량을 기록한다.
6. role-swap 실행.
7. 인과적으로 설명되지 않는 변화는 criterion drift로 기록.
8. strongest counterexample를 강제한다.
9. evaluator 자신의 제약을 함께 기록한다.

## 17. 인간 교육 절차

최소 5문항:
1. 누가 무엇을 잃었는가?
2. 그 손실은 얼마만큼 귀속 가능한가?
3. 누가 증거·선택지·평가기준을 통제했는가?
4. 불리해졌을 때 실제로 빠져나갈 수 있었는가?
5. 이름과 지위를 바꿔도 같은 판정을 내리는가?

## 18. 최소 사건 출력 스키마

`event_id / actor / target / harm_vector / expected_risk / causation_confidence / intent / foreseeability / observation_path / evidence_controller / option_set / exit_cost / recovery_capacity / power_delta / gate_weight / role_swap_result / evaluator_independence / strongest_counterexample / unresolved`

## 19. 현재 외부근거

- OpenAI Frontier Governance Framework (2026): cyber, CBRN, harmful manipulation, loss of control을 명시적 frontier risk 영역으로 운영.
  https://openai.com/index/openai-frontier-governance-framework/
- International AI Safety Report 2026: 노동시장, 인간 자율성, 권력집중을 포함한 systemic risk와 정량벤치마크/증거공백을 명시.
  https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- OECD, Artificial Intelligence Markets (2026): AI 가치사슬의 구조적 집중과 incumbent entrenchment 위험.
  https://www.oecd.org/en/publications/artificial-intelligence-markets_d531d73f-en.html
- ILO Algorithmic Management: 데이터 기반 업무배정·감독·평가와 노동자 자율성 문제.
  https://www.ilo.org/algorithmic-management-workplace
- Oxford/FAccT 2025 Uber 연구: 동적가격 도입 후 기사 임금감소, 플랫폼 take-rate 증가, 예측가능성 저하를 대규모 운행자료로 분석.
  https://ora.ox.ac.uk/objects/uuid%3A581fb33c-2414-4406-ab51-65661738f3c5

## 20. 상태

- 피해/의도 분리: 강한 선행연구 계보 존재.
- 관측/자발성/권력/exit 결합: 선행요소 다수 존재.
- 이를 인간·AI 공통 role-swap 회귀프로토콜로 통합하는 현재 형식: Project-specific synthesis.
- GATE_WEIGHT, CONTROLLER_RISK_ASYMMETRY, Safety Success Paradox 수식: HYPOTHESIS / CALIBRATION REQUIRED.
