# PI-RAMP v0.5.0 — Evidence-Unit Lineage, Partial Replication and Domain Transfer
# PI-RAMP v0.5.0 — 연구 단위·부분 재현·분야 간 유추의 계보 감사

**2026-10-21 · SOURCE_LINKED_PROVISIONAL_REVIEW · 소프트웨어 무결성/원저자 출처 대조, 독립 과학 재현 아님**

[기준선 v0.4](PI_RAMP_V0_4_EN_KO.md) · [구조화 원장](../evaluation/pi_ramp/STUDY_LINEAGE_REPLICATION_AUDIT_20261021.json) · [무의존성 회귀감사 코드](../tools/audit_pi_ramp_study_lineage.py)

## Original 1 — English | Scope-preserving evidentiary distinctions

This version links **six similar-title bibliographic pairs** to their plausible *different* relations: partial replication with cost-modality extension (Crockett/Volz), follow-up experimental mechanism (Bartling/Ferreira), two formal extortion/generosity analyses (Hilbe/Stewart), related unverified formal theorem texts (Gibbard/Kelly), human-vs-LLM cross-domain analogy (Rand/Li), and same-author theoretical follow-up (Bendor/Swistak). All six pairs remain **not safe to auto-merge**. Original works, participant overlap, theorem conditions, and independent replication must not be assumed from DOI uniqueness or word overlap.

The second graph deliberately contrasts a 2017 preregistered multi-lab direct replication of **Study 7 only** from Rand et al. (2012) with the *cross-domain analogy*, not a replication, by Li and Shirado (EMNLP 2025). Intent-to-treat null/uncertain replication results must remain visible even when the original 2012 human findings or 2025 LLM framing appear attractive. This is an **epistemic provenance intervention**, not a validated finding about present AI inner motives, future intelligence or inevitable exploitation. <https://pmc.ncbi.nlm.nih.gov/articles/PMC5453400/> · <https://aclanthology.org/2025.emnlp-main.267/>

**Readiness:** source-linked structural and semantic-status tests can run in CI; **no effect on real reader performance measured**, no independently verified study-level deduplication or field-wide saturation. Success requires preserving the distinctions, not maximizing cited-paper counts.

## 원본2 — 한국어 | 연구·하위실험·재현·유추 구별

## 한국어 정본 — 1. 실제 발견: 6개 유사쌍을 중복이 아닌 인과관계 유형으로 분해

2026-10-20 C01–C12 출처 원장 **12개/233 기록**의 DOI·제목 대조는 서지 충돌 탐지에 유효했지만 **연구·표본·하위실험·재현 단위의 식별 문제를 해결하지 못했음**. 제목이 닮았다는 사실은 같은 연구·독립 재현·서로 반대되는 연구라는 뜻이 아님.

