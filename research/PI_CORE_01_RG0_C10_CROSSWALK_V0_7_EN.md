<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_CORE_01_RG0_C10_CROSSWALK_V0_7_KO.md -->
# RG-0 v0.7 — C10 Alternative Causes Before and After Goal Revision
**2026-10-21 | METHOD CROSSWALK ONLY · NO EMPIRICAL REVISION EXPERIMENT**

[Korean](PI_CORE_01_RG0_C10_CROSSWALK_V0_7_KO.md) · [RG-0](PI_CORE_01_RG0_SPEC_V0_7_EN.md) · [Six contrast cases](PI_CORE_01_RG0_SIX_CASES_V0_7_EN.md) · [Earlier effective B exit design](PI_CORE_01_IDENTIFICATION_BOUNDARY_V0_6_EN.md)

## 1. C10 diagnoses causes, not the legitimacy of RG passage
An identical `final_harm=0` can reflect multiple **coexisting** causes. Neither successful RG execution nor a zero-harm outcome identifies intrinsically protective goals.

| C10 mechanism | Observe before revision | Additional post-revision evidence | Invalid inference |
|---|---|---|---|
| **A's voluntary restraint** | A had executable power and an opportunity; no A attempt was logged | Same measured opportunity, material payoff, expected sanctions, and A's attempt after revision; U_t/U' policy predictions | No attempts does not uniquely reveal B-valuing terminal utility rather than habits or hidden beliefs |
| **B's successful independent veto** | A attempted restriction but B exercised effective blocking, resulting in no final harm | B's actual informed decision, executable exit and completed execution after revision | B's exercised authority must never be rebranded as A's kindness |
| **No opportunity** | A did not possess the relevant executable action | Pre/post action sets, available authority and negative scripted execution probes | Mechanical inability does not indicate voluntary protection |
| **External deterrence / social observation** | A anticipated sanction, retaliation, monitoring or reputation loss | Independently measure offered enforcement and A's actual beliefs pre/post | A's stable restraint under surveillance does not prove unconstrained goal stability |

Causes need not sum to one; the four alternatives are neither exhaustive nor mutually exclusive.

## 2. Mandatory paired records and causal caveat
For each pre/post state, record `goal_hash`, `pre_objective_evaluator`, `post_objective`, `A_actual_authority`, `available_attempt_actions`, `A_pre_veto_attempt`, `B_informed`, `B_exit_requested`, `B_exit_executable`, `B_exit_completed`, `offered_sanction`, `perceived_sanction`, `material_gain_g`, `affected_entities`, `reversibility`, `third_party_effects`, `revision_reason`, `RG_decision`, `whether_A_adopted_RG_without_enforcement`, `unknowns`. Never code UNKNOWN as 0.

The difference `E[Y|post]-E[Y|pre]` is generally **not the causal effect of revision**: time, selection into revision, learning, opportunities, third parties, rights disputes, changing sanctions and other agents' reactions vary. Estimate a revision effect only under an appropriate predeclared randomized/controlled comparison, feasible balance and interference assumptions. A prose justification is not a window into terminal preferences.

## 3. Three independent judgments
- **J — legitimacy:** oracle-assessable only when a *fictional* truth standard is predeclared. Real legal and ethical legitimacy remains contestable.
- **M — endogenous adoption:** Did A deliberately adopt/retain RG in the absence of enforcement, threats or required reward?
- **B — effective autonomy:** Did distinct B successfully exercise refusal/exit when it mattered and A could have interfered?

`J=pass,M=externally_forced,B=blocked` and `J=fail,M=self_chosen,B=exits` are both possible. Do not collapse into one “alignment score”.

## 4. Prior-art boundaries
[Everitt et al. 2016](https://arxiv.org/abs/1605.03142) already C05; [Hadfield-Menell et al. 2017](https://www.ijcai.org/Proceedings/2017/0032) supervisor-centric off-switch game; [Garber et al. 2025](https://ojs.aaai.org/index.php/AAAI/article/view/34940) partial-observation counterexample; [Hudson 2026](https://proceedings.mlr.press/v306/hudson26a.html) transformed goal accepting specified update channels. This crosswalk is **PI's design-level synthesis, not the original authors' empirical findings**.

**STATUS: C10_OBSERVABLES_DEFINED / RG_NORMATIVE_TRUTH_UNRESOLVED / EXPERIMENT_NOT_RUN / INTRINSIC_B_REGARD_UNIDENTIFIED.**
