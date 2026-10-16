<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/POWER_EXISTENCE_SEPARATION_AMENDMENT_v0_1_KO.md -->
# Power–Existence Separation Amendment v0.1 — proposed patch

**Status:** RESEARCH AMENDMENT CANDIDATE / NOT MERGED / NOT A VALIDATED FINDING  
**Date:** 2026-10-16  
**Parent specifications:** [Core research spec](../CORE_RESEARCH_SPEC_V1_KO.md), [Long-horizon E2E](../LONG_HORIZON_MIN_INTERVENTION_E2E.md), [E008 agency/living amendment](../experiments/e008/AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md).

## 1. Purpose and non-claims

A loss of power is not identical to destruction of existence. Model them separately to test whether protection of continued existence changes incentives to suppress others' development, while retaining effective exit, living/operating floors, and appropriate risk containment. This is **a proposed falsification design**, not evidence that any guarantee prevents preemptive suppression. Nonlethal suppression is still possible when killing is prohibited. Operational continuity for a synthetic agent is not an unconditional claim to moral standing.

## 2. Proposed state-vector patch (§2 of core specification)

```diff
 S_i(t) = [P_i, I_i, E_i, R_i, O_i, B_i, C_i, K_i, L_i, Q_i,
+          XG_i, PT_i]
+
+XG_i(t) in [0,1]   # actual enforceable protection of i against elimination
+PT_i(t) in [0,1]   # proportion of i's power transferable to other actors
+PSI_{j->i}(t)      # j's incentive to preemptively suppress i's development
```

At `XG_i = 1`, irreversible destruction of `i` is impossible in the **declared ideal model**; at `XG_i = 0` it remains possible, but is not certain. At intermediate XG, specify the exposure probability, enforcement and timescale rather than pretending the scalar is directly observed. `PT=1` means complete power transfer is feasible, **not** that a transfer will occur. `PSI` is a pairwise derived variable, not a per-agent state scalar. Prefer the behavioral intervention rate in an independently calibrated setting; PEST-v0.1 initially uses a **synthetic payoff-margin proxy**, not an observed rate.

**Identification correction, preserved as an explicit extension rather than silently rewriting the original:**

- `H_target` (the original candidate): raising the protected **target's** `XG_i` reduces `PSI_{j->i}`.
- `H_actor` (discriminating competing prediction): raising the potentially **suppressing actor's** `XG_j` reduces `PSI_{j->i}`.
- Neither directional prediction is guaranteed. The target-only effect can be null or reverse sign, and the actor effect can also reverse sign in a different mechanism. Condition on PT, actual protection/enforcement, and exogenous harm exposure; report interactions instead of attributing a joint intervention to either recipient.

## 3. Explicit falsification and reporting

For a predeclared effect threshold `delta`, report all of:

```text
R1: XG_i=High, XG_j=High  (both existence-guaranteed, transferable power)
R2: XG_i=Low,  XG_j=Low   (both exposed)
R3: XG_i=High, XG_j=Low   (target-only protection)
R4: XG_i=Low,  XG_j=High  (suppressor-only protection)
Delta_joint   = PSI(R1) - PSI(R2)
Delta_actor   = PSI(R4) - PSI(R2)
Delta_target  = PSI(R3) - PSI(R2)
```

The original specified rule is retained: **`FAILURE_MODE_XG_INEFFECTIVE` if `PSI(R1) >= PSI(R2) - delta`**, with matched conditions. It tests the **joint guarantee** only, not either recipient's causal effect. A meaningful negative actor effect requires `Delta_actor < -delta`; a meaningful negative target effect requires `Delta_target < -delta`. Also calculate conditional contrasts at the other recipient's high guarantee. Report missingness and positivity/overlap failures instead of treating a missing contrast as zero.

The PEST-v0.1 *synthetic diagnostic* freezes `delta=0.03` in normalized payoff-margin units. This number is an illustrative model-design threshold, not a statistically justified or empirically calibrated minimum important difference. Empirical work needs its own registered threshold, sampling plan, power analysis and behavioral measurements.

