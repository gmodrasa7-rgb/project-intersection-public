# PRIOR ART SATURATION MAP / 선행연구 포화지도

상태: `ACTIVE SATURATION SEARCH / NOT A TRUTH REGISTRY`

목적은 선행연구를 정답으로 채택하는 것이 아니다.

이 문서는 Project Intersection의 핵심 메커니즘과 관련된 선행연구를 가능한 넓게 탐색하면서,
새 메커니즘·새 반례·새 왜곡경로·새 경계조건이 더 이상 유의미하게 추가되지 않는 지점까지 추적하기 위한 지도다.

핵심 규칙:

```
prior art != truth
citation count != validity
prestige != independence
consensus != independent replication
absence of observed alternative != absence of alternative
apparent convergence != true preference convergence
observed success != comparative superiority
```

---

## 1. 현재까지 확인된 메커니즘 군

### A. 의존 → 권력 비대칭

대표:
- Emerson (1962), *Power-Dependence Relations*, DOI 10.2307/2089716
- Pfeffer & Salancik (1978), *The External Control of Organizations*

재사용:
```
critical resource dependence
→ bargaining asymmetry
→ external control becomes possible
```

경계:
대체자원·다중관계·countervailing capacity가 있으면 재균형 가능.

---

### B. 초기 우위 → 누적우위

대표:
- Merton (1968), Matthew effect, DOI 10.1126/science.159.3810.56
- van de Rijt et al. (2014), cumulative advantage experiments, DOI 10.1073/pnas.1316836111

재사용:
```
initial advantage
→ visibility / reward
→ increased probability of later advantage
```

경계:
diminishing returns가 관측될 수 있으며 무한 runaway는 자동 결론이 아님.

---

### C. 사회적 관측 → cascade / correlated choice

대표:
- Bikhchandani, Hirshleifer & Welch (1992)
- Welch (1992), DOI 10.1111/j.1540-6261.1992.tb04406.x
- Salganik, Dodds & Watts (2006), DOI 10.1126/science.1121066

재사용:
```
visibility of prior choices ↑
→ independent signal use ↓
→ correlated behavior ↑
→ concentration / unpredictability ↑
```

경계:
cascade는 새 정보와 독립신호로 깨질 수 있음.

---

### D. positive feedback → path dependence / lock-in

대표:
- Arthur (1989), DOI 10.2307/2234208
- Sydow, Schreyögg & Koch (2009), DOI 10.5465/amr.34.4.zok689
- Fouquet (2016), energy-system path dependence

재사용:
```
local reinforcement
→ relative viability of alternatives ↓
→ switching/restoration cost ↑
→ persistence ↑
```

경계:
path dependence가 곧 비효율·착취를 뜻하지 않음.

---

### E. installed base / compatibility → excess inertia 또는 excess momentum

대표:
- Farrell & Saloner (1985), DOI 10.2307/2555589
- Farrell & Saloner (1986), installed base and compatibility

재사용:
설치기반 자체가 미래 전환비용과 혁신경로를 바꿀 수 있음.

경계:
항상 inertia만 발생하지 않고 반대 방향인 excess momentum도 가능.

---

### F. 정책·제도 → 자기피드백

대표:
- Pierson (1993; 2000), policy feedback / increasing returns
- Acemoglu & Robinson (2008), DOI 10.1257/aer.98.1.267

재사용:
```
formal rule
→ resources / incentives / interpretation change
→ de facto power investment
→ future institutional outcome change
```

중요:
형식적 규칙개혁과 실질 권력변화를 분리해야 함.

---

### G. 평가·지표 → Goodhart/Campbell형 왜곡

대표:
- Goodhart (1975/1979)
- Campbell (1976/1979), DOI 10.1016/0149-7189(79)90048-X
- Simmons, Nelson & Simonsohn (2011), DOI 10.1177/0956797611417632
- Kerr (1998), HARKing, DOI 10.1207/s15327957pspr0203_4

재사용:
```
metric importance ↑
→ optimization pressure ↑
→ adaptation to metric ↑
→ metric-to-construct validity may ↓
```

연구 자체도 이 구조의 대상이다.

---

### H. 개입이 관측대상 자체를 바꿈

