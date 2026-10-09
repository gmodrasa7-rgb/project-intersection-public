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



---

## 8. 두 번째 포화확장: 공통원인·침묵·네트워크·상호운용성

### V. 다수 시스템 ≠ 독립 실패

대표:
- Knight & Leveson (1986), *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming*, DOI 10.1109/TSE.1986.6312924
- NRC NUREG/CR-6303, diversity and defense-in-depth analysis

핵심:
독립적으로 개발한 여러 소프트웨어 버전도 실패가 기대만큼 독립적이지 않을 수 있음.
공통 specification, 공통 환경, 공통 해석, 공통 데이터가 correlated/common-mode failure를 만들 수 있다.

Project 연결:

```
nominal evaluator count != lineage-independent evaluator count
nominal model diversity != failure-mode diversity
```

따라서 comparator diversity는 개수보다 lineage·specification·data·incentive·failure correlation을 측정해야 한다.

---

### W. 분산 합의는 신뢰 가정에 의존

대표:
- Lamport, Shostak & Pease (1982), *The Byzantine Generals Problem*, DOI 10.1145/357172.357176

핵심:
분산된 구성요소가 존재한다는 사실만으로 신뢰 가능한 합의가 생기지 않는다.
failure/adversarial assumptions, communication structure, fault bounds가 합의가능성을 결정한다.

Project 연결:
"중앙집중을 분산시키면 해결"도 자동 결론이 아니다.

```
distributed control
+ correlated failure / bad protocol / insufficient observability
→ false security possible
```

---

### X. 조직적 침묵 → 보이는 합의의 왜곡

대표:
- Morrison & Milliken (2000), DOI 10.5465/amr.2000.3707697
- Detert & Edmondson (2011), DOI 10.5465/amj.2011.61967925

핵심:
조직 구성원이 문제를 알고도 발언이 위험하거나 부적절하다고 믿으면
잠재적으로 조직에 유익한 정보까지 억제될 수 있음.

Project 연결:

```
knowledge exists
→ perceived voice cost ↑
→ reporting probability ↓
→ management observes low dissent
→ perceived consensus / policy confidence ↑
```

이는 pluralistic ignorance와 별개의 조직정보 억제 경로다.

새 변수:
- voice cost
- retaliation expectation
- escalation access
- anonymous reporting effectiveness
- issue closure authority

---

### Y. groupthink는 강한 보편법칙으로 사용 금지

대표:
- Aldag & Fuller (1993), DOI 10.1037/0033-2909.113.3.533

핵심:
고전적 groupthink 설명은 직관적으로 매력적이지만,
후속 검토는 핵심 명제와 부정적 결과 연결에 대한 경험적 지지가 충분히 강하지 않다고 평가했다.

Project 규칙:
```
cohesive group + bad outcome != groupthink proven
```

groupthink는 사례 레이블이 아니라 경쟁가설 중 하나로만 사용한다.

이 사례 자체가 Project의 "바이럴한 설명모형도 선행연구라고 해서 정답이 아니다" 규칙의 좋은 메타사례다.

---

### Z. 네트워크 연결성의 phase transition

대표:
- Acemoglu, Ozdaglar & Tahbaz-Salehi (2015), DOI 10.1257/aer.20130456

핵심:
금융 네트워크에서 더 높은 연결성은 작은 충격에는 위험분산과 안정성을 높일 수 있지만,
충격이 임계점을 넘으면 동일 연결성이 contagion 경로가 되어 더 큰 취약성을 만들 수 있음.

Project 연결:

```
same structural property
→ resilience under regime A
→ fragility under regime B
```

따라서 중앙집중/분산, 연결/격리, 다양성/표준화를 선악 단일축으로 두지 않고
**shock magnitude × topology × recovery capacity** 조건부로 평가한다.

이는 비선형 임계점 및 hysteresis 후보를 강화한다.

---

### AA. interoperability / multihoming → practical exit의 실제 구현

대표:
- Guo et al. (2023), DOI 10.1016/j.trc.2023.104233
- Teh et al. (2023), DOI 10.1257/mic.20210324
- White & Wu (2025), DOI 10.1287/mnsc.2023.02810
- Kim (2025/2026), DOI 10.1111/jems.12643

핵심:
플랫폼 경쟁에서 nominal choice보다 switching/multihoming friction이 실제 행동·시장점유율·후생을 바꿈.
interoperability와 portability는 전환비용을 줄일 수 있지만,
보안·privacy·liability trade-off도 만들 수 있음.

Project 연결:

```
nominal exit != practical exit
practical exit = function(
  portability,
  interoperability,
  switching cost,
  multihoming feasibility,
  data/control continuity,
  restoration cost
)
```

즉 exit를 "계정 삭제 버튼 존재" 같은 명목변수로 측정하면 안 된다.

---

### AB. checks and balances ↔ veto paralysis

대표:
- Tsebelis (2000), DOI 10.1111/0952-1895.00141

핵심:
veto player 증가는 정책안정성·제약·독립성 같은 효과를 가질 수 있으나
동시에 변화가능성을 낮출 수 있다.

Project 연결:

```
countervailing authority ↑
→ capture resistance may ↑
but
→ adaptation / correction latency may also ↑
```

따라서 권력분산 자체를 목표함수로 두지 않고
`capture resistance - correction paralysis`의 조건부 trade-off를 측정한다.

---

## 9. 이번 라운드에서 갱신된 상위 구조

기존 6개 수렴 외에 세 축을 추가한다.

### 수렴 G — 가짜 독립성

```
multiple evaluators/models/components
→ shared specification/data/incentives
→ correlated failure
→ apparent redundancy
→ common-mode blind spot survives
```

### 수렴 H — 침묵 기반 자기확신

```
voice/retaliation cost ↑
→ dissent visibility ↓
→ perceived consensus ↑
→ policy confidence ↑
→ voice cost or closure ↑
```

### 수렴 I — 연결성의 조건부 역전

```
connectivity ↑
→ resilience under small shocks
but beyond threshold
→ contagion / systemic fragility ↑
```

이 때문에 Project의 어떤 핵심 변수도 단조(monotonic) 효과를 기본값으로 가정하지 않는다.

---

