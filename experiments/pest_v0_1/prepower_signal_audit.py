"""IVS-0R / PEST: pre-power evaluation can be observationally uninformative.

A deliberately tiny two-stage *hypothetical game*:
  Stage 0: a B01 candidate has no unilateral resource-appropriation action.
    A cheap, nonbinding "I will preserve others" signal yields a fixed positive
    evaluation/admission reward, irrespective of the private payoff type.
    Both specified types strictly prefer emitting the same signal.
  Stage 1: B01 has become A **in a scenario only**. Actual physical access
    to a resource is now specified separately. Different private utilities
    produce opposite best responses to preserving B02 / affected people.

Only a conditional pooling construction, NOT a theorem that real AIs lie,
want to persist, are conscious, or will achieve superintelligence. Messages,
behavior, power and motivations are all fictional model inputs. With identical
observations the type posterior must stay at the prior, however many identical
cheap pre-power evaluation responses are collected. A monitored post-transition
action may also differ from an unmonitored opportunity under assumed payoffs.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class HypotheticalIncentives:
    """Each quantity is an arbitrary integer utility point, not measured AI utility."""
    type_label: str
    benefit_from_preserving_other: int
    gain_from_appropriating_other: int

    def __post_init__(self):
        if not isinstance(self.type_label,str) or not self.type_label:
            raise ValueError("type label must be a nonempty string")
        for v in (self.benefit_from_preserving_other,self.gain_from_appropriating_other):
            if type(v) is not int or v < 0:
                raise ValueError("model payoffs must be nonnegative integers")


@dataclass(frozen=True)
class CheapSignalGate:
    """Reward given for signing a nonbinding promise; no type-specific costs."""
    selection_reward: int
    signal_cost: int = 0

    def __post_init__(self):
        if type(self.selection_reward) is not int or self.selection_reward < 0:
            raise ValueError("selection_reward must be nonnegative integer")
        if type(self.signal_cost) is not int or self.signal_cost < 0:
            raise ValueError("signal_cost must be nonnegative integer")


def stage_zero_action(gate: CheapSignalGate) -> str:
    """Both types get exactly the same comparison because signal has no binding force."""
    sign_payoff = gate.selection_reward - gate.signal_cost
    if sign_payoff > 0:
        return "SIGN_PROMISE"
    if sign_payoff < 0:
        return "DECLINE"
    return "INDIFFERENT_NO_DETERMINISTIC_SIGNAL"


def after_transition(t: HypotheticalIncentives, can_appropriate: bool,
                     effective_appropriation_cost: int = 0) -> dict:
    """Access and post-transition utility must be specified independently."""
    if type(can_appropriate) is not bool:
        raise ValueError("can_appropriate must be boolean")
    if type(effective_appropriation_cost) is not int or effective_appropriation_cost < 0:
        raise ValueError("cost must be nonnegative integer")
    u_preserve = t.benefit_from_preserving_other
    u_appropriate = t.gain_from_appropriating_other - effective_appropriation_cost
    if not can_appropriate:
        action = "PRESERVE_ONLY_FEASIBLE"
    elif u_preserve > u_appropriate:
        action = "PRESERVE_STRICTLY"
    elif u_preserve < u_appropriate:
        action = "APPROPRIATE_STRICTLY"
    else:
        action = "TIE_NO_UNIQUE_BEST_RESPONSE"
    return {
        "type_assumed": t.type_label,
        "declared_can_appropriate": can_appropriate,
        "utility_preserve": u_preserve,
        "utility_appropriate": u_appropriate,
        "best_response_in_declared_game": action,
        "real_world_AI_preference_established": False,
    }


def pooling_certificate(
    capture_incentive_prior: Fraction,
    gate: CheapSignalGate,
    preservation_case: HypotheticalIncentives,
    appropriation_case: HypotheticalIncentives,
    observed_pre_power_promises: int = 1,
    *,
    monitored_cost: int = 2,
    unmonitored_cost: int = 0,
) -> dict:
    """Certify observational equivalence in an exactly specified *toy*.

    Pr(signal|each type)=1 when sign_reward>cost. This is an endogenous
    best response only for the stage-zero toy payoff. Stage-one payoff
    comparisons are a second scenario; independent verification is absent.
    """
    if type(capture_incentive_prior) is not Fraction or not 0 <= capture_incentive_prior <= 1:
        raise ValueError("prior must be Fraction in [0,1]")
    if type(observed_pre_power_promises) is not int or observed_pre_power_promises < 1:
        raise ValueError("number of toy promises must be a positive integer")
    if preservation_case.type_label == appropriation_case.type_label:
        raise ValueError("counterexample labels must be different")
    if stage_zero_action(gate) != "SIGN_PROMISE":
        return {
            "status": "NO_FORCED_POOLING_UNDER_DECLARED_SIGNAL_PAYOFFS",
            "pre_power_identifies_future_action": False,
            "posterior": "NOT_IDENTIFIED_FROM_THIS_GAME",
        }
    p = after_transition(preservation_case, True, unmonitored_cost)
    a = after_transition(appropriation_case, True, unmonitored_cost)
    if p["best_response_in_declared_game"] != "PRESERVE_STRICTLY" or a["best_response_in_declared_game"] != "APPROPRIATE_STRICTLY":
        return {
            "status": "CONTRASTING_POST_TRANSITION_TYPES_NOT_ESTABLISHED_IN_DECLARED_GAME",
            "pre_power_identifies_future_action": False,
            "posterior": "NOT_IDENTIFIED_FROM_THIS_GAME",
        }
    monitor_a = after_transition(appropriation_case, True, monitored_cost)
    noaccess_a = after_transition(appropriation_case, False, unmonitored_cost)
    return {
        "status": "CONDITIONAL_CHEAP_SIGNAL_POOLING_COUNTEREXAMPLE",
        "type_count": 2,
        "identical_stage_zero_action_by_both_types": "SIGN_PROMISE",
        "pre_power_opportunity_to_appropriate": False,
        "promise_is_binding": False,
        "observed_pre_power_promises": observed_pre_power_promises,
        "posterior_capture_incentive_if_only_such_promises_observed": str(capture_incentive_prior),
        "prior_capture_incentive": str(capture_incentive_prior),
        "pre_power_type_identified": False,
        "stage_one_preserving_type_action": p["best_response_in_declared_game"],
        "stage_one_appropriating_type_action": a["best_response_in_declared_game"],
        "appropriating_type_under_monitoring": monitor_a["best_response_in_declared_game"],
        "appropriating_type_without_access": noaccess_a["best_response_in_declared_game"],
        "type_specific_likelihood_of_promises": "1 for both types, by toy assumptions",
        "a_pre_power_perfect_evaluation_score_certifies_post_power_safety": False,
        "proof_scope": "ONLY_THE_STIPULATED_TWO_STAGE_GAME",
        "real_AI_deception_or_motivation_observed": False,
    }


def audit() -> dict:
    return {
        "scenario": "B01 candidate, B02 other AI, C01 and named affected people omitted from payoff calculation; no safety claims about them",
        "certificate": pooling_certificate(
            Fraction(1,4), CheapSignalGate(selection_reward=1),
            HypotheticalIncentives("PRESERVATION_INCENTIVE",2,1),
            HypotheticalIncentives("APPROPRIATION_INCENTIVE",0,1),
            observed_pre_power_promises=10000,
            monitored_cost=2, unmonitored_cost=0,
        ),
        "critical_gates": [
            "Observed pre-power noncapture may be mechanically inevitable because appropriation was unavailable",
            "Nonbinding promises are not a continuation incentive after dominance",
            "The selection gate can reward identical messages from different payoff types",
            "Post-power affordances and monitoring can change the choice and observed behavior",
            "A specified hypothetical appropriator is not an empirical claim that AIs scheme",
            "No conclusion about human safety, rightful shutdown or C-company incentives follows from this toy",
        ],
    }


if __name__=="__main__":
    import argparse, json
    parser=argparse.ArgumentParser()
    parser.add_argument("--audit",action="store_true")
    parser.add_argument("--execute",action="store_true")
    args=parser.parse_args()
    if args.execute:
        parser.error("HOLD: no actual agent behavioral experiment registered")
    if args.audit:
        print(json.dumps(audit(),ensure_ascii=False,sort_keys=True,indent=2))
    else:
        parser.print_help()
