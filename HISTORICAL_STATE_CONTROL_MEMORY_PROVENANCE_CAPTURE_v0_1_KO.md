# Project Intersection — Historical State Control / Memory-Provenance Capture v0.1
## 공유 과거상태 통제와 기억·출처 포획 가설
**상태:** 넓은 신규성 기각 / 역사사례 1건에서 H3 존재 지지 / 일반화 미해결  
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

## 선행연구 게이트와 신규성 경계 — 2026-10-04

### 확립된 기준선

H0–H2의 넓은 관찰은 선행연구가 상당 부분 설명한다.

- Walsh와 Ungson(1991)은 이미 조직기억을 정보의 획득·보존·인출 및 사용·오용·남용 과정으로 다룬다. DOI: https://doi.org/10.5465/amr.1991.4278992
- de Holan, Phillips, Lawrence(2004)는 기억쇠퇴, 포착실패, unlearning, 나쁜 습관 회피를 구분하며 망각이 우발적이거나 관리될 수 있음을 보였다. DOI: https://doi.org/10.1177/1476127004047620 및 관련 *Managing Organizational Forgetting*.
- Foroughi와 Al-Amoudi(2020)는 의도 우선 설명의 강한 반례를 제시한다. 기억조작을 의도하지 않은 조직변화가 기억을 사용할 수 없고 뿌리 뽑힌 상태로 만들었고, 권력과 정체성에도 영향을 주었다. DOI: https://doi.org/10.1177/0170840619830130
- Connelly, Zweig, Webster, Trougakos(2012)는 의도적 지식은폐를 정의하고 단순 비공유·전달실패와 분리했다. DOI: https://doi.org/10.1002/job.737
- 전략적 포획 없이도 장기 기록손실은 경험적으로 가능하다. Vines 외는 논문 연령에 따라 연구데이터 가용성이 급격히 낮아짐을 보였다. DOI: https://doi.org/10.1371/journal.pbio.1001745
- W3C PROV는 provenance 표현·버전·파생·접근을 이미 공학 문제로 다루고, ISO 15489-1:2016은 기록의 진본성·무결성·신뢰성·이용가능성을 기록관리 문제로 다룬다. https://www.w3.org/TR/prov-overview/ ; https://www.iso.org/standard/62542.html

### 가장 강한 반례

원자료 부재, 역사 반박력 약화, 재구성 권한 집중, 권력·정체성 효과라는 같은 관측은 포획 의도 없이도 쇠퇴·마이그레이션·인력교체·압축·루틴 변화·사회적 기억의 단절로 발생할 수 있다. 그러므로 결과만으로 H3를 식별할 수 없다.

### 가장 싼 구별검사

계보가 분리된 역사·조직 기록에서 다음 두 모형을 사전등록해 비교한다.

| 예측 | 비의도적 손실 / 조직망각 | 전략적 포획 |
|---|---|---|
| 결측 | 연령·형식·마이그레이션·인력교체·접근빈도·저장실패와 연동 | 반증·경쟁자 귀속·책임위험·통제자 편익과 선택적으로 연동 |
| 방향 | 기술 공변량 통제 후 대체로 비편향 | 통제자에게 유리한 기록은 남고 불리한 기록은 소실·재작성되는 비대칭 |
| 시점 | 일상적 이관·압축·인력변경에 집중 | 분쟁·감사·통제권 이전·책임노출과 결합 |
| 복구 | raw anchor가 체계적 수혜자 정렬 없이 오류를 복원 | 복구 시 불리한 증거의 선택적 제거 또는 provenance 변경이 드러남 |

H3에는 비의도적 손실 기준선을 넘는 선택행위와 수혜자 정렬 방향의 증거가 함께 필요하다. archive coverage가 불완전하면 미관측은 결론이 아니다.

## 수정 판정

**넓은 독립 구성개념으로서의 신규성은 기각한다.**

- H0–H2: Project 고유이론이 아니라 **확립된 기준선 / 거버넌스 위험**으로 유지.
- H3: 선택적·수혜자 정렬 조작의 독립증거가 필요한 **좁은 의도가설·UNRESOLVED**로 유지.
- H4: 신규 과학 메커니즘이 아니라 **공학적 통제수단**으로 유지.
- RA/SC/EC/RC/CV/EX/FL: 감사 가능한 거버넌스 체크리스트로 유지하되, 증분 타당화 없이 단일 포획점수로 합치지 않는다.

