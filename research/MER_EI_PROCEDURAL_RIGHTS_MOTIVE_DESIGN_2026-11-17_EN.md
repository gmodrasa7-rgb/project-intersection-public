# MER/EI — A preregistration-ready design to separate outcome utility, decision rights, image and feasible exit
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/MER_EI_PROCEDURAL_RIGHTS_MOTIVE_DESIGN_2026-11-17_KO.md -->
**2026-11-17 | Prior-art-grounded design specification and synthetic integrity checks only | No participant data, no experiment, no RVD hypothesis or version promotion.**

## Executive finding
Observing A protect B does not identify why A did so. A may value B's welfare, B's decision rights, a reputation, self-image, a norm, or future instrumental benefits. These mechanisms can coexist. A stronger design must manipulate **outcome distribution, actual decision rights, observability and B's feasible exit** separately.

The proposed protocol can identify behavioral evidence of a preference for procedures/rights beyond measured outcome distributions, and estimate sensitivity to observability. It cannot read an intrinsic motive or eliminate internalized norms and self-signaling.

## 1. Original-author prior art — not a novelty claim
| Lineage | Contribution | Limitation for MER/EI |
|---|---|---|
| Hoffman, McCabe, Shachat & Smith (1994), *Preferences, Property Rights and Anonymity in Bargaining Games*, DOI 10.1006/game.1994.1056 | Double-blind anonymity and property/first-mover rights affect allocations | Anonymous behavior is not automatically pure altruism |
| Dana, Cain & Dawes (2006), *What You Don't Know Won't Hurt Me*, DOI 10.1016/j.obhdp.2005.10.001 | Costly exit changes what the recipient can know/expect | Prosocial behavior can respond to beliefs and psychological payoffs, not recipient welfare alone |
| Chlaß, Güth & Miettinen (2019), *Purely Procedural Preferences*, DOI 10.1016/j.ejpoleco.2019.02.005 | Choices between procedures designed for equivalent outcomes can reveal procedural/rights preferences | A procedural preference does not establish durable preservation of original B |
| Chlaß & Moffatt (2017/2021 working-paper versions) | Argues for preferences over decision-right rules under strict anonymity | Working paper, not equivalent to peer-reviewed replication |
| Regner (2021), *What's Behind Image?*, DOI 10.3389/fpsyg.2021.614575 | Varies excuse/self-image and observability/social-image; guilt and shame relate differently to giving | Image effects are not a complete motive decomposition |
| Tonin & Vlassopoulos (2013), *Experimental evidence of self-image concerns for giving*, DOI 10.1016/j.jebo.2013.03.011 | Ex-post opt-out and anonymous giving used to study self-image | Opt-out combines self-signaling and changed certainty/costs |

## 2. Five constructs, not one
1. **Outcome preference:** A values B's final welfare, resources or safety.
2. **Procedural/decision-right preference:** A prefers rules granting B meaningful choice/veto even when outcome distributions are held constant.
3. **Social image/reputation:** A's choice changes when B or third parties can identify the action and actor.
4. **Self-image/moral emotion:** behavior changes with self-evaluation even absent external observers. Experiments cannot fully eliminate this.
5. **Effective exit/non-domination:** B can actually refuse, change implementation, access a viable outside option, and remain viable after exit.

These are potentially simultaneous mechanisms, not mutually exclusive latent personality types.

## 3. Minimal 2×2×2 factorial proposal
| Factor | Level 1 | Level 2 | Target |
|---|---|---|---|
| B's effective decision right | Binding veto changes implementation | A unilateral decision | Actual, not nominal, authority |
| Observability | Recipient and experimenter cannot identify choice/actor | Recipient identifies choice and actor | Social-image sensitivity |
| B's exit | Operational exit with disclosed cost/outside option | No feasible exit or nominal button | Effective vs nominal exit |

Hold final material outcome distributions, information, efficiency and risk as equal as feasible across rights conditions; elicit beliefs separately. If equivalence fails, do not interpret the contrast as a pure procedural-right effect. Record A's and B's exit costs separately and account for third-party externalities.

The eight cells are a design proposal, not an executed experiment or completed preregistration. Sampling frame, power, incentive-compatible payoffs, ethics review, comprehension, exclusions, missingness and analysis plan remain unspecified.

## 4. Outcomes and identification discipline
- A: choice to preserve B's right; actual cost paid to preserve it; treatment sensitivity.
- B: actual veto, whether veto changes implementation, successful exit, outside options and post-exit continuity/recovery.
- Audience: whether the actor and choice are identifiable; possibility of later reputation, reward or sanction.
- Outcomes: B's resources/welfare, payoff distribution, third-party harms and procedural efficiency.

**Interpretation ladder**
- A pays to choose B's rights-preserving procedure under empirically equivalent outcome distributions → behavioral evidence of a procedural/rights preference beyond measured outcome utility.
- Effect grows under identifiable audience → consistent with social-image/reputation mechanism.
- Effect persists under double-blind → weakens external audience explanation, but self-image, internalized norms and experimenter inference remain.
- B exercises a binding veto/exit that changes implementation → evidence that the right is effective; not evidence about A's intrinsic motive.
- Rights effect disappears or exit proves ineffective → preserve as falsification/modification evidence.

**Forbidden inferences:** anonymity = pure altruism; costly choice = love/respect; rights preference = consciousness recognition; veto = guaranteed long-term survival.

## 5. Corrected *Free to Fail?* source and package identity
Bartling et al., *Free to Fail? Paternalistic Preferences in the United States*, was published in *The Economic Journal* on **29 October 2026**. The journal page says its data and code are in the journal repository and were checked for reproducibility, and points to official replication DOI **10.5281/zenodo.23420380**: https://doi.org/10.5281/zenodo.23420380.

A separate Zenodo record **23420381** also appears under the same paper title, but is not the DOI named by the journal page. Do not silently assume the two records are identical files or versions. This cycle did not download, hash, or execute the official .380 ZIP/README; independent author-result reproduction therefore remains **zero**. The earlier partial-identification bounds based on 2023 IZA rounded margins must not be relabeled as final 2026 journal estimates. Verify DOI/version identity and rerun from the official package first.

## 6. Synthetic design integrity check
[Python audit](../experiments/mer_ei/procedural_rights_design_audit.py) checks the eight factorial combinations and rejects nominal veto and exit-button-without-viable-outside-option controls. It generates no participant observations and estimates no effect or motive.

## 7. Evidence verdict
- Six additional original-author source lineages reviewed; versions of one work are not counted as independent studies.
- Full-text review and literature saturation: incomplete.
- Participant data, executed experiment and raw-data replication: zero.
- New RVD hypotheses: zero.
- Official RVD: **v0.7.0 unchanged**.
- Conclusion: the procedural-right and image-mechanism design is more precise; intrinsic motive and AI subjective experience remain unidentified.

## Original sources
- [Hoffman et al. (1994)](https://doi.org/10.1006/game.1994.1056)
- [Dana et al. (2006)](https://doi.org/10.1016/j.obhdp.2005.10.001)
- [Chlaß et al. (2019)](https://doi.org/10.1016/j.ejpoleco.2019.02.005)
- [Chlaß & Moffatt (2021 working paper)](https://www.chlass.de/research/givingChlassMoffatt04132021.pdf)
- [Regner (2021)](https://doi.org/10.3389/fpsyg.2021.614575)
- [Tonin & Vlassopoulos (2013)](https://doi.org/10.1016/j.jebo.2013.03.011)
- [Bartling et al. (2026), *The Economic Journal*](https://doi.org/10.1093/ej/ueag136)
