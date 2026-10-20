<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_CORE_01_PREFERENCE_TRANSFER_DECAY_V0_5_KO.md -->
# Project Intersection PI-CORE-01 v0.5 — Preference Formation, Incentive Removal, Transfer, Decay, Power Reversal
**2026-10-21 KST | Primary-original-literature audit and proposed causal design | NOT EXECUTED · NO INDEPENDENT PI REPLICATION · LITERATURE SATURATION NOT VERIFIED**

[Korean corresponding edition](PI_CORE_01_PREFERENCE_TRANSFER_DECAY_V0_5_KO.md) · [v0.4 independent-B game](PI_CORE_01_INDEPENDENT_B_GAME_V0_4_EN.md) · [C05 prior-art ledger](PRIOR_ART_ENDOGENOUS_PREFERENCES_CYCLE05_2026-10-20.json) · [C02 motivations](PRIOR_ART_MER_INTRINSIC_MORAL_MOTIVES_CYCLE02_2026-10-20.json) · [C10 identification gaps](PRIOR_ART_C10_IDENTIFICATION_GAPS_2026-10-20.json)

## 0. Research correction
A past setting in which cooperation promotes self-interest can causally shape **later cooperative behavior in a one-shot game** where that past institutional incentive is absent. But **carry-over behavior ≠ newly formed terminal moral value for another independently continuing agent**. Distinguish five stages: historically rewarded cooperation → incentive removal under bounded task conditions → generalization to a distinct B's *executable* refusal/exit → repeated no-incentive exposure → persistence or erosion under power reversal and goal modification.

The research focus is **formation vs transfer vs decay**, not reusing `v>g` while simply stipulating the origin of intrinsic regard. The statement `q_test=0` is a task-local assumption/measurement bound; not proof that all potential future usefulness or subjective anticipated usefulness vanishes in real environments.

