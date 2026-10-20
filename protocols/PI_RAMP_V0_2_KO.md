<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: protocols/PI_RAMP_V0_2_EN.md -->
# PI-RAMP v0.2.0 — 연구자료실 재귀개선 메타프로토콜

**원본2 — 한국어 | 2026-10-20 | 상태: 선행 모범사례 기반 설계안·시험 도입, 독립적 효과 검증 이전**

[영어 대응판](PI_RAMP_V0_2_EN.md) · [연구 정본 지도](../navigation/RESEARCH_PROGRAM_KO.md) · [최초 적용 사례 PR #236](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/236)

## 목적·범위·비목적

PI-RAMP(Project Intersection — Research Archive Meta-Protocol)는 **연구의 지식·근거·반례를 발견·검증·재사용하기 쉽게 만드는 자료실 개선 작업 자체를 측정하고 재귀적으로 교정하는 절차**다. 핵심 성과는 문서 양이나 자동검사 통과가 아니라 **정확한 원저자 근거의 발견, 주장–근거 추적, 실패/모름 노출, 실제 이용자의 판단 오류 감소**다.

연구 이론의 진실성, AI 내면 상태, 인간/AI의 권리, 외부 독립검증 또는 문헌 포화를 이 절차의 문서/CI 검사만으로 승인하지 않는다. 기존 연구 원본·부정 결과·기여·권리 기록의 무단 삭제와 저자 기여의 재표시는 금지.

## 1. 선행 모범사례 — 원래 목적과 이식 한계

| 원형·원전 | 적법한 이식 | 이식하면 안 되는 결론 |
| --- | --- | --- |
| [Cochrane Handbook, Ch.4 (2025)](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) | 기록(record)–보고서(report)–연구(study)를 구별. 여러 보고서를 묶되 연구를 이중 계산하지 않음; 철회·정정 확인 | 논문 DOI 수가 독립된 연구 수라는 가정 |
| [PRISMA 2020](https://www.prisma-statement.org/prisma-2020)·[PRISMA-S (2021)](https://www.equator-network.org/reporting-guidelines/prisma-s/) | 검색식·검색일·DB·선별/제외 이유·갱신 경로의 재현가능한 보고 | 체크리스트 작성만으로 탐색의 완전성 또는 연구 품질 승인 |
| [Cochrane living review](https://methods.cochrane.org/news/new-updated-guidance-cochrane-living-systematic-reviews) | 핵심 주장에 영향을 주는 신규·철회·수정된 원전 감시 및 필요시 근거 갱신 | 새 논문 한 편이 나올 때마다 무조건 전체 자료실 개편 |
| [FAIR (Wilkinson 외, 2016; DOI:10.1038/sdata.2016.18)](https://doi.org/10.1038/sdata.2016.18) | 발견성·접근성·상호운용성·재사용성, 지속 식별자·메타데이터 | FAIR가 내용의 참 또는 인과 식별성을 보증 |
| [W3C PROV (2013)](https://www.w3.org/TR/prov-primer/) | 원전·파생 주장·개편 행위·기여 주체·버전 사이의 생성/인용/변경 계보 | 출처가 기록됐다는 이유로 근거의 신뢰성 승인 |
| [Diátaxis](https://diataxis.fr/start-here/) | 처음 읽기, 작업방법, 정본 참조, 논리적 설명을 서로 다른 독자 과제로 분리 | 실제 독자 문제 없이 디렉터리만 4분할 |
| [NASA configuration management](https://www.nasa.gov/reference/6-5-configuration-management/) | 변경 전 기준선, 변경요청, 영향 범위, 동결/승격, 원본·복구점 | 대형 조직의 승인 관료제를 그대로 복제 |
| [Google SRE postmortems](https://sre.google/workbook/postmortem-culture/) | 개편 실패의 관측·원인·재발방지·남은 위험 기록; 책임추궁이 아닌 학습 | 실패를 지웠거나 사람을 비난해야 개선된다는 생각 |
| [DORA metrics](https://dora.dev/guides/dora-metrics/) | 처리량만이 아니라 실패·회복·안정성을 함께 측정 | 배포 빈도가 높으면 연구가 진실에 가까워졌다는 주장 |
| [The Turing Way](https://book.the-turing-way.org/reproducible-research/reproducible-research/) | 원본·코드·환경·검증 단계를 다시 수행할 수 있도록 기록 | 재현 가능한 합성 계산을 현실 적용 성공으로 승격 |

**출처 경계:** Cochrane/PRISMA의 원 분야는 주로 체계적 문헌고찰, DORA/SRE는 소프트웨어 운영. 여기의 연구자료실 적용과 지표·게이트는 **PI-RAMP의 새로운 설계 제안**이며 해당 기관이 그 효과를 검증했다는 뜻이 아니다.

## 2. 재귀 실행: MAP → HYPOTHESIS → CHANGE → TEST → AUDIT → LEARN

1. **MAP (기준선):** main 커밋 SHA·버전, 현재 정본·역사자료·실패자료, 원저자/식별자·끊긴 링크·관측 불능을 기록. 이전 회차와 중복 탐색 방지.
2. **HYPOTHESIS (사전 개선가설):** 누가 무엇을 찾지 못하는가, 어느 변화가 어떤 오류를 줄일 것으로 예상하는가, 역효과는 무엇인가. 실행 전에 성공/실패 기준과 반증 시나리오 기록.
3. **CHANGE (최소 변경):** 독자의 실제 과제에 직접 연결되는 작은 개편 우선. 삭제보다 색인·별칭·이전 안내; 원본 저작권·기여 기록 불변. 근거를 모르는 변경은 잠정 표시.
4. **TEST (두 검사 분리):** (a) 자동: 링크·경로·언어판·정본·형식·CI, (b) 과제 기반: 새로운 독자가 '원전 찾기', 'E009 불리한 결과 확인', 'AI 내면 미입증 확인', '연구–보고 중복 구분'을 실제로 수행. 정답률·소요 시간·잘못된 확신·실패 경로를 수정 전/후 비교. **현재 측정값 없음.**
5. **AUDIT (IVS-0R):** 변경자가 자기검사를 한 기록과 독립 검토를 구분. 이익·권력 역전, 선택적 인용, 저자 누락, 부정결과 은닉, 미관측, 번역 의미 변화의 반례 점검. 독립 감사 부재 = `NOT_INDEPENDENTLY_VERIFIED`, 자동 PASS로 대체 금지.
6. **LEARN (결과 및 방법 개선):** 관측 효과·부작용·실패 원인·복구 가능성·다음 가설을 기록. 필요하면 PI-RAMP 절차 자체를 바꾸되 같은 게이트 적용. 관측 개선이 없거나 비용이 큰 구조개편은 중단/되돌림.

## 3. 표준 실행 영수증 (매회 필수 필드)

각 회차마다 아래를 **증빙 가능한 사실과 미측정 값을 구별**해 기록:

- `run_id`, `protocol_version`, `date_utc`, `base_commit`, `head_commit`, `pr_url`, `actor_role`
- `problem`, `reader_tasks`, `hypothesis`, `counter_hypotheses`, `predeclared_success_criteria`
- `source_ids`, `original_author_links`, `study_id`, `report_ids`, `excluded_with_reasons`, `retraction_check_status`
- `paths_added/changed/retained`, `negative_results_preserved`, `legacy_redirects_or_links`
- `structural_checks`, `before_after_task_evidence`, `independent_review_receipt_or_null`
- `unknowns`, `failure_modes`, `rollback_commit_or_plan`, `decision`, `next_hypothesis`

**연구 문헌 계수 단위:** `source_record_id` ≠ `report_id` ≠ `study_id` ≠ `unique_mechanism_or_counterexample`. DOI가 없는 역사자료도 별도 식별자를 부여하고, 동일 연구의 독립 복수 보고서는 보존·연결.

## 4. 검증 게이트와 상태

| 게이트 | 검사 | 실패 시 |
| --- | --- | --- |
| G0 원본·기여·안전 | 저작권·원저자·부정 결과·소급 기록 왜곡 여부 | 즉시 차단/수정 |
| G1 출처·식별 | 원문 경로·식별자·검색 이력·중복/철회 상태 | 주장을 확정 정본으로 승격 금지 |
| G2 구조·회귀 | 내부 링크·수정 범위·언어 분리·기존 CI | 병합 보류 또는 복구 |
| G3 독자 과제 | 사전 정의 과제에서 정확성·찾기 시간·오판/누락 비교 | `EFFECT_UNMEASURED` 또는 `NO_DEMONSTRATED_GAIN` |
| G4 비독립성 공시 | IVS-0R 반증·책임 분리·독립 검토 영수증 | 독립 검증 표기 금지 |
| G5 재귀 판단 | 과잉 구조화 비용·추가 노동·다른 연구 작업 침식 | 단순화·중단·되돌림 |

**상태:** `PROPOSED` → `PILOT` → `EFFECT_MEASURED`(증빙 있을 때만) → `INDEPENDENTLY_REVIEWED`(독립 영수증 있을 때만). `REJECTED`, `REVERTED`, `SUPERSEDED`, `UNKNOWN`은 지우지 않고 유지. CI PASS ≠ G3/G4 PASS.

**버전:** MAJOR = 기존 실행 영수증/인터페이스와 비호환; MINOR = 새 검증·추적 기능; PATCH = 의미 비변경 교정. 연구결과 버전·프로토콜 버전·실행 영수증 버전을 혼동하지 않음.

## 5. 최초 적용 및 다음 실험

- **RAMP-20261020-001, 사후 등록:** [PR #236](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/236)의 대문/정본 지도/독자 경로 정리. 7개 자동검사 통과는 구조적 사실. 사전 독자 과제·전후 소요 시간·외부 독립검토 영수증 **미확보**. 효과 `EFFECT_UNMEASURED`.
- **v0.2.0:** 위 선행사례를 PI-RAMP 절차에 최초 명문화. 아직 실사용 측정·독립 방법 검증 전. `PROPOSED_PILOT`.
- **다음 우선 실험:** 동등 난도의 4개 독자 과제를 사전 정의하고 기존/개편 자료실 스냅샷의 정확성·근거 경로·시간·과잉확신 측정. 평가자 및 난도 차이 기록. 결과가 없으면 효과 주장은 보류.
- **재귀 중단 규칙:** 신규 문서/절차가 반증 가능성 또는 독자 실제 과제 개선을 보여주지 못하고 유지보수 비용만 증가하면 새 층을 만들지 않는다. 본 연구의 원저자 논문 조사 시간을 우선 보호한다.
