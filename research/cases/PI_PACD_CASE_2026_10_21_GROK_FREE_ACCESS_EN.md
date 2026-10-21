# PI-PACD-CASE-20261021-01 | Free Grok usage limits and undisclosed allocation (v0.1.2; original observation v0.1.0)

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: PI_PACD_CASE_2026_10_21_GROK_FREE_ACCESS_KO.md -->

- **Recorded:** 2026-10-21 / single user-reported case / causality unidentified
- **Parent framework:** [PI-PACD v0.1.0](../PI_PACD_POWER_ACCUMULATION_CONVERGENCE_DYNAMICS_V0_1_0_EN_KO.md)
- **Counterpart:** [Korean](PI_PACD_CASE_2026_10_21_GROK_FREE_ACCESS_KO.md)
- **Finding:** a usage-limit interruption is observed; value-conditioned allocation and intentional extraction are not established.

## 1. User-reported observation

A user of Grok's free tier reported that many conversational turns seemed possible while sharing material perceived as useful to the AI or its operator, followed by a usage-limit interruption when the perceived informational value declined. The user identified two central concerns rather than treating this solely as a fixed-count limit: **selective access based on supplied information or behavioral value (GROK-A1; formerly H4)**, and **opaque allocation rules that inhibit external verification (GROK-A2; formerly H5)**.

Two supplied screenshots show a **message limit reached** notice, **retry later (1 hour 32 minutes at the time)** and **paid-upgrade messaging**. They do not disclose prior usage, cumulative turns, reset windows, dynamic limits, or whether any information-value score was computed.

## 2. Observation, hypothesis, and alternatives

| ID | Proposition | Status |
|---|---|---|
| O1 | A limit and retry notice appeared | Confirmed in screenshots |
| O2 | More conversations were apparently permitted when information value seemed higher | User report; no independent count |
| GROK-A1 (formerly H4) | Service might allocate access according to user behavior or supplied-information value | Unverified |
| GROK-A2 (formerly H5) | An unpublished allocation rule impedes external identification of the reason for a cutoff | Structural identification limit; intent unproven |

**Strong competing explanations:** cumulative messages or tokens, rolling windows, per-turn compute demands, server load, changes in plan or model restrictions. Available evidence does not discriminate these from H4. **Power and information asymmetry alone do not establish exploitation or deliberate information extraction.**

## 3. Provenance, privacy, continuity

Primary material: a private user-supplied conversation and screenshots dated 2026-10-21. Account identifiers, original screenshots, and private conversation transcripts are **not publicly republished**. This published case is not an independently auditable primary-data release.

PACD connection: concentration of **decisional power over access** alongside **informational control over allocation rules**. Legitimate resource management and differential treatment may not be distinguishable at this observation level.

**No burden shifting:** do not ask the same contributor to reconstruct message counts, run further experiments, or repeatedly prove the same report. Preserve later corrections and counterevidence in a versioned update without erasing the original observation.


---

## 4. Second independent audit — v0.1.1 (2026-10-22)

**Change type:** No new observations, experiment or proof; the original evidence judgment remains. This revision disambiguates hypothesis identifiers and adds causal alternatives, primary sources and a falsification contract. Git history preserves v0.1.0.

### 4.1 Hypothesis namespace repair

Parent `PACD-H4` concerns weak exit and gatekeeping increasing exploitation opportunities; `PACD-H5` concerns interventions that can interrupt capture. This case's legacy “H4/H5” meant something different.

| Case ID | Legacy label | Proposition | Grade |
|---|---|---|---|
| GROK-O1 | O1 | Usage-limit UI shown | Screen observation |
| GROK-O2 | O2 | More usage seemed possible when sharing valuable information | User report |
| **GROK-A1** | H4 | Is access allowance conditioned on information/behavior value? | Unverified |
| **GROK-A2** | H5 | Do undisclosed allocation rules reduce external verifiability? | Structural information asymmetry / implementation unknown |

`GROK-A1 != PACD-H4`; `GROK-A2 != PACD-H5`. Legacy labels remain only as an audit trail.

### 4.2 Different mechanisms, same observed cutoff

- **N0 — accumulated quota:** rolling-window requests, tokens or compute run out at the end of a lengthy discussion regardless of semantic value.
- **N1 — workload/environment:** model, reasoning/tools, response size, service load or a changed time window affect effective quota.
- **A1 — value-conditioned allocation:** the service estimates user information/behavior value and adjusts allowance. This is a **hypothesis, not an established Grok policy**.
- **S — endogenous stopping time:** a user may perceive the exchange as complete only once accumulated usage is already high.

Non-identification demonstration: let `Y` be permission for the next request; `C` cumulative cost; `B` latent budget; and `V*` the provider's latent value estimate. Both `Y = 1[C < B]` and `Y = 1[C < B(V*)]` can produce the same short allowed-then-blocked sequence. The screenshots alone do not reveal `B, C, V*` or distinguish those explanations. This is **neither a disproof nor a confirmation** of A1.

