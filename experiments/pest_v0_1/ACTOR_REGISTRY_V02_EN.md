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

Y1 and Y0 do not specify whether an actor is human or AI. Declare actor **kind** independently; do not assume a capability threshold, infer rights from high or low capability, or assign Y1 and Y0 simultaneously without a dated state change. D is now **a C executive, not generic humanity**. The prior D=human role in the PEST-D historical thought experiment is deprecated *only as a general mapping*: its negative controls remain valid as hypothetical individual-party harms after relabeling, not as evidence concerning all D executives.

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
