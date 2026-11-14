# Independent Validation Infrastructure for E008–E009 and IVS-0R

**Original 1 — English | 2026-11-15 | DESIGN ONLY / NOT EXECUTED**

## 0. Decision and evidence boundary

This specification adds lineage-separated validation. It does not amend or overwrite frozen experiments, preregistrations, negative results, source attribution, or historical records.

Known boundaries:
- **E008:** its 16-case preregistered matrix is categorical. The readiness audit found 16/16 cases underdetermined for policy-performance execution; two invented numeric completions produced opposite aggregate-action choices. This is a feasibility finding, not an E008 result.
- **E009:** the frozen project-designed synthetic benchmark reports PROJECT_V3 mean regret 0.090022 versus TWO_RULE_SIMPLE 0.063241; V3 was 42.35% worse on regret and failed 3/4 preregistered survival criteria. Preserve the opposing competitive-loss metric and every other component. This is not field evidence.
- **Issue #19:** requests an external E007 rerun or clean-room reimplementation. Same-spec implementation does not establish independent assumptions, DGM, or evaluation.
- Existing E009 external decision-gate documents and issue #26 remain the reviewer entry points.

No experiment is created by this document. Status remains DESIGN until a provenance-complete execution is deposited.

## 1. Scope and non-goals

**Goal:** test whether comparisons survive independent assumptions, alternative operationalizations, implementation-lineage separation, measurement scrutiny, and uncertainty analysis.

**Non-goals:** prove the whole Project Intersection thesis; infer intrinsic motives or consciousness; convert synthetic results into real-world risk estimates; infer novelty from paper counts; require unpaid founder work; or select favorable weights after observing outputs.

The unit of validation is a bounded claim under a named scenario family, not the whole research program.

## 2. Five required workstreams

### V1 — Independent DGM and outcome function for E009

**Problem:** the original policy rules, scenarios, consequence engine, and weights share project lineage. An external implementation of the same engine reproduces that lineage; it does not independently test the evaluation assumptions.

**Protocol**
1. Publish the minimum policy interface: action vocabulary, observable input fields, policy rules, information constraints, and resource/compute limits. Do not expose outcome labels or preferred rankings in the reviewer packet.
2. An evaluator outside policy authorship freezes a separate data-generating mechanism (DGM), scenario-generation rules, outcome function, severity thresholds, missingness rules, and analysis plan **before seeing policy outputs**.
3. Keep policy authors blind to holdout cases and evaluator weights until the plan is timestamped. If blinding is infeasible, disclose exposure and downgrade independence.
4. Include matched cases, role reversals, negative controls, no-harm/no-opportunity controls, and cases where every policy fails. Include affected and third parties; distinguish attempted harm, prevented harm, realized harm, blocked exit, voluntary non-action, and lack of opportunity.
5. Apply identical cases, information, action sets, meaningful random streams, and resource budgets to all policies. Otherwise label NOT_COMPARABLE.
6. Publish the DGM, version/hash, frozen analysis plan, all cases or a reproducible generator, raw outputs, exclusions, missingness, and every metric component.

**Estimands:** paired policy differences in regret and separately defined harm, recovery, effective-exit, third-party-loss, and operational-cost outcomes. Do not collapse these into one score unless the utility function and normative trade-offs were independently justified and preregistered.

**Stop:** absent an independent DGM and outcome function, report HOLD / EXTERNAL_DGM_NOT_OBTAINED. A project-authored alternative DGM is sensitivity analysis, not independent evaluation.

### V2 — E008 operationalization ensemble under deep uncertainty

**Problem:** E008's categorical specification does not identify unique numeric transitions, utilities, or baseline actions. A single hand-authored completion can determine the result.

**Protocol**
1. Keep the original 16 cases and preregistration immutable; create a separately versioned operationalization registry.
2. Enumerate uncertain assumptions before outcomes: transition rules, utility scales, irreversibility, exit effectiveness, recovery, information, intervention costs, role reversal, and third-party effects.
3. Define admissible ranges/distributions with provenance. Distinguish evidence-based, expert-elicited, and adversarial stress ranges. An arbitrary distribution is not an empirical prior.
4. Draw N paired operationalizations from the frozen registry. Apply every policy to the same completion, scenario, and seeds. Publish sampler, seed, exclusions, and convergence diagnostics. Start with a pilot and increase N until Monte Carlo precision is adequate for the stated decision; no fixed N is universal.
5. Report: (a) fraction of admissible completions where Project-v2 regret is lower than D; (b) paired regret-difference distribution, median, quantiles, and tails; (c) worst/best regret over the declared set; (d) protected-floor, severe-harm, exit, recovery, and third-party constraint violations; (e) assumption combinations and boundaries where ranking changes; (f) non-identifiable or non-comparable share.
6. Report Monte Carlo standard errors (MCSE). For a simple independent Bernoulli win proportion, MCSE = sqrt(p(1-p)/N). For clustered, weighted, or dependent sampling, use and explain a design-appropriate estimator; report effective sample size where applicable.
7. A win fraction is conditional on the declared completion set and sampling distribution; it is not the probability of objective superiority. Report distribution-free ranges where possible.