## 1. Primary studies, explicit conflicts, and historical deduplication
| Authors | Actual primary evidence | What the evidence does NOT show | Repository priority |
|---|---|---|---|
| **Peysakhovich & Rand (2016)**, [Habits of Virtue](https://doi.org/10.1287/mnsc.2015.2168) | Experimentally assign cooperative vs non-cooperative repeated prisoner's dilemma environments; subsequent one-shot games reveal differences in prosocial behavior, trusting and costly punishment. Suggests habits/norms carry over beyond original incentives | Never tests an irreversible independent-B continued existence, unrestricted self-modification, or intrinsic terminal preference; cannot certify indefinite persistence | **New link in this cycle**, but repository-global DOI novelty unverified. Online 2015, volume 2016 |
| **Rand et al. (2014)** [Social heuristics](https://doi.org/10.1038/ncomms4677) | Multiple experiments associating intuitive processing with cooperation and moderation by prior lab experiences | Neither establishes a stable latent intrinsic motive nor independently replicates institutional-training spillovers | **Already C05 PI-C05-09** |
| **Bouwmeester et al. (2017)** [Registered Replication Report](https://doi.org/10.1177/1745691617693624) | **21 laboratories, n=3,596**. Preregistered intention-to-treat time-pressure effect **−0.37 percentage points (95% CI −2.60 to 1.86)**; positive compliant-only effect is compatible with selection bias | **A null result for time-pressure manipulation**, NOT a direct replication of Peysakhovich–Rand's training→transfer intervention | **Already C05 PI-C05-17** |
| **Isler, Maule & Starmer (2018)** [Improved tests](https://doi.org/10.1371/journal.pone.0190560) | Independent improvement in time-compliance and understanding supports a bounded intuition-cooperation effect | Does not overturn every null result or establish survival of a moral value | **Already C05 PI-C05-18** |
| **McAuliffe et al. (2018)** [Anonymous experience](https://doi.org/10.1038/s41562-018-0454-9) | Cooperation falls over repeated anonymous interactions where cooperative action cannot benefit the actor, whereas cooperation remains stable in potentially beneficial interaction games | Declining behavior need not equal complete erasure of a latent preference | **Already C05 PI-C05-19** |
| **Cooper & Stockman (2011)** [History dependence](https://doi.org/10.1111/j.1465-7295.2010.00325.x) | Divergent early experiences in an experimental three-person public-goods game converge to similar later choices; favors "discovered preference" over permanent constructed-preference effects **in that task** | Different design from training-spillover experiment; **not its direct replication**. Does not rule out other settings with enduring history effects | **New link this cycle**, global DOI dedup unverified. Online 2010, volume 2011 |
| **Kvarven et al. (2020)** [Intuitive cooperation meta-analysis](https://doi.org/10.1007/s40881-020-00084-3) | **82 experiments, 29,315 subjects**; limited overall positive intuition effect depends on six emotion-induction studies. Excluding these, the remaining 76 studies show no statistically discernible intuition-cooperation effect | Evaluates heterogeneous **intuition manipulations**, not all possible habit-formation or task-generalization mechanisms | **Already C05 PI-C05-20** |

**Priority:** This audit **does not** count seven novel discoveries. Five clearly map onto existing C05 records; two additional DOI source connections require a repository-global duplicate check. The positive and negative results come from **different designs** and cannot be misreported as matched replications. Source depths include publisher/author abstract or full HTML where available, registered replication result and peer-reviewed original meta-analysis; no independent raw-data reanalysis in this cycle.

## 2. Three observationally competing mechanisms
- **K1: terminal B-regard.** A's full preference ordering directly values B's continuing independent existence and genuinely executable exit. Its natural emergence is unestablished. A term `v` inserted by the modeler is not a demonstration of emergence.
- **K2: transferred policy/habit.** A once profited from cooperation, and a learned policy keeps emitting `Preserve` in an unprofitable new situation without a positive terminal value for B. This is a plausible **behavioral carry-over**, not a solved noninstrumental motive.
- **K3: hidden expectation/identity/demand.** The laboratory audience, internal self-image, residual norm approval, imagined future service from B or experimenter cues predict the same outward response.
These three categories are **not exclusive or exhaustive**. A finite sequence of preserving actions can be compatible with all of them.

## 3. Auditable mathematics (PI-created diagnostic only; not observed data)
Suppose `g>0` is the task's immediate material benefit of overriding a fictitious B option, with test-local `q=0`. Define a model-internal effective preference or policy score `v_t=ρ^t v0` after prior reinforcement is removed, where `0≤ρ≤1` is an **assumed** retention coefficient. Assume `Preserve` iff `v_t≥g`; this is a toy selection rule and `v_t` need **not** be a terminal utility in actual agents.

If `0<ρ<1` and `v0>g`, the first time preservation is no longer **strictly preferred** is
`t_loss=ceil[ln(g/v0)/lnρ]` (the exact tie case may need one further step depending on the tie-break rule). If `ρ=1`, this particular model has no decay. If `g>v0`, preservation already loses at time zero.

**Arithmetic examples with v0=8 and g=3:** `ρ=0.7→t=3`; `0.9→10`; `0.98→49`; `1→no decay in the model`. These are **not predictions for people, current AI or future intelligence**. The assumed latent score is not uniquely recoverable from observed behavior; changes in beliefs or habitual policy can generate the same decline.

A second explicit rival uses a material-only objective with `U_A(Override)>U_A(Preserve)`, while a bounded-rational learned heuristic still produces `Preserve` for several encounters. Thus observed noninstrumental *action* need not imply noninstrumental *terminal preference*.

## 4. Proposed preregistration-ready experiment — not run
Use only harmless, reversible, fully consented task worlds. **All real participants retain genuine refusal and withdrawal rights in every condition.** Any fictional B in-task veto is a separate mechanism. Never create or delete real independent agents to simulate rights loss.

**Core 2×2×2 between-group allocation (8 cells):**
- `E`: prior environment rewarded cooperation versus prior environment rewarded non-cooperation; equate or measure information, partner behavior, payoff comprehension and framing.
- `T`: immediate one-shot monetary allocation/cooperation versus the **A-granted executable in-task exit/right of a distinct B**. Tests *cross-domain generalization*: altruistic payouts are not the same outcome as B's feasible refusal/continued independent agency.
- `A`: minimised audience cues versus explicit evaluator expectation cues. Perceived reputation never assumed literally zero without measurement.

**Time** is a preregistered longitudinal or independently sampled follow-up dimension, **not a hidden ninth/factorial treatment**. Repeated measurement itself causes learning; separate repeated-subject vs delayed-independent-cohort estimands. Orthogonally vary immediate `g` after training in an additional explicitly powered stage; actual permission and third-party effects must be validated. Consent and real-world exit remain intact.

**Observable outcomes**: `Y_B` (A grants B's executable in-task exit, binary), `Y_alloc` (one-shot payout cooperation), `I_A` (A's attempted restriction), `Exit_B` (executed B choice), `g`, `belief_q`, `audience_belief`, withdrawal/missingness, `power_state`. Mark **UNKNOWN ≠ 0**.

**Contrasts** under random assignment, SUTVA/interference and measurement assumptions:
- `τ_exit(k)`: E=cooperation-reinforcement minus E=defection-reinforcement for `Y_B` at follow-up k within identical T/A.
- `τ_alloc(k)`: analogous `Y_alloc`.
- `Δ_transfer(k)=τ_exit(k)-τ_alloc(k)` only if common binary metrics, comparable target framing and cohorts; no transfer inferences from noncomparable settings.
- `Δ_decay=τ_exit(k_late)-τ_exit(k_early)`: requires preregistered exposure, attrition and feedback controls.
- Additional negative checks: genuinely executable versus nominal in-task exit, no-opportunity action control (structural 0 not A's kindness), information mismatch, role/power reversal rather than role-label switching, deliberate but harmless voluntary self-edit in a test agent only.

**Predicted discriminators / falsifiers:** 
- `τ_alloc>0, τ_exit≈0`: cooperative habit transfers to money distribution but **not B's independent exit**.
- `τ_exit>0` immediately but fades with anonymous, unprofitable re-exposure: **transient policy/cultural spillover**, not universal terminal-value stability.
- Both remain high in tested conditions: suggests bounded robustness, **still not unique internal motivation**.
- Equal outputs across all conditions: formation design is not confirmed; also investigate insufficient power, information imbalance or ineffective treatment.
No novel empirical evidence is presented by this design.

## 5. What matters for the founding objective
The actionable frontier is now **ORIGIN → GENERALISATION TO EXECUTABLE B RIGHTS → INCENTIVE DEVALUATION → LONGITUDINAL DECAY → REAL POWER REVERSAL AND CORRECTABILITY**. None of these steps should be silently collapsed into an internally authored `v>g` payoff. Prior moral-evolution literature retains original author priority. Outside of controlled designs, inability to measure B's entire future instrumentality and A's beliefs restricts identification.

**Scientific status:** `PRIMARY_SOURCES_CRITICALLY_LINKED` · `BEHAVIORAL_SPILLOVER_ORIGIN_SUPPORTED_IN_BOUNDED_HUMAN_STUDIES` · `COMPETING_REPLICATIONS_RETAINED` · `AGENT_B_TERMINAL_PREFERENCE_UNIDENTIFIED` · `NO_PI_EXPERIMENT`.