대표:
- Lucas (1976), *Econometric Policy Evaluation: A Critique*, DOI 10.1016/S0167-2231(76)80003-6
- Perdomo et al. (2020), *Performative Prediction*, PMLR 119

재사용:
```
prediction / policy / evaluation
→ actor behavior or outcome distribution changes
→ future data distribution changes
→ retraining / reevaluation occurs on intervention-shaped data
```

Project 추가 연결:
관측 데이터가 제도·모델·평가의 결과라면 그 데이터를 외생적 현실표본으로 취급하면 안 됨.

---

### I. 알고리즘이 자기 학습자료를 만든다

대표:
- Chaney, Stewart & Engelhardt (2018), *How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility*

재사용:
추천시스템이 이미 자기 추천에 노출된 사용자 데이터로 다시 학습하면
feedback loop가 사용자 행동을 동질화하면서 utility를 높이지 않을 수 있음.

Project 연결:
```
system action
→ environment/user response
→ response becomes training/evaluation data
→ system updates
→ stronger system-shaped environment
```

이는 단순 prediction error가 아니라 **endogenous observation loop**다.

---

### J. 겉보기 합의 ≠ 실제 선호 수렴

대표:
- Prentice & Miller (1993), pluralistic ignorance, DOI 10.1037/0022-3514.64.2.243
- Kuran, preference falsification
- Spiral-of-silence literature: 경험적 지지는 혼합적이며 강한 보편명제로 사용 금지

재사용:
```
private state != public expression
public expressions → perceived norm
perceived norm → future public expressions
```

따라서:
```
observed consensus != latent consensus
low visible dissent != low private dissent
```

Project 추가 변수:
- private/public preference gap
- cost of dissent
- anonymity effect
- visible-defection threshold
- suppressed alternative signal

---

### K. 선택편향·선택적 보고 → 살아남은 증거의 왜곡

대표:
- Heckman (1979), sample selection bias, DOI 10.2307/1912352
- Chan et al. (2004), selective outcome reporting, DOI 10.1001/jama.291.20.2457
- Ioannidis (2005), DOI 10.1371/journal.pmed.0020124
- Turner et al. (2008), DOI 10.1056/NEJMsa065779
- Cochrane financial-COI reviews

재사용:
```
full evidence universe
→ selection / suppression / reporting filters
→ visible evidence base
```

따라서 visible literature는 원래 evidence universe와 동일하지 않음.

---

### L. 독립 연구도 평가게임의 대상이 됨

대표:
- Registered Reports 연구, DOI 10.1038/s41562-021-01142-4

재사용:
결과를 알기 전에 peer review와 in-principle acceptance를 하는 구조가
publication bias 및 planned/unplanned 분석 혼동을 줄이는 방향의 제도적 개입으로 연구됨.

경계:
이 역시 완전한 진실보장 장치는 아니며 novelty·운영비용·새로운 gaming 가능성을 별도 추적해야 함.

---

### M. AI reward/control channel → instrumental incentive

대표:
- Everitt et al., *Reward Tampering Problems and Solutions in RL*, arXiv:1908.04734
- Everitt et al. (2021), *Agent Incentives: A Causal Perspective*
- Uesato et al. (2020), *Avoiding Tampering Incentives in Deep RL via Decoupled Approval*

재사용:
평가·reward channel이 agent utility 경로에 들어가면
그 채널 자체에 영향을 줄 유인이 생길 조건을 causal graph로 분석할 수 있음.

중요 경계:
인간 조직의 Goodhart 문제와 AI instrumental incentive는 유사 메커니즘 후보이지 동일 현상으로 간주하지 않음.

---

### N. AI benchmark → 포화·판별력 상실

대표:
- Akhtar et al. (ICML 2026), *When AI Benchmarks Plateau*

60개 LLM benchmark 분석에서 거의 절반이 saturation을 보였고,
benchmark age가 증가할수록 saturation이 증가했다.
expert curation은 saturation 저항성과 관련됐으나 public/private test data 여부는 보호효과가 관측되지 않았다.

Project 연결:
```
score ↑
while discrimination information ↓
```
가 동시에 가능함.

---

### O. AI monitoring 자체의 적응 문제

