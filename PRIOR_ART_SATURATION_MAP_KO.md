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