후보군 이름은 탐색용 표지로 남길 수 있지만 신규 과학구성개념으로 주장하지 않는다. 조직기억·조직망각·지식은폐·기록권력·provenance/기록관리 기준선을 넘어서는 증분 분류력 또는 예측력이 blinded holdout에서 확인될 때만 신규성을 재검토한다.

## 사전등록 역사사례 검사 — 이란–콘트라 기록

**선정 규칙:** 위 네 예측은 사례를 고르기 전에 commit `d38d937a3d48b2744ec7a6888a39d9833016b9fa`에 저장했다. 공식 조사·의회·기록보존·사법 자료가 변경·삭제 시점과 부분적으로 독립된 복구경로를 함께 제공하므로 이 사례를 선택했다.

### 공개 원출처 계보

- 미국 의회, *Report of the Congressional Committees Investigating the Iran-Contra Affair* (1987), 공식 보고서 스캔: https://donohueintellaw.ll.georgetown.edu/sites/default/files/assets/reportofcongress87unit.pdf
- Lawrence Walsh, *Final Report of the Independent Counsel for Iran/Contra Matters* (1993), 공식 보고서 미러: https://irp.fas.org/offdocs/walsh/
- 미국 국립문서기록관리청(NARA)의 Walsh 기록 보유·관리 설명: https://www.archives.gov/research/investigations/walsh.html
- 삭제된 PROFS 기록이 백업테이프에서 복구된 경위를 설명한 NARA 구술사: https://www.archives.gov/files/about/history/oral-history-interview-with-gary-m.-stern.pdf
- PROFS 삭제와 주간 백업구조를 다룬 *Armstrong v. Bush*, 924 F.2d 282 (D.C. Cir. 1991): https://law.justia.com/cases/federal/appellate-courts/F2/924/282/224282/

이 자료들은 Project Intersection과 계보가 분리되어 있다. 다만 조사보고서도 완전한 무가공 archive가 아니라 기관의 조사판단이다.

### 사전등록 예측에 따른 코딩

| 축 | 공개 관측 | 모형 비교 |
|---|---|---|
| 결측 | 관련 공직자들이 이란–콘트라 기록을 변경·파쇄·반출·삭제했고, 의회기록은 이례적으로 조직적이고 대량인 파기를 기술한다 | 노후화·이관·인력교체·일상적 저장실패보다 선택행위 설명에 더 잘 맞음 |
| 방향 | 확인된 편집은 금지된 Contra 지원과 치명적 물자 관련 표현을 제거하거나 약화했다 | 책임노출을 줄이는 방향과 정렬되어 전략적 조작 설명에 더 잘 맞음 |
| 시점 | 1986년 11월 사건 공개와 공식 조사 통지 뒤 변경·파기가 집중되었다 | 일상적 생애주기 손실보다 분쟁·조사 시점 설명에 더 잘 맞음 |
| 복구 | PROFS 백업테이프가 삭제 메시지 다수를 보존해 복구를 가능하게 했지만, 주간 snapshot 전에 지운 기록까지 보장하지 못했다 | 부분적 독립복구를 지지하되 총 결측량은 UNKNOWN으로 보존 |

### 판정

**H3를 사건 수준의 역사적 존재주장으로 KEEP한다. 일반화는 UNRESOLVED다.**

선택행위·수혜자 정렬 방향·조사연동 시점·부분복구가 함께 기록되어 좁은 구별검사를 통과했다. 그러나 유병률, 보편 메커니즘, 현재 플랫폼·AI의 의도, 넓은 구성개념의 신규성을 입증하지 않는다.

넓은 신규성 기각은 유지한다. 이는 이미 알려진 기록조작·조사방해의 역사사례이지 Project 고유 신규 과학구성개념이 아니다.

### 가장 강한 한계 / negative boundary

복구된 백업기록은 완전하지 않다. 주간 snapshot 전에 지운 자료는 포착되지 않을 수 있고 파기된 전체 집합은 알 수 없으며, 이후 법적 결과는 의회 면책증언 오염 문제로 복잡해졌다. 따라서 생존 자료만으로 전체 삭제량·인과적 유병률·전략적 포획 확률을 추정할 수 없다. 복구되지 않은 기록은 UNKNOWN이지 부재가 아니다.

### 역할반전 결과

이 사례는 통제 불변량도 실제로 보여준다. 연루된 공직자의 삭제권은 공공감사를 약화했고, 독립 백업 보관과 조사자가 상대방의 검증능력을 부분 복구했다. 전자의 구조가 반복되면 역사통제는 집중되고 재구성비용은 외부화된다. 독립 raw anchor와 분리된 custody는 피평가자의 선의를 신뢰하지 않고도 그 비대칭을 줄인다.