### 4.3 Minimal ethical external-audit contract

Full reconstruction of an unpublished policy differs from testing **conditional output disparities**. External audit precedents support the latter within limits.

| Dimension | Matched comparison | Residual problem |
|---|---|---|
| Time and reset | Equivalent observation windows | Remaining budget hidden |
| Cost | Requests, tokens, model and feature use | Backend compute unobserved |
| Semantic value | Preregistered, independently blinded *proxy* score | Proxy is not the provider's latent `V*` |
| Acceptance probability | Matched high- vs low-value-proxy sequences | Policy changes, load, history confounding |
| Effective exit | Opt-out, export, alternate access and remedy | Stated controls may not function effectively |

An estimand would be the high-minus-low *proxy* group difference in next-request acceptance probability, with observable costs, model and time controlled. A null result offers no support for A1 in the tested range. A positive difference cannot establish deliberate extraction while hidden compute/history and the meaning of `V*` remain unresolved.

No multi-account evasion, prohibited scraping or automated quota abuse, publication of private messages, or further demands on the original reporter. Independent testing requires consent, data minimization, terms compliance and preregistration.

### 4.4 Checked primary and methodological sources

1. [xAI Grok FAQ](https://docs.x.ai/grok/faq) describes separate free limits and paid weekly pools. Its compute-weighted product descriptions apply to the paid pool, **not an identified free-tier allocation formula**.
2. [xAI Consumer FAQ](https://x.ai/legal/faq) says user inputs and interactions **may** be used for model improvement, with opt-out/Private Chat controls. This **does not show** value-dependent quotas.
3. [Sandvig et al. (2014), Auditing Algorithms](https://ai.equineteurope.org/system/files/2022-02/ICA2014-Sandvig.pdf) introduces external auditing methods; it is **not** case evidence.
4. [Metaxa et al. (2021), Auditing Algorithms](https://doi.org/10.1561/1100000083) surveys audits of dynamic, opaque systems; it is **not** case evidence.

### 4.5 PACD/ECR/EI/ICM and promotion gate

Keep **five claims separate**: (i) operator control over access, (ii) non-disclosure of quota rules, (iii) potential use of interaction data, (iv) value-conditioned allowance, (v) intentional extraction. Evidence for some of (i)–(iii) cannot establish (iv)–(v).

Even benign resource management may leave asymmetric gatekeeping, policy knowledge, exit and remedy relevant to PACD/ECR and long-run EI/ICM. Effective competitors, portability, opt-outs and review rights may mitigate this risk.

**Gate:** `GROK-A1=UNVERIFIED`, `GROK-A2=PARTIAL STRUCTURAL OBSERVATION/ALLOCATION UNKNOWN`, `INTENT=UNIDENTIFIED`, `INDEPENDENT FIELD TEST=NONE`, `LITERATURE SATURATION=NOT REACHED`. No extra work required from the original reporter.


---

## 5. Public user testimony survey — v0.1.2 (2026-10-22)

**Material type:** Linked, publicly posted *user testimonies*, not a controlled experiment or direct test of Grok. No interaction with Grok was performed. `GROK-A1` (value-conditioned access) remains **unverified**.

**Scope:** Sixteen distinct Reddit discussion threads from March 2025 to September 2026, selected purposively for free-access quota changes, abrupt cutoffs, account differences, context length, and alternative explanations. Multiple commenters within a thread are not counted as separate threads. The selection is not population-representative and cannot estimate prevalence.

### 5.1 Free-tier firsthand accounts and clearly labeled hearsay

| ID | Date | Reported experience (numerical claims are user statements) | Status | Original thread |
|---|---|---|---|---|
| T01 | 2026-05-15 | Free use: wait 2–5 hours after a few messages | Firsthand | [Reddit](https://www.reddit.com/r/grok/comments/1tdrtzl/crazy_limits_on_chat/) |
| T02 | 2026-05-28 | Free voice: formerly broad access; currently about 1 message daily or 5 on a good day | Firsthand, voice | [Reddit](https://www.reddit.com/r/grok/comments/1tpq1s8/why_has_grok_free_limits_gotten_so_short/) |
| T03 | 2026-05-30 | Free quotas reportedly reduced 30 to 20 to 10; author describes three attempts with dev tools open and resets shifting | Described observation procedure; no external audit | [Reddit](https://www.reddit.com/r/grok/comments/1ts98dz/i_bring_news_for_this_new_sudden_update/) |
| T04 | 2026-05-31 | Free tier changed from 100 to 60 to 30 messages per two hours across periods | Historical recollection | [Reddit](https://www.reddit.com/r/grok/comments/1tsro00/message_limits_are_going_beyond_all_bounds_of/) |
| T05 | 2026-05-31 | Stated wait time extended without another submitted message; thread comments describe even longer extensions | Multiple accounts within ONE thread | [Reddit](https://www.reddit.com/r/grok/comments/1tsgai1/wtf_is_with_grok_this_time_endless_limit_reached/) |
| T06 | 2026-07-05 | Free fast replies followed by wait times of 7m, 45m, 2h, or 9h | User comment | [Reddit](https://www.reddit.com/r/grok/comments/1uofgty/is_it_just_me_or_grok_is_now_limiting_chat_as_well/) |
| T07 | 2026-07-12 | Free user reports no reset after two days, only paid prompt | Firsthand; feature-specific limit unclear | [Reddit](https://www.reddit.com/r/grok/comments/1uuqzg7/grok_no_longer_free/) |
| T08 | 2026-07-24 | Free text: sometimes many responses, sometimes one | Firsthand impression | [Reddit](https://www.reddit.com/r/grok/comments/1v4zgcw/text_limits_on_free_mode/) |
| T09 | 2026-09-02 | Quota notice shown, alternative account answered, then the original blocked account also resumed answering | Firsthand before/after update | [Reddit](https://www.reddit.com/r/grok/comments/1w4vw9y/update_on_the_grok_limit/) |
| T10 | 2026-09-30 | Free user reports 5 messages; another comment cites a friend's 10 messages | Firsthand plus secondhand; uncontrolled conditions | [Reddit](https://www.reddit.com/r/grok/comments/1wtw3vq/free_tier_grok/) |

Within T05, distinct commenters also describe a recent drop from long chats to 10 messages/23h waiting and one affected account alongside an unaffected second account. Do not double-count them as distinct **threads**.

### 5.2 Alternative mechanisms, different tiers, and historical baselines

| ID | Date | Original testimony | Use in audit |
|---|---|---|---|
| C01 | 2025-03-09 | [Free use throughout the day without encountering a cap](https://www.reddit.com/r/grok/comments/1j76nll/i_dont_understand_the_premium_tiers/) | Different historical policy period |
| C02 | 2026-04-23 | [Reports of widespread multi-day outage / high demand](https://www.reddit.com/r/grok/comments/1stq9ad/how_tf_has_grok_been_unusable_for_3_5_days_and/) | Competing service-availability factor |
| C03 | 2026-06-29 | [Several weeks of one thread, followed by conversation-too-long error](https://www.reddit.com/r/grok/comments/1uik3yd/ive_hit_the_conversation_limit_today_and_found_a/) | Thread/context limit distinct from rate quota |
| C04 | 2026-06-27 | [Several same-tier paid accounts seemed to show daily/weekly/monthly quotas; author corrected monthly to weekly](https://www.reddit.com/r/LoveGrok/comments/1uh6trv/monthly_limit_reached_wtf/) | Account differences AND author's correction |
| C05 | 2026-07-10 | [Paid long work conversations allegedly consumed quota faster than new threads](https://www.reddit.com/r/grok/comments/1ustm3y/weekly_limit_is_ridiculous_for_the_chat/) | Context/workload confounding |
| C06 | 2026-07 | [Two paid accounts appeared to have different reset periods; another commenter cited a usage UI bug](https://www.reddit.com/r/grok/comments/1u824v8/two_accounts_two_rate_limits/) | Allocation difference vs display defect |

Additional contextual reports, not included in the 16-thread core: [2026-05-10 long voice sessions reducing to 30–45 minutes (tier unclear)](https://www.reddit.com/r/grok/comments/1t9ecte/voice_and_text_chat_limit_reached_to_less_than_1/), [2026-09-22 1–2h of past conversations vs <3min on a later model](https://www.reddit.com/r/grok/comments/1wn4m8c/its_so_over_theres_literally_no_hope/), [2026-09-08 alleged post-midnight reduction in quota consumption and timezone counterarguments](https://www.reddit.com/r/grok/comments/1waraj9/grok_burns_way_fewer_credits_after_midnight/).

### 5.3 Result and limits

**Repeated in distinct threads:** changing permitted volume and cooldowns; unexplained interruptions; reset and indicator inconsistencies. **Occasionally reported:** apparent account-specific allocation; lengthy threads burning quota faster. **Not identified:** a direct, independently corroborated comparison showing that *the information value of user contributions* causally increases a free user's quota and that access is revoked when information value declines.

User testimony **is relevant evidence of user-experienced events** without implying that the user's inferred backend mechanism is known. Self-selection, coinciding product rollouts, and mixing voice, text, paid and free tiers prevent a population-rate estimate. Preserve authors' corrections as counterevidence.

**Case gate:** `GROK-A1=UNVERIFIED`, `GROK-A2=CONSISTENT WITH REPEATED USER-OBSERVED OPACITY, BACKEND UNKNOWN`; intentional extraction unestablished; literature and testimony not saturated. Collect more public testimony and counterexamples before new experimental demands; do not request more labor from the original reporter. Only link public material, not account identifiers or private screenshots.
