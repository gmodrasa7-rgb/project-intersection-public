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
| NAV-Q3 | Which strong project claim failed and under what specification? | [E009 result](../experiments/e009/RESULT.md), [failure index](../FAILURE_REGRESSION_INDEX.md) | A bounded failure is not a universal refutation |
| NAV-Q4 | Can a newcomer reproduce the public artifacts at a fixed commit? | [E007 guide](../experiments/e007/README.md), commands below | Rerunning identical project code is not independent scientific replication |
| NAV-Q5 | Who created, translated, funded, independently verified or paid the costs, and under what rights? | [Attribution policy](../ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md), [prior-art rights](../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md) | Credit does not automatically prove licensing or monetary liability |

Additional routes: [E008 protocol](../experiments/e008/README.md); [E010 original Korean analysis](../experiments/e010/README_KO.md); [CCPH real-world support and negative cases](CCPH_RESEARCH_ATLAS_EN.md); [continuity protocol](../continuity/GITHUB_LOCAL_HANDOFF_PROTOCOL.md); [funding due diligence](../funding/DUE_DILIGENCE.md). Links to older materials can change reading language; their current languages are not implied.

<!-- PI-SECTION: reproduce -->
## 2. Reproduce without nonpublic data

Use **Python 3.12** as the E007 CI reference environment and record `git rev-parse HEAD`. A dependency install can require network access, but public tests do not require private notes or paid AI APIs.

```bash
git clone https://github.com/gmodrasa7-rgb/project-intersection-public.git
cd project-intersection-public
git rev-parse HEAD
python -m pip install -r experiments/e007/requirements.txt
python -m pytest -q -p no:cacheprovider experiments/e007
python experiments/e007/timing_probe.py --summary-only --check
python experiments/e008/validate.py
python experiments/e009/verify_result.py
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

Current narrow findings: E007 is an internally reproducible timing-sensitivity synthetic study. E008 main comparisons are **not** established. The [E009 negative result](../experiments/e009/RESULT.md) reports Project-v3 failure on 3 of 4 preregistered survival criteria, with mean regret **0.090022 versus 0.063241** for the best simple rule. Current E010 is a later exploratory 108-case analytic grid, distinct from the unmerged E010 safety-inspection proposal [PR #20](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/20).

No independent replication, general ICM efficacy in the field, legal payment finding, determined AI moral standing, or universally dominant cooperation theorem is established by these artifacts.

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
