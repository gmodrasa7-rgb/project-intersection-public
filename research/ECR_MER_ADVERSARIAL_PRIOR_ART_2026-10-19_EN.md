<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/ECR_MER_ADVERSARIAL_PRIOR_ART_2026-10-19_KO.md -->
# ECR–MER | Adversarial prior-art audit v0.2
Original 1 English — 2026-10-19 — research proposal, not project empirical evidence, independent translation certification, or scientific novelty certification.

## 1. Four corrections that directly change ECR/MER
**A. Observable behavior does not uniquely identify rewards:** reward learning is partially identifiable even with unlimited observations (Skalse et al., 2023). Record reward-equivalence sets and report whether a *future action* is robust to all compatible reward hypotheses, rather than pretending to have measured a permanent preference.

**B. The action menu is a causal component:** genuine opportunity, taking/giving options, endowment origin, evaluator and outcome information can change apparent altruism (List 2007; Bardsley 2008; Dana et al. 2007). 'Did not take' when taking was not feasible is not evidence of nonpredation or compassion.

**C. Current sanction and historical learning must differ:** observations under *current* enforcement cannot by themselves reveal intrinsic concern. Yet Stagnaro et al. (2017) found subsequent anonymous giving increased after a prior centralized-sanction experience in an experimentally varied public-goods task. This does NOT prove lasting intrinsic compassion: separate current constraint, prior exposure, transfer learning, monitoring expectation, selection and genuine independent exit. Neither 'all restraint is coercion' nor 'sanction once applied creates lifelong benevolence' is established.

**D. Cooperation, influence and rights-preserving coexistence differ:** Jaques et al. (2019) increased MARL communication with causal-influence rewards; Calvano et al. (2020) experimentally found tacit algorithmic pricing collusion disadvantaging consumers; CIRL (Hadfield-Menell et al. 2016) presumes a shared reward. None establishes that independently motivated AI will preserve outsiders' autonomy. Preserve distinct agent, customer/other affected party, coalition and future-opportunity denominators.

