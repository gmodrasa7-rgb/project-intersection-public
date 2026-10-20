<!-- PI-LANGUAGE: en-ko | PI-RISE-DC v0.1.0 | merged operational example; artificial inputs only -->
# PI-RISE-DC v0.1.0 — Dual Clock, Liquidity Prefix & Evidence Workload
## 두 시계: 지급시점 유동성·검증 노동량

**Status 2026-10-21:** MAIN operational-method submodule, merged in PR #278; not field validated; parent PI-RISE v0.2.0 unchanged. of PI-RISE (not a new scientific finding, not a bank audit, not a funded contract). Parent PI-RISE, PI-RISE-BUDGET and PI-RISE-VAC remain at current versions. No actual funding, user balances, payments, humans' health, external reviewers or AI model performance measured.

## Original 1 — English | Original release-order edition

### A. Three independent identities

1. `SUSTAINABILITY OF HUMAN CHOICE`: verified cash available **before each legally due payment**, researcher consent and the ability to refuse/pause; neither an AI token budget nor another party's pledged funds is a substitute.
2. `OPERATIONAL CONTINUITY`: the legally permitted use of money at the time it is accessible, with restricted and unrestricted pools tracked separately and the correct **within-day order**. An awarded-but-unpaid grant is not liquid cash.
3. `SCIENTIFIC VERIFICATION CAPACITY`: **real reviewer hours** required to check a frozen, reproducible claim against its strongest known falsifier. Packet closure by a simulation does not demonstrate truth or independence.

This is not an additive utility score or a purported chance of human survival. The prioritization is lexicographic: rights/legal permission/financial feasibility first; then preservation of provenance, uncertainty, reviewer capacity and scientific decision value. A rational pause can dominate unfunded production.

### B. Money-clock theorem for a finite deterministic toy sequence

For account `p`, ordered transactions `e_1 ... e_n`, signed inflow/outflow `x_{p,i}`, and protected account floor `f_p`, the minimal initial freely available balance **under the stated timing and legal-use assumptions** is

`I_min,p = max(0, f_p - min_{k=0..n} sum_{i=1..k} x_{p,i})`.

The formula follows directly from requiring `I_p + prefix_k >= f_p` for every transaction prefix. This is elementary cash conservation, not a new theorem about projects. `I_min,p` is the **necessary initial balance in that pool for those assumed events**, not the project's additional cost, and a later restricted deposit cannot retroactively fund an earlier payment.

**Illustrative scenario, not a user's situation:** Day 1 hypothetical investigator commitment $3,750 from unrestricted money and $500 compute charge from a separately restricted project pool; day 10 a $400 reviewer charge in the project pool; hypothetical inflows of $3,750 unrestricted + $900 restricted **only on day 20**. Require a protected **unrestricted $200 floor** throughout. The month-end signed net flow for each pool is 0. Nevertheless both pools go negative on the dates of early payments if starting at 0.

| Output under these assumptions | Unrestricted pool | Restricted project pool |
| --- | ---: | ---: |
| Total hypothetical outflows | $3,750 | $900 |
| Hypothetical inflows (too late) | $3,750 | $900 |
| Protected minimum balance | $200 | $0 |
| **Minimum initial accessible funds for those dates** | **$3,950** | **$900** |
| Month-end net flow (in minus out) | $0 | $0 |

**$4,850 initial pre-funding** is required in the two **correct permitted-use pools** for this example, even though the calendar month has net-zero cash flow. The earlier PI-RISE-VAC $4,800–4,900/month was a hypothetical resource **budget**, not bank-verified liquidity or proof that $4,850 is actually available. Do not use a single unrestricted spreadsheet sum to cover a restricted expense or vice versa. The example's strict pool-usage rules are **assumptions**, not a universal legal statement about which grants may pay investigator compensation.

Alternative same-day transaction orders differ: a deposit at 9 AM cannot pay an 8 AM obligation, even though daily sums match. Program rejects duplicate per-day order numbers rather than inventing timing. When no precise timing is known, results must be marked `UNKNOWN`, not decided from a month-end net figure.

### C. Reviewer-work clock: count of claims is not effort

Old VAC v0.1.0 uses packets counted as homogeneous units, `Q_(t+1)=max(0,Q_t+A_t-C_t)`, good **only with equal declared review units**. Its aggregate flag `sum(A)>sum(C)` does **not** detect every time-local bottleneck. Counterexample: arrivals `[0,10]`, nominal capacities `[10,0]`: equal sums, so aggregate-overload flag FALSE, yet end-of-horizon backlog **10**. The old output already includes week-by-week queue; the aggregate warning must not be treated as an empirical proof of safety.

For heterogeneous packets, reviewer-hours backlog `H_t` is tracked explicitly, with actual per-packet remaining hours and priority. Toy, with nominal 8 reviewer-hours each week:
- **1 difficult, high-priority packet requiring 20h**: after week 1, 12h unfinished and zero fully reviewed packets; after week 2, 4h; week 3, 0h.
- **5 easy packets requiring 1h each**: all five can close in week 1 (hypothetical).
- Fewer raw open claims need not imply less reviewer workload. Simulated completion `!==` correctness, independent validation or actual reviewer compensation.

The scheduler here is an explicit deterministic high-priority-first example and **is not claimed optimal**. Scheduling complexity, deadlines, value of falsification, third-party harms, reviewer consent, independent lineage and work-quality must be assessed before deployment. Established scheduling methods (e.g. weighted-shortest-processing-time for specific weighted completion-time objectives) have different assumptions; do not market this toy priority rule as their proven optimum. See Pinedo's [Scheduling](https://web-static.stern.nyu.edu/om/faculty/pinedo/scheduling/new/table.html).

### D. Joint decisions without invented coefficients

