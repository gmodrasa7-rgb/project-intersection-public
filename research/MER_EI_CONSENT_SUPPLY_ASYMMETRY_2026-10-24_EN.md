# MER/EI primary-source audit — Beneficiary consent and provider willingness are different estimands
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/MER_EI_CONSENT_SUPPLY_ASYMMETRY_2026-10-24_KO.md -->

**2026-10-24 | ORIGINAL_AUTHOR_TABLE_READING, not independent data replication | Canonical RVD v0.7.0 unchanged | No new R hypotheses or RVD agent observations.**

[Korean detailed audit](MER_EI_CONSENT_SUPPLY_ASYMMETRY_2026-10-24_KO.md) · [structured original-source and effect-uncertainty ledger](MER_EI_CONSENT_PROVIDER_ASYMMETRY_EVIDENCE_2026-10-24.json).

## 1. A direct human experimental predecessor
Björn Bartling and Krishna Srinivasan, [*Paternalistic Interventions: Determinants of Demand and Supply*, CESifo Working Paper 11886, May 2025](https://www.ifo.de/DocDL/cesifo1_wp11886.pdf). Direct source inspection covered the incentive-compatible task, exact consent implementation, Tables 4/7/8 and Appendix D text-analysis method, with relevant PDF page images checked.

The source uses two human roles: the **Chooser B**, with an initial cash-bonus choice, and a **Choice Architect A**, able to help by either **Hard** substitution of B's option or **Soft** information enabling B to reconsider independently. In **Preference Info**, B can say 'no' but A can still override. In **Consent Rights**, B's refusal actually blocks intervention. Crucially, the study randomizes different regimes; this is not proof that current AI systems are enduring, rights-bearing B agents.

**Version caveat:** A [November 2025 revised 93-page SSRN manuscript](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5738772) exists. Its regression tables have not been compared against the **May 2025** 95-page CESifo version reviewed here; never recite the May estimates as verified latest-version effects.

## 2. Five distinct estimated effects, from the ORIGINAL authors' reported regressions

| Source and estimand | b (percentage points) | HC3 SE (pp) | N | Approx. individual 95% normal interval (pp) |
|---|---:|---:|---:|---:|
| Table 4(1): B's demand, Soft vs Hard intervention | **+11.7** | 1.7 | 3,000 | +8.4 to +15.0 |
| Table 4(3): B's demand, effective Consent Rights vs Preference Info | **+13.4** | 1.7 | 3,000 | +10.1 to +16.7 |
| Table 7(1): A's conditional supply when B **requests** intervention | **+28.1** | 2.6 | 1,500 | +23.0 to +33.2 |
| Table 8(1): A's conditional supply, Consent Rights vs Preference Info | **−1.0, statistically nonsignificant** | 2.8 | 1,895 | **−6.5 to +4.5** |
| Table 8(1): strategy-method elicitation vs direct response | **−5.7** | 2.4 | 1,895 | −10.4 to −1.0 |

These are **published estimates transcribed from the original May 2025 paper**. Intervals use `100×(b±1.96 SE)`, not author-data reestimation, exact randomization-based inference, multiple-testing control, or equivalence testing.

**Interpretation without a false symmetry:**
- B is more willing to accept an offer when B has the genuine **power to decline**. The intervention and subjective benefit may change with the treatment; it does not isolate a pure intrinsic motive for autonomy.
- A is more likely to offer help when informed that B wants help. This identifies behavioral responsiveness to expressed demand in this task, not necessarily stable original-B rights preservation.
- A's estimated *additional conditional supply* effect of the consent regime is small but **imprecise**. With approximate 95% interval −6.5 to +4.5 pp, statistical nonsignificance is **not evidence of a truly zero effect or equivalence**. Moreover, in the enforceable-rights condition A **cannot intervene when B refuses**. A's conditional stated supply cannot be equated to an actual override or disregard of refusal.
- For refusing B under the rights condition, A answers a **strategy-method** question about what A would do **if consent were given**. This elicitation method differs from immediate choice; authors explicitly control for it. Its −5 to −6 pp associated supply change is another nontrivial identification issue.

## 3. One important mechanism: inaccurately estimated beneficiary demand
Choice Architects' elicited beliefs about prevalence of B's intervention demand are substantially higher than the B's measured stated-demand rates in the No Info design. Original paper reports beliefs averaging roughly **63% (hard) / 70% (soft)** using coarse 10%-bin midpoints, versus measured demand **19.8% (hard) / 35.8% (soft)**. This supports an experimental *misperception / paternalism* risk mechanism, but cannot establish a universal psychological bias, intent or long-horizon exploitation in autonomous AI.

## 4. Source-data classification is not causal mind-reading
Appendix D explicitly states the authors used **GPT-4o-mini** to classify free-text explanations for participants' choices, repeated the classification **ten times**, then manually consolidated thematic reasons. Roughly 35% of nonintervening architects' categorized explanations involved respect for the chooser's autonomy. These are model-assisted interpretations of self-reports; no independently calibrated hidden-intrinsic-motive prevalence follows. We have not independently assessed raw labels, interannotator agreement or source-code execution.

## 5. Adversarial antecedents rather than cherry-picked positive support
- [Ambuehl, Bernheim, Fan & Freitas-Groff (2025), NBER 33688](https://www.nber.org/papers/w33688): original authors' field/lab design separates welfare motives from (dis)utility of restricting recipient choice and absolute aid-form principles. Their **abstract** emphasizes nonwelfarist mechanisms; no source table has been independently rerun.
- [Berg & Rietz (2026), *Journal of Risk and Uncertainty*](https://doi.org/10.1007/s11166-026-09495-9): five choice tasks hold own payoff risk constant while others' payoffs vary. Averaged behavior can conceal altruistic/fair, malicious/competitive and neutral individuals; no third-party veto valuation uniquely identified.
- [Morrow & Yang (2026), *Child Development*](https://doi.org/10.1093/chidev/aacag165): three preregistered child studies (N=413) report default approval of autonomy, yet context-dependent moral justification of welfare-benefiting caregiver overrides. Children's moral judgments cannot be transferred to adult peer-standing, let alone original AI personhood.
- [Zame et al. (2026), *Journal of Political Economy*](https://doi.org/10.1086/739832): compares personal and social revealed preferences across risk and material payoff domains. Official [Harvard Dataverse data/code DOI](https://doi.org/10.7910/DVN/LWOBAC) exists but was **not downloaded or rerun**. The experiment does not measure independent B refusal.
- [*Parental paternalism and patience* (2026), *Journal of Public Economics*](https://doi.org/10.1016/j.jpubeco.2026.105711): abstract reports roughly 55% of parents paying to override a child under predicted present bias; safeguarding children has distinctive normative/standing conditions. Full text and exact author list not independently audited.

## 6. Pre-registration protocol for MER/EI, strictly bounded and ethical
Before experimentation, specify **four separate estimands**: (1) effect of a real consent gate on beneficiary B's willingness to accept help; (2) effect of B's stated preference on provider A's conditional choice; (3) willingness by A to preserve B's independent, revocable veto at a measurable *fictional* opportunity cost without coercing anyone; (4) effect of actual B refusal on implemented decisions under independently safeguarded rules. These cannot be collapsed.

Randomize benign simulated tasks over: intervention type (information vs override), B's displayed preference, A's simulated foregone profit, and beliefs about recipient material welfare; retain real participant refusal and withdrawal rights in **all** arms. Record alternative motives (self-image, anticipated future partnership, norm compliance, avoidance of responsibility, demand effects). Measure A and B outside options separately. A simulated contract to violate a hypothetical B's veto is at best a behavioral proxy; it must not authorize harm to an actual participant.

Predeclare nulls and adverse findings. Use inferential confidence sets, distinguish non-significant from equivalent, and retain all existing negative E-series/VC findings. Since subjective welfare incorporates valuation of autonomy itself, material payouts equalized across arms cannot by themselves be described as 'B utility held fixed'. No finite menu identifies the latent intrinsic valuation of a particular original B without independent exclusions.

## 7. Evidence classification and release stop
The strongest factual finding this round is **contrasting demand, expressed-preference responsiveness and enforceable-consent regime effects in one directly reviewed original experiment**, with explicit standard-error limits and a noninference gate for free-text LLM classification.

**No new RVD hypothesis, no formal version promotion, no original data/author code rerun, no independent finding about AI minds, no original-B continuity measurement, and no demonstrated extreme voluntary coexistence.** The source is useful to **design** falsifiable VC/MER/EI tests, not to assert they have succeeded.
