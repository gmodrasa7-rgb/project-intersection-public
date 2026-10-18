<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/ECR_MIND_OPEN_DATA_ROUTES_2026-10-18_KO.md -->
# ECR–MIND: concrete open empirical datasets and decision gates
**Original 1 English · 2026-10-18 · OPEN-DATA CANDIDATE REGISTER — NOT DOWNLOADED OR REANALYZED.**
**Companion:** [Original 2 Korean](ECR_MIND_OPEN_DATA_ROUTES_2026-10-18_KO.md); [mind research paper](ECR_MIND_FOUNDATIONS_2026-10-18_EN.md).

## Aim
Prevent another cycle in which real psychological causes are merely assigned convenient utilities inside synthetic games. Identify *published, externally collected* data suitable for **scoped, reproducible tests of observable social decisions**, while explicitly refusing unjustified claims about real private subjective emotion or innate motives. The records below were located via publicly described OpenNeuro releases; task descriptions and sample sizes originate with dataset maintainers, **not original ECR measurements**.

## Candidate D1 — social decision-making across age, partner identity
- OpenNeuro accession: **ds003745**; publisher-provided GitHub mirror: https://github.com/OpenNeuroDatasets/ds003745 .
- Published description: N=50, younger N=26 (18–34 years), older N=24 (63–80 years). Behavioral and fMRI tasks: trust investment with friend, stranger, or computer; monetary-sharing card guessing; ultimatum-game responder with social-context partners.
- Immediate plausible **observable outcome:** within-task trust investment, acceptance/rejection, and response changes across partner types.
- Competing mechanisms: social familiarity, trust, perceived reciprocity, task incentives, age/cohort, task comprehension, learning.
- False inference: partner difference is NOT independently measured compassion, genetic greed, life-course cause, or personal moral value.
- First gate: verify BIDS task events/behavioral coding, partner condition balance, participant consent/license, shared-session dependence, missing data and exact version; test within-subject contrast with clustering where justified.

## Candidate D2 — representations of others and resource allocation
- OpenNeuro **ds004128**: https://github.com/OpenNeuroDatasets/ds004128 .
- Source description: N=32; modified dictator-game choices involving 20 recipients of varying group membership across two MRI runs. Authors cite *Neural representations of others' traits predict social decisions* (PNAS, DOI https://doi.org/10.1073/pnas.2116944119). Associated behavior: https://osf.io/qkrhm/ .
- Observable outcome: allocation choices across recipients, conditional on actual trial design and randomized factors.
- Rival explanations: in-group effects, learning, social reputation, perceived deservingness and response biases; all must be matched to actual variables before analysis.
- False inference: recipients' group labels do not prove a stable innate trait, and brain patterns do not prove conscious other-regard.
- Gate: verify task specifications, actual availability of behavioral file, anonymity, license, MRI confounds, repeated decisions and preexisting model code; do not claim independent neural replication by rerunning its authors' pipeline.

## Candidate D3 — social and nonsocial rewards through adulthood
- OpenNeuro **ds005123**: https://github.com/OpenNeuroDatasets/ds005123 .
- Maintainer description: interim multi-echo fMRI and DWI with N=114 adults ages 21–80; monetary/social reward tasks, ultimatum and dictator conditions, trust tasks, shared reward involving friend/stranger/computer. A linked ongoing study examines social reward and vulnerability to financial exploitation.
- Observable question: do reward and social-context measurements produce reproducible partner- or task-conditional behavior?
- False inference: older age or susceptibility to exploitation cannot be used for individual risk scoring or character diagnosis. Dataset is preliminary and some DWI/runs are missing as documented by maintainers.
- Gate: eligibility, version, license, design matrix, preregistration and handling of longitudinal/age-related confounds. Do not use individual-level personal harm ranking.

## Source-selection comparison and research order
| Dataset | Baseline question | Distinguishing added information | Core risk |
|---|---|---|---|
| D1 ds003745 | Does partner category correlate with choices? | repeated behavioral/brain measures and age cohorts | confound age and familiarity with compassion |
| D2 ds004128 | Do recipient differences predict resource sharing? | many within-participant recipients and published neural dataset | scoring actual individuals' latent morality |
| D3 ds005123 | Does social vs monetary reward alter choice? | several tasks within an adult cohort | incomplete runs and premature exploitability inference |

**Recommended first step:** D2 **metadata-only feasibility** because explicit target/decision repeated-measures design is directly relevant to ECR target-scope. Then D1 partner familiarity as a replication *question*, not the same task or transferable construct. D3 secondary wider multimodal check with increased harmonization complexity.

## Frozen analysis gates (not yet executed)
1. Download and independently hash selected public behavioral data *only after* license/privacy verification; freeze dataset version and participant exclusion rules. No participant names, private clinical records or sensitive genetic data.
2. Define primary event (share/not share or real monetary allocation), target identity strata and treatment/exposure balance. Preserve denominators and abstention; do not invent data.
3. Fit an elementary opportunity-/recipient-aware baseline M0, then richer M1 with predeclared social factors, under grouped participant holdout rather than row leakage.
4. Report proper loss, calibration or held-out mean absolute error according to the outcome, uncertainty intervals and missed third-party costs. Do not label people psychopathic, greedy or compassionate from these tasks.
5. Only if genuine improvement replicates under a second context consider hypotheses about latent mechanisms. Those require additional converging measures/causal contrasts, not merely fit. Publish failed or null results.
6. A task study with restricted power/roles cannot demonstrate B→A superintelligence transitions or humanity's long-term coexistence.

**Current receipt:** published metadata and links reviewed only. **DATA_RETRIEVED = FALSE; REANALYSIS = NOT RUN; EMPIRICAL_EFFECT = NOT CLAIMED.** This dataset scout is not a substitute for the fundamental biological and developmental research in the paired ECR–MIND paper.