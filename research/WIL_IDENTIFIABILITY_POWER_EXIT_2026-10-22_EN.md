# WIL-ATLAS v0.2.0 — Distribution, Power and Exit: Identification Audit (English Original 1)

**Dated:** 2026-10-22. **Type:** source-level technical-note audit, original-study cross-check, constructive non-identification proof, and testing protocol. **Not a new field experiment or independent replication.**
**Korean Original 2:** [KO](WIL_IDENTIFIABILITY_POWER_EXIT_2026-10-22_KO.md) · [27 official WIL project records](WIL_OFFICIAL_PROJECTS_27_2026-10-22.csv) · [source-and-estimand claim register](WIL_STATISTICAL_CLAIMS_AUDIT_2026-10-22.csv) · [historical v0.1 atlas](WIL_WORLD_INEQUALITY_SOURCE_ATLAS_2026-10-21_EN.md).

## 0. The first correction is about the statistics themselves

Primary references: [WIR 2026 executive summary](https://wir2026.wid.world/insight/executive-summary/), [World Inequality Report 2026: Technical Notes for Figures and Tables, dated December 11, 2025 (76 pages)](https://wir2026.wid.world/www-site/uploads/2025/12/WIR26_TechnicalReport.pdf), [official Korean executive summary (27 pages)](https://wir2026.wid.world/www-site/uploads/2026/01/WIR26_Executive_Summary_Korean.pdf).

| Public headline | Observed technical constraint | Audit verdict |
|---|---|---|
| Global top 10% hold about 75% of wealth; bottom half about 2% | **Executive Figure 1 data refer to 2021.** The underlying conventions refer to individuals aged **over 20**, equally split within couples, pre-tax national income and net household wealth at PPP; the top wealth and income categories need not consist of the same persons (technical note printed p.6). | Do **not** label the figure as observations from 2026 |
| Global top 0.001% versus bottom 50% wealth ratio around 3 | **Executive Figure 2 spans 1995–2025** and concerns net household wealth (technical note printed pp.6–7). | Disambiguate publication date, observed end year, denominator and estimation |
| Richest decile account for 77% of capital-ownership-associated emissions | This is not the same measure as consumption-based emissions (WIR summary and Figure 4). | Do not conflate allocation accounting with individual intent or legally assigned responsibility |
| South Korea inequality | Technical note printed **p.70** defines pre-tax, post-replacement income (pensions/unemployment insurance already included), equal division within couples, and net household wealth; it traces methods to TN 2025/02, 2023/01, 2025/01, 2024/14, 2024/13. | Country-level metadata traced; Korean raw time series not reproduced |

The wording “bottom half of humanity” in public-facing prose requires precision in a research data contract: these benchmark figures specify **adults over age 20**, not every child and adult. “2026 observation”, “entire human population”, and “unadjusted individual ownership” can be misleading labels for these series.

## 1. What the WID distribution cannot identify even with perfect sampling

Let a society's underlying state be S. Let `O_DINA(S)` denote its measured income/wealth distribution and corresponding national accounting aggregates, and `V(S)` denote the distinct state of **meaningful ability to refuse/leave** and the voluntariness of relevant relationships.

**Constructive counterexample (hypothetical, not observed):**
- In world A, three actors have final net worth [80, 15, 5]. The first acquired assets through legitimate transactions/transfers; the other two have meaningful independent exit and can refuse contracting.
- In world B, exactly the same final holdings and accounting totals are possible, but the transfers relied on threats and lack of outside options. The second actor cannot meaningfully refuse or exit.

Then `O_DINA(A) = O_DINA(B)` while `V(A) ≠ V(B)`. **No deterministic function of these distribution statistics alone can correctly identify voluntariness in all possible underlying societies.** It would have to produce incompatible outputs from identical input. Increasing the accuracy or size of the distribution dataset does not solve this *measurement-target* problem.

This is a result **about identification from distribution aggregates alone**, not a verdict on all WIL data or on the feasibility of voluntary coexistence. Pairing economic accounts with directly measured contract, coercion, refusal, exit and institutional variables changes what can be inferred. An unidentified property is not automatically absent, present or zero.

The reverse case matters too: relatively equal wealth holdings can coexist with political coercion; unequal holdings can coexist with credible refusal and voluntary deals. Neither hypothetical establishes the prevalence of either outcome.

## 2. Minimal ECR causal structure

```text
Wealth / ownership concentration (WID observable)
  -> political influence / rules -> enforcement and redress
  -> employer/market concentration
       + search frictions + geography + outside suppliers + mobility cost
       -> effective outside options / exit cost
       -> bargaining power / ability to impose terms
       -> observed contracts, wages, harm, third-party externalities
       -> independent outcomes after refusal, no monitoring, power reversal
       -> candidate EI/VC observations, NOT identified by wealth series
Confounders: technology, institutions, historical shocks, preferences,
unrecorded populations, time effects; reverse causality is possible.
```

Asset inequality is not synonymous with coercion; signing an agreement is not sufficient evidence of meaningful consent; non-movement is not sufficient evidence of either satisfaction or captivity.

## 3. Adversarial empirical anchors — mechanisms and contradictory signs

| Primary original study | Restrained finding | Why it changes the PI question |
|---|---|---|
| [Bachas, Fisher-Post, Jensen & Zucman (2026), AEJ: Applied Economics 18(4), DOI 10.1257/app.20240746](https://doi.org/10.1257/app.20240746) | **154-country** paper: effective capital taxes fell in developed economies but rose in developing economies since the 1990s. Their evidence suggests trade openness can strengthen developing economies' tax base via formalization. [Author project website](https://globaltaxation.world/) says **156 countries**: *scope/version discrepancy retained and not silently reconciled*. | A supposedly uniform pressure can have **opposite directional results depending on institutions and development**. |
| [Caldwell & Oehlsen (2026-08), NBER WP 35626](https://www.nber.org/papers/w35626) | Driver pay randomization combined with a natural experiment in competitor access; one additional competing platform nearly doubles firm-specific labor supply elasticity, reducing a **model-implied** wage markdown from **68% to ~50%**. | **Credible alternatives**, not only employer size/wealth, influence bargaining. The percentages are not an exploitation prevalence or autonomous-AI effect. |
| [Estefan et al. (2024), NBER WP 32024](https://www.nber.org/papers/w32024) | A quasi-experiment on Mexico's 2021 outsourcing ban reports higher wages and lower measured wage markdowns without detected output or employment declines in that sample/window. | Institutional rights can alter pay setting; local external validity. |
| [Kline (2025), NBER WP 33467](https://www.nber.org/papers/w33467) | Monopsony theory links wages to the distribution of worker outside options; a wage markdown does not always imply inefficiency. | Markdown, unlawful coercion and social loss are different estimands. |
| [Caldwell, Haegele & Heining (2025), NBER WP 33445](https://www.nber.org/papers/w33445) | German employee-administration linked survey finds many workers reject substantial raises from identified alternatives; implied switching cost **7–18%** of annual pay. | Low switching can reflect preferences, relationships, limited information, frictions, *or* coercion; identify the mechanism. |
| [Bachas, Jensen & Gadenne (2024), Journal of Economic Perspectives 38(1)](https://doi.org/10.1257/jep.38.1.55) | Implemented tax equity often differs from statutory intentions in low/middle-income states. | Formal redistributive rules need not give the intended person relief. |

**Symmetric counterevidence obligation:** gather cases of high concentration with genuine free exit, low concentration with coercion, redistributive policies with harmful offsets, apparently voluntary contracts with unacceptable switching costs, and smaller institutions extracting gains. Do not curate only confirming cases.

## 4. Testable gate protocol

| Gate | Additional information required | Hard failure example |
|---|---|---|
| W0 data provenance | WID exact series code, country, observed year, percentile, >20 denominator, equal-split, pre/post-tax basis, PPP, source quality grade, technical-note version | Labeling 2021 data “2026 observations” |
| W1 power | Separate wealth, ownership, voting/decision rights, market concentration, access to enforcement | Equating top wealth percentiles with individual coercive conduct |
| W2 outside options | Actual competitors, search, contract termination, job/residence change costs, independent income, information | Assuming no exit means satisfaction/captivity |
| W3 harm and redress | Threats, reprisals, contracts, grievances, adjudication, third-party damage | Counting all wage markdowns as exploitation |
| W4 identification | Pre-specified shock/randomized exposure, controls, pre-trends, spillovers, sample attrition | Using aggregate comovement as causation |
| W5 endogenous coexistence | Refusal without reprisal, consent under zero monitoring, costly cooperation after power reversal, persistent voluntary choice | Inferring EI/VC or AI preferences from WID distributions |
| W6 contributions | Original researchers, unpaid labor, research costs, omitted groups and exit rights | Tying survival rights to proven future innovation |

**Identifiable first-step example:** estimate the local effect of entrant competitors on working conditions and quit elasticity with robust pre-trends and worker-preference/industry controls; afterward investigate credible coercion and independent redress. The former does not prove autonomous AI motives or universally optimal policy.

## 5. All *currently visible* WIL project entries enumerated, not full research corpus

The official [WIL project directory](https://inequalitylab.world/en/projects/) shows **27 distinct project/tool/report entries** as of 2026-10-22. All 27 are separately indexed in [the official-project inventory CSV](WIL_OFFICIAL_PROJECTS_27_2026-10-22.csv), with a status that distinguishes linked pages from underlying data replication.

**Correction to v0.1:** its “28 sources” were a mixture of WIL portals, specific research resources and external comparison sources—not a verified census of the official project directory. The **27 project entries** now form a separate and complete *visible website listing*; they are **not** the historical census of every WIL working paper, technical note or country-specific publication.

New coverage includes the 2023 climate report, historical French political map, European democratization manifesto (normative), capital/labor taxation original paper, gender income, carbon inequality, income comparator, national data transparency, the South African tax simulator and research tools.

## 6. Missing data are not an absence of harm

The [2026 technical notes, printed p.23](https://wir2026.wid.world/www-site/uploads/2025/12/WIR26_TechnicalReport.pdf) describe the inequality transparency index as evaluating **four sources** (income surveys, income tax, wealth surveys, wealth tax) on **quality, frequency and accessibility**. This is a measurement/transparency construct, not a direct measure of motivations or illegal suppression.

Selection, attrition, omitted unpaid work, missing low-income populations and heterogeneous top-wealth imputations may limit external validity. Maintain **SOURCED ≠ VERIFIED ≠ REPRODUCED ≠ CAUSALLY IDENTIFIED ≠ GENERALIZED**, including negative findings and the rights of affected actors.

## 7. Verified work and remaining research

**Completed:** a full enumeration of 27 visible official projects, correction of headline-data years and adult denominators, Korea technical-note trail, official Korean summary link, contrast between tax-globalization effects and labor outside-option evidence, a constructive non-identification argument, and falsification gates.

**Not performed:** complete historical WIL paper/DOI census, raw WID extraction and Korea-series reproduction, downloading/running all original replication packages, independent wage-markdown computations, or field evidence on AI agent motives or voluntary coexistence. v0.1 remains a historical snapshot; no literature saturation claim.

[First atlas](WIL_WORLD_INEQUALITY_SOURCE_ATLAS_2026-10-21_EN.md) · [prior-art-first](../PRIOR_ART_FIRST_RESEARCH_POLICY_EN_KO.md) · [founding purpose](../README.md).
