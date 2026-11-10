# Independent raw-data reanalysis: *Free to Fail?* — IVS-0R evidence repair
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/MER_EI_FREE_TO_FAIL_INDEPENDENT_RAW_REANALYSIS_2026-11-10_KO.md -->

**2026-11-10 | AUTHOR-DATA INDEPENDENT REANALYSIS | NOT NEW HUMAN EXPERIMENT | NOT AUTHOR-STATA FULL RERUN | RVD v0.7.0 UNCHANGED.**

[Original 2 — Korean](MER_EI_FREE_TO_FAIL_INDEPENDENT_RAW_REANALYSIS_2026-11-10_KO.md) · [Machine-readable receipt](MER_EI_FREE_TO_FAIL_INDEPENDENT_RAW_REANALYSIS_2026-11-10.json) · [Independent runnable script](../experiments/mer_ei/independent_free_to_fail_replication.py) · [Prior access-failure ledger](MER_EI_FREE_TO_FAIL_PRIMARY_RESULT_REPRO_GATE_2026-10-21.json) · [Prior partial-identification proof](MER_EI_SOFT_HARD_PARTIAL_IDENTIFICATION_2026-10-22_EN.md).

## 1. New contribution versus work already preserved

This project's 2026-10-21 ledger had verified the original **2023 paper**, but recorded `OPEN_LISTED_NOT_DOWNLOADED`: zero original archive bytes, no checked raw variables, and no reproduced model. The 2026-10-22 project document **already independently derived Fréchet bounds** for unobserved joint acceptance types using rounded published percentages. **Those mathematical bounds are not a new discovery here.**

**New operational delta:** actual Zenodo archive and README bytes obtained; publisher-listed MD5 verified; all seven experimental cells independently counted from the authors' de-identified CSV data; the two 2023 paper regression tables independently rebuilt with NumPy rather than Stata (eight OLS models, HC1 heteroskedasticity-robust standard errors). An independent implementation on the **same authors' sample** is not an independent-sample replication, independent external laboratory, or an RVD experiment.

## 2. Source, environment, permission and freeze points

