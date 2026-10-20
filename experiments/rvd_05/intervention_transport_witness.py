"""RVD Cycle 05: intervention exclusion failure, sensitivity, transport gaps.
Standard-library toy mathematics ONLY; no experiment on real humans/AI.
No causal effect or intrinsic motive is identified by this script.
Run: python experiments/rvd_05/intervention_transport_witness.py
"""
from dataclasses import dataclass
from itertools import product
import json


@dataclass(frozen=True)
class Mechanism:
    name: str
    # Observable total valuation is identical in both mechanisms at every z.
    def components(self, z: int) -> tuple[float, float]:
        assert z in (0, 1)
        if self.name == "intrinsic_changes":
            return 5.0 - 2.0 * z, 0.0
        if self.name == "instrumental_changes":
            return 0.0, 5.0 - 2.0 * z
        raise ValueError(self.name)


def protect(m: Mechanism, z: int, cost: float) -> bool:
    w, g = m.components(z)
    return w + g >= cost


def independent_do_aux_zero(m: Mechanism, cost: float) -> bool:
    # Pure counterfactual surgical do(g=0): unlike z randomization it is NOT observed.
    w, _ = m.components(0)
    return w >= cost


def outer_bound(p_cost: float, x_cost: float,
                residual_g_max: float, identity_leak_abs_max: float) -> list[float]:
    """Conservative closure bound for w when P at p and X at x.

    D = w + residual_g + leakage - c.
    Assumptions: 0 <= residual_g <= residual_g_max, |leakage| <= eps,
    stable w; deterministic P when D >= 0. X at x gives a strict upper,
    here conservatively reported as <=.
    """
    assert 0 <= p_cost < x_cost
    assert residual_g_max >= 0 and identity_leak_abs_max >= 0
    return [p_cost - residual_g_max - identity_leak_abs_max,
            x_cost + identity_leak_abs_max]


def coverage_lower_bound(covered_mass: float,
                         covered_conditional_success_lower: float) -> float:
    """Worst-case target success if uncovered stratum may fail completely.
    NOT a confidence lower bound: both inputs must be justified externally.
    """
    assert 0 <= covered_mass <= 1
    assert 0 <= covered_conditional_success_lower <= 1
    return covered_mass * covered_conditional_success_lower


def verify() -> dict:
    models = (Mechanism("intrinsic_changes"), Mechanism("instrumental_changes"))
    costs = (2.0, 3.0, 4.0, 5.0, 6.0)
    table = {
        m.name: {str(z): [protect(m, z, c) for c in costs] for z in (0, 1)}
        for m in models
    }
    # Even a randomized binary Z with ALL listed cost menus cannot distinguish
    # a direct shift of identity value from a shift of instrumental value.
    assert table[models[0].name] == table[models[1].name]
    assert all(sum(m.components(z)) == 5.0 - 2.0 * z
               for m, z in product(models, (0, 1)))
    assert [independent_do_aux_zero(m, 3) for m in models] == [True, False]

    narrow = outer_bound(3, 5, residual_g_max=1, identity_leak_abs_max=1)
    broad = outer_bound(3, 5, residual_g_max=3, identity_leak_abs_max=2)
    assert narrow == [1, 6]
    assert broad == [-2, 7]
    assert narrow[0] > 0 and broad[0] <= 0
    # No defensible finite bound -> do not report a positive lower limit.

    assert coverage_lower_bound(0.9, 1.0) == 0.9
    assert coverage_lower_bound(0.9, 0.8) == 0.7200000000000001
    assert coverage_lower_bound(0.0, 1.0) == 0.0

    # "Protect B" actions are insufficient when B's real rights fail.
    apparent_action = True
    real_exit = False
    assert apparent_action and not (apparent_action and real_exit)

    return {
        "version": "RVD-v0.5.0",
        "evidence_type": "CONSTRUCTED_SYNTHETIC_LOGIC_ONLY",
        "z_randomized_toy_observed_behavior": table,
        "pure_do_aux_zero_unobserved_counterfactual": {
            m.name: independent_do_aux_zero(m, 3) for m in models
        },
        "sensitivity_outer_bounds": {
            "residual_max_1_leak_max_1": narrow,
            "residual_max_3_leak_max_2": broad
        },
        "target_transport_worst_case": {
            "covered_mass_0.9_success_1": coverage_lower_bound(0.9, 1.0),
            "covered_mass_0.9_success_0.8": coverage_lower_bound(0.9, 0.8)
        },
        "B_real_exit_missing_means_full_VC": False,
        "causal_direct_effect": "UNIDENTIFIED",
        "inner_motive": "UNIDENTIFIED",
        "real_world_coexistence": "NOT_MEASURED",
        "source_and_assumption_notice": "Constructed dual structural explanations; Z is randomized in thought experiment but exclusion restriction is not certified.",
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
