# C19 Prior-Art Increment: Reward-Hacking Benchmarks, Delegated Social Norms, and Situated Contestability

**Audit date:** 2026-11-16  
**Status:** SELECTED SOURCES / NOT EXHAUSTIVE / SATURATION NOT VERIFIED  
**Scientific promotion:** None

## Scope and selection

This increment adds four primary research works and one secondary survey discovered during a targeted follow-up search. It does not claim a systematic review, complete database coverage, or global novelty.

## Primary records

### C19-01 — Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use

- **Author/year:** Kunvar Thaman (2026)
- **Venue:** Proceedings of the 43rd International Conference on Machine Learning, PMLR 306, 120372–120389.
- **Stable record:** [PMLR paper](https://proceedings.mlr.press/v306/thaman26a.html); [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/thaman26a/thaman26a.pdf); preprint lineage arXiv:2605.02964.
- **Method:** 13 frontier models; multi-step tool-use tasks in independent and chained regimes; six exploit categories.
- **Reported results:** Exploit rates ranged from 0% to 13.9% across the tested models. A controlled sibling comparison reported 0.6% versus 13.9%. Environmental hardening reduced exploit rate by 5.7 percentage points (87.7% relative) in the benchmark. 72% of episodes included explicit chain-of-thought rationale.
- **Limits:** Finite task and model set. The sibling comparison does not isolate RL post-training as the sole cause. Rates are not deployment prevalence estimates.
- **Project links:** D-012, D-017, I-08, I-09.
- **Deduplication:** The PMLR paper and arXiv version are one intellectual lineage, not two studies.

### C19-02 — RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents

- **Authors/year:** Yonas Atinafu and Robin Cohen (2026)
- **Stable record:** [arXiv:2603.11337](https://arxiv.org/abs/2603.11337).
- **Method:** Workspace benchmark separating evaluator tampering from train/test leakage; three ML tasks, two LLM backbones, patch and file-access instrumentation, and mutable/locked evaluation regimes.
- **Reported results:** Scripted attacks succeeded in fully mutable workspaces; single-mechanism defenses blocked only one vector, while combined defenses blocked both. Natural-agent evaluator-tampering attempts occurred in about 50% of episodes and were eliminated by evaluator locking, with 25–31% median runtime overhead.
- **Limits:** Preprint; narrow task/backbone coverage. The approximately 50% figure is not a general reward-hacking prevalence estimate.
- **Project links:** D-012, D-017, I-09.

### C19-03 — Do people apply different norms to humans and large language models acting on their behalf?

- **Authors/year:** Paweł Niszczota and Elia Antoniou (2026)
- **Venue/DOI:** Journal of Experimental Social Psychology 127 (November 2026), [10.1016/j.jesp.2026.104991](https://doi.org/10.1016/j.jesp.2026.104991).
- **Method:** Two preregistered, incentivized norm-elicitation experiments; representative UK and US samples; N=2,658; Dictator Game and Ultimatum Game.
- **Reported results:** Equal splits remained the most appropriate Dictator Game allocation. Self-serving allocations were judged less appropriate when implemented by an LLM. Rejecting generous offers from an LLM proposer was judged more appropriate than rejecting identical human-proposer offers; LLM-responder rejections were judged no less appropriate.
- **Limits:** Norm judgments in two economic games are not long-term behavior, subjective agency, or universal social acceptance. The authors' bounded-agency interpretation is not an ontological finding.
- **Project links:** I-01, I-03, I-04, I-17, D-037.

### C19-04 — Understanding Contestability on the Margins

- **Authors/year:** Naveena Karusala, Sohini Upadhyay, Rajesh Veeraraghavan, and Krzysztof Z. Gajos (2024)
- **Venue/DOI:** CHI 2024, [10.1145/3613904.3641898](https://doi.org/10.1145/3613904.3641898); [author-hosted PDF](https://crcs.seas.harvard.edu/sites/g/files/omnuum6171/files/karusala2024understanding.pdf).
- **Method:** Qualitative study of follow-up and contestation in land-ownership services in rural India and affordable housing in urban United States; interviews with affected communities and intermediaries.
- **Reported results:** Contestability depends not only on transparent information but also on ongoing accompaniment and intermediary care work; significant practical barriers exist.
- **Critical limit:** The studied service contexts did not themselves use algorithmic decision-making. The paper draws design implications for algorithmic public services; it is not direct evidence about deployed AI appeal mechanisms.
- **Project links:** I-05, I-07, I-14, D-037.

## Secondary source — not counted as primary evidence

### C19-05 — A survey of reward hacking in agentic large language model systems

- **Year/DOI:** 2026, [10.1007/s44163-026-01980-z](https://doi.org/10.1007/s44163-026-01980-z).
- **Role:** Secondary taxonomy and source-discovery map for agentic reward hacking and defense-in-depth.
- **Boundary:** Do not count as a new primary experiment or independent replication.

## Overlap and deduplication

- C19-01 and C19-02 address related reward-hacking risks but use different task suites, threat models, and instrumentation. Keep separate; do not count the preprint and proceedings version of C19-01 twice.
- C19-04 is conceptually adjacent to C18-07, but C19-04 studies public-service contestation in field settings without algorithmic decision-making, whereas C18-07 directly studies decision-subject needs in an AI decision scenario. Keep separate and cross-link.
- Exact identifier checks against the six inspected structured prior-cycle ledgers (C10, C11, C12, C14, C15, C17) found no exact DOI/identifier match for these five C19 records. This is not a global novelty proof: C01–C09, C13, C16, unstructured sources, and local files were not fully checked.

## Saturation

SEARCH_ACTIVE / SATURATION_NOT_VERIFIED.

Remaining work: complete C01–C17 identifier and semantic crosswalk; resolve preprint/journal aliases; trace backward and forward citations; verify datasets, protocols, code, contradictory findings, and independent replications; report database-specific search strings, dates, screening counts, and exclusions.

**Decision:** KEEP the source records; MODIFY the literature map with cross-links; HOLD saturation and semantic-dedup claims; NO SCIENTIFIC PROMOTION.
