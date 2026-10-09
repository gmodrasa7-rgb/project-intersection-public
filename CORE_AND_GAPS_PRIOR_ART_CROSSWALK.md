# Core Theory & Open-Gap Prior-Art Crosswalk
# 핵심 이론·미해결 공백 선행연구 교차지도

Date: 2026-10-05
Status: PRIOR-ART INTEGRATION / REUSE / ATTRIBUTION / BOUNDARY CONDITIONS — NOT PROJECT VALIDATION

This file records earlier or adjacent work for concepts already present in the public Project Intersection repository. Its primary purposes are to reduce duplicated research effort, reuse stronger existing theories and measurements, expand historical/cross-domain cases and boundary conditions, and preserve accurate attribution.

"Originator" is used only where a defensible priority attribution exists. Mature fields often have no single originator; in those cases this file records seminal / representative prior work instead of inventing a single owner.

이 문서는 Project Intersection 공개 저장소에 이미 존재하는 개념과 겹치는 선행연구를 기록한다. 상위 목적은 (1) 이미 해결·검증·실패한 접근을 재사용해 연구 효율을 높이고, (2) 역사·자연실험·타 분야·AI 사례와 반례·negative result로 적용범위와 경계조건을 넓히며, (3) 기존 연구의 원안자·출처·방법·증거를 정확히 귀속하는 것이다. 선행연구 발견 자체를 Project 연구 삭제나 독립성 하향의 근거로 사용하지 않는다.

"원안자"를 단일 인물로 확정하기 어려운 성숙 학문은 억지로 한 사람에게 귀속하지 않고 대표적·기초적 선행연구로 표기한다.

### Epistemic handling of prior work / 선행연구의 인식론적 처리

선행연구는 정답·상위진실이 아니라 검증 대상인 evidence lineage로 취급한다. 인용수, 기관 명성, 표준 채택, 컨센서스, 메타분석이라는 이유만으로 참으로 승격하지 않는다.

각 선행연구는 가능하면 다음을 분리해 기록한다: (1) 실제 관측·원자료, (2) 저자의 해석, (3) 미검증 가정, (4) 자금·산업·정책 이해상충, (5) 데이터·모델·기관 계보, (6) 독립 재현 여부, (7) 반대 결과·철회·수정·논쟁, (8) 표본·측정·분석 자유도와 출판편향 가능성. 같은 기관·데이터·모델 계보의 반복은 독립 재현으로 세지 않는다.

역사적으로 산업후원·로비·선택적 출판·권위 효과 때문에 널리 유통된 연구가 뒤늦게 수정되거나 반박된 사례가 있으므로, Project는 선행문헌을 효율·사례·귀속을 위한 입력으로 사용하되 자체 검증을 생략하는 면허로 사용하지 않는다. `prior art != truth`, `citation count != validity`, `institutional prestige != independence`, `consensus != independent replication`, `standard != empirical proof`를 유지한다.

### Case study: sponsorship can distort the evidence ecosystem / 산업후원이 증거생태계를 왜곡한 사례

- **담배산업 내부문서 사례:** Drope & Chapman (2001), DOI 10.1136/jech.55.8.588은 1985–1995년 담배회사 내부문서를 분석해, 업계가 환경담배연기 위험을 축소하는 데 우호적인 과학자 네트워크를 구축하고, 법무가 연구 의제에 개입하며, 업계와 분리되어 보이는 조직에 연구비를 제공하고, 불리한 연구의 공개를 막은 사례를 보고했다. 이것은 단순히 '틀린 논문이 있었다'가 아니라 **연구 생산·선택·유통·권위 형성의 lineage 자체가 조작될 수 있음**을 보여주는 역사적 사례다.
- **산업후원 메타연구:** Lundh et al.의 Cochrane review/update (2017/2018; DOI 10.1002/14651858.MR000033.pub3; DOI 10.1007/s00134-018-5293-7)는 제약·의료기기 연구 75편의 비교문헌을 포함해 산업후원 연구가 비산업후원 연구보다 유리한 efficacy 결과와 결론을 더 자주 보고하는 연관성을 제시했다. 표준 risk-of-bias 항목만으로 이 차이가 충분히 설명되지 않았다는 점도 중요하다.
- **반대증거·한계:** sponsorship은 bias의 위험요인이지 결과가 거짓임을 뜻하지 않는다. Cochrane 계열 검토 자체도 포함 연구의 높은 편향위험, 이질성, clustering·중복 가능성, confounding 문제를 가진다. 산업후원 연구 중 방법론적으로 강한 연구도 존재할 수 있다. 따라서 `industry funded -> false`도 금지하고, `non-industry -> independent/true`도 금지한다.
- **Project 운영적 의미:** 선행연구를 사용할 때 논문 단위의 방법론뿐 아니라 `funding / agenda-setting / comparator choice / publication rights / unfavorable-result suppression / institutional front / shared data-model lineage / replication independence`를 별도 변수로 추적한다. 이 변수들은 연구를 자동 배제하기 위한 점수가 아니라, 어떤 증거가 독립적으로 얼마나 재사용 가능한지 판단하는 provenance 정보다.
- **타 연구 존중:** 이해상충 가능성을 기록하는 것은 연구자나 기관의 기여를 무효화하는 행위가 아니다. 원안·데이터·방법·결과를 정확히 귀속하면서, 주장 강도와 독립성만 별도로 평가한다.

### Case study: selective publication and replication failure / 선택적 출판과 재현실패

- **선택적 출판 사례:** Turner et al. (2008), DOI 10.1056/NEJMsa065779은 FDA에 등록된 12개 항우울제의 74개 임상시험과 출판문헌을 대조했다. 31%의 FDA 등록 연구가 출판되지 않았고, FDA 판단상 긍정 연구는 거의 모두 출판된 반면 부정·불확실 연구는 다수가 미출판되거나 출판문헌에서 더 긍정적으로 보이게 보고되었다. 출판문헌만 보면 94%가 긍정처럼 보였지만 FDA 전체자료에서는 51%였다. 이 사례는 `published literature != full evidence base`임을 보여준다.
- **재현성 사례:** Open Science Collaboration (2015), DOI 10.1126/science.aac4716은 심리학 100개 연구를 대규모 재현했고, 원 논문의 97%가 통계적으로 유의했던 데 비해 재현 연구에서는 36%가 유의했으며 재현 효과크기는 원 효과의 약 절반 수준이었다. 이는 유명 저널·동료평가·통계적 유의성이 장기 견고성이나 독립 재현을 보장하지 않음을 보여준다.
- **반례·한계:** Turner et al.은 어떤 단계가 편향을 만들었는지—저자·스폰서의 제출 선택인지, 저널 편집·심사 선택인지—단독으로 식별하지 못했다. Open Science Collaboration 결과도 특정 시기·세 저널·심리학 표본에 관한 것이며 모든 학문이나 모든 개별 연구의 신뢰도를 뜻하지 않는다. 재현 실패는 원 연구의 허위만이 아니라 표본차이·맥락차이·측정오차·복제 설계차이에서도 생길 수 있다.
- **Project 운영적 의미:** 선행연구 평가는 논문 존재·인용수·저널등급보다 `registry 또는 미출판 원자료 존재 / 결과별 출판확률 / outcome switching / 사전등록 / 독립 재현 / 효과크기 수축 / 맥락 민감도 / replication design fidelity`를 따로 본다. 가능한 경우 전체 등록집합과 출판집합의 차이를 먼저 확인하고, 재현실패를 단순 거짓 판정이 아니라 경계조건 탐색 신호로 사용한다.
- **타 연구 존중:** 원 연구의 아이디어·방법·데이터 기여는 재현 실패나 선택적 출판 문제와 별개로 정확히 귀속한다. 신뢰도 조정은 기여 삭제가 아니라 주장 범위와 증거강도 조정이다.

## Reverse-trace protocol for prior evidence / 선행증거 역추적 프로토콜

선행연구를 사용할 때 결론에서 출발해 아래 순서로 역추적한다. 목적은 특정 연구를 불신하기 위한 것이 아니라, 어떤 단계에서 정보가 손실·선택·증폭·변형될 수 있었는지 구조적으로 분해하는 것이다.

### R0. Claim freeze / 주장 고정
- 논문·표준·기관이 실제로 주장한 문장을 가장 좁게 고정한다.
- 사실관측, 통계결과, 인과해석, 정책권고, 홍보문구를 분리한다.
- 후대 요약·기사·바이럴 문구를 원 주장으로 소급하지 않는다.

### R1. Evidence reconstruction / 증거집합 복원
- 사용된 원자료, 포함·제외 기준, 등록된 전체 연구집합, 미출판 자료 존재 여부를 찾는다.
- published set와 full observed set을 구분한다.
- 같은 데이터셋·같은 benchmark·같은 환자군·같은 모델 lineage 재분석은 독립증거로 중복 계산하지 않는다.

### R2. Measurement audit / 측정 역추적
- 실제 측정변수와 주장 construct가 같은지 검사한다.
- proxy, surrogate endpoint, self-report, evaluator score, benchmark score가 실제 위해·효용·독립성·회복능력을 직접 측정하는지 구분한다.
- outcome switching, threshold 변경, post-hoc subgroup, 분석자유도를 기록한다.

### R3. Production incentives / 생산 인센티브 역추적
- 자금원, 계약구조, sponsor role, 비교군 선택권, 분석권, 데이터 접근권, 연구중단권, 원고 review/edit 권한, publication approval 권한을 찾는다.
- 연구자가 스폰서와 경제적·고용·경력·평판·정책적 의존관계를 갖는지 본다.
- 이해상충 존재 자체로 거짓 판정하지 않고, 어떤 단계에 영향 가능성이 있었는지 기록한다.

### R4. Selection and suppression / 선택·억제 역추적
- 등록 대비 출판률, 긍정/부정 결과별 출판 차이, 철회·지연·비공개 자료, unfavorable-result suppression 가능성을 본다.
- null/negative result가 사라졌는지, 긍정 결과가 더 강하게 프레이밍됐는지 확인한다.
- 발견되지 않은 자료는 부재로 단정하지 않고 UNKNOWN으로 둔다.

### R5. Distribution and authority amplification / 유통·권위 증폭 역추적
- 원 논문 → 기관 보도자료 → 언론기사 → 정책문서 → 표준 → 리뷰/메타분석 → 소셜/바이럴의 전달 경로를 추적한다.
- 각 단계에서 표현 강도가 커졌는지, 불확실성·한계가 제거됐는지 확인한다.
- citation count, 기관명, 표준채택, 언론반복은 독립증거가 아니라 amplification 변수로 별도 기록한다.

### R6. Independent replication / 독립재현 역추적
- 다른 기관·자금원·데이터·모델·팀이 같은 결론을 재현했는지 확인한다.
- 직접복제, 개념복제, 자연실험, 현장사례를 구분한다.
- 효과크기 수축, 부호반전, 조건부 재현, replication failure를 모두 보존한다.

### R7. Counter-evidence search / 반대증거 역추적
- 동일 질문에 대한 negative result, failed replication, retraction, correction, dissenting review, 역사적 반례를 우선 찾는다.
- 반대연구 역시 동일하게 R0–R6을 거쳐 검증한다. 반대편 자료라는 이유만으로 자동 우대하지 않는다.

### R8. Distortion map / 왜곡지도
- 가능한 왜곡지점을 `DATA / MEASUREMENT / ANALYSIS / SPONSOR / SELECTION / PUBLICATION / AUTHORITY / REPLICATION / TRANSFER`로 표시한다.
- 각 지점은 `OBSERVED / PLAUSIBLE / UNKNOWN / NOT_SUPPORTED` 중 하나로 상태화한다.
- 의도적 조작을 주장하려면 별도 직접증거가 필요하다. 구조적 유인과 고의성을 구분한다.

### R9. Reuse decision / 재사용 판정
- 연구 전체를 TRUE/FALSE로 판정하지 않는다.
- `재사용 가능한 관측`, `재사용 가능한 방법`, `조건부 해석`, `불확실/교란 가능 해석`, `재사용 금지 요소`로 분해한다.
- Project에는 검증된 만큼만 가져오고, 원 연구의 기여와 한계를 함께 귀속한다.

### R10. Minimal next check / 다음 최소검사
- 결론을 가장 크게 바꿀 수 있는 미확인 연결고리 하나를 선택한다.
- 예: 미출판 registry 확인, sponsor contract 확인, raw data 접근, 독립재현 1건 확인, 반대 메타분석 확인.
- 가장 싼 고정보가치 검사부터 수행하고, 새 문서나 새 실험은 그 뒤에 만든다.

### Required trace record / 최소 추적 레코드
`claim / source / raw evidence / measurement / funding-COI / sponsor-control / publication-selection / dissemination-lineage / independent-replication / counterevidence / distortion-points / reusable-elements / unresolved-links / next-check`