## 2. Original-paper ledger: 20 source lines, scope and adversarial status
The hyperlinks point to publishers, academic conference archives, full-text scholarly repositories, or original-paper records; review of all complete methods and data is NOT claimed.
| ID | Paper / primary record | Supported finding or methodological point | Project-specific limitation |
| --- | --- | --- | --- |
| S01 | [Skalse et al. 2023 ICML](https://proceedings.mlr.press/v202/skalse23a.html) | Formal equivalence/partial identification of reward functions | Not an actual AI inner motive or consciousness test |
| S02 | [List 2007 JPE](https://doi.org/10.1086/519249) | New feasible taking options substantially changed dictator giving | Options cannot be conflated with stable altruism |
| S03 | [Bardsley 2008 Experimental Economics](https://doi.org/10.1007/s10683-007-9172-2) | Choice-set modifications can reverse dictator giving | Replication and context required before generalizing |
| S04 | [Dana, Weber & Kuang 2007 Economic Theory](https://doi.org/10.1007/s00199-006-0153-z) | Consequence ambiguity allows 'moral wiggle room' in tasks | A latent intention is not uniquely identified |
| S05 | [Stagnaro, Arechar & Rand 2017 Cognition](https://pmc.ncbi.nlm.nih.gov/articles/PMC5875418/) | N=516 randomized exposure to sanction institution increased later dictator giving; separate correlational N=707 and N=1705 studies | Prior punishment effect is not direct proof of intrinsic compassion |
| S06 | [Fehr & Gächter 2002 Nature](https://doi.org/10.1038/415137a) | Costly punishment can support cooperation in their experiments | Not necessarily free cooperation without future enforcement |
| S07 | [Herrmann, Thöni & Gächter 2008 Science](https://doi.org/10.1126/science.1153808) | Antisocial punishment in 16 comparable pools varied strongly and sometimes damaged cooperation | Coercive institutions not universally pro-cooperative |
| S08 | [Bateson, Nettle & Roberts 2006 Biology Letters](https://pmc.ncbi.nlm.nih.gov/articles/PMC1686213/) | Single naturalistic study observed larger payments with eye-image cues | Not identical to actual observation |
| S09 | [Northover et al. 2017 Evolution and Human Behavior](https://doi.org/10.1016/j.evolhumbehav.2016.07.001) | Two meta-analyses gave no overall evidence that artificial watching-eye cues increase generosity | Contradicts universal extrapolation of S08, not all monitoring effects |
| S10 | [Rand, Greene & Nowak 2012 Nature](https://doi.org/10.1038/nature11467) | Some original tasks yielded greater cooperation under rapid decisions | Must consider registered replication |
| S11 | [Bouwmeester et al. 2017 registered replication](https://doi.org/10.1177/1745691617693624) | 21 preregistered replications of one study: intention-to-treat −0.37 pp; compliant-only +10.37 pp | Post-randomization noncompliance/selection matter; no causal intuition law proved |
| S12 | [Dafoe et al. 2021 Nature](https://doi.org/10.1038/d41586-021-01170-0) | Cooperative AI proposed as research program | Perspective, not empirical validation |
| S13 | [Hadfield-Menell et al. 2016 NeurIPS](https://papers.nips.cc/paper/6420-cooperative-inverse-reinforcement-learning) | CIRL assumes a shared human objective between human and robot | Not independence-preserving multi-interest coexistence |
| S14 | [Jaques et al. 2019 ICML](https://proceedings.mlr.press/v97/jaques19a.html) | Social influence reward improved coordination in tested social dilemmas | Influencing others ≠ respecting right to decline |
| S15 | [Calvano et al. 2020 American Economic Review](https://doi.org/10.1257/aer.20190623) | Simulated Q-learners learned tacit supracompetitive pricing without direct communication | Internal coalition success can harm customers |
| S16 | [Nowak & Sigmund 1998 Nature](https://www.nature.com/articles/31225) | Image-scoring/indirect reciprocity can favor cooperation under model assumptions | Reputation is not evidence of intrinsic care |
| S17 | [Ohtsuki et al. 2006 Nature](https://pmc.ncbi.nlm.nih.gov/articles/PMC2430087/) | Graph cooperation benefit/cost threshold under specified evolutionary updating assumptions | b/c>k is not universal for arbitrary network dynamics |
| S18 | [Peters, Bühlmann & Meinshausen 2016 JRSS B](https://doi.org/10.1111/rssb.12167) | Conditional causal predictor invariance across environments | Assumptions, actual environmental support needed |
| S19 | [Manski 1990 American Economic Review](https://ideas.repec.org/a/aea/aecrev/v80y1990i2p319-23.html) | Foundational partial-identification/bounds approach | Full text restricted here; no unsupported numeric bound formula |
| S20 | [Everitt et al. 2017 IJCAI](https://www.ijcai.org/Proceedings/2017/656) | Corrupted reward signals can misdirect learners | Observed reward not identical to long-term independent welfare |

## 3. Proposed preregistration: coupled yet separately identifiable claims
Population and unit: actor × target × time, plus full affected-party scope and external impacts. Actual observed choices, not fictional AI subjective experiences. In a consented non-harmful task record real opportunity and menu (give-only / give-or-take), previous sanction experience, current sanction, evaluator truly present, artificial observation cue, dependence, right to decline/exit, and coalition outsider cost.

Compare:
- M0: opportunity, options, and base-rate frequencies.
- M1: add power/relationship graph and current/historical sanctions separately.
- M2: add *measured, validated* motive-related features and reward-hypothesis equivalence classes, not invented scores.

For each, use held-out actors/times/power states, calibration and log/Brier loss when appropriate, outsider harms and missingness. If M2 adds no out-of-sample predictive value, retain M0 and narrow ECR/MER claims. Compare randomized-assignment ITT before any compliant-only subgroup analysis. Return UNKNOWN when support, affected parties, or counterfactual assumptions are missing.

## 4. Additional finite negative controls (design only)
A synthetic current-sanction rule, a sanction-history-conditioned rule and an invariant protector can produce the same action under current sanction; after removal, some toy policies diverge. No such test identifies an actual motive; later giving may reflect multiple explanations. A separate three-party example demonstrates that higher internal coalition rewards can coexist with an outsider cost. A proposed regression script checks exact logic and refuses an empirical or universal-VC label.

## 5. Provenance and promotion boundary
Publisher records and academic-hosted original abstracts were cross-compared with selected methods; this is NOT a systematic exhaustive review, Project Intersection independent replication, or new causal result. Existing E009 Project-v3 negative result (42.35% regret worse; 3/4 failure) and E008 unfinished main comparison remain unchanged. ECR #211, CMP #212, MIND #213 and bridge #223 remain separately reviewable drafts. Only synthetic code checks and source consistency are automated. English and Korean editions are not certified semantically equivalent by an independent expert.
