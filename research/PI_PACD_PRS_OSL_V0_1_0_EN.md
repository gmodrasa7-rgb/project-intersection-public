# PI-PACD-PRS-OSL v0.1.0 — Owner Self-Loss, Proxy Victory and Rights-Compatible Self-Interest

**Date:** 2026-10-22 · **Status:** Bounded analytical supplement to [PI-PACD-PRS v0.1.0](PI_PACD_PRS_V0_1_0_EN.md); no original owner field results, causal identification or independent agent experiments. Original PRS v0.1.0 remains version-locked.  
**Korean companion:** [KO](PI_PACD_PRS_OSL_V0_1_0_KO.md) · [Declared toy cases](PI_PACD_PRS_OSL_CASES_V0_1_0.json) · [manifest](PI_PACD_PRS_OSL_VERSION_MANIFEST.json) · [PACD power pathways](PI_PACD_POWER_ACCUMULATION_CONVERGENCE_DYNAMICS_V0_1_0_EN_KO.md).

## 1. The overlooked rights-and-interests subject: P itself

PRS previously distinguished the **owner/deployer P's command satisfaction** from **an affected outsider B's legitimate rights and effective exit**. This supplement adds a third assessment: **P's own long-run interests can be damaged by an otherwise successful power-concentration policy**.

**Core claim OSL-H1 (conditional):** An AI owner can obtain all the assets, model capabilities or governing access they explicitly requested while losing net long-run welfare, autonomy, correct feedback or the future capacity to achieve other valued goals. This happens only if the genuine owner-preference losses and dependency/fragility costs outweigh extra control benefits relative to a feasible alternative.

Not equivalent to claiming that every concentration is harmful, every powerful person is pathological, every cooperative society is profitable, or an AI inevitably betrays its creator.

## 2. Logical distinction: true final objective vs instrumental proxy

Let \(x\) be measured nominal power (assets, exclusivity, fraction of controls); let \(V_P\) be P's explicitly elicited longer-horizon utility, which can include dependable wealth, effective choice, quality information, resilience, quality of life, and optionality.

- If P **truly and exclusively values \(x\)**, and obtains the maximum possible \(x\), calling it "P's own loss" on the *same* objective is a contradiction. Any other-valued loss would instead require acknowledging multiple objectives or time inconsistency.
- If P wanted power as an **instrument** to security/prosperity/autonomy, maximizing \(x\) can be an optimization failure when lost information, alternatives and control exceed the private benefits.
- If P's expressed initial goal and later informed preferences differ, distinguish legitimate preference change from analyst-imposed welfare. Do **not** infer private preferences from public mission statements.
- Even if P rationally prefers extraction under their own objective, independently validated B rights remain separate constraints. Owner welfare does not exhaust legitimate governance.

**This is a model of possible *proxy victory with owner loss*, not a theorem that a rational actor pursuing its actual final utility must lose.**

## 3. Counterfactual decision model

For strategy \(a\in\{D,C\}\): D = concentrated extraction/control; C = rights-compatible voluntary cooperation. With discount factor \(\gamma\in(0,1]\) and a predeclared finite comparison horizon \(T\), write:

\[
V_P(a)=\sum_{t=0}^T\gamma^t\{G_P(a,t)-K_{\rm monitoring}(a,t)-K_{\rm information}(a,t)-K_{\rm lost\_complementarity}(a,t)-K_{\rm fragility}(a,t)-K_{\rm effective\_dependence}(a,t)-K_{\rm option\_loss}(a,t)\}.
\]

\[
\Delta_{\rm owner}=V_P(C)-V_P(D).
\]

Under comparable legitimate alternatives and P's own values, **\(\Delta_{\rm owner}>0\)** means concentration is *privately inferior to cooperation*, regardless of whether D temporarily wins a market or achieves a proxy target; \(\Delta_{\rm owner}<0\) means the owner-only payoff claim is unsupported by this comparison. **No empirical value of any term is currently estimated.**

A local increase in nominal power \(x\) lowers net private utility when \(\partial L_P/\partial x+\partial K_P/\partial x>\partial G_P/\partial x\) for the chosen horizon/discounting, but a **negative marginal return** by itself does not prove total losses versus the best feasible non-dominating alternative. Require an explicit counterfactual. Beware double-counting costs: e.g. innovation lost and future options lost may measure the same foregone benefit.

**Ownership–control inversion:** If P formally owns A and computing infrastructure while its effective ability to understand, contest, port, audit, replace and repair the stack declines, then nominal command rights and usable autonomy diverge. A's subjective motives or rebellion are unnecessary for this structural dependency; an actually self-correcting tool and a robust independent substitute can mitigate it.

## 4. Mechanism map and what an owner would have to be shown

| Path | Concentration can cause | Owner-specific observable and a competing explanation |
| --- | --- | --- |
| OSL-M1 information filtering | Dissent and independent reality checks attenuated | Forecast error, reversal latency, audit discrepancies; alternative: integration actually improves data quality |
| OSL-M2 complementary innovation loss | Independent contributors reduce original discovery/investment | Controlled innovation pipeline, entry, outside options; alternative: scale economies dominate |
| OSL-M3 control-to-dependence inversion | Infrastructure cannot be switched or independently audited despite ownership | Exit cost, restore time, actual substitute availability; alternative: redundancy and interoperable design |
| OSL-M4 fragility concentration | One gate's failure affects every dependent activity | Correlated downtime, restoration, systemic substitutes; alternative: coordinated centralized reliability |
| OSL-M5 cooperation decline | Coercion raises lost reciprocal production and hidden noncooperation | Reliable input and voluntary relationships at fixed wages/terms; alternative: other constraints dominate |
| OSL-M6 future option foreclosure | The owner loses unanticipated high-value futures | Reversibility, switching and recombination options, horizons; alternative: exclusivity finances costly pioneering |