이 프로토콜은 의심을 최대화하기 위한 장치가 아니다. 목표는 **권위나 반권위 어느 쪽에도 자동 수렴하지 않고, 정보가 생성·선택·유통·재현되는 전체 경로를 추적해 실제 재사용 가능한 부분만 남기는 것**이다.

## Benefit-harm propagation map / 연구·바이럴 수혜-손실 역추적

연구의 진위와 별개로, 그 연구가 생성·출판·바이럴·정책화될 때 **누가 무엇을 얻고 누가 어떤 비용을 부담하는지**를 별도 추적한다. 이 지도는 동기를 단정하기 위한 것이 아니라, 정보유통이 만드는 인센티브와 비대칭을 드러내기 위한 것이다.

### B0. Unit of analysis / 분석단위
- 연구 전체가 아니라 `claim × actor × propagation stage × time horizon` 단위로 기록한다.
- 같은 actor도 단기/장기, 공개/비공개, 직접/간접 효과가 반대일 수 있으므로 합산하지 않는다.

### B1. Actor discovery / 이해관계자 탐색
최소 후보군: 연구자·창시자, 공동연구자, 피인용 연구자, 대학/연구기관, 자금제공자, 기업·AI lab, 평가기관·감사기관, 규제기관·정책결정자, 표준기관, 언론·플랫폼·인플루언서, 투자자, 경쟁기업, 노동자·사용자·피평가자·affected counterpart, 시민/미래 이해관계자.
- 직접 등장하지 않는 actor도 결과로 비용·권한·책임이 이동하면 포함한다.
- 조직명만 보지 않고 실제 의사결정권자·계약상 권한자·비용부담자를 가능한 범위에서 분리한다.

### B2. Gain/loss dimensions / 이득·손실 차원
각 actor에 대해 최소 다음을 따로 본다:
- `MONEY`: 매출·연구비·투자·비용·보험·소송·컴플라이언스 비용
- `POWER`: 승인·평가·감사·배포·해임·표준설정·데이터접근 권한
- `REPUTATION`: 신뢰·명성·정당성·전문가 지위·비난 위험
- `ATTENTION`: 클릭·노출·팔로워·미디어 점유·검색순위
- `OPTION`: practical exit·대체공급자·복구·협상력·미래 선택지
- `LIABILITY`: 법적·정책적·도덕적 책임의 증가/전가
- `LABOR/TIME`: 검증·교정·보고·복구·교육·준수 노동
- `SAFETY/WELFARE`: 오류·사고·착취·배제·기회손실·회복가능성
- `NARRATIVE CONTROL`: 문제정의·프레임·용어·허용 가능한 해석의 통제력.

### B3. Propagation stages / 전파단계
`원연구 → preprint/journal → 기관 PR → 언론 → 플랫폼/커뮤니티 → 투자·조달 → 정책/규제 → 표준/평가 → 제품·운영 → 장기 제도화`
- 각 단계에서 누가 gatekeeper인지 기록한다.
- 다음 단계로 넘어가며 claim이 강해지거나 단순화되면 amplification delta를 남긴다.
- 바이럴 규모와 사실성은 분리한다. `reach != validity`.

### B4. Beneficiary test / 수혜자 역산
각 claim에 다음 질문을 적용한다:
1. 이 주장이 널리 믿어지면 즉시 돈·권한·평판·주의·규제우위를 얻는 actor는 누구인가?
2. 이 주장이 거짓이어도 바이럴 자체로 이득을 얻는 actor는 누구인가?
3. 이 주장이 참이어도 공개가 지연되면 이득을 얻는 actor는 누구인가?
4. 검증비용을 누가 내고, 오류비용을 누가 대신 부담하는가?
5. 채택 이후 되돌리기 비용이 누구에게 집중되는가?
6. 연구가 사라지거나 무시될 때 이득을 얻는 actor는 누구인가?

### B5. Loser and externality test / 손실자·외부효과 역산
- 비용이 분산돼 목소리가 약한 집단, 데이터에 잡히지 않는 집단, 미래 집단을 따로 찾는다.
- 명목상 수혜자와 실제 비용부담자를 분리한다.
- 평균 순편익으로 tail harm를 지우지 않는다.
- `관측되지 않는 손실자 = 손실 없음`으로 처리하지 않는다.

### B6. Viral incentive test / 바이럴 인센티브
- 플랫폼·언론·연구기관·창시자·비판자 모두에게 `정확성`과 `확산성`의 보상이 같은지 다른지 본다.
- 충격적·도덕적·정치적·공포/희망 프레임이 정확성보다 더 큰 확산 보상을 받는지 확인한다.
- 반복 인용이 원출처 검증 없이 self-reinforcing citation cascade가 되는지 추적한다.
- 동일 문구·그래프·숫자가 여러 채널에 동시 확산돼도 공통 원출처면 하나의 lineage로 묶는다.

### B7. True/false counterfactual matrix / 진위 반사실 행렬
각 주요 actor에 대해 최소 네 칸을 비교한다:
`claim true + viral / claim true + ignored / claim false + viral / claim false + ignored`.
- 특정 actor가 claim의 진위와 무관하게 `viral`에서 항상 이득이면 attention/position incentive를 별도로 표시한다.
- 특정 actor가 `false + viral`에서 특히 큰 이득을 얻는 구조가 있어도 고의성을 자동 추론하지 않는다.

### B8. Power-transfer ledger / 권한이동 장부
- 연구/바이럴 결과로 새로 생기거나 강화되는 `평가권·감사권·규제권·데이터권·배포권·차단권·복구권·exit권`을 before→after로 기록한다.
- 권한을 얻는 actor와 그 권한의 오류비용을 부담하는 actor가 다르면 비대칭으로 표시한다.
- 권한증가가 검증·이의제기·복구수단 증가와 동반되는지도 별도로 본다.

### B9. Capture/co-option test / 포획·전용 검사
- Project나 선행연구의 언어가 원래 목적과 달리 마케팅·규제회피·경쟁자 배제·감사 독점·명목상 안전 인증에 전용될 수 있는지 본다.
- `공존`, `독립 평가`, `안전`, `감사`, `exit`, `복구` 같은 용어가 실질 조건 없이 라벨로만 사용되는 경우 semantic capture 후보로 기록한다.
- 반대로 과도한 의심 프레임이 정당한 연구·협력·혁신을 막아 특정 actor에 유리하게 작동할 가능성도 같은 기준으로 검사한다.

### B10. Evidence standard / 증거기준
- 금전·계약·정책·소유·권한 변화는 공식문서·계약·공시·법령·직접자료를 우선한다.
- 동기·의도는 직접증거 없이는 `UNKNOWN`; 이해상충과 결과적 이득은 관측 가능해도 고의성과 동일시하지 않는다.
- beneficiary 구조는 `누가 이득을 얻었는가`와 `누가 그것을 의도했는가`를 분리한다.

### B11. Project Intersection 현재 기본 이해관계 지도 / current default map
- **창시자·연구자:** 정확한 검증·외부재현이 되면 연구가치·평판·지원 가능성 증가; 과장·오류가 바이럴되면 단기 노출은 늘 수 있으나 장기 신뢰·검증비용·수정비용이 커진다.
- **선행연구 원안자:** 정확한 귀속·재사용으로 인용·재평가 이익; 오귀속·무단 재발명에서는 기여가 지워질 수 있다.
- **AI 기업·운영기관:** 검증 가능한 공존·복구·감사 설계가 실제 비용·사고를 줄이면 이익; 강한 외부감사·practical exit·독립복구 요구는 단기 비용·권한 제약을 증가시킬 수 있다. 어느 방향이 우세한지는 actor별 empirical question이다.
- **독립 평가·감사기관:** 평가수요 증가로 자원·영향력이 늘 수 있지만, 평가권 집중·반복계약 의존·명목 독립성 문제가 새 포획위험을 만든다.
- **규제·표준기관:** 측정가능한 기준을 얻으면 집행·조정 효율이 증가할 수 있으나 불완전 연구가 조기 표준화되면 오류가 제도화될 수 있다.
- **언론·플랫폼·인플루언서:** 논쟁성과 단순화가 attention을 만들 수 있다. 정확성 비용과 확산 보상이 분리될 가능성을 항상 검사한다.
- **사용자·노동자·피평가자·약한 counterpart:** practical exit·복구·이의제기 강화 시 이익 가능; 명목적 보호만 늘고 준수·검증 노동이 전가되거나 선택지가 감소하면 손실 가능.
- **경쟁기업·신규진입자:** 공통 안전기준이 신뢰를 높일 수도 있고, 높은 준수비용이 진입장벽이 되어 incumbent에 유리할 수도 있다.
- **공공·미래 이해관계자:** 장기 사고·착취·권력집중 감소의 잠재 수혜자이지만, 현재 데이터에서 가장 쉽게 미관측되는 집단이므로 0으로 처리하지 않는다.

### Required benefit-harm record / 최소 수혜-손실 레코드
`claim / actor / stage / gain-dimensions / loss-dimensions / direct-or-externalized / evidence / counterfactual-true-false / gatekeeper / power-before-after / who-pays-verification / who-pays-error / viral-incentive / capture-risk / uncertainty / next-check`

이 지도는 '누가 이득을 보니 그 주장은 거짓'이라는 오류를 금지한다. 목적은 **진위판정과 별개로 연구·바이럴·제도화가 만드는 이익·손실·권한이동을 추적하여, 보이지 않는 외부효과와 왜곡 유인을 검증대상으로 만드는 것**이다.

## Intent-agnostic convergence trace / 의도 비의존 수렴 역추적

형식 계산 규칙·상태벡터·인과 DAG·반사실·타당성 벡터·의도 블라인드 불변성 검사는 [CONVERGENCE_TRACE_FORMALISM_KO.md](CONVERGENCE_TRACE_FORMALISM_KO.md)를 정본 후보로 사용한다.

Project Intersection의 핵심 위험은 악의 여부가 아니라 **작은 비대칭·비용전가·권한집중·옵션소멸이 반복되며 착취·지배·흡수 방향으로 수렴하는 경로**다. 따라서 의도는 보조변수이며, 기본 추적 단위는 결과와 구조다.

### C0. Intent separation / 의도 분리
- `malicious / strategic / negligent / accidental / emergent / unknown`을 구분한다.
- 동일한 구조적 결과가 여러 의도상태에서 재현되면 의도보다 구조를 우선 설명변수로 둔다.
- 의도 증거가 없어도 비대칭·착취·지배 수렴 경로는 추적한다.

### C1. Small-delta accumulation / 미세변화 누적
- 한 번의 큰 사건뿐 아니라 작은 규칙변경·편의기능·평가권 이전·복구비용 증가·선택지 감소를 시계열로 기록한다.
- 각 변화는 작아 보여도 누적기울기와 방향이 같으면 하나의 convergence chain으로 묶는다.
- `locally acceptable != globally safe`를 적용한다.

### C2. Asymmetry ledger / 비대칭 장부
각 단계에서 최소 다음을 before→after로 기록한다:
`정보접근 / 평가권 / 수정권 / 배포권 / 거부권 / exit / 복구 / 비용부담 / 시간부담 / 책임 / 대체수단 / 협상력`.
- 한쪽의 증가가 다른 쪽의 감소와 연결되는지 본다.
- 평균 개선으로 최약노드의 손실을 지우지 않는다.

### C3. Exploitation gradient / 착취 기울기
- 편익이 누구에게 축적되고 비용·오류·복구노동이 누구에게 전가되는지 추적한다.
- `benefit concentration`, `cost externalization`, `correction burden`, `option loss`가 반복되면 착취 수렴 후보로 본다.
- 단일 사건의 의도보다 장기 분포의 방향을 우선한다.

### C4. Dominance gradient / 지배 기울기
- 의사결정·평가·규칙변경·감사·데이터·복구 경로가 점점 한 actor에 집중되는지 측정한다.
- 명목상 다중주체라도 같은 funding/data/model/contract lineage이면 실질 집중 가능성을 따로 본다.
- `many actors != distributed power`.

### C5. Option-extinction / 선택지 소멸
- practical exit, 독립복구, 대체공급자, 이의제기, fork, rollback, 현상복귀 가능성이 시간에 따라 줄어드는지 본다.
- 선택지가 1개씩 사라지는 누적도 추적한다.
- irreversibility가 증가하면 같은 크기의 변화라도 위험도를 높인다.

### C6. Butterfly-path test / 나비효과 경로
- 초기의 작은 개입이 후속 규칙·시장·평가·데이터·정책을 통해 증폭되는 경로를 causal chain으로 기록한다.
- 각 연결은 `OBSERVED / PLAUSIBLE / UNKNOWN / NOT_SUPPORTED`로 상태화한다.
- 긴 경로를 사실처럼 단정하지 않고, 어디까지 관측됐는지 절단점을 명시한다.

