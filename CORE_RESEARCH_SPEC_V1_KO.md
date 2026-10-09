# Project Intersection — 핵심 연구 명세 v1

Status: CORE SPEC CANDIDATE / NOT EMPIRICAL VALIDATION

## 0. 연구 질문

Project Intersection의 핵심 질문은 다음이다.

> 어떤 시스템이 국소적 성과를 최적화하면서 대안·비교·복구·practical exit·독립검증을 점진적으로 제거할 때, 자신이 만든 닫힌계 안에서 점점 더 성공해 보이면서 실제로는 비대칭·비용전가·착취·지배·옵션소멸 방향으로 수렴할 수 있는가?

그리고:

> 그 수렴을 악의·선의·도덕성 판단에 의존하지 않고 관측변수·시간축·인과·반사실·대체모형으로 얼마나 조기에 탐지할 수 있는가?

이 문서는 이 두 질문을 위한 최소 실행 명세다.

---

## 1. 기본 원칙

1. 의도는 구조판정의 필수입력이 아니다.
2. 관측되지 않은 것은 0이나 부재로 처리하지 않는다.
3. 현재 경로의 성과는 제거된 대안보다의 우월성을 증명하지 않는다.
4. 선행연구·표준·컨센서스·기관권위는 정답이 아니라 검증대상 evidence lineage다.
5. Project 가설도 기본승자가 아니다.
6. 결론을 먼저 정하지 않고 관측값과 연산규칙을 먼저 고정한다.
7. 같은 lineage 반복은 독립증거로 세지 않는다.
8. 실패·반례·negative result·재현실패·철회는 보존한다.

핵심 금지식:

```
unobserved != zero
survivor performance != comparative superiority
citation count != validity
institutional prestige != independence
consensus != independent replication
standard != empirical proof
```

---

## 2. 상태변수

actor i의 시점 t 상태:

```
S_i(t) = [
  P_i(t),  # effective power
  I_i(t),  # usable information access
  E_i(t),  # practical exit
  R_i(t),  # independent recovery
  O_i(t),  # effective option-space
  B_i(t),  # captured benefit
  C_i(t),  # borne cost
  K_i(t),  # correction/verification burden
  L_i(t),  # liability/responsibility burden
  Q_i(t)   # contestability
]
```

직접 관측이 불가능하면 proxy와 construct를 분리한다.

`score != construct`

---

## 3. 방향을 미리 정하지 않는 비교

어느 actor가 약자인지, 지배자인지 먼저 정하지 않는다.

모든 ordered pair `(a,b)`에 대해 동일한 차분을 계산한다.

```
D_ab(t) = [
  Δ(P_a-P_b),
  Δ(I_a-I_b),
  Δ(E_a-E_b),
  Δ(R_a-R_b),
  Δ(O_a-O_b),
  Δ(B_a-B_b),
  Δ(C_a-C_b),
  Δ(K_a-K_b),
  Δ(L_a-L_b),
  Δ(Q_a-Q_b)
]
```

부호는 결과일 뿐 해석을 선결정하지 않는다.

---

## 4. 수렴 패턴 후보

다음 변화가 반복적으로 같은 방향으로 묶일 때 구조적 수렴 후보가 된다.

- 권한 비대칭 증가
- practical exit 감소
- 독립복구 감소
- option-space 감소
- 비용 외부화 증가
- 교정·검증 노동의 한쪽 집중
- contestability 감소
- 비가역성 증가
- 독립 비교경로 감소

단일 변수는 충분조건이 아니다.

```
POWER_ASYMMETRY => EXPLOITATION
```

같은 추론은 금지한다.

---

## 5. 제거된 미래와 반사실 소멸

핵심 폐루프:

```
선택
→ 대안 제거
→ 제거된 미래 미관측
→ 현재 경로만 성과 생성
→ 현재 정책 신뢰 증가
→ 추가 대안 제거
```

이 구조를 `COUNTERFACTUAL_EXTINCTION_LOOP`로 부른다.

핵심은 제거된 대안이 더 좋았다고 가정하는 것이 아니다.

핵심은:

> 대안을 제거하면 현재 경로가 실제로 더 우월했는지 비교할 능력 자체가 사라질 수 있다.

---

## 6. 옵션공간

시점 t의 옵션집합:

```
Ω(t) = {o1, o2, ..., on}
```

각 옵션은 최소 다음 속성을 가진다.

