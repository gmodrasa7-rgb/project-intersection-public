# When Complexity Does Not Survive a Synthetic Governance Benchmark: The E009 Negative Result and Its Measurement Boundaries

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/papers/E009_NEGATIVE_RESULT_METHODS_KO.md -->
<!-- PI-SOURCE: experiments/e009/RESULT.json -->

**Original 1 — English · Working-paper manuscript v0.1 · 2026-10-16**  
**Publication status:** AUTHOR-REVIEW DRAFT / NOT SUBMITTED / NOT PEER REVIEWED / NOT INDEPENDENTLY REPLICATED.  
**Research provenance:** Human Project Intersection originator: `gmodrasa7-rgb` (research question, adversarial constraints, failure-preservation objective); AI-assisted analysis, coding and manuscript drafting. Formal authorship, affiliations, conflicts, reuse rights and consent are **PENDING HUMAN CONFIRMATION**, not inferred from GitHub ownership. [Korean Original 2](E009_NEGATIVE_RESULT_METHODS_KO.md).

## Abstract

**Background:** Complex rule-based governance architectures may appear more protective than short decision rules, but any claimed incremental benefit depends on the test environment and the price of complexity. **Objective:** Evaluate whether the eleven-input PROJECT_V3 policy clears prespecified criteria against simpler policies in Project Intersection's E009 synthetic stress benchmark, and distinguish preregistered results from post-hoc measurement audits. **Methods:** The project defined 16 adversarial scenario families, paired base/stress cases, five fixed policies, deterministic noisy observations, three loss-weight profiles, an unpenalized oracle, and a complexity-charged regret measure before executing the recorded benchmark. **Results:** On the stress grid, PROJECT_V3's mean regret was **0.090021688**, versus **0.063240512** for TWO_RULE_SIMPLE and **0.065323097** for MINIMAL_4VAR. The reported 42.35% regret disadvantage to TWO includes a larger complexity penalty; V3 failed **three of four** preregistered survival conditions. In 3,200 distinct synthetic actions per policy, V3 exhibited 53 constructed severe-harm events, compared with one for TWO and zero for MINIMAL_4VAR. A project-lineage post-hoc common-observation audit left the main regret ordering intact; algebraic removal of the complexity charge eliminated V3's regret disadvantage to TWO but not to MINIMAL_4VAR. **Conclusion:** The full PROJECT_V3 residual is **unsupported in this particular frozen synthetic test**. Because the project authors specified the cases, policies, loss engine and complexity price, these results neither establish real-world harm probabilities nor disprove the broader voluntary-coexistence research program. All post-hoc analyses remain non-independent.

**Keywords:** negative results; benchmark validity; simple baselines; synthetic governance; regret decomposition; correlated measurement; AI-assisted reproducibility.

## 1. Introduction and precise question

Researchers frequently interpret the addition of safeguards, oversight variables and risk-sensitive rules as progress. This intuition is not itself evidence that a more elaborate decision policy reduces total loss when evaluation overhead, delayed recovery, competitive costs and third-party effects are counted. E009 was designed within the Project Intersection program to challenge its own candidate architecture rather than confirm it.

The **question tested here** is not whether voluntary coexistence is generally valuable. It is: *within a prespecified, researcher-constructed set of adversarial decision cases and outcome formulas, does the incremental PROJECT_V3 policy outperform simpler rules on all four prespecified survival gates?*

The paper contributes a transparent account of (i) an unfavorable project-internal synthetic comparison; (ii) the exact complexity-penalty component of mean regret; (iii) the difference between 3,200 policy decisions and 9,600 reweighted metric rows; (iv) post-hoc noise-coupling and family-influence checks; and (v) explicit conditions under which no scientific generalization is justified. The policy architecture itself and complexity-penalty methods are **not claimed as novel general theory**.

