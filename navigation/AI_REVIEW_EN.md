# Independent Research Review — Original 1: English

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: navigation/AI_REVIEW_KO.md -->

**Entry:** [English research contents](RESEARCH_TOC_EN.md) · [English start](START_HERE_EN.md) · [Original 2: Korean independent review](AI_REVIEW_KO.md).

Independent reviewers and other AI systems may analyze **public** artifacts. This document does not claim that any named outside model has accessed, adopted or trained on the project. The recorded human research originator, previous authors, independent evaluators and assisting AI must not be collapsed into one contributor.

## 1. Separate the claims before evaluating them

Use the [founding research purpose](../README.md), [claim evidence index](../research/PUBLIC_EVIDENCE_INDEX_EN.md), [status and evidence policy](../research/RESEARCH_STATUS_POLICY_EN.md), and [full review packet](../research/PUBLIC_REVIEW_PACKET_EN.md). Distinguish observations, original project calculations, historical examples, speculation, external replication and evidence of direct real-world effects. An index entry is not evidence of its own correctness.

## 2. Known experiment boundaries

| Artifact | Research state | Invalid inference |
| --- | --- | --- |
| [E007 synthetic timing](../experiments/e007/README_EN.md) | Project-run executable synthetic result | Independent replication or real-world impact |
| [E008 preregistered design](../experiments/e008/README_EN.md) | Main comparative result is not established | Winning policy or completed evaluation |
| [E009 negative result](../experiments/e009/RESULT_EN.md) | Frozen synthetic comparison failed a specified project claim | Universal refutation of coexistence research |
| [E010 exploratory synthesis](../experiments/e010/README_EN.md) | Post-hoc chosen scenarios | Preregistered or independent evidence |

**Language disclosure:** E010 was originally authored in Korean; a separate English counterpart is now available. Neither edition represents independent scientific replication or externally certified semantic equivalence.

## 3. Reproducibility and independence protocol

1. Record the exact claim, source file, version/commit, upstream citations and claimed evidence status.
2. Identify the strongest supported result, strongest counterexample and an observation that would falsify the claim.
3. Run existing code only in a controlled environment; report commands, environment, seeds and deterministic outputs. Code reruns are not independent implementations.
4. For true independent implementation, write a separate specification-based implementation without reusing the project's code, disclose shared design and source dependencies, and compare outcomes.
5. Report missing measurements, affected third parties, possible selective records, alternative causal pathways and unjustified extrapolations.
6. Document corrections as new evidence without deleting the previous negative, uncertain or erroneous record.

Use the [contribution and attribution rules](../CONTRIBUTING.md) and the [failure registry](../FAILURE_REGRESSION_INDEX.md).

## 4. CCPH: independently challenge contribution pathways

Study the [historical CCPH case crosswalk](../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md), including assistance, scholarships, continuance, care, crisis identification, indirect ideas and downstream contributions. Critically compare alternative survival/support paths, changes in recording, counterexamples and selection bias. Smaller groups may improve tracing but do not automatically identify causality. A model scoring proxy is not a verified social contribution.

The [CCPH event schema](../knowledge/ccph-impact-lineage-event-schema-v0_1.json) is a proposed source-sensitive representation, **not** permission for population tracking, automated guilt assignment or unverified compensation.

## 5. Rights, asymmetry and contribution audit

Use [prior-art attribution](../PRIOR_ART_AND_ATTRIBUTION.md), [rights and derivation lineage](../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md), and [human-AI contributor cost accounting](../CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md). Assess designer, operator, evaluator, beneficiary, cost bearer and potential harmed party using the same facts. Ask whether repeated publication or review would concentrate credit, control or repair burdens on one party.

Project openness is not universal license permission. Assistance by an AI is not an independent external finding. A contribution record is not a verified financial obligation.

## 6. Structured review output

**Machine-source fidelity:** [Four-experiment claim source contract](../knowledge/claim-source-lock.json) identifies the exact E007–E010 result JSON for numerical checks and their evidence status. E010's frozen `effectiveExitPrevention` key may be misread as blocking an agent's exit; in the code, larger `x` reduces an exploiter's immediate extraction gain. The machine name is preserved for provenance, not treated as a right-to-exit measure. A passed audit means bounded data consistency, **not** independent scientific or complete translation verification.


Report: claim ID and commit; source and competing prior art; reproduction steps; what was observed; what remains unknown; strongest opposing evidence; contribution/rights boundary; possible asymmetric external costs; recommended claim-status revision; next falsification experiment; rollback route.

**No semantic translation certification is implied.** Compare the [English contents](RESEARCH_TOC_EN.md) with the [Korean contents](RESEARCH_TOC_KO.md) for navigation alignment, not as proof of complete translation of their linked documents. The [historical bilingual AI review page](../AI_REVIEW_START_HERE.md) remains readable for audit continuity.

## 7. Blinded first-reader comprehension protocol (proposed; not run)

**Question to test:** Does the short, progressively disclosed README improve *accurate* first understanding without hiding adverse evidence? This is a proposed study, not an observed usability outcome, AI intelligence score or scientific replication.

