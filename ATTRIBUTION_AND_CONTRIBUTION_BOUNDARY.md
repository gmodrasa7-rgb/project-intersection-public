# Attribution & Contribution Boundary
## 귀속·기여 경계

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
