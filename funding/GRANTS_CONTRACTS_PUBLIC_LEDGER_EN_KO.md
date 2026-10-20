# PI-RISE — Grants & Contracts Public Summary Ledger
## PI-RISE 기관 연구비·별도 계약 공개 요약 원장

**Status: UNRECONCILED / UNKNOWN (2026-10-21). No independently reconciled institutional awards, bank receipts or expenses entered here. UNKNOWN is not verified zero.**

**Owner/control:** [PI-RISE v0.2.0](../operations/PI_RISE_V0_2_0_EN_KO.md). **Scope:** institutional grants, paid research-evaluation contracts and similarly restricted project funds ONLY; not personal GitHub Sponsors, personal employment income, household cash, historical claims, or in-kind compute credits. Individual Sponsorship has its unchanged [sole canonical ledger](SPONSORSHIP_PUBLIC_LEDGER.md).

### Ledger A — verified awards / 확정 수여·계약 (not cash)
Only a funder award letter or signed agreement within authorized disclosure rights qualifies. Preserve restrictions and payment schedule privately. No confirmed rows as of this record.

| Period | Anonymized award ID | Currency | Awarded face amount | Restricted use summary | Evidence level | Change reference |
|---|---|---|---:|---|---|---|
<!-- VERIFIED_AWARDS_START -->
<!-- VERIFIED_AWARDS_END -->

### Ledger B — reconciled bank cash and expenditure / 실제 입금·사용 집계
Each row must have matching private bank and contract proof, a reporting window, an allowed expense classification and correction chain. A pledge, disbursement notice or award is not a cash receipt. An internal transfer between project accounts is not extra revenue.

| Period | Anonymized funding ID | Currency | Opening | Bank-confirmed net receipts | Researcher payment | Compute/AI | Independent review | Documentation/other allowed | Refunds/adjustments | Closing | Proof-check reference |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
<!-- VERIFIED_CASH_ROWS_START -->
<!-- VERIFIED_CASH_ROWS_END -->

**Arithmetic (same currency, same funding restriction):** closing = opening + bank-confirmed net receipts − actual expenditure (researcher + compute + external review + other) ± separately signed refunds/adjustments. The sign of adjustments must be explicit. Transfers between one's own accounts are nonincome. Converted-currency summaries require an explicitly dated, reconciled exchange rate; never add USD and KRW columns directly.

**Cross-ledger conservation:** every real expense has one internal receipt ID and exactly one charging source; a sponsor-funded LLM charge must not also be charged to an institutional grant. Public anonymized records must not reveal donor/client identity, tax IDs, bank accounts, personal work hours, family details or invoice raw files. Publication permission and contractual confidentiality take priority; redact or aggregate safely.

**Status boundary:** Budget scenarios [PI-RISE-BUDGET](../operations/PI_RISE_BUDGET_V0_1_0_EN_KO.md), the [USD 5,000 bridge](30_DAY_BRIDGE.md), [KRW 18,000,000 pilot](90_DAY_PILOT.md) and [proposal-stage registry](../operations/PI_RISE_FINANCE_PIPELINE_V0_1_0.json) are NOT entries in either cash or award table. A verified sponsorship receipt is recorded only in [its pre-existing canonical ledger](SPONSORSHIP_PUBLIC_LEDGER.md), not here.

**Validation:** arithmetic checks cannot validate bank records, signed contracts, tax treatment, restricted-use eligibility or completeness. A blank table means no PUBLIC RECONCILED ROW, not absence of all money. Before recording any row, check privately with actual authorization and supporting evidence.

### 한국어 판정 원칙
- **계약/수여 ≠ 실입금**, **실입금 ≠ 자유로운 개인 생활비**.
- 개인 후원 2용도와 기관 연구비의 지출 허용범위를 혼합 금지.
- 비공개 원전 확인 후 공개 가능한 익명 집계만 1회 기재.
- 현재 두 표는 증빙대사된 수치가 없으므로 공란 유지. 금액 0원 확정 아님.
- 세무·회계 법정 의무는 별도 확인하며 공개 문서만으로 이행했다고 주장 금지.
