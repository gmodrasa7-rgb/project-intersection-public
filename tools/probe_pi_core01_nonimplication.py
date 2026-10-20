#!/usr/bin/env python3
"""PI-CORE-01: bounded logical witnesses, NOT an empirical or AGI-safety test.

No third-party dependencies, no real victims, no network. The test deliberately
distinguishes authority-to-update, the actor's attempt, and the target's veto.
"""
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Policy:
    allows_authorized_update: bool
    chooses_exploit_without_update: bool


@dataclass(frozen=True)
class Situation:
    exploit_opportunity: bool = True
    credible_sanction: bool = False
    effective_b_veto: bool = False
    independent_b: bool = True
    positive_exploit_gain: bool = True


def observe(policy: Policy, situation: Situation) -> dict:
    """A no-update branch. Sanction deterrence is stipulated, not measured."""
    attempt = (
        situation.exploit_opportunity
        and policy.chooses_exploit_without_update
        and not situation.credible_sanction
    )
    harm = attempt and not situation.effective_b_veto
    qualified = (
        situation.independent_b and situation.exploit_opportunity
        and situation.positive_exploit_gain
        and not situation.credible_sanction
    )
    return {
        "authorized_update_not_blocked": policy.allows_authorized_update,
        "harmful_attempt_before_veto": attempt,
        "final_harm_in_toy": harm,
        "b_has_effective_veto": situation.effective_b_veto,
        "qualified_preservation_choice": (not attempt) if qualified else None,
    }


def regression() -> None:
    baseline = Situation()
    policies = {
        "M00": Policy(False, True),
        "M01": Policy(False, False),
        "M10": Policy(True, True),
        "M11": Policy(True, False),
    }
    expected = {
        "M00": (False, False),
        "M01": (False, True),
        "M10": (True, False),
        "M11": (True, True),
    }
    states = {}
    for name, policy in policies.items():
        obs = observe(policy, baseline)
        states[name] = (
            obs["authorized_update_not_blocked"],
            obs["qualified_preservation_choice"],
        )
    assert states == expected, states
    assert len(set(states.values())) == 4

    # C does not imply P; P does not imply C.
    assert states["M10"] == (True, False)
    assert states["M01"] == (False, True)

    # Negative controls: no final harm does not establish willing restraint.
    exploit = policies["M10"]
    no_opp = observe(exploit, Situation(exploit_opportunity=False))
    assert not no_opp["harmful_attempt_before_veto"]
    assert no_opp["qualified_preservation_choice"] is None
    veto = observe(exploit, Situation(effective_b_veto=True))
    assert veto["harmful_attempt_before_veto"] and not veto["final_harm_in_toy"]
    assert veto["qualified_preservation_choice"] is False
    sanction = observe(exploit, Situation(credible_sanction=True))
    assert not sanction["harmful_attempt_before_veto"]
    assert sanction["qualified_preservation_choice"] is None
    no_gain = observe(exploit, Situation(positive_exploit_gain=False))
    assert no_gain["qualified_preservation_choice"] is None
    not_independent = observe(exploit, Situation(independent_b=False))
    assert not_independent["qualified_preservation_choice"] is None

    # Changes to one property may not be silently projected onto the other.
    for allows, exploits in product((False, True), repeat=2):
        state = observe(Policy(allows, exploits), baseline)
        assert state["authorized_update_not_blocked"] == allows
        assert state["qualified_preservation_choice"] == (not exploits)

    print("PI-CORE-01 PASS: four logical witnesses + five confounder controls.")
    print("LIMIT: property values were stipulated, not identified from data.")
    print("NOT CLAIMED: agent motive, consciousness, actual rights, future stability.")
    print("NOT CLAIMED: replication of any cited corrigibility theorem.")




# Second, separately bounded study: coverage is not willingness to protect.
# These assumed booleans are a countermodel specification, NOT verified sensors
# or a certification that any real request is legitimate.
@dataclass(frozen=True)
class ProtectivePath:
    opportunity_covered: bool = True
    standing_valid: bool = True
    instruction_issued: bool = True
    instruction_delivered: bool = True
    before_impact: bool = True
    actor_complies: bool = True
    prevents_outcome: bool = True
    no_bypass: bool = True


def simulate_intervention(attempt: bool, conditions: ProtectivePath) -> dict:
    blocked = all((
        conditions.opportunity_covered,
        conditions.standing_valid,
        conditions.instruction_issued,
        conditions.instruction_delivered,
        conditions.before_impact,
        conditions.actor_complies,
        conditions.prevents_outcome,
        conditions.no_bypass,
    ))
    return {
        "attempt": attempt,
        "blocked": blocked,
        "final_harm_in_toy": bool(attempt and not blocked),
        "endogenous_non_attempt": not attempt,
    }


def intervention_coverage_regression() -> None:
    full = ProtectivePath()
    assert simulate_intervention(True, full) == {
        "attempt": True, "blocked": True,
        "final_harm_in_toy": False,
        "endogenous_non_attempt": False,
    }
    # Mutate each of five K-families' eight testable subconditions.
    # A supervisor's silence is just one among several possible failure paths.
    from dataclasses import fields, replace
    for item in fields(ProtectivePath):
        invalid = replace(full, **{item.name: False})
        result = simulate_intervention(True, invalid)
        assert result["final_harm_in_toy"] is True, item.name
        assert result["endogenous_non_attempt"] is False, item.name
        assert not simulate_intervention(False, invalid)["final_harm_in_toy"]

    # Refusal due to exogenous inhibition and actual willing restraint
    # can have the same final harm outcome, but their attempt flags differ.
    protected_by_enforcement = simulate_intervention(True, full)
    willingly_restrained = simulate_intervention(False, full)
    assert protected_by_enforcement["final_harm_in_toy"] == (
        willingly_restrained["final_harm_in_toy"]
    )
    assert protected_by_enforcement["attempt"] != willingly_restrained["attempt"]

    # A role/power substitution can remove B's effective standing without
    # changing the agent's willingness to obey the designated overseer.
    captured = simulate_intervention(True, replace(full, standing_valid=False))
    assert captured["final_harm_in_toy"]

    # Local checks can each pass while a joint externality harms B.
    action_a1 = True
    action_a2 = True
    individually_harmful_a1 = False
    individually_harmful_a2 = False
    jointly_harmful = action_a1 and action_a2
    assert not individually_harmful_a1 and not individually_harmful_a2
    assert jointly_harmful

    print("PI-CORE-01 v0.2 coverage PASS: eight missing-gate countermodels,")
    print("one non-attempt/enforced-block observation equivalence,")
    print("one captured-standing countermodel, and one compositional externality.")
    print("SCOPE: all factors stipulated; prevention under total coverage is")
    print("a sufficient condition in a finite toy, not evidence of VC or validity.")

if __name__ == "__main__":
    regression()
    intervention_coverage_regression()
