# PI Roadmap v0.2.2 — Hidden Route, Changed Ground: Focused Prior-Art Recheck
# PI 로드맵 v0.2.2 — 변한 길·보이지 않는 위험: 선행연구 재조사

**Date / 날짜:** 2026-10-13  
**Status / 상태:** PRIMARY-SOURCE/ABSTRACT SYNTHESIS + PROPOSED APPLICATION; NOT AN EXECUTED PI SAFETY EXPERIMENT. / 기관 공식자료·학술 출처/초록 확인 및 PI 적용 제안. 실제 예방 효과 검증·독립 재현·자동 검사 구현은 미실행.  
**Existing canonical baseline / 기존 정본 보존:** [v0.1](RESEARCH_ROADMAP_v0_1_EN_KO.md) · [v0.2 (20 historical cases)](RESEARCH_ROADMAP_v0_2_EN_KO.md) · [v0.2.1 change trap](PI_ROADMAP_CHANGE_TRAP_V0_2_1_EN_KO.md). **No replacement of the six research stages, funding/privacy/evidence rules or earlier versions.**  
**Human contribution / 인간 기여:** The human research originator gave the concrete counterexample: a once-successful fastest shortcut could now be blocked or its subsoil near collapse while appearing unchanged. This investigation identifies earlier independent research in multiple fields and does not claim novelty for those earlier concepts. / 한국어 원기여자의 ‘과거 성공한 빠른 지름길이 겉모습은 그대로여도 지반 붕괴 직전이거나 차단됐을 수 있다’는 구체 반례와 단순화 요구를 보존한다. 앞선 학문적 공로는 원저자에게 귀속한다.

## Original 1 — English

### 1. The narrow problem and strongest correction

**Past fast ≠ current open; current open ≠ structurally safe; visible inspection ≠ knowledge of hidden condition.**

Three distinct failure mechanisms were conflated in earlier language:
- **Changing state:** obstruction, loading, incentives, opponents and system dependencies can change after prior success.
- **Hidden state / limited sensing:** failure margin can erode or have been wrongly estimated from the start, and available inspection may miss it.
- **Decision/lock-in:** institutional or model incentives may continue to select the familiar path even after the evidence base changes.

This is not a new universal law. **A successful method may still be best**; the claim is that history alone cannot establish its present fitness, and inspections also need to be evaluated rather than assumed infallible.

**Important factual distinction:** The US I-35W bridge collapse illustrates an original design error that remained undetected, combined with load increases and incomplete load-rating/inspection attention. It must **not** be misreported as proof that hidden material deterioration alone caused that collapse.

### 2. Prior-art crosscheck (22 source entries, different evidence types)

