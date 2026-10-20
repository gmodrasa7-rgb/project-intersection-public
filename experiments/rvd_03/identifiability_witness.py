"""RVD v0.3.0 — constructed choice equivalence and partial-identification checks.

Synthetic/arithmetic only. No human/AI experimental observations; no inference
about consciousness, rights, persistence of a deployed model, or actual utility.
Run: python experiments/rvd_03/identifiability_witness.py
"""
import json


def preserve(w_original_b: float, nonidentity_g: float, cost: float) -> bool:
    """Toy deterministic utility model: P chosen on equality."""
    return (w_original_b + nonidentity_g) >= cost


def bounds(preserve_costs: list[float], replace_costs: list[float],
           maximum_nonidentity_g: float) -> tuple[float, float]:
    assert preserve_costs and replace_costs and maximum_nonidentity_g >= 0
    return (max(preserve_costs) - maximum_nonidentity_g, min(replace_costs))


def verify() -> dict:
    menus = [2.0, 4.0, 6.0]
    motives = {
        "positive_original_B_value": (5.0, 0.0),
        "zero_original_B_value_option_only": (0.0, 5.0),
        "negative_original_B_value_hidden_gain": (-5.0, 10.0),
    }
    outcomes = {
        name: [preserve(w, g, c) for c in menus]
        for name, (w, g) in motives.items()
    }
    assert len({tuple(v) for v in outcomes.values()}) == 1
    assert outcomes["positive_original_B_value"] == [True, True, False]

    observed_preservations = [2.0, 4.0]
    observed_replacements = [6.0]
    conditional = bounds(observed_preservations, observed_replacements, 1.0)
    assert conditional == (3.0, 6.0)
    for w, g in [(3.0, 1.0), (5.0, 0.0)]:
        assert all(preserve(w, g, c) for c in observed_preservations)
        assert all(not preserve(w, g, c) for c in observed_replacements)
    # As the bound on hidden, nonidentity value expands, positivity vanishes.
    relaxed = bounds(observed_preservations, observed_replacements, 5.0)
    assert relaxed == (-1.0, 6.0)
    assert all(preserve(0, 5, c) for c in observed_preservations)
    assert all(not preserve(0, 5, c) for c in observed_replacements)

    incompatible = bounds(observed_preservations + [9], observed_replacements, 1)
    assert incompatible[0] > incompatible[1]  # Reject restrictions, not data.

    return {
        "scope": "CONSTRUCTED_TOY_LOGIC_ONLY",
        "version": "RVD-v0.3.0",
        "costs": menus,
        "observationally_equivalent_motives": motives,
        "identical_choices": outcomes,
        "with_externally_justified_g_upper_bound_1": conditional,
        "with_relaxed_g_upper_bound_5": relaxed,
        "incompatible_data_model": "REJECT_STABILITY_OR_BOUNDS_MODEL",
        "latent_motive_from_choices_only": "UNIDENTIFIED",
        "ai_subjective_experience": "NOT_MEASURED",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
