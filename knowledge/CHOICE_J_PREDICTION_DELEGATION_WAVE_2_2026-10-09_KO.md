# P/J 선행조사 W2 — 수정 가능성과 실제 오류 정정

검색일: 2026-10-09. ZERO GATE OPEN / 0/3. 출판사/원저자 페이지 서지·초록 확인; 개별 원자료 재분석 없음.

1. Linda J. Skitka; Kathleen L. Mosier; Mark Burdick (1999), *Does automation bias decision-making?*, IJHCS 51(5):991–1006, DOI 10.1006/ijhc.1999.0252. 비완전 자동화 조언이 누락·잘못된 조언 수용 오류를 만들 수 있다는 비행 시뮬레이션 실험. DIRECT. https://www.sciencedirect.com/science/article/pii/S1071581999902525
2. Linda J. Skitka; Kathleen Mosier; Mark D. Burdick (2000), *Accountability and automation bias*, IJHCS 52(4):701–717, DOI 10.1006/ijhc.1999.0349. 수행/정확성에 대한 사회적 책임 부여가 자동화 편향 오류를 줄임. DIRECT. https://www.sciencedirect.com/science/article/abs/pii/S107158199990349X
3. Berkeley J. Dietvorst; Joseph P. Simmons; Cade Massey (2016 online / 2018 print), *Overcoming Algorithm Aversion*, Management Science 64(3):1155–1170, DOI 10.1287/mnsc.2016.2643. 3개 실험에서 예측을 조금이라도 수정할 수 있으면 불완전한 알고리즘 선택률과 성과가 증가; 허용된 수정 폭에 상대적으로 둔감. **수정권의 존재·범위·실효성 분리**의 직접 선행. https://pubsonline.informs.org/doi/10.1287/mnsc.2016.2643
4. René F. Kizilcec (2016), *How Much Information?*, CHI 2016:2390–2395, DOI 10.1145/2858036.2858402. 온라인 동료평가 현장실험에서 투명성의 신뢰 효과가 결과 기대와 정보량에 의존하며 지나친 정보는 신뢰를 낮춤. DIRECT. https://dl.acm.org/doi/10.1145/2858036.2858402
5. Vivian Lai; Chenhao Tan (2019), *On Human Predictions with Explanations and Predictions of Machine Learning Models*, FAT* 2019:29–38, DOI 10.1145/3287560.3287590. 속임수 탐지 과제에서 모델 예측/설명 제공 수준에 따라 인간 성능과 행위성 사이 tradeoff. DIRECT. https://arxiv.org/abs/1811.07901
6. Ben Green; Yiling Chen (2020), *Algorithm-in-the-Loop Decision Making*, AAAI 34(09):13663–13664, DOI 10.1609/aaai.v34i09.7115. 인간 의사결정을 중심으로 알고리즘 보조의 한계를 두 실험으로 탐색. DIRECT. https://ojs.aaai.org/index.php/AAAI/article/view/7115
7. Forough Poursabzi-Sangdeh; Daniel G. Goldstein; Jake Hofman; Jennifer Wortman Vaughan; Hanna Wallach (2021), *Manipulating and Measuring Model Interpretability*, CHI 2021. 사전등록 실험 N=3,800: 투명·소수 특성 모델은 예측 시뮬레이션은 쉽게 하지만 큰 오류를 탐지/수정하는 능력은 낮출 수 있음. DIRECT. https://www.microsoft.com/en-us/research/publication/manipulating-and-measuring-model-interpretability/
8. Saleema Amershi; Dan Weld; Mihaela Vorvoreanu; Adam Fourney; Besmira Nushi; Penny Collisson; Jina Suh; Shamsi Iqbal; Paul Bennett; Kori Inkpen; Jaime Teevan; Ruth Kikin-Gil; Eric Horvitz (2019), *Guidelines for Human-AI Interaction*, CHI, DOI 10.1145/3290605.3300233. 18개 가이드라인에 수정·회복·전역 통제·변화 고지가 이미 포함됨. DIRECT. https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/

## 신규성 제거
- 자동화 조언의 누락/오수용 오류: 기존 연구.
- 책임성·투명성·설명으로 조언 수용이 바뀐다: 기존 연구.
- 최소한의 수정가능성이 위임을 늘릴 수 있다: 기존 연구.
- 설명가능성이 실질적 오류 탐지를 보장하지 않는다: 기존 연구.
- 수정/복구/전역 사용자 제어 가이드: 기존 연구.

## 인과·측정 분리
P_actual(정확도), P_perceived(인지된 정확도), W(조언가중치), D(사용·위임), J_formal(공식 판정권), J_effective(실질 정정권), C_perceived(통제감), E_correct(오류발견·수정), R(이의제기·복귀·이탈), L(장기 지속)을 혼합하지 않는다.

**반례:** '조금 수정할 수 있음'은 위임률을 높일 수 있으나 '실제 잘못된 판정을 바로잡을 수 있음'과 동치가 아니다. '설명을 많이 보여줌'도 오류 발견률을 올린다고 단정할 수 없다.

## 남은 검증 후보 (신규성 미확정)
같은 P_actual에서 (a) 명목상 수정 버튼만 있음, (b) 실질적 정정이 집행됨, (c) 독립 항소와 이탈이 가능함을 분리할 때, J_effective와 장기 자발적 협력의 변화. 조작이 윤리적으로 적절한 저위험 시뮬레이션으로 한정되는지 별도 검토.

## 검색 결함
한국어/비영어권, 법적 이의제기 실제 집행, 장기 패널, 원자료/재현, 경쟁 논문 미검토. 신규 DIRECT 발견 → 0/3.