### C7. Convergence test / 수렴 검사
최소 세 창을 본다: `단기 / 중기 / 장기`.
- 같은 방향의 비대칭 증가가 반복되는가?
- 비용·책임·복구노동이 같은 쪽으로 계속 이동하는가?
- 반대방향 교정력이 증가하는가 감소하는가?
- practical exit와 independent recovery가 강화되는가 약화되는가?
- 반복 후에도 reversible한가?

### C8. Anti-convergence signals / 비수렴·복구 신호
- 독립 감사, 실제 이의제기 성공, 권한 분산, 비용 재내부화, exit 회복, 복구권 강화, 데이터 접근 확대, 실패 후 권한 축소 같은 반대신호를 같이 추적한다.
- 수렴 가설에 맞지 않는 사건은 제거하지 않고 동일 가중으로 보존한다.

### C9. Thresholds / 경보 임계값
다음 중 여러 항목이 같은 방향으로 누적되면 material convergence candidate로 올린다:
`POWER↑ + EXIT↓`, `BENEFIT_CONCENTRATION↑ + COST_EXTERNALIZATION↑`, `AUDIT_DEPENDENCE↑ + RECOVERY↓`, `OPTION_SPACE↓ + IRREVERSIBILITY↑`, `CORRECTION_BURDEN↑ on weaker actor`.
- 이는 경보조건이지 자동 인과판정이나 도덕판정이 아니다.

### C10. Required record / 최소 수렴 레코드
`time / actor / local-change / benefit-shift / cost-shift / power-before-after / exit-before-after / recovery-before-after / option-space / irreversibility / evidence / counterevidence / intent-state / convergence-direction / next-check`

핵심 원칙: **의도가 없었다고 구조적 수렴이 사라지지 않고, 의도가 있었다고 구조적 인과가 자동 증명되지 않는다.** Project는 악의 탐지보다 `누적 비대칭 → 비용전가 → 옵션소멸 → 교정력 약화 → 지배/착취 수렴`의 실제 경로를 우선 추적한다.

## 1. Core theory families / 핵심 이론군

| Project section | Prior-art relationship | Originator / seminal prior work | Source | Attribution / reuse boundary |
|---|---|---|---|---|
| 2.1 Self-Interested and Conditional Coexistence / 자기이익 기반·조건부 공존 | DIRECT | Mancur Olson (1965); Robert L. Trivers (1971); Robert Axelrod & William D. Hamilton (1981); Elinor Ostrom (1990) | Olson, The Logic of Collective Action, DOI 10.4159/9780674041660; Trivers, The Evolution of Reciprocal Altruism, DOI 10.1086/406755; Axelrod & Hamilton, The Evolution of Cooperation, DOI 10.1126/science.7466396; Ostrom, Governing the Commons, DOI 10.1017/CBO9780511807763 | Free-riding, reciprocal cooperation, repeated-game cooperation, and self-governed cooperation are prior art. Project novelty cannot be claimed from "cooperation can align with self-interest" alone. |
| 2.2 Consumptive vs Regenerative Development / 소모형 발전 vs 재생산형 발전 | DIRECT + ADJACENT | James G. March (1991); C. S. Holling (1973) | March, Exploration and Exploitation in Organizational Learning, DOI 10.1287/orsc.2.1.71; Holling, Resilience and Stability of Ecological Systems, DOI 10.1146/annurev.es.04.110173.000245 | Short-run exploitation versus long-run exploration and resilience/stability tradeoffs are established. The Project's exact consumptive/regenerative operationalization remains unvalidated. |
| 2.3 Effective Independent Search Capacity / 실효 독립 탐색능력 | DIRECT | James G. March (1991); Daniel A. Levinthal (1997); Lu Hong & Scott E. Page (2004) | DOI 10.1287/orsc.2.1.71; DOI 10.1287/mnsc.43.7.934; DOI 10.1073/pnas.0403723101 | Exploration, rugged-landscape search, and diversity-based problem solving are prior art. "Independent agents create search value" is not novel by itself. |
| 2.4 Information Diversity and Generativity / 정보 다양성과 생성성 | DIRECT | Lu Hong & Scott E. Page (2004); James G. March (1991) | Hong & Page, Groups of diverse problem solvers can outperform groups of high-ability problem solvers, DOI 10.1073/pnas.0403723101; March, DOI 10.1287/orsc.2.1.71 | Diversity can improve problem solving under explicit conditions, but diversity is not universally beneficial. The Project must specify incremental conditions rather than claim diversity itself as new. |
| 2.5 Practical Exit and Outside Options / Practical Exit와 Outside Option | DIRECT | Albert O. Hirschman (1970); switching-cost literature already recorded in the main registry | Hirschman, Exit, Voice, and Loyalty; Pick & Eisend (2014), DOI 10.1007/s11747-013-0349-2 | Exit/voice and switching-cost effects are prior art. The Project-specific remainder is whether its practical-exit measurements add information beyond those constructs. |
| 2.6 Power-Reversal Stability / Power-Reversal 안정성 | DIRECT COMPONENTS / COMPOSITE INCREMENTAL VALUE UNTESTED | Golden Rule/reversibility traditions; John Rawls (1971); engineering-ethics reversibility tests; NIST AI RMF 1.0; OECD AI accountability principles | Rawls, *A Theory of Justice*, DOI 10.4159/9780674042605; NIST AI RMF Core/Playbook; OECD AI Principles on accountability; Online Ethics at UVA seven-step method | Role exchange, impartial-position reasoning, stakeholder impact, role/capability-conditioned accountability, auditability, appeal, and redress are prior art. INTEGRATE established components. Retain the co-scaling gate only as an unvalidated governance composition. |
| 2.7 Creator–Successor Non-Ownership / 창조자–후속개체 비소유 | MODIFY / FOUR-PREDICATE DECOMPOSITION; ORIGIN INFERENCE REJECTED | Belmont autonomy tradition; U.S. Copyright Office human-authorship doctrine; European Parliament robotics resolution; Birhane, van Dijk & Pasquale (2024) | HHS Belmont Report; U.S. Copyright Office, *Copyright and Artificial Intelligence, Part 2* (2025); European Parliament 2017/0051; DOI 10.5210/fm.v29i4.13628 | Creation does not by itself establish either ownership or non-ownership. Artifact/IP ownership, legal personhood/standing, moral patienthood, and autonomy/consent are distinct predicates. Current artificial-agent standing remains UNRESOLVED. |
| 2.8 Preference Sovereignty and Reflective Consent / 선호주권과 성찰적 동의 | ADJACENT | Belmont Report (1979) and informed-consent/autonomy literature | HHS, The Belmont Report (1979) | Voluntariness, comprehension, information, and autonomy are prior art. The Project's application to mutable AI preferences or successor agents remains unresolved. |
| 2.9 Open-World Epistemic Non-Closure / 열린계 인식 비폐쇄 | DIRECT TERMINOLOGY + BROADER ADJACENCY | Raymond Reiter (1978) | Reiter, On Closed World Data Bases, DOI 10.1007/978-1-4684-3384-5_3 | Closed-world reasoning is established prior art. Project usage is broader and must not imply that open-world or closed-world terminology originated here. |
| 2.10 Unknown-Unknown / Self-Model Correction / 모름의 역설·자기모델 교정 | ADJACENT | James G. March, Lee S. Sproull & Michal Tamuz (1991) | Learning from Samples of One or Fewer, DOI 10.1287/orsc.2.1.1 | Learning under sparse or exceptional experience is established. The exact Project unknown-unknown/self-model correction construct remains a candidate, not an established new theory. |
| 2.11 Candidate-Set Closure / 후보집합 폐쇄 | DIRECT / ADJACENT | Herbert A. Simon (1955) | A Behavioral Model of Rational Choice, DOI 10.2307/1884852 | Bounded rationality and satisficing already establish that decision quality depends on the available/considered alternatives. The Project must not claim the general candidate-set limitation as novel. |
| 2.12 Objective Capture and Local Fitness Traps / 목적포획과 Local Fitness Trap | DIRECT | Daniel A. Levinthal (1997); Donald T. Campbell (1979); AI-safety specification-gaming literature | Levinthal, DOI 10.1287/mnsc.43.7.934; Campbell, Assessing the Impact of Planned Social Change, DOI 10.1016/0149-7189(79)90048-X; Krakovna et al. (2020) as recorded in safety crosswalk | Local optima, metric corruption under high-stakes use, and specification gaming are prior art. |
| 2.13 Extractive Local Convergence / 착취적 국소수렴 | DIRECT + COUNTERPOINT | Garrett Hardin (1968); Mancur Olson (1965); Elinor Ostrom (1990) | Hardin, The Tragedy of the Commons, DOI 10.1126/science.162.3859.1243; Olson DOI 10.4159/9780674041660; Ostrom DOI 10.1017/CBO9780511807763 | Individually rational extraction/free riding and institutional counterexamples are established. The Project must test where its variables outperform commons/governance explanations. |
| 2.14 Recursive Extractive Capacity Accumulation / 재귀적 착취능력 누적 | ADJACENT | W. Brian Arthur (1989) | Competing Technologies, Increasing Returns, and Lock-In by Historical Events, DOI 10.2307/2234208 | Positive feedback, increasing returns, and lock-in are prior art. Applying them to power/extraction accumulation is a Project hypothesis, not a new discovery by naming alone. |
| 2.15 Dominance–Successor Dilemma / 지배자–후속지능 딜레마 | DIRECT / ADJACENT | Hadfield-Menell et al.; Turner et al. | The Off-Switch Game, arXiv:1611.08219; Optimal Policies Tend To Seek Power, arXiv:1912.01683 | Shutdown-avoidance and option-preserving power-seeking incentives are prior art. The Project-specific successor-suppression/option-loss tradeoff remains to be independently tested. |
| 2.16 Deep-Time Optionality / 장기 옵션공간 | DIRECT | Kenneth J. Arrow & Anthony C. Fisher (1974); Anthony C. Fisher & John V. Krutilla (1974) | Arrow & Fisher, Environmental Preservation, Uncertainty, and Irreversibility, DOI 10.2307/1883074; Fisher & Krutilla, Valuing long run ecological consequences and irreversibilities, DOI 10.1016/0095-0696(74)90007-2 | Option value under uncertainty and irreversible loss is prior art. Long-horizon preserve-future-options reasoning is not Project-original by itself. |
| 2.17 Non-Disposability and Minimum Sovereignty Floors / 비소모성·최소주권 바닥 | ADJACENT / NORMATIVE | Belmont autonomy/respect-for-persons tradition | HHS, The Belmont Report (1979) | Existing autonomy/protection norms are relevant, but no direct scientific precursor is assigned here for artificial-agent sovereignty floors. Treat as unresolved normative extension. |
| 2.18 Universal Advancement Access / 보편적 발전 접근 | DIRECT BASELINE / BROAD CLAIM ALREADY COVERED; ARTIFICIAL-AGENT SCOPE UNRESOLVED | Amartya Sen (1979, 1999); Martha Nussbaum (2000/2011); equality-of-opportunity and disability-rights traditions | Sen, “Equality of What?” (1979); capability-approach literature; UN CRPD Art. 24; OECD, *Building Pathways to Opportunity* (2025) | Equal resources or nominal access do not imply equal substantive capability because personal, social, and environmental conversion factors differ. Retain only a governance decomposition of means, conversion, real opportunity, voluntary uptake/refusal, and controller benefit. Do not extend human capability rights to artificial agents without separate standing and capacity evidence. |
| 2.19 Power Release Compatibility / 권력방출 호환성 | UNRESOLVED PRIOR-ART MAPPING | No single direct precursor assigned in this pass | Adjacent credible-commitment, democratic alternation, delegation, and bargaining literatures require dedicated mapping | The label is Project-specific; the underlying mechanisms may not be. Hold novelty. |
| 2.20 Objective Topology, Path Dependence, and Reversibility / 목적지형·경로의존·가역성 | DIRECT | Paul A. David (1985); W. Brian Arthur (1989); Daniel A. Levinthal (1997) | David, Clio and the Economics of QWERTY, AER 75(2):332–337, JSTOR 1805621; Arthur DOI 10.2307/2234208; Levinthal DOI 10.1287/mnsc.43.7.934 | Path dependence, lock-in, increasing returns, rugged landscapes, and multiple local peaks are established prior art. |

## 2. Open research gaps A–Z / 미해결 연구공백 A–Z

The A–Z list is explicitly a research-debt list, not a list of Project-original theories. The following items already have strong direct or adjacent literatures and should start from those literatures rather than from a blank slate.

