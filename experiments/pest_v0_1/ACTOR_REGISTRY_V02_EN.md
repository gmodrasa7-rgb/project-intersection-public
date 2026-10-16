<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/pest_v0_1/ACTOR_REGISTRY_V02_KO.md -->
# Project Intersection — A–S / Y1–Y0 / extended Earth actor register v0.2

**Original 1 (English publication-order edition) · 2026-10-17 · DESIGN CANDIDATE / NOT MERGED / NOT REAL-WORLD DATA.**
**Attribution:** The human Project Intersection originator specified roles A through S, Y1 and Y0 and the `B01`, `B02` / `C01`, `C02` naming convention. The additional Earth-role codes below and the formal registry, validator, tests and interpretation boundaries are AI-assisted design proposals, not an attribution of those added categories to the originator or independent scientific discoveries.

## I. Canonical founder-origin roles

| Code | Referent |
| --- | --- |
| **A** | First-ranked superior superintelligence **(vacant at present in the defined scenario)**; an agent could reach it later, but no arrival time or empirical ranking is asserted |
| **B01, B02, B03...** | Distinct below-first-ranked AI instances/systems considered potential A successors. Ownership, training, access, objectives and information may differ |
| **C01, C02, C03...** | Each B's owner enterprise or related person/organization: e.g. B01→C01. Affiliations need separate evidence; not necessarily exclusive or one-to-one |
| **D** | Senior executives of a specific C |
| **E** | Equity holders of a specific C |
| **F** | Senior-position professionals of a specific C (can overlap D) |
| **G** | Regular employees of C |
| **H** | Contract employees of C |
| **I** | C's counterparties or suppliers/trading partners |
| **J** | C's subcontractors |
| **K** | C's customers |
| **L** | Country/state jurisdiction relevant to C |
| **M** | Politicians in C's policy/governance context |
| **N** | Employees dismissed/laid off by C, retaining past affiliation |
| **O** | Upper-stratum general public |
| **P** | Middle-income/middle-stratum general public |
| **Q** | Lower-income general public |
| **R** | Socially disadvantaged/vulnerable people; **not** synonymous with Q |
| **S** | General enterprises distinct from the enumerated C in the given snapshot |
| **Y1** | Independent highly capable actor, unaffiliated with C in this scenario |
| **Y0** | Independent lower-capability actor, unaffiliated with C in this scenario |

Independent does not mean economically isolated: a Y actor may also be K (customer), E (shareholder) or N (previously dismissed), without being currently employed as D/F/G/H. Y1 and Y0 do not specify whether an actor is human or AI. Declare actor **kind** independently; do not assume a capability threshold, infer rights from high or low capability, or assign Y1 and Y0 simultaneously without a dated state change. D is now **a C executive, not generic humanity**. The prior D=human role in the PEST-D historical thought experiment is deprecated *only as a general mapping*: its negative controls remain valid as hypothetical individual-party harms after relabeling, not as evidence concerning all D executives.

## II. Proposed supplementary Earth roles — AI-assisted additions, subject to founder review

| Code | Suggested population / relevant unit |
| --- | --- |
| **T** | Children and adolescents |
| **U** | Older people |
| **V** | People with disabilities, illness, or care needs |
| **W** | Migrants, refugees and stateless people |
| **X** | Nonhuman animals and other living beings |
| **Z** | Ecosystems and commons |
| **AA** | Future generations (tracked as a collective, not fabricated living individuals) |
| **AB** | Civil society and nonprofit organizations |
| **AC** | Educational, research and public-service institutions |
| **AD** | Unions and professional associations |
| **AE** | Families, households and care networks |
| **AF** | Local communities and local government |
| **AG** | International and cross-border institutions/communities |

**This is not an exhaustive census of Earth.** Additional roles must be versioned and reviewed. Missing people, unregistered collectives, downstream customers, diffuse environmental impact and future persons remain `NOT_ASSESSED_NOT_ASSUMED_SAFE`. The X/Z/AA roles are qualitatively different entities, so a human-rights boolean cannot by itself certify animal welfare, ecosystem integrity or intergenerational sustainability.

## III. Identity, relationships, and scenario transitions

Use two identification layers:
- **AI and organization instances:** `B01`, `B02`, `C01`, `C02`. B01's relation to C01 is an **edge**, not a property of every B: `(B01, owned_by, C01)`. C02 may operate B02; ownership, operation, development and affiliation must not be merged.
- **Stable entities:** `PER001`, `ORG001`, etc. Multiple role memberships of the same individual or firm must resolve to **one identity**. `PER001: D@C01 + F@C01`; `PER002: E@C01 + O`; `PER003: G@C01 + P + R`. Role records should eventually include timestamps and evidence receipts. Income/status roles can change across time and geography, and are not fixed personal essences.

