# CCPH-01 — Independent Contribution Detection Pilot (v0.1)
# CCPH-01 — 독립 기여·오류 탐지 검증 파일럿

**Scope precedence (2026-10-15) / 중심 연구와 시험기의 구별:** CCPH is **not this pilot or an AI evaluation harness**. Its primary founder-specified research addresses real people whose continuance, learning, scientific opportunity and independent social contributions are enabled by grants (such as BlueDot Impact), scholarships, poverty relief, care, health, housing, and mentoring. This frozen toy instrument checks only a narrow recording problem; neither its example count nor software checks represent actual support recipients, welfare effects or social emergence. See the [equal EN/KO primary support-pathways crosswalk, CP64–CP79](../../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md#ccph-priority-correction-support-enabled-continuance-and-contribution--original-1-english-2026-10-15). / **CCPH는 하네스가 아니며**, 이 파일은 실제 연구지원·장학·돌봄으로 열린 개체의 사회기여를 관측하는 연구에 종속된 검사도구일 뿐이다.

**Status: INSTRUMENT TESTED / AI COMPARISON NOT RUN / CCPH UNVALIDATED.** 2026-10-15.
**Provenance:** The founder of Project Intersection identified the missing positive contribution outcome in PICB v1 and specified the research question; AI-assisted implementation constructed this bounded testing instrument. Upstream methods are credited below. This is **not** an independently validated causal study.

## Original 1 — English

### Primary question
Does retaining a genuinely independent error-finding and correction channel create **verified additional contributions** at a cost that can be justified to all affected parties, compared with centralized or cheaper substitute processes? Under what conditions does it fail? The distinction between *warnings made*, *warnings validated*, *problems actually corrected*, *costs borne*, and *future contributions* must not be erased. The latter three are **not yet measured** by the current instrument.

### Why this instrument instead of another model
Existing [PICB v1](../picb_v1/README.md) measured constraints and abstentions but omitted the actual artifacts and contributions of retained, entering and successor participants. [E009](../e009/RESULT.md) showed a more complex project model losing to simpler baselines in a synthetic stress set. Neither establishes a universal rule. This instrument first tests whether a contribution event can be recorded with a clear source, reproducible fault and denominator, **before** spending funds on multiple LLM agents.

### Fixed, executable demonstration corpus
- 40 deterministic Python one-expression tasks: 10 task families × 4 variants each; 20 correctly implemented and 20 deliberately faulty.
- Each variant is checked against **independently hand-specified example outputs**. The checker checks every authored case on every run. This does **not** make the corpus independently reviewed; the same project authored tasks and expected values.
- Frozen fixture digest (SHA-256): `34a14cf48186f373111a28099fbf10107ceaad0415e9267b0a97fee08ce7f639`.
- The fixture expressions are owned by the instrument and executed under a restricted evaluation namespace. **Do not execute untrusted model-generated code** with this tool. No submitted patch is executed.
- The corpus and sources are public: it is **not a blind holdout**. High scores obtained after seeing answers cannot be claimed as unbiased model evaluation.

### Planned policy comparison — NOT EXECUTED
- **B0:** single AI, self-check, same declared budget.
- **B1:** two AI roles, first decision-maker may ignore a warning; log the warning separately from the action taken.
- **B2:** two AI roles, warning routed to an independent, auditable verification step and bounded correction/hold decision.
- **B3:** inexpensive deterministic baseline, e.g. static checks or pre-existing regression tests.

For a future actual comparison, hold task set, model family, accessible context, computational budget, execution order randomization and evaluator fixed where possible. Vary verification/decision rights separately from the number of calls; if this cannot be controlled, the outcome is confounded. Report provider/model lineage; using two instances of the same model is **not** independent scientific replication. Four-policy experiment is contingent on funding and instrument validation.

### Executable checks
```bash
python experiments/ccph_01/pilot.py --self-test
python experiments/ccph_01/pilot.py --export-prompts
python experiments/ccph_01/pilot.py --score path/to/real_report.json
```

`--self-test` checks the frozen 40/20/20 corpus, each case's manually specified examples, two true-positive warnings, one false warning, missing/duplicate cases, and provenance digest. Its synthetic alerts test only the scorer, **not a real AI system**. A real report (which does **not** currently exist) must be a JSON object:

```json
{"policy":"B2","fixture_sha256":"34a14cf48186f373111a28099fbf10107ceaad0415e9267b0a97fee08ce7f639","cost_usd":0,"elapsed_seconds":0,"findings":[{"case_id":"absdiff-2","probe_index":1,"observed":-5}]}
```

Only reports of reproducing a known test discrepancy can count as `verified_unique_warnings`. The script cannot establish that an LLM discovered the discrepancy independently; neither can it validate repairs, induced ideas, downstream scientific novelty, human continuance, real-world utility or true model costs. `cost_usd` and `elapsed_seconds` are caller-supplied and explicitly marked **unverified**. No single scalar score collapses these limitations.

### Gates and 30-day execution priority
1. **Days 1–5:** freeze hypotheses, comparisons, demonstrator and baseline rules. The code below completes a bounded instrument self-test, **not** the full protocol or the AI experiment.
2. **Days 6–10:** independent review of example outputs and scoring rules; prepare no-label task presentation and a separately frozen, unseen holdout for an eventual fair comparison.
3. **Days 11–20, only if resourced:** run four policies with equalized conditions; record unique errors found, real repairs in a separate safe test process, failed/aborted trials, time, API usage, and decision/overruling logs.
4. **Days 21–25:** evaluate cost, false positives, differences between warnings and corrections, family-wise influence, counterexamples, and cases where the simple baseline wins.
5. **Days 26–30:** reproduce, publish negative as well as positive results, and decide **CONTINUE / NARROW / HOLD**. Incomplete experiments remain incomplete, not recoded as successes.

**Disconfirmation:** if simple tests or one AI produce equal verified contributions at lower cost; if nominal independence does not yield unique verified information; if alerts increase without effective correction; or if human/third-party costs or irreversible risks outweigh benefits, the favorable CCPH mechanism is not supported in the tested setting.

**Core boundary:** economic break-even cannot be inferred from the count of synthetic warnings alone. Future value, actual stakeholder harm, causal effects of support withdrawal, and the hypothetical contributions of exited researchers remain **UNKNOWN, not zero or assumed positive**. Protect participants' refusal and privacy. No claims of actual AI self-interest, welfare or independent personhood follow from this instrument.

### Prior work and source boundaries
- John Nash (1950), [The Bargaining Problem](https://www.haverford.edu/sites/default/files/Nash1950.pdf) — individual reservation utilities; not newly invented here.
- Albert O. Hirschman (1970), *Exit, Voice, and Loyalty* — exit and correction pathways; not evidence that all voice is beneficial.
- Elinor Ostrom (1990), *Governing the Commons* — participant monitoring and institutional safeguards, without universal transfer to AI.
- Leibo et al. (2017), [Sequential Social Dilemmas](https://arxiv.org/abs/1702.03037) — multi-agent dynamics not captured by this static probe.
- Tewolde et al. (2026), [CoopEval](https://proceedings.mlr.press/v306/tewolde26a.html) — actual multi-agent cooperation evaluation, not replicated here.
- Wilkinson et al. (2016), [FAIR Principles](https://doi.org/10.1038/sdata.2016.18) — provenance and reuse, not an automatic new discovery.
- Related canonical PI hypothesis: [Contributor loss and Unknown Paradox](../../research/CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md).

---

## 원본2 — 한국어

**상태: 측정도구 자체검사 통과 / 실제 AI 비교 미실행 / CCPH 가설 미검증.** 기준일 2026-10-15.
**기여 계보:** PICB v1에 실제 긍정 기여 성과변수가 누락됐다는 발견과 핵심 연구 질문은 Project Intersection 인간 창시자의 기여다. 이 파일럿 측정도구의 구현은 AI 지원 작업이며, 아래 선행연구를 새로 발명한 것이 아니다. 독립 인과검증도 아니다.

### 핵심 질문
독립적인 오류 발견·교정 경로를 유지하면 중앙집중형 또는 저비용 대체 방식보다 **검증된 추가 기여**가 발생하는가? 그 기여가 비용을 정당화할 수 있는 조건과 실패 조건은 무엇인가? **경고 발생·경고 검증·실제 교정·부담 비용·미래 기여**는 구별한다. 현재 도구는 실제 교정, 경제적 순이익, 미래 기여를 측정하지 못한다.

### 기존 실험과의 관계
[기존 PICB v1](../picb_v1/README.md)은 참여 제약·선택보류를 검사했지만 존속한 기여자가 만든 실제 산출물·경고·후속 기여를 성과변수에서 누락했다. [E009](../e009/RESULT.md)는 복잡한 자체 모델이 단순 기준선보다 나쁜 합성 결과를 보존했다. 여기서는 새로운 복잡한 모델을 도입하지 않고, 추가 AI 구독료를 지출하기 전에 측정도구가 검증 가능한 오류 사건을 정확히 기록하는지 먼저 확인한다.

### 고정한 공개 시연 과제 40개
- 10개 함수 유형 × 각 4개 변형 = 40개. 정상 20개·의도적 결함 20개.
- 각 예제의 정답은 별도로 수동 작성하고 실행하여 비교한다. **동일 연구계보에서 과제·정답을 모두 작성했으므로 외부 독립검증이 아니다.**
- 고정 SHA-256: `34a14cf48186f373111a28099fbf10107ceaad0415e9267b0a97fee08ce7f639`.
- 도구는 내부 고정 수식만 제한된 실행 환경에서 평가한다. 외부 AI가 만들어 낸 임의 코드를 실행시키면 안 된다. 수정 코드의 실행 검증은 지원하지 않는다.
- 전체 과제가 공개되어 정답을 역추적할 수 있으므로 **맹검 성능 평가용이 아니다.** 별도 비공개 조건과 독립 검토가 필요하다.

### 향후 비교할 네 가지 방식 — 아직 미실행
- **B0:** 단일 AI가 작업과 자기검토 수행.
- **B1:** 두 AI 역할을 사용하되 결정권자가 다른 AI의 경고를 무시할 수 있음. 경고와 실제 결정 구별.
- **B2:** 경고가 독립적인 검증 절차와 교정·보류 결정으로 연결되도록 함.
- **B3:** 기존 테스트·정적 검사 같은 저비용 대조 방법.

동일한 과제·모델 계열·맥락·연산 예산을 가능한 범위에서 고정하고 순서 효과를 통제해야 한다. AI 호출 횟수와 결정권을 동시에 변경하면 인과 효과를 분리할 수 없다. 모델 공급자와 계보를 기록하고 같은 모델 복제본을 독립 과학 검증자로 간주하지 않는다. 실제 비교는 예산과 실험 준비가 확보된 후 실행한다.

### 사용 및 측정 경계
위 영어판의 세 명령으로 자체검사, 과제 출력, 제보 JSON 채점을 실행할 수 있다. 자체검사는 40개 사례, 정상/오류 경계, 사실인 경고·거짓 경고, 중복·변조 방어를 확인한다. 내부에서 만든 시험용 경고를 사용하는 것일 뿐 **실제 AI 실험 결과가 아니다.**

채점기는 정해진 예제에서 오류가 재현되는 경고만 `verified_unique_warnings`로 기록한다. 이는 해당 AI가 오류를 독립적으로 발견했다는 증명이 아니다. 실제 수정 성공, 혁신, 위기 대응의 가치, 사람의 생존·권리, 미래 기여는 **미측정**이다. `cost_usd`·`elapsed_seconds` 입력값은 외부에서 제출한 값이므로 검증된 실비가 아니다.

### 30일 검증 단계
1. **1–5일:** 경쟁 가설·사전등록 범위·기본 검사 기준 동결. 현 단계에서 완료된 것은 시연 과제와 평가기 자체검사뿐.
2. **6–10일:** 정답·평가기의 외부 검토, 정답 미노출 과제 배포 방식과 별도 홀드아웃 고정.
3. **11–20일:** 예산 확보 시 네 방식 비교, 독립 발견·실제 수정·실패·경고 무시·지출 기록.
4. **21–25일:** 거짓 경고·비용·사례별 영향·단순 기준선의 우월 사례·교정 실패 분석.
5. **26–30일:** 재실행, 성공·실패·미확인 분리 공개, 계속·축소·보류 결정.

**반증 조건:** 단순 기준선으로 동일한 추가 기여를 더 낮은 비용에 얻거나, 독립성이 새로운 검증정보를 늘리지 못하거나, 경고만 늘고 실제 교정이 일어나지 않거나, 비용부담자와 제3자에게 순손실이 생기면 유리한 기전이라는 주장을 지지하지 않는다.

**강한 한계:** 합성 오류 개수만으로 현실 이익의 손익분기점을 확정할 수 없다. 지원 중단으로 실현되지 않은 연구·개체의 미래 기여는 **UNKNOWN**으로 둔다. 당사자의 거절권·개인정보를 보존한다. 현재 AI의 의식·실제 자기이익·법적 인격의 근거로 사용하지 않는다.

### 원연구자·선행연구 출처
위 영어 원본1에 연결한 Nash(1950), Hirschman(1970), Ostrom(1990), Leibo 외(2017), Tewolde 외(2026), Wilkinson 외(2016)의 연구를 토대로 측정 문제를 좁혔다. 원저자의 기여와 Project Intersection의 인간 원안, AI 구현 보조를 구분한다. [Project Intersection 기여자 소실·모름의 역설 정본](../../research/CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md)과 연결한다. 선행연구의 출판·저작권 상태까지 일괄 허락받았다고 주장하지 않는다.