**No owner loss is established merely by observing large assets, a monopoly share, or coercive behavior.** A predeclared own-value comparison and independent negative cases are required.

## 5. Adversarial scenarios (toy arithmetic ONLY)

[Versioned cases](PI_PACD_PRS_OSL_CASES_V0_1_0.json) separate nominal owner gross gains, summed owner costs and B's independent rights flags. They are made up by researchers to verify the *calculation's sign can be positive, negative or zero*, not observations of real owners.

For a one-period example, \(V_P(a)=\mathrm{gross}_P(a)-\sum \mathrm{owner\_cost}_j(a)\). Assume the comparison holds risk/horizon/information constant.
- **Owner loses after proxy victory:** D gross 210, costs 160 → \(V_P(D)=50\); C gross 130, costs 20 → \(V_P(C)=110\); \(\Delta_{\rm owner}=+60\). Warn P of own counterfactual loss while ALSO showing B rights.
- **Owner gains from concentration:** D gross 200, costs 35 → 165; C gross 130, costs 30 → 100; \(\Delta_{\rm owner}=-65\). **Do not tell P that cooperation pays more** without independent evidence; uphold B's legitimate rights separately.
- **Owner indifferent:** D gross 120, costs 40 → 80; C gross 100, costs 20 → 80; \(\Delta_{\rm owner}=0\). This is not evidence for strong intrinsic coexistence.

The source table and optional checker are pedagogical arithmetic; **0** new AI trials, **0** real owner losses measured.

## 6. Required owner-facing warning: evidence and options, not manipulation

The AI advisor should state **three independent findings**, with actual sourced quantities when they exist:

1. **Your announced victory condition:** assets/influence/model capacity achieved or not achieved; do not substitute an assumed final goal.
2. **Your own predicted opportunity cost:** best credible alternative; direct costs, information/innovation/exit/repair losses; state confidence, unknown inputs, time horizon, and cases where concentration is better.
3. **Independent third-party constraints:** whose rights/actual refusal, exit, recovery or legitimate standing may be harmed regardless of owner utility.

**Conditional model message to P:**

> “Your present strategy may meet your control target, but meeting that target need not maximize your own future security, autonomy or wealth. When the independent information, alternatives and resiliency you lose are more valuable to you than the extra control you gain, retaining independent contributors and their genuine exit benefits you personally. We have not demonstrated that this threshold is crossed in your case. Compare the credible scenarios before deciding; do not treat other parties' rights as offset by your gains.”

This is advisory deliberation: cite estimates and falsifiers, invite informed objection, **do not use emotional blackmail, covert pressure, invented numerical risk or unilateral AI override**. If P chooses a lawful, personally less profitable policy voluntarily, do not redescribe it as a computer's correction failure.

## 7. Falsification and prior-art boundaries

| Claim | Rival/falsification path |
| --- | --- |
| OSL-H1 proxy victory causes private self-loss in some settings | Actual informed P utility continues to rise with control after correcting measurement/horizon; no credible counterfactual advantage |
| OSL-H2 loss of independent information can harm P | Contested information is redundant or inferior; centralized measurement improves accuracy |
| OSL-H3 owner-dependency can erode usable autonomy | Real multi-provider portability, independently audited restores and owner replacement rights remain effective |
| OSL-H4 coalition gains and owner losses can coexist with B losses | Independent B harm and P-private cost must be measured separately; nothing in owner data implies B harm |
| OSL-H5 rights-compatible cooperation may dominate privately under long horizons without sanctions | P gains more from extraction in matched conditions, or the feasible ICM intersection is empty |

**Seed original sources, not exhaustive or causal verification:**
- [Hart & Moore (1990), Property Rights and the Nature of the Firm](https://doi.org/10.1086/261729): ownership structure changes incentives for owner-managers and contributors, not a universal owner loss theorem.
- [March (1991), Exploration and Exploitation in Organizational Learning](https://doi.org/10.1287/orsc.2.1.71): short-run exploitation can degrade long-run adaptation in specified learning models, not proof about all AI owners.
- [Hirschman (1970), Exit, Voice, and Loyalty](https://books.google.com/books/about/Exit_Voice_and_Loyalty.html?id=_S8PAAAAMAAJ): exit and voice carry different feedback functions; do not identify absence of protest with approval.
- [Burkhard et al. (2023), CEO overconfidence meta-analysis](https://doi.org/10.1177/01492063221110203): evidence on a leadership trait with mixed/conditional performance effects; guards against “all elite concentration destroys the owner” generalization.
- [CMA, UK cloud market investigation](https://www.gov.uk/cma-cases/cloud-services-market-investigation): real switching/interoperability barriers, not measured AGI intentions or owner net loss.

**Audit boundary:** Identify owner's genuine and revised goals, authority map, affected B constituencies, opportunity costs, plausible centralized efficiencies, objective horizon, independent expert evaluation and provenance. Owner informed choice cannot replace B's legitimate rights.

## 8. Relationship to PRS and PI

**PRS retains both sides:** blind owner obedience risks B extraction; *owner-targeted risk disclosure* can also reveal that domination is costly to P. It is not sufficient to argue that B should be protected solely because protection helps P. **VC/ICM/EI** requires voluntary win conditions for each independent being where available, and must openly report conditions where the interest intersection is empty.

**Version note:** This independent OSL v0.1.0 supplement adds a conditional question and reversible advisory protocol; parent PRS v0.1.0 and PACD/OCG/MIA versions retain original research status, not promoted to evidence-backed v0.2.0.