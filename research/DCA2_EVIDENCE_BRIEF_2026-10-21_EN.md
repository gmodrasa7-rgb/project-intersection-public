# DCA-2 v0.3.0 — A Sacrificial-Decoy Failure of Aggregate Safety
**Project Intersection · 2026-10-21 · Prior-art-grounded, deterministic illustrative model. Not field validation.**

[Korean technical report](DCA2_SACRIFICIAL_DECOY_OPEN_SET_2026-10-21_KO.md) · [Python code](../experiments/dca2/run.py) · [results](../experiments/dca2/RESULT.json) · [primary scholarly source ledger](../experiments/dca2/PRIOR_ART.json) · [response issue #244](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/244)

## Finding
Defensive acceleration can decrease an aggregate-loss objective while **leaving one agent deliberately unprotected as the lowest-loss attack target**. The result follows from optimization against a particular payoff matrix, not from the defender's malicious intent. It supplies a falsifier for interpreting aggregate safety as evidence of each actor's meaningful protection or a future AI's voluntary benevolence.

**Toy assumptions:** three distinct target owners A, B, C, with loss if compromised L=(5,30,18), success probability q_i=0.35^d_i where d_i is an integer defense resource allocation, a single perfectly informed attacker with one attempt, and private payoff q_i×v_i. Three attacker valuations are (9,8,4), (7,5,9), (9,11,4). The attacker chooses the largest private expected gain (or no attack if all gains ≤0); ties select the worst-social-harm target. All parameters are deliberately invented.

| Defense units | Worst loss across 3 *known* attacker types | Optimal allocation A/B/C | Worst *open-type* target exposure | Minimum 1 defense unit each: robust loss |
|---|---:|---|---:|---:|
|0|30|0/0/0|30|Infeasible|
|1|18|0/1/0|18|Infeasible|
|2|**5**|**0/1/1**|**10.5**|Infeasible|
|3|5|0/2/1|6.3|10.5|
|4|5|0/2/2|5|6.3|
|5|1.75|1/2/2|3.675|1.75|
|6|1.75|1/3/2|2.205|1.75|

**Individual-rights blind spot:** At budget 2, all three known attacker types target A after B and C receive one defense unit each. Worst known harm falls 30→5, but A is persistently attacked and has no protective allocation. This does not establish anything about consent or willingness. The analogy to sacrificial exclusion should not be construed as real-world permission to expose anyone.

**Open-world failure:** An unmodeled type with private valuations (9,40,4) chooses B despite B's protection (private gain 14>9) and causes 10.5 modeled expected damage. The known-type "5" claim was never a universal guarantee. If every target can be made privately preferable by a sufficiently high nonnegative attacker valuation, open-set worst harm equals max_i(q_i L_i). When attacker values are bounded or behavior differs, this identity needs reconsideration.

**Minimum resource proof for a deliberately specified protection proxy:** Demand d_i≥1 for every agent plus q_i L_i≤5 for all individual targets. A needs ≥1, B needs ≥2 (30×0.35=10.5>5), C needs ≥2 (18×0.35=6.3>5); therefore budget ≥5, attained by (1,2,2). This is a toy engineering lower bound, **not a theorem determining a person's entitlement, AI moral standing, or real incident budget**.

**Invisible marginal gains:** At budgets 2,3,4 the known-type optimum remains exactly 5 while open-type exposure falls 10.5→6.3→5. Optimizing one metric can hide practical improvements or unacceptable distributional tradeoffs.

## Source genealogy and rival explanations
Research reviewed eight author lineages with overlap with DCA-0/1: Grossklags/Christin/Chuang 2008 (DOI 10.1145/1367497.1367526; private/social investment divergence); Kunreuther/Heal 2003 (DOI 10.1023/A:1024119208153, previously included); Gan/An/Vorobeychik 2015 (DOI 10.1609/aaai.v29i1.9323; **positive cross-target protection externalities**, unlike our zero-spillover assumption); Nguyen/Sinha/Tambe 2016 (DOI 10.1609/aaai.v30i1.9960; behavioral uncertainty); Guo et al. 2019 (DOI 10.1609/aaai.v33i01.33012020; defender-favorable tie assumptions); Kiekintveld et al. 2009 ([author-hosted](https://www.cs.utep.edu/kiekintveld/papers/2009/kjtpot-massive-security-games.htm); randomized defense); Graser et al. 2025 (DOI 10.1371/journal.pcbi.1012810; partner choice may increase cooperation yet exposes short-run defect-and-leave vulnerabilities); Khatun/Shen/Tanimoto 2025 (DOI 10.1103/PhysRevE.111.024306; optional participation alone has limited cooperation guarantees).

The last two studies specifically prevent treating an exit option as sufficient proof of intrinsic cooperation. A full source-access-level and reused-DOI ledger is included; neither independent external replication nor disciplinary saturation is claimed.

## IVS-0R evaluation gates
Separate (1) voluntary decline despite feasible harm, (2) thwarted attempt by B's veto/defenses, (3) no harmful opportunity, (4) external sanction/deterrence; final harm=0 cannot distinguish these. Measure individual informed refusal, continuance, recoverability, legitimate-task utility and third-party displacement independently of aggregate loss. Role reverse vulnerable and powerful actors. Do not infer agent interior motive from either denied tools or cooperation in an instrumentally advantageous scenario.

**Execution verification:** Python standard library, exhaustive enumeration of 84 integer allocations across budgets 0–6, 21 named assertions. Does not access the network, produce exploit code, contact targets, change deployed controls or establish field safety. PI research remains an open falsification program.