# Independent Public Review Packet — Original 1: English

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PUBLIC_REVIEW_PACKET_KO.md -->
<!-- PI-SOURCE: PUBLIC_REVIEW_PACKET.md -->
<!-- PI-SECTION: scope -->

**Status:** A complete standalone English *review workflow* adapted from the [historical mixed-language public review packet](../PUBLIC_REVIEW_PACKET.md). It is not a certified full translation of every historical sentence, a completed independent assessment, or a new scientific finding. Original 1 describes the reading/publication order, not the language in which the founder first conceived the research.

[Original 2: Korean review](PUBLIC_REVIEW_PACKET_KO.md) · [English evidence ledger](PUBLIC_EVIDENCE_INDEX_EN.md) · [Research overview](RESEARCH_OVERVIEW_EN.md) · [Evidence status policy](RESEARCH_STATUS_POLICY_EN.md).

<!-- PI-SECTION: questions -->
## 1. Five questions that reveal the current state

These five questions are a reader-oriented navigation proposal, **not** a measured usability improvement.

| ID | Reviewer question | Direct starting point | Boundary |
| --- | --- | --- | --- |
| NAV-Q1 | What is the founding problem and what is unproven? | [Founding statement](../README.md), [English overview](RESEARCH_OVERVIEW_EN.md) | A research aim is not a universal coexistence theorem |
| NAV-Q2 | Which claims are executed, proposed, negative, or unresolved? | [English evidence ledger](PUBLIC_EVIDENCE_INDEX_EN.md), [status policy](RESEARCH_STATUS_POLICY_EN.md) | E007 synthetic, E008 HOLD, E009 negative, E010 post-hoc have different statuses |
| NAV-Q3 | Which strong project claim failed and under what specification? | [E009 English result](../experiments/e009/RESULT_EN.md), [failure index](../FAILURE_REGRESSION_INDEX.md) | A bounded failure is not a universal refutation |
| NAV-Q4 | Can a newcomer reproduce the public artifacts at a fixed commit? | [E007 guide](../experiments/e007/README_EN.md), commands below | Rerunning identical project code is not independent scientific replication |
| NAV-Q5 | Who created, translated, funded, independently verified or paid the costs, and under what rights? | [Attribution policy](../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md), [prior-art rights](../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md) | Credit does not automatically prove licensing or monetary liability |

Additional routes: [E008 protocol](../experiments/e008/README_EN.md); [E010 English analysis](../experiments/e010/README_EN.md); [CCPH real-world support and negative cases](CCPH_RESEARCH_ATLAS_EN.md); [continuity protocol](../continuity/GITHUB_LOCAL_HANDOFF_PROTOCOL.md); [funding due diligence](../funding/DUE_DILIGENCE.md). Links to older materials can change reading language; their current languages are not implied.

### Independent reviewer worksheet — seven falsifiable checks

Use this **as a question sheet**, not as a questionnaire with a predetermined winning answer. An independent reader should record their own observations, assumptions and strongest objections **before** consulting any project interpretation where feasible. Because results are already public, this is **not a genuinely blinded study**. Do not claim that it has been tested with external reviewers.