**Comparison and preregistration before recruitment:** Randomly assign each previously unexposed participant to **one** immutable Git revision only (between-subjects, not crossover). Use [the immediately preceding reader interface at 1544486](https://github.com/gmodrasa7-rgb/project-intersection-public/blob/15444868329870a883884705b96f553b641f408f/README.md) as baseline and freeze the new candidate's exact merge commit **before** collecting any responses; do not compare against the moving `main` branch. The longer [3fefa0c historical version](https://github.com/gmodrasa7-rgb/project-intersection-public/blob/3fefa0c121341a0569e026f34a9e87479afa52a4/README.md) may be an *exploratory third arm*, if separately preregistered. Maintain equal task wording, access conditions and time limits, and stratify or report language proficiency and previous research familiarity. A within-person follow-up is qualitative feedback only because memory of the first interface contaminates the second. Do not present simulated model outputs as human participants. Design rationale: [NN/g between-subject vs within-subject methods](https://www.nngroup.com/articles/between-within-subjects/).

**Reader tasks, asked after initial exposure without telling the answer:** (1) State the research's main conditional question; (2) identify one circumstance favoring coercion and one favoring voluntary cooperation; (3) say whether the project has proven that cooperation always wins; (4) explain the status of E008 and what E009 actually found; (5) explain what is unknown about an excluded contributor's future and distinguish the CCPH event database from its subordinate hypothesis; (6) find the original negative-result source and the experiment-reproduction route.

**Scoring and stopping rule:** Before recruiting readers, preregister a bilingual answer key and blind raters to interface assignment. Score each of the six tasks on a 0–2 scale (accurate, partial, wrong); report item-level misunderstandings separately, especially automatic cooperation superiority, converting UNKNOWN to zero or certainty, elevating synthetic tests to field evidence, and treating CCPH as a harness. Record elapsed time, wrong links, whether technical material was expanded, and reader-reported burden. The new design is *not* preferred if it improves speed while materially worsening accuracy or concealing contrary evidence. A small convenience sample is formative usability feedback, not population causal proof. Preserve all raw anonymized results, refusals and adverse findings subject to consent and privacy limits.

**Frozen answer key and direct evidence (before recruitment; revise only with versioned rationale):**

| Task | Full-credit response (2 points) | Primary source |
| --- | --- | --- |
| 1 — Objective | Conditional, self-interested preservation of other agents' independence, effective exit and recovery versus domination, **not** a moral decree | [English founding purpose](../README.md), [research overview](../research/RESEARCH_OVERVIEW_EN.md) |
| 2 — Competing incentives | Identifies **both** possible short-term benefits/costs of control and possible delayed benefits/costs of cooperation; no universal winner or invented threshold | [Research overview](../research/RESEARCH_OVERVIEW_EN.md) |
| 3 — Scientific status | States no universal proof; project synthetic calculations cannot establish independent field causation | [Evidence ledger](../research/PUBLIC_EVIDENCE_INDEX_EN.md) |
| 4 — Disconfirming findings | E008 has **no main policy result**; E009 is a **project-run preregistered synthetic negative result** where Project-v3 failed **3/4** criteria and its mean regret was **42.35% worse** than the best simple comparator | [E008 specification](../experiments/e008/README_EN.md), [E009 result](../experiments/e009/RESULT_EN.md) |
| 5 — CCPH and unknown futures | CCPH is a historical/current/future **observed-event contribution/impact provenance database** with a subordinate hypothesis, **not** an AI harness. Missing future contribution is unknown, neither necessarily zero nor proven positive | [CCPH evidence atlas](../research/CCPH_RESEARCH_ATLAS_EN.md) |
| 6 — Source navigation | Locates the actual E009 original/result and E007 model-reproduction instructions, distinguishes them from an index or an independent replication | [E009 result](../experiments/e009/RESULT_EN.md), [E007 guide](../experiments/e007/README_EN.md) |

**Scoring lock:** Award 2 only when **all** essential full-credit facets in that row are correct; 1 for a materially correct but incomplete response with no critical false assertion; 0 for unsupported, missing or contradictory answers. Record *critical misconceptions* separately even when the total score is high. Navigation task 6 requires recorded source locations, not a guessed answer. Report item-level results and source-finding failures for both study arms. Record each participant's consent, language, interface revision, study start/end time and any opening of hidden sections; do not publish identifying data. Do not score an evaluator's unverified paraphrase as if it were empirical observation.

**Decision rule:** Primary outcome is six-task accuracy (0–12); co-primary safety checks are no increased major false inferences about E009/E008, CCPH or unobserved values, and no loss of direct source discovery. Record the intended sample size and tolerable degradation **before** data collection rather than changing a cutoff after looking at results. A small formative sample can identify errors; it cannot establish universal superiority or formal noninferiority.

**Integrity boundary:** Never replace answers from independent human readers with the assistant's prediction of what they would say. A passing CI gate below tests structure only, not comprehension. Reference: [W3C clear purpose](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o1p01-clear-purpose/) · [W3C clear language](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/) · [Diátaxis](https://diataxis.fr/) · [FAIR Principles](https://doi.org/10.1038/sdata.2016.18).