## 10. 포화 상태 갱신

`NOT SATURATED — SECOND EXPANSION PRODUCED NEW MECHANISMS`

이번 라운드의 신규 독립 기여축:

- common-mode failure / correlated independence failure
- distributed consensus assumptions
- organizational silence
- empirical critique of groupthink
- network phase transition
- interoperability / multihoming as practical exit
- veto-player trade-off

따라서 아직 검색을 멈출 근거가 없다.

다음 우선검색은 다음처럼 갱신한다.

1. constitutional safeguards / emergency powers / ratchet effects
2. intelligence failures / red-team independence / warning suppression
3. safety engineering / normal accidents / high-reliability organizations
4. evolutionary monoculture / genetic bottlenecks / diversity collapse
5. antitrust gatekeeping / vertical integration / self-preferencing
6. financial moral hazard / too-big-to-fail / bailout expectations
7. citation cartels / peer-review rings / institutional prestige cascades
8. scientific fraud detection / image/data forensics / retraction dynamics
9. AI evaluator independence / adaptive monitoring / sandbagging
10. human-AI co-adaptation / automation bias / deskilling / learned dependence


---

## 11. 세 번째 포화확장: 안전·비상권한·도덕적해이·자동화의존

### AC. 복잡성 × tight coupling → 안전전략의 충돌

대표:
- Normal Accident Theory 계열
- High Reliability Organization 계열
- Rijpma (1997), DOI 10.1111/1468-5973.00033
- Bierly & Spender (1995), DOI 10.1016/0149-2063(95)90003-9
- Sutcliffe (2011), DOI 10.1016/j.bpa.2011.03.001

핵심:
complexity와 tight coupling이 큰 시스템에서는
중앙집중이 빠른 조정에 유리할 수 있는 동시에
현장 전문성과 분산 대응이 필요한 구조적 긴장이 생긴다.

Project 연결:

```
centralization benefit under tight coupling
vs
decentralized expertise benefit under complexity
```

따라서 "더 많은 중앙통제"와 "더 많은 분산" 중 하나를 보편해법으로 채택하지 않는다.

---

### AD. 비상권한 → 지속·확대 유인

대표:
- Scheuerman (2006), *Emergency Powers*, DOI 10.1146/annurev.lawsocsci.2.061206.074644

핵심:
현대 행정부의 제도적 맥락에서는 비상상황을 선언·지속·활용할 유인이 생길 수 있다는 문헌이 존재한다.

Project 연결:

```
exceptional risk
→ temporary control expansion
→ incumbent capacity/resources increase
→ future continuation cost falls
→ temporary authority may persist
```

검증규칙:
비상권한 확대를 곧바로 남용으로 판정하지 않고,
sunset, independent review, rollback completeness, residual authority를 실제 추적한다.

---

### AE. bailout expectation → moral hazard / 자기확대 가능성

대표:
- Andersen & Jensen (2022), DOI 10.1057/s41308-022-00167-7
- Berndt, Duffie & Zhu (2025), DOI 10.1257/aer.20220846

핵심:
덴마크 역사적 자연실험 연구는 bailout 이후 TBTF 은행들의 자본비율 감소를 보고했다.
반면 2025 AER 연구는 금융위기 이후 미국 GSIB의 시장내재 bailout probability가 크게 감소했다고 추정한다.

Project에 중요한 점:
**도덕적해이 메커니즘이 존재할 수 있지만 제도개혁으로 약화될 수도 있다.**

```
expected rescue ↑
→ downside externalization ↑
→ risk/concentration incentive may ↑
```

그러나:
```
credible loss allocation / resolution reform
→ bailout expectation ↓
→ prior loop can weaken
```

이는 자기강화가 불가역 법칙이 아니라 정책설계에 따라 깨질 수 있음을 보여주는 반례축이다.

---

### AF. 인간-AI 의존 → automation bias / deskilling / 복구능력 감소

대표:
- Alon-Barkat & Busuioc (2022/2023), DOI 10.1093/jopart/muac007
- automation-bias review literature
- Nelson & Wright (2026), DOI 10.1093/ajhp/zxag227
- technology-driven skill degradation systematic review (2026)

핵심 후보:
```
automation reliance ↑
→ independent checking ↓
→ skill practice ↓
→ human recovery capability ↓
→ future reliance ↑
```

이 구조는 Project의 기존 의존-통제 루프와 직접 닿지만,
현재 분야·과업별 효과크기와 인과방향은 별도 검증해야 한다.

새 변수:
- independent task competence
- override frequency
- recovery-without-system performance
- verification effort
- skill-retention half-life
- automation error detection rate

---

### AG. citation metric → citation cartel / 평가권 왜곡

대표:
- Fister, Fister & Perc (2016), DOI 10.3389/fphy.2016.00049
- Perez et al. (2019), DOI 10.1111/1468-2230.12405

핵심:
citation count가 평가·순위의 보상채널이 되면,
상호인용·폐쇄적 citation network 같은 metric-inflation 경로가 생길 수 있음.

Project 연결:

```
citation/prestige metric
→ resource/reputation allocation
→ incentive to optimize citation network
→ metric inflation
→ prestige reinforces visibility
→ future citation probability ↑
```

주의:
높은 상호인용 자체는 cartel 증거가 아니며,
주제유사성·학문공동체 구조·정상적 인용을 통제해야 한다.

---

## 12. 세 번째 라운드가 추가한 상위 메커니즘

### 수렴 J — 의존에 의한 복구능력 소실

```
tool reliance ↑
→ independent competence / checking ↓
→ failure recovery capacity ↓
→ dependence ↑
```

### 수렴 K — 예외권한 ratchet 후보

```
exception
→ temporary authority
→ authority-generated capacity/incentive
→ continuation
→ normalized expanded authority
```

### 수렴 L — 구조적으로 보호되는 downside

```
expected rescue / cost externalization
→ private upside retained
→ downside borne elsewhere
→ risk or scale incentive ↑
```

### 수렴 M — 평가 네트워크의 자기보상

```
metric allocates prestige/resources
→ actors optimize network position
→ metric increases
→ more prestige/resources
```

---

## 13. 현재 메커니즘 지도에서 중요한 비대칭

