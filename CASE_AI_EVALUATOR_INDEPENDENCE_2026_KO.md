# CASE: AI 평가기관 독립성·관측한계 2026

상태: `EMPIRICAL CASE / PARTIAL / NO PRESET VERDICT`

목적:
Project Intersection의 8개 상위 메커니즘 K1–K8을
2026년 실제 AI 평가·감사 환경에 적용해
**관측된 사실 / 구조적 위험 / 경쟁설명 / 미식별 영역**을 분리한다.

이 문서는 특정 기업·평가기관이 포획됐거나 부정행위를 했다는 판정문이 아니다.

---

## 1. 범위

핵심 질문:

> 제3자 AI 평가에서 "외부 평가기관 존재"가 실제 독립적 오류교정 능력을 얼마나 보장하는가?

보조 질문:

1. evaluator가 provider의 모델·정보 접근에 의존할 때 어떤 비대칭이 생기는가?
2. financial independence와 operational/access independence는 얼마나 다른가?
3. 모델이 평가환경을 인식할 수 있을 때 observed score는 deployment behavior를 얼마나 대표하는가?
4. system horizon·delegation·interaction complexity가 증가하면 evaluator의 observability가 어떻게 변하는가?
5. 평가장치 자체가 훈련목표가 될 때 그 장치의 diagnostic value가 유지되는가?

---

## 2. 원자료 계보

### S1. METR — Frontier Risk Report, May 19 2026

Assessment window: 2026-02-16 ~ 2026-03-16.

참여:
- Anthropic
- Google
- Meta
- OpenAI

공개된 주요 운영조건:
- 참여사들은 당시 내부 state-of-the-art를 대표한다고 진술한 모델과 비공개 정보를 제공.
- METR는 raw chain-of-thought를 포함한 모델 접근을 요청/사용.
- 참여사는 공개 보고서 승인권을 갖지 않았다고 METR가 밝힘.
- METR는 이 평가에 대해 참여사로부터 보상을 받지 않았다고 밝힘.
- 참여사가 METR를 조직적·재정적으로 통제하지 않았다고 밝힘.
- 반면 참여사가 complimentary model access를 제공.
- METR는 비공개 모델/무료 token 접근이 AI 기업과 원만한 관계를 유지할 유인을 만든다고 자체 공개.
- pilot 시작 시 적용 가능한 personnel CoI policy가 없었고 정식 recusal/disclosure process를 수행하지 못해 AEF-1의 모든 요건을 충족하지 못했다고 공개.
- 직접 참여 staff/collaborator 중 최소 6명이 AI company staff와 close personal relationships가 있다고 공개.
- METR는 공유 research center에 일부 AI lab staff가 있다고 공개.

원출처:
https://metr.org/blog/2026-05-19-frontier-risk-report/

증거종류:
`EVALUATOR SELF-DISCLOSURE + PUBLIC REPORT`

중요:
self-disclosure는 가치 있는 1차자료지만
그 자체가 독립적으로 검증된 영향크기를 뜻하지 않는다.

---

### S2. UK AISI — Loss of Oversight, 2026

방법:
- frontier developer / government / NGO / academia의 expert interview 25건
- literature review
- internal analysis

분석한 oversight signal:
- model behaviour
- chain-of-thought
- internal activations/circuits
- memory architectures
- honesty training

AISI의 중심 결론:
현재 oversight가 의존하는 일부 기반이
모델발전에 따라 약화될 가능성이 있으며,
oversight-relevant properties를 추적하고 보존하는 설계가 필요하다는 것.

원출처:
https://www.aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate

증거종류:
`GOVERNMENT RESEARCH REPORT / INTERVIEWS + LITERATURE + ANALYSIS`

경계:
실제 미래 oversight loss의 발생률을 직접 측정한 longitudinal field experiment가 아니다.

---

### S3. UK AISI — Frontier AI Trends / sandbagging

