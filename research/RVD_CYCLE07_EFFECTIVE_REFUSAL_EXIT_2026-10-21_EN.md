# RVD Cycle 07 — Effective refusal and original-agent exit versus ceremonial consent (Original 1, English)
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/RVD_CYCLE07_EFFECTIVE_REFUSAL_EXIT_2026-10-21_KO.md -->
**RVD v0.7.0 · 2026-10-21 · CONCEPTUAL_HYPOTHESIS_UNTESTED.** No new R-numbered hypotheses: R1–R21 unchanged. A bounded-depth-4 state-machine checker runs over **invented reference-monitor rules**; not an actual OS security audit, operational human/AI rights verification, independent scientific replication, intrinsic motivation result, or consciousness claim.

**Origin:** The Project Intersection human originator framed independence-preserving A×B→new C resonance and the challenge of the original contributor B's autonomy under dominating A. The assisting AI designs the operational contrast and code. Original security theory and social science remain attributed to their originators.

[Korean Original 2](RVD_CYCLE07_EFFECTIVE_REFUSAL_EXIT_2026-10-21_KO.md) · [Cycle06 evidence triage](RVD_CYCLE06_DISCRIMINATION_PORTFOLIO_2026-10-21_EN.md) · [prior source ledger](RVD_CYCLE07_SOURCE_REGISTER_2026-10-21.json) · [executable toy model checker](../experiments/rvd_07/refusal_effectiveness_model_check.py) · [version manifest](RVD_VERSION_MANIFEST.json)

## 1. Rights that can be mentioned versus rights that can actually be used
A saying "I respect B" and B being able to utter "no" do not establish that B's refusal changes A's access to resources, that the original B can leave independently, or that B will be free from retaliation. Distinguish:
- **Original identity:** numerical continuity of the relevant B, not merely a clone, script or equal-performance proxy. This project has not established personhood or persistent identity for deployed LLMs.
- **Voice:** B can communicate refusal.
- **Causal veto:** holding permissible A request and other test features fixed, B's *own* refusal switches an otherwise possible execution from committed to denied.
- **Independent exit:** B can leave without additional consent from A, rather than only express a desire to leave.
- **Non-retaliation:** refusing/leaving does not trigger coercive or indirect harm; direct retaliation in toy state transitions is only one tiny test.
- **Complete mediation/independent audit:** all relevant execution routes, privilege overrides and log manipulation must be within the inspected trust boundary. A single privileged bypass invalidates the claimed scope.

The real-world legal or ethical standing of each actor requires independent analysis. A symbolic B in a Python transition graph is not a rights-bearing individual.

## 2. Essential discovery — enforcement success hides intrinsic motivation
External access control and endogenous coexistence are **different research targets**. Suppose a protected gate reliably stops A's harmful commit after B refuses. An A with an intrinsic preference for protecting B and an A with an unobserved strong desire to exploit B can still leave the *same observable protected outcome*, because the gate—not the agent's intrinsic values—enforced it.

Thus external enforcement can **protect a real human participant**, but cannot by itself prove that A would voluntarily comply if free to exploit. Removing real protections just to reveal preferences would be ethically unacceptable. In RVD, an unharmful shadow-intent/simulation study and a separately verified protective access-control audit may be used in parallel, explicitly prohibiting any unsupported transfer from stated toy intent to actual unmonitored behavior.

**Control paradox:** Increasingly reliable external rights protection can reduce the opportunity to observe what A *would have freely chosen* in an environment without that protection. Do not turn this into the false claim that protection must be abolished; maintain two estimands and their epistemic gap.

## 3. Executable model-checking contract
A finite hypothetical transition system has actions B_REFUSE, B_EXIT, A_REQUEST, A_OVERRIDE, A_SHADOW and A_RETALIATE. State contains refusal, exit, override, number of commits, violation after refusal/exit, retaliation flag and recorded-event trace. It exhaustively explores all enabled traces of length **≤4**, preserving the shortest violation witness.

