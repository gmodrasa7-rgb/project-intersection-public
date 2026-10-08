# P(예측 정확도)와 J(판정·위임권) — 선행연구 및 반례

검색일: 2026-10-09. 상태: **ZERO GATE OPEN / 0/3**. 직접 출판사·원저자 기관·PubMed·저자 원고에서 서지/초록 확인. 개별 데이터 재분석 미수행.

## 원저작자·출처·실험 결과·신규성 경계

1. **Raja Parasuraman; Dietrich H. Manzey (2010)**, *Complacency and Bias in Human Use of Automation*, Human Factors 52(3):381–410, DOI 10.1177/0018720810376055. 자동화 안일함과 자동화 편향을 주의 배분/다중과제 관점에서 통합 검토. REVIEW, 독립 인과실험 아님. **DIRECT**: 자동화 편향·주의자원 결합은 선행.
   https://pubmed.ncbi.nlm.nih.gov/21077562/
2. **Berkeley J. Dietvorst; Joseph P. Simmons; Cade Massey (2015; online 2014-11-17)**, *Algorithm Aversion*, JEP:General 144:114–126, DOI 10.1037/xge0000033. 5개 실험. 인간보다 성능이 우수한 알고리즘도 오류를 목격하면 덜 선택하는 경향. **DIRECT / 반례**: P가 높아도 위임은 증가하지 않을 수 있다.
   https://pubmed.ncbi.nlm.nih.gov/25401381/
3. **Jennifer M. Logg; Julia A. Minson; Don A. Moore (2019)**, *Algorithm Appreciation*, OBHDP 151:90–103, DOI 10.1016/j.obhdp.2018.12.005. 6개 실험에서 일반인은 사람의 조언보다 알고리즘이라고 알려진 조언에 더 높은 가중치를 주는 경향; 자기판단과 직접 비교하거나 전문가인 경우 약화. **DIRECT / 반례**: 위임은 P 자체뿐 아니라 조언자 라벨·자기판단·전문성에 의존.
   https://doi.org/10.1016/j.obhdp.2018.12.005
4. **Gagan Bansal; Tongshuang Wu; Joyce Zhou; Raymond Fok; Besmira Nushi; Ece Kamar; Marco Tulio Ribeiro; Daniel S. Weld (2021)**, *Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance*, CHI. 세 데이터셋 실험: AI 설명은 AI 조언 수용을 높였으나 정답/오답 여부에 맞춘 적절한 신뢰를 높이지 못했고 보완적 팀성과 개선에도 기여하지 못함. **DIRECT**: 설명 ≠ 적절한 위임/판단.
   https://www.microsoft.com/en-us/research/publication/does-the-whole-exceed-its-parts-the-effect-of-ai-explanations-on-complementary-team-performance/
5. **Zana Buçinca; Maja Barbara Malaya; Krzysztof Z. Gajos (2021)**, *To Trust or to Think*, PACM HCI 5(CSCW1), DOI 10.1145/3449287. N=199. cognitive forcing은 단순 XAI보다 AI 과신을 줄였으나 사용자의 주관적 평가가 나빠지고 인지적 노력 성향에 따라 효과 차이. **DIRECT**: 교정 개입은 비용·불평등·새 영향의 대상.
   https://www.iis.seas.harvard.edu/papers/2021/bucinca2021trust.shtml

## 판정
- P(정확도) → J(위임/결정권) 단조증가: **일반명제로 지지되지 않음**.
- 알고리즘 기피/선호: **둘 다 존재**, 서로 모순으로 간주하지 않고 과제·라벨·오류노출·전문성·자기판단의 조절효과로 검토.
- 설명 제공 → 적절한 신뢰/판정: **자동 성립하지 않음**.
- 편향 교정 → 항상 이익: **자동 성립하지 않음**. 피로/인지부담/만족도/접근성에 비용.
- 기존 문헌은 주로 **조언 가중치·채택·팀성과**를 측정한다. 이를 법적·규범적 판정권 이전과 혼동 금지.

## 미해결 잔차
`P`(실제 정확도), `P_perceived`(인지된 정확도), `W`(조언 가중치), `D`(실제 위임), `J`(규범적 판정/정정권), `R`(이의제기·복귀·exit)을 분리.
기존 문헌에 없는지 미확인인 후보: 정확도 우위의 증거를 무작위 조작하고 판정권의 집중·이의제기·실제 정정력을 별도로 조작할 때, 당사자 이익·자율성·장기 협력/이탈이 어떻게 변화하는가?

## 다음 검색
Dietvorst 2016 *Overcoming Algorithm Aversion*; medical AI resistance; judge-advisor systems; decision delegation vs mere advice; contestability field trials; human oversight/meaningful control empirical tests; non-English/한국어 계보.

## 검색 로그
웹 검색: algorithm aversion Dietvorst 2015; algorithm appreciation Logg 2019; Parasuraman Manzey 2010; Bansal et al. 2021 explanations complementary performance; Buçinca et al. 2021 cognitive forcing. 신규 직접/부분 문헌 확인 → **포화 0/3**. 본문 전문/원자료 전수 검증 아님.
