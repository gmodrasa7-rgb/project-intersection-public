# PI-RAMP v0.4.0 — Source Identity ≠ Study Identity / 출처 식별 ≠ 동일 연구

<!-- PI-RAMP-DOMAIN: source-level integrity, not scientific truth -->
<!-- PI-RAMP-EFFECT: EFFECT_UNMEASURED -->
## Original 1 — English | Evidence-fingerprint and contrast-preservation gate

**2026-10-20 · Pilot source-integrity audit, not certified systematic-review saturation or independent scientific validation.** [v0.3 protocol](PI_RAMP_V0_3_EN.md) · [Frozen 12-source manifest](../evaluation/pi_ramp/PRIOR_ART_C01_C12_IDENTITY_AUDIT_20261020.json) · [Executable regression](../tools/audit_prior_art_c01_c12_identity.py)

### What the real repository audit found

- Inspected all 12 structured original-author prior-art files C01–C12: **233 curated records, 203 records with 203 distinct normalized DOI identifiers, 30 with other source identifiers**. These are **not 233 independently conducted studies**. Every count refers only to this bounded, snapshotted corpus.
- **Zero exact DOI collisions; zero identical normalized titles in this selected corpus.** Do not infer that there are no duplicate underlying datasets or samples, overlapping study reports, erroneous source abstracts, uncaught retractions, or citations elsewhere in the repository.
- Title-token screening at a declared Jaccard threshold of **0.56** yields **six pairs for human review**. **No pair is automatically deduplicated.** Source JSON Git blob digests and a machine-computed manifest lock the reproducible baseline.
- The difference between *same source*, *different reports of one study*, *replication*, *follow-up research*, *contradictory outcomes*, and *conceptual resemblance* requires original methods, author and sample comparisons; the current records alone do not establish that final classification.

### Six near-title pairs (not six established duplicates)

| Candidate records | Working interpretation; remain distinct |
| --- | --- |
| C09-16 / C09-17 | Different harm/benefit trade-offs; never flatten into one invariant altruism result |
| PI-C07-09 / PI-C07-15 | Decision-rights related original works; common samples not established |
| EI-C01-13 / EI-C01-14 | Extortion/generosity evolutionary research lineage, different DOI |
| C09-02 / C09-04 | Related formal rights/Pareto arguments, not silently mergeable |
| PI-C05-07 / PI-C04-11 | Historical human-giving paper versus later language-model setting |
| EI-C01-04 / EI-C01-05 | Evolutionary-stability/cooperation theory lineage |