- accessibility
- reversibility
- switching cost
- restoration cost
- independence
- information diversity
- execution feasibility
- expected value range
- uncertainty

따라서:

```
nominal_option_count != effective_option_count
```

같은 공급자·데이터·평가기준·기관 lineage에 종속된 여러 옵션은 실질적으로 독립적이지 않을 수 있다.

---

## 7. 식별가능성

모든 값은 세 종류로 분리한다.

```
OBSERVED
ESTIMABLE
NONIDENTIFIED
```

규칙:

```
NONIDENTIFIED != ZERO
NONIDENTIFIED != FALSE
ESTIMATED != OBSERVED
```

제거된 미래가치처럼 직접 관측하기 어려운 값은 가능한 경우 점추정 대신 구간으로 유지한다.

```
V_removed(o) ∈ [LB(o), UB(o)]
```

---

## 8. 정보손실

옵션 제거비용은 단순 직접비용이 아니다.

```
TotalRemovalCost =
  DirectRemovalCost
+ RestorationCost
+ InformationLoss
+ ExternalizedCost
```

여기서:

```
InformationLoss =
  lost_future_observations
+ lost_comparator_value
+ lost_model_discrimination
+ lost_recovery_path
```

즉 대안 제거는 정보생성능력 제거일 수 있다.

---

## 9. 자기검증 폐루프

현재 정책 신뢰 H,
실효 옵션공간 N_eff,
독립교정능력 Q_ext를 두면 다음 구조가 가능하다.

```
H↑
→ pruning↑
→ N_eff↓
→ comparator evidence↓
→ contradiction rate↓
→ H↑
```

따라서 contradiction 감소를 자동으로 성과개선으로 해석하지 않는다.

```
ObservedAgreement =
  TrueImprovement
+ ComparatorLossEffect
+ MeasurementNarrowingEffect
+ SelectionEffect
```

---

## 10. 반증가능성 보존량

```
FalsifiabilityReserve(t) = [
  independent_comparators,
  reversible_branches,
  dissenting_evidence_access,
  raw_data_access,
  external_audit_access,
  restoration_capacity
]
```

이 값이 지속 감소하면 현재 정책의 참/거짓과 별개로 검증가능성이 약화된다.

---

## 11. 히스테리시스

정책을 되돌릴 수 있어도 시스템 상태가 돌아온다는 보장은 없다.

```
policy reversibility != system reversibility
state_after_reversal != state_before_intervention
```

한번 제거된 생태계·인력·데이터·대안·신뢰·복구경로는 정책 철회만으로 복구되지 않을 수 있다.

---

## 12. 선행연구 역추적

선행연구는 다음 순서로 역추적한다.

```
최종 주장
→ 원출처
→ 원자료
→ 측정
→ 분석
→ 자금·이해상충
→ 선택·억제
→ 출판
→ 기관 PR
→ 언론·바이럴
→ 정책·표준
→ 독립재현
→ 반대증거
→ 재사용 판정
```

왜곡 지점:

```
DATA / MEASUREMENT / ANALYSIS / SPONSOR / SELECTION /
PUBLICATION / AUTHORITY / REPLICATION / TRANSFER
```

각 상태:

```
OBSERVED / PLAUSIBLE / UNKNOWN / NOT_SUPPORTED
```

---

## 13. 연구·바이럴 수혜/손실 추적

분석단위:

```
claim × actor × propagation stage × time horizon
```

추적 차원:

- MONEY
- POWER
- REPUTATION
- ATTENTION
- OPTION
- LIABILITY
- LABOR/TIME
- SAFETY/WELFARE
- NARRATIVE CONTROL

핵심 질문:

- 누가 주장의 진위와 무관하게 바이럴 자체로 이득을 얻는가?
- 누가 검증비용을 내는가?
- 누가 오류비용을 떠안는가?
- 누가 복구노동을 담당하는가?
- 누가 새 권한을 얻는가?
- 누가 practical exit를 잃는가?

`beneficiary != manipulator`

고의성은 별도 직접증거가 필요하다.

---

## 14. 대체모형 경쟁

Project 가설은 기본승자가 아니다.

최소 다음을 동시에 경쟁시킨다.

```
M1 실제 구조적 권한집중
M2 측정오류
M3 선택편향
M4 공통 외생충격
M5 효율화
M6 자발적 전문화/delegation
M7 lock-in / switching-cost accumulation
M8 cost externalization
M9 데이터·평가기준 drift
M10 comparator loss
M11 measurement narrowing
M12 UNKNOWN
```

