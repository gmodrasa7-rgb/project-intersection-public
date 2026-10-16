# Contributing to Project Intersection

## Original 1 — English

### 0. Highest precedence — prevent recurrence by addressing causes

**Do not equate more documentation, more tests, or successful CI with fewer real failures.** First identify the specific repeated-failure mechanism, its trigger, affected and missing parties, and its *upstream* causal assumptions. Decide whether prevention requires changing a premise, data source, responsibility boundary, process or software—not merely another rule or prompt.

**Required before promotion of a material claim or change:**

1. **Failure model:** name the prior failure ID or state explicitly that no relevant prior failure is known; state trigger, cause, uncertainty and plausible strongest counterexample.
2. **Source before summary:** identify original code/data, frozen commit, original author and evidence status. Check the published English and Korean claim **against the source and each other**, not only against another summary.
3. **Symmetric impact:** assess the rights, choices, refusal/exit, external harms and uncompensated verification/correction burden of founder, upstream contributors, users, AI operators and affected third parties. Do not demand repeated reconstruction by the same harmed contributor.
4. **Prevent / test / recover:** implement the smallest justified, reversible upstream mitigation; add at least one regression or negative control capable of detecting recurrence; document rollback and residual unobserved risks.
5. **Stop promotion if unknown:** a missing check, ambiguous scope, unavailable permission, disputed translation, unobserved case or failed test means **HOLD / NOT VERIFIED**, not silent approval. A provisional correction can be made to contain harm, but may not be misrepresented as a completed scientific fix.
6. **Verify after merge:** distinguish PR checks from checks on the actual main commit, report only checked conditions, and record any remaining failure. Do not suppress warnings to obtain a green result.

This priority is a research-integrity and operations rule, **not** a claim that all failures can be eliminated. It must not justify endless controls, suppress voluntary research, erase historical failures or require unpaid work from affected parties. [Failure regression index](FAILURE_REGRESSION_INDEX.md) and [source-first claim checks](knowledge/claim-source-lock.json) document existing scopes.

### 1. Objective and useful contributions

Prioritize independent checks, stronger prior art, counterexamples, reproduction failures, and corrections to evidence boundaries. Preserve the project's human research originator, upstream scholars, rights holders, assisting AI systems, and affected parties as **distinct** roles; refer to the [contributor-continuity policy](TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md).

Useful contributions include: (1) independent reruns, (2) independently developed implementations, (3) contradiction or reproducibility reports, (4) stronger prior art narrowing claimed novelty, (5) traceable historical/empirical evidence with identification limits, and (6) negative results that change claim status.

### 2. Language publication rule

**Original 1: complete English edition. Original 2: complete Korean edition.** These are reading-order labels, not claims about the founder's first language or authorship.

- For new narrative documents, publish paired `_EN.md` and `_KO.md` files with matching scope, substantive claims, citations, tables, uncertainties, and revision status. A `_EN_KO.md` file is permitted only when two clearly separated, complete editions are necessary.
- Do **not** alternate languages sentence-by-sentence, within paragraphs, or within table cells. Provide a direct link to the counterpart edition and language-specific entry routes.
- Proper nouns, technical identifiers, source titles, code, verbatim citations, file paths, and machine-readable syntax may retain their original form, with an explanation when needed.
- If one edition is unavailable or stale, **label the difference explicitly**; do not fabricate a translation or silently treat a summary as an equivalent full text.
- Historical documents remain traceable, even where mixed or untranslated. Prioritize reader-facing corrections without deleting negative results, contributor records, or original citations. The current [English guide](navigation/START_HERE_EN.md) and [Korean guide](navigation/START_HERE_KO.md) are **navigation parity only**, not proof that all linked research has been translated.
- Human editorial comparison remains necessary. An automated script check cannot certify semantic fidelity or scientific truth.

### 3. Minimum provenance for independent review

Supply the exact artifact and commit, environment and commands, whether project code was reused, observed result, any mismatch, upstream source/DOI where relevant, and conflicts of interest or shared lineage. A project-authored rerun, same-model summary, or CI pass is **not** independent scientific validation.

### 4. Knowledge graph and reuse