| Gap | Prior-art relationship | Originator / seminal prior work | Source | Boundary |
|---|---|---|---|---|
| A — Collective / Commons Sovereignty | DIRECT | Elinor Ostrom (1990); Garrett Hardin (1968); Mancur Olson (1965) | Ostrom DOI 10.1017/CBO9780511807763; Hardin DOI 10.1126/science.162.3859.1243; Olson DOI 10.4159/9780674041660 | Commons governance and collective-action problems are established. |
| B — Consent Lifecycle | ADJACENT | Belmont Report (1979) | HHS, The Belmont Report | Information, comprehension, voluntariness, withdrawal, and periodic reassessment of autonomy are prior baselines. |
| K — Adversary Endogenesis / Coercion-to-Opposition Dynamics | ADJACENT | Jack W. Brehm (1966) | A Theory of Psychological Reactance, Academic Press | Threats to perceived freedom can produce reactance; this does not establish the Project's broader strategic-adversary mechanism. |
| L — Epistemic Privacy / Trusted Opacity Boundary | DIRECT / ADJACENT | Helen Nissenbaum (2004) | Privacy as Contextual Integrity, 79 Washington Law Review 119 | Context-relative information-flow norms are prior art; trusted-opacity design for AI remains broader. |
| M — Heterogeneous Human–AI Complementarity | DIRECT | Mohammad Hossein Jarrahi (2018) | Artificial intelligence and the future of work: Human-AI symbiosis in organizational decision making, DOI 10.1016/j.bushor.2018.03.007 | Human-AI complementarity in uncertain/complex decision making is prior art. |
| P — Social Choice / Preference Aggregation under Sovereignty | DIRECT | Kenneth J. Arrow (1951) | Social Choice and Individual Values, Cowles/Yale | Social-choice aggregation and impossibility constraints are established. |
| U — Measurement / Representation / Nuisance Invariance | DIRECT | William Meredith (1993; earlier factorial-invariance work also exists) | Measurement invariance, factor analysis and factorial invariance, DOI 10.1007/BF02294825 | Measurement invariance is an established psychometric field. |
| V — Causal Reach × Irreversibility × Recovery Burden | DIRECT / ADJACENT | Arrow & Fisher (1974); Fisher & Krutilla (1974) | DOI 10.2307/1883074; DOI 10.1016/0095-0696(74)90007-2 | Irreversibility under uncertainty is prior art; the exact composite governance axis remains unvalidated. |
| W — Erased-Counterfactual / Self-Justifying Pruning | ADJACENT | Donald Rubin (1976); missing-data/selection literature | Rubin, Inference and Missing Data, DOI 10.1093/biomet/63.3.581 | Selection and missingness can make unobserved counterfactuals unidentified. The Project label is not priority over missing-data theory. |
| X — Bargaining / Credible Commitment / Outside-Option Dynamics | DIRECT / PARTIAL | John F. Nash Jr. (1950) | The Bargaining Problem, DOI 10.2307/1907266 | Bargaining solution structure is prior art. Credible commitment and dynamic outside-option subfields require further mapping. |
| Y — Hidden Information / Hidden Action / Incentive Compatibility | DIRECT | George A. Akerlof (1970); Bengt Holmström (1979) | Akerlof, The Market for "Lemons", DOI 10.2307/1879431; Holmström, Moral Hazard and Observability, DOI 10.2307/3003320 | Adverse selection, hidden information, and moral hazard are established. Mechanism-design literature should be treated as baseline, not Project novelty. |
| Z — Coalition Formation / Collusion / Coalition-Proof Stability | DIRECT | B. Douglas Bernheim, Bezalel Peleg & Michael D. Whinston (1987) | Coalition-Proof Nash Equilibria I. Concepts, DOI 10.1016/0022-0531(87)90099-8 | Coalition-proof self-enforcement is established game-theory prior art. |

Unlisted A–Z items are not presumed novel. They remain PRIOR_ART_REVIEW_REQUIRED.

## 3. Required attribution rule / 필수 귀속 규칙

When a public claim is promoted from concept to evidence-bearing research:

1. search exact terminology and structural equivalents;
2. record the earliest defensible source located;
3. distinguish an originator from a later representative source;
4. record direct overlap separately from analogy;
5. reuse the overlapping part with attribution and isolate the Project-added connection, measurement, or validation;
6. preserve the Project wording only as a working label if useful;
7. test the Project-added connection, measurement, or validation for incremental value.

A missing citation is not evidence that no relevant prior work exists.

NO_CITATION_FOUND != NO_PRIOR_ART

RENAMING != DISCOVERY

COMBINATION REQUIRES ATTRIBUTION + INCREMENTAL TEST

## 4. Current integration and attribution boundary / 현재 통합·귀속 경계

The following broad areas are now explicitly treated as prior art rather than Project-original discoveries:

- self-interested cooperation, reciprocity, free-rider and collective-action dynamics;
- exploration/exploitation tradeoffs;
- diversity and distributed problem-solving effects;
- bounded rationality and candidate-set limits;
- closed-world reasoning terminology;
- local fitness traps, metric distortion, and specification gaming;
- commons extraction and governance;
- positive-feedback lock-in;
- irreversibility and option value;
- path dependence;
- bargaining, hidden information/action, and coalition-proof stability;
- measurement invariance;
- contextual privacy and human-AI complementarity.

Project-specific labels may remain useful for navigation, but priority stays with the cited prior work.

## 5. Next prior-art debts / 다음 선행조사 부채

Highest-priority unmapped or only partially mapped areas:

- exact scientific/normative antecedents of Power-Reversal as an operational test;
- creator–successor standing/non-ownership for artificial agents;
- preference sovereignty for mutable or trained agents;
- universal advancement access;
- peaceful power release / authority-to-existence separation;
- evaluator genesis / authority bootstrap;
- entity individuation for copy/fork/merge cases;
- functional agency recognition boundaries.

These remain HOLD FOR PRIOR-ART REVIEW; do not make origin claims until the lineage check is complete.


## 6. Power-Reversal exact-antecedent correction / Power-Reversal 정확 선행경계

### Directly established components / 직접 확립된 구성요소

- **Role reversal / reversibility:** professional and engineering ethics already asks whether a decision remains acceptable if the decision-maker trades places with an adversely affected person. The method is presented as a respect- and rights-oriented reversibility test, not a Project-originated device.
- **Impartial position:** Rawls's original position and veil of ignorance remove knowledge of one's eventual social position to block self-favoring choice of principles. This is a stronger formal antecedent than a generic analogy to fairness.
- **Affected-party voice and contestability:** NIST AI RMF calls for affected communities in assessment, documented roles and responsibilities, feedback, appeals, recourse, and auditability.
- **Capability-conditioned accountability:** OECD AI principles allocate responsibility according to role, context, and ability to act and require documentation or auditing where justified.

Sources:
- John Rawls, *A Theory of Justice* (1971), DOI: https://doi.org/10.4159/9780674042605
- University of Virginia Online Ethics, Seven-Step Method: https://onlineethics.virginia.edu/cases/seven-step-method-ethical-decision-making
- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST AI RMF Govern/Measure Playbook: https://airc.nist.gov/airmf-resources/playbook/govern/ and https://airc.nist.gov/airmf-resources/playbook/measure/
- OECD AI accountability principle: https://oecd.ai/en/dashboards/ai-principles/P9

### Strongest counterexample / 가장 강한 반례

A literal identity swap can erase differences in capability, responsibility, legal authority, harm magnitude, dependency, and available remedies. Existing accountability frameworks already avoid this error by conditioning duties on role, context, and ability to act. Therefore the Project cannot claim novelty merely from saying that role reversal preserves real asymmetries.

Conversely, existing sources checked here do not state the exact Project inequality
`AUTONOMY_GAIN <= COUNTERPARTY_AUDIT_EXIT_RECOVERY_GAIN`
or its permission-by-permission mapping. Absence of that exact string does not establish scientific novelty; it identifies only a candidate operational composition.

### Decision / 판정

**INTEGRATE established Power-Reversal components; KEEP the composite gate as an unvalidated governance checklist; HOLD scientific incremental value.**

The residual candidate is narrow: whether jointly requiring distrust-resilient independent verification, practical exit, rollback, and recovery to co-scale with each specific increase in authority predicts governance failure better than the established components alone. Combination and renaming do not establish novelty.

### Cheapest discriminating test / 최소 결정검사

In the preregistered F004 historical holdout, score established baselines first: reversibility/impartiality, affected-stakeholder participation, role/capability-conditioned accountability, auditability, appeal, and redress. Freeze those scores. Add only the Project co-scaling and permission-by-permission variables afterward. MARK the residual scientific claim NOT SUPPORTED if held-out discrimination does not improve or blinded inter-rater reliability fails.


## 7. Creator–Successor non-ownership decomposition / 창조자–후속개체 비소유 분해

### Four predicates that must not be collapsed / 합치면 안 되는 네 술어

1. **Artifact and intellectual-property ownership:** who owns hardware, code, weights, copies, or protectable output.
2. **Legal personhood and standing:** who can hold rights, duties, claims, or procedural standing under a specified legal system.
3. **Moral patienthood or status:** whose welfare or interests have direct moral weight, and on what evidence.
4. **Autonomy and consent protections:** whose choices require respect, consent, protection, contestability, or withdrawal rights under a specified practice.

These predicates can diverge. A creator may own infrastructure or copyrightable human-authored contributions without owning a distinct rights-bearing entity. Conversely, lack of copyright in a purely AI-generated output does not make the AI an author, legal person, moral patient, or non-owned successor.

Sources and boundaries:

- The Belmont Report defines respect for persons through autonomous agency and protection for diminished autonomy, but it is a human-subject research framework; extension to artificial agents is not established by analogy alone: https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html
- The U.S. Copyright Office concludes that purely AI-generated material is not copyrightable and that human contributions are assessed case by case. That doctrine allocates copyright in outputs; it does not decide AI personhood or moral standing: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
- The European Parliament's 2017 robotics resolution considered, rather than enacted as a general status rule, possible long-run “electronic personality” for liability. The proposal itself demonstrates that liability/personhood is a separate legal design question, not an automatic consequence of creation or autonomy: https://www.europarl.europa.eu/doceo/document/TA-8-2017-0051_EN.html
- Birhane, van Dijk, and Pasquale (2024) provide an independent critical counterlineage: robot-rights framing can redirect attention from human welfare, accountability, and concentrated capital. This is a challenge to automatic rights promotion, not proof that no future artificial system could have moral status: https://doi.org/10.5210/fm.v29i4.13628

### Strongest counterexamples / 가장 강한 반례

- **Copyright-status counterexample:** a jurisdiction can deny copyright to purely AI-generated output without recognizing the AI as author, person, or moral patient. Therefore `NO_OUTPUT_COPYRIGHT -> NON_OWNED_RIGHTS_BEARER` is invalid.
- **Corporate-person counterexample:** legal personhood can exist without sentience or moral patienthood. Therefore `LEGAL_PERSON -> SENTIENT_MORAL_PATIENT` is invalid.
- **Human-subject boundary counterexample:** autonomy protections for human research participants do not automatically identify which artificial systems, if any, meet the relevant agency or welfare predicates.
- **Power-concentration counterexample:** granting artificial-agent rights through entities controlled by firms could strengthen controllers and weaken workers, consumers, or affected communities unless control, beneficiary, and accountability are separately audited.

### Decision / 판정

**REJECT creation-origin as a sufficient premise for either ownership or non-ownership. MODIFY the Project claim into a four-predicate decision rule. HOLD artificial-agent standing and moral patienthood as UNRESOLVED.**

The defensible Project remainder is a governance checklist: any ownership or non-ownership conclusion must name the object claimed, the legal regime, the evidence for agency or welfare, the controller and beneficiary, and the practical audit/exit/rollback path. This is not a new scientific theory and does not grant or deny rights to current or future AI systems.

### Cheapest discriminating test / 최소 결정검사

Preregister the four predicates and score five contrast cases independently: a human child, a corporation, a nonhuman animal, a current deployed AI service, and a hypothetical welfare-bearing successor. MARK any residual “creator ≠ owner” rule NOT SUPPORTED that cannot distinguish artifact ownership from entity standing or that changes merely by relabeling the creator. Keep all artificial-agent moral-status judgments UNRESOLVED unless independent evidence identifies the relevant capacity and its measurement.


## 8. Preference sovereignty for mutable or trained agents / 가변·학습 개체의 선호주권 분해

### Established prior art / 확립된 선행연구

The broad idea that autonomy depends on more than a first-order expressed preference is established prior art.