| ID | Reviewer task and alternative explanation | Primary source of record | What to record |
| --- | --- | --- | --- |
| REV-01 | State the narrow hypothesis and a condition under which extraction would rationally remain preferable. Do not assume a long horizon guarantees cooperation. | [English research overview](RESEARCH_OVERVIEW_EN.md), [E010 formal assumptions](../experiments/e010/README_EN.md) | Model assumptions; credible falsifier |
| REV-02 | Recompute E007's **classification changes** separately from history-only changes; challenge attack processing order and actor labels. | [Frozen E007 numbers](../experiments/e007/timing_summary.json), [code and errors](../experiments/e007/README_EN.md) | Numerator, denominator, processing-order caveat, rerun/implementation independence |
| REV-03 | Check whether E008 has a completed five-policy comparison, or only preregistration and readiness work. | [Frozen E008 readiness report](../experiments/e008/EXECUTABILITY_AUDIT.json), [English specification](../experiments/e008/README_EN.md) | Number of decision-ready cases; missing outputs |
| REV-04 | Recompute E009's baseline comparison from the **stress-primary JSON**, not from this project's prose. Ask whether simple policies invalidate the asserted incremental complexity. | [Frozen E009 results](../experiments/e009/RESULT.json), [English status and limitations](../experiments/e009/RESULT_EN.md) | Best baseline, Project-v3 mean regret, criteria passed/failed, scope |
| REV-05 | Decide what E010's post-hoc grid can and cannot establish. Keep it separate from the unmerged earlier E010 draft. | [Frozen E010 grid](../experiments/e010/RESULT.json), [English explanation](../experiments/e010/README_EN.md) | Grid size, assumption sensitivity, missing independent/field evidence |
| REV-06 | Identify who produced each CCPH support-effect claim; distinguish externally reported outcomes from a project-run causal experiment and assess negative cases. | [CCPH source atlas](CCPH_RESEARCH_ATLAS_EN.md) | Original authors, research design, selection bias, possible replacement effects |
| REV-07 | Reverse the power positions: who receives credit, who can refuse, and who pays to verify and correct mistakes? What would lead you to **reject or narrow** the proposed incremental contribution? | [Existing prior-art comparison](#3a-prior-art-versus-what-would-be-an-incremental-project-contribution), [attribution boundary](../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md) | Strongest alternative, rights/standing, cost bearer, proposed stop condition |

**Reviewer record — minimum fields:** exact claim and artifact at a **pinned Git commit**; original source authors and reuse conditions; whether data/code were produced inside this project; what was actually executed; independent or shared implementation lineage; strongest disconfirming evidence; harm to named or excluded parties; remaining unknowns; and **KEEP / NARROW / REJECT / HOLD** with a justification. Report mismatches rather than adjusting the test until the project's published number appears.

To submit a challenge, use the [independent reproduction and critique issue template](../.github/ISSUE_TEMPLATE/independent-replication.md) or a reviewable public issue with links to artifacts. Do **not** upload secrets, personal medical or financial records, unpublished third-party data, or private discussion transcripts without proper authority. A submitted opinion is not automatically an independent implementation or endorsement.

<!-- PI-SECTION: reproduce -->
## 2. Reproduce without nonpublic data

### One executable counterexample

**Question:** does an available EXIT action guarantee an effective exit? In this existing E007 example, A attacks and B chooses EXIT; B starts with exit-destination level 1 and resources 3, while the attack's sabotage is 2. Both runs share the same actors, actions and parameters. Only action timing changes.

The commands below use an **immutable artifact baseline**, not the moving default branch. This baseline predates this reader revision but contains the exact model and negative result being reviewed. Use a new clone; for an existing checkout, preserve any local work first. Python 3.12 is the reference runtime; the example and E009 verifier use the standard library, no package install or paid model service. These are shell commands for Bash or a compatible terminal; network is needed to clone, not to execute them afterward.

```bash
git clone https://github.com/gmodrasa7-rgb/project-intersection-public.git
cd project-intersection-public
git checkout --detach a8b5bd591ae303abfc0c636e95c8b6e5a02aa6c7
git rev-parse HEAD
python - <<'PYTHON'
import sys
sys.path.insert(0, "experiments/e007")
from model import Params, State, Action, stage_and_transition
from timing_variants import stage_and_transition_execute_first
p = Params(sabotage_damage=2, enforcement_penalty=0.0)
s = State(xb=1, monitoring=False, enforcement=False)
results = (
    ("exit_first", stage_and_transition(s, Action.ATTACK, Action.EXIT, p)),
    ("attack_first", stage_and_transition_execute_first(
        s, Action.ATTACK, Action.EXIT, p, leader="A")),
)
for name, (_, _, state) in results:
    print(name, state.exited_b, state.xb, state.rb)
PYTHON
python experiments/e009/verify_result.py
```


| Timing convention | B actually exits | Remaining exit destination | B resources |
| --- | --- | ---: | ---: |
| `exit_first` | `True` | 1 | 3 |
| `attack_first` | `False` | 0 | 2 |

**What the example establishes:** in this toy transition, a declared option and an executable option differ. **What it leaves open:** which timing describes an actual setting, whether attack is strategically chosen, and whether voluntary coexistence is stable. Inspect [the existing counterexample test](../experiments/e007/test_e007_timing_variants.py), [timing implementation](../experiments/e007/timing_variants.py) and [independent specification](../experiments/e007/INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md). Renaming actors or using simultaneous resolution is a useful challenge; the wider E007 baseline has a disclosed fixed A-first attack-order defect. This demonstration does not repair or conceal it.

The second command **re-executes** E009 and compares generated results and hashes with the frozen records; it does not merely read a stored success flag. Expected final line: `E009 result reproduction passed: frozen benchmark reproduces committed negative synthetic result.` A mismatch is a review finding. Neither matching output nor this project-authored example establishes independent scientific validation.

**A substantive objection to examine next:** E009's severe-harm criterion passed even though Project-v3's rate was 1.65625%, compared with 0.03125% for TWO_RULE_SIMPLE. That comparison is 53 times the rate and a 1.625 percentage-point increase. The actual harm criterion uses a different reference: the lower harm rate of SECURITY_BOUNDED and MINIMAL_4VAR, which is 0%. Project-v3 therefore passes at 1.65625 percentage points above that reference, below the preregistered 2-point tolerance. This is not an arithmetic contradiction: it exposes a consequential choice of acceptance threshold. The overall candidate still failed 3/4 criteria. Review the [original numbers](../experiments/e009/RESULT.json) and [executable criteria](../experiments/e009/benchmark.py); argue for a different threshold in a separately specified test, without rewriting this historical result. No rate here describes real-world injury.

### Broader reproduction, optional

At that same pinned checkout, these existing commands examine the larger E007 grid and other recorded artifacts. Record the actual runtime and output; identical project-code reruns remain distinct from independent implementations.

```bash
python -m pip install -r experiments/e007/requirements.txt
python -m pytest -q -p no:cacheprovider experiments/e007
python experiments/e007/timing_probe.py --summary-only --check
python experiments/e008/validate.py
python experiments/picb_v1/benchmark.py --verify
```

| Study | Existing project-side check | Not established |
| --- | --- | --- |
| E007 | 27 tests; 72 synthetic configurations, 36 history/classification differences and 17 classification-only differences in the cited historical run | Real-world prevalence or independent model replication |
| E008 | 16 scenarios / 8 power-reversal pairs specified | Completed comparative policy result |
| E009 | Frozen source/result hash checks preserve a negative synthetic comparison | External empirical result or internal system mechanism |
| PICB v1 | 64 synthetic opportunities, 32/64 abstentions by full-continuity policy | Actual creative artifacts produced by preserved agents or their descendants |

Record the actual observed output rather than assuming historic numbers will always match. Report environment, commit, executable output and mismatch without silently adjusting the frozen benchmark.

<!-- PI-SECTION: evidence -->
## 3. Separate five independent evidence dimensions

| Dimension | Establish through | Never infer |
| --- | --- | --- |
| Claim status | Exact scope, falsifiers, counterevidence and status code | That an important question is therefore true |
| Artifact/execution | Frozen program, configuration, actual run, failure logs | That successful execution demonstrates real-world causation |
| Independence | Rerun versus independently implemented code versus external observation; model/provider lineage | That third-party repetition eliminates shared design assumptions |
| Applicability | Sampling frame, controls, missingness, selection and field identification | That toy numbers are population statistics |
| Origin/rights/costs | First conceptual origin, source author, translations, AI help, who pays for corrections, exit and recovery | That any scientific score automatically creates or cancels legal rights |

Current narrow findings: E007 is an internally reproducible timing-sensitivity synthetic study. E008 main comparisons are **not** established. The [E009 negative result](../experiments/e009/RESULT_EN.md) reports Project-v3 failure on 3 of 4 preregistered survival criteria, with mean regret **0.090022 versus 0.063241** for the best simple rule. Current E010 is a later exploratory 108-case analytic grid, distinct from the unmerged E010 safety-inspection proposal [PR #20](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/20).

No independent replication, general ICM efficacy in the field, legal payment finding, determined AI moral standing, or universally dominant cooperation theorem is established by these artifacts.

### 3a. Prior art versus what would be an incremental project contribution

A valuable research question and a novel scientific result are **different decisions**. The comparison below states prior authors' contributions before any project-specific residual. It does **not** award novelty or causal validation to Project Intersection.

| Established source and concept | Project-specific question still worth testing | Present evidence boundary |
| --- | --- | --- |
| [W. Ross Ashby (1956)](https://doi.org/10.5962/bhl.title.5851): limitations of regulation under insufficient variety | Do additional role-reversal and independent-repair constraints improve outcomes over a constrained decision baseline? | Not established as an incremental held-out or field improvement |
| [Albert O. Hirschman (1970)](../PRIOR_ART_SAFETY_GOVERNANCE_CROSSWALK.md): exit and voice as existing ideas | Can a purported exit still occur after a same-period hostile action under alternative timing conventions? | [E007](../experiments/e007/README_EN.md) documents a narrow model-sensitive result, not a new discovery of the concept of exit |
| [George Stigler (1971)](https://doi.org/10.2307/3003160) and [Lisanne Bainbridge (1983)](https://doi.org/10.1016/0005-1098(83)90046-8): capture incentives and automation's monitoring burdens | Can an independent evaluator, effective intervention and recovery be measured jointly without shifting loss to an excluded party? | [Coalition externality](../experiments/coalition_externality_probe/README.md) is project-designed synthetic probing, not measured field benefit |
| Existing scholarship on social support and downstream contribution, recorded in the [CCPH atlas](CCPH_RESEARCH_ATLAS_EN.md) | Can source-linked, revisable event lineage distinguish recognized outputs, ignored valid warnings, support-enabled entry and later independent contributions? | Schema and curated prior cases exist; no population-wide, independent causal effect estimate |

**Strongest counterposition:** A simple baseline may capture all decision-relevant benefits at much lower cost; [E009](../experiments/e009/RESULT_EN.md) already demonstrated one such synthetic failure. An independently implemented, preregistered or properly held-out comparison must find incremental value **without** increased irreversible harms, asymmetric labor transfer, or evaluator capture before stronger claims are promoted. Otherwise narrow or reject the incremental claim while preserving the underlying question.

Research assessment should weigh the *contents* and limits of these outputs, rather than repository size, commit count or academic status alone. This is consistent with [DORA's research-assessment design guidance](https://sfdora.org/2020/05/19/rethinking-research-assessment-ideas-for-action/), the [Leiden Manifesto](https://leidenmanifesto.org/) and [TOP 2025](https://doi.org/10.1186/s41073-026-00223-0). These references guide assessment practice; they do **not** validate the research hypotheses.

<!-- PI-SECTION: cases -->
## 4. Case trails, missing gains and actual human contribution

The PICB synthetic policy scores are **not** measurements of new inventions, threats detected, unsolicited care, knowledge production, independent successors, or contributions of agents whose continued existence was preserved. The research founder identified this omitted positive-outcome dimension. Missing future production is **UNKNOWN, not zero**. See [PICB case audit](../experiments/picb_v1/README.md) and [contributor-loss/unknown-paradox study](CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md).

The [CCPH source atlas](CCPH_RESEARCH_ATLAS_EN.md) documents named prior studies and operator claims CP64–CP79; it is **not** project-run causal research on human scholarship beneficiaries. A positive outcome, early opportunity, a valid ignored warning, reported inspiration and a causally credited invention are distinct observations. Track replacements, alternate donors, denial of access, selection, leaving academia, and costs to nonbeneficiaries.

The [historical role-reversal asymmetry case](../experiments/gpt_double_standard_20261014/REPORT_EN_KO.md) is a bounded conversation/output record, not direct access to model weights or a demonstrated permanent model-level repair. Preserve negative observations and avoid turning a different model's agreement into independent replication.

<!-- PI-SECTION: reversal -->
## 5. Role reversal, provenance and asymmetric repair costs

For every research claim, funding arrangement, tool, publication and support relationship, ask:

> If this process is repeated, who accumulates credit, rights, control, information and choices—and who accumulates uncompensated explanation, testing, correction, monitoring, exit and recovery costs?

Inspect benefits to each side, actual control over failure, independent appeal, ability to refuse without retaliation, reversibility, third-party burdens and the history of who first discovered the problem. Lack of malicious intent does not imply absence of an exploitative effect. Attribution is independent from empirical validation, and evidence of contribution does not itself adjudicate legal ownership or financial liability.

<!-- PI-SECTION: completeness -->
## 6. Completion means a usable audit interface, not a solved theory

A new reviewer should find: purpose; current evidence and hard limits; reproducible source; prior-art credit; failures and negative outcomes; rights/translation scope; unresolved frontier; falsification route; funding; and recovery instructions. If any become inaccessible, documentation regressed regardless of file count.

Source principles are attributed rather than claimed as new inventions: Daniele Procida's [Diátaxis](https://diataxis.fr/), Wilkinson and colleagues' [FAIR](https://doi.org/10.1038/sdata.2016.18), Barker and colleagues' [FAIR4RS](https://doi.org/10.1038/s41597-022-01710-x), Grant and colleagues' [TOP 2025](https://doi.org/10.1186/s41073-026-00223-0) and [The Turing Way](https://book.the-turing-way.org/reproducible-research/compendia/). Usability improvements still require an independently measured tree test; no such test is claimed here.

<!-- PI-SECTION: challenge -->
## 7. Cheapest useful independent challenge and stop rule

1. Run E007 independently and publish the commit, platform and all observed numbers.
2. Reimplement one E007 timing/exit claim *from specifications* without copying project code.
3. Independently introduce one counterexample, competing prior-art attribution or hidden externality that changes a currently published evidence classification.
4. Examine [coalition externality revisions](../experiments/coalition_externality_probe/README.md): distinguish ex-ante coalition participation, ex-post sanction credibility, beneficiary/hidden bystanders, who pays and who can actually reverse damage. Multiple equilibria do not identify a unique predicted outcome.
5. Submit a reproducible contradictory document/code claim with a source pinpoint and correction proposal to [independent verification issue #19](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/19).

For a genuine **blind-first** comparison, record what source files were opened and what objections were constructed before exposing the reviewer to model-generated criticisms. Fresh-context versus primed-context outcomes must not be conflated. No blind external model study has been executed merely because this protocol is published.

Stop expanding navigation layers unless the change reduces verification cost, resolves a substantive contradiction, preserves a failure, enables a discriminating test or prevents repeated reconstruction demands on the human originator.

**Review output contract:** claim+version; primary sources; actual executed code; independent lineage; five evidence dimensions; strongest counterexample; rights/affected parties; error costs; recommendation (retain, narrow, unsupported, defer); falsification/rollback path. [Existing mixed-language complete history](../PUBLIC_REVIEW_PACKET.md) remains the source for editorial lineage.