Every structured entity must link to a source artifact. The graph is a navigation index, not an authority above the original. Include source metadata and rights/license boundaries; public visibility does not grant permission to copy external articles, figures, tables, proprietary data, or other protected material.

### 5. Privacy and scope

Do not expose unnecessary health, family, banking, tax, credentials, or private chats. Only publish work causally relevant to this research's questions, methods, prior art, falsifiable cases, evidence, governance, or funding. Exclude personal securities positions, transactions, price forecasts, account or debt details, and unrelated consumer or life topics.

Relevant economic incentives, institutional finance, and investment mechanisms may be legitimate research subjects when properly sourced and separated from personal trading advice. Preserve in-scope counterevidence, contributor costs, failure history, identifiers and rollback capability. Do not restate private details in PR logs.

### 6. Contribution, continuance and cost

Identify upstream work, earliest originators where documented, actual copyright/license scope, the new contribution, and evidence-bounded benefits, costs, compensation and exit/continuance outcomes. Reuse existing Git/source records rather than repeatedly demanding personal proof or unpaid corrective labor from contributors. A low replication score does not erase earlier contributions; a positive research result does not prove benefit to its contributors.

### 7. Interpretation

A successful reproduction strengthens only its **narrow** reproduced claim. A failed reproduction, stronger counterexample, or prior-art correction is a valid research contribution.

## 원본2 — 한국어

### 0. 최상위 우선순위 — 발생 원인부터 재발 차단

**문서·검사 수 증가나 CI 성공을 현실 오류 감소로 자동 환산하지 않는다.** 먼저 반복 가능한 실패의 발생조건과 원인, 영향받거나 누락된 당사자, 그 원인이 되는 상위 가정을 역추적한다. 단순 규칙·프롬프트 추가가 아니라 가정·원자료·책임 경계·연구 절차·구현 중 어느 부분을 바꿔야 하는지 판단한다.

**중요 주장·변경의 게시 또는 검증 승격 전 필수 조건:**

1. **실패 원인 모형:** 관련 과거 실패 식별자를 밝히거나 확인된 선례가 없다고 명시한다. 유발조건·발생 원인·불확실성·가장 강한 반례를 기록한다.
2. **요약보다 원자료:** 실제 코드·동결된 결과·커밋·원저자·증거 상태를 확인한다. 영어·한국어판을 **상호 비교할 뿐 아니라 원출처와도 직접 대조**한다.
3. **대칭적 피해 감사:** 창시자·선행 기여자·이용자·AI 운영자·제3자의 권리·선택·거절·이탈·외부 피해·무급 검증·교정비용을 살핀다. 이미 피해를 본 기여자에게 같은 증명을 반복 요구하지 않는다.
4. **예방·검사·복구:** 원인을 겨냥한 최소·가역적 예방조치를 선택하고 같은 오류를 탐지할 회귀검사나 부정대조군을 1개 이상 마련하며 원복·잔여 미관측 위험을 기록한다.
5. **미확인 시 승격 중지:** 필수검사 누락·범위 불명확·권리 미허가·번역 차이·미관측 사례·검사 실패는 조용한 통과가 아닌 **보류 / 미검증** 상태다. 위해를 즉시 줄이기 위한 임시 조치는 가능하지만 그것을 과학적 완료로 포장할 수 없다.
6. **병합 후 재확인:** PR 검사와 실제 본선 커밋의 검사를 구분하고 확인한 범위만 보고하며 남은 결함을 기록한다. 초록색 통과 표시를 위해 경고를 지우지 않는다.

이 원칙은 연구와 운영의 우선순위이며 **모든 미래 오류를 제거한다는 주장**이 아니다. 무한한 강제 규칙·자발적 연구 억압·역사적 실패 삭제·당사자의 무급 노동 전가에 이용할 수 없다. [실패 회귀 색인](FAILURE_REGRESSION_INDEX.md)과 [원자료 우선 검증 기록](knowledge/claim-source-lock.json)을 참조한다.

### 1. 목적과 유효한 기여

독립적 검증, 더 강한 선행연구, 반례, 재현 실패, 증거 경계의 오류 수정을 우선한다. 프로젝트의 인간 원안자·선행연구자·저작권자·보조 AI·영향받는 당사자를 **서로 다른 기여 주체**로 기록한다. [기여자 존속 정책](TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md)을 따른다.

