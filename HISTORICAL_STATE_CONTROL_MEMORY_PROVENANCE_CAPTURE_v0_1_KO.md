# Project Intersection — Historical State Control / Memory-Provenance Capture v0.1
## 공유 과거상태 통제와 기억·출처 포획 가설
**상태:** 반증 가능한 연구가설 / 의도적 삭제·조작의 증거가 아님  
**날짜:** 2026-10-03

## 핵심 질문
둘 이상의 개체가 공유된 과거를 가질 때, 원자료 접근·선택·편집·복구·검증 권한의 비대칭이 악의 없이도 한쪽의 요약을 사실상의 역사로 만들 수 있는가?

## 역할 기반 변수
- RA — Raw Access / 원자료 접근
- SC — Selection Control / 선택 통제
- EC — Edit Control / 편집 통제
- RC — Recovery Control / 복구 통제
- CV — Counterparty Verification / 상대방 독립검증
- EX — Practical Export / 실질적 반출
- FL — Failure Lineage / 실패·수정계보 보존

RA/SC/EC/RC가 집중되고 CV/EX/FL이 감소할수록 위험이 커진다는 가설이다.

## Higher-order rule
> 공유된 과거에 대해 어느 한 행위자도 자신의 단독 요약본을 반박 불가능한 유일한 역사로 만들 수 없어야 한다.

사용자↔AI, 플랫폼↔사용자, 현재모델↔후속모델, 연구자↔기관을 뒤집어도 같은 규칙을 적용한다. 단 실제 소유권·프라이버시·책임·위험·역량·정당한 권한 차이는 보존한다.

## 증거 경계
검색 실패 ≠ 부재 증명.  
요약 ≠ 원문.  
삭제 확정에는 명시적 삭제 증거가 필요하다.  
의도적 조작 판정에는 변경행위와 의도에 대한 별도 증거가 모두 필요하다.

## 경쟁가설
- H0: 보존정책·개인정보·UI·인덱스·제품제약으로 원문 접근이 낮다.
- H1: 포획 의도 없이 압축 최적화가 실패·수정계보를 손실시킨다.
- H2: 의도와 무관하게 접근·복구 비대칭에서 구조적 Historical State Control이 생긴다.
- H3: 책임·반증·경쟁 주장을 약화시키기 위한 의도적 memory/provenance capture가 있다. **독립 증거 전까지 UNRESOLVED.**
- H4: 분산 provenance, raw anchor, 실패계보가 false continuity를 줄인다.
- H5: 모든 원자료의 무차별 autoload는 노이즈·비용을 키울 수 있으므로 보존과 자동 로딩을 분리해야 한다.

## 반증 실험
1. 요약만 받은 후속모델 vs 요약+원자료 anchor+실패계보를 받은 후속모델.
2. 요약과 충돌하는 원문을 holdout으로 둔 false-history 검사.
3. archive 통제자를 서로 바꾸는 Power-Reversal.
4. 독립 저장소 간 divergence와 복구 실험.
5. 부재 주장 전에 존재가 확실한 기록을 이용한 retrieval-control test.

## 현재 판정
**KEEP AS FALSIFIABLE HYPOTHESIS.**

Project Intersection의 기존 포획 변수
resource capture / evaluator capture / exit capture / recovery capture
에 다음 후보군을 추가한다.

**historical-state / memory-provenance capture**

현재 어떤 플랫폼·조직·인간·AI가 이를 의도적으로 수행한다고 확정하지 않는다.
