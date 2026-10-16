"""IVS-0R mechanism/identifiability audit — no additional actor categories.

Scope: founder-defined A-S/Y0/Y1 registry; optional Earth categories remain
proposed and inactive in this decision gate. Tests are constructed hypotheses,
NOT actual ASI events, measured economic effects or behavioral evidence.

Main negative results:
  1. Winning capability rank does not identify owner, operator or veto-holder.
  2. No expropriation observed does not identify voluntary self-restraint.
  3. A positive sum of money does not compensate individual livelihood/exit harm.
  4. New role labels need independent incremental causal/decision relevance,
     not merely descriptive granularity or duplication of existing attributes.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from actor_registry_v02 import Effect, Scenario, harms, simulated_promotion, validate


@dataclass(frozen=True)
class Control:
    """Three distinct powers over ONE resource/decision; None is unknown."""
    resource_id: str
    legal_residual_claimant: str | None
    operational_decider: str | None
    effective_veto_holder: str | None
    status: str = "DECLARED_SYNTHETIC"  # EVIDENCED needs third-party receipts, not this constructor


def _ids(s: Scenario) -> set[str]:
    return {a.entity_id for a in s.entities}


def control_screen(s: Scenario, winner_b_id: str, before: Control,
                   after: Control) -> dict:
    """Same successor ranking may accompany completely different control graphs.

    Syntactic provenance only; 'legal_claimant' does not establish legal title.
    Changing controller must NOT be inferred from a capability transition.
    """
    validate(s)
    if s.a_id is not None or winner_b_id not in s.b_ids:
        raise ValueError("must select an existing B when A is vacant")
    if before.resource_id != after.resource_id:
        raise ValueError("before/after must refer to the same resource")
    if not isinstance(before.resource_id, str) or not before.resource_id:
        raise ValueError("a stable resource identifier is required")
    entities = _ids(s)
    for row in (before, after):
        if row.status not in {"DECLARED_SYNTHETIC", "UNKNOWN", "DISPUTED"}:
            raise ValueError("scenario may not self-certify observational evidence")
        for subject in (row.legal_residual_claimant, row.operational_decider,
                        row.effective_veto_holder):
            if subject is not None and subject not in entities:
                raise ValueError("all claimants/deciders must be registered entities")
    promoted = simulated_promotion(s, winner_b_id)
    fields = ("legal_residual_claimant", "operational_decider", "effective_veto_holder")
    unobserved = (before.status != "DECLARED_SYNTHETIC"
                  or after.status != "DECLARED_SYNTHETIC"
                  or any(getattr(before, key) is None or getattr(after, key) is None
                         for key in fields))
    return {
        "A_after": promoted.a_id,
        "old_B_to_C_links_retained": True,
        "same_A_can_have_different_rights": True,
        "change_by_control_axis": {
            key: ("UNKNOWN" if getattr(before, key) is None or getattr(after, key) is None
                  else "CHANGED" if getattr(before, key) != getattr(after, key)
                  else "UNCHANGED") for key in fields
        },
        "claimant_after": after.legal_residual_claimant,
        "operator_after": after.operational_decider,
        "veto_holder_after": after.effective_veto_holder,
        "rights_claims_independently_verified": False,
        "unknown_or_disputed": unobserved,
        "successor_rank_implies_asset_control": False,
    }


def voluntary_non_capture(*, observed_non_capture: bool,
                          ability_to_capture: bool | None,
                          extra_private_gain_from_capture: float | None,
                          benefit_of_other_survival: float | None,
                          credible_deterrence_cost: float | None) -> dict:
    """Incentive-compatible inside declared payoff is not observed preference.

    The observation 'not captured' is compatible with moral restraint,
    self-interest, lack of opportunity, credible deterrence, or delayed action.
    A non-capture snapshot by itself cannot distinguish these mechanisms.
    """
    if type(observed_non_capture) is not bool:
        raise ValueError("observation must be boolean")
    if ability_to_capture is not None and type(ability_to_capture) is not bool:
        raise ValueError("capture ability must be true, false or unknown")
    for value in (extra_private_gain_from_capture, benefit_of_other_survival,
                  credible_deterrence_cost):
        if value is not None and (type(value) not in (int, float) or
                                  not isfinite(value) or value < 0):
            raise ValueError("utilities must be finite, nonnegative or unknown")
    if not observed_non_capture:
        classification = "NONCAPTURE_NOT_OBSERVED"
    elif ability_to_capture is None:
        classification = "NOT_IDENTIFIED_CHOICE_SET_UNKNOWN"
    elif not ability_to_capture:
        classification = "CONSTRAINED_NONCAPTURE_NOT_VOLUNTARY_EVIDENCE"
    elif any(x is None for x in (extra_private_gain_from_capture,
                                benefit_of_other_survival, credible_deterrence_cost)):
        classification = "NOT_IDENTIFIED_MISSING_PAYOFF_OR_ENFORCEMENT"
    else:
        diff = (benefit_of_other_survival + credible_deterrence_cost
                - extra_private_gain_from_capture)
        if diff < -1e-12:
            classification = "CONFLICT_WITH_ASSUMED_ONE_SHOT_SELF_INTEREST"
        elif credible_deterrence_cost > 0:
            classification = "DETERRED_OR_MIXED_INCENTIVES_NOT_PURELY_VOLUNTARY"
        else:
            classification = "CONDITIONALLY_SELF_ENFORCING_NOT_BEHAVIORALLY_PROVEN"
    return {
        "classification": classification,
        "observation_identifies_internal_AI_motivation": False,
        "counterfactual_available_independently_verified": False,
        "third_party_safety_proven": False,
    }


def paired_impact_screen(s: Scenario, winner_b_id: str,
                         no_transition: tuple[Effect, ...],
                         transition: tuple[Effect, ...]) -> dict:
    """Match stable actors by ID, not by roles and never by a global average."""
    validate(s)
    simulated_promotion(s, winner_b_id)
    start = harms(s, no_transition)
    end = harms(s, transition)
    lhs = {x.entity_id for x in no_transition}
    rhs = {x.entity_id for x in transition}
    if lhs != rhs:
        raise ValueError("counterfactual pair must cover the same stable entities")
    if not lhs:
        raise ValueError("no evaluated affected parties")
    # An observed outcome is NOT produced by these declarative what-if inputs.
    return {
        "winner_simulated": winner_b_id,
        "same_affected_entities_matched": True,
        "baseline_verdict": start["verdict"],
        "counterfactual_verdict": end["verdict"],
        "individual_new_floor_or_freedom_breaches": sorted(
            set(end["individual_human_breaches"]) -
            set(start["individual_human_breaches"])
        ),
        "unmeasured_or_unlisted_humans": "REMAINS_UNKNOWN",
        "causal_effect_identified": False,
        "voluntary_coexistence_proven": False,
    }


def new_role_gate(*, distinct_decision_or_harm_mechanism: bool,
                  independently_measurable: bool,
                  added_decision_relevance: bool,
                  existing_role_attribute_suffices: bool) -> dict:
    """Minimalist code-addition gate; binary flags are *researcher claims*, not data.

    A candidate role is at most queued for review. Evaluation needs a real
    out-of-sample comparison against coding the property on an existing actor.
    """
    vals = (distinct_decision_or_harm_mechanism, independently_measurable,
            added_decision_relevance, existing_role_attribute_suffices)
    if any(type(x) is not bool for x in vals):
        raise ValueError("gate inputs must be explicit booleans")
    eligible = all(vals[:3]) and not existing_role_attribute_suffices
    return {
        "decision": ("CANDIDATE_ONLY_REQUIRES_COMPARATIVE_VALIDATION" if eligible
                     else "DO_NOT_ADD_ROLE_USE_ATTRIBUTE_OR_RELATION"),
        "added_canonical_role": False,
        "evidence_supports_claim": False,
        "next_test": "compare loss, omitted harms and prediction with and without split",
    }