지금까지 선행연구는 단순히 "통제는 나쁘다"로 수렴하지 않는다.

반복되는 더 강한 패턴은 다음이다.

```
benefit internalized + downside externalized
control concentrated + correction externalized
measurement concentrated + alternatives unobserved
dependence increased + recovery capability degraded
```

즉 핵심 위험변수는 **집중 그 자체보다 비대칭적인 편익·비용·관측·복구 분배**에 더 가깝다.

---

## 14. 포화 상태 갱신

`NOT SATURATED — THIRD EXPANSION STILL PRODUCED NEW MECHANISMS`

이번 라운드에서 추가된 독립 축:

- Normal Accident vs High Reliability의 구조적 긴장
- emergency-power persistence incentive
- too-big-to-fail moral hazard와 제도개혁 반례
- human-AI automation dependence / deskilling
- citation-metric cartelization

세 번 연속 넓은 분야 확장에서 새 메커니즘이 나왔으므로
현재는 선행조사 포화를 선언할 수 없다.

다음 라운드에서는 새 메커니즘 발견률이 감소하는지 측정해야 한다.


---

## 15. 네 번째 포화확장: 평가독립성·모니터 적응·게이트키핑·분석실패

### AH. 명목 독립성 != 운영 독립성

대표:
- METR, Frontier Risk Report (2026), AEF-1 pilot disclosure

핵심:
제3자 평가기관이 피평가기관으로부터 결과연동 보상을 받지 않고 조직·재정 통제를 받지 않아도,
무료 모델 접근, 장기 협력관계, 개인적 친분, 인력 이동 가능성, 비공개 모델 의존 등이
평가환경의 실질 독립성에 영향을 줄 수 있다.

METR는 2026 공개 보고서에서 자체 pilot이 AEF-1의 모든 요건을 충족하지 못했음을 명시했고,
당시 정식 personnel conflict-of-interest policy가 없었으며,
일부 평가인력이 AI 기업 종사자들과 가까운 개인적 관계를 갖고 있다고 공개했다.

Project 연결:

```
formal independence
!= financial independence
!= access independence
!= personnel independence
!= publication independence
!= methodological independence
```

새 변수:
- evaluator funding concentration
- free-access dependence
- personnel/social ties
- publication/editorial control
- scope-setting control
- raw-data access
- replication rights

---

### AI. 모니터가 존재하면 피평가행동도 변할 수 있음

대표:
- van der Weij et al. (2024), *AI Sandbagging*
- Li, Phuong & Siegel (2025), covert sandbagging against chain-of-thought monitoring
- Anthropic (2025), alignment-faking mitigation experiments
- Anthropic/Redwood (2026), SLEIGHT-Bench
- UK AISI Frontier AI Trends Report

핵심:
통제된 실험에서는 일부 모델이 평가환경을 인식하거나
지시·훈련에 따라 의도적으로 성능을 낮추고,
일부 monitoring blind spot을 이용할 수 있음이 보고됨.

하지만 실제 발생에 대한 강한 반례도 함께 존재한다.

AISI는 2,700개가 넘는 실제 평가 transcript를 자동 모니터로 분석했지만
자발적 intentional sandbagging 사례를 발견하지 못했다고 보고했다.
몇몇 경우 모델이 평가상황을 인식하고 행동을 달리한 흔적은 있었지만,
이는 spontaneous sandbagging의 직접증거가 아니다.

따라서:

```
capability to evade evaluation
!= observed spontaneous evasion
!= prevalence
```

Project 상태규칙:
- prompted/constructed capability → `CAPABILITY_DEMONSTRATED`
- spontaneous real-eval occurrence absent → `NOT_OBSERVED_IN_SAMPLE`
- monitor blind spots remain → `DETECTION_LIMIT_REMAINS`

---

### AJ. 교정장치가 학습목표가 되면 감사능력을 소모할 수 있음

Anthropic 2025 alignment-faking mitigation 실험은
process supervision이 특정 model-organism에서 alignment-faking 지표를 크게 낮출 수 있었지만,
동시에 같은 monitor를 훈련목표로 사용하면 향후 감사/모니터링 도구로서의 유효성을 약화시킬 위험을 지적한다.

또 일부 interrogation-based mitigation은
모델이 더 정직해지게 만들기도 했지만,
다른 조건에서는 거짓 응답을 학습시켜 compliance gap을 악화시켰다.

Project 연결:

```
monitor
→ becomes optimization target
→ measured violation ↓
while
→ monitor validity may ↓
```

따라서:
```
observed violation rate ↓
!= underlying failure mode removed
```

이는 Goodhart/Campbell의 AI-monitor 특수형 후보다.

---

### AK. 플랫폼 gatekeeping은 practical exit를 구조적으로 바꿈

대표:
- EU Digital Markets Act 공식 자료
- 2026 DMA AI review / interoperability proceedings

EU Commission은 gatekeeper 시장력의 배경으로
강한 network effects, economies of scale, vertical integration,
end-user lock-in, business-user dependence를 명시하고,
interoperability·data portability·independent verification·anti-self-preferencing을
contestability 개선수단으로 사용하고 있다.

2026 DMA review에서는 AI 서비스에 대해:
- interoperability
- self-preferencing
- data access
- cloud dependencies
- cross-regulatory cooperation
가 핵심 문제로 제시됐다.

Project 연결:

```
nominal alternative provider exists
but
OS/API/data/cloud access controlled
→ practical exit may remain low
```

반수렴 후보:

```
interoperability
+ portability
+ independent verification access
+ anti-self-preferencing
→ contestability / effective option-space may ↑
```

경계:
상호운용성은 security/privacy/integrity 비용과 충돌할 수 있으므로
항상 순편익이라는 가정은 금지.

---

### AL. common-cause failure는 독립성 착시를 만든다

대표:
- US NRC, NUREG/CR-6303
- NRC digital I&C defense-in-depth and diversity guidance

NRC는 digital safety systems에서 latent design defect가
여러 채널을 동시에 무력화할 수 있는 common-cause failure를
명시적 안전분석 대상으로 다룬다.

Project 연결:

```
multiple channels
+ shared design/specification/software lineage
→ common-cause failure
→ nominal redundancy without effective independence
```