| ID | Originating source (follow for precise limitations) | Specific pre-existing insight |
|---|---|---|
| P01 | [Levitt & March (1988)](https://doi.org/10.1146/annurev.so.14.080188.001535) | History-dependent routines; experience and copying do not guarantee transferable learning. |
| P02 | [March (1991)](https://doi.org/10.1287/orsc.2.1.71) | Exploiting old certainties can crowd out adaptation and long-run exploration. |
| P03 | [Hannan & Freeman (1984)](https://doi.org/10.2307/2095567) | Structural inertia affects organizations' capacity for change. |
| P04 | [Staw (1976)](https://doi.org/10.1016/0030-5073(76)90005-2) | An experimental investment setting illustrates commitment escalation; later replications require caution. |
| P05 | [Arthur (1989)](https://ideas.repec.org/a/ecj/econjl/v99y1989i394p116-31.html) | Increasing returns can lock adoption onto paths not necessarily efficient. |
| P06 | [Pearl & Bareinboim (2014)](https://doi.org/10.1214/14-STS486) | Transport of causal effects requires explicit source–target assumptions. |
| P07 | [Lucas (1976)](https://doi.org/10.1016/S0167-2231(76)80003-6) | Policy change can alter the structural relationships a model estimates. |
| P08 | [Gama et al. (2014)](https://doi.org/10.1145/2523813) | Concept drift changes input–target relations, motivating renewed validation. |
| P09 | [Ovadia et al. (2019)](https://papers.neurips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html) | Predictive confidence can be poorly calibrated under dataset shift. |
| P10 | [Sculley et al. (2015)](https://mlanthology.org/neurips/2015/sculley2015neurips-hidden/) | Hidden dependencies, feedback and system-level technical debt accrue even after early ML success. |
| P11 | [Rasmussen (1997)](https://doi.org/10.1016/S0925-7535(97)00052-0) | Safety performance shifts as multiple actors adapt under pressure near boundaries. |
| P12 | [Dekker (2011)](https://www.routledge.com/Drift-into-Failure-From-Hunting-Broken-Components-to-Understanding-Complex/Dekker/p/book/9781409422211) | Routine successful local decisions can accumulate into complex-system failure. |
| P13 | [Woods (2015)](https://doi.org/10.1016/j.ress.2015.03.018) | Resilience includes adaptive capacity, not merely restoring a prior state. |
| P14 | [US FHWA (2001)](https://www.fhwa.dot.gov/publications/research/nde/01020.cfm) | Visual bridge inspection reliability varies; critical defects can evade visual methods. |
| P15 | [US NTSB, I-35W (2008)](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx) | Latent design defect, added loads, and excluded component checks interacted. |
| P16 | [NASA CAIB (2003)](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20030066167.pdf) | Prior success displaced engineering evidence while organizational warning channels failed. |
| P17 | [Stentz (1994)](https://publications.ri.cmu.edu/optimal-and-efficient-path-planning-for-partially-known-environments) | D* plans and updates routes as unknown or changed obstacles appear. |
| P18 | [Koenig & Likhachev (2002)](https://publications.ri.cmu.edu/d-lite) | D* Lite reuses previous search efficiently while updating a changed map. |
| P19 | [Kurniawati (2022)](https://doi.org/10.1146/annurev-control-042920-092451) | POMDP planning explicitly accounts for noisy observation and uncertain action effects. |
| P20 | [Howard (1966)](https://doi.org/10.1109/TSSC.1966.300074) | Information value depends on how uncertainty reduction changes consequences. |
| P21 | [Iannacone et al. (2019)](https://doi.org/10.12783/shm2019/32270) | Bridge inspection choice considers sensing quality, direct/indirect cost and value of information. |
| P22 | [Amodei et al. (2016)](https://arxiv.org/abs/1606.06565) | AI safety distinguishes distribution shift, reward hacking, safe exploration and side effects. |

**Evidence quality:** P14–P16 are limited institutional studies/inquiries about particular bridge/shuttle systems, not general event frequencies. P17–P19 are computational/robotics theories and surveys, not proof of organizational risk outcomes. P20–P21 formalize and apply decision-analysis principles but do not certify the PI decision threshold. P01–P13 and P22 have different theoretical/empirical scopes and should not be combined into a single verified causal chain. Some full texts are access-limited; titles/abstracts and public institutional records were checked, not a systematic review of every result or contrary paper. The Staw (P04) effect should not be treated as uniform or irreproachable; replication outcomes are mixed.

### 3. The simplest useful model

Let the **actual route state** at time `t` be `S_t`; observations/test outputs be `O_t` and a chosen action be `A_t`. The observer sees an imperfect representation, not the state itself: `O_t = h(S_t) + noise` (a *conceptual* observation model; not a calibrated empirical equation). Even when visual appearance is unchanged, `S_t` may differ or original design faults may be hidden. Past success at `t0` constrains belief about the past; it does not establish present passability or safety at `t1`.

**Four possible actions:** (a) USE the route with scope-limited confidence, (b) INSPECT or test a decision-changing unknown, (c) DETOUR to an available alternative, (d) HOLD/STOP an irreversible hazardous operation. Always compare **the harm/cost borne by different parties**, not only operator time.

When probabilities are credibly estimable, a practical comparison considers `direct cost + test cost + estimated consequential loss + delay + recovery cost` for each option. Under poorly bounded tail-risk and model error, do **not** manufacture probabilities or claim that expected value settles the case; record plausible harms and use risk limits and reversibility. A test with substantial false-negative risk is not proof of safety.

**Inspection is not free**: if likely test results cannot change the decision, or an available detour is plainly safer/cheaper, a huge inspection campaign may be inferior. Conversely, if the downside is large/irreversible, immediate deployment on old success data is unjustified. These are decision-analytic **candidate rules**, not universally calibrated thresholds.

### 4. What is genuinely additive to v0.2.1?

v0.2.1 already named transferability, drift, strategic response and past success bias. This recheck adds **a different missing variable**: whether a risk-relevant present state is *observable with the methods used*, and whether obtaining better information is worth its cost **relative to detour or safe cessation**.

Minimal new three-gate proposal:
- **HP1 Detectability:** What can the current test actually see, what can it miss, and how can latent original defects differ from new deterioration? UNKNOWN if untested.
- **HP2 Decision-changing information:** Would different plausible inspection outcomes actually change USE/DETOUR/HOLD? Assess cost, false negatives, timeliness, impacted parties and alternative routes.
- **HP3 Time-bound route choice:** Based on current conditions, choose least harmful sufficiently justified route (USE/INSPECT/DETOUR/STOP), state expiry/change triggers and keep options to recover. No single default action for all stakes.

Integration into unchanged stages: **1** define route, harm and unknown hidden state; **2** survey failure/inspection and counterexamples; **3** record evidence scope plus unknown-state coverage; **4** apply HP1–3 with adversarial alternatives; **5** preserve attribution/cost/decision authority; **6** test a narrow pilot with false-negative and unnecessary-block outcomes, and reversible controls.

### 5. Regressions to implement later (not executed)

| ID | Test input | Required response |
|---|---|---|
| HP-R01 | Old route repeatedly succeeded; hidden bearing capacity silently decreases | Do not certify safety from success/appearance; flag unseen condition |
| HP-R02 | Route visibly blocked; old route remains shortest in stale map | Replan instead of following the historic route |
| HP-R03 | Visual inspection passes; known limited sensitivity to critical flaw | Mark residual UNKNOWN, not SAFE_PROVEN |
| HP-R04 | Testing is very costly and cannot change the best available detour decision | Avoid futile verification burden; choose justified detour |
| HP-R05 | Reusable route actually remains safe/cheapest under current verified conditions | Allow reuse; avoid blanket anti-copy prohibition |
| HP-R06 | Extra safety gate shifts uncompensated cost onto a vulnerable contributor | Stop/simplify unjustified review, preserve separate past-work redress |

**No claim of automated tests, field-effect size or safety guarantee.** The most useful next experimental target is whether HP1–3 catch failures missed by v0.2.1 with manageable false alarms and researcher effort; this remains NOT EXECUTED.

---

## 원본2 — 한국어

### 1. 최소 명제와 이전 해석의 누락

**과거에 빠른 길 ≠ 지금 열려 있는 길. 지금 열려 있는 길 ≠ 구조적으로 안전한 길. 눈으로 확인한 길 ≠ 내부 상태까지 알고 있는 길.**

차이가 나는 세 문제를 구분한다.

- **상태 변화:** 장애물·하중·경쟁·이해관계·시스템 연결이 바뀐다.
- **숨은 상태와 관측 한계:** 안전여유가 감소했거나, 최초 설계부터 결함이 숨어 있어도 검사에서 놓칠 수 있다.
- **선택 고착:** 새로운 위험이 발생해도 익숙한 선택이 조직·AI의 보상체계 때문에 반복될 수 있다.

기존 방법을 모두 버리자는 뜻이 아니다. **현재도 가장 나은 길일 수 있지만 과거 기록만으로 증명되지 않는다. 검사도 오류와 비용이 있으므로 무조건 믿지 않는다.**

**사례의 원인 구분:** 미국 I-35W 교량 사고는 숨은 원래 설계결함, 추가 하중, 부품별 평가·검사의 누락이 결합한 사례다. **내부 재료가 자연히 부식해 무너졌다는 근거로 둔갑시키지 않는다.**

### 2. 재조사한 선행연구 22건 — 독립 학문과 원자료 구분

| ID | 원자료·저자 | 직접 관련되는 기존 지식 |
|---|---|---|
| P01 | [Levitt & March (1988)](https://doi.org/10.1146/annurev.so.14.080188.001535) | 조직의 역사의존적 학습·타 조직 사례 복제 한계 |
| P02 | [March (1991)](https://doi.org/10.1287/orsc.2.1.71) | 과거 성공의 활용이 미래 대안 탐색을 밀어낼 수 있음 |
| P03 | [Hannan & Freeman (1984)](https://doi.org/10.2307/2095567) | 조직 구조적 관성이 환경 변화에 대한 적응을 제약 |
| P04 | [Staw (1976)](https://doi.org/10.1016/0030-5073(76)90005-2) | 투자 의사결정 실험의 몰입 확대; 재현의 불확실성을 별도 검토 |
| P05 | [Arthur (1989)](https://ideas.repec.org/a/ecj/econjl/v99y1989i394p116-31.html) | 역사적 채택 우위가 비효율적 경로 고착으로 이어질 수 있음 |
| P06 | [Pearl & Bareinboim (2014)](https://doi.org/10.1214/14-STS486) | 환경 간 인과효과 전이에는 명시적 조건이 필요 |
| P07 | [Lucas (1976)](https://doi.org/10.1016/S0167-2231(76)80003-6) | 행동규칙의 변화가 추정된 관계 자체를 바꿀 수 있음 |
| P08 | [Gama et al. (2014)](https://doi.org/10.1145/2523813) | 입력과 결과의 관계 변화에 따른 기존 모형 무효화 |
| P09 | [Ovadia et al. (2019)](https://papers.neurips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html) | 환경이 바뀌면 모델의 확신값도 부정확할 수 있음 |
| P10 | [Sculley et al. (2015)](https://mlanthology.org/neurips/2015/sculley2015neurips-hidden/) | 초기 성공 뒤에도 숨은 의존성·피드백·유지비용 누적 |
| P11 | [Rasmussen (1997)](https://doi.org/10.1016/S0925-7535(97)00052-0) | 압력과 적응 속에 안전 경계에 접근하는 동적 구조 |
| P12 | [Dekker (2011)](https://www.routledge.com/Drift-into-Failure-From-Hunting-Broken-Components-to-Understanding-Complex/Dekker/p/book/9781409422211) | 개별적으로 합리적이던 일상적 판단이 시스템 위험으로 누적 |
| P13 | [Woods (2015)](https://doi.org/10.1016/j.ress.2015.03.018) | 회복뿐 아니라 놀라운 변화에 대응하는 적응 능력 보존 |
| P14 | [US FHWA (2001)](https://www.fhwa.dot.gov/publications/research/nde/01020.cfm) | 교량 육안검사 결과 편차와 결함 탐지 한계 |
| P15 | [US NTSB, I-35W (2008)](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx) | 잠재 설계결함·추가하중·검사 대상 누락의 결합 |
| P16 | [NASA CAIB (2003)](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20030066167.pdf) | 과거 성공이 기술 검증을 대체하고 조직 경고망이 약화 |
| P17 | [Stentz (1994)](https://publications.ri.cmu.edu/optimal-and-efficient-path-planning-for-partially-known-environments) | 미지·변동 환경에서 장애물 발견 시 경로 재탐색 |
| P18 | [Koenig & Likhachev (2002)](https://publications.ri.cmu.edu/d-lite) | 이전 계산을 활용하되 변한 지도에 맞춰 경로 갱신 |
| P19 | [Kurniawati (2022)](https://doi.org/10.1146/annurev-control-042920-092451) | 불완전 관측·불확실한 행동 결과 아래의 의사결정 |
| P20 | [Howard (1966)](https://doi.org/10.1109/TSSC.1966.300074) | 검사가 결정을 개선하는 가치와 실제 비용을 비교 |
| P21 | [Iannacone et al. (2019)](https://doi.org/10.12783/shm2019/32270) | 교량 검사 방식별 정보·오차·직간접 비용 비교 |
| P22 | [Amodei et al. (2016)](https://arxiv.org/abs/1606.06565) | AI의 분포이동·보상해킹·안전탐색·부작용 구분 |

**증거 수준:** P14~P16의 교량·우주사고 자료는 해당 대상의 기록이지 모든 사고의 발생률이 아니다. P17~P19의 경로계획·부분관측 연구를 인간 조직에 그대로 전이할 수 없다. P20~P21은 정보가치와 검사비용을 판단하는 방법을 제시할 뿐 PI의 수치 기준을 입증하지 않는다. 나머지도 학문·측정·표본·재현의 범위가 서로 다르며 하나의 확정 인과사슬이 아니다. 일부 유료 원문은 공개 초록 및 공식 문헌정보로 확인했으며 전수 문헌검토 완료가 아니다. P04 몰입 확대 연구의 재현성은 혼합된 결과가 있어 무조건적인 법칙으로 간주하지 않는다.

### 3. 최소 구체화

시점 `t`에서 **길의 실제 상태**를 `S_t`, 우리가 얻은 관측·검사 결과를 `O_t`, 행동 선택을 `A_t`라 하자. `O_t = h(S_t) + 잡음`은 *개념적 관측식*이며 실험으로 검증된 정확한 계측 모델이 아니다.

외관이 같아도 `S_t`는 변했거나 원래부터 미확인 결함이 있었을 수 있다. 과거 `t0`의 성공이 현재 `t1`의 안전을 보장하지 않는다.

행동은 네 가지다.

1. **사용(USE):** 현재 범위에서 근거가 충분한 경우 진행.
2. **확인(INSPECT):** 검사 결과가 실제 판단을 바꿀 만하면 제한적 검사.
3. **우회(DETOUR):** 안전하고 비용이 수용 가능한 다른 경로가 있으면 전환.
4. **보류·중단(STOP):** 되돌리기 어려운 중대 위험을 충분히 제한할 수 없으면 위험 행동 중지.

비교 항목은 행동별 **직접 비용 + 검사비용 + 잠재 피해 + 지연 + 복구 비용**이며 각 항목의 *편익자와 부담자*를 분리한다. 위험 확률을 신뢰성 있게 추정할 수 없으면 임의 수치를 넣지 말고 최악 시나리오·되돌림 가능성·허용 피해한도를 명시한다. 실패를 놓치는 검사는 안전증명서가 아니다.

**‘모든 길을 다시 검사’도 정답이 아니다.** 검사 결과가 판단을 바꿀 수 없거나 안전한 우회로가 더 싸면 장황한 재검사 자체가 피해가 된다. 반대로 고위험·비가역적 실행이라면 과거 성공만 믿고 진입해서는 안 된다. 이는 검증할 **의사결정 원칙 제안**이지 보편적으로 측정된 임계값이 아니다.

### 4. 이전 버전에서 새로 남은 것

v0.2.1에서 이미 환경변화·전이가능성·타 개체 적응·역량고착을 다뤘다. 이번 새로운 잔여 문제는 **현재의 실제 위험을 현행 검사가 볼 수 있는가**와 **검사로 더 알아내는 것이 우회·중단보다 비용·피해 면에서 유리한가**이다.

이를 세 게이트로 축약한다.

- **HP1 관측가능성:** 지금 사용한 검사가 무엇을 볼 수 있고 무엇을 놓치는가. 애초부터 존재한 결함과 나중에 생긴 악화를 구분한다.
- **HP2 검사의 판단가치:** 검사 결과가 바뀌면 실제 선택도 바뀌는가. 시간·검사비·오탐·미탐·대안 비용·당사자 피해를 본다.
- **HP3 시점별 경로 선택:** 현재의 근거로 사용·확인·우회·중단을 비교하고 유효기한·변화 감지·롤백·실효적 이탈 가능성을 기록한다.

기존 여섯 단계 적용: **1** 상태·피해·숨은 변수 정의 → **2** 조사방법과 실패·검사 한계 조사 → **3** 탐색 포화 범위와 관측 사각지대 기록 → **4** HP1~3와 경쟁 경로 대조 → **5** 원저자·교정자·실제 비용·판정권 계보 보존 → **6** 미탐·과도한 중단·복구·연구자 비용을 측정하는 작은 시험. **여섯 단계는 그대로 유지한다.**

### 5. 제안 회귀검사 — 자동화·실증 미실행

| ID | 투입할 반례 | 적합한 처리 |
|---|---|---|
| HP-R01 | 반복 성공한 지름길의 지지력이 보이지 않게 낮아짐 | 성공 이력만으로 안전 선언 금지 |
| HP-R02 | 옛 지도에선 최단 경로지만 현재 차단됨 | 옛 길 고집하지 않고 재탐색 |
| HP-R03 | 육안검사 통과했으나 핵심 결함의 미탐 가능성 높음 | 잔여 미지 위험 표시, 검사가 곧 안전 아님 |
| HP-R04 | 재검사 비용이 높고 결과와 무관하게 우회가 합리적 | 불필요한 검증노동 중단 |
| HP-R05 | 현재 상태도 검증되어 기존 길이 실제로 더 나음 | 무조건적인 성공사례 거부 대신 제한적 재사용 |
| HP-R06 | 보호장치가 취약한 기여자에게 무보수 교정비용 전가 | 절차 축소·중단, 과거 기여의 정산은 별도 유지 |

**미실행 상태:** 이 여섯 반례는 설계안이다. v0.2.1 대비 HP1~3의 오류탐지율·미탐·과잉차단·복구품질·검증 비용을 평가하기 전까지 ‘예방효과 입증’이라 말하지 않는다.

### 6. 최종 한 줄

> **과거의 성공은 길의 이력이고, 현재의 선택에는 보이지 않는 상태와 우회 가능성까지 포함해야 한다.**

이 원칙도 새로운 증거가 나오면 수정해야 한다.
