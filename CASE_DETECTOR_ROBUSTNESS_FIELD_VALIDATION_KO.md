# CASE: 탐지기 강건성 현장검증 — 의료 분모이동 · 보고빈도 역효과 · 실제 AI drift

상태: `FIELD ROBUSTNESS VALIDATION / MIXED EVIDENCE / FALSE-POSITIVE+FALSE-NEGATIVE CONTROL`

목적:
평가재가공 탐지기가 실제 환경에서
1) 분류·분모 변화,
2) 감시 강화의 역효과,
3) 탐지기 자체의 노후화/누락
를 얼마나 구별할 수 있는지 검증한다.

핵심:
```
metric movement != mechanism
more monitoring != more truth
stable performance metric != stable data-generating process
```

---

## 1. 의료 readmission — 분류/분모 변화는 metric을 크게 바꿀 수 있음

### 관측

Hospital readmission metric은 inpatient admission을 중심으로 계산되는 경우가 많고
observation stay는 numerator/denominator에서 제외될 수 있다.

여러 연구에서 observation status 사용비율이 병원별로 크게 달랐고,
observation stay를 포함하면 병원 ranking이 상당히 변했다.

소아병원 50곳 연구:
- observation use: 0–53%
- observation을 포함하면 60%의 병원이 최소 1 quintile 이동
- 20%는 2 quintile 이상 이동

Medicare 전체병원 연구:
- observation stay를 포함한 대안지표를 사용하면 약 14.9% 병원이
  high/low performer 분류를 바꿀 수 있음.

### 중요한 반례

HRRP 도입 뒤 observation stay가 증가했고
이를 gaming 가능성으로 해석하는 논의가 존재하지만,
JAMA Network Open 분석에서는 observation을 포함해도
target condition과 nontarget condition 간 차이가 사라지며
"readmission 개선이 전부 observation reclassification 때문"이라는
단순 설명은 지지되지 않았다.

즉:

```
classification shift observed
!= incentive-caused manipulation identified
```

### 탐지기 영향

F5 `CLASSIFICATION_DENOMINATOR_SHIFT`는
`CROSS_DOMAIN`에서 `EMPIRICAL_METRIC_EFFECT`로 승격할 수 있다.

그러나 C2 deliberate reprocessing은 자동승격 금지.

필수 판별:
- 동일 환자군에 fixed denominator replay
- observation 포함/제외 모두 계산
- incentive 전후 target/nontarget 비교
- severity/composition 변화 통제

---

## 2. Mutual funds — 더 자주 공개하면 window dressing이 오히려 증가할 수 있음

### 자연실험

Xin & Zhang (2024),
*Wrong Kind of Transparency? Mutual Funds’ Higher Reporting Frequency, Window Dressing, and Performance*
DOI 10.1111/1475-679X.12527

2004 SEC의 holdings reporting frequency 증가를 이용한 자연실험에서
더 잦은 공개가 window dressing을 증가시켰다고 보고했다.

또 window dressing 증가가 큰 일부 fund는:
- lower returns
- greater outflows
- higher collapse rate
와 연결됐다.

### Project delta

기존의 직관:

```
monitoring frequency ↑
→ observability ↑
→ gaming ↓
```

은 보편법칙이 아니다.

경쟁구조:

```
monitoring frequency ↑
→ observability ↑
AND
→ report-date salience / optimization incentive ↑
→ point-in-time signal manipulation ↑
```

따라서 monitoring 강화는
탐지력과 적응압력을 동시에 올릴 수 있다.

### 탐지기 영향

F1 reporting-window effect 강화.
새 규칙:

```
monitoring_intensity_effect =
  detection_gain
  - adaptation_signal_gain
```

둘을 분리 측정한다.

---

## 3. 실제 의료 AI — 성능감시만으로 drift를 못 볼 수 있음

### 실증

Kore et al., Nature Communications (2024)
*Empirical data drift detection experiments on real-world medical imaging data*

실제 흉부 X-ray 환경에서 COVID-19 출현에 따른
real-world data drift를 사용해 drift detector를 비교했다.

핵심:
- aggregate performance 변화 없이도 data drift가 발생할 수 있음
- performance monitoring alone은 drift의 좋은 대리변수가 아닐 수 있음
- drift detection sensitivity는 sample size와 patient feature에 의존
- automated gold labels 자체도 drift의 영향을 받을 수 있음

### Project delta

F7 detector aging/validity decay를
단순 구조가설에서 실제 field drift evidence로 강화한다.

```
stable detector metric
!= stable input distribution
!= stable construct validity
```

탐지기 자체가 정상으로 보이는 동안
관측대상 분포가 변할 수 있다.

### 방어적 검증

- output performance와 input distribution을 별도 감시
- population/composition shift 추적
- delayed ground-truth 발생 시 retrospective recalibration
- detector의 sample-size sensitivity 기록

---

## 4. 세 사례의 공통 판별

| 실패유형 | field evidence | 자동 의도판정 가능? | 필요한 재검증 |
|---|---|---:|---|
| F5 classification/denominator | 강함 | 아니오 | fixed-denominator replay |
| F1 reporting-window | 강함 | 아니오 | event-time + long-window measure |
| F7 detector aging/drift | 강함 | 해당 없음 | input drift + delayed outcome |

공통 규칙:

```
metric anomaly
→ first ask whether representation changed
→ then whether behavior changed
→ only then ask whether incentive caused the change
```

---

## 5. 탐지기 수정

기존 강건성 감시를 다음처럼 변경한다.

### R-A. REPRESENTATION CHECK
metric 정의·분모·분류·missingness가 바뀌었는지 먼저 확인.

### R-B. TEMPORAL CHECK
점시점/보고일 효과와 장기평균을 분리.

### R-C. SYSTEM CHECK
한 node 개선과 전체 system outcome을 분리.

### R-D. DISTRIBUTION CHECK
output metric 안정과 input/data-generating process 안정성을 분리.

### R-E. CAUSAL CHECK
incentive change가 실제 behavior change를 만들었는지 별도 식별.

---

## 6. 탐지기 자체의 새 상태변수

```
representation_version
denominator_version
population_distribution_version
monitoring_frequency
reporting_frequency
last_field_revalidation
drift_evidence
metric_stability
distribution_stability
```

`metric_stability=true`라도
`distribution_stability=unknown/false`이면
탐지기 유효성을 자동 연장하지 않는다.

---

## 7. 현재 판정

```
F1 REPORTING_WINDOW_EFFECT:
  EMPIRICAL → EMPIRICAL + POLICY-NATURAL-EXPERIMENT SUPPORT

F5 CLASSIFICATION_DENOMINATOR_SHIFT:
  CROSS_DOMAIN → EMPIRICAL_METRIC_EFFECT
  deliberate manipulation causal weight = UNRESOLVED

F7 DETECTOR_AGING:
  STRUCTURAL → EMPIRICAL_REAL_WORLD_DRIFT_SUPPORT
```

새 1차 K 커널:
`NONE`

새 강건성 원칙:
`MORE MONITORING CAN INCREASE BOTH DETECTION AND ADAPTATION PRESSURE`

---

## 8. 다음 최소검증

1. reporting frequency가 바뀐 전후에
   point-in-time anomaly와 long-horizon Y가 어떻게 달라지는지 추가 사례 확보
2. fixed-denominator replay를 다른 공공성과지표에 적용
3. detector output이 안정적이지만 input distribution이 변한 실제 AI deployment 사례 추가
4. 새 monitor 도입 뒤 behavior가 다른 proxy/channel로 이동한 전후자료 확보