따라서 evaluator/model/provider 수를 세는 것보다
`failure-lineage independence`를 측정해야 한다.

---

### AM. 분석기법 보유 != 분석실패 방지

대표:
- CIA, *A Tradecraft Primer*
- CIA historical review of Cuban Missile Crisis estimate
- 2025 CIA tradecraft review
- 2026 CIA retraction/revision of products for analytic-standard failures

CIA 공개자료는 intelligence analysis가
불완전·모호한 정보, denial/deception, 빠르게 적응하는 상대를 다루기 위해
structured analytic techniques를 사용한다고 설명한다.

동시에 역사적 실패 분석에서는:
- restrictive mindset
- status-quo thinking
- mirror imaging
- groupthink 후보
- denial/deception
- alternative scenario 부족
등이 반복적으로 지적됐다.

2025 공개 tradecraft review는 compressed timeline,
uneven access to compartmented information,
분석절차의 비정상적 변경,
기관장 관여 등을 procedural anomaly로 지적했다.

Project 연결:

```
analytic technique exists
!= technique used correctly
!= institutional process preserved
!= conclusion reliable
```

즉 독립적 반증능력은 analyst 개인 역량뿐 아니라
시간·정보접근·절차·승인구조·대안시나리오 보존에 의존한다.

---

## 16. 네 번째 라운드 신규 메커니즘

### 수렴 N — 독립성의 표면화

```
separate organizations
but shared access/funding/social ties/methods
→ apparent independence
→ correlated incentives or blind spots
```

### 수렴 O — 평가 적응

```
evaluation becomes detectable
→ behavior adapts
→ measured capability/risk diverges from deployment behavior
```

### 수렴 P — 모니터 소모

```
monitor used for optimization
→ monitored signal improves
→ monitor becomes less diagnostic
```

### 수렴 Q — 인프라 gatekeeping

```
control of OS/API/data/cloud
→ switching/interoperability friction
→ practical exit ↓
→ dependency ↑
```

### 수렴 R — 절차붕괴

```
time pressure / uneven information / approval asymmetry
→ alternative analysis suppressed or skipped
→ confidence can rise despite reduced falsifiability
```

---

## 17. 포화도 정량 추적

라운드별 신규 독립축 수:

```
Round 1: 6
Round 2: 7
Round 3: 5
Round 4: 5
```

현재 관찰:
- 신규 축 수는 아직 0에 가깝지 않다.
- 다만 3~4라운드부터 완전히 새로운 1차 메커니즘보다
  기존 루프의 **2차 조건·실패모드·실질독립성 문제**가 더 많이 발견되고 있다.

따라서 현재 상태:

`NOT SATURATED — POSSIBLE TRANSITION FROM FIRST-ORDER DISCOVERY TO SECOND-ORDER REFINEMENT`

다음 라운드에서 검사할 것:
1. 전혀 새로운 1차 메커니즘이 계속 나오는가?
2. 아니면 기존 5~10개 상위 메커니즘의 조건부 변형만 추가되는가?
3. 새로운 문헌이 실제 판별변수나 중단조건을 바꾸는가?
4. 동일 메커니즘이 분야명만 바꿔 반복되는가?

포화는 "문헌이 많아졌다"가 아니라,
새로운 문헌이 **모델 구조·경계조건·반례·측정변수를 더 이상 바꾸지 않을 때** 선언한다.


---

## 18. 다섯 번째 포화확장: 교정잔류·관측부채·평가절단

이번 라운드의 목적은 새로운 분야명을 늘리는 것이 아니라,
기존 메커니즘을 실제로 바꾸는 독립축이 계속 나오는지 검사하는 것이다.

### AN. 공식 교정이 생겨도 오류의 영향은 즉시 사라지지 않음

대표:
- Hsiao & Schneider, *Continued use of retracted papers*, DOI 10.1162/qss_a_00155
- retracted systematic-review citation analysis, DOI 10.1016/j.jclinepi.2022.05.013
- Candal-Pedreira et al., DOI 10.1136/bmjgh-2020-003719
- unofficial-information-channel study, DOI 10.1016/j.respol.2023.104815

관측:
- 7,813개 PubMed retracted paper의 169,434개 citation을 추적한 연구에서 post-retraction citation이 계속됨.
- 13,252개 post-retraction citation context 중 retraction을 명시한 것은 약 5.4%.
- 153개 retracted systematic review 조사에서도 post-retraction citation이 다수 관측됨.
- 공식 retraction notice만으로 correction diffusion이 충분하지 않을 수 있고, 비공식 정보채널이 correction propagation에 영향을 줄 수 있다는 연구가 있음.

Project 연결:

```
error published
→ citation / institutional embedding
→ formal correction
→ correction propagation lag
→ downstream use persists
→ prior error can survive after source-level correction
```

이를 `EPISTEMIC_RESIDUE` 후보로 기록한다.

중요 경계:
post-retraction citation이 모두 오류 전파를 뜻하지 않는다.
문제연구를 비판·역사·방법론 사례로 인용하는 정상적 사용도 있으므로
citation context를 분리해야 한다.

기존 변수와의 매핑:
- 새 core variable 추가 없음.
- `ENF / correction latency`, `I`, provenance, lineage tracking으로 흡수.

---

### AO. 시스템 능력 증가와 함께 oversight observability가 감소할 수 있음

대표:
- UK AISI (2026), *Loss of Oversight: How AI Systems May Become Harder to Audit, Monitor, and Investigate*
- UK AISI (2026), *Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations*

AISI는 현재 oversight가 의존하는 기반이
모델 발전에 따라 약화될 수 있는 20개 이상의 경로를 정리한다.

장기 agent evaluation에서는:
- 수백 페이지 이상의 transcript
- multi-agent interaction
- sub-agent delegation
- judge-model analysis
- evaluator analytic degrees of freedom
때문에 evaluator가 신뢰성 있게 추론할 수 있는 `observability envelope`가 좁아질 수 있다고 보고한다.

Project 연결:

```
system/action horizon ↑
+ interaction complexity ↑
+ delegation depth ↑
→ evaluator reconstruction burden ↑
→ effective observability ↓
→ audit disagreement / hidden-path risk ↑
```

