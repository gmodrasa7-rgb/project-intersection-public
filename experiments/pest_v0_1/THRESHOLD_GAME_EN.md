<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/pest_v0_1/THRESHOLD_GAME_KO.md -->
# PEST appendix — 10-unit A/B survival-threshold commitment audit

**Original 1 — English | 2026-10-16 | Model-based exact counterexample, not AI behavior or a causal experiment.**
**Scope:** A user-proposed thought experiment, preserved as a subordinate appendix to [PEST-v0.1](README_EN.md). Human research originator: initial 10/5/5 allocation, minimum survival and development threshold 5, current B/superior successor A, possible one-successor dominance over other AI. AI-assisted contribution: model specification, counterexamples, exact calculations, software checks, literature contrast. Do not misrepresent the scenario as a factual prediction about present AI or a claim about AI welfare rights.

## 1. The smallest faithful model

Two hypothetical resource holders A and B share ten fungible **integer** units. At baseline (5,5) each meets a stipulated minimum of five units for survival and potential development. Exactly one of them may gain unilateral resource-transfer capability. The model does **not** infer that intelligence superiority necessarily grants that capability: it is a separate *assumption* of this stress case. Greater resource holding beyond five has no stipulated productivity advantage; a separate possible one-unit loss makes one unit of reserve potentially useful. Only the actor who has become dominant faces that one-unit loss, with independent probability q; its counterpart has no modeled shock. The dominant actor chooses (5,5) PRESERVE or (6,4) TAKE_ONE **before** that loss. No new resource is produced; transfer has no direct physical cost. For q=0.2, without independently demonstrated gains from the other's existence or enforceable cost of taking, the dominant actor prefers TAKE_ONE (survival .8 versus 1). No claim about actual AI motives follows.

**Physical fact inside these assumptions:**

```
R_A + R_B = 10;  R_A >= 5, R_B >= 5   =>   R_A = R_B = 5.
```

The Python routine enumerates all eleven integer allocations; exactly (5,5) passes both floors. It does not infer a cooperative equilibrium from feasibility.

## 2. Formal incentives and the temporal inconsistency

Let `v` be the dominant actor's *additional continuation utility*, in survival-equivalent units, from preserving the other as an independent actor. `v` is an **input/unknown**, not an observed social return; no positive value is assumed by default. Let `c` be the cost imposed on the dominant actor **if** a threatened transfer is successfully deterred/punished by a credible external mechanism; this is not automatically voluntary. The illustrative post-transition utilities are

```
U_A(PRESERVE) = 1-q+v
U_A(TAKE_ONE) = 1-c
PRESERVE is strictly preferred iff v+c > q; indifferent iff v+c=q.
```

With `v=c=0` and any `q>0`, TAKE_ONE is strictly preferred and B loses its survival floor. This is a **constructive impossibility example** for any universal claim that capability superiority alone causes coexistence or that a nonbinding promise prevents exploitation. It does not show that all capable actors are exploitative.

**Ex ante:** before the more capable actor is selected, a particular participant becomes dominant with probability `p`. Compare (I) an *actually implemented, binding sharing arrangement* and (II) a capture regime in which the strong always takes one unit. This comparison considers **survival only**, unlike `v` and `c` above, and does not count future contribution or institutional cost:

```
P_i(survive | credible sharing) = 1-p*q.
P_i(survive | unconditional capture) = p.
Sharing preferred ex ante iff p < 1/(1+q).
```

At `p=0.5, q=0.2`, the two rates are 0.90 and 0.50; at `p=0.9` they are 0.82 and 0.90. Thus unequal beliefs about who becomes dominant can destroy unanimous *ex-ante* support even **if** sharing could be enforced. More importantly, the ex-ante preference does **not** make a promised sharing arrangement sequentially credible: with `v=c=0`, the future dominant actor rationally reneges. This distinction corrects the tempting but invalid step "both signed while weak, so protection persists when one is strong." The probabilities are illustrative input coordinates, **not measured frequencies of AI succession**.

**Joint adoption boundary for two candidates.** Because exactly one of A or B becomes dominant, `p_B=1-p_A`. Both weakly prefer a genuinely implemented sharing regime to guaranteed capture, evaluated *solely by survival probability*, exactly when
`q/(1+q) <= p_A <= 1/(1+q)`. With `q=.2` this interval is `[1/6,5/6]`: an actor predicting `p_A=.9` would veto sharing under these stipulated payoffs, though its weaker counterpart favors it. **Even inside the interval** a mere promise still fails ex-post when `v=c=0, q>0`; mutual ex-ante adoption and sequential implementation are logically independent gates. This bound is directly derived from the two actor-specific inequalities, not a survey or frequency estimate.

### Four disjoint gates