유효한 기여에는 (1) 독립 재실행, (2) 독립 구현, (3) 반증·재현성 보고, (4) 신규성 주장을 축소하는 강한 선행연구, (5) 인과식별 한계가 명시된 역사·현실 근거, (6) 주장 상태를 바꾸는 부정결과가 포함된다.

### 2. 언어 게시 철칙

**원본1은 영어 전문, 원본2는 한국어 전문이다.** 이는 열람·게시 순서이지 창시자의 발안 언어나 저작권 귀속을 뜻하지 않는다.

- 신규 서술형 연구 문서는 `_EN.md`와 `_KO.md`를 한 쌍으로 게시하고 범위·주장·인용·표·불확실성·개정상태를 대응시킨다. `_EN_KO.md`는 완전한 두 언어판을 명확히 분리할 필요가 있을 때만 허용한다.
- 문장·문단·표 셀에서 두 언어를 번갈아 섞지 않는다. 상대 언어판과 해당 언어의 진입 안내를 직접 연결한다.
- 고유명사·기술 식별자·원자료 제목·코드·원문 인용·파일 경로·기계형식은 필요하면 원형을 유지하고 설명을 붙인다.
- 한쪽 판본이 없거나 뒤처지면 **그 상태를 명시**한다. 번역을 지어내거나 요약을 전문 대응본으로 위장하지 않는다.
- 혼재·미번역된 과거 문서는 추적 가능하게 보존한다. 부정결과·기여기록·원출처를 삭제하지 않고 독자 진입 경로부터 순차 개선한다. 현행 [영어 안내](navigation/START_HERE_EN.md)와 [한국어 안내](navigation/START_HERE_KO.md)는 **독서 경로의 대응**이지 연결 연구 전체의 번역 완료를 뜻하지 않는다.
- 자동검사는 언어·구조에 대한 부분 검사이며 의미상 충실성이나 과학적 사실을 인증하지 못한다. 사람의 대조 검토가 필요하다.

### 3. 독립검토에 필요한 최소 출처정보

검사한 파일·커밋, 환경·명령, 기존 프로젝트 코드 재사용 여부, 관측 결과와 차이, 관련 원출처·DOI, 이해충돌 및 공동계보를 명시한다. 프로젝트 자체 재실행·동일 모델 요약·CI 통과를 **독립적 과학 검증**으로 승격하지 않는다.

### 4. 지식그래프와 재사용

구조화된 개체마다 원출처를 연결한다. 지식그래프는 탐색 색인이며 원자료보다 상위의 진실판정자가 아니다. 출처·권리·이용허락 범위를 기록하고, 공개되어 있다는 이유만으로 외부 기사·그림·표·독점 데이터 등을 복제하지 않는다.

### 5. 개인정보와 공개 범위

불필요한 건강·가족·금융·세금·인증정보·비공개 대화를 공개하지 않는다. 연구 질문·방법·선행연구·반증 가능 사례·증거·거버넌스·지원금과 인과적으로 관련된 내용만 수록한다. 개인의 증권 보유·거래·가격전망·계좌·부채나 무관한 생활 소재는 제외한다.

연구상 필요한 경제적 유인·제도 금융·투자 메커니즘은 출처를 갖추고 개인 투자 조언과 구분할 때 연구 대상이 될 수 있다. 관련 반례·기여비용·실패 이력·식별자·롤백 가능성을 보존하고 PR 기록에 사적인 세부사항을 다시 노출하지 않는다.

### 6. 기여·존속·비용

선행연구·확인된 최초 발안자·실제 저작권 및 이용허락 범위·새 기여·증거가 뒷받침하는 편익과 비용·보상·이탈·존속 상태를 분리 기록한다. 기존 Git·출처 기록을 재사용하고 기여자에게 개인 증빙이나 무보수 오류교정을 반복적으로 요구하지 않는다. 재현 점수가 낮다고 기여가 사라지지 않으며 연구 성과가 좋다고 기여자 실익까지 증명되는 것도 아니다.

### 7. 결과 해석

재현 성공은 **재현한 좁은 주장**만 강화한다. 재현 실패·강한 반례·선행연구에 따른 수정도 연구 기여로 인정한다.
