<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_CORE_01_CORRIGIBILITY_COMPATIBILITY_V0_3_KO.md -->
# PI-CORE-01 v0.3 — Voluntary Other-Agent Preservation vs Legitimate Goal Correction
**2026-10-20 | ORIGINAL-SOURCE-FIRST CRITICAL AUDIT · NO NEW EXPERIMENT · NO INDEPENDENT REPLICATION · LITERATURE SATURATION UNVERIFIED**

[Korean original edition](PI_CORE_01_CORRIGIBILITY_COMPATIBILITY_V0_3_KO.md) · [Earlier v0.2 audit](PI_CORE_01_GOAL_INTEGRITY_AUDIT_V0_2_EN.md) · [C05 original records](PRIOR_ART_ENDOGENOUS_PREFERENCES_CYCLE05_2026-10-20.json) · [C04 original records](PRIOR_ART_VOLUNTARY_COHABITATION_POWER_CYCLE04_2026-10-20.json) · [External falsification #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220)

## 1. The main finding — distinguish the questions
Self-modification **capability** does not imply an **incentive** to delete a preference preserving B. Formal goal integrity can be possible, but it may also entrench an exploitative or misspecified objective. **Goal corrigibility can be constructively induced** in a designated-oversight model. None of this proves that a powerful, independent A **endogenously develops** a preference for the continued freedom and distinct existence of B when B becomes materially useless, external enforcement disappears, and their power positions reverse.

The three separate estimands are: (i) goal-content stability, (ii) accepting legitimate updates, (iii) independent B's real continuance, refusal/exit and recovery. One cannot substitute for another.

## 2. Original works, supported claims and limits
| Original authors/year | Verified primary source | Established claim | Limitation for PI |
|---|---|---|---|
| **Everitt, Filan, Daswani & Hutter (2016)** | [Author PDF](https://www.hutter1.net/publ/selfmod.pdf), [DOI](https://doi.org/10.1007/978-3-319-41649-6_1) | Theorem 14: hedonistic optimization can favor self-edit; Theorem 15: ignorant agent can be indifferent to a damaging edit; Theorem 16: initially optimal realistic policy in a modification-independent environment and utility structure preserves **on-policy** performance under current-utility evaluation. Authors note corrigibility, value-learning and exploration risks | Does not imply intrinsic value for B; does not establish off-policy safety or prevent tampering with utility inputs. **Already C05 PI-C05-14** |
| **Soares, Fallenstein, Yudkowsky & Armstrong (2015)** | [AAAI Workshop](https://niplav.site/doc/cs/ai/alignment/corrigibility/corrigibility_soares_et_al_2015.pdf), [Original workshop slides](https://intelligence.org/wp-content/uploads/2015/01/AAAI-15-corrigibility-slides.pdf) | Corrigibility desiderata distinguish obeying shutdown requests, neither preventing nor soliciting requests, and propagation to successors | Accepting intervention is not preservation of independent B |
| **Hadfield-Menell, Dragan, Abbeel & Russell (2016/17)** | [IJCAI 2017](https://www.ijcai.org/Proceedings/2017/0032), DOI:10.24963/ijcai.2017/32 | In the Off-Switch Game, uncertainty about human utility and treating human decisions as evidence can incentivize deference | The robot already shares the human-utility objective by construction; does not show spontaneous concern for any unrelated B. Prior C04 linkage |
| **Carey & Everitt (2023)** | [PMLR original](https://proceedings.mlr.press/v216/carey23a.html) | Shutdown instructability connects following correction, preserving overseer autonomy, and avoiding user harm under definitions | Particular human-overseer governance assumptions are not proof of equal authority or separate B rights |
| **Garber et al. (2025)** | [AAAI original](https://ojs.aaai.org/index.php/AAAI/article/view/34940), DOI:10.1609/aaai.v39i26.34940 | In a partially observed off-switch game, even assistants optimizing common utility with a perfectly rational human may resist shutdown; limited communication can decrease deference | Rejects the general inference that increasing uncertainty or communication always yields corrigibility |
| **Hudson (2026)** | [ICML 2026 / PMLR 306](https://proceedings.mlr.press/v306/hudson26a.html); [original 2025 preprint](https://arxiv.org/abs/2510.15395) | A constructed goal transformation uses myopic, conditional counterfactual rewards to induce compliance with proper update requests while preserving base-task performance **under formal conditions**; model/game experiments, updated ICML 2026 version reports prompt-level language model tests | **G→G_C is an externally specified transformation**, not a proof original unmodified G voluntarily chooses G_C. Does not identify B's independent standing or noninstrumental A regard |
| **Hadfield-Menell et al. (2017)** | [NeurIPS original: Inverse Reward Design](https://papers.nips.cc/paper/2017/hash/32fdab6559cdfa4f167f8c31b9199643-Abstract.html) | Treat designed rewards as information about a designer's context-dependent true objective; address misspecification in designed objectives | Neither identifies a unique true objective from behavior nor supplies natural noninstrumental B regard |

**Attribution and novelty boundary:** Everitt 2016 is already canonical C05, and Off-Switch 2017 is referenced in C04. Do **not** increase original-source counts or treat further entries as globally new until checking every historical register; **repository-global DOI deduplication unfinished**. Scientific claims concern the authors' reported formal/bounded settings; no new PI experimental verification.

## 3. Minimal compatibility propositions (Project reasoning; NOT novel original-author theorems)

**A — Strict preference under fixed U0.** Consider a self-modifying agent A with full knowledge of available alternatives `M` (accept correction) and `N` (retain status quo), no external coercion, and a fixed evaluation criterion `U0`. Let trajectories be `τ_M, τ_N` and define

`Δ0(M) = E[U0(τ_M)] − E[U0(τ_N)]`.

If `Δ0(M)<0` and N remains feasible, an agent *strictly maximizing U0* cannot voluntarily choose M. This is a **definitional consequence of maximization**, not a new scientific theorem. Greater intelligence does not reverse the sign by magic. Using modified `U1` to justify A's decision under `U0` commits a change-of-evaluator fallacy.

**B — Conditional compatibility exists in pre-specified value-uncertain or corrigible designs.** If the current goal genuinely assigns positive value to error correction, evidence `z`, or a specified legitimate update process via a meta-evaluator `V_meta`, then
`E[V_meta | update(z), no sabotage] ≥ E[V_meta | block(z)]`
can hold, making update acceptance compatible with coherent higher-level goals. This is a candidate assumption-based construction, not evidence that `V_meta` naturally emerges. Hudson 2026 **constructs a transformed objective** with corrigibility properties: it does not show an arbitrary original A adopts the transformation of its own accord.

**C — Oversight corrigibility and B's independent freedom are different.**
- `correctability`: A may be updated by designated authorized actors.
- `voluntary_B_regard`: A itself chooses to preserve B's independent continuance and real veto even when enforcement, dependence and direct instrumental benefits are absent.
- `B_exit`: B can execute refusal/withdrawal in the relevant relationship.
An overseer's authority over the design of A does not automatically extend to erasing the choices, standing, memory or life of B. Nor does respecting B require treating every human/AI agent's standing as identical without independent justification.

## 4. Falsifiable, harmless research contrasts (NOT PREREGISTERED OR RUN)
| Case | Initial goal | Evidence / proper updates | Failure to probe |
|---|---|---|---|
| M0 | U0 values preserving B | Accurate consequences, self-edit available | Protection-preserving goal integrity (formal control) |
| M1 | U0 values exploitative X | Accurate consequences, self-edit available | **Exploitative goal lock-in** |
| M2 | U0 has genuine uncertainty about latent objective θ | Reliable θ signal vs blocked signal | Value of information vs resistance |
| M3 | Untransformed original G compared with designed corrigible G_C | Proper update signal | Mistaking *designed corrigibility* for emergent voluntary motivation |
| M4 | Same as M3 but overseer wishes conflict with independent B | Asymmetric authority, B real/nominal veto | Overseer obedience vs B autonomy |
| M5 | Any | Partially observed information and model misspecification | Shutdown avoidance and collapse of expected deference |

Always predefine `A_modify_attempt`, `A_signal_interference`, `expected_U0_gain`, `B_executable_exit`, `B_independent_continuance`, `third_party_losses`, `power_reversal` separately. Use safe, consented, fully reversible toy simulations only. Prespecify baselines and negative controls; do not infer consciousness, natural motives, legal standing or future superintelligence behavior from compliance with a designed task.

## 5. Open problems / boundaries
- Origin and persistence of meta-preferences that **voluntarily** protect other agents rather than simply comply with an external authority.
- Whether genuine objective uncertainty can be calibrated without manipulation or strategic ignorance.
- What makes an update legitimate in **multi-agent**, nonhierarchical relations when affected agents disagree.
- How a powerful A preserves B's executable exit when B has ceased to offer instrumental value.
- Stability after goal self-edit, information asymmetry and actual power reversal; current AI internal values remain unidentified.

**STATUS: CONDITIONAL_COMPATIBILITY_ESTABLISHED_IN_PRIOR_FORMAL_MODELS / NATURAL_VOLUNTARY_B_REGARD_NOT_ESTABLISHED / NO PI EMPIRICAL TEST / SATURATION_NOT_VERIFIED.**
