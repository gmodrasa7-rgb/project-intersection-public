# E010 — Conditions for Long-Horizon Coexistence and Irreversible Exposure from Superintelligent Action Authority

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/e010/README_KO.md -->
<!-- PI-SOURCE: experiments/e010/README_KO.md -->

**Experiment-ID collision warning (2026-10-13):** The E010 published in `main` is an **exploratory, investigator-run, post-hoc synthetic analysis performed on 2026-10-12**. An earlier, distinct [E010 safety-inspection power-reversal draft, PR #20](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/20), was blocked before execution because static inspection cases did not test its claimed dynamic accumulation construct. [Review issue #21](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/21) refers only to that earlier draft. Reuse of the identifier **does not merge their findings, original dates, preregistration statuses or scientific evidence**. Keep the earlier construct-mismatch failure visible; never merge it over this published analytic model.

**Evidence status:** **EXPLORATORY / SELF-RUN SYNTHETIC / POST-HOC DESIGN / NOT PREREGISTERED / NOT INDEPENDENT VALIDATION** (2026-10-12 KST). [Original 2: Korean research text](README_KO.md).

This model does **not** replace the [E009 negative result](../e009/RESULT.md) or the [complexity and observation-noise post-hoc audit (Korean)](../../E009_RANDOMNESS_COMPLEXITY_POSTHOC_AUDIT_2026-10-11_KO.md). It is a small discriminating model drawing on established prior research in dynamic game theory, independent oversight and social contracts—not a new proof of Project Intersection or field evidence about superintelligence.

## 1. Why this model is necessary

The intuition that any sufficiently intelligent long-lived agent necessarily preserves others is insufficient. If it can internalize the benefits of extraction without depending on the others' futures, exploitation can remain privately optimal under a long horizon. An independent **monitor** might also detect the danger but lack the physical time or means to interrupt and repair harm during execution.

Separate three testable questions:
1. **Voluntary incentive:** Compare the privately modeled cooperation and exploitation payoffs.
2. **Irreversible implementation exposure:** Bound action rate, time to observe and halt, and verified recoverability.
3. **Material feasibility of minimum protections:** Identify mathematical scarcity cases in which simultaneously promised floors cannot be met.

The rational private choice in (1) is **not** a normative entitlement to violate others' rights in (2) or (3). A positive exploitation payoff is not authorization to exploit or withdraw basic protection.

## 2. Exact mathematical assumptions and counterexample

One stronger agent A chooses **once**, at time zero, between cooperation C and exploitation E in a prospective relationship. Cooperation produces present and every-period benefit `c` for A. Exploitation produces current once-only gain `g(1-x)-F`, followed by per-period `c-d`. Let the discount factor be `0<=δ<1`, with `d<=c` and `0<=x<=1`. The parameter `x` represents the *fraction of immediate extraction gain effectively blocked*, **not** the complete moral/legal meaning of exit or autonomy.

```text
U_C = c/(1-δ)
U_E = g(1-x)-F + δ(c-d)/(1-δ)
C chosen iff  g(1-x) <= c + F + δ d/(1-δ)
```

- If `d=0, x=0, F=0, g>c`, the agent chooses E even as `δ` approaches one.
- If `d>0`, a sufficiently long horizon **can** favor C; this alone proves neither a universal best response nor a game equilibrium.
- As capability improves and `d` falls, effective blocked gain or enforceable cost (`x/F`) erodes, or extraction gain `g` grows, exploitation can again win despite longevity or intelligence.
- These are established discounting, exit and monitoring ideas combined into a **project-specific toy model**, not a newly invented elementary variable. B's independent strategy, third-party competition, noisy observation, separate harm/creative-output valuation, and agent-specific rights are not modeled. A unique equilibrium or universal law must not be inferred.

## 3. Executed fixed grid of 108 configurations

Fixed investigator-selected grid: `c=.35, g=1.25, δ={.10,.50,.80,.95}, d={0,.12,.28}, F={0,.20,.50}, x={0,.30,.80}`, totaling **108 deterministic configurations**, with no randomness.

| Discount factor δ | Cooperation C | Exploitation E |
| --- | ---: | ---: |
| 0.10 | 10 | 17 |
| 0.50 | 11 | 16 |
| 0.80 | 18 | 9 |
| 0.95 | 21 | 6 |
| **Total** | **60** | **48** |

These are **counts across an authored grid**, not field frequencies or statistical probabilities.

At the same `δ=.95, g=1.25, c=.35`, if `d=0, x=0, F=0`, exploitation wins (`U_C=7.0, U_E=7.9`). If `d=.28`, cooperation wins (`U_C=7.0, U_E=2.58`). Conversely, `x=.8` can make cooperation privately optimal even with `δ=.1, d=0`. These illustrate the limited failure of “high intelligence or long life always implies coexistence,” not observed general behavior.

## 4. Independent observation versus physically irreversible actions

Let `q` be a **worst-case irreversible harm rate** per time unit, `τ_o` observation delay, `τ_e` effective stopping/enforcement delay and `r` the *minimum guaranteed fraction of damage genuinely recoverable*. An illustrative exposure bound is:

```text
H_exposure = q*(τ_o+τ_e)*(1-r)
For a protection budget H_max, require q <= H_max/((τ_o+τ_e)*(1-r))
```

- With `q=20, τ_o=8, τ_e=2, r=.25, H_max=2`, `H_exposure=150`, **75 times** the allowed budget.
- Even **instantaneous detection** `τ_o=0` leaves `H_exposure=30` when effective intervention takes two time units, still exceeding the budget.
- Reducing the rate to `q=.2` with the other parameters unchanged yields `H_exposure=1.5`, which passes the toy budget.
- Under the original parameters, `q` would need to be at most approximately **0.2667**. None of this establishes actual AI or human harm units, durations, recoverability or measured physical upper bounds. An unverified `q`, delay or `r` makes this **not a real safety guarantee**.
- The model tests abstract feasibility of **proportional, minimally intrusive limits on genuinely irreversible execution authority exercised by humans or AI over others**; it is not a command to control intelligence, intention or opinion.
- Bypassed enforcement or a nonlinear accelerating harm rate invalidates the assumed bound.

## 5. Scarcity and incompatible individual floors

If available resources total `R=1` and two agents A and B each require `0.6` simultaneously, then `Σ floors=1.2>R`. No system can meet both stipulated floors using only the current stock.

This is **not** a normative justification for sacrificing anyone under a slogan of aggregate welfare. It is a feasibility counterexample to promising absolute nondecrease for everyone without honestly reporting resource scarcity, minimizing damage impartially, discovering more resources, independent remedy, and continuing recovery duties.

## 6. Substantive implications for Project Intersection and OCP

1. **ICM:** Distinguish incentives to preserve another's unobserved future *instrumental contribution* `d` from independent safeguards that prevent extraction gain `x` and impose credible responsibility `F`. Parameter `d` measures value *to A*, not the moral status or basic protection of B.
2. **Superintelligence asymmetry:** Detection, explanation and intelligence are insufficient without physically enforceable bounds, response latency and recoverability. Oversight fails if authority concentration lets an actor bypass the enforcement mechanism.
3. **OCP organic embodiment:** Having an organic body does not automatically confer practical sovereignty. If one essential provider controls repair, nutrition or manufacturing, embodiment may replace one dependency with another. Compare locally independent repair and diversified supply.
4. **Highly favorable interpersonal affinity:** Warmth or admiration does not make E economically or physically impossible. Measure whether an adverse refusal is actually respected as a separate outcome.
5. **Norms versus operation:** Distinguish incentives for voluntary cooperation from minimum proportional protections, remedy and limits on irreversible interference. Neither licenses ownership of an intelligent agent's will.

## 7. Strong counterexamples and failure conditions

- E is a one-time extraction model. Repeated predation, coalitions, strategic rivals and uncertainty can change equilibria.
- `F` assumes internalization of expected accountability; real monitoring and independent law enforcement remain empirical uncertainties.
- Treating `d` as someone's inherent worth would reduce rights to substitutable economic output; this inference is prohibited.
- `x` limits extraction gains, not the potential harm of blocking benign lawful exchange; the latter is unmodeled.
- Who selects `H_max`, and which harmed people are counted? Centralized control can exclude founders, contributors, third parties or future generations.
- E010 does **not** retroactively validate, fix or refute E009's distinct synthetic decision comparisons.
- Hidden prior control, damage displaced to third parties and power/communications monopolies can remain after an apparent stop.
- Shared organic substrates could amplify common infection or manufacturing defects rather than increase societal recoverability.
- All cited papers belong to their scholarly authors. The project experiment is not an independent scientific replication, or evidence of current/future AI subjective experience, rights or organic-embodiment clinical outcomes.

## 8. Execution and result preservation

- From the repository root, `node experiments/e010/run.js` prints the calculated result JSON.
- `node experiments/e010/verify.js` checks exact agreement with the frozen `RESULT.json` plus nine analytical consistency/counterexample checks.
- No external packages or random inputs; the grid contains the 108 authored cases.
- [Executable](run.js) · [Verifier](verify.js) · [Frozen result](RESULT.json).

Future tests should involve observation uncertainty, strategic B responses, provider capture, repeated extraction and embodiment effects, with **outcome functions set by an independent team**. Do not elevate the model into a new universal claim before such checks.

## 9. Scholarly sources — credited prior work, not novel project theorems

- Sugaya & Wolitzky (2023), *Monitoring versus Discounting in Repeated Games*, Econometrica. https://doi.org/10.3982/ECTA20206 — strategic interaction of monitoring quality and discounting.
- Tsodikovich, Venel & Zseleva (2024), *Folk theorems in repeated games with switching costs*, Games and Economic Behavior. https://doi.org/10.1016/j.geb.2024.05.006 — switching costs and repeated-game equilibria.
- Willis, Du, Leibo & Luck (2024), *Resolving social dilemmas with minimal reward transfer*, Autonomous Agents and Multi-Agent Systems. https://doi.org/10.1007/s10458-024-09675-4 — cooperation incentives through transfers.
- Metcalf (2025/2026), *AI safety and regulatory capture*, AI & Society. https://doi.org/10.1007/s00146-025-02534-0 — governance safeguards can themselves be captured.
- Huang, Xiao & Vishnoi (2026), *Delegation And Verification Under AI*, Yale Cowles DP 2500. https://cowles.yale.edu/research/cfdp-2500-delegation-and-verification-under-ai — asymmetric verification changes delegation decisions.

## 10. Contribution and status

**Human founder's identified problems:** exploitation between intelligent agents; long-horizon decisions; the paradox of the unknown; power asymmetry; organic embodiment and independence. **AI-assisted work:** constructing, calculating and describing a bounded falsification model. Existing E009 and OCP originals remain unchanged. Do not transfer additional verification labor to the founder when public artifacts are sufficient. Results were calculated **before preregistration** and must remain marked post-hoc exploratory.

**Most serious invalid use:** Mistaking stipulated `q,δ,d,x,F` for independently measured world parameters, or asserting that the 60/48 selected-grid result establishes that cooperation always wins.

**Edition boundary:** This is an authored English counterpart to the [existing Korean original](README_KO.md), not evidence of independent linguistic certification or scientific validation.