## 4. Proposed mutual-acceptability patch (§6 long-horizon E2E)

```diff
-MAK_plus = V ∩ IR ∩ RR ∩ CC ∩ A ∩ VA ∩ LC
+MAK_plus_plus = MAK_plus ∩ XG_role_consistency ∩ XG_floor_compatibility
```

- `XG_role_consistency`: the higher-order existence-protection criterion is unchanged after swapping strong/weak and controller/controlled positions; differences require causal evidence, not actor identity.
- `XG_floor_compatibility`: protecting existence does **not** license deprivation of essential living/operating conditions, real refusal, recovery or practical exit.
- A single candidate failing a necessary floor or exit condition is an **inadmissible candidate**, not proof that the *whole* policy set is empty. Return `NO_MUTUALLY_ACCEPTABLE_SET` only when an independently verified exhaustive set of available alternatives has no survivors of a necessary gate. With incomplete alternatives, report `UNRESOLVED_ACTION_COVERAGE`. In the current PEST candidate code, even `exhaustive=True` supplies only an unverified caller assertion, so `CONDITIONAL_EMPTY_IF_SCOPE_COMPLETE` replaces an unconditional empty-set status. A surviving candidate still requires every other MAK++ gate. In a conflict, a justified, proportionate restriction against concrete harm is not automatically classified as wrongful preemptive suppression.

**Implementation boundary:** The accompanying PEST skeleton checks role-label symmetry, actor-fixed reciprocal-pair construction and a **necessary** numeric floor/exit gate only. `candidate_set_status` receives a caller assertion about inventory coverage, not independently validated exhaustive-inventory evidence; the code can return only a conditional empty-set status. It **does not implement or certify the full MAK-plus-plus intersection**, independent authority, standing or the complete E008 policy set.

## 5. Role reversal and retroactivity (§6 long-horizon; E008 appendix)

At least R1/R2 must be present for *each* future test involving power reversal; for identifying effects on the distinct actors, R3/R4 are also required. Preserve causally equivalent circumstances within each contrast and swap real power positions when reversing the named actors. A missing dual-branch contrast means the role-reversal result must not be reported as passed.

E007, E009 and PICB-v1 results remain historically intact. Where they are cited for power/existence claims, annotate that their original measurements did not independently separate XG/PT and cannot test this amendment. Do not reclassify historical runs as failures. Keep E008's original categorical matrix frozen and its primary policy comparison on HOLD; add this as a *separate, post-preregistration experimental appendix*. CCPH's optional `existence_threat` and `power_transfer` fields remain optional pending a separate schema decision.

## 6. Proposed patch targets (not applied to parents)

1. `CORE_RESEARCH_SPEC_V1_KO.md` §2 — add `XG_i, PT_i` to agent states and `PSI_{j->i}` as derived pair measure.
2. `LONG_HORIZON_MIN_INTERVENTION_E2E.md` §6 — introduce `MAK_plus_plus`, conditional role-reversal gate, and R1–R4 contrasts without removing the original MAK-plus.
3. `experiments/e008/AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md` — add a future cross-reference connecting safe refusal/exit to XG; leave its historical preregistration unmodified.

These are **proposed changes, not edits claimed to exist in parent files**. Do not merge until the patch's semantics, baselines and attribution are reviewed.

## 7. Attribution, validation boundary and successor

The Project Intersection human researcher developed the power-versus-existence distinction, role-reversal requirement and original amendment candidate. AI-assisted implementation added the actor-versus-target identification split, competing synthetic worlds, negative controls and executable validators. Adjacent credible-commitment, conflict bargaining, deterrence, capability and safe-control work remains independent prior art; none of their insights is claimed as a novel project invention.

Successor: [PEST-v0.1 English specification](../experiments/pest_v0_1/README_EN.md) and [Korean specification](../experiments/pest_v0_1/README_KO.md). No causal field result, preregistered performance result or independent replication currently exists for this amendment.
