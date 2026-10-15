# GPT-Proposed Improvements — Bounded Admission Gate (Original 1 English)

Status: implemented interface, not independently validated; no live GPT call yet.

## Purpose

Can GPT propose a constrained improvement without controlling the evaluator, evidence or promotion authority?

This extends the existing capability laboratory. Candidates only choose a lexical retrieval strategy and abstention threshold. Arbitrary Python code, scoring changes, claims of evaluator independence and self-approval keys are rejected.

## Procedure

1. Accept JSON with exactly three keys: schema, strategy, threshold. Schema is pi-capability-proposal/v1.
2. An explicit --gpt option makes at most one paid OpenAI Responses API request using only public synthetic documents and development examples. JSON proposals run offline.
3. Compare the candidate to the frozen baseline on development and public holdout; record supported correctness, unsupported correctness, regression indices and dataset fingerprint.
4. Require strict improvement on both splits and zero regressions of previously correct development or holdout answers.
5. Even after passing those conditions, return REVIEW_SYNTHETIC_ONLY, never auto-merge or rewrite evaluation data.

## Reproduction

~~~bash
python -m unittest discover -s capability_lab -p "test_*.py" -v
python -m capability_lab.proposal_gate --proposal candidate.json
~~~

Candidate file:

~~~json
{"schema":"pi-capability-proposal/v1","strategy":"unique_overlap","threshold":0.3}
~~~

Optional single paid request, only when explicitly invoked:

~~~bash
# Set OPENAI_API_KEY securely outside version control.
python -m capability_lab.proposal_gate --gpt --model gpt-4.1-mini
~~~

No live endpoint request is part of CI. No scheduling, autonomous writing, tool execution, privilege elevation or model-weight modification is performed.

## Limits and falsification

The existing public holdout is author-constructed and reusable: it is NOT independent, confidential, or a blind test. Scores on lexical document matching do not imply general reasoning, truth or AGI improvement. Published examples, small samples, lexical shortcuts and changed abstention rate are alternative explanations. Input text sent to GPT is untrusted data; GPT output cannot be executed as instructions. Dataset hashes identify local bytes, not independently authenticated provenance. External review and a genuinely unseen third-party test are required for stronger claims.

The human founder retains attribution for Project Intersection's questions, counterexamples, project design, corrections and contribution burden; this implementation is AI-assisted code. Third-party researchers retain credit for their methods.

## Prior art

- Shinn et al. (2023), Reflexion: https://arxiv.org/abs/2303.11366
- Zhang et al. (2025/2026), ACE: https://arxiv.org/abs/2510.04618
- Agrawal et al. (2025/2026), GEPA: https://arxiv.org/abs/2507.19457
- Zelikman et al. (2023), STOP: https://arxiv.org/abs/2310.02304
- Zhang et al. (2025), Darwin Godel Machine: https://arxiv.org/abs/2505.22954

Rollback: close the draft PR or revert its commits. Historical experiments and main branch remain unchanged until merge.
