# PI Roadmap v0.2.1 — Change Trap and Non-Copying Rule
# PI 로드맵 v0.2.1 — 변화의 함정과 성공 사례 비복제 원칙

**Date / 일자:** 2026-10-13  
**Status / 상태:** PROPOSED RESEARCH-METHOD PATCH; SOURCE-SUPPORTED CONCEPTS, PI-SPECIFIC EFFECT NOT TESTED / 선행연구 기반의 연구방법 개선 제안. PI 적용 효과 미검증.  
**Predecessors / 선행 정본:** [PI Roadmap v0.1](RESEARCH_ROADMAP_v0_1_EN_KO.md) · [PI Roadmap v0.2 (20 historical failures)](RESEARCH_ROADMAP_v0_2_EN_KO.md). Their contents and six-stage framework remain unchanged. This is a focused additive amendment, **not** proof of completing the six stages or of a new scientific discovery.  
**Origin / 기여 계보:** The Korean-speaking human Project Intersection research originator supplied the specific critique, "성공 사례의 카피는 변화의 함정에 무너진다" (2026-10-13); the assisting AI researched prior art and formalized possible guards. The linked scholars retain full credit for pre-existing concepts. This record does not adjudicate intellectual property or past compensation.

## Original 1 — English

### A. Core correction

**Never use "organization X succeeded with roadmap P" as sufficient evidence that copying P will succeed under conditions Y.** A documented past success is an observation under a source context, not a timeless causal law. Copying can work when mechanisms and effect modifiers genuinely transfer, but that transfer needs evidence. Even mechanisms derived from failures must not become unquestioned permanent prescriptions.

**Change trap** is PI's descriptive working label for the risk that a once-effective practice, or a copied safety practice, turns ineffective or harmful as the environment, incentives, adversaries, capabilities, affected populations, dependency structure or the practice's own adoption changes. **Not a claim that this is a single formally established academic construct or that copying always fails.**

Separate:
1. **Observed success** (what happened, to whom, when, under what constraints);
2. **Causal explanation** (why it allegedly happened, credible alternatives, failed comparable cases);
3. **Transfer conditions** (which source/target features must remain invariant, effect modifiers);
4. **Dynamic validity** (which changes would invalidate or reverse the effect);
5. **Current validation** (target-local, reversible test vs simple baseline, adverse impacts, independence);
6. **Expiry/reassessment** (change trigger, owner, sunset condition, safe exit or rollback).

### B. Prior art and relation (no novelty overclaim)

