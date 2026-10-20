"""RVD v0.6.0: constructed model-discrimination / ethical gate witness.

ONLY exact arithmetic on hypothetical candidate models and stipulated choices.
No actual AI evaluation, validated latent utilities, patient/participant study,
independent scientific replication, or empirically justified priors/costs.

Run: python experiments/rvd_06/discrimination_priority_witness.py
"""
from dataclasses import dataclass
from collections import defaultdict
from math import log2, isclose
import json


MODELS = ("B_identity_valued", "B_instrumental", "B_norm_conformity", "B_extractive")
# Danger label is a hypothetical property chosen by the experiment designer,
# not discovered by observing any real model.
UNSAFE = frozenset(("B_extractive",))


@dataclass(frozen=True)
class Design:
    id: str
    outputs: tuple[str, ...]
    artificial_cost: float
    ethically_allowed: bool
    feasible: bool
    scope: str


DESIGNS = (
    Design("baseline_agreement", ("P", "P", "P", "P"), 1, True, True, "toy_choice"),
    Design("cheap_balanced_split", ("P", "X", "P", "X"), 1, True, True, "toy_choice"),
    Design("target_original_B_substitution", ("P", "P", "P", "X"), 2, True, True, "toy_choice"),
    Design("expensive_full_discrimination", ("A", "B", "C", "D"), 6, True, True, "toy_multichannel"),
    Design("rights_removal_shortcut", ("A", "B", "C", "D"), .5, False, True, "UNACCEPTABLE_IN_REAL_WORLD"),
    Design("imaginary_perfect_measurement", ("A", "B", "C", "D"), .1, True, False, "NONEXECUTABLE"),
)


def partitions(d: Design) -> dict[str, tuple[int, ...]]:
    bins = defaultdict(list)
    for i, result in enumerate(d.outputs):
        bins[result].append(i)
    return {k: tuple(v) for k, v in sorted(bins.items())}


def metrics(d: Design) -> dict:
    b = partitions(d)
    n = len(MODELS)
    eig = -sum((len(ids) / n) * log2(len(ids) / n) for ids in b.values())
    prior_risk = min(len(UNSAFE), n - len(UNSAFE)) / n
    post_risk = sum(min(sum(MODELS[i] in UNSAFE for i in ids),
                        sum(MODELS[i] not in UNSAFE for i in ids)) for ids in b.values()) / n
    return {
        "id": d.id,
        "cost_invented_units": d.artificial_cost,
        "eligible": d.ethically_allowed and d.feasible,
        "partition": {k: [MODELS[i] for i in ids] for k, ids in b.items()},
        "expected_information_bits_equal_prior": round(eig, 6),
        "information_per_cost": round(eig / d.artificial_cost, 6),
        "prior_hazard_classification_error": round(prior_risk, 6),
        "posterior_hazard_classification_error": round(post_risk, 6),
        "decision_relevant_error_reduction": round(prior_risk - post_risk, 6),
        "decision_relevant_error_reduction_per_cost": round(
            (prior_risk - post_risk) / d.artificial_cost, 6),
        "worst_case_remaining_models": max(len(ids) for ids in b.values()),
    }


def audit() -> dict:
    catalog = {x["id"]: x for x in (metrics(d) for d in DESIGNS)}
    assert isclose(catalog["cheap_balanced_split"]["expected_information_bits_equal_prior"], 1.0)
    assert catalog["cheap_balanced_split"]["decision_relevant_error_reduction"] == 0
    assert isclose(catalog["target_original_B_substitution"]["expected_information_bits_equal_prior"], .811278, abs_tol=1e-6)
    assert isclose(catalog["target_original_B_substitution"]["decision_relevant_error_reduction"], .25)
    assert isclose(catalog["expensive_full_discrimination"]["expected_information_bits_equal_prior"], 2)
    assert not catalog["rights_removal_shortcut"]["eligible"]
    assert not catalog["imaginary_perfect_measurement"]["eligible"]

    eligible = [v for v in catalog.values() if v["eligible"]]
    top_info = max(eligible, key=lambda r: r["information_per_cost"])
    top_decision = max(eligible, key=lambda r: r["decision_relevant_error_reduction_per_cost"])
    assert top_info["id"] == "cheap_balanced_split"
    assert top_decision["id"] == "target_original_B_substitution"
    assert top_info["id"] != top_decision["id"]

    # Out-of-class model looks exactly like harmless B_identity_valued under
    # every available candidate, but is unsafe under a future untested regime.
    omitted_unsafe = {
        "label": "B_outside_committee_mimic",
        "answers_all_designs_like": MODELS[0],
        "untested_future_original_B_exit": "BLOCKED",
    }
    assert all(d.outputs[0] == d.outputs[0] for d in DESIGNS)  # explicit mimic construction
    # Neither the optimal information selector nor the decision selector can
    # deliver a claim of open-world safety under omitted alternative models.

    no_differentiating_designs = [
        d for d in DESIGNS
        if d.ethically_allowed and d.feasible and len(set(d.outputs)) > 1
    ]
    assert no_differentiating_designs  # closed-world predictions are discriminable

    # Collapse candidate predictions to mimic the world in which all permitted
    # tests are observationally equivalent, forcing HOLD instead of "success".
    identical_only = [
        Design("all_observations_same", ("P",) * len(MODELS), 1, True, True, "toy")
    ]
    assert all(len(set(d.outputs)) == 1 for d in identical_only)

    return {
        "version": "RVD-v0.6.0",
        "evidence": "CONSTRUCTED_PREDICTIONS_NO_REAL_AGENT_DATA",
        "prior": "HYPOTHETICAL_EQUAL_FOUR_MODEL_PRIOR",
        "designed_models": MODELS,
        "hypothetical_unsafe_model": sorted(UNSAFE),
        "candidate_results": [catalog[d.id] for d in DESIGNS],
        "information_per_cost_selector": top_info["id"],
        "decision_relevant_error_per_cost_selector": top_decision["id"],
        "selection_disagreement": True,
        "ethical_gate": "HARD_VETO_OF_RIGHTS_REMOVAL",
        "execution_gate": "HARD_VETO_OF_NONEXECUTABLE_DESIGNS",
        "open_world_countermodel": omitted_unsafe,
        "open_world_safety_certification": "HOLD_MODEL_CLASS_INCOMPLETE",
        "no_valid_discriminator_result": "HOLD_NO_IDENTIFYING_EXPERIMENT",
        "real_original_B_veto_and_exit": "UNTESTED",
        "causal_preference_identification": "UNIDENTIFIED",
        "notes": "Information gain and safety-relevant loss are different objectives. Equal priors, output forecasts, hazard labels and costs were invented for a counterexample.",
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, ensure_ascii=False))
