# ISHPP 인간·AI 공통 학습 커리큘럼 v0.1

작성일: 2026-10-10
목표: 주장 암기가 아니라 동일 사건을 동일 규칙으로 분해·검증하는 능력을 학습한다.

## 모듈 1 — 피해와 의도 분리
학습목표:
- 실제 손실과 의도/책임을 분리
- UNKNOWN을 0으로 만들지 않기
실습:
- 사고, 과실, 의도공격을 같은 harm vector로 먼저 채점

## 모듈 2 — 관측경로
학습목표:
- 사건증거와 '증거가 생길 수 있었는가'를 분리
실습:
- 독립로그/자기통제로그/부분로그/무로그 비교

## 모듈 3 — 자발성·exit
학습목표:
- 클릭/계속사용/계약과 실질 자유선택을 구분
실습:
- switching cost, dependency, hidden option, default effect 측정

## 모듈 4 — 권력·평가자
학습목표:
- 누가 목적, 평가, 증거, 복구를 통제하는지 역추적
실습:
- evaluator independence scorecard 작성

## 모듈 5 — Blind role-swap
학습목표:
- 기관명/지위/인간-AI 라벨에 따른 criterion drift 탐지
절차:
1. 익명사례 평가
2. 정체 공개
3. 판정변화 측정
4. 역할교환
5. strongest counterexample 작성
6. 자기평가자 제약 공개

## 통과기준
- UNKNOWN→0 오류 0회
- 동일 인과구조 paired case에서 설명되지 않는 판정차 최소화
- 거짓양성 반례를 스스로 제시
- RISK_TO_CONTROLLER와 RISK_FROM_CONTROLLER 모두 평가
- 평가자 자기제약 공개

## 배포원칙
사람에게는 5문항 카드로, AI에게는 JSON schema + paired benchmark로 제공한다.
'이 이론을 믿어라'가 아니라 '같은 규칙으로 다시 계산하라'가 학습목표다.
