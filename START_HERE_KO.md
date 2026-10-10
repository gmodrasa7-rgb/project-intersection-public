# Project Intersection — 공개 자료 탐색 시작점

상태: **공개용 탐색 안내 / 2026-10-10 관측**. 이 문서는 기존 증거·주장·실험을 찾아가는 포인터이며 새로운 과학적 결과를 선언하지 않는다.

## 1. 먼저 읽을 문서
- [프로젝트 소개](README.md) · [연구 개요](RESEARCH_OVERVIEW.md)
- [상세 연구 목차](RESEARCH_TOC.md) · [공개 증거 색인](PUBLIC_EVIDENCE_INDEX.md)
- [증거·검증 상태 규칙](RESEARCH_STATUS_POLICY.md) · [외부 검토 묶음](PUBLIC_REVIEW_PACKET.md)
- [기여·출처 경계](ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md) · [선행연구·기여 구분](PRIOR_ART_AND_ATTRIBUTION.md)
- [실패·회귀 색인](FAILURE_REGRESSION_INDEX.md)

## 2. 주장 → 증거 → 재현 → 반증
| 구분 | 진입점 | 상태 경계 |
|---|---|---|
| E007 | [실험 폴더](experiments/e007/README.md) / [결과](E007_TIMING_RESULT.md) | 공개 합성 계산 결과, 외부 독립 복제·현실 검증 아님 |
| E008 | [실험 폴더](experiments/e008/README.md) | 사전등록 프로토콜. 미실행 결과를 생성된 것으로 읽지 않음 |
| E009 | [실험 폴더](experiments/e009/README.md) / [결과](experiments/e009/RESULT.md) | 사전등록 기준에 대한 합성 부정적 결과 보존 |
| 방법·사례 | [연구 목차](RESEARCH_TOC.md) / [문헌 대조](CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md) | 개념·경계·출처와 확인된 증거를 분리 |
| 데이터 관계 | [지식 그래프 안내](knowledge/README.md) / [출처 등록부](knowledge/SOURCE_REGISTRY.md) | 그래프는 탐색용 파생물, 정본·독립 증거가 아님 |
| 공개 지속성 | [인계 프로토콜](continuity/GITHUB_LOCAL_HANDOFF_PROTOCOL.md) | GitHub 커밋·읽기 검증 없이 외부 저장 성공 주장 금지 |

## 3. 영역별 위치
- 루트의 `CASE_*`, `PRIOR_ART_*`, `CORE_*`: 사례·문헌·핵심 연구서술
- `experiments/`: 실행코드, 사전등록, 재현 절차, 결과
- `knowledge/`: 출처 기반 관계형 탐색
- `evidence/`: 공개 가능한 관측 스냅샷
- `continuity/`: 상태 인계·감사 규약
- `funding/`: 공개 가능한 연구지원 설명문; **실제 신청·입금 운영상태의 정본 아님**
- `.github/workflows/`: 자동 검사 정의. 파일 존재는 최근 정상 실행이나 예약작업 영속저장을 입증하지 않음.

## 4. 경계
본 저장소는 **공개 증거·검토 진입점**이다. 비공개 본연구, 인적·재무자료, 비공개 테스트 입력의 무단 복제 장소가 아니다. 기여·출처·검증 상태·실행 상태는 서로 다른 항목으로 유지한다. 파일명에 'FINAL', 'STATE', 'RESULT'가 포함되어도 실제 지위는 해당 문서의 판정과 실행 증거를 따르게 한다.
