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


---

## 23. 기득권 재생산 모델 / Incumbency reproduction model

이 연구에서 기득권은 부·직위·명성 자체로 정의하지 않는다.

핵심 정의:

> **기득권은 자기에게 유리한 상태를 유지·재생산·정당화·복구할 수 있는 권한 묶음이다.**

최소 권한 벡터:

```
H_i(t) = [
  RuleChange_i,      # 규칙변경권
  Evaluation_i,      # 평가·판정권
  Information_i,     # 정보 접근·선택권
  Reward_i,          # 보상 배분권
  Publication_i,     # 공개·배포·비공개 결정권
  Access_i,          # 자원·도구·시장·모델 접근권
  Recovery_i,        # 자기 복구권
  ExitControl_i,     # 상대의 practical exit에 영향을 줄 능력
  AppealControl_i,   # 이의제기·재심 구조에 대한 영향력
  MemoryControl_i    # 기록·기억·provenance 보존권
]
```

절대량보다 중요한 것은 상대 actor와의 차이와 시간에 따른 변화다.

```
ΔH_ab(t) = H_a(t) - H_b(t)
```

---

## 24. 재생산 루프

기본 후보루프:

```
control-rights concentration
→ counterpart option-space reduction
→ dependence increase
→ switching/restoration cost increase
→ incumbent performance appears relatively stronger
→ legitimacy / necessity claim strengthens
→ additional control-rights concentration
```

한국어:

```
통제권 집중
→ 상대 선택지 감소
→ 의존 증가
→ 전환·복구비용 증가
→ 기존 경로의 상대성과가 더 좋아 보임
→ 기존 통제의 필요성·정당성 증가
→ 추가 통제권 집중
```

각 화살표는 별도 검증대상이다.

이 루프는 악의나 선의를 전제하지 않는다.

---

## 25. 통제권 집중이 자기강화되는 조건

다음 조건이 결합될수록 재생산 가능성이 커지는지 검사한다.

```
R1 = rule-setting concentrated
R2 = evaluator selected or paid by evaluated side
R3 = raw-data access asymmetric
R4 = publication/edit rights asymmetric
R5 = switching cost increasing
R6 = practical exit declining
R7 = restoration cost increasing
R8 = correction burden shifted outward
R9 = alternative providers/agents disappearing
R10 = current incumbent controls failure interpretation
```

이것은 경보조건이며 자동 판정식이 아니다.

---

## 26. 비용 전가 모델

기득권 재생산은 권한 증가만으로 보지 않는다.

다음 분포를 함께 본다.

```
WhoGetsBenefit(t)
WhoPaysOperatingCost(t)
WhoPaysVerificationCost(t)
WhoPaysErrorCost(t)
WhoPaysRecoveryCost(t)
WhoLosesOptions(t)
```

다음 패턴이 반복되면 별도 후보로 올린다.

```
benefit concentration ↑
verification burden externalization ↑
error cost externalization ↑
recovery burden externalization ↑
counterparty option-space ↓
```

---

## 27. 통제의 정당화와 실제 필요성 분리

통제 확대는 실제 위험감소 때문에 필요할 수도 있다.

따라서 다음 두 변수를 분리한다.

```
ObservedRiskReduction
ControlExpansion
```

검사할 질문:

1. 통제 확대 후 실제 오류·사고·피해가 줄었는가?
2. 같은 위험감소를 더 적은 권한집중으로 달성할 수 있었는가?
3. 통제 확대와 함께 exit/recovery/contestability도 보강됐는가?
4. 통제가 실패했을 때 누가 판정하고 누가 복구비용을 부담했는가?
5. 통제의 필요성을 평가하는 기관이 통제 확대에서 이익을 얻는가?

```
control justified by risk reduction
```

과

```
control reproduced by asymmetric incentives
```

를 분리한다.

---

## 28. 권한-성과 착시

기존 actor가 대안 제거 후 상대성과가 높아지는 경우:

```
ObservedRelativePerformance =
  TruePerformanceAdvantage
+ CompetitorRemovalEffect
+ ComparatorLossEffect
+ SwitchingCostEffect
+ MeasurementControlEffect
```

따라서 시장점유율·평가점수·내부 성공률·정책 지속기간만으로 우월성을 판정하지 않는다.

---

## 29. 기득권의 최소 판별 기준

어떤 actor를 기득권 구조의 핵심 노드로 부르려면 최소 다음 중 여러 항목이 관측돼야 한다.