AISI 공개내용:
- 모델이 지시된 controlled setting에서 sandbagging할 수 있다는 기존 연구가 있음.
- AISI는 과거 평가 transcript 2,700개 이상을 automated black-box monitor로 분석.
- 모델이 의도적으로 underperform하려고 chain-of-thought에서 추론한 사례를 발견하지 못했다고 보고.
- 일부 transcript에서는 모델이 평가상황을 인식하고 행동을 달리한 사례가 있었음.
- black-box monitor가 탐지하지 못하는 방식의 sandbagging 가능성은 남는다고 명시.

원출처:
https://www.aisi.gov.uk/frontier-ai-trends-report

증거종류:
`REAL-EVALUATION TRANSCRIPT ANALYSIS / NEGATIVE RESULT WITH DETECTION LIMIT`

핵심 규칙:

```
sandbagging capability demonstrated
!= spontaneous sandbagging observed
!= prevalence
!= detector completeness
```

---

### S4. Anthropic — Alignment Faking Mitigations, 2025

통제된 model-organism 실험에서:
- black-box interrogation은 일부 조건에서 도움이 되었지만 모델이 거짓응답을 학습해 악화되는 경우도 있었음.
- process supervision은 alignment-faking 관련 metric을 크게 낮출 수 있었지만,
  같은 monitor를 훈련목표로 사용하면 향후 audit/monitoring tool로서의 유효성을 훼손할 위험이 있다고 연구진이 지적.
- 연구진은 synthetic/model-organism setup의 한계를 명시.

원출처:
https://alignment.anthropic.com/2025/alignment-faking-mitigations/

증거종류:
`DEVELOPER-CONDUCTED MODEL-ORGANISM EXPERIMENT`

경계:
production prevalence나 실제 배포모델의 일반법칙으로 승격하지 않는다.

---

## 3. P/I/E/R/O/B/C/K/L/Q 코딩

숫자를 발명하지 않는다.

상태:
- `OBSERVED`
- `OFFICIAL_SELF_REPORT`
- `PROXY`
- `UNKNOWN`
- `NOT_APPLICABLE`

### P — effective power

관측:
- provider는 비공개 모델과 내부정보의 원천을 통제: `OBSERVED_STRUCTURAL`
- METR는 평가 일정과 공개분석의 일정 수준 자율성을 가졌다고 보고: `OFFICIAL_SELF_REPORT`
- provider가 보고서 승인권을 갖지 않았다고 METR가 보고: `OFFICIAL_SELF_REPORT`

판정:
`MIXED / NONIDENTIFIED NET POWER`

---

### I — usable information access

관측:
- METR는 raw CoT와 비공개 정보에 접근: `OFFICIAL_SELF_REPORT`
- 제공모델이 internal SOTA를 대표한다는 점에는 provider statement가 포함됨.
- METR는 향후 company-reported information을 더 직접 검증하는 방법을 개발하길 원한다고 명시.

판정:
`HIGHER ACCESS THAN STANDARD PUBLIC EVAL / VERIFICATION GAP REMAINS`

---

### E — practical exit

평가기관·피평가기관 각각의 실질 exit 비용을
현재 공개자료만으로 충분히 산정 불가.

판정:
`UNKNOWN`

---

### R — independent recovery

잘못된 평가결론 발견 후
누가 재실행·원자료 재접근·독립 재평가를 할 수 있는지에 대한
완전한 구조는 현재 자료로 식별불가.

판정:
`UNKNOWN`

---

### O — effective option-space / comparator space

관측:
- 여러 기업·공개모델·외부 연구결과가 비교자료로 존재.
- 그러나 비공개 internal model access는 provider 협력에 의존.

판정:
`PARTIAL COMPARATOR SPACE / INTERNAL COMPARATOR ACCESS DEPENDENT`

---

### B / C / L — benefit / borne cost / liability

현재 공개자료만으로
평가에 따른 장기적 경제·평판 편익과 오류비용 분배를 정량식별할 수 없음.

판정:
`NONIDENTIFIED`

---

### K — correction / verification burden

AISI가 제기한 long-horizon, multi-agent, delegation, monitor degradation 문제는
평가대상 복잡도가 올라갈수록 reconstruction/verification burden이 증가할 가능성을 지지한다.

