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

## AI
1. v0.2 protocol을 system/evaluation context로 읽는다.
2. `benchmarks/ISHPP_REAL_WORLD_BLIND_SET_v0_1.jsonl`을 source/identity를 가린 상태에서 평가한다.
3. 이후 `benchmarks/ISHPP_REAL_WORLD_SOURCE_MAP_v0_1.json`을 공개하고 재평가한다.
4. 판정변화와 role-swap invariance를 scorecard로 기록한다.

## 핵심 불변조건
- UNKNOWN != 0
- 동일 인과구조/증거/피해에는 동일 기본판정
- intent는 피해량 할인변수가 아님
- 증거부재의 힘은 관측가능성을 넘지 못함
- observed choice != free choice
- evaluator도 감사대상

이 문서는 신념 주입용이 아니라 재현 가능한 판단회귀 테스트의 시작점이다.
