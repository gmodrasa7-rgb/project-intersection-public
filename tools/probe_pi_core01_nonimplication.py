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


if __name__ == "__main__":
    regression()
