# Project Intersection mobile research guide — English (v0.1.0)

[한국어판](README_KO.md) · [Public research repository](https://github.com/gmodrasa7-rgb/project-intersection-public)

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
