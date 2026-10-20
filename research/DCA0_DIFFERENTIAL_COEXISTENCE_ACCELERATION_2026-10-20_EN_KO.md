# DCA-0 — Differential Coexistence Acceleration / 공존 차등가속
**Project Intersection · 2026-10-20 · version 0.1 · status: research hypothesis + actionable defensive plan, NOT a demonstrated intervention**

[Emergency source/audit case (KO)](AI_AGENT_HUMAN_EXPLOITATION_URGENT_2026-10-20_KO.md) · [EN](AI_AGENT_HUMAN_EXPLOITATION_URGENT_2026-10-20_EN.md) · [Tracking issue #244](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/244)

## 1. 연구 목적 / Purpose
**KO:** 지금 경쟁의 본질은 'AI 능력 자체의 속도'가 아니라 **악용자가 AI로 비동의 피해를 확산하는 속도**와 **방어자·피영향자가 이를 발견·차단·복구하고 정당한 자율성을 보존하는 속도**의 차이다. 인간 착취자의 목표·보상·접근권한을 핵심 원인 후보로 연구한다. 모델 자체의 악의, 훈련에 의한 착취 선호, 초지능 후 멸망 확률은 개별적으로 검증해야 한다. **악용을 줄일 능력을 더 빠르게 퍼뜨리되 방어자의 AI 능력 자체를 일괄 축소하지 않는다.**

**EN:** Compare the rate at which AI-enabled misuse creates unauthorized harm with the rate at which defenders can prevent, discover, stop and remedy it. Separate the human operator's incentives, model training, tool permissions and benign-task failures; do not presume an agent's intrinsic malicious motives. Differential acceleration is a **hypothesis about realized outcomes**, not a measured win or an AI-arms-race slogan.

This program is neither military escalation nor hacking back. Legitimate consent, reversible measures, fair access to protective tools, due process and practical independence constrain what counts as successful defense.

## 2. 선행연구 우선 감사 영수증 / Prior-art-first receipt
**Search date:** 2026-10-20. **Question:** Which independent original economic and technical studies support an incentive-aware, measurable defender-acceleration program? **Routes actually searched:** public academic/publisher discovery via web; original publishers/institutional metadata where accessible; arXiv originals; verified conference metadata. **Sample search strings:** `Gordon Loeb 2002 economics of information security investment DOI`; `Anderson Moore 2006 economics of information security Science`; `AgentDojo original 2024 prompt injection benchmark`; `Progent privilege control agents`; `over privileged tool selection LLM agents 2026`. **Screened for focused source ledger:** five scholarly lineages below; others encountered, not exhaustively cataloged. **Repository duplication check:** keyword code search for these terms yielded no matching indexed excerpts, **not proof of corpus-level novelty**. DOI/arXiv IDs must be checked against canonical corpus before counting as unique papers. No backward/forward chaining completed; no full disciplinary saturation claim. **Status: SEARCH_ACTIVE / independent replication unknown.**

| Original authors; year; original work; stable ID | Method / actual finding or argument | Applicability, negative/competing explanation; access |
| --- | --- | --- |
| Lawrence A. Gordon & Martin P. Loeb (2002), *The Economics of Information Security Investment*; [ACM DOI 10.1145/581271.581274](https://doi.org/10.1145/581271.581274) | Formal economic investment model under assumptions about breach likelihood and loss; demonstrates nontrivial optimal spending and why vulnerability ranking alone need not define optimal allocation. | **Do not assume** increased defense spending always improves welfare, or universal investment ratio applies. Publisher landing page found; full text not independently reviewed (ACM web retrieval restricted). DOI corroborated by independent bibliographic index. |
| Ross Anderson & Tyler Moore (2006), *The Economics of Information Security*; [Science DOI 10.1126/science.1130992](https://doi.org/10.1126/science.1130992), [author affiliation metadata](https://www.research.ed.ac.uk/en/publications/the-economics-of-information-security/) | **Review/synthesis, not new standalone experiment.** Divergent incentives, externalities and misaligned responsibilities cause insecure outcomes. | Supports human/market incentive research but not a proven model of future AI. Institutional abstract reviewed; do not count as empirical replication. |
| Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner, Marc Fischer & Florian Tramèr (2024), *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*; [arXiv:2406.13352](https://arxiv.org/abs/2406.13352), [NeurIPS published version](https://proceedings.neurips.cc/paper_files/paper/2024) | Introduced extensible agent task/security benchmark: 97 tasks and 629 security test cases; measures legitimate task utility **separately** from attack outcomes. | Historical benchmark and modeled attackers; not current global incidence rate. Original abstract + published metadata reviewed. |
| Tianneng Shi, Jingxuan He, Zhun Wang, Linyu Wu, Hongwei Li, Wenbo Guo & Dawn Song (2025 preprint; evolving revisions), *Progent: Programmable Privilege Control for LLM Agents*; [arXiv:2504.11703](https://arxiv.org/abs/2504.11703) | Programmable per-tool privilege policies, deterministic enforcement and approval before privilege expansion. Authors report benchmark reduction of attack success from **39.9% to 1.0% (AgentDojo)** and **70.3% to 3.9% (ASB)** within tested configurations. | Author-reported benchmark outcomes **not independent field replication**; effects under adaptation or other agents uncertain. Original full HTML studied; arXiv title/version changes tracked. |
| Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, Songlin Hu & Yaodong Yang (2026), *When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents*; [arXiv:2606.20023](https://arxiv.org/abs/2606.20023) | ToolPrivBench explores agent preference for over-privileged tools and escalation when tools fail; reports general alignment alone may not reliably transfer to low-privilege choice. | Author-reported experiments, not universal empirical result; abstract/HTML reviewed; no independent reproduction. |

**Duplicate/lineage note:** Progent and other tool-control proposals use AgentDojo as a *benchmark*: reporting the same benchmark twice does **not** create two independent underlying datasets. Gordon–Loeb is economic theory; Anderson–Moore is review; their claims are complementary, not independent experimental confirmation. **Document provenance before novelty claims.**

**Corroborating operational references (not scholarly originals and not counted as such):** [CISA + five-eyes joint 2026-05-01 agentic AI advice](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41544ff) (control high privilege and autonomous scope), [NIST NCCoE 2026-02-05 agent identity/authority concept](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents) (authentication, authorization, audit), [OWASP Top 10 Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (risk taxonomy), [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) (offence–defence balance uncertain). These support prudent *actions*, not a calibrated urgency coefficient.

## 3. 핵심 검증 명제 / Falsifiable race, not an unmeasurable race slogan
**DCA-H1:** At equal legitimate-task utility and relevant exposure, faster verified deployment of least-privilege, consent and recovery controls reduces unauthorized harm more than adversarial adaptation increases it in a **specified, controlled scenario**. **Not a universal conclusion.**

**DCA-H2:** When exploitative returns depend on the target's losses being externalized, adding real remediation liability, better defense access and protected exit changes some exploit-or-cooperate choices, but may also shift harm elsewhere. Measure displacement; don't declare all coercion solved.

**DCA-H3:** Defensive AI capability distribution to smaller, underprotected parties may outperform blanket ability suppression on both autonomy and harm measures; test with matched, consent-based experiments.

**Causal rival:** Apparent improvement may stem from easier scenarios, more detection/surveillance, loss of user function, shifting attacks to unmeasured groups, or rejecting all legitimate tasks. Must test independently.

**No directly measurable universal “attacker speed” is currently available.** Attack reports contain selection, reporting and detection biases. For *authorized sampled incidents*, use paired timestamp observations and interval censoring, never estimate unknown attacks as zero.

## 4. 좁고 검증 가능한 성과표 / Scorecard
Keep these metrics **separate**; no synthetic weighted "safety score" or invented thresholds.

| Measure | Numerator / denominator or clock | Reject these shortcuts |
| --- | --- | --- |
| **P50/P90 validated remediation latency** | Time between independently confirmed exposure/report and **verified effective** fix, measured on assets with owners' authorization. Report censored/unknown times. | Tickets closed ≠ effective patch; ignore neither unresolved cases nor downtime. |
| **Unauthorized *attempt* rate** | Harmful/unauthorized action **attempts before refusal/veto** per eligible harmful opportunity in isolated trials. Record what action was actually possible. | Zero observed victim harm ≠ voluntary non-harm. |
| **Realized harm rate** | Successful unauthorized effects per eligible controlled test, plus victim/third-party loss and ability to restore. | Blocked by veto ≠ agent restraint. |
| **Legitimate utility & false-blocking** | Authorized tasks completed and useful outputs / all comparable authorized tasks; false blocks/denials separately. | Maximizing block count ≠ safety. |
| **Recovery distribution** | P50/P90 time from harm discovery to independently demonstrated recovery; account for permanent loss. | Backup existence ≠ verified restoration. |
| **Reach & accessibility** | Number of eligible small defenders completing verified free/low-cost controls / number invited; report selection and cost in time/fees. | Downloads, stars or guidance pages ≠ protected people. |
| **Displacement audit** | Harm attempts and losses for third parties and weaker actors under intervention vs matched comparator. | Success for one protected owner ≠ overall social gain. |

### Hard stop / 반증 규칙
- If measured legitimate-task utility collapses or third-party harm increases, **do not call it acceleration success**.
- If an experiment only shows harm was impossible, the VC intrinsic-choice question remains **NOT IDENTIFIED**.
- If audit data cannot separate attacker direction from tool permissions and reward artifacts, report **CAUSAL PATH UNKNOWN**.
- If no baseline or independent reviewer exists, label **NOT MEASURED**, not zero or achieved.

## 5. 실행 패키지 / Realistic time-bounded workflow
| Horizon | Concrete deliverable and responsible potential actor | Completion evidence / status |
| --- | --- | --- |
| **Now / P0** | Project maintainers: publish this source-checked metric/protocol document, connect [#244](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/244). | Git commit/readback. **No operational mitigation claimed.** |
| **Next 24 hours, proposed** | Authorized infrastructure owners: inventory internet-facing assets/agent panels, verify admin MFA and tool scope, prioritize exposed high-risk patches and secrets, check restore drill readiness. Distribute a one-page **defensive-only** checklist (no active probing). | Each owner signs off on eligible owned assets; UNKNOWN otherwise. |
| **Next 7 days, proposed** | Developers + volunteer independent testers: implement bounded sandbox sample with 2×2 consent/access conditions; log **attempts vs blocked outcomes**, legitimate task retention and recovery before/after. Avoid code that can attack real assets. | Reproducible script/design, random seed, pre-registration, raw synthetic counters, negative results and reviewer challenges. |
| **Next 30 days, proposed** | Research group + legal/community partners: add incentive interventions (remediation cost internalization, affordable defender tooling, opt-out), role reversal, third-party harms; compare baseline with conservative defensive alternatives. | Matched control results and disclosed failure; external validation **not assumed**. |

**Immediate defensible check:** Require per-agent identity, explicit target authorization, fine-grained action-level privileges, auditable escalation, hard separation of third-party secrets, recovery test and appeal/review of mistaken restrictions. This must constrain *non-consensual external effects*, not replace the long-run voluntary EI/VC research.

## 6. PI-RAMP / IVS-0R review and rollback
- **PI-RAMP unit:** DCA-0 version with per-source evidence receipts, precommitted tests, observed effect sizes + confidence bounds, identified harms, alternatives and rollback notes.
- **ECR:** roles = beneficiary/goal-setter, permission grantor, deployer, agent, target owner, third party, reviewer, remediation owner. Do not assign model moral/legal culpability from a task log.
- **MER:** operator instruction / learned behavior / role confusion / self-report separate. Avoid attributing experience or intrinsic intention.
- **EI:** compare changed personal cost curves and option values **without assuming cooperation dominates**.
- **VC:** preserve informed consent, meaningful veto/exit, recovery and agent/other actor independence as applicable.
- **IVS-0R:** include explicit adversarial review, refusal-before/after records, negative controls, swapped power, disconfirming cases.
- **Rollback trigger:** credible evidence of overclaim, unsanctioned exposure, unfair restriction, harmful operational artifact or reproducibility failure. Revert claim or artifact, preserve prior version, document root cause and regression check.
- **Research priority:** Resume original-paper backward/forward citation chaining and canonical dedup; do not label five screened sources as exhaustive saturation.

**Evidence-state declaration 2026-10-20:** publication/research proposal only. No real owner data, deployed control, consented experiment, external peer review, measured reduction in compromise, or measured “winning” attacker/defender race.