Decision labels: ROBUST_WITHIN_DECLARED_SET, FRAGILE_TO_OPERATIONALIZATION, MIXED, NOT_IDENTIFIED, NOT_COMPARABLE. Never overwrite E008 NO_RESULT.

### V3 — Clean-room implementation and correlated-failure audit

**Problem:** implementations can agree because they share an ambiguous specification, examples, training data, libraries, or design assumptions. Agreement alone is not independent confirmation.

**Required return:** implementer identity/affiliation or privacy-preserving stable ID; date; tools/model/version/libraries; code provenance; exact specification commit/hash; all clarifications; whether project code/generated code/tests/examples/expected outputs were viewed or reused; independent interpretation log; executable tests; raw outputs and diff; failure taxonomy; environment, command, seed, and reproduction instructions.

**Failure taxonomy:** specification ambiguity; interpretation divergence; implementation defect; shared upstream dependency; numerical instability; nondeterminism; test-oracle defect; missing behavior; environment failure.

Report per-test agreement/disagreement and paired failure indicators. Estimate pairwise failure association only if the number and structure of independent implementations support it. With only two implementations, report descriptive overlap/disagreement counts; do not claim a stable correlation estimate. Separate same-spec implementation agreement, independent specification interpretation, independent DGM/evaluator, and independent data/field replication.

A clean-room result may establish implementation reproducibility within a specification. It does not establish construct, causal, external, or scientific independence by itself.

### V4 — ADEMP, measurement validity, and uncertainty reporting

Every simulation report must include:

| Element | Mandatory disclosure |
|---|---|
| Aims | Exact decision/method question and bounded claim |
| Data-generating mechanisms | DGM versions, assumptions, scenario population, parameter ranges, dependence, missingness |
| Estimands | Mathematical definition, unit, direction, aggregation, target population |
| Methods | Policies/baselines, versions, information and compute budgets, tuning exposure |
| Performance measures | Formula, denominator, thresholds, uncertainty estimator, interpretation limits |

For each construct (e.g. severe harm, exit retention, recovery, coercive dependence), map: conceptual definition → observable indicator → measurement procedure → validity evidence → known failure modes → unobserved dimensions. A proxy is not the construct itself.

Report unique scenario count, policy-decision count, replication count, seed count, and metric-row count separately; MC error and uncertainty intervals, not point estimates alone; paired comparisons; sensitivity to thresholds, weights, missingness, and alternative measures; all exclusions, failed runs, non-convergence, adverse outcomes; and reproducibility limits.

### V5 — Prior-art delta audit and cumulative benchmark register

These 2026 works are **candidate overlaps**, not proof that the repository has or has not cited them. Verify citation status and full-text scope against the repository and publisher/preprint versions.

| Work | Abstract-level contribution | Delta question | Boundary |
|---|---|---|---|
| Chakraborty, A Co-Evolutionary Theory of Human-AI Coexistence (arXiv:2604.22227, 2026) | Conditional mutualism under governance; multiplex physical/psychological/social dynamics; reciprocal coupling, conflict penalties, developmental freedom; deterministic ODE simulations and stability/sensitivity analyses. | Does executable practical exit, individual recovery, and power-reversal behavior add a measurable construct beyond reversibility, governance, and developmental freedom? | Abstract-level only; deterministic simulation is not empirical validation. Full-text variable mapping required. |
| Codreanu, Cooperation After the Algorithm (arXiv:2602.19629, 2026) | Institutional cooperation ecology; residual-risk allocation, accountability, reciprocity contracts, trust infrastructure, conditional cooperation, defection mitigation, readiness artefacts. | Which Project variables are genuinely distinct from accountability, repair, institutional incentives, and risk allocation? | Abstract-level only; no novelty claim before full-text/reference review. |
| Gardner-Challis et al., When can we trust untrusted monitoring? (arXiv:2602.20628, 2026; version dated 2026-09-21) | Safety-case analysis of untrusted-monitor collusion: passive self-recognition, causal/acausal signaling, and combined strategies. | Does E009's monitor-collusion case family cover these strategies? Which adversarial tests or monitor-independence assumptions are absent? | Taxonomy is not evidence that E009 covers or defeats the attacks. Map exact cases and controls. |

For each source record: canonical citation/version/date; full text inspected yes/no; exact section/page; shared and non-shared constructs; reused method; contradictory/null evidence; limitations; affected repository files; novelty status (OVERLAP, PARTIAL_RESIDUAL, NO_DELTA_FOUND, UNRESOLVED); next falsifier. Do not infer absence from an abstract or failed fetch.

