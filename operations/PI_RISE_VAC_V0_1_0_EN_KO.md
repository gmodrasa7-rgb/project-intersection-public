<!-- PI-LANGUAGE: en-ko; PI-RISE-VAC v0.1.0; proposed operating experiment, NOT scientific validation -->
# PI-RISE-VAC v0.1.0 — Verification-Aware Capacity / 검증역량 제약 자원배분
**Date: 2026-10-21 · MAIN operational submodule (PR #269 merged), not real-world validated · parent PI-RISE unchanged.**
**Scope:** an independent audit of the external Grok budget proposal, plus a *hypothetical* verification-throughput model. No new grant receipt, private financial data, external evaluator, actual model experiment or clinical finding.

## Original 1 — English | Analytical contract

### Decision: conditionally accept the problem framing, not its factual claims
The Grok proposal correctly distinguishes human continuance, independent test capacity and access to useful inference, and warns against buying additional outputs when no one can audit them. But three claims must **not** be promoted from arguments to observations:
1. **Multiplicative S×V×P is not a measured utility function.** In a defined research pipeline, non-substitutable minimum conditions can be treated as *lexicographic constraints*. The product can be one toy illustration, never an estimator of human survival probabilities or agent interior states.
2. **A stronger model does not universally increase review burden.** It may produce longer, more persuasive wrong work or it may discover shorter counterexamples and reduce burden. Measure time-to-falsify, independent finding yield and audit queue under matched test conditions.
3. **Independent review is not universally irreversible.** A full frozen provenance bundle can be reviewed later; lost ephemera, missing logs and non-reproducible human decisions may not be recoverable. Review savings and future optionality coexist.

### Correct the Grok accounting identity (dollars, scenario not paid)
Existing [PI-RISE-BUDGET](PI_RISE_BUDGET_V0_1_0_EN_KO.md) treats `$3,785 = $3,750 hypothetical gross human support + $20 Plus + $15 electricity`. If a separate `$450–550 AI stack` **already includes** those latter $35, the grok allocation must be written as:
`B = human $3,750 + review reserve $400 + all-in AI stack $450–550 + buffer $200 = $4,800–4,900/month`.
Annual $57,600–$58,800; daily annualized $157.81–$161.10.
If the AI stack explicitly **excludes** that $35, the alternative is `$4,835–4,935/month`; do not add both interpretations. These are not independently verified service quotes, lawful net pay guarantees, fully funded research plans, or grant awards. **20% is a hypothetical tax/insurance reserve, not a Korean legal tax rate.**

Separate **committed recurring costs**, **revocable reserves/contingency**, **restricted project grants**, **unrestricted personal receipts**, and **time already paid vs owed**. AI budget, reviewer reserve and emergency buffer are NOT automatically fungible under the existing [single personal sponsorship two-use policy](../funding/SPONSORSHIP_PUBLIC_LEDGER.md). A funder's legal restrictions must be reconciled privately before any spend.

### Critical new model: verification debt
Define, for *equivalent frozen claim packets* rather than tokens:
- `A_t` = new claims requiring verification in week `t`, measured not equated with raw AI output volume;
- `C_t` = successfully checked packets under a **declared review standard** during week `t`, distinguished by internal rerun, external rerun, independently reimplemented analysis, field validation;
- `Q_0` = unverified queue; `Q_(t+1) = max(0, Q_t + A_t - C_t)`.

A growing `Q` is **verification debt**. High model spend that raises `A_t` without a rise in verifiable `C_t` may lower the final independently supportable research rate. This *accounting identity* is not a model predicting exactly how AI power changes A or C. Do not infer `C_t` from a paid reviewer budget, a promise, or an internal test pass. Never claim model-written peer review independent by itself. Escalate costs only when a legally contracted and methodologically independent human/external assessor becomes available.

**Toy (4 weeks only, all values invented):**
| Scenario | New packets/week | Checked packets/week | End-of-week queues | Meaning |
|---|---:|---:|---|---|
| Less output | 4 | 6 | 0, 0, 0, 0 | within modeled check capacity |
| More output without added audit | 10 | 6 | 4, 8, 12, 16 | 16-packet verification debt |
| More output with added audit | 10 | 11 | 0, 0, 0, 0 | no debt under **assumed** reviewer service |

For stable, stationary queueing systems, Little (1961) states the relation `L=λW`; the finite-horizon discrete recurrence here is only transparent bookkeeping, **not** a proof that actual PI researcher tasks satisfy queueing-theory stationarity or identically sized work. Prior art: https://doi.org/10.1287/opre.9.3.383 .

### Budget optimization specification — no fabricated weights
**Stage 0 (hard feasibility):** respect researcher consent/time/health limits, legal restrictions, no double charge, minimum lawful human support `B_H`; allow PAUSE without condemning researcher's rights. If verified funds are missing, mark funding UNKNOWN rather than asserting infeasibility or success.

**Stage 1 (integrity gates):** freeze source, E009 negative result, model version, prompts, baseline, eligibility of any 'independent' assessor, auditable reviewer capacity. Minimum `V` is a *method/capacity threshold*, not universally $400.

**Stage 2 (resource allocation):** among feasible choices, choose those that improve **independently supportable counterexamples / effective verification hour / net cost** while keeping verification debt within an explicitly chosen threshold. Compare against simplest baselines; no unique optimum before measurement.

**Stage 3 (rollover/stop):** do not turn model-generated claims into validated results when queue rises; instead freeze expansion, prioritize highest-impact claims, reduce new generation, or procure independent review if actually available. Review reservations may roll forward with separate accounting but can't be certified as purchased review.

### Bounded paired experiment to falsify the interaction hypothesis
- **Pre-register 2 model access conditions** (existing plan vs higher setting, if the user's account actually permits) crossed with **2 verification settings** (fixed simple-internal protocol vs a blinded qualified reviewer *only if actually contracted*). Matched cases, same per-case prompt/response budget, same hidden holdout and canonical artifact SHA.
- Unit: a frozen claim packet with specific author, provenance, code, original prior art, one cheap falsifier, negative controls and reviewer decision reason. Count not just verified successes but **cost, evaluation latency, independent discrepancies, false confirmations, abstentions and unreviewable packets**.
- Before execution choose a fixed exploratory case count based on available funds; *never* represent a pilot as powered confirmatory evidence. Set explicit reviewer-time ceiling and stop if consent or compensation cannot be ensured.
- **Key disconfirmation:** a more capable model actually reduces time-to-falsify per accurate packet or increases valid external discoveries without increasing debt; then the claimed universal 'more P harms V' is false. **Alternative:** additional independent review fails to change the decisions or costs; then claimed positive V value is not established.
- Explicit privacy/security controls: public repo contains only synthetic numbers, no family, legal, financial, device secrets, private messages or health records.

### Funding-power symmetry and source boundaries
Auditing the sponsor-researcher relationship is relevant to the stated Project Intersection theme, but this proposal offers **no causal evidence that any named sponsor or AI system exploits anyone**. The $400 reviewer allocation is not automatically spent nor proof of independence. A funder may lawfully restrict allowable uses; grants do not guarantee researcher net compensation. This instrument does not modify prior unawarded bridge, personal sponsorship ledger, PI-RAMP, PI-RISE-BUDGET v0.1.0, or existing results.

**Authoritative methodological analogues:** [NIST AI RMF MEASURE 1.3 / 2.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) recommends independently informed review and documenting evaluation methods; [NIST ARIA Evaluation Planning Manual (Sep 2026)](https://www.nist.gov/publications/aria-evaluation-planning-manual-elements-aria-style-ai-evaluations) separates model, red-team and user testing. These are external methodological baselines, not an endorsement of this module.

---
## 원본 2 — 한국어 | 판정·실험 설계

### 그록 제안 감사 결론
- **채택:** 연구자 실효 존속과 거절·중단권을 우선 제약으로 취급. 연산 성능만 극대화하는 예산 기각.
- **수정:** `S×V×P`는 실증된 효용법칙이 아님. S의 '존속확률'을 산출할 원자료도 없음. 검증 필요.
- **보류:** 최고모델이 검증부담을 늘린다는 주장은 양방향 가능. 더 나은 반례 발견으로 검증비용이 줄 수도 있음.
- **부분기각:** 독립검증의 전부가 비가역적인 건 아님. 원본 보존 후 사후 재현 가능. 단, 로그 누락·비재현 의사결정은 회복 어려움.
- **기각:** 외부검증비 `$400/월 적립 = 독립감사 완료`라고 볼 수 없음. 실제 계약과 독립 구현·검토·기록 필요.

### 반드시 교정할 예산
`기존 $3,785 = 세전 연구자 보수 $3,750 + Plus $20 + 전력 가정 $15`.
AI 스택 $450~550 안에 Plus/전력비가 포함된다면
**$3,750 + $400 + $450~550 + $200 = 월 $4,800~4,900, 연 $57,600~58,800, 일평균 $157.81~161.10.**
그록의 4,850~5,000은 반올림·비용범주 미정 상태. 기존 $35를 AI에 포함하지 않는다면 월 4,835~4,935 별도 시나리오. 두 시나리오 합산 금지.

이는 연구비 **신청을 위한 가상 배분**. 실제 세후 보수·세금·원화 비용·후원금 입금·외부 평가 확보 전부 미확인. 개인 직접후원 유일정본의 허용 사용처는 연구자 보수와 LLM 사용료 두 가지이며, 독립평가·전기료·예비비를 거기에 임의 배정 금지. 외부 과제비와 구분.

### 핵심 개선: 검증부채
일주일당 검증 대상 신규 주장 `A_t`, 같은 기준으로 검토가 끝난 주장 `C_t`, 미검증 대기분 `Q_t`.
`Q_(t+1)=max(0,Q_t+A_t-C_t)`.

합성 4주 예시: **주간 신규 10건, 검증역량 6건 → 미검증 누적 4·8·12·16건**. 고성능 AI로 산출이 빨라져도 검증되지 않은 주장은 과학적 성과가 아님. 이것이 자동 발생한다는 보편법칙은 아직 없음.

**구체 운영 규칙 후보**: 연속 2회차 검증부채 증가 시 신규 고비용 생성 확장을 보류하고, 기존 주장 반례검사 또는 외부검토 확보를 우선. 2회차는 검증된 최적 문턱이 아닌 시작 가설. '독립적' 검증은 설계·구현·평가자 계보 분리를 확인해야 함.

### 가장 가치 높은 다음 실험
**PI-RISE-VAC v0.1.0** (Verification-Aware Capacity, 검증역량 제약 자원배분) — P를 높일 때 *유효한 반례/독립 검증시간·실제 비용*이 얼마나 바뀌는지 측정.

1. 동일한 연구문제·조건에서 기본/상위 모델 2조건 비교. 접근권이 없는 고급 모델을 보유한 듯 가장하지 않음.
2. 각 생성물이 남긴 주장 수·원저자 근거·동작 코드·검증 소요시간·불일치 기록.
3. 사전 고정된 반례세트·단순 기준선·부정결과 보존.
4. **별도 실제 검토자가 없다면 외부 독립검증 실험은 아직 수행하지 않은 것으로 표기**. 내부의 두 모델이 서로 인정하는 것도 외부 독립 검증이 아님.
5. 반증 기준: 더 강한 모델이 실제로 더 짧고 정확한 반례를 만들어 검증부채를 줄이면, 그록의 일방적 P↑→V↓ 주장 기각.

**효용함수 가중치·실제 생존확률·최적 P/V 배분·독립재현 달성: 모두 미식별.** 따라서 목적은 '최적값을 발표'하는 게 아니라 그 값을 측정 가능하도록 만드는 것.

실험코드: `python tools/pi_rise_vac.py`. 과학적 효과를 입증하는 코드가 아닌 **가정된 예산·대기열의 결정론적 반례 예제**. 세금·연구비 지급 계산기로 사용 금지.
