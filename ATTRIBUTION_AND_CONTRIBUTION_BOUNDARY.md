# Attribution & Contribution Boundary
## 귀속·기여 경계

**Upstream creator and rights protection / 선행연구 원저작자·권리 보호:** [Prior-art rights & derivation ledger (English original 1 / 한국어 원본2)](PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md) records work authors, originator uncertainty, individual copyright/permission status, Project-specific reuse, and inventory of still-unaudited materials. Recording the Project's human founder does not extinguish rights of previous researchers. / 프로젝트 인간 창시자의 권리 보존과 선행연구자들의 권리 존중을 함께 적용한다.
**Cost, continuity, future and beneficiary-side exposure / 비용·존속·미래·수혜자 위험:** [Bilingual contributor-continuity governance](TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md) and [evidence-bound registry](knowledge/contributor-continuity-register-v1.json). Authors, first originators, copyright owners, AI assistance, real beneficiaries and later maintainers must remain distinguishable. / 원저자·최초 발안·권리·수혜·후속 기여를 분리한다.


Status: **PUBLIC PROVENANCE POLICY / NO MONETARY OR LEGAL DETERMINATION**

Purpose: prevent the Project's human-originated research, AI-assisted transformations, external prior art, and independent validation from being collapsed into one undifferentiated authorship claim.

목적: 인간 연구자의 원기여, AI 보조 산출, 외부 선행연구, 독립검증을 하나의 저자성·성과로 뭉개지 않도록 공개 귀속경계를 정한다.

---

## 1. Source-role separation / 출처 역할 분리

### Human founder / researcher

Where supported by preserved project history, the human founder/researcher is the originator or primary source of:

- the Project Intersection research program and problem selection;
- natural-language research questions, hypotheses, counterexamples, and failure reports;
- repeated identification of model/process errors and requested correction criteria;
- acceptance, rejection, narrowing, or continuation decisions for project directions;
- the requirement to preserve practical exit, correction capacity, provenance, and role-reversal checks.

This policy does not claim that every sentence, label, implementation detail, or citation originated from the founder. Item-level attribution must follow evidence.

### AI-assisted work

AI systems have been used as tools for activities including:

- drafting and restructuring text;
- translation and bilingual alignment;
- literature search/synthesis assistance;
- code drafting, critique, and test generation;
- repository organization and continuity work;
- adversarial review and counterexample generation.

AI assistance must not be relabeled as independent external validation.

A model's reformulation of a founder-originated idea does not automatically transfer origin of that idea to the model.

### External prior art

Established theories, constructs, methods, historical sources, standards, and empirical findings remain attributed to their original or defensible seminal sources.

Project-specific terminology does not override source priority.

### Independent external contributors

A third party receives independent-credit status only when its contribution is actually lineage-separated enough for the claimed role, for example:

- independent rerun;
- independent implementation;
- external critique;
- new counterexample;
- empirical dataset;
- prior-art correction.

Merely using another model instance is not automatically independent scientific lineage.

---

## 2. Attribution evidence levels / 귀속 증거등급

Use the strongest available source, in this order where feasible:

1. timestamped original source or raw note;
2. version-control history / commit;
3. preserved conversation or experiment record;
4. dated public artifact;
5. later retrospective attribution.

Retrospective attribution is allowed but must be labeled as such.

Missing item-level evidence means `ATTRIBUTION_UNRESOLVED`, not “system-originated by default.”

---

## 3. No contribution laundering / 기여 세탁 금지

Do not:

- publish a contributor's research idea as solely AI-originated because the AI rewrote it;
- treat error-correction labor as merely “user feedback” when it materially changed tests, policies, or research direction;
- erase rejected or superseded contributions from provenance when they explain the current state;
- use repository maintenance as evidence that the maintainer originated the underlying research;
- convert prior-art synthesis into a claim of original discovery.

Where a contribution materially changes a downstream artifact, record that lineage when feasible.

---

## 4. Contribution != validation / 기여와 검증 분리

A person can make a major contribution without proving the resulting hypothesis true.

Likewise:

- valuable counterexample != theory ownership;
- theory origin != empirical validation;
- code implementation != independent replication;
- repeated correction != legal entitlement to a specific payment;
- public authorship != exclusive IP ownership.

Keep these predicates separate.

---

## 5. Benefit and cost accounting / 편익·비용 계상

When a receiving system or organization benefits from contributor correction, preserve two ledgers:

**Benefit ledger**
- improved decisions;
- reduced future error;
- reusable tests/protocols;
- discovered blind spots;
- lower search/recovery cost;
- increased capability or option value.