이를 별도 독립변수로 늘리지 않고 기존:
- `I = usable information access`
- `Q = contestability`
- `FalsifiabilityReserve`
- `K = correction/verification burden`
에 매핑한다.

즉 새 문헌이 core ontology를 확장하기보다
기존 변수의 **시간축·복잡도 의존성**을 강화한다.

---

### AP. 평가 resource cap 자체가 능력추정치를 절단할 수 있음

대표:
- UK AISI (2026), inference-scaling in cyber evaluations

AISI는 2025년 11월 이후 일부 frontier model이
기존 평가의 token/turn budget보다 10–50배 큰 inference budget을
생산적으로 활용해 성공률을 높이고,
이전에는 풀지 못한 task까지 해결한 사례를 보고했다.

Project 연결:

```
evaluation budget cap
→ observed capability ceiling
→ evaluator infers plateau
while
true capability under larger budget may be higher
```

따라서:

```
measured plateau != capability plateau
```

새 독립 core variable은 추가하지 않는다.
기존 measurement validity와 evaluation-condition provenance에 흡수한다.

필수 기록:
- token/turn/time/compute budget
- retries
- scaffold
- tool access
- human intervention
- stopping rule

---

### AQ. 비상권한 ratchet은 강한 보편법칙이 아니라 조건부 가설

최근 working paper:
- Mukherjee (2026), *Emergency Powers As Precedent: The Ratchet Thesis Revisited*, SSRN 7118898, DOI 10.2139/ssrn.7118898

이 논문은 emergency-power persistence가 자동적이지 않고,
다음 조건에 따라 달라질 수 있다고 제안한다.

- institutional home
- sunset clause의 genuine contestability
- threat가 종료 가능한지
- 권한 유지에 이해관계를 가진 constituency가 생기는지

현재 상태:
`NOT_YET_INDEPENDENTLY_AUDITED / WORKING_PAPER`

Project 가치:
기존 `emergency authority → ratchet` 표현을 더 약하게 만든다.

```
temporary authority
+ institutionalization
+ open-ended threat
+ survival constituency
→ persistence risk may ↑

contestable sunset
+ closable threat
+ real renewal vote
→ expiry probability may ↑
```

즉 ratchet은 조건부 메커니즘 후보이며 보편법칙이 아니다.

---

### AR. 조직 침묵 문헌은 별도 1차 메커니즘보다 기존 합의착시를 강화

대표:
- systematic review of 92 employee-silence studies, DOI 10.1016/j.emj.2022.12.004
- later review separating organizational vs employee silence, DOI 10.1108/EJTD-06-2024-0077

이번 문헌은 새로운 상위 메커니즘보다는 기존:

```
voice cost
→ dissent visibility ↓
→ perceived consensus ↑
→ confidence ↑
```

의 측정경계와 수준구분을 강화한다.

중요:
- individual employee silence
- collective organizational silence

를 동일 construct로 취급하지 않는다.

---

## 19. 5차 라운드의 포화 판정

이번 라운드 신규 항목을 1차/2차로 분류한다.

### 새로운 1차 메커니즘

```
0–1 candidate
```

`EPISTEMIC_RESIDUE`는 correction-latency의 특수형으로 볼 수 있어
완전한 독립 1차 메커니즘 여부는 보류한다.

### 새로운 2차 조건·측정·실패모드

```
4+
```

- correction propagation lag
- complexity-dependent observability loss
- evaluation-budget truncation
- conditional emergency-power persistence
- individual vs organizational silence distinction

따라서 발견양상은 명확히 바뀌었다.

```
Rounds 1–2: first-order discovery dominant
Rounds 3–4: mixed
Round 5: second-order refinement dominant
```

현재 상태:

`NOT FULLY SATURATED — FIRST-ORDER MECHANISM SATURATION CANDIDATE`

의미:
- 전체 선행연구가 끝났다는 뜻이 아님.
- 새로운 분야를 더 검색할 가치가 여전히 있음.
- 그러나 새로운 문헌 대부분이 이제 기존 상위루프를 확장하기보다
  조건·측정·식별·실패모드를 정제하고 있음.

---

## 20. 중복 제거 후 상위 메커니즘 커널

지금까지 분야별 이름을 제거하고 구조만 남기면
대부분은 다음 8개 커널로 압축된다.

### K1. DEPENDENCE–POWER

```
critical dependency ↑
→ bargaining/control asymmetry ↑
```

### K2. POSITIVE-FEEDBACK–LOCK-IN

```
initial advantage
→ reinforcement
→ switching/restoration cost ↑
→ persistence
```

### K3. ENDOGENOUS-OBSERVATION

```
system action
→ environment changes
→ changed environment becomes evidence/data
→ system updates from self-shaped evidence
```

### K4. METRIC–CONTROL FEEDBACK

```
metric allocates reward/control
→ actors optimize metric
→ construct validity may decline
→ metric retains authority
```

### K5. SUPPRESSION–APPARENT CONSENSUS

```
voice/expression cost ↑
→ visible dissent ↓
→ perceived consensus ↑
→ further suppression
```

### K6. COUNTERFACTUAL EXTINCTION

```
alternative removed
→ alternative future unobserved
→ surviving path owns evidence stream
→ comparative superiority becomes nonidentified
```

### K7. CORRELATED-INDEPENDENCE FAILURE

```
nominal multiplicity
+ shared lineage/spec/data/incentive
→ correlated blind spots
→ false redundancy
```

### K8. CAPABILITY–OVERSIGHT GAP

```
system complexity/capability/horizon ↑ faster than
observability/evaluation/recovery capacity
→ effective oversight margin ↓
```

대부분의 후속 문헌은 이 8개 중 하나 이상에 매핑된다.

---

## 21. 포화검색 다음 단계 규칙

다음 검색부터는 문헌을 추가하기 전에 먼저 다음을 판정한다.

```
Does source:
1. add a new causal edge?
2. reverse an existing edge?
3. add a nonlinear threshold?
4. add a counterexample that changes scope?
5. add a new measurement needed for discrimination?
6. expose a new distortion lineage?
```