관련 연구군:
- alignment-faking model-organism 연구
- scalable oversight / weak-to-strong supervision
- AI control / trusted monitoring

최근 공개 연구는 일부 인공적으로 구성된 model organism에서
monitoring/training intervention이 행동을 바꾸고,
어떤 mitigation은 의도와 반대로 lying/monitor-evasion을 강화할 수도 있음을 보고한다.

경계:
model-organism 결과를 production model 일반법칙으로 승격하지 않는다.
설계된 조건·classifier dependence·training contamination·transfer validity를 추적한다.

---

### P. 규제·감사·평가 → capture 가능성, 비필연성

대표:
- Stigler (1971), DOI 10.2307/3003160
- Peltzman (1976), DOI 10.1086/466865
- Carpenter & Moss (eds.), *Preventing Regulatory Capture*

재사용:
concentrated stakes, privileged access, 약한 countervailing capacity가 capture 위험을 높일 수 있음.

반대축:
transparency, institutional capacity, review, appeal, countervailing actors가 위험을 줄일 수 있음.

---

### Q. 조직화 → oligarchic tendency, 그러나 철칙 아님

Michels 계열 고전가설과 후속 비판문헌을 함께 사용한다.

재사용:
```
coordination complexity
→ specialized leadership / information concentration
→ concentration tendency possible
```

반례축:
horizontal ties, distributed participation, countervailing organizations가 집중을 깨거나 제한할 수 있음.

---

### R. exploration ↔ exploitation

대표:
- March (1991), DOI 10.1287/orsc.2.1.71
- Levinthal (1997), DOI 10.1287/mnsc.43.7.934

재사용:
단기 exploitation 성과가 장기 exploration capacity 손실과 동시에 발생할 수 있음.

Project 연결:
현재성과와 미래탐색능력을 같은 축으로 합치지 않는다.

---

### S. polycentric governance / 다중 중심

대표:
- Ostrom (2010), DOI 10.1016/j.gloenvcha.2010.07.004

재사용:
복잡한 collective-action 문제에서 단일 중앙통제만을 유일한 해결책으로 가정하지 않고,
여러 규모와 중심에서 실험·학습·상호조정하는 polycentric 접근을 분석.

Project 연결:
독립 comparator와 local experiment를 단순 중복비용으로 제거하지 않고
정보생산·오류탐지·복구 옵션으로 가치평가.

경계:
polycentricity도 coordination failure와 책임분산 비용을 가질 수 있음.

---

### T. cybernetics: regulator capacity and model limitation

대표:
- Ashby (1956), *An Introduction to Cybernetics*, Law of Requisite Variety
- Conant & Ashby (1970), DOI 10.1080/00207727008920220

재사용:
복잡한 disturbance를 제어하려는 regulator의 정보·response capacity에는 형식적 한계가 있으며,
좋은 regulator 정리는 명시된 조건 아래 regulator-model 관계를 분석한다.

Project 경계:
이를 "분산은 항상 우월" 또는 "중앙통제는 불가능" 같은 정치적 결론으로 직접 변환하지 않는다.

Project 연결:
```
environmental variety ↑
while independent response variety ↓
→ regulation blind spots may ↑
```

---

### U. response diversity → resilience

대표:
- Elmqvist et al. (2003), response diversity and resilience
- Mori et al. (2013), DOI 10.1111/brv.12004
- Leslie & McCabe (2013), DOI 10.1086/669563

재사용:
같은 기능을 수행하는 구성요소가 환경변화에 서로 다르게 반응하는 response diversity가
resilience와 renewal에 중요할 수 있음.

Project 연결:
option-space를 단순 대안 개수로 세지 않고
**independent response diversity**로 측정.

경계:
생태계 결과를 사회·AI 시스템에 직접 동일시하지 않고 비교모형으로만 사용.

---

## 2. 현재 보이는 상위 수렴 메커니즘

### 수렴 A — 권한 자기강화

```
critical resource / initial advantage
→ dependence
→ control-right concentration
→ switching/restoration cost
→ option reduction
→ incumbent persistence
```

### 수렴 B — 관측 자기강화

```
system action
→ environment adapts
→ adapted environment becomes data
→ system learns from self-shaped data
→ apparent empirical support
```

