# CASE: 단기보상 × 평가재가공권 — Wells Fargo · VA wait-time · Atlanta Schools

상태: `CROSS-DOMAIN EMPIRICAL CASE / K4 DISCRIMINATION`

목적:
Project Intersection의 `STI × ERP × IV/RDA/CI/RH` 가설을
은행·의료행정·교육 세 분야의 실제 사례에 적용한다.

핵심 질문:

> 단기 성과지표가 보상·평가·직무압력에 연결되고, 현장 actor가 그 지표를 직접 바꿀 수 있을 때, 실제 목표상태보다 관측지표를 바꾸는 행동이 반복되는가?

도덕·선악·성향은 변수에서 제외한다.

---

## 1. 공통 변수

```
STI = short-term incentive intensity
ERP = evaluation reprocessing power
IV  = independent verification
RDA = raw-data access
CI  = cost internalization
RH  = reward horizon

M = measured/reported performance
Y = underlying/long-horizon target state
G = distance(M,Y)
```

### STI는 금전만이 아니다

이번 사례군 때문에 STI를 벡터로 분해한다.

```
STI = [
  cash_bonus,
  promotion/career,
  job_retention,
  status/reputation,
  target_pressure,
  unit_budget/resource,
  deadline/short-cycle evaluation
]
```

한 요소가 낮아도 다른 요소가 높으면
단기 evaluation pressure는 강할 수 있다.

---

## 2. Wells Fargo — sales target / compensation → unauthorized accounts

### 강한 공식자료

미국 CFPB는 2016년 Wells Fargo의 광범위한 불법 판매관행에 대해 제재하면서,
직원들이 sales target과 compensation incentive에 의해
고객 동의 없이 deposit/credit-card account를 개설하고
기존 계좌에서 자금을 옮겨 sales figures를 높였다고 밝혔다.

당시 bank 자체 분석상
2백만 개가 넘는 deposit/credit-card account가
고객 승인 없이 개설됐을 가능성이 있다고 CFPB가 밝혔다.

원출처:
- CFPB enforcement action
  https://www.consumerfinance.gov/enforcement/actions/wells-fargo-bank-2016/
- CFPB press release
  https://www.consumerfinance.gov/archive/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/

### 변수 매핑

```
STI: HIGH — sales target + financial compensation
ERP: HIGH — 직원이 account count/sales figure를 직접 변경 가능
M: accounts/products sold
Y: 실제 고객수요·유효 서비스 제공
G: unauthorized accounts가 많을수록 확대
IV/RDA: 고객동의·실사용·complaint와 대조할 때 개선
CI: 고객 fee·장기 법적비용이 frontline 단기보상에 즉시 완전 내부화되지 않음
RH: short sales cycle
```

### 판정

`STRONG SUPPORT FOR STI × ERP → PROXY-RESPONSIVE ACTION`

중요:
이 사례는 단순 "거짓 보고"보다 강하다.

```
metric-relevant object itself was created
→ M increases
while underlying customer demand Y does not
```

즉 K4a의 `OBJECT FABRICATION / PROXY PRODUCTION` 하위형이다.

---

## 3. Phoenix VA — wait-time metric → scheduling-data manipulation

### 강한 공식자료

VA OIG 2014 interim/final review:
- Phoenix leadership의 FY2013 performance appraisal에는 wait-time 관련 성과가 포함됐고,
  awards/salary increases의 고려요소였다.
- 표본 226명의 공식 VA data에서는 평균 wait 24일로 보고됐지만
  OIG 재구성에서는 평균 약 115일.
- schedulers가 desired date를 바꿔 false 0-day wait time을 만드는 manipulation이 관측됨.
- final report는 부적절한 scheduling practice와 wait-time manipulation이 VHA 전반에서 광범위하게 확인됐다고 보고.

원출처:
- VA OIG interim report 14-02603-178
- VA OIG final report 14-02603-267
- Oversight.gov:
  https://www.oversight.gov/reports/audit/review-alleged-patient-deaths-patient-wait-times-and-scheduling-practices-phoenix-va

VA leadership는 이후:
- wait-time metric이 care의 수단이 아니라 목적이 됐다고 공개적으로 인정
- 14-day access measure를 개인 performance plan에서 제거해
  inappropriate scheduling motive를 줄이겠다고 발표.

### 변수 매핑

```
STI: performance appraisal / award / salary / target pressure
ERP: HIGH — desired-date entry와 scheduling process가 reported wait metric을 바꿈
M: reported wait days / 14-day compliance
Y: veteran's actual elapsed access time and care availability
G: OIG reconstruction에서 매우 크게 관측
IV/RDA: external reconstruction of appointment history가 있을 때 증가
CI: patient delay cost가 metric manipulator에게 즉시 동일하게 귀속되지 않음
RH: annual/short performance cycle
```

### 강한 판별증거

```
Official M ≈ 24 days
Independent reconstruction Y-like access interval ≈ 115 days
```

정확히 같은 construct는 아니므로
`M-Y`를 단순 산술차로 보편화하지 않지만,
reported metric과 independently reconstructed access experience 사이의
대규모 divergence가 직접 관측됐다.

### 판정

`VERY STRONG SUPPORT FOR K4a + K8`

특히:
```
metric became target
→ data-entry/scheduling practice adapts
→ reported metric improves
→ actual waiting problem remains less visible
```

---

## 4. Atlanta Public Schools — test-score target → answer-sheet alteration

### 증거계보

Georgia Governor special investigation report:
- APS에서 조직적 test tampering 조사
- report TOC 자체가 "Why Cheating Occurred", "Targets", "Culture of Fear",
  "Early Warnings", "Allegations of Cover-Up", "Alteration and Destruction of Documents"를 별도 분석축으로 둠.