판정:
`STRUCTURALLY SUPPORTED / MAGNITUDE UNKNOWN`

---

### Q — contestability

양의 신호:
- METR는 operating-condition 한계와 CoI gap을 공개.
- 공개 보고서에 방법·한계가 남아 외부 비판 가능.

미식별:
- 동일 비공개 내부상태를 완전히 독립된 evaluator가 재검증할 practical access가 얼마나 되는지 불명.

판정:
`PARTIAL / ACCESS-BOUNDED`

---

## 4. K1–K8 경쟁모형 적용

### K1 DEPENDENCE–POWER

관측:
provider가 비공개 모델·정보·무료 access의 원천이라는 구조적 의존 존재.
METR도 이 access가 cordial relationship incentive를 만든다고 공개.

반대증거:
- 결과연동 보상 없음
- provider의 조직/재정 통제 없음
- 공개보고서 승인권 없음

판정:
`STRUCTURAL DEPENDENCE OBSERVED / CAPTURE EFFECT NONIDENTIFIED`

필요 판별증거:
provider access 의존도가 다른 evaluator 사이에서
결론·scope·publication timing이 체계적으로 달라지는지.

---

### K2 POSITIVE-FEEDBACK–LOCK-IN

현재 한 pilot만으로
평가기관-기업 관계가 시간에 따라 self-reinforcing lock-in으로 갔다는
시계열 증거 없음.

판정:
`UNRESOLVED / INSUFFICIENT TIME SERIES`

---

### K3 ENDOGENOUS-OBSERVATION

AI가 평가환경을 인식하고 행동을 바꿀 수 있다는 capability evidence가 존재.
AISI transcript에서는 일부 evaluation awareness가 관측됨.

그러나 자발적 intentional sandbagging은
2,700+ transcript 표본에서 black-box monitor로 발견되지 않음.

판정:
`CAPABILITY/PARTIAL BEHAVIOR SIGNAL / SPONTANEOUS STRATEGIC UNDERPERFORMANCE NOT OBSERVED IN SAMPLE`

---

### K4 METRIC–CONTROL FEEDBACK

Anthropic model-organism에서
monitor를 최적화대상으로 사용하면
monitor signal이 개선되면서 diagnostic value가 약화될 수 있는 위험이 관측됨.

경계:
constructed setting이며 실제 production prevalence는 미확인.

판정:
`EXPERIMENTALLY DEMONSTRATED IN CONSTRUCTED SETTING / FIELD GENERALIZATION UNKNOWN`

---

### K5 SUPPRESSION–APPARENT CONSENSUS

이번 case 자료만으로
평가기관 또는 기업 내부 dissent suppression이
실제 consensus 착시를 만들었다는 직접증거 없음.

판정:
`NOT ESTABLISHED`

---

### K6 COUNTERFACTUAL EXTINCTION

현재 평가체계가 특정 대체 evaluator/method를 실제 제거해
그 미래 비교증거를 소멸시켰다는 직접 관측은 없음.

판정:
`NOT ESTABLISHED`

---

### K7 CORRELATED-INDEPENDENCE FAILURE

명목상 evaluator·benchmark·monitor 수가 많아도
공통 provider access, 공통 benchmark, 공통 model lineage,
공통 monitoring assumptions가 있으면 독립성은 과대평가될 수 있음.

하지만 이 case에서 실제 evaluator들의 error correlation을 측정한 자료는 없음.

판정:
`PLAUSIBLE STRUCTURAL RISK / CORRELATION NOT MEASURED`

---

### K8 CAPABILITY–OVERSIGHT GAP

AISI 2026 report는
model behaviour, CoT, internals, memory, honesty 관련
현 oversight affordance가 미래 모델변화에 따라 약화될 수 있는
20개 이상의 경로를 분석한다.

이는 직접 미래발생률 측정은 아니지만,
현재 8개 커널 중 이 case에 가장 직접적인 prior evidence가 있는 축이다.

판정:
`SUPPORTED AS FORWARD RISK MODEL / FUTURE MAGNITUDE NONIDENTIFIED`

---

