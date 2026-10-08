# R3 — 성능·채택·데이터/권한 집중 자기강화 선행연구

검색일: 2026-10-09. ZERO GATE OPEN / 포화 0/3. 공개 원문·출판사·저자 페이지 확인 범위. 원자료 재분석 없음.

## 직접/부분 선행
1. **Paul A. David (1985)**, *Clio and the Economics of QWERTY*, AER Papers & Proceedings 75(2):332–337. 경로의존·잠금의 고전. PARTIAL: 초기 우위/채택이 장기 구조를 고착할 수 있다는 일반 메커니즘.
2. **W. Brian Arthur (1989)**, *Competing Technologies, Increasing Returns, and Lock-In by Historical Events*, Economic Journal 99(394):116–131, DOI 10.2307/2234208. increasing returns 아래 작은 역사적 사건이 기술 우위·잠금으로 증폭. DIRECT/PARTIAL.
3. **Hal R. Varian (2018)**, *Artificial Intelligence, Economics, and Industrial Organization*, NBER w24839, DOI 10.3386/w24839. 데이터·AI·산업조직의 경제적 관계를 분석. BACKGROUND/PARTIAL; '데이터가 자동으로 독점'이라고 과장 금지.
4. **Daron Acemoglu; Pascual Restrepo (2018/2019)**, *Artificial Intelligence, Automation and Work*, NBER/Chicago chapter, DOI 10.7208/chicago/9780226613475.003.0008. 자동화·새 과업·노동수요의 균형을 다룸. PARTIAL: algorithmic management 권력 자체의 직접 검증은 아님.
5. **James Grimmelmann (2015)**, *The Virtues of Moderation*, Yale J.L. & Tech. 17:42. 플랫폼의 규칙·중재 권력과 사용자 거버넌스 문제. PARTIAL.
6. **Taina Bucher (2018)**, *If...Then: Algorithmic Power and Politics*, Oxford UP, DOI 10.1093/oso/9780190493028.001.0001. 알고리즘 권력을 관계적·경험적 관점에서 분석. DIRECT/PARTIAL: 권력은 단순 정확도 변수가 아님.
7. **Min Kyung Lee; Daniel Kusbit; Evan Metsky; Laura Dabbish (2015)**, *Working with Machines: The Impact of Algorithmic and Data-Driven Management on Human Workers*, CHI, DOI 10.1145/2702123.2702548. 알고리즘 관리가 노동자의 인식·행동에 미치는 영향. DIRECT/PARTIAL.
8. **Alex Rosenblat; Luke Stark (2016)**, *Algorithmic Labor and Information Asymmetries: A Case Study of Uber's Drivers*, IJOC 10:3758–3784. 정보비대칭과 알고리즘 관리의 권력 문제. DIRECT/PARTIAL.
9. **Kristian Lum; William Isaac (2016)**, *To predict and serve?*, Significance 13(5):14–19, DOI 10.1111/j.1740-9713.2016.00960.x. 예측치안에서 관측/배치가 다음 데이터에 영향을 주는 피드백 문제를 설명. DIRECT: 모델 출력→행동→데이터→모델의 재귀적 피드백.
10. **Danielle Ensign; Sorelle A. Friedler; Scott Neville; Carlos Scheidegger; Suresh Venkatasubramanian (2018)**, *Runaway Feedback Loops in Predictive Policing*, FAT* / PMLR 81:160–171. 예측치안 배치와 관측 데이터가 runaway feedback loop를 형성할 수 있음을 수학/시뮬레이션으로 분석. DIRECT.
11. **Allison J. B. Chaney; Brandon M. Stewart; Barbara E. Engelhardt (2018)**, *How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility*, RecSys, DOI 10.1145/3240323.3240370. 추천이 소비 데이터를 만들고 그 데이터를 다시 학습하는 feedback에서 동질화·효용저하가 발생 가능. DIRECT.
12. **Jonathan Stray (2021)**, *Designing Recommender Systems to Depolarize*, arXiv 2107.04953. 추천 목적·측정·사회효과를 다루는 설계 논의. ADJACENT; 권한집중 인과의 직접증거 아님.

## R3 판정
다음 일반형은 **신규성에서 제거**:
`출력/추천 → 인간 행동 → 관측 데이터 → 다음 모델/추천` 피드백.
`초기 우위 → 채택 → increasing returns → lock-in`.
`알고리즘 관리 → 정보비대칭/권력비대칭`.
따라서 R3의 '자기강화가 존재한다' 자체는 Project 신규성이 아님.

## 아직 남는 좁은 잔차
**R3-residual:** 동일한 모델 성능 조건에서 *실효적 판정권 집중(J_effective)*과 *실효적 appeal/exit*를 독립적으로 변화시켰을 때, 모델-행동-데이터 피드백의 강도·오류수정·장기 자발적 참여가 어떻게 달라지는가.

이 잔차도 contestability, platform governance, algorithmic management intervention 연구와 추가 대조 전 신규성 주장 금지.

## 반례/주의
- 데이터 규모 증가가 항상 성능 증가를 보장하지 않는다.
- 높은 성능이 항상 채택/lock-in을 만들지 않는다(algorithm aversion 선행).
- 피드백 루프가 항상 해롭지 않다; 올바른 오류수정 신호를 반영할 수도 있다.
- 플랫폼 집중은 알고리즘 정확도만으로 설명할 수 없다: 네트워크 효과, 전환비용, 자본, 계약, 규제, 브랜드, 보완재를 분리해야 한다.
- predictive policing 결과를 일반 AI 거버넌스로 그대로 외삽하지 않는다.

신규 DIRECT/PARTIAL 다수 발견 → 포화 0/3.