원출처:
https://gosa.georgia.gov/sites/gosa.georgia.gov/files/related_files/site_page/APS-Investigation-Volume-1.pdf

AJC의 state-report 기반 보도:
- 약 178명의 educator, 38명의 principal이 cheating에 연루됐다고 조사결과를 보도
- wrong-to-right erasure 등으로 test result 수정
- 일부 implicated school의 educator에게 test target 연계 bonus 지급
- 그러나 조사/보도는 금전보상만보다 pressure/intimidation/culture of fear가 더 큰 설명일 수 있음을 지적

보조출처:
Atlanta Journal-Constitution investigative archive.

### 변수 매핑

```
STI:
  cash bonus = 일부 존재
  target pressure = high
  status/reputation = high
  career/job pressure = material candidate

ERP:
  HIGH where answer sheets/testing process physically controllable

M:
  standardized test score / target attainment

Y:
  student's underlying learning/capability

IV:
  erasure analysis + external investigation이 들어오면 증가

RDA:
  raw answer sheets / erasure marks / class-level histories가 중요
```

### 가장 중요한 구조적 delta

이 사례는:

```
STI != cash incentive only
```

를 강제한다.

단기압력은:
- bonus
- target
- supervisor pressure
- status
- career consequences

의 합성구조일 수 있다.

### 판정

`STRONG SUPPORT FOR METRIC GAMING / STI SOURCE MIXED`

단,
각 개인의 행동원인을 하나의 incentive로 환원하지 않는다.

---

## 5. 세 사례의 동일 구조

| Case | M: 단기지표 | Y: 실제 목표 | ERP | STI 핵심 | 재가공 방식 |
|---|---|---|---|---|---|
| Wells Fargo | products/accounts sold | 실제 고객수요·유효서비스 | high | sales target + compensation | unauthorized object creation |
| Phoenix VA | reported wait time | 실제 진료접근 시간 | high | performance/award/target | desired-date/data-process manipulation |
| Atlanta APS | test score/target | 학생 학습 | high | target + career/status + 일부 bonus | answer alteration |

공통:

```
short-cycle evaluated proxy M
+ actor can directly influence M
+ reward/pressure responds faster to M than to Y
→ effort can shift toward M-responsive action
```

중요:
세 사례는 동일한 행위나 법적 성격이 아니다.
공통되는 것은 인센티브-측정 구조다.

---

## 6. 기존 가설 수정

이 사례군은 기존:

```
STI × ERP × low IV
→ M-Y gap may ↑
```

를 유지하지만 STI를 scalar 하나로 두는 것은 부족함을 보여준다.

수정:

```
STI_vector = [
  monetary,
  employment,
  promotion,
  reputation,
  hierarchy/target,
  resource,
  temporal
]
```

그리고 ERP도 분해한다.

```
ERP = [
  object_creation,
  data_entry,
  sampling,
  timing,
  metric_definition,
  disclosure,
  context_transformation,
  evaluation-aware_behavior
]
```

### 새 1차 커널 여부

`NO NEW FIRST-ORDER KERNEL`

K4의 측정해상도가 올라간 것이다.

---

## 7. 자동 탐지용 최소 시그널

앞으로 사건을 찾을 때 다음 순서로 역검색한다.

```
S1. 짧은 평가주기의 proxy metric이 있는가?
S2. proxy가 보상·진급·생존·평판·자원과 연결되는가?
S3. 평가대상 actor가 proxy 생성과정에 직접 접근 가능한가?
S4. underlying Y는 M보다 늦게 또는 더 어렵게 관측되는가?
S5. M과 독립 raw/field measure가 어긋나는가?
S6. external verification이 들어온 뒤 discrepancy가 드러났는가?
S7. correction 뒤 reward/evaluation design이 바뀌었는가?
```

특히 S7은 강한 자연실험 신호다.

예:
VA가 14-day access measure를 individual performance plan에서 제거한 것은
해당 metric-incentive coupling 자체가 operational concern이었다는
정책적 반응증거다.

---

## 8. 경쟁가설

각 사례에서 동시에 검사:

```
M1 deliberate metric gaming
M2 ambiguous rules / training failure
M3 resource shortage
M4 measurement design failure
M5 local misconduct without system incentive effect
M6 mixed mechanism
M7 UNKNOWN
```

VA OIG 후속 조사에서는
metric이 비직관적이고 훈련이 부족했으며 잘못된 practice가 광범위했던 점도 원인으로 제시됐다.

따라서:
```
metric manipulation observed
!= every instance caused by reward incentive
```

을 유지한다.

---

## 9. 현재 결론

이번 세 사례는
"단기보상을 원하는 actor는 조작한다"를 지지하는 것이 아니다.

더 좁게:

> **실제 목표 Y보다 빨리 보상되는 proxy M이 있고, 평가대상 actor가 M의 생성과정에 접근할 수 있으며, 독립검증이 늦을 때, M에 반응하는 행동이 Y를 개선하는 행동과 분리될 수 있다는 현상이 서로 다른 분야에서 반복 관측된다.**

현재 상태:
`CROSS-DOMAIN SUPPORT FOR K4 / CAUSAL WEIGHT OF EACH STI COMPONENT PARTIAL`

다음 checkpoint:
- 같은 metric을 유지하면서 incentive coupling만 바뀐 전후자료
- ERP만 제한한 전후자료
- independent raw-data verification이 도입된 전후자료

를 찾아 `STI`와 `ERP`의 인과효과를 분리한다.
