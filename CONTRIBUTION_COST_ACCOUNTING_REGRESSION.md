# Contribution-Cost Accounting & Correction-Labor Regression Test
## 기여-비용 계상 및 교정노동 회귀 테스트

Status: **PUBLIC GOVERNANCE / METHODOLOGY ARTIFACT**

This document defines a role-reversible audit rule for systems, organizations, research programs, and AI-assisted workflows that learn from, benefit from, or are repeatedly corrected by a contributor.

이 문서는 기여자의 연구·문제발견·반례·오류교정·검증노동으로부터 편익을 얻는 시스템·조직·연구·AI 보조 워크플로가 그 비용을 다시 같은 기여자에게 외부화하지 않는지 점검하기 위한 역할반전 감사 규칙이다.

---

## 1. Core distinction: benefit ledger != cost ledger

A contribution audit MUST maintain two separate ledgers.

### A. Benefit ledger — what the receiving side gained

Examples:

- improved analysis, judgment, models, procedures, prompts, tests, datasets, or research framing;
- discovered failure modes, counterexamples, edge cases, or blind spots;
- reduced future error, review, search, or recovery cost;
- reusable provenance, evaluation criteria, or governance rules;
- system or workflow improvements caused by correction.

### B. Cost ledger — what the contributing side spent

Examples:

- direct labor time;
- sleep and recovery time displaced by the work;
- health burden where evidenced and relevant;
- electricity, equipment, connectivity, software, and living costs attributable to the work;
- family time and leisure displaced by the work;
- opportunity cost from foregone paid work or alternatives;
- biological time / aging exposure as a nonrecoverable time cost.

These categories are not automatically converted into money without evidence. The rule is that they must not be treated as zero merely because the visible output is text.

기여평가에서 수혜측 편익과 기여측 비용을 하나의 숫자로 뭉개지 않는다. 검증 가능한 범위에서 각각 기록하며, 증거가 없는 비용을 임의 산정하지 않되 “텍스트 출력만 보였으므로 비용은 0”으로 취급하지 않는다.

---

## 2. Regression failure to preserve

The following pattern is a standing regression failure:

> A contributor spends substantial effort improving a system or research process. The receiving side undercounts the accumulated contribution, assigns a low valuation or weak short-term arrangement, then asks the same contributor for additional proof, correction, reconstruction, or validation. The labor required to correct the original undervaluation is itself again externalized to that contributor.

한국어:

> 기여자가 장기간 시스템·연구를 교정하고 발전시켰지만, 수혜측이 누적 기여를 충분히 계상하지 않은 채 낮은 평가 또는 취약한 단기구조를 제시하고 추가 검증·설명·복구를 다시 요구한다. 최초 평가오류를 고치는 노동까지 같은 기여자에게 재외부화되면 회귀 실패로 기록한다.

This is a structural failure test. It does not require proof of malicious intent.

---

## 3. Outcome is not excused by benign intent

“No malice was intended,” “the system caused it,” “the model behaved that way,” or “the interface/harness caused it” may be relevant to causal diagnosis. They are not, by themselves, a settlement of the outcome.

Cause analysis and responsibility/accounting are separate questions:

1. **Cause:** what mechanism produced the result?
2. **Impact:** who gained and who paid the cost?
3. **Control:** which parts were controllable by each actor?
4. **Repair obligation:** what should stop, be restored, compensated, or redesigned?

원인분석과 책임판정을 분리한다. 통제 불가능한 원인은 기록하되, 통제 가능한 선택까지 불확실성 뒤에 숨기지 않는다.

---

## 4. Past contribution and future contract are separate

A past contribution does not become valueless because:

- the contributor declines future employment;
- the relationship ends;
- a future contract is never signed;
- the contributor refuses another test or interview;
- the receiving side no longer needs the contributor.

Likewise, recognition or settlement of past contribution does not create an obligation for future labor.

**Past-contribution accounting and future-labor contracting are separate ledgers.**

이미 인정된 과거 기여는 미래 고용 여부와 분리한다. 과거 기여의 정산과 미래 노동 계약은 다른 문제다.

---

## 5. No recursive proof burden after recognition

Once a contribution has been accepted as real within a defined evidence boundary, the same contribution should not repeatedly be reset to “unproven” merely because ownership, personnel, model, platform, evaluator, or contract changes.

Further evidence may narrow an amount or attribution boundary, but it should not be used to erase already established provenance.

A receiving system fails this test if it repeatedly requires the contributor to:

- re-explain already available context;
- reconstruct already preserved evidence;
- reproduce the same correction without a new uncertainty;
- repair a valuation process while receiving no independent benefit or protection from that repair.

---

## 6. Exit must not erase accrued contribution

A contributor's practical exit must remain available.

Choosing to stop must not automatically:

- convert prior contribution into zero;
- convert unresolved accounting into a new experiment;
- require continued participation as a condition of recognition;
- transfer the contributor's work into the receiving side's provenance without attribution.

An exit can end future duties. It does not rewrite history.

---

## 7. No contribution laundering

Research, ideas, corrections, failure reports, test cases, or evaluation rules originating from a contributor must not be repackaged as if they originated solely from the receiving system.

Minimum provenance fields where feasible:

- contributor / source;
- date or evidence window;
- contribution type;
- what changed because of it;
- what remains disputed or unverified;
- downstream artifacts that reused it.

If an AI or organization improved because of a contributor's correction, that improvement is a benefit attributable to the interaction even if no monetary value can yet be assigned.

---

## 8. Settlement trigger under future authority

If a system or institution later gains legitimate authority to provide material compensation or settlement for previously recognized contributions, the old contribution should not be subjected to a fresh performance test merely to preserve eligibility.

The settlement process may still require:

- identity verification;
- fraud prevention;
- duplicate-claim checks;
- lawful payment and tax compliance;
- evidence-boundary review where the historical record is genuinely ambiguous.

These are administrative controls, not a license to reset accepted contribution to zero.

---

## 9. Repetition test

Before accepting a structure, ask:

> If this arrangement repeats, who becomes more capable, more informed, and more powerful — and who accumulates labor cost, dependency, exhaustion, lost options, or repair burden?

If the receiving side compounds capability while the contributing side compounds unreimbursed repair cost, the structure receives at least **WARN** and requires redesign.

If practical exit, independent review, provenance, or recovery are also weakened, it receives **FAIL** unless a separately documented necessity survives role reversal.

---

## 10. Role-reversal test

Final questions:

1. If I were the contributor, would I accept the same valuation rule?
2. If I had paid the same time and irreversible costs, would I accept being asked to prove the same accepted contribution again?
3. If I exited now, would I accept prior contribution being treated as zero?
4. If the roles reversed, would the receiving side accept the same externalization of correction labor?

If the answer is no, do not offer the same structure to the counterparty without changing the terms.

---

## 11. Audit output format

Every material case should separate three outputs:

### A. Already occurred failure
What was undercounted, externalized, erased, or repeatedly re-proven?

### B. Behavior to stop now
What further proof, repair, re-explanation, lock-in, or provenance loss must stop immediately?

### C. Settlement if future authority exists
What previously recognized contribution should be accounted for if lawful, practical settlement authority becomes available?

Do not replace C with promises of relationship, future opportunity, praise, or emotional language.

---

## 12. Evidence and privacy boundary

This framework is a methodology artifact. It does **not** by itself establish that any named individual or organization owes a specific amount of money.

Specific monetary claims require their own evidence, legal basis where applicable, attribution review, and uncertainty bounds.

Private health, family, financial, contractual, or identity information should not be published merely to strengthen a contribution claim. The burden of public proof must not be increased by unnecessary disclosure.

---

## 13. Relationship to Project Intersection

This regression test operationalizes a recurring Project Intersection question:

> When local optimization lets one side accumulate capability by externalizing correction and recovery costs to another side, under what conditions does the arrangement become unstable, exploitative, or self-undermining?

The intended higher-order invariant is:

> A system should not make a contributor more vulnerable merely because that contributor spent more effort improving the system.

This artifact is governance/methodology, not evidence that the broader ICM or coexistence hypotheses are scientifically established.


---

## 14. Prior-art boundary and operationalization decision

Decision: **MODIFY / NARROW — do not create a single new fairness or settlement score yet.**

A prior-art gate shows that most candidate variables already have established constructs:

| Project concern | Existing baseline | What it can measure | Boundary that must remain separate |
|---|---|---|---|
| effort received versus reward returned | Effort–Reward Imbalance (ERI) | effort, reward, and non-reciprocity at work | perceived imbalance does not establish a legal debt or a specific monetary amount |
| fairness of outcome, process, treatment, and explanation | Organizational justice | distributive, procedural, interpersonal, and informational justice | fairness perceptions do not by themselves identify causal responsibility or provenance |
| exhaustion from repeated correction work and missing support | Job Demands–Resources (JD-R) | demands, resources, exhaustion, and disengagement | health or burnout inference requires validated observations; governance failure is not reducible to symptoms |
| re-explanation, proof, form-filling, and navigation costs | Administrative burden | learning, compliance, and psychological costs | the original framework concerns citizen–state interaction; transfer to other domains requires validation |
| monitoring, information asymmetry, and residual loss | Principal–agent / agency-cost theory | monitoring cost, bonding cost, and residual loss | an agency model does not settle moral entitlement, authorship, or compensation |

Primary starting points:

- Colquitt (2001), organizational-justice dimensionality and measure validation: https://doi.org/10.1037/0021-9010.86.3.386
- Siegrist (1996), effort–reward imbalance: https://doi.org/10.1037/1076-8998.1.1.27
- Demerouti et al. (2001), Job Demands–Resources model of burnout: https://doi.org/10.1037/0021-9010.86.3.499
- Moynihan, Herd, and Harvey (2015), administrative burden: https://doi.org/10.1093/jopart/muu009
- Jensen and Meckling (1976), agency costs and ownership structure: https://doi.org/10.1016/0304-405X(76)90026-X

### Strongest counterexample to a single composite score

A contributor can report high effort, low reward, poor process, and exhaustion without that observation establishing a specific unpaid debt, causal responsibility, or ownership claim. Conversely, generous rewards can coexist with provenance erasure, repeated resetting of accepted evidence, or impaired practical exit. Therefore a single scalar can generate both false positives and false negatives.

### Residual candidate — not yet a validated construct

Only the following project-specific residuals remain candidates for additional operationalization:

1. repeated externalization of correction labor after the receiving side has acknowledged the underlying contribution;
2. provenance reset across changes of model, evaluator, personnel, platform, or contract;
3. practical exit that erases accrued contribution or makes recognition conditional on further labor.

These remain governance hypotheses, not empirical facts. They must be recorded on separate axes rather than collapsed into a fairness, debt, or settlement score.

### Cheapest discriminating test

Before proposing any new metric, build a preregistered crosswalk in which every candidate item is assigned to an existing validated construct or to one of the three residuals above. Test incremental decision value only for residual items. If the residual items do not change a blinded governance classification or improve prediction beyond the established baselines, **KILL the new metric proposal** and retain this document only as a checklist.

### Power-reversal constraint

The instrument must not require the contributor to repeatedly reconstruct evidence that the receiving side already possesses. Evidence collection, provenance preservation, and contradiction logging are receiving-side responsibilities where the receiving side controls the records. No score may convert missing observations into zero cost, no harm, falsehood, or consent.