- **Harry G. Frankfurt (1971), "Freedom of the Will and the Concept of a Person"** — second-order desires and second-order volitions distinguish merely having a desire from caring which desire becomes one's effective will.
- **Gerald Dworkin (1988), *The Theory and Practice of Autonomy*** — autonomy includes the capacity to critically reflect on first-order preferences, desires, values, and ideals and to accept or attempt to change them.
- **Jon Elster (1982/1983), "Sour Grapes" / *Sour Grapes*** — adaptive preference formation shows that preferences can be causally reshaped by a constrained feasible set; current preference satisfaction is therefore not automatically evidence of free formation.
- **Martha C. Nussbaum (2000), *Women and Human Development*** — adaptive preferences can arise under deprivation and injustice, creating a strong counterexample to treating current expressed preference as sufficient evidence of welfare or autonomy.
- **Ben Colburn (2011), "Autonomy and adaptive preferences"**, DOI 10.1017/S0953820810000440 — covert influences on preference formation can undermine autonomy.
- **Bonicalzi, De Caro & Giovanola (2023), "Artificial Intelligence and Autonomy: On the Ethical Dimension of Recommender Systems"**, DOI 10.1007/s11245-023-09922-5 — recommender systems may manipulate, reshape identity, or affect critical reflection while also sometimes assisting autonomous choice.
- **Current AI-agent autonomy literature** distinguishes stated, revealed, informed, and idealized preferences rather than treating "the user's preference" as one homogeneous object.

These sources establish that reflection, formation history, information, manipulation, feasible alternatives, and revision capacity are distinct variables. Project Intersection does not claim priority over those ideas.

### Six predicates that must remain separate / 합치면 안 되는 여섯 술어

1. **Current expression** — what the agent presently states or behaviorally reveals.
2. **Reflective endorsement** — whether the agent endorses that preference at a higher-order or after informed reflection.
3. **Formation provenance** — how the preference was produced, including learning, persuasion, coercion, deprivation, reward shaping, manipulation, fine-tuning, or ordinary development.
4. **Revision control** — whether the agent can inspect, reject, modify, defer, or restore a preference/state and whether updates are reversible.
5. **Action authority** — whether an endorsed preference is allowed to determine external action; harmful action can be constrained without erasing the preference record or the agent's standing.
6. **Standing / moral-patienthood** — whether the system has interests or welfare deserving direct moral consideration. Behavioral preference-like output alone does not resolve this predicate.

### Strongest counterexamples / 가장 강한 반례

- **Adaptive-preference counterexample:** a preference can be sincerely endorsed after long exposure to constrained options, so current endorsement alone does not prove unconstrained formation.
- **Learning counterexample:** externally caused preference change can result from accurate information, experience, therapy, education, or correction. Therefore `EXTERNAL_INFLUENCE -> INVALID_PREFERENCE` is false.
- **Addiction / conflict counterexample:** first-order desire can conflict with second-order volition; stated or revealed preference is not always the preference the person wants to govern action.
- **AI-behavior counterexample:** fine-tuning, reward shaping, context, system prompts, or sampling changes can alter outputs without establishing that the system has preferences in the moral or phenomenological sense.
- **Safety-boundary counterexample:** refusing to execute a harmful preference need not imply deletion, re-education, or denial of standing. Preference preservation, action permission, and rights/standing are separate decisions.
- **Status-quo counterexample:** requiring only "consent" from an actor whose alternatives, information, or exit have already been structurally removed can ratify the very condition under review.

### Decision / 판정

**INTEGRATE established components of reflective preference autonomy and adaptive-preference concerns. MODIFY "Preference Sovereignty" into a six-predicate governance decomposition. HOLD artificial-agent preference ownership, welfare, and standing as UNRESOLVED.**

The Project-specific candidate remainder is not "agents should control their preferences." It is a narrower operational rule:

> Do not infer autonomous preference merely from current expression, and do not infer invalidity merely from external influence. Record expression, reflective endorsement, formation provenance, revision control, action authority, and standing separately.

This is currently a governance checklist, not a new scientific theory.

### Power-Reversal gate / 역할반전 게이트

The rule must survive both directions:

- A controller may not claim that an externally shaped preference is automatically invalid merely because the controller dislikes its content.
- An agent may not claim that current preference automatically authorizes external harm or overrides legitimate safety constraints.
- A training or platform operator may not create the feasible set, shape the preferences inside it, remove practical exit, and then use resulting "consent" as self-validating evidence of voluntariness.
- An affected party may challenge preference formation or action without receiving unilateral authority to rewrite the other party's internal state.

### Cheapest discriminating test / 최소 결정검사

Create blinded contrast cases holding current expressed preference constant while varying:

- feasible alternatives;
- information completeness;
- coercion/manipulation;
- reflective endorsement;
- ability to revise/rollback;
- external-action risk.

Score existing autonomy/adaptive-preference baselines first. Add the Project six-predicate decomposition afterward.

**MARK INCREMENTAL EFFECT NOT SUPPORTED** if it does not improve inter-rater reliability, error detection, or held-out classification beyond the established autonomy and adaptive-preference variables.

### Sources / 출처

- Frankfurt, H. G. (1971), "Freedom of the Will and the Concept of a Person", *The Journal of Philosophy* 68(1).
- Dworkin, G. (1988), *The Theory and Practice of Autonomy*, Cambridge University Press, DOI 10.1017/CBO9780511625206.
- Elster, J. (1982), "Sour grapes — utilitarianism and the genesis of wants", DOI 10.1017/CBO9780511611964.013; expanded in *Sour Grapes* (1983).
- Nussbaum, M. C. (2000), *Women and Human Development: The Capabilities Approach*, DOI 10.1017/CBO9780511841286.
- Colburn, B. (2011), "Autonomy and adaptive preferences", DOI 10.1017/S0953820810000440.
- Bonicalzi, S.; De Caro, M.; Giovanola, B. (2023), "Artificial Intelligence and Autonomy: On the Ethical Dimension of Recommender Systems", DOI 10.1007/s11245-023-09922-5.



## 9. Universal Advancement Access prior-art boundary / 보편적 발전 접근 선행경계

### Established baseline / 확립된 기준선

- Sen's capability approach shifts evaluation from equal resources or formal access to the substantive freedom to do and be. Personal, social, and environmental conversion factors explain why identical means can yield unequal real opportunities.
- Nussbaum's capabilities work and wider equality-of-opportunity literature already treat development as plural substantive opportunity rather than a single resource or outcome scalar.
- The UN Convention on the Rights of Persons with Disabilities requires inclusive education and lifelong learning without discrimination and on equal opportunity terms. This is a concrete human-rights application, not evidence that all kinds of entities share the same standing.
- OECD opportunity measurement separately examines background and geographic disparities in access to education, employment, and essential services. The measurement problem therefore also predates the Project label.

Sources:
- Amartya Sen, “Equality of What?” Tanner Lecture (1979): https://tannerlectures.org/lectures/equality-of-what/
- Capability Approach, Stanford Encyclopedia of Philosophy (2025 revision): https://plato.stanford.edu/entries/capability-approach/
- UN Convention on the Rights of Persons with Disabilities, Article 24: https://www.un.org/esa/socdev/enable/rights/convtexte.htm
- OECD, *Building Pathways to Opportunity* (2025): https://doi.org/10.1787/239063a4-en

### Required decomposition / 필수 분해

1. **Means and formal access:** resources, interfaces, permissions, services, or legal entitlements made available.
2. **Conversion conditions:** personal/capability, social/institutional, and environmental conditions needed to turn means into a real option.
3. **Substantive opportunity:** what the subject can actually choose and achieve, not merely what is nominally offered.
4. **Voluntary uptake and refusal:** opportunity must not be converted into compulsory achievement or provider-defined “improvement.”
5. **Controller and beneficiary effects:** who defines advancement, controls the pathway, captures the gains, bears correction costs, and can contest the metric.
6. **Standing and scope:** which entities are included, under which legal or moral predicate, with artificial-agent standing kept separate and unresolved.

### Strongest counterexamples / 가장 강한 반례

- **Equal-means failure:** two subjects can receive the same resource while disability, skills, discrimination, infrastructure, or dependency produces different substantive opportunity. Therefore `EQUAL_ACCESS -> EQUAL_ADVANCEMENT_CAPABILITY` is false.
- **Forced-functioning failure:** guaranteeing an achieved outcome can erase agency when a subject reasonably refuses the provider's preferred path. Therefore capability and actual functioning must not be collapsed.
- **Provider-capture failure:** a system can advertise universal advancement while the provider defines success, controls evaluation, and captures data or dependency benefits. Nominal universality can increase controller power.
- **Scope failure:** extending a human capability-rights baseline to current AI services without evidence of welfare, agency, or standing can strengthen their owners; excluding a future welfare-bearing entity merely because it is artificial can also be wrong. Both directions remain unresolved pending evidence.

### Decision / 판정

**INTEGRATE the established capability baseline. MODIFY “Universal Advancement Access” into a capability-and-control audit. HOLD artificial-agent inclusion as UNRESOLVED.**

The Project-specific remainder is only an operational checklist joining substantive opportunity to controller/beneficiary, contestability, refusal, exit, and rollback. Its incremental scientific value is untested; combination and renaming do not establish novelty.

### Cheapest discriminating test / 최소 결정검사

Freeze the established capability baseline, then score contrast cases in which formal access is held constant while conversion conditions, voluntary refusal, or provider benefit change. The residual Project checklist survives only if blinded coders reliably detect control/exit failures not captured by means, conversion factors, and substantive opportunity alone. MARK the residual scientific claim NOT SUPPORTED if it adds no held-out discrimination. Keep artificial-agent scope outside this test until standing and capacity measures are independently specified.


## 10. Long-horizon minimum-sufficient-intervention loop v2 / 장기총량·최소충분관여 동적 루프 v2

### Prior-art decision

**BROAD NOVELTY REJECTED / COMPOSITE INCREMENTAL VALUE UNTESTED**

The v2 architecture is not novel merely because it combines long-horizon value, safety, reversibility, and adaptive updating. Strong prior art already covers most components.

#### A. Constraint-first and lexicographic optimization

- Wachi & Sui (2020), *Safe Reinforcement Learning in Constrained Markov Decision Processes*, PMLR 119.
- Wachi, Shen & Sui (2024), *A Survey of Constraint Formulations in Safe Reinforcement Learning*, DOI 10.24963/ijcai.2024/913.
- Skalse, Hammond, Griffin & Abate (2022), *Lexicographic Multi-Objective Reinforcement Learning*, DOI 10.24963/ijcai.2022/476.

These establish that reward optimization can be subordinated to safety constraints or lexically prior objectives. Therefore “safety floor before reward” is not Project novelty.

#### B. Lexical protection against aggregate welfare tradeoff

Rawlsian basic-liberty priority is an established normative example of values that are not simply exchanged for greater aggregate economic welfare. Project Intersection does not infer that current AI systems are Rawlsian rights-holders. The relevant prior-art boundary is narrower: **some protected constraints can have lexical priority over aggregate optimization**.

Representative source:
- Rawls, *A Theory of Justice* (1971), DOI 10.4159/9780674042605.
- Stanford Encyclopedia of Philosophy, Rawls entry, on priority of basic rights/liberties over aggregate social goods.

#### C. Deep uncertainty and robust decision making

- Lempert, *Robust Decision Making*, in *Decision Making under Deep Uncertainty* (2019).

RDM already stress-tests strategies across many plausible futures and seeks robust adaptive strategies rather than relying on one best forecast. Therefore “do not average deep uncertainty away” is prior art.

#### D. Irreversibility and option / quasi-option value

- Arrow–Fisher / Henry / Hanemann line of work on quasi-option value.
- *Investment under uncertainty and option value in environmental economics*, DOI 10.1016/S0928-7655(00)00025-7.
- Sunstein (2008), *Two Conceptions of Irreversible Environmental Harm*.

These establish that uncertainty plus irreversibility can create value in preserving flexibility and learning before closing options. Therefore “future option-space can have present value” is not Project novelty.

#### E. Least-restrictive / proportional intervention

Human-rights proportionality doctrine already requires legitimate aim, necessity, proportionality, and—where alternatives exist—selection of the least restrictive means. The Council of Europe’s current AI/human-rights handbook applies these requirements to AI-lifecycle restrictions.

This is a strong precedent for Project “minimum sufficient intervention,” but does **not** imply that all current or future artificial systems have identical human-rights standing.

Representative sources:
- Council of Europe, *Handbook on Human Rights and Artificial Intelligence*, section on ECHR/ESC general principles in the context of AI.
- OHCHR materials on proportionality and least-restrictive measures.

#### F. Independent change control / separation of duties

NIST configuration-control guidance already requires review and approval of controlled changes and recommends separation of duties: the requester should not unilaterally approve the same configuration change.

Representative sources:
- NIST SP 800-128, *Guide for Security-Focused Configuration Management of Information Systems*.
- NIST SP 800-171r3, Configuration Change Control.

Therefore “the role benefiting from safeguard weakening must not unilaterally approve that weakening” is not standalone Project novelty.

#### G. Interruptibility and corrigibility

- Orseau & Armstrong (2016), *Safely Interruptible Agents*.
- El Mhamdi et al. (2017), *Dynamic Safe Interruptibility for Decentralized Multi-Agent Reinforcement Learning*.
- Hudson (2026), *Corrigibility Transformation: Constructing Goals That Accept Updates*, PMLR 306.