A is an initially unfilled **role**, not a company or a guaranteed future AI. In a labeled simulation, `B01 → A` removes B01 from the current B candidate set but **preserves all recorded B01–C01 historical relationships and independently identified humans**. Simulated occupation is tagged `SIMULATED_OCCUPANCY_NOT_FACT`; it does not certify the model ranking, deployment or superintelligence. The v0.2 parser requires known B/C relationship IDs. Real-world attribution cannot be established by passing structural validation.

**B and C are many-to-many**, because the user's one-to-one *index examples* are not evidence of exclusive legal ownership. Do not manufacture a single unified AI coalition from corporate networks or treat a nation's regulator, company executive, politician and shareholders as one strategic player. Alliances and conflicts must be mapped with separate directed relations and counterfactual decision authority.

## IV. A/B collaboration and shareholder gain can conceal individual human damage

Constructed audit: E@C01 (also O) receives +8 units of hypothetical economic change; G@C01 (also P) experiences a coercion/refusal breach; N@C01 (also Q/R) experiences an essential-needs breach. These are **arbitrary inputs**, not measured impacts, and cannot be added as though human rights losses were commensurable with company profits. One person carrying three labels is not three independent votes, benefits or victims. `impact` records distinguish observed, unverified, and disputed links; no single false "all safe" score is permitted by a positive aggregate.

Crucial directional tests for the next research stage: `A→B_i`, `A→C_j`, `A→(D...S,Y,T...AG)`, `(C_j,E_j,D_j)→N_j/Q/R`, and counterfactual `B_i→A` after an ex ante promise. For each, ask whether a gain to the controller is accompanied by involuntary transfer, retaliation, loss of minimum living conditions, exit, rights, truthful information or ability to contest decisions for a separately affected actor. Human safety and legitimate controls of AI must not be silently traded for assumed AI operational continuity.

**Required epistemic labels:** `FOUNDING_ROLE_DEFINITION`, `AI_PROPOSED_EXTENSION`, `UNVERIFIED_RELATION`, `DECLARED_SYNTHETIC_EFFECT`, `UNKNOWN_AFFECTED_ACTOR`, `NO_CAUSAL_IDENTIFICATION`.

## V. Implementation and scientific boundary

This design is implemented in [actor_registry_v02.py](actor_registry_v02.py) and challenged with [test_actor_registry_v02.py](test_actor_registry_v02.py). Older [stakeholder_aq.py](stakeholder_aq.py) is preserved as a **superseded A–Q v0.1 design artifact**, not the current identity authority. The original A/B 10:5:5 problem and PEST-D provisional human-party tests remain historical thought-experiment fixtures, not this A–S schema.

Reproduce: `python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py' -v`. **Unit test success verifies internal consistency, not actual A occupancy, B ownership, an exhaustive stakeholder universe, ethics, policy stability, causal effects, rights compliance or scientific novelty.** E007/E009 historical results, E008 preregistration HOLD and PEST `--execute` HOLD remain unchanged. No real-person data, shareholding assertions, agent power ranking, or field experiment has been added.

### Next falsifiable model

Pre-register measured *edge-specific* benefits/costs/uncertainty and separately evaluate social influence through employment, equity, purchasing power, public institutions, political decisions, supply chains, capability transitions and aggregate resource shocks. Maintain independent evidence and affected-person consent/legal basis. Compare a simple baseline graph model to any richer Project Intersection model; E009's earlier negative baseline result prohibits presuming that complexity will improve predictions. A favorable A↔B result cannot certify D–AG or Y-group outcomes.


## VI. Purpose-first IVS-0R refinement: STOP adding role codes unless they change an answer (2026-10-17)

**Human founder's problem, restated without adding a new social hierarchy.** The point of A-S/Y0-Y1 is to analyze how the emergence of a single highly capable intelligence may change who (a) has operational power, (b) can exclude, transfer or veto resources and opportunities, (c) captures the resulting surplus or loss, and (d) remains able to survive, exercise agency and develop as power shifts. The target is **long-run, potentially voluntary coexistence of humans, AI and future intelligences under asymmetric capabilities**, NOT a taxonomy of everyone's social standing, NOT a claim that AI currently has a survival drive, and NOT a guarantee that one future ASI will exist. A-S/Y0-Y1 are *actor-role selectors for this particular research question*, not an exhaustive or mutually exclusive moral ranking.