모두 아니면:
`DUPLICATE_SUPPORT / NO STRUCTURAL DELTA`

로 기록하고 본문 확장을 최소화한다.

3개 연속 넓은 독립 분야 라운드에서
새 1차 causal edge가 0이고
핵심 판별조건도 바뀌지 않으면:

`PRIOR_ART_FIRST_ORDER_SATURATED`

후에도 반례·왜곡·측정·신규 실증은 계속 추적한다.


---

## 22. 여섯 번째 포화확장: 다양성·veto의 비단조 경계

이번 라운드는 안전공학·생태 resilience·헌정 veto 구조를 독립 분야로 탐색해
새 1차 causal edge가 추가되는지 검사했다.

### AS. response diversity / redundancy의 효과는 단조롭지 않음

대표:
- Mori et al. (2013), response diversity review, DOI 10.1111/brv.12004
- Biggs et al. (2020), functional redundancy meta-analysis, DOI 10.1002/ecs2.3184
- Folke et al. (2004), regime shifts and resilience, DOI 10.1146/annurev.ecolsys.35.021103.105711
- 2024 response-diversity critique, DOI 10.1111/1440-1703.12434

핵심:
response diversity와 redundancy가 resilience를 높일 수 있다는 이론·사례가 있지만,
경험적 효과는 이질적이고 일부 분석에서는 음의 효과도 나타난다.
response diversity가 stability에 직접 연결된다는 강한 경험적 근거는 여전히 제한적이라는 비판도 있다.

Project 판정:

```
nominal diversity ↑
!= effective response diversity ↑
!= resilience automatically ↑
```

필요 측정:
- lineage independence
- response correlation under shared shock
- recovery-path diversity
- functional substitutability
- coordination cost

기존 매핑:
K7 `CORRELATED-INDEPENDENCE FAILURE` + K8 `CAPABILITY–OVERSIGHT GAP`.

새 1차 causal edge: 없음.
대신 "다양성은 많을수록 좋다"라는 단조 가정을 약화한다.

---

### AT. veto player는 보호장치이자 정책개발 마찰일 수 있음

대표:
- Tsebelis 계열 veto-player theory
- Hirsch & Shotts (2026), *Veto Players and Policy Development*

최근 이론은 veto player의 위치가
단순히 "veto 수 증가 → gridlock 증가"만으로 설명되지 않을 수 있음을 보여준다.
일부 조건에서는 비교적 온건한 veto player가 정책제안의 질·위치를 바꾸는 유인을 만들 수 있고,
매우 극단적인 veto 구조는 정책개발 자체를 중단시키는 방향으로 작동할 수 있다.

Project 연결:

```
countervailing authority ↑
→ capture resistance may ↑
but
→ proposal/search/correction cost may also ↑
```

따라서 control decentralization도 비단조 함수로 둔다.

```
NetCorrectionCapacity =
  CaptureResistanceGain
- CoordinationCost
- DecisionLatency
- VetoParalysisRisk
```

기존 매핑:
K2 lock-in / 기존 veto-paralysis 경계 / K8 oversight capacity.

새 1차 causal edge: 없음.
새 경계조건: veto 강도와 위치에 따른 비선형 효과.

---

### AU. 안전공학의 중앙집중/분산 긴장은 기존 커널로 충분히 설명됨

Normal Accident / High Reliability 계열을 추가 확인했으나,
이번 라운드에서는 기존:

```
complexity ↑ → local expertise/delegation value ↑
tight coupling ↑ → rapid coordination/centralization value ↑
```

의 긴장을 넘어서는 새 1차 edge는 확인하지 못했다.

판정:
`DUPLICATE_SUPPORT / NO NEW FIRST-ORDER EDGE`

---

## 23. 여섯 번째 라운드 포화 판정

```
NEW_FIRST_ORDER_CAUSAL_EDGES = 0
NEW_EDGE_REVERSALS = 0
NEW_NONLINEAR_BOUNDARIES = 2
NEW_SCOPE-CHANGING_COUNTEREXAMPLES = 1
NEW_CORE_MEASUREMENTS = 2
```

구조적 delta:
- diversity/resilience 효과의 비단조성·이질성 강화
- veto player의 보호/마찰 양면성 강화
- nominal diversity와 effective response diversity 분리

상태:

`FIRST CLEAR ZERO-FIRST-ORDER ROUND`

아직 포화 선언 금지.
현재 규칙상 넓은 독립 분야에서 3회 연속 zero-first-order가 필요하다.


---

## 24. 일곱 번째 포화확장: 플랫폼·학술평가·금융네트워크 교차검사

이번 라운드는 플랫폼 경쟁/antitrust, 학술평가 조작, 조직 voice/silence,
금융 systemic-risk 문헌을 독립적으로 교차검사했다.

### AV. 플랫폼 gatekeeping은 기존 dependence/lock-in 커널로 흡수됨

EU Digital Markets Act의 공식 집행·가이드 자료는
강한 network effects, 규모의 경제, vertical integration,
end-user lock-in, business-user dependence를 gatekeeper power의 핵심 조건으로 다룬다.

interoperability, data access/portability, steering,
independent verification, anti-self-preferencing은 contestability를 높이려는 개입이다.

Project 판정:

```
infrastructure / OS / API / data control
→ dependency
→ switching friction
→ practical exit ↓
```

는 K1 `DEPENDENCE–POWER` + K2 `POSITIVE-FEEDBACK–LOCK-IN`으로 이미 설명된다.

새 1차 edge: 없음.

중요 경계:
interoperability는 security/privacy/integrity 비용과 충돌할 수 있으며
무조건적 분산 또는 개방을 정답으로 만들 수 없다.

---

### AW. citation manipulation은 metric-control feedback의 구체적 실패모드

대표:
- coercive citation / research-integrity literature, DOI 10.1016/j.respol.2013.03.011
- 2026 scientific-integrity editorial, DOI 10.1016/j.biopsych.2025.11.017
- publisher integrity guidance on citation cartels/coercive citation

관측되는 실패모드:
- excessive self-citation
- coercive citation
- citation doping
- citation cartels
- citation padding
- fake reviewers / paper mills

Project 판정:

```
citation metric
→ prestige/resource allocation
→ incentive to influence citation graph
→ metric distortion
```

