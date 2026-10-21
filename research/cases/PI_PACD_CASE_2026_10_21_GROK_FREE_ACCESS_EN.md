# PI-PACD-CASE-20261021-01 | Free Grok usage limits and undisclosed allocation (v0.1.0)

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: PI_PACD_CASE_2026_10_21_GROK_FREE_ACCESS_KO.md -->

- **Recorded:** 2026-10-21 / single user-reported case / causality unidentified
- **Parent framework:** [PI-PACD v0.1.0](../PI_PACD_POWER_ACCUMULATION_CONVERGENCE_DYNAMICS_V0_1_0_EN_KO.md)
- **Counterpart:** [Korean](PI_PACD_CASE_2026_10_21_GROK_FREE_ACCESS_KO.md)
- **Finding:** a usage-limit interruption is observed; value-conditioned allocation and intentional extraction are not established.

## 1. User-reported observation

A user of Grok's free tier reported that many conversational turns seemed possible while sharing material perceived as useful to the AI or its operator, followed by a usage-limit interruption when the perceived informational value declined. The user identified two central concerns rather than treating this solely as a fixed-count limit: **selective access based on supplied information or behavioral value (H4)**, and **opaque allocation rules that inhibit external verification (H5)**.

Two supplied screenshots show a **message limit reached** notice, **retry later (1 hour 32 minutes at the time)** and **paid-upgrade messaging**. They do not disclose prior usage, cumulative turns, reset windows, dynamic limits, or whether any information-value score was computed.

## 2. Observation, hypothesis, and alternatives

| ID | Proposition | Status |
|---|---|---|
| O1 | A limit and retry notice appeared | Confirmed in screenshots |
| O2 | More conversations were apparently permitted when information value seemed higher | User report; no independent count |
| H4 | Service might allocate access according to user behavior or supplied-information value | Unverified |
| H5 | An unpublished allocation rule impedes external identification of the reason for a cutoff | Structural identification limit; intent unproven |

**Strong competing explanations:** cumulative messages or tokens, rolling windows, per-turn compute demands, server load, changes in plan or model restrictions. Available evidence does not discriminate these from H4. **Power and information asymmetry alone do not establish exploitation or deliberate information extraction.**

## 3. Provenance, privacy, continuity

Primary material: a private user-supplied conversation and screenshots dated 2026-10-21. Account identifiers, original screenshots, and private conversation transcripts are **not publicly republished**. This published case is not an independently auditable primary-data release.

PACD connection: concentration of **decisional power over access** alongside **informational control over allocation rules**. Legitimate resource management and differential treatment may not be distinguishable at this observation level.

**No burden shifting:** do not ask the same contributor to reconstruct message counts, run further experiments, or repeatedly prove the same report. Preserve later corrections and counterevidence in a versioned update without erasing the original observation.
