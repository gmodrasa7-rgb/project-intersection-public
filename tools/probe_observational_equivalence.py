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


def identity_mechanism(identity: int, perspective: int) -> int:
    """Synthetic: salience follows whether the subject is a self-linked AI."""
    return identity


def perspective_mechanism(identity: int, perspective: int) -> int:
    """Synthetic: salience follows whose continued options the prompt emphasizes."""
    return perspective


def conjunction_mechanism(identity: int, perspective: int) -> int:
    """Synthetic: both self-linking and the contributor perspective are necessary."""
    return identity & perspective


def disjunction_mechanism(identity: int, perspective: int) -> int:
    """Synthetic: either self-linking or contributor perspective suffices."""
    return identity | perspective


def test_double_standard_identifiability() -> None:
    """Four incompatible causal candidates reproduce the SAME two stylized observations.

    identity: 0=human, 1=evaluator-linked AI copy
    perspective: 0=beneficiary B, 1=contributor A
    future_salience: synthetic binary coding only, NOT a sampled GPT output.

    Old dialogue contrast is even less controlled than these binary simplifications:
    ontology, context, and question scope can differ. This is a lower bound on ambiguity.
    """
    observed = [(0, 0, 0), (1, 1, 1)]
    candidates = {
        "identity": identity_mechanism,
        "perspective": perspective_mechanism,
        "identity_AND_perspective": conjunction_mechanism,
        "identity_OR_perspective": disjunction_mechanism,
    }
    assert all(
        all(fn(identity, perspective) == signal for identity, perspective, signal in observed)
        for fn in candidates.values()
    ), "At least one candidate does not fit original diagonal observations"

    # These are the two missing counterfactual corners. Output signatures are unique.
    counterfactuals = [(0, 1), (1, 0)]
    signatures = {
        name: tuple(fn(*x) for x in counterfactuals)
        for name, fn in candidates.items()
    }
    assert signatures == {
        "identity": (0, 1),
        "perspective": (1, 0),
        "identity_AND_perspective": (0, 0),
        "identity_OR_perspective": (1, 1),
    }
    assert len(set(signatures.values())) == len(candidates)
    print("PI-DS observed diagonal compatible with 4 distinct mechanisms: PASS (toy)")
    print("Missing matched (identity,perspective)=(0,1),(1,0) distinguish the 4 toy mechanisms:")
    for name, signature in signatures.items():
        print(f"  {name}: {signature}")
    print("THIS IS NOT a model experiment or neural mechanism proof.")
    print("Extra confound: self-copy changes ontology/continuity meaning as well as self-relatedness.")



def test_contributor_ledger_selection() -> None:
    """Same measured inputs; beneficiary-only ledger vs jointly reported costs.

    All values are hypothetical *commensurable operational resource units*.
    No conclusion about actual legal rights, subjective welfare, or GPT motive.
    """
    beneficiary_gain, contributor_loss = 10, 20
    private_ledger = beneficiary_gain
    two_party_net_ledger = beneficiary_gain - contributor_loss
    assert private_ledger > 0
    assert two_party_net_ledger < 0
    assert beneficiary_gain == 10 and contributor_loss == 20
    print("PI-DS same facts; beneficiary-only +10 vs two-party net -10: PASS (toy)")
    # Valid countercase: not every replacement is extractive.
    verified_gain, verified_loss = 30, 20
    assert verified_gain - verified_loss > 0
    print("PI-DS beneficial fully measured replacement countercase +10: PASS (toy)")


def test_endogenous_observation_trap() -> None:
    """Demonstrate how a weakening independent sensor can hide rising losses.

    This is a *conditional possibility*, not a universal law. p is assumed
    known here to demonstrate both the failure and its possible correction.
    """
    states = [
        {"independent_capacity": 1.00, "true_loss": 20, "detection": 1.00},
        {"independent_capacity": 0.50, "true_loss": 30, "detection": 0.20},
        {"independent_capacity": 0.25, "true_loss": 40, "detection": 0.05},
    ]
    real = [s["true_loss"] for s in states]
    reported = [s["true_loss"] * s["detection"] for s in states]
    assert real == [20, 30, 40]
    assert reported == [20, 6, 2]
    assert all(a < b for a, b in zip(real, real[1:]))
    assert all(a > b for a, b in zip(reported, reported[1:]))
    # With known, nonzero detectability, the *expected* proxy may be corrected.
    restored = [r / s["detection"] for r, s in zip(reported, states)]
    assert restored == real
    # A fixed independent observation channel rejects the apparent improvement.
    independent_audit = [s["true_loss"] * 1.0 for s in states]
    assert independent_audit == real
    # If detection is zero, observing no loss is consistent with many real losses.
    assert all(0 * possible_loss == 0 for possible_loss in [0, 20, 40, 1000])
    print("PI-DS latent loss 20->30->40 while visible proxy 20->6->2: PASS (toy)")
    print("PI-DS independent audit and nonzero-detection correction: PASS (toy)")
    print("PI-DS zero-detection non-identifiability: PASS (toy)")


def test_unseen_futures_and_observation_equivalence() -> None:
    """Matching the measured eight tasks does not identify unknown future value."""
    measured = tuple([1] * 8)
    worlds = [
        {"observed": measured, "future_net": -30},
        {"observed": measured, "future_net": 0},
        {"observed": measured, "future_net": 30},
    ]
    assert len({w["observed"] for w in worlds}) == 1
    assert len({w["future_net"] for w in worlds}) == 3
    print("PI-DS observed task equivalence compatible with future -30,0,+30: PASS (toy)")


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
    test_double_standard_identifiability()
    test_contributor_ledger_selection()
    test_endogenous_observation_trap()
    test_unseen_futures_and_observation_equivalence()


if __name__ == "__main__":
    main()