- Authors: Björn Bartling, Alexander W. Cappelen, Henning Hermes, Marit Skivenes, Bertil Tungodden. *Free to Fail? Paternalistic Preferences in the United States*, *The Economic Journal* (published online 2026-10-29), DOI [10.1093/ej/ueag136](https://doi.org/10.1093/ej/ueag136). The older 2023 author draft provides the printed regression Tables 2 and 3 used below; a direct row-for-row check against the final 2026 typeset tables is **NOT VERIFIED**.
- Official original author data: [Zenodo record 23420381](https://doi.org/10.5281/zenodo.23420381), package `3-replication-package.zip`, MD5 `7f1ebe690e3704d8ba81409626834b77`; `README.pdf`, MD5 `409f958d3c6f4f5490f776c66dd7a602`. Both locally downloaded and MD5-matched the public record on 2026-11-10.
- The original README states the authors have permission to redistribute de-identified data and that participant identifiers were excluded. **No respondent-level records, extracts, ZIP or participant attributes are committed to this repository.** Only reproducible code and aggregated counts appear here. The authors' data and scholarship retain upstream attribution.
- Original reference implementation: `1_BCHST_build_samples.do`, `2_BCHST_pool_samples.do`, `3_BCHST_analysis.do`, requires Stata 17+ and SSC extensions. Stata was unavailable in this execution environment. Independent reanalysis uses Python 3/NumPy and the in-archive CSVs without extracting respondent files to disk.
- Frozen public project comparison: `main` SHA `e81e6657cc33ff6b522bbd90740428a31f7e1c65`. Reanalysis does **not** change original 2026-10-21/22 failure or partial-identification records.

## 3. Observed aggregate results

| Study and randomized arm | Positive choice | N | Rate |
|---|---:|---:|---:|
| Study 1, hard/internal | 673 | 2,008 | 33.52% |
| Study 1, soft/internal | 1,714 | 1,994 | 85.96% |
| Study 1, hard/external | 600 | 2,000 | 30.00% |
| Study 1, soft/external | 1,752 | 2,002 | 87.51% |
| Study 2, hard/internal | 710 | 2,006 | 35.39% |
| Study 2, soft/internal | 1,651 | 2,001 | 82.51% |
| Study 2, welfare/mandatory: allocation of safe option | 1,415 | 2,026 | 69.84% |

Study 1: 8,004/8,004 source records retained; unadjusted pooled soft-minus-hard = **+54.9753 percentage points**, HC1 95% normal-approximation confidence interval **[+53.1908, +56.7597] pp**. Study 2: 6,033/6,033 retained; soft-minus-hard within internal condition = **+47.1149 pp**, analogous interval **[+44.4404, +49.7895] pp**. Confidence intervals are *sampling intervals for treatment contrasts*, not confidence intervals on latent-type fractions or intrinsic motives.

Study 1's interaction of intervention type with external rather than internal error = **+5.0706 pp** (robust SE **1.8200 pp** in the four-arm saturated OLS). This is a real paper contrast, not an independent new causal mechanism. Pre-registration deviations and multiple testing considerations remain in the original author appendices.

## 4. Independent regression and negative-control verification

For Study 1, independently constructed six models: soft only, soft plus six published binary controls, external only, external plus controls, soft/external/interaction, interaction model plus controls. For Study 2, independently constructed welfare-reference hard/soft indicators with and without those controls. **8/8** models reproduce the 2023 authors' displayed principal coefficients to three decimal places, including the Study 1 soft coefficient `0.550` (HC1 SE `0.009`), interaction `0.051` (HC1 SE `0.018`), and Study 2 welfare-reference soft `0.127` (HC1 SE `0.013`), hard `-0.344` (HC1 SE `0.015`). Complete aggregate model coefficients and standard errors are generated by the script, not asserted as an independent author's Stata run.

Validation performed: exact archive MD5; exact verbatim treatment choice matching; exactly one answered treatment screen; complete category checks; expected sample counts; eight model coefficient checks; **2/2 adversarial controls** (forged intervention text, double-answered treatment screen) rejected. A wrong-archive MD5 also stops processing. The original Stata 24-exhibit workflow, Romano-Wolf resampling, authors' results for all outcomes and final 2026 article table-by-table reproduction were **not executed or certified**.

Reproduction from a legitimately obtained original ZIP:

```bash
python3 experiments/mer_ei/independent_free_to_fail_replication.py --archive 3-replication-package.zip
```

The script prints aggregated JSON only. It refuses unknown archive bytes, altered answers and invalid treatment assignment. Local script run finished successfully on 2026-11-10. There is no claim that another external lab independently repeated this work.

## 5. IVS-0R inversion: mechanism and generalization boundaries

- **Role reversal:** spectators choose for other people, not themselves. Observed spectator preferences do not establish the beneficiary's real ex post freedom or approved delegation. In Study 2, about **30.16%** selected the risky option even when forced to choose between safe and risky outcomes, illustrating that a substitute evaluator may disagree with the stakeholder's stated welfare preference; this **does not** diagnose malign intent.
- **Meta-consent and effective exit:** a soft information treatment preserves a displayed option set, but does not separately measure valid permission to intervene, manipulative framing, enforcement of veto, exit cost, future retaliation, independent survival or AI identity. The project already treats free delegation and forced direct choice as distinct; do not erase that precedent.
- **Latent types:** recomputing the pre-existing classical bounds from exact raw marginals yields Study 1 pooled `soft-only` **[54.975%, 68.239%]** and Study 2 internal **[47.115%, 64.606%]** as *estimated identification bounds*, not population confidence regions and not a newly invented method. The older project calculated source-condition bounds from rounded published percentages.
- **Strongest competing mechanisms:** direct dislike of coercion; information as a lower-cost or more effective instrument; perceived responsibility; social desirability; expectations about beneficiaries' choices. Randomized treatment contrasts identify process-sensitive choices under the authors' design, not the unique intrinsic motive or future strong actor's preservation of original B.
- **Independent counterevidence:** Wilson and Wu (2017), *Games and Economic Behavior*, DOI [10.1016/j.geb.2017.02.007](https://doi.org/10.1016/j.geb.2017.02.007), found cooperation efficiency in repeated partnerships can be highly sensitive to the *asymmetry* in outside options; exit freedom alone is not a monotonic cooperation guarantee. Bushong et al., [NBER WP 27681](https://www.nber.org/papers/w27681), revised July 2025 (not peer reviewed), report more persistent uptake of expert recommendations under greater agricultural input autonomy after two years. These are **other original studies**, not independent reproductions of this study or RVD.

## 6. Failure accounting and gates

| Gate | Exact present status |
|---|---|
| A0 original source lineage | `PASS_2023_TABLES_AND_2026_JOURNAL_METADATA`, complete final 2026 printed results `HOLD` |
| A1 original ZIP/PDF bytes | `PASS_MD5_MATCHED` |
| A2 README/software/privacy | `PASS_READ`, author Stata 17 rerun `NOT_RUN` |
| A3 sample and treatment identification | `PASS_14037_ROWS_7_CELLS` |
| A4 independent arithmetic and 2023 printed headline tables | `PASS_8_OLS_MODELS_2_NEGATIVE_CONTROLS` |
| A4 full 2026 paper and all 24 exhibits | `HOLD_NOT_RUN` |
| A5 original-B/AI intrinsic autonomy motive | `HOLD_NOT_IDENTIFIED` |

**KEEP** source-matched human behavioral contrast; **MODIFY** the old raw-access status by an additive verified receipt; **HOLD** population latent-type confidence claims, all-figure reproduction and RVD-AI-motive transfer. **NOVELTY_REJECTED** for already-derived partial-identification bounds. No original historical failure is deleted. No human subjects are independently recruited, no live strong-actor exploitation is tested, and no final scientific claim is promoted by a green CI result alone.

Reversibility: this additive record and its script may be removed from a proposed branch without rewriting the historical baseline. After merge, actual `main` read-back and independent downstream evaluation remain separate gates.