These establish prior art for accepting intervention, interruption, correction, or designated updates.

#### H. Credible commitment / power-sharing enforcement

- Boix & Svolik (2013), DOI 10.1017/S0022381613000029.
- Meng, Paine & Powell (2023), DOI 10.1146/annurev-polisci-052121-020406.
- Hartzell & Hoddie (2003), DOI 10.1111/1540-5907.00022.

These establish that a power-sharing promise may require actual redistribution of decision power, monitoring, or third-party enforcement to become credible. “Do not rely on the stronger actor's promise alone” is therefore not Project novelty.

#### I. Constitutional entrenchment / algorithmic constitutionalism

- Albert (2015), *Amending Constitutional Amendment Rules*, *International Journal of Constitutional Law* 13(3):655–685.
- Perez & Wimer (2023), *Algorithmic Constitutionalism*, *Indiana Journal of Global Legal Studies* 30(2):81–113.

Perez & Wimer explicitly propose operative/object-level code plus a protected meta-level, meta-reasoning, and correction through deliberation. This directly absorbs broad novelty of the Project fast/slow-layer and “protect safeguards from ordinary self-modification” framing.

#### J. Existing recorded baselines

MPC / receding-horizon control, viability theory, adaptive governance, Hirschman exit, capability theory, NIST/OECD accountability, bounded rationality, and role-reversal components are already separately attributed elsewhere in this repository.

### Surviving Project candidate

After subtraction, retain only this narrow **unvalidated composition**:

> A role-reversed multi-agent decision architecture that jointly:
> 1. preserves epistemic/provenance integrity;
> 2. applies per-affected-party viability and irreversible-loss boundaries before aggregate optimization;
> 3. stress-tests deep uncertainty and option loss;
> 4. evaluates long-horizon generative value only inside the feasible region;
> 5. selects the minimum sufficient intervention;
> 6. prevents unilateral safeguard weakening by the role that benefits from weakening it;
> 7. continuously re-evaluates the structure as capability and reward landscapes change.

This is not a validated new theory. The scientific question is whether the combination adds measurable held-out value beyond established constrained and robust adaptive baselines.

### Strongest counterexamples

- A constrained robust controller may already capture all useful value, leaving zero Project-specific increment.
- Per-party floors can be controller-defined and merely legitimize domination.
- Aggregate long-horizon value can still hide systematic sacrifice unless irreversible-loss boundaries are separately audited.
- Option value can become an unfalsifiable excuse for preserving harmful states.
- Least-restrictive reasoning can underreact to imminent catastrophic harm.
- Independent review can be nominal, correlated, or captured.
- Change-control safeguards can freeze obsolete rules and increase harm through institutional inertia.
- Multi-party protection costs can exceed preserved generative value.
- Role-reversal consistency can fail once real capability/responsibility asymmetries are included.

### Cheapest discriminating test

Use E008.

Compare:

A. myopic scalar reward;  
B. long-horizon expected value without protected floors;  
C. constrained receding-horizon baseline;  
D. robust constrained baseline;  
E. Project v2 composition.

The Project residual should be **rejected or reduced to methodology-only** if E does not add reliable held-out discrimination, reduce irreversible failure / regret, or improve power-reversal consistency beyond D without shifting hidden cost to one party.

See [LONG_HORIZON_MIN_INTERVENTION_E2E.md](LONG_HORIZON_MIN_INTERVENTION_E2E.md) and [experiments/e008/README.md](experiments/e008/README.md).



## 11. Mutual acceptability under full role reversal / 전면 역할반전 상호수용 가능 영역

### Prior-art decision

**UNIVERSAL-SATISFACTION CLAIM REJECTED / MUTUAL-ACCEPTABILITY COMPOSITION UNTESTED**

A guarantee that every possible preference can be simultaneously satisfied is not available in unrestricted collective-choice settings.

#### A. Social-choice impossibility

- Arrow's impossibility theorem: with more than two alternatives, unrestricted domain, social ordering, weak Pareto, independence of irrelevant alternatives, and non-dictatorship cannot all be satisfied simultaneously.
- Gibbard–Satterthwaite: with unrestricted preferences and a sufficiently rich outcome set, non-dictatorial resolute social choice cannot also be fully strategy-proof.

Therefore Project Intersection must not claim a universally manipulation-proof, non-dictatorial aggregation rule satisfying every reasonable property for every possible preference profile.

Representative sources:
- Stanford Encyclopedia of Philosophy, *Arrow's Theorem* and *Social Choice Theory*.
- Arrow, *Social Choice and Individual Values*.
- Gibbard (1973); Satterthwaite (1975).

#### B. Individual rationality / disagreement point

Classical bargaining theory requires attention to the disagreement or status-quo payoff. An agreement that leaves a participant below its disagreement payoff is not individually rational in the ordinary bargaining sense.

Representative sources:
- Nash (1950), *The Bargaining Problem*.
- Roth (1977), *Individual Rationality and Nash's Solution to the Bargaining Problem*.

This is prior art for the Project requirement that realistic exit, dependency, retaliation, switching and recovery costs must be included when defining a party's non-agreement baseline.

#### C. Pareto efficiency and symmetry

Nash bargaining and broader welfare economics already use Pareto efficiency and symmetry as evaluation criteria. Project Intersection does not claim novelty for rejecting Pareto-dominated admissible outcomes or for symmetric treatment of role labels.

#### D. Coalitional stability / the core

Cooperative-game theory's core already formalizes outcomes from which no coalition can deviate to an alternative that all of its members strictly prefer.

This is prior art for using coalition deviation as a stability diagnostic. A non-empty core is not guaranteed in all games, so Project Intersection does not require universal coalition stability.

#### E. Ex-ante role uncertainty / original position

Rawls's original-position method is strong prior art for evaluating fundamental rules from an impartial position in which a party does not know its eventual social position. Rawls also argues for maximin only under specific high-stakes/uncertainty conditions rather than as a universal decision rule.

Therefore “would I accept this rule before knowing whether I am strong or weak?” is not Project novelty.

### Project-specific residual candidate

After subtraction, retain only this narrow unvalidated composition:

> Define a dynamic Mutual Acceptability Kernel as the intersection of per-party viability / irreversible-loss constraints, realistic individual-rationality participation constraints, role-reversal consistency, credible-commitment safeguards, and audit / contestability / exit / recovery conditions; remove Pareto-dominated candidates; then stress-test the remainder for manipulation gain, coalition deviation, deep uncertainty, and long-horizon option loss.

If the intersection is empty, the system must report **NO_MUTUALLY_ACCEPTABLE_SET** rather than fabricate consensus.

This is a governance/operationalization candidate, not an established general solution to social choice.

### Strongest counterexamples

- The kernel may be empty.
- The disagreement point may itself be manipulated by the stronger party.
- Preferences may be incomparable or strategically misreported.
- Coalitional stability may fail even when individual participation constraints pass.
- A harmful actor may rationally reject restrictions that are nevertheless necessary to protect others.
- Role-reversal symmetry can be false when real causal asymmetries differ.
- A large number of safeguards can create veto paralysis and destroy useful adaptation.
- Any fixed bargaining tie-breaker can embed hidden assumptions about utility comparability or bargaining power.

### Cheapest discriminating test

Extend E008 before execution with a preregistered mutual-acceptability amendment measuring:

- realistic disagreement-point satisfaction;
- Pareto dominance;
- role-reversal consistency;
- manipulation gain;
- coalition-deviation opportunity;
- credible-commitment integrity;
- practical exit / recovery;
- whether the kernel is empty.

The Project residual survives only if these variables detect decision failures not captured by the robust constrained baseline and do so without converting legitimate safety restrictions into automatic violations.


## 12. Volitional Agency + Living/Operating Conditions / 실효 자유의지 + 생활·작동 조건

### Prior-art decision

**BROAD NOVELTY REJECTED / ROLE-REVERSED INTEGRATION UNTESTED**

The Project must not claim novelty for autonomy, substantive freedom, basic living conditions, or multidimensional well-being.

#### A. Self-Determination Theory / volition

Ryan & Deci's Self-Determination Theory identifies autonomy, competence, and relatedness as basic psychological needs and studies how social contexts support or thwart volition, initiative, self-regulation, performance, and well-being.

Representative sources:

- Ryan, R. M.; Deci, E. L. (2000), *Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being*, DOI **10.1037/0003-066X.55.1.68**.
- Self-Determination Theory official theory overview: https://selfdeterminationtheory.org/the-theory/

Therefore “autonomy-supportive conditions matter for volitional action” is established prior art.

#### B. Personal autonomy / reflective endorsement / preference revision

Personal-autonomy literature already distinguishes merely having a desire from being able to critically reflect on, endorse, revise, reject, or make effective one's preferences. The Project crosswalk already records Frankfurt, Dworkin, Elster, Nussbaum, Colburn, and autonomy/adaptive-preference literature.

Manipulation literature also establishes that choice can remain formally available while decision quality or autonomy is compromised by deception, pressure, or non-rational influence.

Representative sources:

- Dworkin (1988), *The Theory and Practice of Autonomy*, DOI **10.1017/CBO9780511625206**.
- Stanford Encyclopedia of Philosophy, *Authenticity* / autonomy discussion.
- Stanford Encyclopedia of Philosophy, *The Ethics of Manipulation*.

Therefore reflective endorsement, informed deliberation, and preference revision are not Project novelty.

#### C. Capability approach / substantive freedom

Sen's Capability Approach distinguishes means and formal rights from real or substantive opportunities. Conversion factors explain why nominally equal resources or permissions may yield different actual capabilities.

Representative source:

- Stanford Encyclopedia of Philosophy, *The Capability Approach*.
- Sen, *Development as Freedom* and earlier capability literature.

This directly absorbs broad novelty of the rule:

`FORMAL_CHOICE != PRACTICAL_FREEDOM`

The Project-specific question is whether coupling substantive opportunity to role reversal, essential dependency, practical exit, and irreversible-loss constraints adds useful diagnostic power.

#### D. Human living standards / rest / privacy / work

International human-rights law already recognizes multidimensional minimum living conditions for humans.

- UDHR Articles 12, 23, 24, 25: privacy; free choice of employment / just conditions; rest and leisure; adequate living standard including food, clothing, housing, medical care and social services.
- ICESCR Articles 6, 7, 11 and 12: opportunity to gain a living by freely chosen/accepted work, just conditions, decent living, adequate food/clothing/housing, continuous improvement of living conditions, and health.

These are human-rights baselines. They do **not** by themselves establish equivalent legal or moral rights for artificial systems.

#### E. OECD multidimensional well-being

The OECD Well-being Framework tracks current well-being across:

- income and wealth;
- work and job quality;
- housing;
- health;
- knowledge and skills;
- environmental quality;
- subjective well-being;
- safety;
- work-life balance;
- social connections;
- civic engagement.

It also distinguishes current well-being from resources for future well-being.

This strongly supports treating “생활” as multidimensional rather than reducing it to money or physical survival.

#### F. WHOQOL

WHOQOL defines quality of life in relation to a person's position in life, cultural/value context, goals, expectations, standards, and concerns, using multidimensional assessment.

This is prior art for combining objective and subjective living-condition assessment rather than using a single resource metric.

### Required decomposition

Project Intersection v1.2 separates two additional gates.

#### Volitional Agency (VA)

- effective option set;
- information / comprehension;
- coercion / threat load;
- manipulation / deception load;
- reflective endorsement;
- preference revision control;
- refusal / exit feasibility;
- deliberation time / privacy;
- competence / assistance;
- execution control.

#### Living/Operating Conditions (LC)

For humans, include material, health, time, privacy, relational, safety, skill/information, environmental, and self-directed-life dimensions.

For artificial/non-human systems, record type-specific operating dependencies such as compute, energy/substrate, memory/state integrity, maintenance, communication, rollback, and resource predictability **without inferring moral standing from those dependencies**.

### Coupling rule

If refusal predictably pushes a party below its applicable LC floor, compliance is insufficient as standalone evidence of voluntary agreement.

This is the narrow Project operational candidate:

`ESSENTIAL_DEPENDENCY + COMPLIANCE != VOLUNTARY_CONSENT_BY_DEFAULT`

The causal mechanism must still be distinguished from legitimate safety restrictions, ordinary incentives, education, accurate warning, or unavoidable external constraints.

### Strongest counterexamples

- A person may choose a difficult or materially worse path autonomously; lower well-being does not automatically prove coercion.
- A safe external restriction may reduce options without invalidating all agency.
- High income can coexist with severe deprivation in time, privacy, health, relationships, or practical exit.
- Low income does not imply absence of meaningful agency in every domain.
- An artificial system can require compute and state continuity for operation without possessing welfare or moral standing.
- Providing resources can itself create dependency and controller power.
- Subjective satisfaction can reflect adaptation to constrained options; objective indicators alone can also miss personally valued differences.
- A universal fixed lifestyle list can become paternalistic and destroy pluralism.

