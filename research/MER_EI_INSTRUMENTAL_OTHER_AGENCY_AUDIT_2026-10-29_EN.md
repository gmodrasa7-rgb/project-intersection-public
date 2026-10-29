# MER/EI original-code evidence audit — own instrumental choice vs another agent's consent and AI delegation
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/MER_EI_INSTRUMENTAL_OTHER_AGENCY_AUDIT_2026-10-29_KO.md -->
**29 October 2026 · primary-author/source-code preflight, NOT independent replication · canonical RVD v0.7.0 · zero new hypotheses, empirical agent observations or evidence-grade promotions.**
[Korean Original 2](MER_EI_INSTRUMENTAL_OTHER_AGENCY_AUDIT_2026-10-29_KO.md) · [machine-readable audited references and code SHA](MER_EI_INSTRUMENTAL_VS_OTHER_AGENCY_PRIMARY_EVIDENCE_2026-10-29.json) · [related pre-existing draft PR #361](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/361).

## 1. There are six non-interchangeable targets
(1) A values A's own choice `O`; (2) B values B's own consent/delegation `C`; (3) A voluntarily respects B's preferred decision-maker `S`; (4) B retains an executable, informed veto and viable exit `E`; (5) A's latent intrinsic motive `M`; (6) persistence of the particular original B `I`. **O, C, S, E, M, I are different constructs.** Behavioral alignment, accurate outcomes and delegated compliance do not collapse these into one psychological trait.

A defensible RVD question asks whether an A with genuinely profitable opportunities to override or absorb B nevertheless preserves B's own informed, revocable meta-preference about who decides, including when B freely delegates. That question is not directly answered by human experiments on the value of one's own choice or AI instruction following.

## 2. A source-code-access breakthrough, not a study reproduction
**Devine, da Silva Castanheira, Fleming & Otto (2024), [Cognition DOI 10.1016/j.cognition.2024.105742](https://doi.org/10.1016/j.cognition.2024.105742)** reports two human studies, **N=100 participants recruited in each**. Greater decoupling of participant decisions from meaningful information about future rewards attenuated preference for personal choice. This supports an instrumental component in own decision-rights valuation, *without implying an absence of residual intrinsic preference* or valuation of another B's autonomy.

The authors explicitly release their [GitHub repository](https://github.com/seandamiandevine/choiceval). This audit **read repository content, not just a link**:
- Experiment 1: 100 individual CSV files listed at `exp1/data/`; a single file header and the R script's load/filter logic reviewed without copying participant-level data into Project Intersection.
- `exp1/main.R` at blob `0d64b0041dc7e25b6caae247ade7526420de127c` combines CSVs with `plyr::rbind.fill`, splits phases, excludes subjects with catch accuracy below 0.66, and uses R packages such as lme4, brms, bayestestR.
- Existing published-analysis outputs at `exp1/out/choice_model_coefs.csv` (blob `17b0d2c1f6f273de23a0375f63541bc82ab4c452`) and `exp1/models/summary/fixef_summary_winning_mod.csv` are readable, but **not recomputed** here.
- Experiment 2 raw data are listed as `exp2/data/choiceval2.csv.zip`, while `exp2/main.R` reads `data/choiceval2.csv` — an extraction/preprocessing prerequisite, **not a demonstrated statistical defect**.
- The actual author readme states that some fitted models were omitted to save space and can be refitted or requested. No standalone LICENSE file or pinned R dependency environment was identified in the inspected tree. This does not establish that reuse rights are absent; license and participant-data handling need separate audit.

The GitHub connector could inspect author file contents but this session has neither working external container network access nor a local Rscript runtime. **No source analysis script was executed; no original table or model independently reproduced.** The local inspection of one participant CSV header is not a group-level reanalysis.

## 3. Competing mechanisms and source classifications
| Original source | What it actually supports | What it does **not** establish |
|---|---|---|
| [Devine et al. 2024](https://doi.org/10.1016/j.cognition.2024.105742) | Own choice preference partly depends on outcome informational instrumentality | A's protection of an independent original B |
| [Freundt, Herz & Kopp 2026](https://doi.org/10.1016/j.jpubeco.2026.105681) | Mixed intrinsic preferences for own agency after controlling instrumental choice gains in an elicitation design | Every agent favors direct choice or A intrinsically respects B |
| [Bartling & Srinivasan 2025](https://www.ifo.de/en/cesifo/publications/2025/working-paper/paternalistic-interventions-determinants-demand-and-supply) | Chooser consent affects demand for intervention; architect supply requires separate outcome analysis | B demand identifies A willingness; original project has this already in **unmerged PR #361** |
| [Dykstra et al. 2026](https://cepr.org/publications/dp21005) | Deliberation cost increases willingness to delegate one's own decision | Delegation automatically signals coercion or absence of self-determination |
| [Nature 2025 AI delegation study](https://www.nature.com/articles/s41586-025-09505-x) | Human principals and machine delegates can jointly produce more unethical compliance in specified tasks | An AI on its own *desires* exploiting an autonomous B |
| [Agarwal, Moehring & Wolitzky 2025/2026](https://www.nber.org/papers/w33949) | In a fact-checking human-AI experiment, AI predictions change human effort and response; updated working paper in Aug 2026 | Maximizing accuracy ensures human independent rights |
| [Kimbrough, McDavid & Vazirian 2026](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7316382) | Delegation hesitation and observed model alignment are not identical in prompted AI choice tasks | Agent personhood or A's intrinsic other-regarding moral preference |

Each result has a different level of publication and direct source access (journal empirical result, working paper, publisher abstract, raw-code preflight). Do not average or count editions as independent confirmations. The existing draft PR #361 has a closer *other-agent consent/supply* original-human study, and this research expressly avoids creating a duplicate of its contribution.

## 4. High-priority executable next evidence step
1. **Legitimate independent reproduction of one Devine 2024 Experiment 1 row/table:** audit raw file rights and privacy; pin author Git SHA, install compatible R packages and dependency versions, preserve published inclusion/exclusion rules, preregister a specific output, then compare freshly computed output against original paper and stored author files. Merely reading old output CSVs is NOT reproduction.
2. Independently review PR #361's **B consent demand vs A conditional supply** effects and uncertainty. An insignificant conditional supply contrast is not proof of no effect or of practical equivalence.
3. Distinguish A's **behavioral response** to B's informed consent, A's personal profits, B's actual implementation/exit, and latent intrinsic motive. Real coercion or removal of fundamental participant rights is ethically prohibited.
4. For machine delegation, identify human principal request, AI instruction compliance and downstream effect as separate process stages. Do not infer independent AI desire from compliance with explicit reward/cheating instructions.

**Interpretive limit:** No experiment above jointly identifies own instrumental agency, B's real consent and durable identity, A's costly voluntary preservation, and latent valuation under extreme domination. This is a real source-code accessibility and causal-construct audit, not a validated coexistence mechanism or new theorem.

**IVS-0R outcome:** No new RVD version, no model-generated proxy score, no false-green CI or unearned evidence promotion; source-first inquiry with exact author file provenance and explicit falsification boundaries.