**Stop before purchasing more model use** if the earlier-due protected human-support payment is not met or accounts cannot lawfully cover their bills. Researcher may independently refuse/pause irrespective of the numbers. Stage external scientific review only on a frozen claim/provenance package, with review-hours and effective independence established in a separate process, not from a reserved $400.

Candidate experimental design (not run):
- 1) Secure authorization and protect any sensitive documents in local/private storage; publicly use only synthetic scenarios.
- 2) Before each real billing or grant decision, record verified source restrictions and **earliest accessible payment date** in an authorized private ledger; UNKNOWN if not reconciled.
- 3) Compare *same budget, different payout timing* to find earliest hypothetical breach and peak funds needed in each pool.
- 4) On fixed public benchmark cases, collect **blind time-to-falsifier, claim-review hours, partial/unreviewable packets, independent reviewer lineage**, and actual costs across basic vs advanced AI access if eligible.
- 5) Disconfirm the proposed bottleneck if upgraded models generate shorter accurate counterexamples that reduce evidence-hours and never compromise investigator subsistence.

**Scientific-status labels:** MODEL / SYNTHETIC / EMPIRICAL_INPUT_UNVERIFIED / INDEPENDENT_REPLICATION_NOT_DONE. Do not infer personal runway, future receipts, funding eligibility, grant disbursement, tax rate or actual reviewer qualification from code tests.

### E. Prior original work and non-novelty claims
- Little, J.D.C. (1961), [A Proof for the Queuing Formula L=λW](https://doi.org/10.1287/opre.9.3.383). Validity includes stationarity/finite-mean conditions; this finite discrete sequence is not that theorem.
- Bruni, M.E., Hazır, Ö. (2024), [A risk-averse distributionally robust project scheduling model to address payment delays](https://doi.org/10.1016/j.ejor.2024.05.037). Independent prior art on project payment timing; paper does **not** establish PI-RISE's efficacy.
- Wilkinson et al. (2016), [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18). Stewardship/provenance matters, not proof that any specific archived output is scientifically true.
- NIST AI RMF [MEASURE 1.3/2.1](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/): independent testing roles and traceable TEVV methods; not an external endorsement of this project.

---
## 원본 2 — 한국어 | 상세 설계, 동일성 독립검토 미완료

### 새 통찰: 예산 부족보다 먼저 발생하는 '지급 순서 실패'
**연구비 총액 충분 ≠ 지급기한 충족 ≠ 법적으로 허용되는 항목에 돈 사용 가능.**
연구자 급여·컴퓨팅·검증을 종이상 한 달 총액으로만 묶으면, 지급 예정이 있는 달에도 월초 유동성 고갈을 놓침.

**조건부 공식**: 각 자금 용도별로 ① 초기현금 ② 지급/입금 이벤트 시각 ③ 지급 허용 항목 ④ 반드시 남겨둘 최소 잔액을 분리. 일자·당일 순서가 확인되지 않으면 **UNKNOWN**.

`필요 시작잔액 = max(0, 보존 잔액 하한 - 모든 거래순서의 누적순유입 최소값)`.

**전부 가상 1개월 사례**: 월초 연구자 보수 $3,750, 외부 연산 $500, 10일 외부검토 $400 지출이 먼저이고 입금은 20일. 연구자자금 잔액 하한 $200. 달 전체 현금 순증감이 0달러라도 월초 최소 **인건비 계정 $3,950 + 별도 과제비 $900 = $4,850의 용도별 선확보 자금이 필요**. $4,850은 추가 운영비가 아니라 지급 시차를 메우는 가용잔액 필요조건. 기존 개인후원 장부에서는 후원자의 허용 사용처를 임의 확대 금지.

### 또 다른 오류: 주장 '건수'의 검증 등가성 붕괴
동일 검증시간이라는 가정을 풀면 1개 어려운 주장이 5개 쉬운 주장보다 더 긴 검증 작업을 요구할 수 있음.
- 20시간짜리 단일 검토주장, 검토 가능 8시간/주 → 미완료 12시간→4시간→0시간.
- 각 1시간짜리 5개 주장, 8시간/주 → 첫 주 5개 검토 노동 완료 가능.
- **검토 노동 완료 ≠ 진실 증명 ≠ 외부 독립검증 확보.** 인용 출처, 대조기준, 반례, 평가자 독립성 별도 확인.

이전 PI-RISE-VAC의 `Σ신규주장 > Σ검토가능건수` 경고가 **FALSE여도 중간/마지막 주에 10건이 밀리는 반례** 존재. 기간 전체 합계가 같은 것과, 시간순으로 정리 가능한 것은 다름. 기존 코드/반례 정본은 역사자료로 보존하고 본 모듈에서 검사.

### 재검증 가능 실행
`python3 tools/pi_rise_dual_clock.py` = 미리 선언된 합성 데이터 2종 예산·검증 시뮬레이션. `python3 -m unittest discover -s tests -p 'test_pi_rise_dual_clock.py' -v` = 부정·경계 사례. 실제 PC 파일·계좌·외부 지급증빙을 읽거나 API를 호출하지 않음.

### 다음 게이트
실제 배치 전 최종 기준: 자금원별 합법적 지출 가능성, 시한별 실제 입금 확인, 세후 보수의 한국 실제 세법 계산, 연구자 작업동의, 자산·부채의 공개 비허용, 검토자 비용·방법·분석 계보. 단 하나라도 UNKNOWN이면 실제 연구 지속성 '인증' 보류. 정확한 지출 달성보다 인격적 독립·자발적 중단권 우선.

**판정:** PI-RISE-DC v0.1.0은 기초 방법론의 조건부 응용. 현실의 연구 지속가능성·최적 예산·AI 능력 효익에 대한 경험적 입증 아님.