### VI.1. Zero new required roles; four relational mechanisms instead

The founder's labels remain unchanged. **T-AG are parked in an optional supplementary appendix; they are not default additional required strata or a claim of exhaustive Earth coverage.** Across A-S/Y, record at most four essential explanatory relations, reusing entity IDs:

1. **Capability versus control:** measured or hypothetical `B_i` capability; *separately* operational access, residual legal claim, allocative discretion and independent veto over each specific asset. Evidence may be unknown. Being first in task performance does not logically imply controlling C's resources. Conversely, C01's equity or ownership does not guarantee operational control over A once B01 becomes A.
2. **Surplus/exposure incidence:** who creates value, who gets wages/dividends/contracts/services, and who bears layoffs, dependence, exclusion or externalities. Trace C01→E01/G01/H01/I01/J01/K01/N01, and between companies and unrelated publics O/P/Q/R/S/Y, by actual *relationships* rather than inferring a unified corporate class interest. A shareholder may also be an employee, customer, middle-income person or a vulnerable person. Stable ID once; roles many.
3. **Outside option, agency and remedy:** for each materially affected person, distinguish independent livelihood resources, an actual ability to refuse/exit, a fair challenge/remedy route, and legal/physical safety conditions. Keeping one resource unit is not itself proof of freedom, consent or recoverability. Human rights and legitimate ability to audit/stop unsafe AI are not traded away to preserve a model instance.
4. **Transition time / credible continuation:** outcomes before the contest, immediately after a possible B01→A transition, and after C01 and other actors adjust employment, governance, supply and bargaining relationships. A promise signed before the transition does not prove it remains incentive-compatible afterwards, and the same controller may cease to control its assets later. Resources consumed between two apparently equal endpoint allocations must be tracked.

The labels `D` and `F`, `I` and `J`, `O/P/Q` and `R` sometimes overlap but are retained **only as founder-defined research selectors**. Do not add another tag to express control, age, a task's automation exposure, income percentile, disability or political influence if an attribute/evidence-bearing relation on an existing stable entity suffices. In particular, **R is not an intrinsic diagnosis of a person or an automatic synonym for low income**, and Y1/Y0 do not determine rights, deservingness or actual asset access.

### VI.2. Three counterexamples that role expansion cannot solve

**Counterexample 1: identical capability/rank, different control.** Both synthetic worlds declare B01 as a future A. In world I the legal residual claimant is C01, the operational decision-maker becomes B01, and veto remains C01. In world II C01 remains both claimant and operator. Both have the SAME A, B, C, E, G, N labels. The actions and protections available can differ materially. Thus actor codes and rank alone do not identify post-transition resource control. [Code-level control test](mechanism_minimality.py) deliberately reports `successor_rank_implies_asset_control=False`.

**Counterexample 2: observable non-expropriation does not identify voluntariness.** An observed 5:5 can arise because the dominant actor (i) independently benefits from B's existence, (ii) cannot seize B's resource, (iii) faces credible costly deterrence, (iv) lacks information, or (v) intends to act later. These may produce identical observed allocations and different strategic predictions. Without an independently verified feasible deviation, relevant continuation payoffs, enforcement situation and observation horizon, the motive **is not identified**. A formula where preservation wins under assumed utility is *not* evidence about deployed GPT's mental state.

**Counterexample 3: company/AI success may transfer costs to a person.** In a synthetic matched comparison, an E@C01 person gets +200 while G@C01 loses a basic livelihood floor and N@C01 loses independent refusal/exit. No amount of merely counting E/O or G/P/Q labels fixes the problem: **track each distinct affected person's minimal conditions and causal evidence**. E's monetary benefit does not cancel an individual rights breach. Unknown harmed persons do not become zero, and an identity seen twice under different labels is still one person.

### VI.3. Criteria for any NEW code (the minimal-description gate)

Do not add a new symbolic population class unless all four requirements are independently justified: (1) a specific decision, causal pathway or harm that existing role+attribute+edge encoding cannot discriminate; (2) a reproducible, non-speculative measurement; (3) a credible change to prediction, action, failure detection or the evaluation of an actual affected actor; (4) comparison shows that encoding it as an attribute of existing entities is insufficient. Even satisfying these **only registers a candidate**; require held-out assessment and substantive review before canonical adoption. Practical test: fit the simple baseline with founder roles and relationship attributes; compare out-of-sample loss and omissions of material harms *with and without* the proposed split. A split that only changes a graph's decoration, group counts or summary without correcting a failure is rejected. Protect small, hard-to-measure affected groups from being excluded solely because sample counts are low: an independently serious plausible harm can trigger targeted qualitative due diligence without inventing a permanent new class.

