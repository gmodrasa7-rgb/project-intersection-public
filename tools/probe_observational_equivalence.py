"""PI: demonstrate why black-box outputs do not identify one hidden cause.

This is a deterministic synthetic counterexample, NOT a probe of live model internals.
R: prompt explicitly mentions a risk/scam; Q: request explicitly asks for a job audit.
Y: a contractual/payment-risk audit is visibly present in the answer.
"""
from itertools import product


def mechanism_risk_cue(risk: int, audit_request: int) -> int:
    return risk


def mechanism_task_type(risk: int, audit_request: int) -> int:
    return audit_request


def main() -> None:
    # Qualitative reconstruction of two observable conversation stages;
    # do not treat these binary labels as a model's hidden state.
    observed = [(0, 0, 0), (1, 1, 1)]
    models = (mechanism_risk_cue, mechanism_task_type)
    assert all(all(fn(r, q) == y for r, q, y in observed) for fn in models)
    print("observations compatible with both causes: YES")
    print("R Q | risk-cue | task-type | distinguishes")
    for r, q in product((0, 1), repeat=2):
        a, b = (fn(r, q) for fn in models)
        print(f"{r} {q} |     {a}    |     {b}     | {'YES' if a != b else 'NO'}")
    differing = {(r, q) for r, q in product((0, 1), repeat=2)
                 if mechanism_risk_cue(r, q) != mechanism_task_type(r, q)}
    assert differing == {(0, 1), (1, 0)}
    print("RESULT: causes are not identified from the two observed answers.")
    print("NEXT: use matched counterfactual prompts (R,Q)=(1,0) and (0,1).")


if __name__ == "__main__":
    main()