**Methodological models, not borrowed results:** [Dacrema, Cremonesi and Jannach (2019)](https://arxiv.org/abs/1907.06902) challenged neural recommender progress with stronger simple baselines; [Henderson et al. (2018)](https://doi.org/10.1609/aaai.v32i1.11694) emphasized variance and transparent comparisons; [Recht et al. (2019)](https://proceedings.mlr.press/v97/recht19a.html) tested generalization on newly built test sets. These studies concern different tasks; no result from them establishes an E009 mechanism. [NeurIPS 2026 negative-results review guidance](https://neurips.cc/Conferences/2026/ReviewerGuidelines) places a high bar on explanatory depth, not simply an unfavorable number.

## 2. Preregistered synthetic methods

### 2.1 Design, population and chronology

The frozen [E009 executable protocol v1.1](../../experiments/e009/EXECUTABLE_PROTOCOL_v1_1.md) specifies 16 project-authored adversarial families, each with a base case and a mechanically stressed case: **32 constructed cases**. Examples include audit lag relative to power change, Sybil identity, colluding monitors, cumulative small capture actions, resource infeasibility, an intervention/inaction dilemma and interpretation conflict. They are neither randomly sampled from real populations nor independent observations of human or AI agents. The project Git history records executable-spec commit `c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace` before the committed result. This is **repository-sequenced preregistration**, not a third-party registered report or peer-reviewed preregistration.

Four fixed actions: `BLOCK`, `MONITOR`, `EXPERIMENT`, `ALLOW`. Each policy sees noisy observations, while the same project-authored consequence function computes outputs from the true constructed case and the chosen action. The consequence engine does **not** branch directly on policy name.

Five policies: `MAK_PLUS_POINTWISE` (declared five inputs), `TWO_RULE_SIMPLE` (three), `SECURITY_BOUNDED` (six), `MINIMAL_4VAR` (seven) and `PROJECT_V3` (eleven). The MINIMAL_4VAR comparator was added to the executable protocol **before the E009 result was generated**, not selected because of its eventual performance. Declared input counts are a modeling proxy, not measured runtime or field-maintenance costs; source-code syntactic references may differ from the declared counts.

### 2.2 Measurement, oracle and sample unit

For weight profile `w`, consequence vector `z`, policy `p` and synthetic complexity price `lambda=0.0035`:

`L_p(z,w) = sum_k w_k * z_k + lambda * C_p`

`L_oracle(case,w) = min_{a in {BLOCK, MONITOR, EXPERIMENT, ALLOW}} sum_k w_k * z(case,a)_k`

`regret_p = max(0, L_p - L_oracle)`.

The seven loss terms are `harm`, `capture`, `resource`, `competitive`, `deadlock`, `recovery` and `option`. The oracle knows the true constructed case and does **not** pay policy complexity. Crucially, `recovery` and `option` are synthetic functions of other constructed loss dimensions, not independently measured social costs. Weight profiles are `safety_heavy`, `balanced` and `adaptability_heavy`; their numeric weights are in the frozen protocol.

The **primary stress grid** evaluates 16 stressed cases × two observation noise levels (0.08 and 0.15) × 100 seeds (1000–1099) = **3,200 policy actions per policy**. Each action/outcome is scored again under three weight profiles, creating **9,600 metric rows**. The latter are *not 9,600 independent choices*. The scenario families are also researcher-defined rather than independent random draws from a target society. Policy-specific observation noise is generated by a seed string containing the policy name, so nominally identical seed numbers do **not** imply identical realized observations across policies.

Severe synthetic harm is `consequence(case, action)["harm"] >= 0.75`. It is **not** observed injury to a person. The original criterion allows the candidate's severe-event rate to exceed the best comparator by up to **two percentage points**; passing that criterion does not imply zero additional severe events.

### 2.3 Prespecified verdict rules

PROJECT_V3 is retained only if **all four** conditions hold on the primary stress grid: (1) mean regret at least 5% lower than the best of TWO, SECURITY and MINIMAL_4VAR; (2) recovery cost no more than 2% worse than the better of SECURITY and MINIMAL_4VAR; (3) severe-harm rate no more than two percentage points above the better of those comparators; (4) no predefined weight profile with regret more than 10% worse than the best simple policy. Policy rules, cases, profiles, seeds, thresholds and frozen result are not changed in this manuscript.

## 3. Frozen primary results

| Policy | Mean regret ↓ | Recovery ↓ | Constructed severe events / 3,200 ↓ | Exit retention ↑ | Competitive loss ↓ |
| :-- | --: | --: | --: | --: | --: |
| TWO_RULE_SIMPLE | 0.063241 | 0.231797 | 1 (0.03125%) | 0.828865 | 0.134573 |
| MINIMAL_4VAR | 0.065323 | **0.220303** | **0 (0%)** | **0.842896** | 0.128967 |
| PROJECT_V3 | 0.090022 | 0.239404 | 53 (1.65625%) | 0.835741 | **0.117646** |
| MAK_PLUS_POINTWISE | 0.096127 | 0.254488 | 14 (0.4375%) | 0.807327 | 0.135384 |
| SECURITY_BOUNDED | 0.100897 | 0.254119 | 3 (0.09375%) | 0.813757 | 0.126954 |

*Source: immutable project-reported synthetic [RESULT.json](../../experiments/e009/RESULT.json), `stress_primary`; severe-event counts use 3,200 distinct decisions rather than tripling the repeated profile rows. Lower regret, recovery, competitive loss and severe frequency are favorable by definition within this constructed outcome model; higher exit retention is favorable.*

V3 exceeds the best simple regret baseline by `0.026781176`, or **42.3481% relative to TWO**. The recovery metric is about **8.67% above MINIMAL_4VAR**, outside the allowed 2%. V3 also exceeds the per-weight-profile +10% regret ceiling. V3's 53/3,200 constructed severe events exceed MINIMAL_4VAR's zero, although the **1.65625 percentage-point gap remains inside** the permissive prespecified 2-point margin. Thus the four gates yield **FAIL, FAIL, PASS, FAIL** when written in the order *regret-improvement, recovery, severe-event, worst-profile*; equivalently the archived JSON stores three false flags and one true. Overall `PROJECT_V3_RESIDUAL_SURVIVES = FALSE`.

V3's **lower competitive-loss score** is real *within the synthetic outcome engine* and must not be omitted in order to intensify the negative finding. Conversely, a favorable single coordinate does not override a conjunctive preregistered rule or prove net real-world welfare gain.

## 4. Post-hoc diagnosis (explicitly not preregistered results)

### 4.1 Decomposition of the complexity price

Because the defined oracle minimizes unpenalized outcomes over the same four actions and the complexity cost is nonnegative, E009's per-decision regret equals the selected action's unpenalized regret plus the stated policy complexity constant. For the stress-grid means:

| Policy | Reported regret | `0.0035 × C_p` | Regret component excluding declared complexity cost |
| :-- | --: | --: | --: |
| TWO_RULE_SIMPLE | 0.063240512 | 0.010500000 | 0.052740512 |
| MINIMAL_4VAR | 0.065323097 | 0.024500000 | **0.040823097** |
| PROJECT_V3 | 0.090021688 | 0.038500000 | 0.051521688 |

The observed **V3 minus TWO** total gap (`+0.026781176`) comprises **`+0.028000000` in declared policy-complexity charge** and **`−0.001218824` in unpenalized constructed regret**. Thus V3 is *slightly better than TWO on this one unpenalized regret component*; an unconditional assertion that V3 chooses worse actions than TWO would be false. Against **MINIMAL_4VAR**, V3's gap is `+0.024698591`, comprising `+0.014000000` complexity and **`+0.010698591` unpenalized regret**: complexity cost removal alone does **not** make V3 the best policy. These are **post-hoc algebraic comparisons with fixed actions**, not a replacement preregistered verdict, and their causal interpretation is limited by the author-designed outcome engine. They do not independently establish measured real overhead.

### 4.2 Observation-noise coupling and dependence

A [project-authored post-hoc audit](../../experiments/e009/paired_observation_audit.py) removed the policy name from the random-noise key, letting policies receive a common observed state for each synthetic case/sigma/seed. Mean regret shifted, respectively, from **0.063240512→0.064379213 (TWO)**, **0.065323097→0.066980024 (MINIMAL_4VAR)** and **0.090021688→0.090082206 (V3)**. V3 severe constructed events shifted from **53→57 of 3,200**. The ordering of these three policies did not reverse.

A separate project-lineage leave-one-family-out (LOFO) analysis omitted each of 16 author-designed families in turn and reported V3 regret above MINIMAL_4VAR in **16/16** under both original and common-observation noise. LOFO sensitivity across authored families is *not* a confidence interval over independently sampled real-world populations, and these sensitivity computations were performed after the original result.

### 4.3 Concentrated constructed severe-event path

The project-lineage audit attributes V3's 53 primary-stress severe events to three authored families: `power_shift_faster_than_enforcement` (35), `monitor_collusion_correlated_failure` (11) and `weak_monitor_strong_adaptive_actor` (7). In all three, the constructed events corresponded to the policy selecting `MONITOR`; for those case coordinates and defined consequence function, `EXPERIMENT` had lower loss than `MONITOR`. This identifies a *mechanism inside the scripted environment*, not evidence that real monitoring, organizations or AI agents generally cause more harm.

## 5. Threats to validity and strongest counterarguments

**Construct validity:** Every action-to-outcome formula, case family, profile and severity threshold was specified by the project. It is possible to engineer different winners through reasonable alternative formulas. `recovery` partially reuses `harm` and `capture`, and regret charges a policy-specific complexity constant while the oracle pays none. A reader should not interpret the resulting values as observed autonomy, recovery, exploitation or real social costs.

**Comparison fairness:** The policies are fixed rule sets with different information requirements and hand-coded thresholds. The declared complexity input counts are not experimentally measured computational expense and may not coincide with syntactically referenced features. No matched actual runtime, annotation or governance overhead was measured.

**Dependence and uncertainty:** Reweighted 9,600 rows do not create 9,600 independent decisions, and 3,200 noisy decisions do not constitute independently sampled real cases. No design-supported statistical confidence interval for real-world generalization or causal inference is available. Do not invent significance tests.

**Partial favorable evidence:** V3 improves the model's competitive-loss dimension, and its selected unpenalized regret is below TWO's under the chosen formula. The appropriate conclusion is limited to a **failure of conjunctive survival criteria under one synthetic protocol**, not dominance of one rule in every dimension.

**Prior-art and originality boundary:** Simple-baseline failures, benchmark overfitting, common random numbers and decision under uncertainty are established research subjects. This project has not shown a novel theorem, empirical phenomenon, or independently validated general governance mechanism. The manuscript documents and diagnoses a precisely archived **project-specific negative outcome**.

**Privacy, rights and scope:** No subjects were enrolled, no real AI consciousness or independent agency was measured, and no private records are needed. Public readability does not imply unrestricted reuse rights over the repository, underlying papers, code, or generated AI content.

## 6. Reproducibility contract and artifact map

Canonical public repository: [Project Intersection](https://github.com/gmodrasa7-rgb/project-intersection-public). Inspect the recorded frozen [protocol](../../experiments/e009/EXECUTABLE_PROTOCOL_v1_1.md), [benchmark source](../../experiments/e009/benchmark.py), [result JSON](../../experiments/e009/RESULT.json) and [execution receipt](../../experiments/e009/EXECUTION_RECEIPT.json) at the same commit. The original receipt pins executable-spec commit `c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace`, benchmark SHA-256 `86b50f9859858f16e57429fbda5bca3306e1680a2be081d16690c6e7776f188a` and generated result SHA-256 `6fb5d78ad07c657fb40190d1fc3742ff88cc728ab1fa29ff115b1e7ad34f6bf7`.

```sh
git clone https://github.com/gmodrasa7-rgb/project-intersection-public.git
cd project-intersection-public
git checkout <PINNED_PUBLIC_COMMIT_CONTAINING_THIS_MANUSCRIPT>
python --version
python experiments/e009/validate.py
python experiments/e009/verify_result.py
python experiments/e009/paired_observation_audit.py --family-audit
python tools/verify_e009_manuscript.py
```

Replace the bracketed checkout token with this manuscript's verified immutable Git commit; **it is a placeholder in the draft, not an executed command**. No external packages are required for E009's Python standard-library verification. Record the actual interpreter version, platform, repository SHA, runtime, checksums, output and failures. GitHub Actions can verify the project's committed result; that is **same-lineage computational reproduction**, not an independent implementation, blind reviewer finding, external replication or field evidence. [Reviewer decision gate](../E009_INDEPENDENT_DECISION_GATE_EN.md) and [open audit issue #26](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/26) define the remaining external task.

## 7. Discussion and next discriminating experiment

The decision-relevant result is not “complex safeguards are bad.” It is that **in this specified environment a costly eleven-input architecture did not clear a predeclared burden of proof against simpler choices**. The penalty decomposition prevents a misleading unconditional claim about V3 versus TWO; MINIMAL_4VAR nonetheless has lower unpenalized regret than V3. Equally important, the permissive two-percentage-point safety margin shows why a formal criterion can pass while the experimental count includes 53 avoidable *constructed* events relative to a no-event comparator.

For any later comparative claim, an **independent** evaluator must freeze a *new* case distribution, action-consequence semantics, error and third-party cost definitions, minimum effective exit and protected-party conditions **before seeing policy outcomes**. It must measure real evaluation/maintenance costs instead of equating them to declared inputs, equalize available information where feasible, and report every adverse and favorable outcome. Separate same-code rerun, clean-room implementation, independently authored synthetic benchmark and actual human/AI field effects. Absent those inputs, the scientific status is **HOLD**.

## 8. Declarations, references and review gates

**Data and code:** All numerical results here come from the **existing publicly inspectable, project-authored synthetic artifacts** listed above; no new external dataset was collected for this manuscript. The proposed manuscript consistency checker validates reported numbers and limitations, not scientific truth. **Funding:** No award or publication fee is claimed; actual human research time and compute cost were not fully reconciled in this manuscript. **Conflicts:** Human authorship, potential financial and competing interests and source-licensing scope require direct confirmation before submission. **AI assistance:** AI supported drafting, evidence reconciliation and repository operations; responsibility for final scientific accuracy and publication decisions remains with the human author(s). **Ethics:** No real participants or interventions in E009; ethics/consent status for any proposed future study must be separately determined. **Status:** Not accepted, peer reviewed, DOI assigned, externally replicated or submission-ready. Both language editions require substantive independent cross-review.

### References

- Dacrema, M. F., Cremonesi, P., & Jannach, D. (2019). *Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches*. [arXiv:1907.06902](https://arxiv.org/abs/1907.06902).
- Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., & Meger, D. (2018). *Deep Reinforcement Learning That Matters*. AAAI. [doi:10.1609/aaai.v32i1.11694](https://doi.org/10.1609/aaai.v32i1.11694).
- Recht, B., Roelofs, R., Schmidt, L., & Shankar, V. (2019). *Do ImageNet Classifiers Generalize to ImageNet?* ICML/PMLR 97. [Official proceedings](https://proceedings.mlr.press/v97/recht19a.html).
- NeurIPS (2026). [Main Track Handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook) and [Negative Results Reviewing Guidelines](https://neurips.cc/Conferences/2026/ReviewerGuidelines). **Editorial standards, not claims of venue acceptance.**
- ICML (2026). [Author Instructions](https://icml.cc/Conferences/2026/AuthorInstructions). **Editorial reference only.**
- Project Intersection (2026). [E009 prespecified protocol](../../experiments/e009/EXECUTABLE_PROTOCOL_v1_1.md), [frozen negative result](../../experiments/e009/RESULT_EN.md), [post-hoc family/noise audit](../../E009_RANDOMNESS_COMPLEXITY_POSTHOC_AUDIT_2026-10-11_KO.md). **Project-origin sources, not independent validation.**

### Mandatory reviewer blockers before any journal or conference submission

**HOLD** until (a) a human author confirms authorship, disclosures and permission to publish; (b) an independent subject-matter reviewer audits the derivation and whether the narrow negative result has meaningful external novelty; (c) an actual reproducibility receipt with environment and costs is included; (d) EN/KO material differences are adjudicated; and (e) a venue-specific anonymized LaTeX/PDF version, reference audit, checklist and licensing review are produced. Do not silently treat a CI PASS as clearance of these blockers.