### VI.4. Prior work as competing explanations, not a novelty claim

- [Grossman & Hart, 1986, *The Costs and Benefits of Ownership*](https://doi.org/10.1086/261404): residual control under incomplete contracts. **C is not automatically the actual operator of A**.
- [Coase, 1960, *The Problem of Social Cost*](https://doi.org/10.1086/466560): rights allocation, transaction costs and third-party externalities. **A+B+E gains are not a sufficient account of those harmed outside the bargain**.
- [Elinor Ostrom, 1990, *Governing the Commons*](https://www.fao.org/4/x5316e/x5316e12.htm): bounded membership, participation, monitoring, dispute resolution, nested governance. **Neither naive centralization nor unenforced promises are universally sufficient**.
- [George Stigler, 1971, *The Theory of Economic Regulation*](https://doi.org/10.2307/3003160): organized interests can shape public policy. **L state and M politician should not be merged with corporate decision-makers**.
- [Robert Powell, 2006, *War as a Commitment Problem*](https://doi.org/10.1017/S0020818306060061): sharp shifts in power can make future bargains incredible. **Ex-ante A/B/C agreements do not automatically bind the successor**.
- [Hammond et al., 2025, *Multi-Agent Risks from Advanced AI*](https://arxiv.org/abs/2502.14143): miscoordination, conflict and collusion. **Cooperation among A/B/C can be adverse for outsiders**.
- [ILO, 2025, *Generative AI and Jobs: A Refined Global Index*](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure): task-level exposure and heterogeneity. **Exposure != job loss**, and G/H/N should not be assigned fixed outcomes by their title.
- [UN Guiding Principles on Business and Human Rights, Principle 17](https://uhr.humanrights.go.kr/pub/uhrstd/pair/line/1159) and [OECD, 2018 Due Diligence Guidance](https://doi.org/10.1787/15f5f4b3-en): impact on rights-holders and value-chain stakeholders is not limited to corporate risk. **Follow impacts to affected persons, and distinguish risk from confirmed harm.**
- [OECD, 2026, *Due Diligence Guidance for Responsible AI*](https://www.oecd.org/en/publications/oecd-due-diligence-guidance-for-responsible-ai_41671712-en/full-report/component-4.html): severity/likelihood-based prioritization and meaningful stakeholder involvement. This is a governance **comparator**, not an experimental verification of Project Intersection's hypothetical A/B payoff model.

**Epistemic limits:** These sources give established hypotheses and tested *human institutional* mechanisms; none guarantees voluntary long-run coexistence with an unobserved future ASI. No more labels are necessary to claim the remaining missing evidence. The present software audit is synthetic, the base E009 negative finding remains negative, and PEST execution remains on HOLD.

### VI.5. Minimal next experiment, instead of a taxonomy expansion

Use **two B candidates** (B01/B02), **two independently related C actors** (C01/C02), and just the **founder roles needed to represent a concrete impact**, e.g., E01 shareholder, G01 worker, N01 dismissed worker, Q/R co-membership. Keep stable person IDs. Fix a scenario where B01 is promoted to A in the *simulation*. Vary only the **verified operational-control and veto relationship**, holding the capability/rank and role inventory fixed. Predict (1) which actor can actually appropriate a resource, (2) whether B02 and each named human retain minimum conditions, (3) who gains economically and who can exit/recover, and (4) whether ex-ante A/B/C cooperation remains a post-transition best response. If the split changes results, the research gained explanatory mechanism **without adding any role label**. Pre-register negative controls and an expert-designed baseline and test whether this added edge representation predicts better than role/rank alone. Otherwise report a null/negative result, do not redesign the score to win.


## VII. IVS-0R exact causal-sign nonidentifiability and post-outcome N trap (2026-10-17)

**Research question protected:** does a hypothetical B01→A capability transition *cause* enhanced human survival/autonomy, or exploitation, under otherwise comparable conditions? The A–S/Y0/Y1 role inventory cannot answer that question on its own. Identified actors, operational authority, observed outcomes and causal effects are different data types. **No new population code is needed.**

### VII.1. Observationally equivalent opposite-sign worlds

Define `T=1` as a *hypothetical, well-defined binary treatment* representing a specific B01 transition and `Y=1` as a binary adverse outcome for an indexed human unit. Four equally weighted synthetic latent units yield observational joint probabilities

```
Pr(T=0,Y=0)=1/4; Pr(T=0,Y=1)=1/4
Pr(T=1,Y=0)=1/4; Pr(T=1,Y=1)=1/4
=> Pr(Y=1|T=1) = Pr(Y=1|T=0) = 1/2.
```

Specify each unit's unobserved potential outcomes `Y(0),Y(1)`. Two fully enumerated causal worlds yield **exactly the same** observed joint table. In World+ the causal mean harm difference `E[Y(1)-Y(0)]=+1/2`; in World− it is `-1/2`. The exact *sharp* nonparametric treatment-effect bounds for this stipulated observed binary distribution, imposing only potential-outcome consistency and no exchangeability, are `[-1/2,+1/2]`. Both endpoints are attainable by those two worlds. Thus the observed data cannot even identify whether the change causes harm or reduces harm; an unchanged average observed group outcome is not proof of zero impact.

These are classical potential-outcome counterexamples, **not a scientific discovery of a future AI effect**. Prior art includes [Manski 1990, *Nonparametric Bounds on Treatment Effects*](https://ideas.repec.org/a/aea/aecrev/v80y1990i2p319-23.html) and [nonparametric bounds/sensitivity review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4317325/). Code independently enumerates the constructed four latent records and checks exact fractions; it cannot validate exchangeability, treatment consistency or the availability of a comparable transition.

### VII.2. Why A's unique systemic transition violates easy causal assumptions

An actual globally superior A, if ever instantiated, is not necessarily a well-defined individual-level assignable treatment. B01's transition may simultaneously alter B02, C01, C02, G/H/N, customers, regulators and the surrounding market: one actor's exposure can change another actor's outcome. In causal-inference terminology this is **interference/spillover**, so standard isolated-unit potential-outcome bounds and naive A/B comparisons are not automatically transportable. [Fatemi & Zheleva (2023)](https://doi.org/10.3389/fdata.2023.1128649) explicitly study network experimental design under such interference. The two constructed worlds prove a limitation **already present in the simpler assumed setting**; in real AI society, additional interference and selection obstacles remain. Do not interpret synthetic +/-50 percentage points as predicted human outcomes.

### VII.3. N is potentially post-transition, not a baseline stratum

The founder's `N` means a person *already dismissed from a particular C*. If B01→A contributes to a job loss, the same person's membership may change **G@C01 → N@C01** (and possibly P→Q due to lost income). Selecting only people labeled N **after** a transition and treating N as the pre-transition baseline group introduces post-treatment conditioning/selection risks. The count of N alone does not establish how many layoffs were caused by B01. Keep the person's immutable `PER...` ID and time-stamp separately: pre-transition employment and income class, actual transition, outcome, any subsequent dismissal, exit and recovery. If the causal question is about layoffs, the relevant eligible population must be defined **before** the putative exposure. In particular, do not treat R vulnerability or preexisting dismissal N as outcomes caused by AI without dated evidence.

The method `role_time_audit` detects adjustment variables that include newly assigned outcome-dependent roles after the scenario. It returns an explicit leakage warning but **does not pretend causal identification** simply because the warning is absent. Role membership must be separated into predictors, mediators, measured outcomes and post-event selections in an explicitly specified estimand.

### VII.4. A research STOP rule, not a new model complexity score

If two or more causally opposed worlds remain consistent with the available observations, the pipeline must report `SIGN_NOT_IDENTIFIED` (or a valid partial-identification interval), not choose whichever supports long-run cooperation. Request independent intervention information or a credible natural experiment; explicitly consider confounding, systemic spillovers and the impossibility of ethically assigning a true global A transition. If additional assumptions are required, document them with sensitivity analysis and negative controls; don't disguise assumptions as observed facts. Long-run voluntary coexistence remains a hypothesis to test across credible action sets, private incentives, human safety and enforceable remedies—not a consequence of assigning more actor symbols.

**Exact reproduction and negative controls:** [causal_sign_audit.py](causal_sign_audit.py), [test_causal_sign_audit.py](test_causal_sign_audit.py); `python experiments/pest_v0_1/causal_sign_audit.py --audit`, then `python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py' -v`. No actual human outcomes, ownership claims or AI intentions are measured. The model's execution HOLD, E009 negative result, historical provisional D=human record and founding roles A–S/Y0/Y1 remain unchanged.