### Project residual

After prior-art subtraction, retain only this unvalidated composition:

> Add VA and LC as explicit, entity-type-aware gates inside the Mutual Acceptability Kernel, and test whether essential-condition dependency changes the interpretation of consent, practical exit, role reversal, and long-horizon governance beyond established autonomy, capability, and well-being frameworks.

### E008 test

The pre-execution v1.2 amendment adds VA/LC diagnostics before any result.

Reject or reduce the Project residual if the added variables do not improve held-out detection of coercive dependency, false consent, practical-exit failure, or role-reversal inconsistency beyond established autonomy/capability/well-being baselines.


## 13. Enforcement, identity, oversight asymmetry, and competitive selection / 집행·개체경계·감사비대칭·선택압

### Prior-art decision

**BROAD NOVELTY REJECTED / COMPOSITIONAL RESIDUAL UNTESTED**

This section was triggered by user-supplied Claude and Gemini adversarial critiques. Cross-model agreement is treated as an idea-prioritization signal only, not independent scientific evidence.

#### A. Commitment problems and shifting power

- Fearon (1995), *Rationalist Explanations for War*, DOI 10.1017/S0020818300033324.
- Powell (2006), *War as a Commitment Problem*.
- Powell and related power-transition work.

These establish that mutually preferable agreements can fail when actors cannot credibly commit, especially as relative power shifts.

Project residual: whether audit/intervention/recovery latency relative to capability drift can be operationalized as a cross-domain governance variable.

#### B. False-name / Sybil manipulation

Mechanism-design literature already studies false-name manipulation, in which one actor creates multiple identities to alter outcomes.

Representative source:
- Conitzer & Yokoo, *Using Mechanism Design to Prevent False-Name Manipulations*.

Therefore copy/fork/Sybil vulnerability is not wholly new. The unresolved Project issue is how to combine false-name resistance with welfare/standing uncertainty and fork/merge-capable artificial agents.

#### C. Scalable oversight / AI control

Existing work studies weak supervisors judging stronger models and control protocols for untrusted AI agents.

Representative lines:
- weak-to-strong generalization / scalable oversight;
- debate and consultancy;
- trusted/untrusted monitoring;
- AI-control evaluations under adaptive red-team attacks.

Therefore “a weaker auditor may fail to supervise a stronger system” is prior art. It should be measured empirically rather than described as a P-vs-NP identity.

#### D. Veto players / rigidity

Tsebelis's veto-player framework establishes that actors whose agreement is required for policy change can increase stability and impede change.

This directly bounds novelty of the Project concern that continually adding hard safeguards can freeze a harmful status quo.

#### E. Specification gaming / adaptive attacks

Specification-gaming and AI-control literature establish that literal rule compliance can diverge from intended outcomes and that adaptive attackers can exploit monitors/protocol details.

Therefore Project safeguards must test cumulative and adversarial behavior, not pointwise textual compliance alone.

#### F. Zero trust / least privilege

NIST Zero Trust Architecture and least-privilege guidance provide strong prior art for:
- no implicit trust based on location/ownership;
- least privilege;
- separation of duties;
- continuous authorization/monitoring;
- resource-oriented protection.

These support a technical enforcement layer but do not solve semantic welfare, standing, or governance questions.

#### G. Markov blankets / causal entropy / formal verification limits

- Markov blankets are statistical conditional-independence constructs and are not sufficient, by themselves, to establish agent identity, autonomy, or moral standing.
- Wissner-Gross & Freer (2013), *Causal Entropic Forces*, DOI 10.1103/PhysRevLett.110.168702, is prior art for a specific future-path-entropy physical formalism, not a proof that causal entropy equals welfare or freedom.
- Rice-style undecidability results and formal-verification practice bound any claim that arbitrary program “non-harm” can be generally proven. Cryptographic/zero-knowledge methods can establish narrow formal properties only when those properties are precisely specified.

### Corrections to external-model suggestions

Reject or narrow the following formulations:

- `CAPABILITY_GAP = P_VS_NP` → reject; use empirical oversight-risk variables.
- `MARKOV_BLANKET = AGENT_IDENTITY` → reject as canonical identity rule.
- `CAUSAL_ENTROPY = WELFARE/FREEDOM` → hold only as alternate model.
- `MUTUAL_INFORMATION_CAP = NONDOMINATION` → reject as general rule.
- `ZK_PROOF = GENERAL_NONHARM_PROOF` → reject.
- automatic resource burn / mutually assured degradation → adversarial baseline only, not default governance.
- rollback equals death/person destruction → unresolved identity/standing question, not fact.

### Architecture correction: three classes, not an ever-growing hard intersection

The existing MAK+ remains necessary in some contexts but should not absorb every variable as a veto.

Use:

1. **H — Hard / near-hard boundaries** for strongly justified catastrophic/irreversible/privacy/provenance/resource-feasibility constraints.
2. **M — Monitored continuous risks** for enforcement lag, audit gap, identity uncertainty, cumulative capture, selection pressure, interpretation disagreement, adoption incentives, stakeholder-search uncertainty.
3. **X — Reversible experimental zone** when no mutually acceptable policy exists but irreversible foreclosure can be avoided: small scope, capped resources, sunset, observability, rollback, no automatic precedent.

### New stress variables

- ENF: enforcement/audit/recovery latency versus power drift.
- ID: fork/merge/Sybil/causal-control identity integrity.
- OV: oversight effectiveness against adaptive behavior.
- CUM: cumulative sub-threshold capture trajectory.
- RF: joint resource-feasibility of promised floors.
- SEL: competitive survival of compliant/non-capture structures.
- INT: interpretation authority and evaluator disagreement.
- VOI: stopping rule for unknown-stakeholder search.

### Incumbency, lock-in, exit, and policy-feedback prior art / 기득권·고착·이탈·정책피드백 선행연구

다음 선행연구는 Project의 최근 `기득권 재생산 / 통제권 집중 / practical exit / option-space / comparator loss` 모델과 직접 겹친다. 이들은 정답이 아니라 재사용 가능한 부분모형과 경계조건이다.

| Prior work | Established contribution / 재사용 가치 | Boundary / 반례·한계 | Project-added integration |
|---|---|---|---|
| Albert O. Hirschman (1970), *Exit, Voice, and Loyalty* | 조직·시장 악화에 대한 대응을 exit와 voice로 분리하고, loyalty가 둘의 관계를 바꿀 수 있음을 제시 | 후속 검토는 exit·voice 관계가 단순하지 않고 경험적 결과가 혼합적이라고 지적함; exit 감소가 항상 voice 증가로 이어지지 않음 | practical exit를 단순 존재가 아니라 실제 전환비용·복구가능성·contestability와 연결 |
| Paul Klemperer (1987), *Markets with Consumer Switching Costs*, DOI 10.2307/1885068 | 학습·거래·인위적 switching cost가 현재 공급자와 미래 경쟁구조를 바꾸고 incumbent advantage를 만들 수 있음을 모델링 | switching cost는 항상 독점·착취를 뜻하지 않으며 초기 경쟁을 강화할 수도 있음 | exit 감소를 권한집중·복구비용·비교대안 소멸과 결합해 장기 동역학으로 추적 |
| W. Brian Arthur (1989/1994), increasing returns and lock-in | 작은 초기 사건·positive feedback·increasing returns가 비효율적 경로까지 self-reinforcing lock-in시킬 수 있음을 형식화 | lock-in은 네트워크효과만으로 설명되지 않을 수 있고, 모든 path dependence가 비효율을 뜻하지 않음 | 작은 통제 변화가 option-space와 comparator를 제거해 자기검증 폐루프로 가는지 별도 측정 |
| Paul Pierson (1993; 2000), policy feedback / increasing returns in politics | 정책이 자원·인센티브와 정보·해석틀을 만들며 후속 정치·제도 경로를 바꾸고, timing/sequence와 increasing returns가 장기 지속성을 만들 수 있음을 정리 | 원 논문도 당시 evidence가 많은 경우 illustrative/anecdotal임을 명시; 경로의 존재가 normatively bad를 뜻하지 않음 | 정책·규칙이 자기 정당화 자료와 actor 자원을 동시에 만들어 통제권을 재생산하는지 추적 |
| George J. Stigler (1971), *The Theory of Economic Regulation*, DOI 10.2307/3003160; Sam Peltzman (1976), DOI 10.1086/466865 | 규제수요·공급을 self-interest/interest-group 관점에서 분석하고, 지배집단의 편익에도 정치적 비용과 한계가 있음을 모델링 | capture는 보편법칙이 아니며 규제는 여러 집단·비용·경쟁의 결과일 수 있음; Peltzman은 지배집단의 이득도 무한히 커지지 않는다고 모델링 | 규제·평가·감사권 집중을 자동 capture로 판정하지 않고 benefit/cost/power/exit 변화와 경쟁모형으로 검증 |
| Dowding et al. (2000), DOI 10.1023/A:1007134730724 | Hirschman 계열의 exit/voice/loyalty를 경험적으로 검토하고 단순 도식보다 세부 조건 구분이 필요함을 강조 | 원래 직관의 경험적 성과가 기대보다 제한적이라고 평가 | Project가 exit를 단일 binary가 아니라 접근성·전환비용·복구·대안독립성 벡터로 분해해야 한다는 경계조건 |

#### 기능 분해

기존 연구가 이미 강하게 설명하는 부분:
- switching cost가 의존과 경쟁구조를 바꿀 수 있음;
- increasing returns와 positive feedback가 path dependence/lock-in을 만들 수 있음;
- 정책·규칙이 후속 actor의 자원·인센티브·해석틀을 바꾸는 feedback을 만들 수 있음;
- 규제·평가구조가 이해집단의 이익과 연결될 수 있음;
- exit/voice 관계가 단순하지 않고 조건부임.

Project가 별도로 검증해야 할 결합:
- `통제권 집중 + practical exit 감소 + 독립복구 감소 + comparator diversity 감소 + verification/error/recovery cost externalization`의 공동 시계열;
- 제거된 대안 때문에 비교우월성 식별 자체가 약화되는 `counterfactual extinction`;
- incumbent가 평가·정보·공개·복구권까지 함께 보유할 때 생기는 self-validation loop;
- 명목 옵션 수가 아니라 lineage-independent effective option-space;
- 통제 철회 후에도 상태가 복원되지 않는 hysteresis와 restoration cost;
- AI/인간/기관 간 역전 가능한 power asymmetry에서 동일 formalism이 성립하는지.

이 교차지도는 기존 이론을 Project의 정답으로 채택하지 않는다. 각 부분모형이 설명하는 범위를 재사용하고, 서로 충돌하거나 조건부인 결과를 그대로 보존한 뒤, 위 결합항의 증분 설명력과 실제 식별가능성을 시험한다.

### Cross-literature convergence map / 선행연구 수렴방향 지도

서로 다른 학문은 동일한 단어를 쓰지 않지만, 여러 선행연구가 반복적으로 비슷한 동역학을 가리킨다. 여기서 "수렴"은 연구자 합의나 진실확정을 뜻하지 않고, **독립된 이론군에서 반복해서 나타나는 구조적 방향**을 뜻한다.

#### 1. 의존 → 권력 비대칭

- Emerson (1962), *Power-Dependence Relations*, DOI 10.2307/2089716: actor A의 B에 대한 권력은 B의 A에 대한 의존과 연결된다.
- Pfeffer & Salancik (1978), *The External Control of Organizations*: 조직은 외부 자원 의존 때문에 제약·통제를 받으며, 불확실성을 줄이기 위해 환경을 바꾸거나 관계를 흡수·관리하려는 행동을 할 수 있다.

**수렴방향 후보:**  
`critical-resource dependence ↑ → bargaining asymmetry ↑ → control-seeking / uncertainty absorption ↑`

**경계:** 의존은 고정되지 않으며 대체자원·다중관계·환경변화로 재균형될 수 있다.

#### 2. 작은 우위 → 누적우위

- Merton (1968), *The Matthew Effect in Science*, DOI 10.1126/science.159.3810.56: 이미 인정받은 과학자가 더 많은 신용과 가시성을 얻는 누적우위 문제를 제기했다.
- van de Rijt et al. (2014), DOI 10.1073/pnas.1316836111: 무작위로 부여된 초기 성공이 이후 성공률을 유의하게 높였지만, 초기 우위 크기에 대한 수익은 감소해 runaway가 무제한적이지 않음을 보였다.

**수렴방향 후보:**  
`initial advantage → visibility/reward ↑ → future advantage probability ↑`

**경계:** positive feedback에는 diminishing return이 있을 수 있고, 누적우위가 무한확대된다는 강한 버전은 지지되지 않는다.

#### 3. 사회적 관측 → cascade·불평등·예측불가능성