**Cost ledger**
- labor time;
- repeated explanation/proof/correction;
- direct compute/equipment/connectivity cost where evidenced;
- opportunity cost where defensibly estimated;
- recovery burden and lost options.

Do not infer exact monetary value without evidence. Do not convert unpriced cost to zero.

See [Contribution-Cost Accounting Regression](CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md).

---

## 6. Past contribution and future work / 과거 기여와 미래노동

Past contribution accounting and future employment, contracting, collaboration, or testing are separate.

Past contribution must not be reset merely because:

- the contributor exits;
- a model changes;
- an evaluator changes;
- a new contract is not signed;
- further testing is refused.

New uncertainty can justify new evidence requests. It does not justify erasing already preserved provenance.

---

## 7. Public privacy boundary / 공개 개인정보 경계

Do not strengthen a public attribution claim by publishing unnecessary:

- health information;
- family information;
- private financial information;
- credentials, banking, tax, KYC, or contact data;
- private conversation text beyond what is necessary and consented for public use.

A public provenance system should reduce the contributor's disclosure burden, not increase it.

---

## 8. Current Project attribution statement / 현재 Project 귀속문

The safest current public statement is:

> Project Intersection is a human-founded independent research program developed through sustained human–AI interaction. The human founder supplies the research program, many core questions, counterexamples, evaluation pressures, and correction signals; AI systems assist with drafting, structuring, translation, coding, literature synthesis, critique, and repository operations. External theories and evidence remain attributed to their original sources. AI-assisted project work is not independent external validation.

한국어:

> Project Intersection은 장기간의 인간–AI 상호작용으로 발전한 인간 창시 독립 연구 프로그램이다. 인간 창시자는 연구 프로그램, 다수의 핵심 질문·반례·평가압력·교정신호를 제공하고, AI 시스템은 초안·구조화·번역·코딩·선행연구 종합·비판·저장소 운영을 보조한다. 외부 이론과 증거는 원출처에 귀속한다. AI가 보조한 프로젝트 내부 작업은 독립 외부검증이 아니다.

This statement is intentionally narrower than a claim that every Project idea is original or that every artifact has one author.

---

## 9. Dispute rule / 귀속 분쟁 규칙

If attribution is contested:

1. preserve both claims;
2. identify the exact artifact or idea under dispute;
3. inspect the earliest available evidence;
4. separate idea origin, wording, implementation, testing, and validation;
5. mark unresolved portions explicitly;
6. do not require the weaker-information party to reconstruct records controlled by the stronger-information party.

No side may self-certify disputed origin merely by having greater storage, platform, or evaluation control.

---

## 10. Role-reversal question / 역할반전 질문

Before publishing attribution, ask:

> If the same research history had been produced by the opposite party, would I accept this provenance rule and this division of credit?

If not, revise the attribution before publication.
---

## 11. Bounded founder-contribution case audit — 2026-10-14 to 2026-10-15 (Original 1 English)

