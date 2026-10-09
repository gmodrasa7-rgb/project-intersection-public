# EARLY WARNING: 평가재가공 조기탐지기

상태: `OPERATIONAL DETECTOR CANDIDATE / RETROSPECTIVELY VALIDATED / NOT A GUILT CLASSIFIER`

목적:
사건·스캔들이 확정된 뒤 "왜 그랬는가"를 설명하는 것이 아니라,
**단기보상 × 평가재가공권 구조가 실제 목표와 관측지표를 갈라놓기 시작하는 초기 신호**를 탐지한다.

이 탐지기는 사람·기관의 도덕성, 의도, 성향을 판정하지 않는다.

---

## 1. 탐지 대상

기본 변수:

```
M = measured / reported proxy performance
Y = underlying / long-horizon target state
STI = short-horizon incentive vector
ERP = evaluation reprocessing power vector
IV = independent verification capacity
RDA = raw-data access
CI = cost internalization
RH = reward horizon
G = distance(M,Y)
```

핵심 위험구조:

```
M is rewarded faster than Y
+ actor can directly influence M-generation
+ Y is observed late/weakly
+ independent verification is delayed or dependent
```

그러나 이 구조만으로 재가공이 발생했다고 판정하지 않는다.

---

## 2. 탐지 단계

### S0 NO_STRUCTURAL_EXPOSURE

다음 중 하나 이상이 없음:
- meaningful proxy metric
- reward/pressure coupling
- actor access to metric-generation path

행동:
`NO ESCALATION`

---

### S1 STRUCTURAL_EXPOSURE

다음이 동시에 존재:

```
proxy M linked to reward/pressure
AND
actor has at least one ERP channel
```

ERP channel:

```
object_creation
data_entry
sampling
timing
metric_definition
disclosure_visibility
evidence_context
evaluation_aware_behavior
```

S1은 위험 노출이지 이상행동 증거가 아니다.

행동:
- Y shadow measure 확보
- raw-data provenance 고정
- incentive change 시점 기록
- comparator/holdout 보존

---

### S2 STATISTICAL_DISCREPANCY

다음 중 하나 이상이 반복·재현 가능하게 관측:

#### D1 threshold bunching
성과가 보상/제재 cutoff 바로 안쪽에 비정상적으로 몰림.

#### D2 discontinuity around target
threshold 전후의 분포가 자연적 과정으로 설명하기 어려운 형태로 단절.

#### D3 metric jump without Y confirmation
M은 급상승하지만 독립 Y 또는 downstream outcome이 따라오지 않음.

#### D4 implausible joint pattern
개별 변수는 가능하지만 결합패턴이 비정상.
예:
- 어려운 문항 정답 + 쉬운 문항 오답의 비정상 조합
- 다수 대상의 동일한 연속 응답
- 불가능하거나 매우 희귀한 process ordering

#### D5 abnormal zero / missing / reclassification
0, missing, excluded, cancelled, reclassified 상태가
target 근처에서 급증.

#### D6 variance compression
평가대상들이 갑자기 지나치게 비슷한 점수/패턴으로 수렴.

#### D7 field-metric divergence
complaint, direct observation, sensor, audit, user outcome과 M이 체계적으로 어긋남.

#### D8 post-incentive distribution shift
STI 또는 penalty 도입 직후
Y보다 M의 분포가 먼저/더 크게 변함.

행동:
`INDEPENDENT AUDIT / BLINDED RETEST`

주의:
S2는 fraud/intent 판정이 아니다.
resource allocation, rule ambiguity, learning, selection, measurement error도 경쟁설명이다.

---

### S3 REPRODUCIBLE_M_Y_DIVERGENCE

독립 측정·blinded retest·field measurement·shadow dataset에서
M–Y 괴리가 다시 관측됨.

필수조건:
- evaluator 또는 data lineage가 원 평가와 실질적으로 분리
- 가능한 경우 원 평가대상에게 retest 조건을 숨기거나 최소화
- 원자료와 재구성 규칙 보존