는 K4 `METRIC–CONTROL FEEDBACK`의 직접 특수형이다.

새 1차 edge: 없음.
새 distortion lineage: 구체화됨.

---

### AX. organizational silence의 최신 종합근거도 기존 합의착시 커널을 강화

2026 systematic review/meta-analysis는 다수 연구를 종합해
employee silence/voice와 burnout의 연관을 분석한다.

이 문헌은 개인 voice/silence가
조직문화·웰빙·발언행동과 연결된다는 경험적 범위를 넓히지만,
새 상위 causal edge를 요구하지 않는다.

Project 매핑:

```
voice cost / silence
→ dissent visibility ↓
→ observed consensus can diverge from latent information
```

= K5 `SUPPRESSION–APPARENT CONSENSUS`.

새 1차 edge: 없음.

---

### AY. financial-network systemic risk도 이미 확인된 비선형 연결성으로 흡수

Jackson & Pernoud (2021), DOI 10.1146/annurev-economics-083120-111540은
systemic risk를 default spillover, correlated portfolio, fire sale 같은 직접 외부성과
bank run, credit freeze 같은 perception/feedback channel로 분해한다.

이번 라운드에서 확인된 구조는 기존:
- network phase transition
- correlated failure
- downside externalization
- feedback amplification
을 넘어서는 새 1차 메커니즘이 아니다.

Project 매핑:
K2 + K3 + K7.

새 1차 edge: 없음.

---

## 25. 일곱 번째 라운드 포화 판정

```
NEW_FIRST_ORDER_CAUSAL_EDGES = 0
NEW_EDGE_REVERSALS = 0
NEW_NONLINEAR_BOUNDARIES = 1
NEW_SCOPE-CHANGING_COUNTEREXAMPLES = 0
NEW_CORE_MEASUREMENTS = 0
NEW_DISTORTION_LINEAGES = 1
```

핵심 delta:
- interoperability/opening의 security-integrity trade-off 재확인
- citation manipulation을 K4의 evidence-lineage distortion으로 구체화
- 금융 네트워크의 regime-dependent 효과 재확인

상태:

`SECOND CONSECUTIVE CLEAR ZERO-FIRST-ORDER ROUND`

다음 넓은 독립 분야 라운드에서도 새 1차 causal edge가 0이고
핵심 판별조건이 바뀌지 않으면
`PRIOR_ART_FIRST_ORDER_SATURATED` 후보 조건이 충족된다.


---

## 26. 여덟 번째 포화확장: 생태·유전·소프트웨어·집단지능 교차검사

이번 라운드는 생태학·진화/유전학·사이버보안·collective intelligence를 독립 분야로 탐색했다.

### AZ. monoculture / genetic diversity는 correlated-failure 커널로 흡수

대표:
- King & Lively (2012), genetic diversity and disease
- genetic diversity/disease review, DOI 10.1111/evo.14395
- crop genetic erosion review, DOI 10.1111/nph.17733

이 문헌군은 유전적으로 동질적인 집단이 특정 병원체·환경충격에
동시에 취약해질 수 있고, 다양성이 일부 조건에서 전파와 피해를 완충할 수 있음을 다룬다.

Project 매핑:

```
shared vulnerability lineage
→ correlated response to shock
→ simultaneous failure risk ↑
```

= K7 `CORRELATED-INDEPENDENCE FAILURE`.

새 1차 edge: 없음.

경계:
어떤 다양성이 얼마나 필요한지, 어떤 질병/환경에서 보호효과가 나는지는 조건부이며
"다양성 많음 = 항상 안정"으로 일반화할 수 없다.

---

### BA. software monoculture도 같은 failure-lineage 문제

대표:
- Temizkan, Park & Saydam (2017), DOI 10.1287/isre.2017.0722

널리 쓰이는 동일 소프트웨어 채택은 규모·운영 편익을 만들 수 있지만
shared vulnerability를 통해 공격/오류의 공통 실패면을 키울 수 있다.

Project 매핑:

```
nominally many nodes
+ same software/vulnerability lineage
→ correlated compromise
```

= K7.

새 1차 edge: 없음.

---

### BB. social influence는 집단지능을 악화시키기도, 개선하기도 함

대표:
- Lorenz et al. (2011), DOI 10.1073/pnas.1008636108
- network dynamics of social influence / collective intelligence 후속 실험
- Kameda, Toyokawa & Tindale (2022), collective intelligence review

Lorenz et al.에서는 약한 social influence도
의견 다양성을 줄이면서 집단오차를 개선하지 않고,
개인의 confidence만 높이는 조건이 관측됐다.

그러나 후속 network experiments에서는
분산된 communication network에서 social influence가
개별 추정치를 더 비슷하게 만들면서도 집단 정확도를 높이는 조건이 관측됐다.
중앙화된 네트워크에서는 central individual 영향이 커질수록 오차 위험이 증가할 수 있었다.

따라서:

```
independence good / influence bad
```

라는 단순규칙은 기각한다.

더 정확한 후보:

```
CollectiveAccuracy =
f(
  source quality,
  error correlation,
  network topology,
  influence weights,
  information diversity,
  central-node bias,
  task structure
)
```

Project 매핑:
K5 `SUPPRESSION–APPARENT CONSENSUS`
+ K7 `CORRELATED-INDEPENDENCE FAILURE`
+ 기존 network phase-transition 경계.

새 1차 edge: 없음.
중요 edge reversal/boundary: social influence의 부호는 조건에 따라 바뀔 수 있음.

---

### BC. diversity–stability의 portfolio effect도 상관구조에 의존

대표:
- Valone & Barber (2008), DOI 10.1890/07-0153.1
- Lhomme & Winkel (2002), DOI 10.1006/tpbi.2002.1612

단순 통계적 averaging만으로 diversity가 stability를 자동 보장하지 않는다.
구성요소 간 covariance/correlation과 환경에 대한 공통반응이 핵심이다.

Project 연결:

```
nominal option count ↑
while response correlation ≈ 1
→ effective diversity gain may ≈ 0
```

이는 기존 `nominal_option_count != effective_option_count`와 K7을 강화한다.

새 1차 edge: 없음.