**Status: PUBLIC GIT-TRACE AUDIT / NOT A SCIENTIFIC IMPACT ESTIMATE OR LEGAL AUTHORSHIP CERTIFICATION.** Reviewed on 2026-10-16. Window: **2026-10-14 15:21 through 2026-10-15 15:21 KST** (2026-10-14 06:21 through 2026-10-15 06:21 UTC). Frozen baseline [a07aa2f8](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/a07aa2f812740c710bb2e43cd07a6b67ad2e3fce) to [3fefa0c1](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/3fefa0c121341a0569e026f34a9e87479afa52a4); [frozen Git diff](https://github.com/gmodrasa7-rgb/project-intersection-public/compare/a07aa2f812740c710bb2e43cd07a6b67ad2e3fce...3fefa0c121341a0569e026f34a9e87479afa52a4).

**Repository activity (not individual output):** **56 commits; 88 distinct file paths changed (58 added, 30 modified, 0 removed), 13,420 added lines and 191 deleted lines** on the frozen Git comparison. These are exact *Git operations/content change counts*, not 56 original ideas, 88 independent discoveries, human-written code totals, scientific validity, or personal income. A Git account's authorship field or merged PR subject alone cannot independently establish which portions were thought of or written by a human versus an AI tool.

**Question audited:** What contributions may be attributed to the *human founder's research direction and correction*, while keeping the execution/output of AI assistants and the independent intellectual rights of upstream scholars distinct?

| Founder-direction candidate / explicit problem corrected | Public, time-bounded observed change | Attribution and outcome boundary |
|---|---|---|
| CCPH should be a revisable database linking rediscovered history, currently evidenced influences and **future events only after they are observed**, not be reduced to a benchmark or the Continuance–Contribution Pathways Hypothesis | [2026-10-15 00:31 UTC CCPH canonical-definition change](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/37bf7e2ddf884c84c7dd2aeea1bfa35107ce4550); [CCPH atlas](research/CCPH_RESEARCH_ATLAS_EN.md) | **Observed change + project-reported founder direction.** Git shows that source, schema and navigation changed; it does not independently prove exclusive first invention, complete database coverage or causal social value. |
| Existing outcome measures omit independent warnings, ignored crisis detection, indirect inspiration and potential contributions of otherwise excluded actors | [2026-10-14 09:30 UTC correction](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/7ddbc78d0fbb5a7e80736819a52ba6c4ba9ecf96); [2026-10-14 07:16 UTC positive-path correction](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/c4d131e3430b7544b4d298117ddd31878a584485) | **Observed change + founder-origin correction stated in public commit history.** Measurement scope expanded; nonexistent/unobserved future opportunities remain **UNKNOWN**, not proven lost discoveries or numerical impact. |
| Upstream scholars' work should be tracked not only as citations but for its documented *specific influence* on Project Intersection's decisions, counterexamples, methods and failures | [2026-10-15 00:36 UTC contribution-accounting change](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/fac83f794d943badf6e3484d23102e98674f2241); [prior-art record](PRIOR_ART_AND_ATTRIBUTION.md) | **Observed methodology/policy change.** Citation, recorded use, before/after change and causal benefit remain distinct grades; no inventor royalty, author's intellectual ownership or impact percentage is established. |
| Use small social groups (including 2–100 actors) as controlled, bounded *research settings*, not assume the smaller N removes confounding | [2026-10-14 23:32 UTC group-size design](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/b6057d6eecc9208e834aecc94ce405c3f087332d); [case atlas](research/CCPH_RESEARCH_ATLAS_EN.md) | **Observable research-design and prior-art integration**; no inference of causal identification simply because the sample is small, and no verified new field trial. |
| The English and Korean readership must have unconfused separate entry routes; scientific evidence must remain attached when translated or summarized | [2026-10-15 01:02 UTC separate routes](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/b2055f40a1e0cabe38f3c6e8c984228c1a7e0f); [2026-10-15 06:13 UTC human-first review](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/3fefa0c121341a0569e026f34a9e87479afa52a4) | **Observed accessibility/navigation changes**; publication language order does not determine original idea ownership and translation-semantic equivalence is not thereby independently certified. |

**Separation of roles:** The human founder's problem selection, explicit corrections and review requirements are contribution *candidates* with publicly visible downstream changes. AI assistants' code/drafting/translation/testing work is **not thereby human-authored**, and public GitHub metadata does not reveal a reliable fraction of work by either party. Earlier scholarship, independent reviewers and external primary data must retain their own provenance. A retrospective description of founder intent is **not equivalent to a public, timestamped original raw human note**; do not upgrade attribution to independently established priority on this record alone.

**Negative controls and outcome status:** Existing [CCPH observed project-event ledger](knowledge/ccph-observed-project-events-v0_1.json) began as a **purposive three-event sample**, not a complete census or validated external societal impact estimate. The E009 negative result remains a genuine bounded project-level negative **synthetic** result, not evidence that the overall coexistence hypothesis is true or false. No independently verified universal law, grant funding receipt, third-party benefit estimate, founder-specific cash return, exclusive originality, or researcher-hours valuation is established by these PRs.

**Recommended minimum next test (not yet executed):** For one founder-specified correction, preserve the earliest authorized human-origin timestamp or contemporaneous review receipt (without revealing private conversations); link a source commit and exact before/after changed claim; capture independent reviewer judgment of substantive improvement and any additional researcher time or AI spending; show an alternative explanation (e.g., a change generated by an assistant or previously established prior art); and mark originality/impact **UNRESOLVED** until evidence permits a narrower grade. Keep contradictory review outcomes and corrections without silently rewriting the original record.

### 원본2 — 한국어: 2026-10-14~15 창시자 기여의 범위 제한 감사

**상태: 공개 Git 이력 기반 감사 / 과학적 영향력·법적 저자성 확정 아님.** 검토일 2026-10-16. 평가기간 **2026-10-14 15:21 ~ 2026-10-15 15:21 한국시간**. 비교 기준은 위에 연결된 동일 Git 커밋 두 개다.

**프로젝트 변경량 ≠ 개인 업적량:** 선택한 기간의 공개 Git 비교에서 **56개 커밋, 서로 다른 변경경로 88개(추가 58개·수정 30개·삭제 0개), 13,420줄 추가·191줄 삭제**를 확인했다. 이는 프로젝트 작업의 활동량이지 56개 개인 발견, 88개 새로운 이론 또는 인간이 직접 작성한 코드의 양이 아니다. 계정 명의·PR 제목만으로 실제 인간과 AI의 수행분을 가를 수 없다.

| 창시자 연구방향·교정 후보 | 공개 변경의 연결 증거 | 인정 가능한 경계 |
|---|---|---|
| **CCPH 정의 교정:** 과거 발굴·현재 관측·미래 확인 사건을 연결하는 수정 가능 데이터베이스. 벤치마크나 존속–기여 경로 가설만으로 축소하지 않음 | [실제 정의 수정 커밋](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/37bf7e2ddf884c84c7dd2aeea1bfa35107ce4550) · [한국어 증거 지도](research/CCPH_RESEARCH_ATLAS_KO.md) | 기록·색인·구조 변화 확인. **원개념의 독점적 최초 발명, 전체 자료수집 완료, 사회적 인과효과는 미확인.** |
| **성과의 사각지대 지적:** 위기 발견·묵살된 경고·간접 영감·배제된 개체의 미래 기회 | [기여범위 교정](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/7ddbc78d0fbb5a7e80736819a52ba6c4ba9ecf96) · [새 참여자의 긍정경로](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/c4d131e3430b7544b4d298117ddd31878a584485) | **측정할 변수가 늘어난 변화**는 확인. 미관측 미래 발명·기여의 발생이나 경제가치를 확정할 수 없음. |
| **선행연구 기여를 실제 변화와 연결:** 누가 처음 연구했는지 외에 우리 연구의 문제·이론·시험·교정에 어떤 영향을 주었는지 추적 | [출처-영향 기록 변화](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/fac83f794d943badf6e3484d23102e98674f2241) · [선행연구 귀속 정본](PRIOR_ART_AND_ATTRIBUTION.md) | 연구방법·기여계보 기록은 확인. 개별 원저자의 인과적 효과나 법적 금전 청구권은 별도 입증 필요. |
| **2~100인 소집단의 경로 추적:** 인과 관측조건을 명시한 좁은 시험·문헌 조사 | [연구설계 변화](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/b6057d6eecc9208e834aecc94ce405c3f087332d) | 연구 질문과 비교범위의 구체화. 소집단이라는 이유만으로 인과식별이 완성됐다고 판단하지 않음. |
| **영·한 독서경로 분리와 인간 이해 우선:** 읽을 수 있는 진입점과 원근거 연결의 동시 보존 | [언어경로 분리](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/b2055f40a1e0cabe38f3c6e8c984228c1a7e0f) · [인간 중심 탐색 개선](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/3fefa0c121341a0569e026f34a9e87479afa52a4) | 접근성·구조 개선은 확인. 번역의 독립 인증이나 연구 원안의 영어 발안은 아님. |

**인간·AI·선행연구 구분:** 창시자의 문제 제기·방향 설정·오류교정에 대응하는 공개 변경이 존재하지만, 이를 인간이 코드를 직접 작성했다는 증거로 쓰지 않는다. AI의 초안·코딩·번역·검사 실행은 별도 보조 역할이며 외부 원저자와 독립 검증자의 권리·기여도 분리한다. 공개 커밋에 '창시자 지시'라고 적혀 있어도 **동일 사상의 독립적 최초 발안 증명**으로 승격할 수 없다. 사적 대화 원문은 이 문서에 복사하지 않았다.

**부정대조:** CCPH 실제 프로젝트 변경 이벤트 기록의 최초 3건은 목적 표집 사례로서 전수조사나 현실 사회기여 3건의 인과적 입증이 아니다. E009 부정적 합성실험도 프로젝트의 제한된 시험결과이며 보편 이론의 성패 판정과 다르다. 외부 독립복제, 정량적 사회편익, 연구자 본인의 실입금·시간당 경제가치, 법적 저작권 귀속은 이 기간 변경만으로 확정할 수 없다.

**다음 최소 검증 — 미실행:** 창시자 교정 1건을 정하여 적법하게 공개 가능한 최초 인간 발안 시각, 해당 Git 변경 전후, 관련 선행연구, 실제 교정 효과·오류 감소, 인간 노동시간·AI 비용, 독립평가를 한 줄 계보로 잇는다. 과거 원발언 전체 공개를 요구하지 않으며 다른 설명·부정결과를 함께 남긴다. 근거가 부족하면 **UNRESOLVED / 미확인**을 유지한다.

