# E051 공개 실증 전환 게이트 — 사전 결과 없는 Phase 0

**상태:** 공개 프로토콜 / NOT EXECUTED / NO EMPIRICAL RESULT. E048–E050의 합성 결과를 현실 공존·포획 법칙으로 해석하지 않는다. 본 문서는 비공개 연구의 측정 논리를 공개용으로 재작성한 것으로, 미공개 원문이나 데이터를 복사하지 않았다.

## 질문과 경쟁모형
H0 정적 충분성: 현재 R&D·자원·규모·산업/연도 정보만으로 다음 생성성과를 설명할 수 있다.
H1 경로의존 추가정보: 현재 정보 통제 후에도 과거 지식 stock이 out-of-sample 예측력을 개선한다.
Phase 0은 **데이터 생존성**만 검사한다. H1 자체를 시험하지 않는다.

## 공식 공개원천
- U.S. SEC, EDGAR Data APIs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces (submissions, companyfacts, nightly bulk; 공개 읽기 API는 인증키 불필요).
- U.S. USPTO, PatentsView: https://www.uspto.gov/ip-policy/economic-research/patentsview (ODP 이관; annualized data 2025-12까지).
- USPTO 2026-06-17 annualized update: https://www.uspto.gov/subscription-center/2026/june-17-new-update-patentsview-annualized-datasets

**주의:** SEC companyfacts는 non-custom taxonomy entity-wide facts만 집계. R&D 표준태그 부재는 R&D=0이 아니다. USPTO annualized 자료의 필드 지원 범위를 확인하기 전 품질가중 특허지표를 만들지 않는다.

## P0-A SEC 관측가능성
기업×회계연도별 us-gaap ResearchAndDevelopmentExpense, 매출, 자산, 현금, 부채의 tag coverage, 기간/통화 단위, 중복 filing, restatement, 산업·규모·연도별 결측 편향을 먼저 기록. R&D 결측→0 대체 금지. 관측 기업만 남긴 선택편향을 명시.

## P0-B USPTO 관측가능성
연도별 assignee-특허 건수·기술분야 필드·기간 coverage를 확인. grant-year와 application-year를 혼동하지 않는다. 특허 건수는 혁신 전체가 아니며 산업별 특허성향·조직명 해소 오류가 있다. 특허 품질/인용지표는 필요한 bulk 필드·판본이 검증되기 전 HOLD.

## P0-C 기업 식별
CIK↔assignee는 현재·과거 법인명과 USPTO disambiguated organization을 사용해 **결과변수 확인 전에** 규칙 고정. unique/ambiguous/no-match 비율과 matched vs unmatched selection 차이를 기록. M&A, 자회사, 상호변경은 자동 동일기업 취급 금지.

## P0-D 시간누수·기본비교
회계연도 t의 입력으로 t+1 이후 정보를 사용하지 않는다. 무작위 분할을 기본으로 하지 않고 rolling-origin 또는 past→future split. 이후에만 static(current R&D+controls) vs dynamic(static+lagged patent stock)을 같은 표본·분할에서 비교한다. negative control 1개를 결과 보기 전 지정.

## 중단/보류
(1) 표준태그 coverage가 낮거나 체계적으로 편향, (2) 기업 매핑 모호성 지배, (3) 필수 특허필드 부재, (4) 미래정보 누수, (5) 충분한 패널 연속성 부재 → **HOLD**, 현실 경로의존 결과 주장 금지. Phase 1에서도 동적 모형이 out-of-sample에서 개선되지 않으면 넓은 H1을 약화한다.

## 금지되는 외삽
R&D ≠ 모든 생성행동; lobbying/시장집중 ≠ 자동 포획; 특허 stock ≠ 모든 옵션가치; 예측력 ≠ 인과효과; G/H 검증 ≠ A/K 포획·시점 이력효과·재귀수익 차단 검증. 인간·AI 보편 법칙 주장 금지.

## 결과 제출 인터페이스
후속 공개 결과는 `data_snapshot_date, source_version, unit_count, firm_year_count, coverage_by_tag, unmatched_rate, ambiguous_rate, time_split, leakage_audit, negative_control, baseline_metric, dynamic_metric, code_commit, independent_reproduction_status`를 포함한다. 아직 모두 **NOT MEASURED**.

원천·기여 귀속: SEC와 USPTO는 공공 데이터 원천·관리기관이며, Project는 연구 질문·측정설계의 출처만 별도로 표시한다. 제3자의 연구방법을 Project 독창성으로 주장하지 않는다.


## 2026-10-09 경쟁가설·측정범위 보정
비공개 E051 측정 스키마의 기존 사전고정 조건을 반영한다. H0 정적 흐름 충분성, H1 역사 stock의 **부호 제한 없는** 추가 예측력, H2 음의 경로의존, H3 기업 고정 이질성, H4 특허성향/측정기계 설명을 경쟁시킨다. 동일한 특허자료로 H와 Y를 구성할 때 기계적 자기상관을 반드시 점검한다. 동적 예측 개선은 인과적 지식축적이나 전체 혁신의 증거가 아니다.

**외부 원천 확인:** SEC companyfacts는 비표준 기업별 taxonomy 전체를 포함하지 않으며 R&D 태그 부재는 0이 아니다. USPTO PatentsView annualized data는 2025년 12월까지 갱신되었고, 조직명 disambiguation 자체에 측정오류 가능성이 있다. 출처: https://www.sec.gov/search-filings/edgar-application-programming-interfaces ; https://www.uspto.gov/ip-policy/economic-research/patentsview .

**실행상태:** 공식 API와 데이터 제공범위는 문서로 재확인했지만, 기업별 SEC/USPTO 원자료 다운로드·매칭·결측률 산출은 이 작업에서 실행하지 않았다. Phase 0은 계속 NOT EXECUTED이다.
