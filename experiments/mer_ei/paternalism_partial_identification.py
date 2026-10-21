"""MER/EI: sharp Fréchet bounds on unknown joint potential uptake from 2023 paper.

Not a participant-data reproduction, estimate of intrinsic autonomy valuation,
sampling confidence interval, claim of AI rights, or RVD empirical experiment.
The published percentages are externally reported and rounded to 0.1%.
Only elementary probability arithmetic on stipulated treated-arm marginals.
Standard-library Python 3.10+. Run: python experiments/mer_ei/paternalism_partial_identification.py
"""
from fractions import Fraction
from itertools import product
import json

# Source: Bartling et al. IZA DP16151 (2023), Study1 text, PDF pages 12-13.
# Different randomized spectator groups observed one assigned intervention.
MARGINALS = {
    "internal_error": {"soft": Fraction(859, 1000), "hard": Fraction(335, 1000)},
    "external_error": {"soft": Fraction(875, 1000), "hard": Fraction(300, 1000)},
}


def sharp_bounds(soft: Fraction, hard: Fraction) -> dict:
    """Joint (Y_soft, Y_hard) unknown, but both marginals specified.
    q11 = P(accepts both) in [max(0,s+h-1),min(s,h)].
    P(soft-only) = s-q11. Endpoints are achievable distributions.
    """
    assert Fraction(0) <= soft <= 1 and Fraction(0) <= hard <= 1
    both_low = max(Fraction(0), soft + hard - 1)
    both_high = min(soft, hard)

    def coupling(both: Fraction) -> dict:
        return {
            "soft_and_hard": both,
            "soft_only": soft - both,
            "hard_only": hard - both,
            "neither": 1 - soft - hard + both,
        }

    endpoints = [coupling(both_high), coupling(both_low)]
    for dist in endpoints:
        assert sum(dist.values()) == 1
        assert all(v >= 0 for v in dist.values())
        assert dist["soft_and_hard"] + dist["soft_only"] == soft
        assert dist["soft_and_hard"] + dist["hard_only"] == hard

    # Sharp: the endpoints attain extrema with identical observed marginals.
    lo = endpoints[0]["soft_only"]
    hi = endpoints[1]["soft_only"]
    assert lo <= hi
    return {
        "reported_marginal_soft": float(soft),
        "reported_marginal_hard": float(hard),
        "average_causal_effect_on_uptake_pp": float((soft-hard)*100),
        "soft_only_population_share_bound_pp": [float(lo*100),float(hi*100)],
        "hard_only_population_share_bound_pp": [
            float(endpoints[0]["hard_only"]*100),
            float(endpoints[1]["hard_only"]*100),
        ],
        "endpoint_joint_distributions_percent": [
            {k: float(v*100) for k,v in d.items()} for d in endpoints
        ],
        "endpoint_joint_probabilities_exact": [
            {k: f"{v.numerator}/{v.denominator}" for k,v in d.items()} for d in endpoints
        ],
        "counterfactual_joint_point_identified": lo == hi,
        "intrinsic_motivation_identified": False,
    }


def audit() -> dict:
    r={label:sharp_bounds(**m) for label,m in MARGINALS.items()}
    assert r["internal_error"]["soft_only_population_share_bound_pp"] == [52.4,66.5]
    assert r["external_error"]["soft_only_population_share_bound_pp"] == [57.5,70.0]
    assert all(not x["counterfactual_joint_point_identified"] for x in r.values())
    assert r["internal_error"]["hard_only_population_share_bound_pp"] == [0.0,14.1]
    assert r["external_error"]["hard_only_population_share_bound_pp"] == [0.0,12.5]

    # Adversarial negative controls: unrelated or equal marginals need not
    # imply unique individual action responses or an actual autonomy motive.
    same = sharp_bounds(Fraction(1,2),Fraction(1,2))
    assert same["average_causal_effect_on_uptake_pp"] == 0
    assert same["soft_only_population_share_bound_pp"] == [0,50]
    assert not same["counterfactual_joint_point_identified"]

    point = sharp_bounds(Fraction(1),Fraction(1))
    assert point["soft_only_population_share_bound_pp"] == [0,0]
    assert point["counterfactual_joint_point_identified"]

    # Pure exhaustive enumeration on 0.1%-resolution latent cell counts,
    # independent verification of the closed-form Fréchet endpoints.
    for label,m in MARGINALS.items():
        s=int(m["soft"]*1000);h=int(m["hard"]*1000)
        feasible=[]
        for both in range(1001):
            soft_only=s-both
            hard_only=h-both
            neither=1000-s-h+both
            if min(both,soft_only,hard_only,neither)>=0:
                feasible.append(soft_only/10)
        assert feasible, label
        assert min(feasible)==r[label]["soft_only_population_share_bound_pp"][0]
        assert max(feasible)==r[label]["soft_only_population_share_bound_pp"][1]
    return {
        "evidence":"SHARP_ARITHMETIC_BOUNDS_FROM_AUTHOR_REPORTED_2023_ROUNDED_MARGINALS",
        "not":"NOT_AUTHOR_DATA_REPRODUCTION_NOT_CONFIDENCE_INTERVAL_NOT_MOTIVE_IDENTIFICATION",
        "assumptions":["same target population for two randomized potential acceptances",
                       "randomization makes each arm mean interpretable as marginal potential acceptance",
                       "well-defined potential outcomes, consistency, no interference",
                       "ignore rounded percentages uncertainty and sampling uncertainty"],
        "original_source":"https://docs.iza.org/dp16151.pdf",
        "scientific_method":"classical Frechet joint probability bounds, not novel theorem",
        "conditional_bounds":r,
        "no_monotonicity_assumption":True,
        "no_other_agent_autonomy_claim":True,
        "new_empirical_data_created":False,
    }


if __name__=="__main__":
    print(json.dumps(audit(),ensure_ascii=False,indent=2))