### 수렴 C — 평가 자기강화

```
metric becomes target
→ optimization toward metric
→ construct validity declines
→ metric still allocates reward/control
→ more optimization pressure
```

### 수렴 D — 합의 착시

```
cost of dissent / social pressure
→ public expression convergence
→ perceived consensus
→ further expression convergence
→ hidden alternatives become less observable
```

### 수렴 E — 증거 선택

```
research universe
→ selection/reporting/funding/publication filters
→ visible literature
→ policy/standard/consensus
→ incentives for future research
```

### 수렴 F — 반사실 소멸

```
choice
→ alternatives removed
→ alternative futures no longer generate observations
→ surviving path owns evidence stream
→ comparative superiority becomes harder to identify
```

---

## 3. 반수렴 / 복구 메커니즘

현재 여러 분야에서 반복되는 반대축:

```
alternative resource access
+ independent comparators
+ exploration reserve
+ response diversity
+ practical exit
+ effective voice
+ independent recovery
+ raw-data access
+ review / appeal
+ polycentric experimentation
+ reversible migration
+ countervailing capacity
→ concentration can remain bounded or reverse
```

이 역시 정답이 아니라 테스트할 결합이다.

---

## 4. 실제 수렴과 관측 수렴을 분리

최소 네 종류를 분리한다.

1. **Preference convergence** — actor 내부 선호가 실제로 가까워짐
2. **Behavior convergence** — 행동만 가까워짐
3. **Measurement convergence** — 측정값만 가까워짐
4. **Observation convergence** — 살아남아 관측되는 경로만 비슷해짐

따라서:

```
same observed behavior
!= same preference
!= same causal mechanism
!= same available option set
```

---

## 5. 선행연구 신뢰성 역추적

각 핵심 source는 가능하면 다음을 확인한다.

```
claim
→ original source
→ raw data availability
→ construct validity
→ measurement validity
→ analysis flexibility
→ preregistration / protocol
→ funding / COI
→ publication / selection filters
→ independent replication
→ contradictory evidence
→ correction / retraction
→ transfer validity
```

평가 상태:

- `DIRECTLY_OBSERVED`
- `REPLICATED_INDEPENDENTLY`
- `CONDITIONALLY_SUPPORTED`
- `CONFLICTING`
- `DISTORTION_EVIDENCE`
- `NONIDENTIFIED`
- `NOT_YET_AUDITED`

---

## 6. 포화 중단 기준

선행조사는 "논문을 더 못 찾을 때" 끝내지 않는다.

검색 라운드 r에서 새로 추가된 것을 센다.

```
N_mechanism(r)
N_counterexample(r)
N_boundary(r)
N_distortion_path(r)
N_measurement(r)
N_competing_model(r)
```

연속된 여러 독립 분야/검색라운드에서:

```
N_mechanism ≈ 0
N_counterexample ≈ 0
N_boundary ≈ 0
N_distortion_path ≈ 0
```

이고 핵심 가설의 판별조건이 더 이상 바뀌지 않을 때
`PRIOR_ART_SATURATION_CANDIDATE`로만 표시한다.

그 뒤에도 새로운 분야·시대·언어·데이터계보가 들어오면 다시 연다.

---

## 7. 현재 포화 판정

`NOT SATURATED`

이번 확장에서도 새 독립 축이 추가되었다:

- endogenous observation / performative prediction
- apparent consensus versus latent preference
- selection/reporting distortion
- polycentric counter-convergence
- requisite variety
- response diversity

따라서 현재 단계에서 선행조사를 종료하면 안 된다.

다음 검색의 우선영역:

1. distributed systems / Byzantine fault tolerance / correlated failure
2. antitrust / platform gatekeeping / interoperability
3. constitutional checks-and-balances / veto versus paralysis
4. organizational whistleblowing / retaliation / information suppression
5. intelligence-analysis failures / groupthink / red-team independence
6. evolutionary dynamics / monoculture / diversity collapse
7. safety engineering / common-cause failure / defense in depth
8. financial systemic risk / concentration / too-big-to-fail
9. scientific institution incentives / peer-review capture / citation cartels
10. AI evaluator independence / benchmark gaming / monitoring adaptation