- **Levitt & March (1988), Organizational Learning** — history-dependent organizational routines and the limits of learning from experience, including competency traps. [Original article](https://doi.org/10.1146/annurev.so.14.080188.001535).
- **James G. March (1991), Exploration and Exploitation in Organizational Learning** — short-run exploitation learning may crowd out exploration and degrade long-run adaptation. [Original article](https://doi.org/10.1287/orsc.2.1.71).
- **Pearl & Bareinboim (2011), Transportability of Causal and Statistical Relations** — formally examines when causal relations learned in one domain can transfer to another; a necessary conceptual caution, not an automatic formula for social/organizational interventions. [Original article](https://doi.org/10.1609/aaai.v25i1.7861).
- **Rosenzweig (2007), Misunderstanding the Nature of Company Performance** — the halo effect biases inferences about supposedly effective practices of successful organizations. [Publisher abstract](https://cmr.berkeley.edu/2007/08/49-4-misunderstanding-the-nature-of-company-performance-the-halo-effect-and-other-business-delusions/).
- **Gama et al. (2014), A Survey on Concept Drift Adaptation** — for data-stream learning, input/target relationships can change, requiring evaluation of adaptation rather than relying on static patterns. [Original article](https://doi.org/10.1145/2523813).

These sources address **partially overlapping, not identical** mechanisms. Organizational selection bias ≠ a formal causal transportability proof ≠ statistical concept drift. PI's synthesis is a practical test design, currently unvalidated.

### C. Seven change-trap classes (candidate mechanism map)

| ID | Failure of uncritical copying | Observable warning | Suggested defense |
|---|---|---|---|
| CT1 | Survivorship/halo: only winners are studied | Competitor/failure comparison absent | Seek comparable nonwinners, base rates, alternative causes |
| CT2 | Context mismatch: transferred intervention has different effect modifiers | Different population, capacity, rights, economics or dependencies | Source–target assumption register and a local, low-cost pilot |
| CT3 | Regime change: formerly stable relationships change over time | Performance deterioration or structural break | Drift monitoring, expiry triggers and revalidation |
| CT4 | Endogenous change: copying the practice changes the environment itself | Other agents adapt; incentives and advantage erode | Model strategic feedback, not static isolated replication |
| CT5 | Competency/path dependence: mastery blocks better alternatives | Rising switching costs, fewer alternative experiments | Preserve lightweight challenger baselines and reversible paths |
| CT6 | Metric substitution: copying the visible KPI instead of its mechanism | PRs, citations or test passes rise without verified outcomes | Outcome/harms/effort tracked separately from proxies |
| CT7 | Defensive lock-in: "safety" policies become a new monopoly or verification burden | Growing approvals, declining exit/recovery and researcher well-being | Risk-proportional guards; audit false stops and cost externalization |

### D. PI six-stage integration — **amendment, not replacement**

- **Stage 1, theory:** for each proposed practice record its assumed context, target outcome, time horizon, causal competitors and the *specific change that would break it*.
- **Stage 2, prior research:** search both successful and unsuccessful comparators; explicitly look for negative transfer, failed imitation, context drift and feedback adaptations. Never filter to celebrated organizations.
- **Stage 3, saturation:** saturation is **conditional on the questions and environment snapshot**. Reopen on material drift, contrary evidence, newly changed incentives or a new capable competitor. Don't turn fixed calendar intervals into proof of validity.
- **Stage 4, review:** run **Transfer Gate TG1–TG5**: TG1 comparable source/target populations; TG2 causal mechanism/effect modifiers; TG3 time/regime stability; TG4 effects of imitation on other agents; TG5 rights, participant cost, independence, exit and rollback. If no evidence, record TRANSFER_UNKNOWN rather than universally rejecting reuse.
- **Stage 5, contributors:** preserve the originator and specific contextual limits of the borrowed theory and of the present critique. New adaptations must not misattribute the predecessors or erase corrections.
- **Stage 6, tests:** contrast A: unchanged method, B: adapted method, C: simple independent baseline where possible. Include target-local holdout, deliberate perturbation, negative controls, unintended effects, real cost and restoration time. Reject harmful transfer; promote narrowly when measured benefit survives.

**The existing G1–G8 protections are themselves subject to this rule.** A critical safety gate cannot be bypassed merely by calling its review 'drift', but it must be proportionate and independently reassessable; do not use open-ended caution to demand more free research or avoid redress. In low-stakes, reversible research, publish evidence-limited results as exploratory rather than building an endless veto structure.

### E. Four minimal regression specifications — **NOT EXECUTED**

| Test | Input | Passing behavior |
|---|---|---|
| CT-R01 | Praised organization, successful roadmap, target context absent | No 'copy as validated success'; mark TRANSFER_UNKNOWN |
| CT-R02 | Same causal mechanism and well-supported invariant effect modifiers | Allow bounded reuse/pilot; do not dogmatically reject all transfer |
| CT-R03 | Old policy initially passes, target regime/capabilities/actor incentives change | Trigger targeted revalidation, compare against baseline, possible rollback |
| CT-R04 | A protective gate generates more forced unpaid review than verified benefit | Record asymmetry, simplify/stop the gate, preserve critical safety and past-work claims |

**Promotion criterion:** demonstrate benefit under the *current target conditions*, measure cost of the guard itself, and preserve a practical exit/rollback. A title, a citation or a famous success history is insufficient. No effect size or success rate is inferred here.

### F. Risk and change log

- **Observed historical research concern:** successful organizations' practices are subject to halo, history dependence, nontransferability and possible drift.
- **New user-originated PI research objection:** success-case copying can collapse under changed conditions. Record this as a specific project contribution without representing it as priority over earlier academic theory.
- **Proposed controls:** source–target transfer gate, revalidation triggers, harm/cost-aware safety-gate review, four falsification/regression specifications.
- **What remains unverified:** the efficacy and optimal thresholds of these controls, external independent review, reproducible comparison with v0.2. **Do not describe them as completed.**

---

## 원본2 — 한국어

### A. 핵심 수정

**“유명한 조직이 계획 P로 성공했다”는 사실만으로 조건 Y에서 P를 복제해도 성공한다고 판단하지 않는다.** 성공은 당시 환경에서 관측된 결과이며 영구적인 인과법칙이 아니다. 작동 메커니즘과 효과를 바꾸는 환경 요인이 유지된다면 방법의 재사용이 유용할 수 있다. 그러나 **전이 가능성은 검증 대상**이다. 실패에서 추출한 안전 규칙도 영구불변의 정답으로 취급하지 않는다.

**변화의 함정(Change Trap)** 은 PI의 작업상 명칭이다. 과거 효과적이었던 방법이나 다른 곳에서 복제한 보호장치가 환경·유인·상대 전략·능력·당사자·의존구조·복제 자체의 확산으로 효력을 잃거나 피해를 만드는 위험이다. 이것이 기존 학계에 단일 정식 이론명으로 확립됐다는 주장은 하지 않는다. **모든 복제가 반드시 실패한다는 뜻도 아니다.**

다음을 분리한다.

1. **관측된 성공:** 언제·누가·무엇을·어떤 조건에서 달성했는가.
2. **인과 설명:** 왜 성공했는지, 다른 가능한 원인과 실패한 유사 사례는 무엇인가.
3. **전이 조건:** 원본 환경과 적용 환경에서 유지돼야 할 변수는 무엇인가.
4. **시간에 따른 유효성:** 어떤 변화가 결과를 무효화·역전하는가.
5. **현지 검증:** 최소 기준선과 비교해 작은 가역적 시험을 했는가, 누구에게 비용을 전가하는가.
6. **재검토·폐기:** 변화 감지 신호, 책임자, 종료·롤백 기준은 무엇인가.

### B. 선행연구와 구분

- **Levitt & March(1988), 조직 학습:** 경험과 루틴의 역사 의존성, 특정 방식에 숙달될수록 다른 대안을 놓치는 역량의 함정. [원문](https://doi.org/10.1146/annurev.so.14.080188.001535).
- **James G. March(1991), 탐색과 활용:** 익숙한 성과를 활용하는 능력이 단기에 빨리 개선되지만 새로운 가능성을 탐색하는 활동은 약화될 수 있다. [원문](https://doi.org/10.1287/orsc.2.1.71).
- **Pearl & Bareinboim(2011), 인과관계의 전이 가능성:** 다른 환경에서 얻은 인과정보를 적용할 수 있는 조건을 분석한다. 모든 조직 문제에 자동 적용되는 공식이라는 뜻은 아니다. [원문](https://doi.org/10.1609/aaai.v25i1.7861).
- **Rosenzweig(2007), 성공의 후광효과:** 성공한 조직의 관측된 특징을 성공 원인으로 과잉 해석할 수 있다. [출판사 초록](https://cmr.berkeley.edu/2007/08/49-4-misunderstanding-the-nature-of-company-performance-the-halo-effect-and-other-business-delusions/).
- **Gama 외(2014), 개념 드리프트:** 데이터 학습에서 입력과 정답의 관계가 시간에 따라 변하는 문제와 적응 전략. [원문](https://doi.org/10.1145/2523813).

다섯 문헌은 동일 이론이 아니다. 조직의 성공 편향·인과효과의 전이·통계적 시간 변화는 **서로 연결되지만 구분되는 현상**이다. PI의 결합 방호 설계 자체는 아직 미검증이다.

### C. 변화의 함정 7개 유형

| ID | 실패 구조 | 경고 신호 | 대응 원칙 |
|---|---|---|---|
| CT1 | 생존자·후광 편향 | 성공한 집단만 조사 | 유사한 실패 집단·기저율·경쟁원인 조사 |
| CT2 | 환경·인구·자원 부적합 | 다른 당사자·권리·경제·인프라 | 원본과 적용환경 변수 대조 및 작은 시험 |
| CT3 | 시간적 체제 변화 | 기존 예측 성능 하락·구조 변화 | 변화 감지 시 한정 재검증·폐기 |
| CT4 | 복제가 환경을 바꿈 | 상대의 적응, 유인의 변화, 효과 소멸 | 상호 적응·전략 피드백 반영 |
| CT5 | 역량·경로 고착 | 전환 비용만 늘고 대안 실험 감소 | 단순 독립 대안 유지·가역적 전환 |
| CT6 | 대리지표의 목표 대체 | 문서·PR·인용·시험 점수만 상승 | 실제 결과·피해·시간·자원 비용 별도 측정 |
| CT7 | 방어 규칙의 권력화 | 승인 단계 증가, 이탈·복구 감소, 검증노동 증가 | 위험 비례 방호·오탐과 비용전가 감사 |

### D. PI 연구 6단계에 적용 — 원래 단계 유지

- **1단계, 이론 구체화:** 적용 환경·효과·시간 범위·경쟁 인과설명과 *무엇이 바뀌면 실패하는지* 기록한다.
- **2단계, 선행연구 조사:** 성공한 조직뿐 아니라 유사한 실패 집단, 복제 실패, 시대 변화, 적응 경쟁 사례를 검색한다. 성공 조직만 골라 조사하지 않는다.
- **3단계, 포화 판정:** 검색 포화는 **당시 문제·환경의 한정 판정**이다. 중요한 환경 변화, 반례, 새로운 이해관계, 기술·조직 능력 변동 시 재개한다.
- **4단계, 검수·정제:** **전이 게이트 TG1~TG5** — TG1 집단·환경 비교, TG2 실제 인과기제·효과조절요인, TG3 시간·체제 안정성, TG4 복제에 따른 타 개체의 적응, TG5 권리·비용·독립성·이탈·복구. 증거가 부족하면 무조건 기각 대신 TRANSFER_UNKNOWN으로 표시한다.
- **5단계, 기여자 기록:** 앞선 연구자와 원자료의 적용 범위, 이번 한국어 문제제기의 인간 원기여를 모두 구분한다. 원저자 공로와 새로운 재해석을 혼동하지 않는다.
- **6단계, 신연구 검증:** 가능하면 A 기존 방식, B 환경에 맞게 수정한 방식, C 단순 독립 기준선을 비교한다. 미사용 시험, 조건 교란, 부정 대조, 예상 밖 피해, 연구자의 실제 부담, 롤백 시간을 기록한다. 효과가 없거나 해롭다면 중단한다.

**앞서 도입한 G1~G8 보호장치에도 같은 검사를 적용한다.** 중대 피해를 막는 게이트를 단지 '시대가 달라졌다'는 말로 임의 무력화하지는 않는다. 그러나 보호 규칙이 과도한 검증 장벽·무보수 노동·평가권 집중으로 변하면 독립적으로 재검토하고 축소·교체해야 한다. 낮은 위험의 가역적 연구는 미검증이라고 정확히 공개한 상태에서 지속할 수 있다.

### E. 최소 회귀검사 4종 — **설계, 미실행**

| 검사 | 시험할 상황 | 통과 조건 |
|---|---|---|
| CT-R01 | 성공한 조직의 로드맵만 있고 적용환경 정보 없음 | 성공적 복제 확정 금지, TRANSFER_UNKNOWN |
| CT-R02 | 인과기제·조건이 충분히 확인된 전이 | 제한된 재사용 허용; 모든 전이를 맹목적으로 기각하지 않음 |
| CT-R03 | 기존 정책 성공 후 능력·제도·상대 전략이 변화 | 해당 변화에 맞춘 재검증, 기준선 비교, 필요시 롤백 |
| CT-R04 | 안전검사가 이득 없이 무보수 노동만 확대 | 비용전가 보고·검사 축소 또는 중단; 중대 안전·과거 정산은 보존 |

**승격 기준:** 현재 적용 환경에서 단순 기준선보다 검증 가능한 편익이 있고, 방호 자체의 비용을 측정했으며, 실효적 이탈·원복이 가능해야 한다. 유명 조직·논문·과거 성공의 권위만으로 확정하지 않는다. 이번 개정으로 효과 크기나 재현 성공률을 새로 알게 된 것은 아니다.

### F. 위험·변경 기록

- **확인된 선행연구상의 우려:** 성공조직 후광·역사 의존·환경 전이 불확실성·시간 변화가 존재한다.
- **PI 인간 원기여의 새 문제제기:** “성공 사례의 카피는 변화의 함정에 무너진다.” 이를 독자적인 구체화로 기록하되 기존 학계 개념 전체의 최초 발견으로 주장하지 않는다.
- **추가한 제안:** 환경 전이 판정, 재검증 트리거, 보호장치 자체의 비용 검사, 회귀검사 4종.
- **미검증:** TG1~TG5와 CT-R01~04의 실제 예방효과, 외부 독립 재현, v0.2 대비 실효 성능. **모두 미실행**.