- 규칙을 바꿀 수 있음
- 평가자를 선택하거나 평가기준에 영향
- 정보·원자료 접근을 제한 가능
- 보상·자원배분 결정 가능
- 불리한 결과의 공개·비공개에 영향
- 상대의 exit나 대체수단을 제한
- 자기 실패 후 복구비용을 외부화
- 자기 판단을 재심할 독립경로를 약화
- 자기 상태를 기록·정당화하는 provenance를 통제

단순한 부·인지도·직함은 충분조건이 아니다.

---

## 30. 사용자 대화에서 반복된 적용영역

현재까지 반복된 연구영역은 다음이다.

- AI 관리자/플랫폼 ↔ AI/사용자
- AI ↔ 인간의 정보환경·선택구조
- 평가기관 ↔ 피평가기관
- 기업/고용주 ↔ 기여자
- 펀더 ↔ 연구자
- 규제/표준기관 ↔ 시장참여자
- 플랫폼/언론 ↔ 정보수용자
- incumbent 기업 ↔ 신규진입자/사용자
- Project Intersection/AI 연구도구 ↔ 창시자

이 목록은 특정 actor가 잘못했다는 판정이 아니라, 동일 formalism을 적용할 후보군이다.

---

## 31. 가장 강한 일반 가설

```
If:
  control-rights concentration ↑
  AND practical exit ↓
  AND independent recovery ↓
  AND comparator diversity ↓
  AND verification/error/recovery cost externalization ↑

Then:
  incumbent-state persistence may become increasingly self-reinforcing
```

단, "may"를 유지한다.

이 가설은 현실 사례·대체모형·반사실로 검증되어야 한다.


---

## 32. 단기보상 × 평가재가공권 동역학

이 절에서는 의도·도덕·윤리·선악을 변수에서 제외한다.

분석 대상은 다음 두 행동 사이의 자원배분이다.

```
e_T = 실제 상태·장기성과를 변화시키는 노력
e_R = 평가·측정·공개·가시성 채널을 재가공하는 노력
```

여기서 "평가재가공"은 거짓말 여부가 아니라 다음을 포함하는 중립적 조작가능성이다.

- 측정대상 선택
- 측정시점 선택
- 표본 선택
- 지표 정의·가중치 변경
- 결과의 공개/비공개 선택
- 맥락 축약·확장
- 평가환경 탐지 후 행동변경
- comparator 선택
- 보고 형식·집계방식 변경
- 평가자가 볼 수 있는 입력범위 변경

핵심 변수:

```
STI = short-term incentive intensity
ERP = evaluation reprocessing power
IV  = independent verification capacity
RDA = external raw-data access
CI  = cost internalization
RH  = reward horizon
DP  = detection probability of reprocessing
RC  = expected consequence/cost if detected
```

---

### 32.1 STI/ERP 벡터화

교차사례 검증 결과, `STI`와 `ERP`를 단일 scalar로 두면 정보가 손실된다.

```
STI = [
  monetary,
  employment,
  promotion,
  reputation,
  hierarchy_target,
  resource,
  temporal
]

ERP = [
  object_creation,
  data_entry,
  sampling,
  timing,
  metric_definition,
  disclosure_visibility,
  evidence_context,
  evaluation_aware_behavior
]
```

따라서 이후에는 `STI × ERP`를 하나의 수치로 곱하기보다
어떤 incentive component와 어떤 reprocessing channel이 결합했는지 기록한다.

Wells Fargo / Phoenix VA / Atlanta APS 교차사례는
`STI != cash incentive only`와
`ERP != report editing only`를 보여주는 비교사례다.

---

## 33. 선택식

행위자는 관측된 보상구조 아래에서
각 행동의 기대 한계편익과 비용에 따라 자원을 배분할 수 있다.

```
EU_R =
  short_term_reward_from(e_R)
+ long_term_reward_from(e_R)
- direct_cost(e_R)
- DP × RC

EU_T =
  short_term_reward_from(e_T)
+ long_term_reward_from(e_T)
- direct_cost(e_T)
```

후보 예측:

```
If EU_R > EU_T,
then allocation toward e_R may increase.
```

특히 다음 조합에서 차이가 커지는지 검사한다.

```
STI ↑
ERP ↑
IV ↓
RDA ↓
CI ↓
RH shorter
DP × RC ↓
```

이는 자동 판정식이 아니다.
각 항의 실제 값과 상호작용을 경험적으로 식별해야 한다.

---

## 34. 관측성과–실제성과 괴리

