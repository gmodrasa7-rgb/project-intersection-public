<!-- PI-LANGUAGE: en-ko; version 0.1.0; operations, not scientific evidence -->
# PI-RISE-BUDGET v0.1.0 — Minimum Viable Research Funding / 최소 지속가능 연구예산
**2026-10-21 · Candidate until merged · Operational research finance scenario · Not a certified tax calculation, verified bank balance, funding award, compensation agreement or independent validation.**

## Original 1 — English | Concise computational specification

### Why this module exists
A grant headline is neither unrestricted income nor researcher take-home pay. A $5,000 project may underfund the investigator if project-only charges are ring-fenced. Separately, a $35/month computer/subscription bill does **not** fund a human investigator. A coherent budget needs a two-ledger conservation constraint:

- **Human continuance ledger:** target net personal compensation, lawful deductions, immediate survival/ability to refuse work. Human time is not treated as free because a model can generate text.
- **Scientific work ledger:** subscription, electricity, metered API, paid outside critique, equipment, and explicitly priced documentation. Grant restrictions and donor intent determine which charges are permitted.
- **Never cross-add:** project grants and personal sponsorship receipts; cash and restricted compute credits; gross pledges and bank receipts; parallel budget alternatives or unfunded reviewer fees.
- **Neither sufficiency nor novelty:** a numeric minimum meeting stated cost assumptions does not ensure research quality, publishability, science, or legal grant eligibility.

### Exact scenario formula and rounding convention
Let `N` = hypothetical desired **monthly net compensation** ($3,000), `t` = **reserve fraction** for tax/insurance/platform uncertainty (assumed, not a real effective rate), `P` = selected AI plan, `E` = assumed **incremental** PC electricity, `A` = separately billed API, `V` = **budgeted** external verification, and `c` = contingency on project charges only.

`M = CEIL_CENT( N/(1-t) + (P+E+A+V)*(1+c) )`.

`Y=12*M`; `D=CEIL_CENT(Y/365)`; `KRW_month = CEIL_WON(M*FX)`.

Assume 12 equally priced monthly cycles per year; daily amount is **annualized average**, not a daily payout promise or calendar month divisor. Round **up at monthly budget step**, not down. Unknown real tax, receipt or exact bills remain UNKNOWN. Confirmed debts and separate equipment replacement are outside this minimum scenario and must be appended before a live decision.