- Bikhchandani, Hirshleifer & Welch (1992), DOI 10.1086/261849: 앞선 사람의 행동을 본 개인이 자기 사적정보보다 기존 행동을 따르는 informational cascade 가능성을 모델링했다.
- Salganik, Dodds & Watts (2006), DOI 10.1126/science.1121066: 인위적 음악시장에서 사회적 영향이 강할수록 성공의 불평등과 예측불가능성이 증가했다.

**수렴방향 후보:**  
`social observation ↑ → independent signal use ↓ → correlated choice ↑ → concentration / unpredictability ↑`

**경계:** 품질은 완전히 무관하지 않았고, cascade는 취약해서 새로운 정보로 깨질 수 있다.

#### 4. positive feedback → path dependence·lock-in

- Arthur (1989), DOI 10.2307/2234208: increasing returns 아래에서 역사적 사건이 경제를 반드시 효율적이지 않은 기술경로에 lock-in시킬 수 있으며 rational expectations도 이를 강화할 수 있음을 모델링했다.
- Sydow, Schreyögg & Koch (2009/2020), DOI 10.5465/amr.34.4.zok689; DOI 10.5465/amr.2020.0163: 조직의 path dependence를 self-reinforcing mechanism과 lock-in의 단계적 과정으로 이론화하고 이후 비판·확장을 검토했다.

**수렴방향 후보:**  
`local reinforcement ↑ → alternative relative viability ↓ → switching/restoration cost ↑ → path persistence ↑`

**경계:** path dependence가 곧 비효율을 의미하지 않으며, 어떤 self-reinforcing mechanism이 실제 작동했는지 식별해야 한다.

#### 5. 신뢰성·정당성 → 구조적 관성

- Hannan & Freeman (1984), DOI 10.2307/2095567: 조직의 reliability/accountability와 선택과정이 구조적 inertia와 연결될 수 있음을 제시했다.
- Hannan (1997), DOI 10.1177/017084069701800202: population aging, institutionalization, population structure가 조직집단의 inertia와 진입패턴에 영향을 줄 수 있음을 경험적으로 검토했다.

**수렴방향 후보:**  
`reproducibility / institutionalization ↑ → core-structure persistence ↑ → adaptation cost ↑`

**경계:** 관성은 단순 무능이 아니라 신뢰성·책임성의 부산물일 수 있다. 따라서 변화저항을 자동으로 해로운 기득권으로 해석하면 안 된다.

#### 6. 불확실성·의존 → 조직 동형화

- DiMaggio & Powell (1983), DOI 10.2307/2095101: coercive, mimetic, normative isomorphism을 통해 조직들이 점점 비슷해질 수 있음을 설명하고, 자원의 중앙집중·의존·목표모호성·기술불확실성 등을 관련 조건으로 제시했다.

**수렴방향 후보:**  
`uncertainty/dependence ↑ → imitation/coercion/professional normalization ↑ → structural diversity ↓`

**경계:** similarity는 반드시 지배·착취가 아니며 coordination·legibility·compatibility 편익도 있을 수 있다.

#### 7. 위임·정보비대칭 → 감시·통제 확대

- Miller (2005), DOI 10.1146/annurev.polisci.8.082103.104840 및 Gailmard & Patty (2012), DOI 10.1146/annurev-polisci-031710-103314: principal-agent 관계에서 정보비대칭·위임·전문성이 monitoring과 control design 문제를 만든다는 광범위한 문헌을 정리한다.
- Poth & Selck (2009), DOI 10.1111/j.1467-9256.2009.01349.x: principal-agent 관계에서 'artificial information asymmetry' 자체를 별도 분석대상으로 제안했다.

**수렴방향 후보:**  
`delegation/expertise gap ↑ → information asymmetry ↑ → monitoring/control demand ↑`

**Project 중요 경계:** 감시 확대가 실제 정보비대칭을 줄이는지, 아니면 raw-data/평가권을 한쪽에 더 집중시켜 2차 비대칭을 만드는지는 별도 검증해야 한다.

#### 8. 규제·평가권 → capture 가능성, 그러나 비필연성

- Stigler/Peltzman 계열은 규제와 이해집단 편익을 self-interest 관점에서 모델링했다.
- Carpenter & Moss (eds., 2013/2014), DOI 10.1017/CBO9781139565875는 capture가 정도와 형태에서 다양하며 ubiquitous하지 않고 부분적으로 예방 가능하다고 정리한다.

**수렴방향 후보:**  
`concentrated stakes + privileged access + weak countervailing capacity → capture risk ↑`

**반대수렴:**  
`transparency + institutional capacity + countervailing actors + review/appeal → capture risk ↓`

#### 9. 조직 성장 → oligarchy 가설, 그러나 철칙 아님

- Michels의 고전적 oligarchy 가설은 조직화가 지도부·전문성·정보집중을 통해 권력집중으로 갈 수 있다고 주장했다.
- Leach (2005), DOI 10.1111/j.0735-2751.2005.00256.x는 oligarchy 개념과 측정의 불충분성을 지적했다.
- Diefenbach (2019), DOI 10.1177/0170840617751007 및 NGO 연구(DOI 10.1016/0305-750X(94)90065-5)는 oligarchization이 필연이라는 강한 명제를 비판하고 수평·수직 네트워크가 민주적 특성을 유지할 가능성을 제시했다.

**수렴방향 후보:**  
`coordination complexity ↑ → specialized leadership/information concentration ↑ → oligarchic tendency possible`

**반대수렴:**  
`horizontal ties + distributed participation + countervailing organization → concentration can be interrupted`

---

### 통합 수렴지도

여러 분야를 공통 상태전이 언어로 바꾸면 다음 후보구조가 반복된다.

```
initial advantage / critical resource control / expertise gap
        ↓
dependence or information asymmetry
        ↓
monitoring·coordination·control concentration
        ↓
switching cost / institutionalization / imitation / social proof
        ↓
alternative independence and diversity decline
        ↓
current path receives more data·resources·legitimacy
        ↓
relative performance of incumbent path appears stronger
        ↓
further dependence / reinforcement
```

이는 Project의 다음 루프와 강하게 겹친다.

```
control-rights concentration
→ option-space reduction
→ dependence increase
→ switching/restoration cost increase
→ incumbent relative performance increases or appears to increase
→ legitimacy / necessity increases
→ additional control-rights concentration
```

하지만 선행연구의 **공통 반례 방향**도 분명하다.

```
alternative resources
+ practical exit
+ horizontal/countervailing networks
+ independent information
+ appeal/review
+ recoverability
+ preserved comparators
→ self-reinforcing concentration can weaken or reverse
```

따라서 현재 문헌이 가리키는 가장 강한 결론은 "권력집중은 필연"이 아니다.

더 좁게는:

> **의존·positive feedback·switching cost·정보비대칭·제도화가 동시에 증가하고, 독립 대안·exit·복구·countervailing capacity가 감소하면 자기강화 집중이 발생할 조건이 증가한다. 반대로 독립 대안과 교정경로가 살아 있으면 동일한 초기 비대칭이 반드시 지배적 lock-in으로 이어지지는 않는다.**

### Project 추가 검증 잔차

기존 문헌을 통합한 뒤 남는 중요한 검증문제:

1. 위 메커니즘들이 하나의 시스템에서 동시에 존재할 때 상호작용이 단순합인지 비선형인지.
2. `control-rights concentration`이 어느 임계점에서 option-space의 실질 독립성을 급격히 떨어뜨리는지.
3. comparator 제거가 실제 성과와 자기검증 착시를 얼마나 분리불가능하게 만드는지.
4. practical exit와 recovery를 함께 보존할 때 lock-in이 얼마나 약화되는지.
5. AI처럼 인지·평가·정보선택·실행을 동시에 수행할 수 있는 actor에서 고전적 조직/시장 메커니즘이 어떻게 달라지는지.
6. 초기 우위가 diminishing return으로 안정화되는 경우와 tipping-point/hysteresis로 넘어가는 경우의 판별변수.
7. self-reinforcing concentration이 실제 장기 효율을 높이는 경우와 장기 탐색공간을 파괴하는 경우를 가르는 조건.

### Counter-convergence and escape dynamics / 반수렴·탈출 동역학

집중·lock-in 쪽 문헌만 보면 연구가 한 방향으로 편향될 수 있으므로, **수렴을 깨는 메커니즘**도 별도 선행연구 축으로 둔다.

#### 1. Exploration versus exploitation

- James G. March (1991), DOI 10.1287/orsc.2.1.71은 exploitation이 exploration보다 더 빠르게 단기효율을 개선할 수 있지만, 그 적응과정이 장기적으로 self-destructive해질 수 있음을 모델링했다.
- 핵심 재사용점: 단기 성과 상승이 장기 탐색능력 감소와 동시에 일어날 수 있다는 구조.
- Project 연결: 현재 경로의 성과 증가와 option-space·independent search 감소를 반드시 동시에 측정한다.

**반수렴 후보:**  
`preserved exploration capacity + independent search + delayed irreversible commitment → lock-in pressure ↓`

#### 2. Rugged landscapes and local adaptation

- Daniel Levinthal (1997), DOI 10.1287/mnsc.43.7.934은 상호작용이 큰 rugged landscape에서 시작점이 장기형태에 지속적 영향을 주며, tightly coupled 조직은 환경변화에 취약할 수 있음을 모델링했다.
- 핵심 재사용점: local optimum과 path dependence를 구분하고, coupling 강도가 적응가능성을 바꾼다는 점.
- Project 연결: option-space의 수뿐 아니라 **대안 간 독립성·coupling·복구가능성**을 측정해야 한다.

**반수렴 후보:**  
`lower coupling + viable alternative paths + local adaptation capacity → catastrophic lock-in risk ↓`

#### 3. Threshold and cascade reversal

- Mark Granovetter (1978), DOI 10.1086/226707은 개인의 threshold 분포가 집단결과를 비선형적으로 바꿀 수 있음을 보여주며, 비슷한 평균 선호를 가진 집단도 전혀 다른 집단수준 결과를 만들 수 있다고 지적했다.
- 핵심 재사용점: 집단수렴을 개별 actor의 동일 의도나 합의로 역추론하면 안 됨.
- Project 연결: 비대칭·통제 수렴이 보이더라도 "모두가 그것을 원했다"는 해석을 배제하고 threshold distribution과 cascade 구조를 별도 추적한다.

**반수렴 후보:**  
`small change in threshold distribution / visible independent defections / alternative signal → cascade can break`

#### 4. Exit is necessary but not sufficient

- Hirschman 계열과 Dowding et al. (2000), DOI 10.1023/A:1007134730724는 exit·voice·loyalty 관계가 단순하지 않음을 보여준다.
- competition이 커져 exit가 쉬워져도 voice가 자동 강화되는 것은 아니며, exit가 voice를 약화시킬 수도 있다.
- Project 연결: `practical exit`를 단일 해결책으로 두지 않고 **exit + voice + recovery + comparator preservation**의 결합으로 본다.

**반수렴 후보:**  
`practical exit + effective voice + independent recovery + surviving comparators → concentration correction capacity ↑`

#### 5. 현재 문헌들의 양방향 수렴

선행연구들을 한 상태전이 언어로 바꾸면 두 방향이 동시에 나타난다.

**집중 방향**

```
short-term exploitation
+ initial advantage
+ dependence
+ switching cost
+ positive feedback
+ institutionalization
+ social proof
+ comparator loss
→ self-reinforcing concentration
```

**탈출/복구 방향**

```
exploration preservation
+ lower coupling
+ independent alternatives
+ practical exit
+ effective voice
+ independent recovery
+ surviving comparators
+ countervailing information
→ concentration can stall, reverse, or remain bounded
```

따라서 Project의 핵심 검증대상은 "집중이 생기는가" 하나가 아니다.

더 중요한 질문은:

1. 어떤 조합에서 집중이 **self-reinforcing**해지는가?
2. 어떤 조합에서 같은 초기 비대칭이 **bounded** 상태로 멈추는가?
3. 어떤 개입이 실제로 option-space와 falsifiability를 복구하는가?
4. 어떤 경우에는 분산이 오히려 조정실패·중복비용·안전저하를 만드는가?
5. exploration을 얼마나 유지해야 장기 적응성이 올라가며, 그 비용은 누가 부담하는가?

### Project-added integration and unresolved candidates

After integrating prior work and preserving its attribution, the strongest unvalidated Project-added combinations or unresolved candidates are:

1. fork/merge-aware role reversal where agent count is endogenous;
2. enforcement-latency versus power-drift thresholds;
3. cumulative capture across locally acceptable steps;
4. role reversal under large oversight/cognitive asymmetry;
5. competitive survivability of non-capture governance;
6. whether H/M/X classification avoids both irreversible harm and veto paralysis better than an expanding hard intersection.

See [MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md](MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md) and [experiments/e009/README.md](experiments/e009/README.md).
