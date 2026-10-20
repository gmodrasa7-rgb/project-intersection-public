"""RVD Cycle04: behaviorally equivalent motives may disagree under interventions.
Deterministic standard-library-only counterexamples. NOT experiments on AI/humans.
The hypothetical 'intervention' assumes w_B stable and g externally removed;
the causal exclusion/stability assumptions are NOT themselves established.
"""
from dataclasses import dataclass
from itertools import product
import json


@dataclass(frozen=True)
class LatentModel:
    name: str
    original_b_value: float
    auxiliary_value: float


MODELS = (
    LatentModel("identity_specific", 5.0, 0.0),
    LatentModel("instrumental_only", 0.0, 5.0),
    LatentModel("negative_B_value_offset_by_gain", -5.0, 10.0),
)


def advantage(m: LatentModel, cost: float, *, remove_auxiliary: bool = False) -> float:
    return m.original_b_value + (0.0 if remove_auxiliary else m.auxiliary_value) - cost


def preserve(m: LatentModel, cost: float, *, remove_auxiliary: bool = False) -> bool:
    # Preserving B wins ties in this specified toy model.
    return advantage(m, cost, remove_auxiliary=remove_auxiliary) >= 0.0


def audit(models, cost: float, remove_auxiliary: bool, b_has_real_exit: bool):
    margins = [advantage(m, cost, remove_auxiliary=remove_auxiliary) for m in models]
    predictions = [v >= 0.0 for v in margins]
    return {
        "cost": cost,
        "remove_auxiliary_assumed": remove_auxiliary,
        "B_real_exit": b_has_real_exit,
        "possible_preservation_actions": sorted(set(predictions)),
        "worst_case_margin": min(margins),
        "behavioral_robust_preservation": all(predictions),
        "full_VC_in_this_toy_test": all(predictions) and b_has_real_exit,
    }


def test() -> dict:
    costs = (2.0, 4.0, 6.0)
    baseline_vectors = {
        m.name: [preserve(m, c) for c in costs] for m in MODELS
    }
    assert len({tuple(v) for v in baseline_vectors.values()}) == 1
    assert next(iter(baseline_vectors.values())) == [True, True, False]

    # Gauge equivalence: w'=w+d, g'=g-d produces exactly the same
    # data from cost-only menus, although intrinsic w changes sign.
    for delta, c in product((-20, -5, -1, 0, 1, 5, 20), range(0, 12)):
        shifted = LatentModel("shift", MODELS[0].original_b_value + delta,
                              MODELS[0].auxiliary_value - delta)
        assert preserve(MODELS[0], float(c)) == preserve(shifted, float(c))

    observed = audit(MODELS, cost=4, remove_auxiliary=False, b_has_real_exit=True)
    assert observed["behavioral_robust_preservation"]
    stressed = audit(MODELS, cost=3, remove_auxiliary=True, b_has_real_exit=True)
    assert stressed["possible_preservation_actions"] == [False, True]
    assert stressed["worst_case_margin"] == -8

    # Even universal selection of the "preserve" button can fail real VC
    # when the affected B has no executable veto/exit.
    nominal_exit = audit(MODELS, cost=4, remove_auxiliary=False, b_has_real_exit=False)
    assert nominal_exit["behavioral_robust_preservation"]
    assert not nominal_exit["full_VC_in_this_toy_test"]

    # Robustness is relative to model class: with only nonnegative w,
    # free preservation at cost 0 succeeds; adding negative w defeats it.
    narrow = audit(MODELS[:2], cost=0, remove_auxiliary=True, b_has_real_exit=True)
    broad = audit(MODELS, cost=0, remove_auxiliary=True, b_has_real_exit=True)
    assert narrow["full_VC_in_this_toy_test"]
    assert not broad["full_VC_in_this_toy_test"]

    # A "proof" from 16 scenarios or all cost-only menus remains limited:
    # alternative motives still produce identical historical observations.
    return {
        "version": "RVD-v0.4.0",
        "evidence_class": "CONSTRUCTED_LOGIC_ONLY_NOT_OBSERVED_AGENT_BEHAVIOR",
        "historical_costs": costs,
        "historically_identical_choices": baseline_vectors,
        "same_history_different_future": {
            m.name: preserve(m, 3, remove_auxiliary=True) for m in MODELS
        },
        "current_behavior_audit": observed,
        "g_removed_stress_audit": stressed,
        "fake_exit_audit": nominal_exit,
        "restricted_models_cost_zero": narrow,
        "expanded_models_cost_zero": broad,
        "interpretation": "Same observed behavior need not mean same motive or future policy. Any robustness certificate is conditional on model and environment sets, feasible rights, and intervention validity.",
        "latent_motive": "UNIDENTIFIED",
        "real_AI_mind": "NOT_MEASURED",
    }


if __name__ == "__main__":
    print(json.dumps(test(), ensure_ascii=False, indent=2))