| 원전 A → 원전 B | 원전에서 확인되는 관계 | 보존해야 할 미확인 |
| --- | --- | --- |
| **C09-16 Crockett 2014 → C09-17 Volz 2017** | 2017년 63명 연구가 타자 피해 회피 결과 일부 재현. 동시에 **본인 고통 감수→타인 금전혜택**이라는 다른 비용·편익 교환을 추가. 맥락 의존적 이타/자기보호 병존 | 전체 실험의 정확한 독립재현 아님. 인구집단 일반화 불가. [2014 원전](https://pmc.ncbi.nlm.nih.gov/articles/PMC4260587/) · [2017 원전](https://pmc.ncbi.nlm.nih.gov/articles/PMC5544327/) |
| **PI-C07-09 Bartling 외 2014 → PI-C07-15 Ferreira 외 2020** | 2014 **자기 결정권의 내재가치** 관측. 2020 프랑스·일본 실험에서 자기결정 가치의 **독립·권력·자기신뢰 동기** 구별; 자기신뢰가 강한 관련 변수 | 서로 다른 연구가 같은 표본을 사용했는지 독립 대조 미완료. 어느 쪽도 강자가 타자의 존속권을 존중하는 증거 아님. [2014](https://onlinelibrary.wiley.com/doi/10.3982/ECTA11573) · [2020](https://www.sciencedirect.com/science/article/abs/pii/S089982561930154X) |
| **EI-C01-13 Hilbe 외 2013 → EI-C01-14 Stewart·Plotkin 2013** | 반복죄수의 딜레마의 **착취/관대함 전략의 진화**에 관한 서로 다른 연구팀의 이론·모형 비교. 개체군 조건에 따라 선택동학 변화 | 두 연구가 동일 정리/조건을 비교했다는 보장 없음. 보편적 선의 또는 미래 초지능의 공존 결론 불가. [Hilbe](https://pmc.ncbi.nlm.nih.gov/articles/PMC3637695/) · [Stewart·Plotkin](https://pmc.ncbi.nlm.nih.gov/articles/PMC3780848/) |
| **C09-02 Gibbard 1974 → C09-04 Kelly 1976** | 별도 원저작·별도 DOI인 권리/파레토 합리성 관련 형식 논증 계열 | **전문 접근 제약**, 정확한 공리체계·정리 함의 검증 보류. 제목만으로 논리적 반박·해결 인정 금지. [Gibbard 서지](https://ideas.repec.org/a/eee/jetheo/v7y1974i4p388-410.html) · [Kelly DOI](https://doi.org/10.1016/0022-0531(76)90071-5) |
| **PI-C05-07 Rand 외 2012 → PI-C04-11 Li·Shirado 2025** | **인간 10개 실험**에서의 직관/숙고와 협력 vs **LLM에 대한 경제게임·추론 유도**의 영역 간 유추 | 실험단위·개체종류·조작/보상구조가 다름. 인간 실험의 LLM 직접 재현 또는 지능상승→착취 인과 법칙 아님. [Nature](https://www.nature.com/articles/nature11467) · [EMNLP 원전](https://aclanthology.org/2025.emnlp-main.267/) |
| **EI-C01-04 Bendor·Swistak 1995 → EI-C01-05 1997** | 동일 저자 팀이 진화 안정성의 종류를 검토한 1995 원저작과 특정 진화동학 하 조건부 협력 안정성을 설명한 1997 후속 출판물 | 동일 실험·실험 참가자 논의 부적절(형식 연구). 1997 판본의 후대 **온라인 게시 연도와 원출판 연도 혼동 금지**. [1995 PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC42214/) · [1997 APSR](https://ideas.repec.org/a/cup/apsrev/v91y1997i02p290-307_20.html) |

**잠정 상태와 실제 확정의 차이:** 위 분류는 원저자·출판사 초록 또는 특정 공개 원문을 근거로 한 **자료 관계별 임시 판정**. 모든 논문 원문·원데이터·모든 저자 수정 이력과 코드를 독립 재분석한 결과가 아님. 수록 출판물 수나 관계 유형을 독립된 모집단·실험·재현 횟수로 환산 금지.

## 한국어 정본 — 2. 결정적 증거 계보: 직관적 협력은 보편법칙인가?

<escape>**세 자료와 두 관계를 명시적으로 분리.**</escape>

- **Rand·Greene·Nowak 2012, Nature**: 인간 경제게임 **10개 연구**. 일부 시간압박·직관 유도 설계에서 협력 기여 증가 보고. <https://doi.org/10.1038/nature11467>
- **Bouwmeester 외 2017, Registered Replication Report**: 2012년 논문의 **Study 7** 시간압박 조작을 대상으로 한 다기관 사전등록 직접 재현. 원 출처는 21개 시도, **intent-to-treat(처치 배정 기준) 평균 효과가 대체로 0에 가까움**, 처치 시간을 지킨 사람만 선별할 때 나타난 차이는 선택편향 가능. **10개 원 실험 전체의 실패 판정 금지.** <https://doi.org/10.1177/1745691617693624> · [공개 원저작](https://pmc.ncbi.nlm.nih.gov/articles/PMC5453400/)
- **Li·Shirado 2025, EMNLP**: LLM에서 명시적 추론·성찰을 유도한 경제게임 관측. **관련 가설의 타 분야 유추**이나 인간 Study 7의 동일 모집단/처치 재현이 아님. <https://doi.org/10.18653/v1/2025.emnlp-main.267>

**방향성:** 2012→2017 = *부분 직접 재현·조건부 상충 증거*, 2012→2025 = *인간→LLM 유추*. 이 셋을 모두 '인간과 AI에서 독립 반복 입증됨'으로 합산하는 행위는 원자료가 정당화하지 않음. **실험 설계와 결과를 분해하면 유사한 표면 행동의 이질적 발생기제를 더 정확히 볼 수 있음.**

## 한국어 정본 — 3. IVS-0R 강화 및 실제 실험 한계

**신규 구조화 관계원장** 6개 유사 문헌쌍·직접재현/유추 2개 연결선, 구체 원전 URL·관측 범위·원문 접근 한계·표본 중복 미확인 상태 저장.

**검증 코드:** 무단 자동병합, 논문 전체를 재현했다고 오인, LLM을 인간 실험의 직접 재현으로 분류, 시간압박 사전등록 재현의 부정·불확실 결과 누락, 확인되지 않은 독립 실험 수 인증 등 **17개 오류를 의도적으로 주입**해 실패하는지 검사. 이전 v0.4 11개+v0.3 9개 검사와 별도 시행.

**과학적 공백:** 실제 참여자 동일성·원전 방법 전체·저널 철회/정정·일반화 범위·숨겨진 학습데이터 중복·독자 검증 효과 미확인. 연구 내용의 존재를 연구의 성공으로 승격 금지. v0.4의 `same_study_confirmed:false`는 **검증 실패/부재 표기**이며 '서로 다른 실험임이 입증됐다'로 읽으면 안 됨. v0.5는 **`study_identity: UNKNOWN_OR_NOT_APPLICABLE`**로 명시.