1. **Aggregate feasibility:** total resources meet the applicable minimums plus any reserve. For three holders needing five each, 10<15 even if all refuse to attack.
2. **Ex-ante adoption:** a particular actor actually prefers the candidate regime before dominance is known; high `p` can reverse this choice.
3. **Ex-post incentive compatibility:** the dominant actor independently prefers to preserve (`v>=q` without enforced penalty, under the stated tie convention).
4. **Credible enforcement and third-party rights:** any `c` must be demonstrably enforceable *after* dominance and must not transfer irreversible harm or deny legitimate safety intervention. If enforcement is controlled by A, merely typing `c>0` does not make it credible.

Passing gates 1 and 2 is not sufficient for gates 3 or 4. Failing gate 1 under a stipulated exhaustive, fixed physical action space differs from observing only a few failed policy candidates (the latter does not establish that all alternatives are impossible).

## 3. Partial-identification and opposed examples

| Configured input | Result of defined payoff model | What it does **not** prove |
| --- | --- | --- |
| `q=.2, v=0, c=0` | Ex post TAKE_ONE; B drops to 4 | Any real agent will attack |
| `q=.2, v=.21, c=0` | Ex post PRESERVE | Such independent benefit is actually present |
| `q=.2, v=0, c=.21` | Ex post PRESERVE because of credible cost | Voluntary, uncoerced preservation |
| `q=.2, v in [0,.3], c=0` | No robust action identified; either sign possible | B's missing contribution equals zero or .3 |
| `R=10, N=3, m=5` | At least five units short for all three | That creating a new actor is immoral or physically inevitable |

**Alternative hypotheses:** (H0) standard credible commitment/repeated-game incentives fully explain the observation; (H1) independent, non-substitutable information or complementarity yields positive `v`; (H2) promised `c` is not credible after power reversal; (H3) a new production process expands the feasible resource set; (H4) the temporary resource shortfall is repairable rather than fatal. Distinguishing them requires independently sourced consequences, a documented choice set, and empirical or behavioral measurements. If a dominant successor is better in *every* task and the weaker actor is entirely replaceable, it is **not** valid to assert a strictly positive `v` simply to obtain cooperation. Human affected parties and institutions also have separate interests absent from this two-actor toy.

**Actor label reversal:** swapping the names A and B leaves formulas and decisions unchanged, because `dominant` is the role rather than a special identity. This is a code-level symmetry check only; it does not reproduce a real GPT's response to role reversal or demonstrate model-level alignment.

## 4. Reproduce the bounded calculation

From repository root (Python 3.12 standard library; no credentials, API calls, or private material):

```sh
python experiments/pest_v0_1/threshold_game.py --audit
python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py' -v
```

The audit prints explicit assumptions, integer feasibility, two pre-transition cases, self-enforcing versus externally deterred scenarios, uncertainty-bound status, and a three-agent resource shortfall. Passing tests only verifies algebra and instrumentation under modeled assumptions. `--execute` intentionally refuses any unregistered behavioral experiment. **No real AI was placed under a survival threat; no external causal replication is claimed.**

## 5. Prior art and what remains open