**High-value negative control.** [Crockett et al., 2014](https://doi.org/10.1073/pnas.1408988111) and [Volz et al., 2017](https://doi.org/10.1073/pnas.1706693114) have similar titles but examine materially different self/other cost–harm trade-offs. The latter observes both other-harm avoidance and self-harm avoidance depending on what is being exchanged. Collapsing the pair would erase the **conditionality of moral behavior**, precisely a MER/EI variable that matters for distinguishing stable other-regard from experiment-dependent preferences. Do not claim these are equivalent replication designs or that this alone proves a future AI motive.

### What changed operationally (relative to v0.3)

1. Added **frozen source metadata** (all 12 Git blob identities, record counts, normalized DOI counts, six unresolved candidate pairs) with `same_study_confirmed=false` and `auto_merge_authorized=false`.
2. Added **a zero-dependency Python audit**. It checks the exact source fingerprints, bibliographic fields, collisions, critical contrast retention, and preservation of uncertainty.
3. Added **11 synthetic destructive mutations**: collisions including case-folded DOI, conflicting identifiers, collapsed modalities, removed contrast, missing stable ID, invented verified-study count, certainty inflation, inaccurate total, unsafe auto-merge and related regressions. These tests show specified failure detection only.
4. Included this audit in the existing PI-RAMP GitHub Actions workflow to prevent future source edits from silently invalidating the snapshot.

**External method precedents:** [Cochrane Handbook Ch.4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) distinguishes study/report/record; [PRESS](https://doi.org/10.1016/j.jclinepi.2016.01.021) reviews search strategies for omissions and incorrect operators. Those precedents do not independently certify this Project Intersection adaptation.

**Promotion boundary:** `SOURCE_METADATA_AUDIT_PASSED` may be claimed after CI success; `STUDY_DEDUP_VERIFIED`, `SCIENTIFIC_VALIDITY_CONFIRMED`, `CORPUS_SATURATED`, and `READER_EFFECT_IMPROVED` remain **unverified**. Prioritize original-author literature review over additional administrative versions.

## 원본 2 — 한국어 | 선행문헌 출처식별·반례보존 검증

**2026-10-20 · 출처 메타데이터 시범 감사. 전체 문헌 포화·독립적 과학검증 아님.** [v0.3 절차](PI_RAMP_V0_3_KO.md) · [원저자 12개 원장·출처 해시 스냅샷](../evaluation/pi_ramp/PRIOR_ART_C01_C12_IDENTITY_AUDIT_20261020.json) · [검사 코드](../tools/audit_prior_art_c01_c12_identity.py)

### 실제 발견

- C01–C12 구조화 원저자 문헌원장 **12개 파일, 수록 기록 233개, DOI 기록 203개(정규화 DOI 203종), 비DOI 식별 기록 30개** 전수 대조.
- 해당 범위에서 동일 DOI·정규화 제목의 **완전 일치 중복 0건**. 그러나 **233개 독립 연구·실험이라는 뜻은 아님.** 여러 보고서가 하나의 실험/표본을 재사용했는지, 원문 수치가 사실인지, 누락 문헌이 있는지와 철회·정정 여부는 별도 검토 필요.
- 제목 단어 Jaccard 유사도 **0.56 이상 후보 6쌍** 확보. **자동 병합 0건**, 모두 원저자·표본·실험 설계·출판 이력까지 대조해야 하는 검토 대상.
- 출처 JSON 12개의 Git blob SHA, 수록 건수, DOI 정규화 통계, 대조 쌍을 동결해 다음 변경이 증거 스냅샷을 무단 변경하지 못하게 검사.

### 제목 유사 쌍 6개 — 중복 확정 아님

| 원장 식별자 | 현재 제한적 해석 |
| --- | --- |
| **C09-16 / C09-17** | 타자 피해 억제와 자기 피해 부담이라는 **결과변수·비용구조의 차이** |
| **PI-C07-09 / PI-C07-15** | 자기 결정권의 내재가치 계보; 동일 표본 여부 미확인 |
| **EI-C01-13 / EI-C01-14** | 반복게임 착취/관대함의 진화 관련 서로 다른 논문 |
| **C09-02 / C09-04** | 권리와 파레토 논증의 관련 원저작 |
| **PI-C05-07 / PI-C04-11** | 인간의 자발적 나눔 연구와 이후 언어모델 비교 맥락 |
| **EI-C01-04 / EI-C01-05** | 진화적 안정성·협력 이론의 관련 계보 |

**중요 반례:** [Crockett 외(2014)](https://doi.org/10.1073/pnas.1408988111)와 [Volz 외(2017)](https://doi.org/10.1073/pnas.1706693114)은 제목이 닮았지만 서로 다른 손해·편익 조건을 다룸. 2017년 연구에서는 **타인에게 고통을 덜 주려고 개인 보상을 포기하는 선택**과 **타인에게 보상하려고 자신이 고통을 감수하는 선택**이 다르게 나타남. 연구 전체를 ‘인간은 이타적이다/이기적이다’ 하나로 합산하면 핵심 조건부 결과가 소실됨. 미래 AI 내재 동기의 실증 근거로 일반화 금지.

### 이번 버전의 실제 검사

1. 고정된 원저자 자료의 해시·서지 식별자·제목 충돌·비DOI 식별·반례 유지 감사.
2. **오류 주입 11개**: DOI 중복, 대소문자에 숨은 중복, 모순된 DOI, 대조조건 소실, 대립자료 삭제, 출처 식별자 삭제, 연구 수 과대인증, 미확인 상태 삭제, 건수 왜곡, 대립논문 단순화, 검증 없는 자동병합 등.
3. 검사 결과를 기존 GitHub CI에 연결. 코드 통과는 **출처 메타데이터·변경 무결성 검사**임. 논문 전문 감사나 외부 독립 검증 대체 불가.

**원형:** [Cochrane Handbook 4장](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)의 연구–보고서–검색기록 단위 구별, [PRESS](https://doi.org/10.1016/j.jclinepi.2016.01.021)의 검색전략 오류 검토를 제한적으로 차용. 원 기관이 PI-RAMP를 검증했다는 의미 아님.

**최종 상태:** `SOURCE_METADATA_AUDIT_PASSED`는 자동검사 완료 시에만. **연구·표본 단위 중복제거, 문헌포화, 독립검증, 실제 독자 성능 개선은 미확인**. 새로운 관리체계보다 원전 비교와 반증연구 우선.