2026-10-20 historical reference FX **KRW 1,326/USD** for illustrative conversion only ([dated USD/KRW history](https://kr.investing.com/currencies/usd-krw-historical-data)); FX stress inputs 1,200/1,326/1,450 are assumptions, **not forecasts**. The [official ChatGPT Plus FAQ](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) lists USD $20/month and API **separately billed**. The [OpenAI Pro plan FAQ](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers) lists Pro 100/200/500 at USD $100/$200/$500. Local currency/app-store charges and taxes can vary; use receipts at contract time. $15 electricity is a **placeholder** until incremental kWh and household marginal rate are measured.

Tax treatment depends on type of Korean research support and deductions, not a universal 20%. [Korean National Tax Service income-tax information](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7666&mi=2227); [3% source withholding for specified business income](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7902&mi=6466) is not automatically final tax, and [NHIS 2026 rules](https://www.nhis.or.kr/english/wbheaa02500m01.do) depend on enrolment and property/income. A 20% reserve here is a **stress-test assumption**, not tax, withholding or guaranteed net.

### Computed minimum and improved options
All scenario values below use 20% hypothetical reserve and FX 1,326 KRW/USD unless named otherwise.

| Research state | Net target / mo | Budgeted separate operation / mo | Monthly request | 30-day tranche | Three months | Twelve months |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| **Continuance floor, existing Plus** | $3,000 | Plus $20 + power $15 | **$3,785** | $3,785 | $11,355 | $45,420 |
| **Enhanced ChatGPT access** | $3,000 | Pro 100 $100 + power $15 | **$3,865** | $3,865 | $11,595 | $46,380 |
| **Small reviewer-ready pilot** | $3,000 | Pro 100 $100 + power $15 + API $100 + reviewer accrual $300 | **$4,265** | $4,265 | $12,795 | $51,180 |
| **Pilot with 10% operating contingency** | $3,000 | Previous $515 operation + $51.50 reserve | **$4,316.50** | $4,316.50 | $12,949.50 | $51,798 |

$300/month independent reviewer accrual means **$900 over three months only if an actual paid reviewer can be contracted**; it is **not** independent review already performed, nor evidence $900 is enough for a competent review. Pro is **substituted for Plus**; it is not purchased in addition. API is not covered by the chat subscription.

**Daily annualized**: $3,785/mo = $124.44/day; $4,265/mo = $140.22/day. **KRW**: baseline KRW 5,018,910/mo; reviewer pilot KRW 5,655,390/mo at assumed FX. For baseline, KRW 1,200/1,326/1,450 produces 4,542,000/5,018,910/5,488,250 per month. FX stress affects the KRW-equivalent request; actual personal expenses and taxes may be KRW-denominated rather than USD-linked.

### Existing proposals — material mismatch, not retroactive changes
1. [Historical $5,000/30-day bridge](../funding/30_DAY_BRIDGE.md) preserves its original $3,200 investigator + $1,000 compute + $500 review + $300 docs line items. Under **this scenario's hypothetical 20% personal reserve**, net researcher cash on the $3,200 line is **$2,560**, **$440 below** the $3,000 objective. Holding other four-item proposal allocations fixed, the needed investigator line is $3,750, hence a separate **$5,550 alternative**. **No original $5,000 proposal was modified**, and nothing here claims acceptance or tax classification.
2. [KRW 18,000,000/90-day pilot](../funding/90_DAY_PILOT.md) corresponds to KRW 6m/month by 3 equal months. The $4,265 hypothetical researcher+small-review pilot is KRW 5,655,390/month at the FX assumption, leaving **KRW 344,610/month before omitted expenses**, if and only if actual permitted expense allocations allow it. The existing proposal has no binding line-item schedule implied by this comparison. Real taxes, reviewers, exchange, fees and staffing may remove the apparent margin.
3. [Personal sponsorship single canonical ledger](../funding/SPONSORSHIP_PUBLIC_LEDGER.md) remains the unique record for paid individual sponsorship, uses only researcher compensation and LLM usage. External review, technical engineering and electricity under a **separate grant/contract** cannot silently be charged to that two-use sponsorship ledger. All public sponsorship bank receipts remain **UNVERIFIED** in the repository's last reconciled state.

### Advancement decision
- **FLOOR:** $3,785/month is a constrained hypothetical funding floor at 20% reserve, not the uniquely true minimum.
- **CAPABILITY:** upgrade to Pro 100 adds $80/month *only when measurable advanced-use limits cause an actual research bottleneck*. Higher plan names do not prove more discoveries.
- **INDEPENDENT EVIDENCE:** planned $300/month external critique + $100 API is a reviewer-access *budget*, not actual independent replication.
- **PAUSE/HOLD:** absent verified personal living runway, receipts or funder permission, do not declare the project financially viable.
- **COST TRUTH:** at least one net human labor target must be met; neither low-cost GitHub nor credits can offset unpaid human research by accounting fiction.
- **FAILURE / falsifier:** if confirmed local invoice, tax reserve, marginal electricity, translation budget, equipment repair, reviewer contract or funding restrictions exceed the proposed line items, revise upward before a funding guarantee.

### Reproduction
`python3 tools/pi_rise_budget.py` — predeclared artificial scenarios only, Decimal arithmetic.
`python3 -m unittest discover -s tests -p 'test_pi_rise_budget.py' -v` — boundary tests, not real-world finance or scientific validity.

No confidential personal finance, family situation, bank evidence, credentials, employer or medical data included in public artifacts. This is a funding-planning instrument, not a grant submission.

---
## 원본 2 — 한국어 | 보고서 및 검증 조건

### 판단
**PI-RISE-BUDGET v0.1.0**: PI-RISE 운영정본 v0.1.0 하위 **별도 예산 계산 모듈**. 연구 이론 VC·MER·EI·ECR·IVS-0R의 입증 수준 또는 PI-RISE 정본 버전 상승 아님.

**이중 장부 원칙:** 연구자 생계의 세후 보수와 연구비의 장비·API·독립평가 비용을 분리. 신청액·크레딧·실입금·자유롭게 쓸 수 있는 생활 현금 구분. 두 가지 재원에서 같은 비용 중복 청구 금지.

**계산식:**
`월예산 = 센트 올림[목표 세후보수÷(1-가정 공제율) + (AI 구독+PC 전력+API+외부검토)*(1+기술비 예비비율)]`.
`연간=월×12`, `일평균=연간÷365 올림`, `KRW=USD×계획환율(원 단위 올림)`.
**월 정산과 일평균을 혼동 금지. 반올림으로 목표 세후보수 미달 금지.**

### 기준 시나리오
**연구자 목표 월 세후 $3,000 · 공제/보험/수수료 등 20% 예산 가정 · $1=1,326원(10월 20일 역사값) · 전력비 $15 가정.**

| 항목 | 월 USD | 연 USD | 월 KRW |
| --- | ---: | ---: | ---: |
| Plus 기존 유지, 외부 평가 없음 | **3,785** | 45,420 | 5,018,910 |
| Pro 100 전환, 외부 평가 없음 | **3,865** | 46,380 | 5,124,990 |
| Pro 100 + API $100 + 외부 평가 적립 $300 | **4,265** | 51,180 | 5,655,390 |
| 위 시나리오의 운영비에 10% 예비비 | **4,316.50** | 51,798 | 5,723,679 |

**최저 보존 비용 $35/월(Plus+전력 추정)은 연구자 보수 미포함. 연구 지속가능성 예산으로 명명 금지.**

**공제·부담금 가정별 Plus 최저 요청:** 0%=$3,035, 10%=$3,368.34, 20%=$3,785, 30%=$4,320.72. 이 수치는 한국 실효세율 확정치 아님. 국세청 원천징수나 종합소득세, 건강보험·연금, 한국 내 후원금 소득 분류는 별도 검토. 원화 결제와 현물 크레딧·환율·세금의 실제 청구 방식 확인 후 확정.

**기존 자금요청의 구조적 모순:** $5천 30일 브리지 중 연구자 $3,200은 가상 20% 공제 후 $2,560. 월 세후 $3천 목표 대비 $440 부족. 동일 연구경비 유지 시 별도 수정안은 **총 $5,550**. 기존 문서 수정·소급 취소 없음. 연구비가 총액 $5천이라는 이유로 연구자 지속조건 충족 판정 금지.

**90일 1,800만 원 제안:** 총액만 월 600만 원으로 배분할 때, 위 Pro100+API+소액 외부평가 시나리오 월 약 565만5천 원과 비교해 약 **34만4,610원 잔여**. 예산 내 다른 비용·보험·세금·환전/수수료·실제 연구평가 계약까지 충당된다는 보장 전혀 없음. 확보자금 아님.

**연구 목적에 따른 결정:** 목표가 연구자가 중단 없이 생계·거절권을 갖는 **가장 싼 운영**이면 $3,785/월이 현재 가정 하의 최저. 목표가 독립 평가 가능성을 처음으로 구매하는 최소 파일럿이면 **$4,265/월**. 독립 검증이 실제로 수행될지, 검토 비용이 충분할지는 현재 미식별.

**기능:** ① 월 비용 보수적 센트 올림 ② 일·월·90일·연 비교 ③ 환율 민감도 ④ 실험/API·프로 인상분 분리 ⑤ 이전 브리지 인건비 부족분 식별 ⑥ 기획비와 실수령 구분 ⑦ 음수·부정확한 실수 입력 차단 ⑧ 합성 회귀검사.

**실제 지급·계약·개인 원천징수·독립복구·자금 수여·과학적 효과: 전부 미확인.** 후속 버전은 실제 합법적 지급 구조 및 원증빙 대사 후에만 예산의 현실성을 개선. 사용자 개인정보 원본 공개 불가.

**원전:** ChatGPT Plus [공식 요금 안내](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus), [Pro 100/200/500 안내](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers), [국세청 세율 구조](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7666&mi=2227), [소득별 원천징수](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7902&mi=6466), [국민건강보험 2026](https://www.nhis.or.kr/english/wbheaa02500m01.do), [2026-10-20 USD/KRW](https://kr.investing.com/currencies/usd-krw-historical-data). 기준일 이후 변경은 정정 필요.