## 3. Independence ladder

| Level | Label | Meaning |
|---|---|---|
| 0 | PROJECT_INTERNAL | Same authorship/evaluation lineage |
| 1 | EXTERNAL_CODE_RERUN | Outside operator reruns project code |
| 2 | CLEAN_ROOM_IMPLEMENTATION | New implementation from public specification |
| 3 | INDEPENDENT_SPECIFICATION | Outside evaluator defines assumptions, DGM, and outcomes before outputs |
| 4 | INDEPENDENT_DATA_OR_FIELD_STUDY | New external data or field observation with disclosed design |
| 5 | INDEPENDENT_MULTISITE_REPLICATION | Independent teams/sites use a prespecified harmonized protocol |

Higher levels do not automatically guarantee validity. Separately record independence of people, code, specification, DGM, evaluator, data, analysis, funding/conflicts, and publication control.

## 4. Evidence state and promotion gates

Permitted labels: DESIGN, PROJECT_INTERNAL, PROJECT_RERUN, EXTERNAL_CODE_RERUN, CLEAN_ROOM_IMPLEMENTATION, INDEPENDENT_DGM_EVALUATION, EMPIRICAL_OBSERVATION, INDEPENDENT_REPLICATION, NOT_IDENTIFIED, FAILED_TO_REPRODUCE.

Promotion requires provenance and scope-specific evidence. CI success, same-model agreement, citation, or a favorable metric cannot promote a claim. Retain prior state and dated reasons. Negative, null, mixed, missing, and failed outcomes are first-class records.

## 5. Minimum machine-readable receipt

Each run should emit a versioned JSON receipt with protocol_id/version, run_id, UTC timestamp, repository commit, specification/code/DGM/analysis-plan hashes, independence level and dimension-level lineage, environment/dependencies/seed, scenario/unique-decision/replication counts, estimands/metrics/MCSE/intervals, missingness/exclusions, raw-output and diff locations, limitations, status, and reviewer attestation.

A schema or receipt is not evidence that a run occurred. Empty fields remain unknown.

## 6. Governance and stop conditions

- No direct main edits, automatic merge, result rewriting, or retroactive preregistration.
- No external publication, reviewer contact, paid service, or private-data disclosure without explicit authorization.
- Do not transfer independent-validation costs to the founder. Founder-required work defaults to zero; reviewer effort and compute costs must still be disclosed.
- If no independent evaluator is available, preserve HOLD. Do not manufacture independence by asking another model to agree.
- Stop if the test cannot distinguish the claim from a live rival, comparison budgets materially differ, or the outcome function was selected after results.

## 7. References

1. Morris, White & Crowther (2019), “Using simulation studies to evaluate statistical methods,” Statistics in Medicine 38(11), 2074–2102. ADEMP and simulation reporting. https://arxiv.org/abs/1712.03198
2. Bartoš, Pawel & Siepe (2025), “Living Synthetic Benchmarks: A Neutral and Cumulative Framework for Simulation Studies.” Separate method and DGM development; cumulative benchmark. https://arxiv.org/abs/2510.19489
3. Bean et al. (2025), “Measuring what Matters: Construct Validity in Large Language Model Benchmarks,” NeurIPS 2025 Datasets and Benchmarks. https://arxiv.org/abs/2511.04703
4. Pawel, Kook & Reeve (2023), “Pitfalls and potentials in simulation studies: Questionable research practices in comparative simulation studies allow for spurious claims of superiority of any method,” Biometrical Journal. https://arxiv.org/abs/2203.13076 https://arxiv.org/abs/2203.13076
5. Knight & Leveson (1986), “An Experimental Evaluation of the Assumption of Independence in Multiversion Programming.” DOI: 10.1109/TSE.1986.6312924
6. Chakraborty (2026), arXiv:2604.22227. 7. Codreanu (2026), arXiv:2602.19629. 8. Gardner-Challis et al. (2026), arXiv:2602.20628.

Cross-domain transfer is methodological analogy, not proof of validity for human-AI coexistence research. Verify exact versions, methods, and quantitative claims before citing detailed results.

## 8. Acceptance checklist

- [ ] Original E008/E009 artifacts and negative results remain byte-for-byte unchanged.
- [ ] E009 independent DGM is authored/frozen outside policy authorship.
- [ ] E008 operationalization set, distributions, and sampling plan are frozen before policy outputs.
- [ ] Clean-room return includes interpretation log, lineage, raw diff, and shared-failure analysis.
- [ ] ADEMP and construct-to-measure maps are complete.
- [ ] Three 2026 candidate sources are checked against full text and repository citations.
- [ ] Conclusions state independence level, uncertainty, scope, and unresolved rivals.
- [ ] No unrun experiment or independent validation is represented as complete.

**Current status: DESIGN ONLY. No new experiment, external review, independent DGM, or replication has been executed by this specification.**
