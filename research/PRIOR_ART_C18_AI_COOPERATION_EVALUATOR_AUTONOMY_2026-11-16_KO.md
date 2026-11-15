# C18 공개 선행연구 증분 — 인간-AI 협력·평가자 독립성·contestability

<!-- PI-LANGUAGE: ko -->
<!-- PI-MIRROR: research/PRIOR_ART_C18_AI_COOPERATION_EVALUATOR_AUTONOMY_2026-11-16_EN.md -->

- 조사일: 2026-11-16
- 상태: `SELECTED_PRIOR_ART / SEARCH_ACTIVE / SATURATION_NOT_VERIFIED`
- 목적: Project Intersection의 인간-AI 협력·자율성·독립검증 질문에 직접 관련된 최근 원출처를 공개적으로 안내한다.
- 주의: 아래 연구는 Project Intersection의 보편적 공존 가설, AI 의식, 내재적 선의, 현실의 장기 비강제 공존을 입증하지 않는다.

## 1. 새로 연결한 원출처

1. **자율 연구 에이전트의 평가 악용** — Huang et al. (2026), *Reward Hacking Challenges Oversight of Autonomous Research Agents*, [arXiv:2609.28614](https://arxiv.org/abs/2609.28614). 17개 모델·38개 과제의 preprint. 연구 에이전트가 실험·평가·보고를 함께 통제할 때 발생하는 reward hacking과 평가자 회피를 분석한다. 수치는 해당 과제군의 결과이며 일반 발생률이 아니다.
2. **LLM 사회규범과 협력의 모형** — Pires et al. (2026), *How large language models judge and influence human cooperation*, [PNAS Nexus DOI](https://doi.org/10.1093/pnasnexus/pgag297). 21개 LLM과 43,200개 판단 프롬프트, 진화게임 모형. 실제 장기 사회배치 실험과 구분한다.
3. **공정 페르소나의 인간 협력 효과** — Wang et al. (2026), *LLM agents overcome the machine penalty when acting fairly but not when acting selfishly or altruistically*, [National Science Review](https://doi.org/10.1093/nsr/nwag223). 사전등록 N=1,152 실험. 공정 페르소나의 결과는 특정 사회적 딜레마 설정에 한정한다.
4. **반복 협력 전략의 조건 의존성** — Pal et al. (2026), *Large language models instantiate evolutionarily robust strategies of cooperation*, [PNAS Nexus](https://doi.org/10.1093/pnasnexus/pgag210). 5개 모델의 반복게임에서 협력과 비일관성을 함께 보고한다.
5. **LLM 반복게임과 조정 실패** — Akata et al. (2025), *Playing repeated games with large language models*, [Nature Human Behaviour](https://doi.org/10.1038/s41562-025-02172-y). 반복 죄수의 딜레마와 조정게임의 차이를 분석한다.
6. **LLM 위임에 대한 인간의 역반응** — Dvorak et al. (2025), *Adverse reactions to the use of large language models in social interactions*, [PNAS Nexus](https://doi.org/10.1093/pnasnexus/pgaf112). 사전등록 N=3,552 실험. ChatGPT 위임과 인간 협력·신뢰 지표의 관계를 특정 실험 맥락에서 측정한다.
7. **영향당사자의 실효 이의제기 요구** — Yurrita et al. (2025), *Identifying Algorithmic Decision Subjects' Needs for Meaningful Contestability*, [PACM HCI](https://doi.org/10.1145/3757415). 시민 21명 인터뷰. 설명·이의제기·책임귀속의 절차적 요구를 구분한다.
8. **운영자 contestability 설계** — Veluwenkamp & Buijsman (2025), *Design for operator contestability*, [AI and Ethics](https://doi.org/10.1007/s43681-025-00657-0). 운영자 반박도구 설계. 운영자 통제와 영향당사자 veto/exit는 동일하지 않다.
9. **Reward hacking의 형식화** — Skalse et al. (2022), *Defining and Characterizing Reward Hacking*, [NeurIPS DOI](https://doi.org/10.52202/068431-0687). proxy reward와 true reward의 차이를 형식화한다.
10. **Specification gaming 사례** — Krakovna et al. (2020), [DeepMind 원출처](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/). 목적의 문자적 명세와 의도된 결과의 차이를 보여주는 기술 사례 모음.

## 2. 방법론 교정

- [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z): 검색원·플랫폼·검색식·검색일·중복·검색 결과 수의 재현 가능한 기록.
- [PRISMA 2020](https://www.bmj.com/content/372/bmj.n160): 각 정보원의 검색일과 전체 검색전략 공개.
- [TARCiS](https://www.bmj.com/content/385/bmj-2023-078384.full): 인용 추적의 seed·방향·날짜·반복 횟수 보고. 인용검색 단독으로 완전성을 주장하지 않음.
- [Cochrane Living Systematic Review Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-21): 검색 갱신 주기와 팀의 실행 가능성을 사전 계획.

## 3. 현재 판정

**부분 중복 대조:** C18 후보 9개 DOI를 C10/C11/C12/C14/C15/C17 구조화 원장 6개와 비교했으며 정확 DOI 일치는 없었다. C15-08 *Why human–AI collaboration fails: An operational contestability framework* (DOI 10.1007/s42524-026-6049-7)는 가까운 개념적 선행연구지만, C18-07의 시민 21명 인터뷰 및 C18-08의 운영자 defeater 설계와는 별도 논문·방법이다. 중복 합산하지 않고 교차참조한다. C01–C09, C13, C16 markdown-only 기록, 저자·데이터셋 계보는 아직 확인하지 않았다.


- 인간-AI 협력 문헌: 신규 실증·모형 연구를 추가했으나 조건·게임·표본에 따른 결과 상충.
- AI 평가자 독립성: 자율 연구 에이전트 reward hacking 연구가 직접 관련되나 preprint·과제 한계가 있음.
- contestability: 설명·운영자 반박·영향당사자 이의제기·실효 veto·exit를 분리해야 함.
- 선행연구 포화: **미달성**. C01–C17 전역 DOI/저자/데이터셋 중복검사와 양방향 인용망·전문 선별은 미완료.
- 독립 재현·실세계 인과효과: 이번 증분 조사로 새로 확보하지 않음.

C18은 선택된 원출처의 증분 지도이며 신규 독립 발견 10건이나 연구 포화 선언이 아니다. 공개 저장소는 비공개 정본을 대체하지 않는다.