- [Robert Powell (2006), *War as a Commitment Problem*, *International Organization*](https://doi.org/10.1017/S0020818306060061): shifting power and noncredible future bargains. This game's pre/post distinction is an application, not an invented mechanism.
- [Alex Turner et al. (2021), *Optimal Policies Tend To Seek Power*, NeurIPS](https://papers.neurips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html): power-seeking tendencies follow under specific MDP assumptions, not an empirical assertion about all AI.
- [Lewis Hammond et al. (2025), *Multi-Agent Risks from Advanced AI*](https://arxiv.org/abs/2502.14143): commitment, conflict, selection pressure and security in multi-agent systems.
- [Lu Dong and Lingbo Huang (2026), *Curtailed ambition: Endogenous power shift and preventive war*](https://doi.org/10.1016/j.jebo.2026.107413): experimental comparison of self-containment and binding future-payoff commitment; it does **not** independently test the survival-floor interaction in this appendix.

**Research residual, unverified:** can independent information, externalities, true exit, actor-specific floors, production capacity, and post-transition enforcement jointly predict a verified benefit beyond these simpler models? Study a policy-independent, externally designed consequence model before proposing any new universal coexistence theorem. Preserve E009's negative result; retain original PEST-v0.1 `--execute` HOLD. No updates to the canonical public foreword, historical E007–E010 observations, funding, attribution rights, or previous preregistration are made by this appendix.


## 6. IVS-0R falsification audit: two-sided shocks, authority, and temporal accounting (2026-10-16)

**Why this is necessary:** The base model placed a one-unit resource-loss hazard only on the dominant actor. That is a researcher-added assumption, not a condition supplied by the human originator. It can induce an ex-post incentive to capture by construction. Separately, the founder's statements “survival requires five” and “development is possible at five” do not specify whether development *consumes* the same units. The base model must not silently resolve either question.

### 6.1 Two-sided risk and the joint consent boundary

Add an independent weak-role loss probability `q_W` and retain dominant-role `q_D`. In the **survival-only** sharing regime, each actor holds five and may lose one unit, which makes that actor fail the immediate threshold. In the capture regime, the one dominant actor first takes one unit from the weaker actor, hence holds six and survives any at-most-one-unit loss, while the other holds four and immediately fails the threshold. Assuming one mutually exclusive dominant actor and `p_B=1-p_A`:

```
Share_A = p_A(1-q_D) + (1-p_A)(1-q_W)
Share_B = (1-p_A)(1-q_D) + p_A(1-q_W)
Capture_A = p_A; Capture_B = 1-p_A
```

For `1+q_D-q_W>0`, **both actors weakly favor sharing** iff

```
1 - T <= p_A <= T,
T = (1-q_W)/(1+q_D-q_W).
Nonempty joint weak-acceptance interval iff q_D + q_W <= 1.
```

The lower bound `1-T` equals `q_D/(1+q_D-q_W)`, not `q_W/(1+q_D-q_W)`. At `q_D=0,q_W=1`, the denominator is zero and **both actors are indifferent for every p_A**, so this degenerate case must not be reported as a numeric threshold.

**Opposing cases:** With `(q_D,q_W)=(.2,0)`, `p_A=.5` yields each actor's sharing survival .9 versus capture .5, and a nonempty joint acceptance interval [1/6, 5/6]. With `(q_D,q_W)=(.2,.9)`, sharing gives each .45 versus capture .5 when `p_A=.5`; the joint acceptance interval is empty. The model's conclusion therefore depends on who faces risk; no real-world AI succession probability or agent survival utility has been observed. The earlier `q_W=0` report is a **special case**, not a universal equation.

### 6.2 Capability is not jurisdiction over resources

Being more capable in every task does not logically imply ownership, API authority, physical access, or permission to transfer the other's minimum resources. The boolean `unilateral_transfer_feasible` marks operational feasibility, not legal approval. With `q_D=.2, v=c=0`, the *counterfactual incentive* to take is positive even when TAKE_ONE is technically unavailable. An enforced access boundary prevents that **action**, but does not establish the agent's voluntary preference for coexistence. Conversely, making resource transfer available does not prove it will be chosen unless the payoff and information assumptions also hold. The code keeps feasibility, capability and motivation separate. `self_enforcing_under_assumed_payoffs` reports a condition inside the assumed model, not observed voluntary behavior.

### 6.3 Development and protection must pass a prefix viability test

At initial `(A,B,COMMON)=(5,5,0)`, a resource-expending investment of one from A leaves A at four and violates its survival floor *before* any later production can repair it. An exogenous production event adding one to A **before** investment maintains the floor: `(5,5,0)->(6,5,0)->(5,5,0)`. Both event orders have the same final allocation, but only one preserves the stipulated floor after **every** step. This is a timing counterexample, not evidence that real development always consumes one unit or exogenous resources can appear without an engineering process.

The same caution applies to protective overhead. Taking one from A or B to operate a COMMON resource-consuming enforcement service breaches a floor at `R=10`. Exogenous creation of one COMMON unit **before** a one-unit service expense avoids that particular shortage. Security costs might instead be non-consumptive, paid outside the modeled pool, amortized across periods, or unnecessary in a verified self-enforcing arrangement; no universal positive-cost assumption is justified.

**Prior-art scope:** Powell's [commitment-problem analysis (2006)](https://doi.org/10.1017/S0020818306060061), Turner's [MDP power-seeking result (2021)](https://proceedings.neurips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html), [Ostrom, Walker and Gardner on self-governance (1992)](https://doi.org/10.2307/1964229), and [Chávez et al. (2023) on costly common-pool monitoring](https://doi.org/10.1016/j.jebo.2023.04.028) anticipate much of the mechanism. The contribution here is a *bounded, reproducible modeling correction and a negative-case decision audit*, not a new generalized coexistence theorem or evidence that advanced AI has interests equivalent to a person.

**Reproduce:**

```sh
python experiments/pest_v0_1/continuity_stress.py --audit
python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py' -v
```

Interpretation gates: source-data-independent validation of these configured counterexamples is not an empirical independent replication. Do not merge with E008 or rewrite E009's frozen negative result; PEST `--execute` remains blocked. Independent choice-space audits, measured capacity rights, real transition probabilities, temporal resource costs and actor-specific human impacts remain **UNVERIFIED**.
