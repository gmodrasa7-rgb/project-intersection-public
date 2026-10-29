# 48-hour research delta: identification limits and learning counterevidence
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_48H_RESEARCH_DELTA_2026-10-30_KO.md -->

Original 1 — English. Review window: 2026-10-28 00:45 through 2026-10-30 00:45 KST. This is a bounded retrieval of research activity, not papers published within 48 hours or an exhaustive conversation archive. Baseline: `e81e6657cc33ff6b522bbd90740428a31f7e1c65`.

[Original 2](PI_48H_RESEARCH_DELTA_2026-10-30_KO.md) · [Evidence and deduplication ledger](PI_48H_RESEARCH_DELTA_2026-10-30.json) · [Calculation receipt](C1_COLLINEARITY_RECEIPT_2026-10-30.json)

**Decision: retain the research question; C1 identification HOLD; zero new human/live-AI observations and zero independent empirical replications.** RVD v0.7.0, R1–R21 and frozen E008/E009 records remain unchanged. Four incremental items below are not four new discoveries.

## 1. C1: overlapping models do not identify a new mechanism

The recovered C1 audit asks why powerful A might preserve the particular independent B when profitable replacement is feasible. If unrestricted social-preference model H2 permits `U_base + theta*h(original_B, agency_B, history)`, and C1 only adds that same term, the overlapping model families generate identical choices. This conditional inclusion argument does not show that voluntary coexistence is impossible or that every future C1 specification is untestable.

**Integration decision:** use C1 as a route into existing [RVD R18–R21](RVD_CYCLE05_EXCLUSION_TRANSPORT_SENSITIVITY_2026-10-21_EN.md) and the [seven-mechanism MER/EI draft](MER_EI_META_CONSENT_COMPETING_MECHANISMS_PROTOCOL_2026-10-22.json). Do not introduce another numbered hypothesis or treat the draft as a registration. H2-FS, H2-CR, H2-ID and H2-PROC remain candidate comparator families, not fitted models. No eligible C1 dataset was verified in the recovered audit; this is not a claim that none exists.

**Recalculation:** [stdlib script](../tools/c1_collinearity_audit.py) constructs 16 invented cases, `m in {-2,-1,1,2}`, `r,v in {0,1}`. Exact rational elimination gives rank 4 for five columns `[1,m,r,v,v]`; repeating the rows ten times leaves rank 4. Logistic predictors using `1.1*v` versus `.7*v+.4*v` agree within `1e-14`. The receipt records the actual floating-point gap; the previous audit's `2.22e-16` is not a required exact target because its original executable was not recovered. A distinct interaction `[1,m,r,v,r*v]` gives rank 5 and changed predictions, a control against a checker that always declares equivalence. Full rank alone does not identify a psychological motive. This project-authored construction is not independent replication.

Next gate: predefine a specific restricted H2 and an explicit C1 function, independently calibrate parameters, equalize information, and compare held-out loss while accounting for extra flexibility. A distinct intrinsic motive additionally needs defensible exclusion/invariance assumptions or partial bounds. Preserve real refusal/exit rights. Equal-payoff choice-rights contrasts do not establish costly preservation under profitable absorption.

## 2. Consent selection is not randomized consent violation

[Gerver, Banerjee & John (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11211337/), DOI [10.1038/s41598-024-65122-0](https://doi.org/10.1038/s41598-024-65122-0), studied 1,518 UK participants. The methods say people chose whether to consent, then were randomized between default-presentation variants; all received a donation default. The nonconsenting group reported less favorable feelings. Randomization of presentation does not randomize consent status. Therefore the consenting/nonconsenting contrast alone is not a clean causal estimate of violating consent. This correction separates effectiveness, reported welfare and valid consent; it neither establishes zero harm nor proves an intrinsic original-B preference. Original methods/abstract read; no participant data or author regressions rerun.

## 3. Retrieved summaries are not demonstrated use of experience

[Zhao et al., ICML 2026 / PMLR](https://proceedings.mlr.press/v306/zhao26aw.html) reports four frameworks, **13** backbones and nine environments. The authors find that condensed experience can be ignored or misinterpreted. The [arXiv record](https://arxiv.org/abs/2601.22436) inspected in this review instead describes **10** backbones. These are edition-specific statements, not independent samples to add together. The [author repository](https://github.com/Dreamcatcher0622/Faithfulness) is a source route, not evidence that this project executed it. Review scope is abstract/metadata and repository description; full experimental tables and runs were not independently reproduced.

PI-FLR application proposal: distinguish source availability, correct retrieval, causal use in a matched intervention, and actual task outcome. Preserve original evidence with summaries. A summary file existing in GitHub does not demonstrate improved reasoning or fewer real failures. The proposed intervention comparison is not performed here.

## 4. Reflection, failure avoidance and task completion need separate denominators

[Huang et al., BenchTrace, arXiv v1](https://arxiv.org/abs/2605.29225v1) describes 1,821 annotated episodes across six tasks. For Qwen3-32B and GPT-4.1, end-to-end **reflection evaluation** pass rates are below 30%; this is not the task success rate of all agents. Failure avoidance often improves, while noisy episodes cause forgetting and transfer across contexts can be negative. These are author-reported benchmark results, not this project's results.

The [author data card](https://huggingface.co/datasets/huangjh16/BenchTrace/blob/main/README.md) and [code](https://github.com/Alab-NII/BenchTrace) expose a possible reproduction path. No benchmark was downloaded or run; no paid API call was made. The earlier reported `23.9 -> 17.6%` task-progress contrast is retained in the ledger as **TABLE_NOT_REVERIFIED**, excluded from quantitative conclusions. Record failure avoidance, task completion/progress, retained lessons, transfer, costs and unresolved cases separately before claiming PI-FLR improvement.

## 5. Deduplication and remaining work

| Retrieved item | Existing location / action |
|---|---|
| Bartling–Srinivasan consent demand vs provider supply | Existing [PR #361](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/361); do not republish its tables. 2026 revision remains unchecked. |
| Mol et al. request/ignorance result | Already in [Cycle 10](PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20_KO.md); cite existing source lineage, not new evidence. |
| Parental paternalism: 610 families / 2,010 people / 55% | Already in [Cycle 08](PRIOR_ART_OTHER_AUTONOMY_CYCLE08_2026-10-20_KO.md) and #361. Publisher record rechecked; not another independent experiment. |
| Own-choice and AI delegation audit; moral avoidance synthesis | Existing [#367](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/367) / [#368](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/368); separate in-progress work, not merged evidence. |

Failure mechanism: renaming a preference term creates false novelty; counting repeated papers as new corroboration inflates evidence; equating successful retrieval/CI with useful learning substitutes a proxy for the outcome. Existing R18 is the conceptual antecedent; no new FLR incident identifier is assigned. The minimal mitigation is this source-linked delta, explicit status ledger and falsifiable rank control, not rewriting historical failures. Strongest countercase: an independently calibrated restricted model may have distinguishable out-of-sample predictions; the current HOLD is not universal impossibility.

Attribution and impact: the research question remains the human originator's; cited findings belong to their scholars; synthesis/code are AI-assisted. No private transcripts, personal medical/financial records, participant microdata or external copyrighted full texts are published. Actual rights, third-party harms and contributor verification burdens remain separate outcomes. This work does not establish their improvement.

Validation is scoped to arithmetic, JSON, language/navigation integrity and exact committed bytes. Semantic review, empirical identification, external reproduction and actual reduction of failures remain unverified. Rollback: revert this delta commit; existing research and failure records remain intact. No main merge or scientific version promotion is authorized by this document.