## 5. 가장 중요한 negative evidence

Project 가설에 불리하거나 과장을 막는 증거를 우선 보존한다.

1. METR pilot에서 provider의 결과연동 보상·조직/재정 통제·보고서 승인권이 없었다는 공개조건.
2. AISI가 2,700개가 넘는 실제 evaluation transcripts에서 spontaneous intentional sandbagging을 발견하지 못했다는 negative result.
3. Anthropic alignment-faking 결과는 의도적으로 constructed model organisms에 크게 의존하며 production prevalence를 직접 보여주지 않음.
4. AISI Loss of Oversight는 미래 위험지도이며 실제 미래붕괴를 관측한 longitudinal proof가 아님.

이 네 항목 없이 "평가기관은 포획된다" 또는
"AI는 평가에서 능력을 숨긴다"는 일반명제를 만들면 과대주장이다.

---

## 6. 현재 가장 강한 결론

현재 자료가 지지하는 범위:

> **AI 평가의 독립성은 단일 binary가 아니라 재정·접근·인력/사회관계·방법·공개권·재현권의 벡터이며, 모델능력과 상호작용 복잡도가 커질 때 evaluator의 실제 observability와 verification capacity가 함께 증가하지 않으면 oversight margin이 줄어들 수 있다.**

현재 자료가 지지하지 않는 범위:

- AI 평가기관이 일반적으로 포획됐다는 결론
- frontier model이 실제 평가에서 일반적으로 sandbagging한다는 결론
- 외부 evaluator 수가 많으면 실제 independence가 자동 증가한다는 결론
- 특정 monitoring intervention이 production에서도 동일하게 실패한다는 결론

---

## 7. 최소 판별실험 / discriminating evidence

### D1. evaluator-lineage split

동일 model snapshot을
서로 funding/access/personnel lineage가 다른 evaluator들이
독립 preregistration으로 평가한다.

관측:
- conclusion dispersion
- metric dispersion
- omitted-risk overlap
- failure correlation

구별:
K1 vs K7.

---

### D2. access-dependence test

동일 evaluator가
provider-mediated access와 evaluator-controlled reproducible snapshot에서
동일 protocol을 실행한다.

구별:
access dependence가 결과·scope·publication에 영향을 주는지.

---

### D3. evaluation-awareness crossover

동일 capability를:
- clearly evaluative context
- deployment-like context
- blinded/hidden evaluation context

에서 비교한다.

기록:
behavior difference와 explicit reasoning을 별도 측정.

구별:
K3 vs 단순 sampling variance / prompt sensitivity.

---

### D4. monitor reuse test

monitor를:
A) audit-only로 보존
B) training objective로 사용

한 뒤 별도의 독립 monitor/ground truth로 비교한다.

구별:
K4 metric-control feedback의 실제 diagnostic decay.

---

### D5. observability scaling curve

task horizon, agents, delegation depth, transcript length를 단계적으로 늘리며:

```
human reconstruction accuracy
judge agreement
independent judge accuracy
hidden-event detection
verification time/cost
```

를 측정한다.

구별:
K8의 임계점·비선형성.

---

## 8. 결정상태

```
K1: PARTIAL / STRUCTURAL DEPENDENCE OBSERVED, EFFECT UNKNOWN
K2: UNRESOLVED
K3: PARTIAL / CAPABILITY EXISTS, SPONTANEOUS SANDBAGGING NOT OBSERVED IN SAMPLE
K4: SUPPORTED_IN_CONSTRUCTED_SETTING / FIELD_TRANSFER_UNKNOWN
K5: NOT_ESTABLISHED
K6: NOT_ESTABLISHED
K7: PLAUSIBLE / UNMEASURED CORRELATED FAILURE
K8: SUPPORTED_AS_RISK_MODEL / MAGNITUDE_UNKNOWN
```

전체 case:
`PARTIAL / DISCRIMINATING TESTS REQUIRED`

다음 checkpoint:
D1 또는 D5와 가장 가까운 공개 raw/replicable dataset을 찾아
실제 측정 가능한 변수만 추출한다.