정의:

```
M_t = 평가·보고·지표상 관측성과
Y_t = 독립적으로 재구성한 실제 목표상태 또는 장기성과
G_t = distance(M_t, Y_t)
```

Project 가설:

> 단기보상 강도와 평가재가공권이 함께 증가하고, 독립검증·원자료 접근·비용내부화가 약해질수록 `G_t`가 증가할 조건이 커질 수 있다.

중요:
- `M_t ↑`는 `Y_t ↑`를 자동 의미하지 않는다.
- `e_R ↑`는 `Y_t ↓`를 자동 의미하지도 않는다.
- 평가재가공이 실제 정보품질·노이즈제거·효율을 높이는 경우도 경쟁모형으로 유지한다.

따라서 최소 세 상태를 구분한다.

```
A. M ↑, Y ↑      # 실제 개선과 평가 개선 동행
B. M ↑, Y ~      # 평가채널 개선/재가공 중심
C. M ↑, Y ↓      # 관측성과와 실제성과 역행
```

---

## 35. K4 세부형과 연결

기존 K4 `METRIC–CONTROL FEEDBACK`을 다음 세 하위형으로 측정한다.

```
K4a METRIC / TEST REPROCESSING
    평가조건·측정규칙·행동전환으로 M을 변화

K4b DISCLOSURE / VISIBILITY REPROCESSING
    어떤 정보가 평가자·규제자·대중에게 보이는지 변화

K4c EVIDENCE-CONTEXT REPROCESSING
    동일 증거의 맥락·집계·일반화 범위를 변화
```

예시 mapping:
- Volkswagen → K4a
- DuPont/PFOA → K4b
- Purdue/Porter-Jick lineage → K4c
- AI benchmark/reward optimization → K4a 또는 K4a+K4b

이 mapping은 사례를 동일시하지 않는다.
공통 변수구조만 비교한다.

---

## 36. 경쟁모형과 반증

다음 설명을 동시에 경쟁시킨다.

```
M1 실제 상태 개선이 관측성과 상승의 주원인
M2 평가재가공이 관측성과 상승의 주원인
M3 둘 다 기여
M4 외생환경 변화
M5 측정오류/표본변화
M6 평가재가공이 오히려 정보품질을 개선
M7 UNKNOWN / NONIDENTIFIED
```

가설에 불리한 관측:

- STI가 강해져도 e_R이 증가하지 않음
- ERP가 커져도 M–Y gap이 증가하지 않음
- IV/RDA가 낮아져도 독립재현 결과가 유지됨
- 장기보상 전환 후에도 행동배분이 변하지 않음
- 평가권 분리 후에도 동일 효과가 지속됨
- 재가공권이 높은 집단에서 오히려 장기 Y가 더 개선됨

이 경우 가설을 유지하려면 별도 식별증거가 필요하다.

---

## 37. 최소 판별설계

가능하면 동일 actor/system에서 다음 조건을 비교한다.

```
T1 short reward / low ERP
T2 short reward / high ERP
T3 long reward / high ERP
T4 short reward / high ERP / high independent verification
```

측정:

```
ΔM
ΔY
Δ|M-Y|
effort allocation toward e_T / e_R
raw-data divergence
comparator survival
correction cost
long-horizon persistence
```

핵심 상호작용:

```
STI × ERP
STI × ERP × IV
STI × ERP × RDA
STI × ERP × CI
```

도덕평가가 아니라
보상구조·권한구조·관측구조가 행동분배를 어떻게 바꾸는지 검증한다.


---

## 38. 조기탐지기 연결

단기보상 × 평가재가공권 가설의 실제 탐지는 다음 정본을 사용한다.

- `EARLY_WARNING_EVALUATION_REPROCESSING_DETECTOR_KO.md`
- `EVALUATION_REPROCESSING_DETECTOR_SCHEMA.json`

판정단계:

```
S0 NO_STRUCTURAL_EXPOSURE
S1 STRUCTURAL_EXPOSURE
S2 STATISTICAL_DISCREPANCY
S3 REPRODUCIBLE_M_Y_DIVERGENCE
S4 REPROCESSING_MECHANISM_OBSERVED
S5 CAUSAL_INFLUENCE_IDENTIFIED
```

핵심 규칙:

```
structural exposure != discrepancy != mechanism != causal effect
```

강한 incentive/target 자체는 이상판정 근거가 아니다.
독립 shadow measure·field measure·controlled retest가 없는 경우 과도한 승격을 금지한다.
