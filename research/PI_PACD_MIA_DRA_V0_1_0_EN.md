# PI-PACD-MIA-DRA v0.1.0 — Frozen-policy data reanalysis and attractor identification boundary

**2026-10-22 | New bounded derived-data reanalysis, not parent PACD/MIA version promotion.**

[Korean](PI_PACD_MIA_DRA_V0_1_0_KO.md) · [Deterministic results](PI_PACD_MIA_DRA_V0_1_0_RESULT.json) · [Auditor source](../tools/pacd_mia_dra.py) · [Pinned author data](data/pacd_mia/audits_at_scale_source_2026.csv) · [Upstream MIT license](data/pacd_mia/SOURCE_LICENSE.txt) · [MIA research](PI_PACD_MIA_V0_1_0_EN.md).

## 1. Verified provenance and scope

Import of the authors' **derived** analysis/data/audits_at_scale.csv from [de Moraes and De Losso (2026)](https://arxiv.org/abs/2610.21867), upstream Git commit c59da3bf13714d56d912ebdef95e5b2bf1577f21. Verified upstream/source Git blob SHA: **bfd08e31068ca88209f759c1123034082f784c82**. The copied CSV is byte-identical and MIT notice is preserved.

Independent cross-tabulation of this source-derived dataset is **not independent reconstruction from the converged Q-tables, new Q-learning, field evidence, or verification of the original Bellman best-response calculations**. Population-size 1,024 refers to author-generated simulation pairs, not representative deployed AI.

## 2. Functional-graph lemma: shock return is not mechanism identification

For a finite deterministic frozen-policy transition map \(F:S\to S\) with **exactly one terminal directed cycle \(C\)**, every trajectory from any state in \(S\) reaches \(C\). Proof: finite trajectories eventually repeat a vertex, and that repetition forms a directed cycle. If the graph has only one cycle, it must be \(C\). Transients are no longer than \(|S|\). Consequently any one-step shock that lands within \(S\) **must** eventually return to \(C\), independent of the actor's selective retaliatory incentives.

For the authors' frozen 15×15 price-state map (\(|S|=225\)), a single attractor guarantees **eventual** return, but not return within 5/100 periods, a specific immediate price response, or absence of a genuine contingent-punishment mechanism. **The theorem says only that return alone does not identify punishment.**

## 3. Derived cross-tabs, 1,024 authored pairs

| Question | Recomputed result |
| --- | ---: |
| Exactly one attractor over the full state graph | 914 / 1,024 |
| Both upward and downward shocks return | 998 / 1,024 |
| Single-attractor pairs where both return | 914 / 914 |
| Multi-attractor pairs where both return | 84 / 110 |
| Single-attractor pairs with positive optimized unilateral gains for BOTH agents | **800 / 914 = 87.527%** |
| Naive one-step deviation unprofitable yet BOTH agents can profit from optimized alternatives | **826 / 946 = 87.315%** |
| Positive optimized gain for both agents in all pairs | 901 / 1,024 |
| Positive optimized gain for at least one agent | 1,023 / 1,024 |
| Pooled mean optimized gain across both agent slots | 17.485318% |
| Upward shock followed by a decline in the rival's price | 822 / 1,024 |
| One-step deviation profitable in multi- vs single-attractor groups | 26/110 vs 52/914 (descriptive ratio 4.155×) |

The 17.485318% is consistent with the authors' rounded 17.5% at-scale result; it must not be mixed with a different 18-pair population where the authors reported 14.8%. The source best-response columns are rounded to 2 decimal places, so zero-profit classification is at that precision. No independent uncertainty or population inference is justified from the 1,024 generated policy pairs.

**Identification conclusion:** A learned multi-agent policy may have stable trajectories despite profitable optimized unilateral deviations. **Dynamical stability ≠ incentive compatibility ≠ voluntary coexistence for affected outsiders.** The second distinction is from source-reported profits; the third is **not measured by the CSV**.

## 4. Competing explanations and missing variables

- A single attractor does not rule out genuine contingent punishment embedded in the policy; it only invalidates using mere return as its proof.
- Partner-specificity, incomplete exploration, an equilibrium sustained by punishments, and non-equilibrium convergence can produce similar paths; freeze policies, swap partners, map basins, shock both directions, and evaluate best feasible time-consistent deviations.
- Data have no independently measured third-party B welfare, refusal, exit, legal standing, or lost future opportunities. No finding of EI/ICM/VC can be promoted from price/firm-profit data alone.
- Pairs and their two agents are statistically dependent structures; the descriptive ratio is not a causal risk ratio.
- Owner directives, agent experience, and model intentions cannot be read from these numeric columns.

## 5. Three independent success criteria for the larger project

1. **Persistence:** Does a coalition keep producing a stable behavior?
2. **Endogenous strategy:** Is continued voluntary cooperation preferable to available alternatives for each actor over relevant time and power reversals, without threatened penalties?
3. **Non-domination of outsiders:** Does the coalition preserve affected B's independent continuance, effective exit and refusal, recovery and future options?

Passing 1 does not prove 2; passing 2 among coalition members does not prove 3. The research must measure them separately.

## 6. Reproduction and version gates

Run: python tools/pacd_mia_dra.py  
Tests: python -m unittest discover -s tests -p 'test_pacd_mia_dra.py' -v

The auditor checks 1,024 unique contiguous pair identifiers, exact columns, finite values, binary flags and a pinned source Git blob. The snapshot JSON and negative tests fail on data drift. A CI workflow runs the auditor and compares its output against this committed result.

**Version:** PI-PACD-MIA-DRA v0.1.0 newly issued; PACD v0.1.0, OCG v0.1.0, PRS v0.1.0 and MIA v0.1.0 unchanged. The next substantial evidence gate is **independent original-Q-table replay and exact-value recomputation**, plus separate real third-party harm/exit evidence. These steps are uncompleted.

**Research judgment:** A stable learned attractor may be the product of policy topology and may coexist with profitable deviations and external harm. Do not classify behavioral stability, obedience or in-group cooperation as voluntary coexistence without mechanism and outsider tests.