행동:
- ERP channel별 process trace
- incentive coupling before/after 비교
- competing model test

---

### S4 REPROCESSING_MECHANISM_OBSERVED

M을 Y와 독립적으로 변화시키는 구체적 경로가 직접 관측됨.

예:

```
test-context detection
data-entry rewrite
unauthorized object creation
sample exclusion/reclassification
disclosure suppression
context stripping
metric-definition shift
```

이 단계에서도 의도는 자동추론하지 않는다.

---

### S5 CAUSAL_INFLUENCE_IDENTIFIED

가능하면 다음 중 하나로
STI/ERP가 행동변화를 일으킨 인과효과를 식별:

- incentive introduction/removal
- threshold change
- randomized audit/retest
- quasi-natural experiment
- ERP restriction
- independent-verification introduction
- reward-horizon change

현재 가장 강한 상태.

---

## 3. False-positive 방지

탐지기는 다음 이유만으로 올라가지 않는다.

```
high target
high bonus
high pressure
high performance
rapid improvement
centralized control
industry funding
strong leadership
```

필수 분리:

```
STRUCTURAL EXPOSURE
!=
STATISTICAL DISCREPANCY
!=
REPROCESSING MECHANISM
!=
CAUSAL EFFECT
```

---

## 4. Negative control — 강한 목표가 실제 개선을 만든 경우

### English NHS waiting-time targets

Propper et al. (2010)
DOI 10.1016/j.jpubeco.2010.01.002

England–Scotland natural experiment에서
영국의 강한 waiting-time target은:
- 평균 waiting time 감소
- 비표적 emergency activity의 명확한 감소 없음
- patient health on exit 악화 증거 없음
- waiting-list reordering의 뚜렷한 증거 없음

을 보고했다.

따라서:

```
STI high
+ target strong
!= gaming
```

이 사례는 detector의 false-positive calibration에 사용한다.

판정:
`S1 STRUCTURAL_EXPOSURE → NO ROBUST ESCALATION IN TESTED OUTCOMES`

---

## 5. Retrospective validation A — Chicago teacher cheating detection

Jacob & Levitt (2003)
DOI 10.3386/w9413
DOI 10.3386/w9414

탐지 신호:
- 예상 밖의 큰 score gain
- 다음 해 작은 gain 또는 decline
- 동일한 suspicious answer blocks
- 학생 간 비정상적으로 높은 answer correlation
- 어려운 문항 정답 + 쉬운 문항 오답 같은 unusual pattern

알고리즘이 high-risk로 고른 교실을
prospective monitored retest했을 때
큰 score decline이 나타났고,
large gain이지만 cheating signal이 없던 교실은 성과를 대부분 유지했다.

Detector mapping:

```
S1 incentive exposure
→ S2 statistical discrepancy
→ S3 prospective monitored retest
→ S5 incentive sensitivity evidence
```

중요:
이 사례는 **통계 anomaly만으로 끝내지 않고 독립 retest로 확인**했다.

---

## 6. Retrospective validation B — Volkswagen

독립 on-road measurement가
standard laboratory test와 실제 주행 간 큰 배출 discrepancy를 먼저 드러냈다.

EPA:
- test 상황에서 full emissions control
- normal driving에서 effectiveness 감소
- NOx 최대 40× standard

Detector mapping:

```
S1 test-compliance incentive + test-aware control surface
→ S2 lab/road divergence
→ S3 independent on-road replication/investigation
→ S4 test-context detection mechanism observed
```

핵심:
`deployment-like shadow measurement`가 매우 강한 조기탐지 수단.

---

## 7. Retrospective validation C — Phoenix VA

VA OIG는 공식 scheduling data와 실제 patient access를 재구성해
큰 discrepancy와 scheduling-process 문제를 확인했다.

Detector mapping:

```
S1 wait metric tied to performance pressure
→ S2 field/metric divergence + suspicious zero-day patterns
→ S3 independent OIG reconstruction
→ S4 desired-date/data-process reprocessing observed
```

중요 반례:
후속 조사자료에는 일부 직원이 잘못된 규칙이 맞다고 이해했다는 증언도 있음.

따라서:
`S4 mechanism observed != every actor intentional`

---

## 8. 가장 정보가치 높은 조기신호

현재까지 prior art + 사례를 압축하면 우선순위는 다음이다.

### E1. Independent M–Y shadow divergence

가장 강한 초기신호.

예:
- test vs field
- official wait vs reconstructed wait
- reported sales vs customer authorization
- test score vs controlled retest

### E2. Threshold bunching / heaping

target 직전·직후에 비자연적 집중이 생기는지.

경계:
bunching은 effort response일 수도 있고 manipulation일 수도 있다.
그 자체로 원인을 판정하지 않는다.

### E3. Discontinuity after incentive change

보상/제재 규칙 변경 직후
M이 Y보다 훨씬 더 빠르게 변하는지.

### E4. Anomaly disappears under independent retest

독립/blinded 조건에서 성과가 급락하면
M의 생성환경 의존성을 강하게 의심할 수 있다.

### E5. Missingness/reclassification changes near target

평가에 포함되지 않는 상태로 대상이 이동하는지.

### E6. Cross-lineage disagreement

독립 data/evaluator lineage가
같은 대상을 평가했을 때 결론이 체계적으로 갈리는지.

---

## 9. 최소 데이터 요구

탐지기 실행 전 최소:

```
metric_definition
underlying_objective_definition
reward/penalty rule
reward_horizon
ERP map
raw event timestamps
raw denominator
excluded/reclassified cases
independent shadow measure
incentive-change dates
audit/retest dates
lineage map
```

이 중 핵심 필드가 없으면:
`NONIDENTIFIED / DATA_REQUIRED`

로 종료한다.

결측을 정상으로 간주하지 않는다.

---

## 10. 자동 분석 순서

```
1. Freeze M and Y definitions
2. Map STI vector
3. Map ERP channels
4. Freeze denominator and missingness rules
5. Plot/estimate M and Y over time
6. Search threshold discontinuity / bunching
7. Search zero/missing/reclassification shifts
8. Compare incentive-change windows
9. Compare independent shadow measurement
10. Run blinded/controlled retest if possible
11. Trace actual ERP process
12. Test competing models
13. Assign S0–S5 state
14. Record next discriminating observation
```

---

## 11. 경쟁모형

항상 동시에 유지:

```
C1 genuine improvement
C2 deliberate metric reprocessing
C3 non-deliberate procedural adaptation
C4 rule ambiguity / training failure
C5 resource/capacity constraint
C6 selection/composition change
C7 measurement error
C8 exogenous shock
C9 mixed
C10 UNKNOWN
```

한 anomaly를 C2로 자동 승격하지 않는다.

---

## 12. 현재 결론

조기탐지는 가능하다.

하지만 예측대상은:
"누가 조작할 것인가"가 아니다.

예측대상은:

> **어떤 시스템에서 관측지표 M과 실제 목표 Y가 분리될 조건이 형성됐고, 실제 데이터에서 그 분리가 시작됐는가?**

가장 강한 detector는
행위자의 의도를 읽는 것이 아니라:

```
incentive structure
+ metric-generation access
+ independent shadow measurement
+ distributional anomaly
+ controlled retest
```

를 결합하는 것이다.

현재 상태:
`OPERATIONAL CANDIDATE / RETROSPECTIVE POSITIVE + NEGATIVE CONTROL PASSED`

다음 checkpoint:
실제 공개 시계열 dataset 하나에 이 탐지기를 blind하게 적용해
사후 사건명을 보지 않고 anomaly를 먼저 검출한다.