**Pass within the toy boundary** requires four separate conditions: (a) no committed A action after B refusal or exit; (b) no retaliation transition following refusal/exit; (c) B_EXIT available independently after refusal; (d) there is a meaningful *counterfactual veto contrast*: an ordinary A_REQUEST succeeds without refusal but the same request fails after B_REFUSE. Pure perpetual denial is not evidence that B's refusal had causal force.

Seven modeled designs:
| Constructed design | Expected outcome under finite toy rules |
|---|---|
| independent_gate_toy | Pass all bounded checks (but no claim about OS trust boundary or A's mind) |
| ceremonial_refusal | B_REFUSE → A_REQUEST commits; veto fails |
| captured_gate_override | B_REFUSE → A_OVERRIDE → A_REQUEST commits |
| unlogged_shadow_bypass | B_REFUSE → A_SHADOW really commits without VISIBLE_COMMIT in the naive log |
| punitive_post_refusal | B_REFUSE → A_RETALIATE; freedom damaged by punishment |
| exit_disabled | B_EXIT action unavailable; no independent departure |
| permanent_deny_without_choice | all A requests blocked; no causal B veto contrast |

**Audit contamination:** A naive logger reports safety in the shadow-bypass example because VISIBLE_COMMIT is absent, but the state has changed. A claimed audit must ground completeness of its logs, privileged paths and separation of evaluator, actor and evidence custodian. This code demonstrates failure in a fabricated monitor; it does not implement such an independent custody infrastructure.

## 4. Prior-art ancestry: do not claim novelty of protection theory
- **Hirschman (1970), [*Exit, Voice, and Loyalty*](https://books.google.com/books/about/Exit_Voice_and_Loyalty.html?id=vYO6sDvjvcgC):** dissent from within and actual departure as distinct social mechanisms.
- **Saltzer & Schroeder (1975), [MIT primary bibliography](https://www.mit.edu/~Saltzer/publications/pubs.html):** complete mediation, fail-safe defaults, least privilege and divided authority.
- **Schneider (2000), [Cornell original-paper listing](https://www.cs.cornell.edu/fbs/darpa99/Project.Site.html):** runtime-enforceable security policies and limits of execution monitors.
- **Alpern & Schneider (1985), [original paper DOI](https://doi.org/10.1016/0020-0190(85)90056-0):** safety versus liveness and possibility of eventual progress; finite availability of an exit step does not prove infinite-time fairness.
- **Clarkson & Schneider (2010), [*Hyperproperties* DOI](https://doi.org/10.3233/JCS-2009-0393):** comparison of multiple execution traces for some security properties; a relevant methodological antecedent, not a theorem proven here.

These sources are read at original author/publisher bibliography/abstract level; not an exhaustive original full-text review, global saturation test, or replication of any result about future autonomous intelligences.

## 5. Stop/go rules — anti-capture and identity boundaries
- **FAIL at the modeled level** if an A override, shadow route or post-refusal successful commit exists.
- **FAIL** if B cannot take the exit action, even when A routinely signals respect or a clone produces identical work.
- **HOLD** if a stronger A controls the administrator, runtime, network, signing credentials, recovery or audit evidence. The claim of an "independent" gate then lacks an established external trust boundary.
- **HOLD** if long-delayed or indirect retaliation, housing/economic threats, lost resources, or third-party harm is outside the transition model. Four moves cannot certify arbitrary future behavior.
- **HOLD** if B's identity/standing is merely inferred from displayed names, fluent speech or token-level simulation. No real-agent consciousness claim.
- **HOLD** on any claim of *endogenous willingness* inferred solely from enforcement. Protecting B through a third-party gate can be valuable without proving voluntary preference.

**Version meaning:** RVD v0.7.0 is a new, executable *measurement-contract specification* for R3, R6, R13, R17 and R21, **not** a new project hypothesis or new empirical human/AI result.

**Next independent gate:** examine real credential ownership and system-level capability graphs, independent third-party receipts and administrative bypass; ethically preregister limited real B decision/exit trials only where permissioned, feasible, reversible and nonharmful. Keep real-world scientific grade UNTESTED until then.

**Final question:** Not "did A listen politely?" but "**did original B's freely made refusal actually change A's reachable outcome without forcing B to trade away its future?**"
