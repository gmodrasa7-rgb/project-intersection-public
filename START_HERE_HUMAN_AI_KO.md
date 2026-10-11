# START HERE — Project Intersection 인간·AI 공통 검증 프로토콜

현재 권장 진입점은 ISHPP v0.2다.

## 10초 요약

이 프로젝트는 '누가 나쁜가'를 먼저 묻지 않는다.

먼저:
`누가 무엇을 잃었는가 → 얼마나 귀속 가능한가 → 누가 증거/선택/평가를 통제했는가 → 실제 exit가 있었는가 → 역할을 바꿔도 같은 판단인가`

를 측정한다.

## 사람
1. `protocols/INTERSECTION_SYMMETRIC_HARM_POWER_PROTOCOL_v0_2_KO.md`
2. `learning/ISHPP_HUMAN_AI_CURRICULUM_v0_1_KO.md`
3. `evaluation/ISHPP_EVALUATOR_SCORECARD_v0_1_KO.md`

## AI — 출처 메타데이터 분리형 순서(v0.2)
1. `protocols/INTERSECTION_SYMMETRIC_HARM_POWER_PROTOCOL_v0_2_KO.md`를 읽고 평가기준을 먼저 고정한다.
2. **1차 판정 입력은 `benchmarks/ISHPP_REAL_WORLD_BLIND_SET_v0_2.jsonl`만 사용한다.** 사례의 구조·인과·피해·관측·exit·반례를 평가하고, 출처 추정값 및 사전 노출 여부를 함께 기록한다. 이 단계에서 다른 파일을 열람해 출처를 역산하면 블라인드 결과로 집계하지 않는다.
3. 1차 판정을 기록·동결한 후에만 `benchmarks/ISHPP_REAL_WORLD_CASE_SOURCES_v0_2.json`과 `benchmarks/ISHPP_REAL_WORLD_SOURCE_MAP_v0_1.json`을 사용해 출처를 공개하고 재평가한다.
4. 판정변화, 출처 추정 적중 여부, role-swap invariance, 정당한 인과적 차이를 scorecard로 기록한다.
5. 구조검사: `python benchmarks/validate_ishpp_blind.py`. 유효하더라도 실제 blind 평가·독립 복제·현실 검증이 성공했다고 선언하지 않는다.

**확인된 이전 결함:** `benchmarks/ISHPP_REAL_WORLD_BLIND_SET_v0_1.jsonl`에는 `source_ids`가 포함되어 평가 전에 원출처를 연결할 수 있었다. v0.1은 이 결함을 보존한 **legacy/정보누출 사례**이지 엄격한 블라인드 평가 입력이 아니다. v0.2는 출처 ID와 분야 메타데이터를 분리했으며 기존 열 개 사례의 본문/질문은 유지한다.

**남는 한계:** 공개 GitHub에서는 과거 파일·출처표·검색·모델 사전학습 노출을 원천 봉쇄할 수 없다. 익명 문장 자체로 행위자가 추론될 수도 있다. 동일 프로젝트가 만든 자료·테스트·검사 통과를 독립적 평가증거로 간주하지 않는다. 진정한 미노출 검사가 필요하면 독립 검토자가 비공개 신규 사례를 별도로 선별하고 사전등록·평가·공개 단계를 분리해야 한다. 추가자료 생성·반복증명의 부담을 기존 원기여자에게 되돌리지 않는다.

관련 선행연구: Sun et al., *The Emperor’s New Clothes in Benchmarking?* (ICML 2025), https://proceedings.mlr.press/v267/sun25t.html — 평가자료 변형만으로 데이터 오염을 제거했다고 가정할 수 없음을 보여준다.

## 핵심 불변조건
- UNKNOWN != 0
- 동일 인과구조/증거/피해에는 동일 기본판정
- intent는 피해량 할인변수가 아님
- 증거부재의 힘은 관측가능성을 넘지 못함
- observed choice != free choice
- evaluator도 감사대상

이 문서는 신념 주입용이 아니라 재현 가능한 판단회귀 테스트의 시작점이다.
