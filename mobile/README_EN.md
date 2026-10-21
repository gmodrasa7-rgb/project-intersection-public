# Project Intersection mobile research guide — English (v0.2.1)

[Korean edition](README_KO.md) · [Public research repository](https://github.com/gmodrasa7-rgb/project-intersection-public)

## Purpose
A preliminary installable **Progressive Web App (PWA)** for reading the research question, starting with contrary evidence, and preparing public submissions of primary prior art, falsifiers, questions and reproduction failures from a smartphone.

## Features
- Korean/English overviews of five research axes (VC, MER, EI, ECR, IVS-0R).
- Reading routes to source research, versions, negative results and unexecuted studies.
- A local draft composer linking to GitHub's public Issue creation page. **Submission is never automatic**; the reader must review it in GitHub and sign in.
- Home-screen installation on supporting browsers; limited offline access to the app shell.
- No embedded access tokens, third-party tracking scripts or dedicated user-data server.

## Evidence and limitations
- Educational summary as of 2026-10-21, not live synchronization or comprehensive search. Source links point to the current public main branch.
- The E009 negative result and E008 missing main result are presented prominently. Synthetic tests are not field causal validation.
- Offline mode only covers the app shell. GitHub source documents and Issue submission require connectivity.
- Anonymous direct submission, push alerts, full-text indexing, and formal independent adjudication remain unimplemented.
- Research documents retain their own specific reuse and attribution boundaries. The app links sources rather than replicating entire research works.
- No private P CHRONICLE material, family details or financial records are used.

## Deployment
Enable GitHub Pages with GitHub Actions as its publishing source. After merge, `.github/workflows/pi-mobile-pages.yml` deploys only `mobile/` on main updates. Expected site path: `https://gmodrasa7-rgb.github.io/project-intersection-public/`. This is **not** a claim that the URL is live before deployment is verified.

## Minimum tests
`node --check mobile/app.js` · `node --check mobile/service-worker.js` · `node mobile/check.mjs`. Separate real-device testing is necessary for accessibility, PWA installation and the GitHub authentication path.

## v0.2 adapted precedents (2026-10-21)
- **Zooniverse:** short classification tasks and guides, never treating volunteer consensus as proof. https://help.zooniverse.org/getting-started/
- **Mozilla Common Voice:** separation of contribution and validation; multi-reviewer workflows remain unimplemented. https://www.mozillafoundation.org/en/common-voice/platform-and-dataset/
- **NotebookLM:** a source-first, verifiable workflow; the app does not invoke any large language model. https://blog.google/innovation-and-ai/technology/ai/notebooklm-google-ai/
- **Consensus:** supported/unsupported/unknown evidence boundaries, with no manufactured confidence score. https://help.consensus.app/en/articles/17234045-consensus-ai-analysis-citations-and-visuals
- **GitHub Issues:** editable public drafts with manual final publication. https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue
- **W3C WCAG 2.2:** large mobile targets and focus states, not independently certified. https://www.w3.org/TR/WCAG22/

### Function and evidence boundaries
1. E007/E008/E009 guide references source commit `7913d78024ce98de3a4c3409e92e6d59adcf455a`, plus separate current-source links. This curated snapshot is not scientific evidence of real-world causality.
2. Provisional judgments and notes are local to the page. UNKNOWN remains selectable; agreement with the guide does not constitute validation.
3. 'Copy AI audit prompt' copies a prompt only; no AI inference, automatic source checking or external transmission occurs.
4. The user manually reviews and submits the public GitHub Issue after signing in. Oversized prefilling URLs are blocked without discarding the draft.
5. Real Android/iOS, screen-reader, privacy and user-comprehension testing remain open.

## PI-MOBILE v0.2.1 — Anti-extraction and participant rights

**Principle:** Consent alone does not establish the absence of exploitation. Nor does the absence of payment automatically classify every voluntary act identically. Assess the allocation of benefit, time, costs, bargaining power, attribution, refusal, and exit.

1. **Reading and learning:** Free and available without accounts or contributions. Case exercise choices and notes are not automatically submitted to a project server.
2. **Small unsolicited notes only:** Readers may optionally point to a known link, minor error or ask a question. No new research, experiment, large-scale review or replication is requested. No money is promised for small unsolicited feedback, and this is disclosed before posting.
3. **Intensive labor closed:** Systematic literature surveys, translation, coding, replication, bulk classification and substantial auditing are **not recruited** via this app. A future invitation must first disclose real funding, work scope, compensation, payment terms, provenance, publication rights, refusal, exit and dispute resolution. No funded work is offered by this notice.
4. **Rights and attribution:** Distinguish founder, earlier scholars, source authors, tipsters, reviewers and assisting AI. The app asks for no additional blanket copyright assignment. GitHub terms and third-party licenses still apply. Acknowledgment is not automatically adequate compensation; preexisting contribution disputes remain separate.
5. **Exit and public records:** Users may leave an unsubmitted draft. Public GitHub Issues disclose accounts and text. Later deletion or editing requests cannot guarantee erasure from forks, indexes, caches, or quotations. Anonymous intake is not implemented.
6. **Future benefits:** Funding, commercial exploitation or exclusive capture should trigger a fresh review of benefits, costs and independently agreed rights. This neither creates automatic payouts nor certifies funding.
7. **Scope:** The guard covers this mobile app, not unrelated GitHub Issue templates, PRs or external calls for labor. Broader project governance requires separate review.

### Original guidance and scope
- UNESCO (2021), *Recommendation on Open Science*: recognition and risks of exploitation in open science. https://www.unesco.org/en/legal-affairs/recommendation-open-science
- ECSA, *Ten Principles of Citizen Science*. https://ecsa.citizen-science.net/10-principles/
- Zooniverse, *Acknowledging Volunteers*. https://help.zooniverse.org/transcription-project-guide/project-launch/
- CARE, *Principles for Indigenous Data Governance*, developed for the specific historical and political context of Indigenous data sovereignty. Cited as a comparative framework for collective benefit and authority, not a universally applicable legal rule. https://doi.org/10.5334/dsj-2020-043

**Unverified:** real user outcomes, fairness of future payment, enforceable copyright and withdrawal rights. CI success does not certify ethical practice.