모형은 설명력뿐 아니라 다음으로 비교한다.

- out-of-sample prediction
- 반사실 적합성
- 잔차
- 복잡도
- 식별가능성
- 반대증거

---

## 15. 인과식별

상관과 인과를 분리한다.

각 edge는 다음 상태 중 하나를 가진다.

```
OBSERVED_ASSOCIATION
IDENTIFIED_CAUSAL
PLAUSIBLE
UNKNOWN
NOT_SUPPORTED
```

`post hoc story != causal identification`

가능하면 실험·자연실험·준실험·패널·도구변수·DiD·RDD 등으로 식별을 시도하되, 방법 이름 자체를 증명으로 취급하지 않는다.

---

## 16. 타당성 벡터

각 구조 주장에 다음을 붙인다.

```
Validity = [
  ConstructValidity,
  MeasurementValidity,
  InternalValidity,
  ExternalValidity,
  LineageIndependence,
  TemporalRobustness,
  CounterfactualIdentifiability
]
```

하나의 총점으로 압축하지 않는다.

낮은 축은 높은 축으로 상쇄하지 않는다.

---

## 17. 실행 파이프라인

결론보다 절차를 먼저 고정한다.

```
1. observations freeze
2. variable definitions freeze
3. lineage clustering
4. missingness map
5. actor/option set definition
6. before/after state collection
7. pairwise/all-actor transition
8. comparator survival check
9. competing causal models
10. counterfactual tests
11. sensitivity analysis
12. counterevidence integration
13. FalsifiabilityReserve check
14. hysteresis check
15. validity vector
16. construct mapping
17. decision state
18. next discriminating observation
```

후단 결론이 전단 변수·threshold·weight를 역으로 수정하지 못한다.

수정이 필요하면 새 version으로 재실행하고 기존 결과를 보존한다.

---

## 18. 최소 판정상태

```
SUPPORTED_PATTERN
PARTIAL_PATTERN
MIXED
UNRESOLVED
NOT_SUPPORTED
FALSIFIED_WITHIN_SCOPE
NONIDENTIFIED
```

판정 대상은 사람이나 기관이 아니라 구체적 구조 주장과 경로다.

---

## 19. Project 자체 자기감사

Project Intersection도 같은 formalism의 적용대상이다.

반드시 다음을 검사한다.

- AI가 연구방향을 과도하게 결정하는가?
- 사용자의 대안탐색공간이 줄고 있는가?
- 문서량·commit 증가가 실제 외부검증을 대체하고 있는가?
- 내부 형식화가 외부검증·지원·파트너 확보 없는 폐루프가 되고 있는가?
- 사용자와 AI 사이 정보·도구·실행권 비대칭이 커지고 있는가?
- 연구의 고유 언어가 외부 반증비용을 높이고 있는가?
- 실패·반례가 실제로 살아남는가?
- independent comparator가 유지되는가?

Project가 이 검사를 통과하지 못하면 자기 이론으로 자기 자신부터 문제삼아야 한다.

---

## 20. 현재 현실 경계

현재 공개 상태에서 다음은 확립되지 않았다.

- 독립 외부 과학 재현
- 광범위 현실 검증
- 일반적 ICM/공존 가설의 경험적 타당성
- 제거된 미래가치의 안정적 추정법
- 수렴 임계점의 보편적 calibration

따라서 현재 문서는 **형식명세와 검증 프레임**이지 경험적 정답이 아니다.

---

## 21. 다음 검증 우선순위

새 개념 추가보다 실제 적용을 우선한다.

1. 산업후원·출판편향 역사사례 1건
2. AI 평가·감사·거버넌스 사례 1건
3. Project Intersection 자체 1건

세 사례에 같은 변수·같은 절차를 적용한다.

최소 데이터 구조:

```
actor
time
P
I
E
R
O
B
C
K
L
Q
lineage
evidence
counterevidence
reversibility
comparator_persistence
validity_vector
decision_state
```

---

## 22. 한 문장 요약

> 시스템이 성과를 높이는 과정에서 독립 대안·exit·복구·비교·반증 가능성을 함께 제거하면, 실제 개선과 자기검증 폐루프를 구분하기 어려워질 수 있다. Project Intersection은 그 수렴을 의도나 도덕판단이 아니라 관측변수·시간축·인과·반사실·대체모형으로 추적하려는 연구다.