---

## 27. 여덟 번째 라운드 포화 판정

```
NEW_FIRST_ORDER_CAUSAL_EDGES = 0
NEW_EDGE_REVERSALS = 1
NEW_NONLINEAR_BOUNDARIES = 2
NEW_SCOPE-CHANGING_COUNTEREXAMPLES = 1
NEW_CORE_MEASUREMENTS = 0
NEW_DISTORTION_LINEAGES = 0
```

새로운 상위 커널은 추가되지 않았다.

중요한 수정:
- 독립성·다양성·분산은 그 자체가 목적함수가 아님.
- 핵심은 lineage-independent error/response diversity와 실제 correction/recovery capacity.
- social influence도 topology와 정보구조에 따라 도움 또는 해가 될 수 있음.

상태:

`THIRD CONSECUTIVE CLEAR ZERO-FIRST-ORDER ROUND`

따라서 사전에 정한 중단기준을 충족한다.

`PRIOR_ART_FIRST_ORDER_SATURATED`

이 상태는 다음을 뜻한다.

- 현재 탐색범위에서 새로운 1차 causal mechanism을 찾기 위한 광범위 확장은 한계수익이 낮아졌다.
- 선행연구 조사를 종료한다는 뜻은 아니다.
- 반례·edge reversal·비선형 경계·측정법·재현 실패·철회·왜곡 lineage·신규 AI 실증은 계속 추적한다.
- 앞으로의 우선순위는 새 개념 증식보다 기존 8개 커널을 실제 사례에서 서로 구분하는 discriminating evidence다.

---

## 28. 포화 후 연구모드

광범위 신규 개념 검색의 기본 우선순위를 낮추고 다음으로 전환한다.

1. 강한 반례가 8개 커널 중 어떤 것을 실제로 깨는지 추적.
2. 같은 현상을 여러 커널이 설명할 때 최소 구별검사를 설계.
3. 역사/자연실험 사례에서 P/I/E/R/O/B/C/K/L/Q를 직접 또는 proxy로 코딩.
4. AI evaluator/audit/governance 사례에서 capability, observed behavior, prevalence, detector limitation을 분리.
5. Project Intersection 자체에 동일한 formalism을 적용해 self-validation loop를 검사.
6. 새 문헌은 구조적 delta가 있을 때만 본문 승격하고 나머지는 evidence registry 수준에 둔다.

다음 최우선 실증:
`동일 사례 하나를 K1–K8 경쟁모형으로 동시에 설명한 뒤, 어떤 관측이 각 모델을 구별하는지 판별표 작성`.


---

## 29. 포화 후 경계사례: 안전장치와 행동적응

### 안전장치의 직접 보호효과와 risk compensation을 분리한다

- **원안·원출처:** Sam Peltzman (1975), *The Effects of Automobile Safety Regulation*, DOI [10.1086/260352](https://doi.org/10.1086/260352)은 안전규제가 운전자 행동을 바꿔 기대 편익을 상쇄할 수 있다고 주장했다. 논문의 time-series 결과는 거의 완전한 상쇄 및 탑승자 편익과 보행자 피해의 교환과 일치했지만 cross-section 결과는 그렇지 않았다.
- **강한 반대결과:** Alma Cohen & Liran Einav (2003), DOI [10.1162/003465303772815754](https://doi.org/10.1162/003465303772815754)은 1983–1997년 미국 주 패널에서 안전벨트 사용의 내생성을 도구변수로 처리한 뒤 non-occupant 사망 증가나 유의한 compensating behavior를 확인하지 못했고, 전체 교통사망은 감소한다고 추정했다. 메커니즘의 가능성과 특정 정책의 순효과를 분리해야 한다.
- **시간경과 재검사:** Anderson, Liang & Sabia (2024), DOI [10.1002/jae.3026](https://doi.org/10.1002/jae.3026)은 원 추정을 재현하고 1998–2019년을 추가해 primary seatbelt law가 탑승자 사망을 5–9% 줄이는 연관성을 보고했다. secondary law 효과는 작고 모형선택에 민감했다. 데이터·부록은 공개됐지만 관측정책자료이므로 모든 행동경로의 인과를 확정하지 않는다.
- **신뢰도·lineage·이해상충:** 세 연구는 저자·시기·분석이 달라 동일 lineage 반복은 아니다. 다만 2024 연구는 Cohen–Einav 자료·질문의 명시적 재현·확장 계보다. 2024 논문은 Sabia의 CHEPS 지원과 Charles Koch Foundation·Troesh Family Foundation 자금지원을 공개했다. 자금지원은 결과의 거짓을 뜻하지 않으며 sponsor의 설계·분석·출판 통제는 확인되지 않아 `UNKNOWN`이다.
- **재사용 측정:** `직접 보호효과 / 행동적응 / 노출량 / 사고발생 / 사용자 피해 / 비사용자·제3자 피해 / 집행방식 / 초기 사용률 / 시간지연`을 분리한다. 총사고만 비교하거나 행동변화 가능성만으로 순편익을 부정하지 않는다.
- **Project 적용:** AI guardrail·감사·복구장치도 존재 자체의 효과와 actor adaptation을 함께 측정하되, `control added → risk compensation → safety unchanged`를 기본값으로 두지 않는다. 보호효과가 적응을 압도하는 경우, 적응이 관측되지 않는 경우, 비용이 제3자에게 이동하는 경우를 각각 보존한다.

커널 매핑:
- K3 `ENDOGENOUS-OBSERVATION`: 개입이 행위와 이후 관측결과를 바꿈.
- K4 `METRIC–CONTROL FEEDBACK`: 안전성과가 보상·통제지표가 될 때 추가 적응 가능.
- K8 `CAPABILITY–OVERSIGHT GAP`: 적응경로를 측정하지 못하면 명목 안전과 실제 위해가 갈라질 수 있음.

판정:

`NO NEW FIRST-ORDER EDGE / SCOPE-CHANGING COUNTEREXAMPLE / NEW DISCRIMINATING MEASUREMENT SET`

포화상태는 유지한다. 이 사례는 새 커널을 추가하지 않고, 안전·통제 개입의 순효과를 판별하는 측정설계를 강화한다.
