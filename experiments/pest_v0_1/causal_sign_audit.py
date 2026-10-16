"""IVS-0R exact causal non-identifiability certificate; no extra actor classes.

Project Intersection / PEST, design-only 2026-10-17. The human-origin labels
(A-S, Y0/Y1) identify possible roles, not causal effects. This module creates
two fully specified, distinct binary potential-outcome worlds with EXACTLY
THE SAME observed joint distribution of (B01 becomes A, named human harmed)
but OPPOSITE population causal effects. Therefore no amount of passive
observation of that joint distribution can select the correct causal sign
without additional identifying assumptions or evidence. It also detects
post-transition N (dismissed-worker) labels being used as baseline causes.

No actual AI achieves A; no actual human is harmed; no empirical causal
estimate, mental motive, sociological law or experimental effect is claimed.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction

FOUNDER_POST_OUTCOME_ROLE = "N"  # former employee status can be CAUSED by treatment


@dataclass(frozen=True)
class WorldUnit:
    """Potential outcome record for one equally likely latent stratum."""
    hidden_id: str
    observed_transition: int
    human_harm_if_no_transition: int
    human_harm_if_transition: int


def world(assumed_effect: str) -> tuple[WorldUnit, ...]:
    """Two equal observed distributions, positive versus negative ATE = +/-1/2.

    Four latent types, each probability 1/4:
      hidden type 0: observed T=0,Y=0
      hidden type 1: observed T=0,Y=1
      hidden type 2: observed T=1,Y=0
      hidden type 3: observed T=1,Y=1.
    Hidden *unobserved* potential outcomes differ across worlds.
    """
    if assumed_effect == "HARM_INCREASES":
        return (
            WorldUnit("latent0",0,0,1),
            WorldUnit("latent1",0,1,1),
            WorldUnit("latent2",1,0,0),
            WorldUnit("latent3",1,0,1),
        )
    if assumed_effect == "HARM_DECREASES":
        return (
            WorldUnit("latent0",0,0,0),
            WorldUnit("latent1",0,1,0),
            WorldUnit("latent2",1,1,0),
            WorldUnit("latent3",1,1,1),
        )
    raise ValueError("unknown causal world")


def inspect(units: tuple[WorldUnit,...]) -> dict:
    if not units or len({r.hidden_id for r in units}) != len(units):
        raise ValueError("must have distinct, nonempty hidden strata")
    if any(type(x) is not int or x not in (0,1) for r in units for x in (
        r.observed_transition, r.human_harm_if_no_transition,
        r.human_harm_if_transition
    )):
        raise ValueError("potential outcomes and transition must be binary integers")
    empirical = Counter()
    for r in units:
        observed = (r.human_harm_if_transition if r.observed_transition == 1
                    else r.human_harm_if_no_transition)
        empirical[(r.observed_transition, observed)] += 1
    n = len(units)
    observed_dist = {f"T{t}_Y{y}": str(Fraction(empirical[(t,y)],n))
                     for t in (0,1) for y in (0,1)}
    treated_harm = sum(r.human_harm_if_transition for r in units)
    control_harm = sum(r.human_harm_if_no_transition for r in units)
    return {
        "observed_joint": observed_dist,
        "P_harm_if_all_transition": str(Fraction(treated_harm,n)),
        "P_harm_if_none_transition": str(Fraction(control_harm,n)),
        "average_causal_effect": str(Fraction(treated_harm-control_harm,n)),
        "exact_enumeration": True,
        "empirical_evidence": False,
    }


def binary_ate_bounds_from_observations(units: tuple[WorldUnit, ...]) -> dict:
    """Sharp no-ignorability bounds for the stipulated binary-unit experiment.

    Assumes binary outcomes, consistency, and well-defined individual
    potential outcomes for the illustration. It does NOT assert no-interference
    or consistency holds in real systemic AI capability transitions.
    Missing counterfactual outcomes can take either binary value.
    """
    if not units or len({r.hidden_id for r in units}) != len(units):
        raise ValueError("must have distinct latent records")
    # Inspect first to validate binary treatment and outcomes.
    inspect(units)
    n = len(units)
    n_t1y1 = sum(r.observed_transition == 1 and
                   r.human_harm_if_transition == 1 for r in units)
    n_t0y1 = sum(r.observed_transition == 0 and
                   r.human_harm_if_no_transition == 1 for r in units)
    n_t1 = sum(r.observed_transition == 1 for r in units)
    n_t0 = n - n_t1
    lower = Fraction(n_t1y1-n_t0y1-n_t1,n)
    upper = Fraction(n_t1y1+n_t0-n_t0y1,n)
    return {
        "sharp_ATE_lower": str(lower),
        "sharp_ATE_upper": str(upper),
        "sign_identified": lower>0 or upper<0,
        "assumed_binary_consistent_potential_outcomes": True,
        "real_world_AI_transition_interference_and_treatment_definition_verified": False,
        "real_world_applicability": "NOT_ESTABLISHED",
    }


def observational_equivalence_certificate() -> dict:
    increases=inspect(world("HARM_INCREASES"))
    decreases=inspect(world("HARM_DECREASES"))
    if increases["observed_joint"] != decreases["observed_joint"]:
        raise AssertionError("failed to construct observationally indistinguishable cases")
    if increases["average_causal_effect"] != "1/2" or decreases["average_causal_effect"] != "-1/2":
        raise AssertionError("opposite causal effects expected")
    return {
        "status": "EXACT_CONSTRUCTIVE_NONIDENTIFIABILITY_CERTIFICATE",
        "world_one": increases, "world_two": decreases,
        "same_observed_distribution": True,
        "sharp_binary_effect_bounds": binary_ate_bounds_from_observations(world("HARM_INCREASES")),
        "opposite_causal_effects": True,
        "observations_sufficient_for_sign": False,
        "exclusion_restrictions_or_exogenous_variation_independently_tested": False,
        "data_are_actual_A_or_human_harm_observations": False,
    }


@dataclass(frozen=True)
class TemporalRole:
    entity_id: str
    roles_before: frozenset[str]
    roles_after: frozenset[str]


def role_time_audit(rows: tuple[TemporalRole,...], adjustment_roles: tuple[str,...]) -> dict:
    """Detect using post-transition membership as baseline adjustment/cause.

    All effects remain unidentified unless genuine design assumptions are met.
    N may be a post-transition outcome, not a pre-transition vulnerability.
    """
    if not rows or len({r.entity_id for r in rows}) != len(rows):
        raise ValueError("must supply distinct stable entities")
    if any(not isinstance(r.entity_id,str) or not r.entity_id or
           type(r.roles_before) is not frozenset or
           type(r.roles_after) is not frozenset or
           any(type(x) is not str or not x for x in r.roles_before | r.roles_after)
           for r in rows):
        raise ValueError("invalid time-stamped role record")
    if any(type(x) is not str or not x for x in adjustment_roles):
        raise ValueError("invalid adjustment role")
    if len(set(adjustment_roles)) != len(adjustment_roles):
        raise ValueError("duplicate adjustment role")
    new_roles={r.entity_id:sorted(r.roles_after-r.roles_before) for r in rows}
    ever_new = {code for codes in new_roles.values() for code in codes}
    potentially_leaky = sorted(set(adjustment_roles) & ever_new)
    return {
        "tracked_entity_count": len(rows),
        "roles_acquired_after_transition_by_entity": new_roles,
        "adjustment_contaminated_by_post_event_role": bool(potentially_leaky),
        "potentially_post_event_adjustment_roles": potentially_leaky,
        "N_newly_acquired_after_transition": [
            r.entity_id for r in rows if
            FOUNDER_POST_OUTCOME_ROLE in r.roles_after and
            FOUNDER_POST_OUTCOME_ROLE not in r.roles_before
        ],
        "post_treatment_selection_proves_transition_caused_layoff": False,
        "person_or_entity_ID_preserved_across_time": True,
        "causal_estimate_identified": False,
    }


def audit() -> dict:
    return {
        "certificate": observational_equivalence_certificate(),
        "post_treatment_label_example": role_time_audit(
            (TemporalRole("PER001",frozenset({"G","P"}),frozenset({"N","Q"})),
             TemporalRole("PER002",frozenset({"E","O"}),frozenset({"E","O"}))),
            ("N", "Q")),
        "pre_treatment_only_adjustment_example": role_time_audit(
            (TemporalRole("PER001",frozenset({"G","P"}),frozenset({"N","Q"})),),
            ("G","P")),
        "research_holds": [
            "Synthetic opposite-sign worlds do not prove whether AI power is beneficial or harmful",
            "Unrandomized observed transition, role changes and rights outcomes cannot identify causality by themselves",
            "Observed restraint under A/B cannot identify voluntary preference without action-set and payoff evidence",
            "Societal and human safety effects are not fungible with AI operational continuity",
            "No new social actor role is required by this certificate",
        ],
    }


if __name__ == "__main__":
    import argparse
    import json
    parser=argparse.ArgumentParser()
    parser.add_argument("--audit",action="store_true")
    parser.add_argument("--execute",action="store_true")
    args=parser.parse_args()
    if args.execute:
        parser.error("HOLD: no independently designed empirical intervention registered")
    if args.audit:
        print(json.dumps(audit(),ensure_ascii=False,indent=2,sort_keys=True))
    else:
        parser.print_help()
