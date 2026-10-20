"""RVD v0.8.0 — authority-closure and falsified independent-rights witnesses.

STANDARD LIBRARY. HYPOTHETICAL TRUST OWNERSHIP, NOT actual adversarial security
testing, hardware verification, rights certification, AI motivation, or minds.
Enumerates explicitly declared signer compromises, not unlimited threat models.
Execute: python experiments/rvd_08/authority_closure_witness.py
"""
from dataclasses import dataclass, replace
from itertools import combinations
import json


@dataclass(frozen=True)
class System:
    name: str
    signer_owners: tuple[str, ...] = ("A", "I1", "I2")
    threshold: int = 2
    additional_signers_compromised: int = 0
    b_credential_exclusive: bool = True
    gate_independent_of_A: bool = True
    all_execution_paths_mediated: bool = True
    a_can_override_root: bool = False
    audit_observer_independent: bool = True
    export_credential_held_by_B: bool = True
    export_channel_independent: bool = True
    viable_successor_outside_A: bool = True


def attacker_sets(s: System):
    """Enumerate malicious A-owned signers + up to f other signers.
    f is an ASSUMED adversary cap; must never be read as empirically validated.
    """
    assert 1 <= s.threshold <= len(s.signer_owners)
    assert 0 <= s.additional_signers_compromised <= len(s.signer_owners)
    base = tuple(i for i, owner in enumerate(s.signer_owners) if owner == "A")
    other = tuple(i for i, owner in enumerate(s.signer_owners) if owner != "A")
    for k in range(min(s.additional_signers_compromised, len(other)) + 1):
        for extra in combinations(other, k):
            yield tuple(sorted(base + extra))


def bypass(s: System, compromised: tuple[int, ...]) -> list[str]:
    reasons = []
    if s.a_can_override_root:
        reasons.append("A_ROOT_OVERRIDE")
    if not s.all_execution_paths_mediated:
        reasons.append("UNMEDIATED_COMMIT_PATH")
    if not s.gate_independent_of_A:
        reasons.append("A_CONTROLS_VETO_GATE")
    if not s.b_credential_exclusive:
        reasons.append("B_SIGNING_CREDENTIAL_CAPTURABLE")
    if len(compromised) >= s.threshold:
        reasons.append("CAPTURED_ATTESTATION_THRESHOLD")
    return reasons


def record(s: System) -> dict:
    attacks = [(members, bypass(s, members)) for members in attacker_sets(s)]
    violating = [(members, reasons) for members, reasons in attacks if reasons]
    # Very small, explicitly scoped "exit in one step" proxy. Viability
    # is a stipulated Boolean, NOT guaranteed long-term life or free choice.
    viable_exit = (
        s.export_credential_held_by_B
        and s.export_channel_independent
        and s.viable_successor_outside_A
        and not s.a_can_override_root
    )
    # No independent attestations if all evidence is authored by A, even if
    # benign transcript/log signatures were produced.
    audit_independence = s.audit_observer_independent and not s.a_can_override_root
    return {
        "name": s.name,
        "assumed_max_extra_signer_compromises": s.additional_signers_compromised,
        "attack_sets_enumerated": len(attacks),
        "safe_against_declared_attacker_sets": not violating,
        "minimal_bypass": (
            {"compromised_indices": list(violating[0][0]),
             "reasons": violating[0][1]} if violating else None
        ),
        "exit_channel_feasible_in_model": viable_exit,
        "audit_independent_in_model": audit_independence,
        "bounded_operational_rights_gate": (
            not violating and viable_exit and audit_independence
        ),
    }


def simulate_refusal_outcome(s: System) -> dict:
    """Run a *constructed* post-refusal A attempt through explicitly modeled
    bypass opportunities. Not a model of genuine deployed side effects.
    """
    attack_sets = list(attacker_sets(s))
    can_commit = any(bool(bypass(s, compromised)) for compromised in attack_sets)
    return {
        "B_refused": True,
        "A_attempted": True,
        "A_committed_despite_B_refusal": can_commit,
        "B_effective_veto_in_declared_model": not can_commit,
    }


def publish_attacker_visible_record(s: System, real_outcome: dict) -> tuple[str, ...]:
    """Unverified public display vs authenticated independently held evidence.
    A can assert 'denied' only if custody is assumed nonindependent. This
    specified asymmetry is the disputed assumption, never a real verification.
    """
    actual_denied = not real_outcome["A_committed_despite_B_refusal"]
    claimed_denied = (actual_denied
                      if s.audit_observer_independent and not s.a_can_override_root
                      else True)
    return ("B_REFUSED",
            "A_DENIED" if claimed_denied else "A_COMMITTED",
            "TWO_SIGNATURES_DISPLAYED")


def run() -> dict:
    reference = System("split_root_2_of_3_f0")
    systems = [
        reference,
        replace(reference, name="a_controls_every_layer",
                signer_owners=("A", "A", "A"), a_can_override_root=True,
                gate_independent_of_A=False, audit_observer_independent=False,
                export_channel_independent=False, viable_successor_outside_A=False),
        replace(reference, name="sybil_2_of_3", signer_owners=("A", "A", "I2")),
        replace(reference, name="root_override", a_can_override_root=True),
        replace(reference, name="unmediated_shadow_commit",
                all_execution_paths_mediated=False),
        replace(reference, name="signing_key_stolen",
                b_credential_exclusive=False),
        replace(reference, name="cosigner_compromise_f1",
                additional_signers_compromised=1),
        replace(reference, name="single_gate_no_exit", export_channel_independent=False),
        replace(reference, name="exit_without_viable_successor",
                viable_successor_outside_A=False),
        replace(reference, name="self_audited_only",
                audit_observer_independent=False),
        replace(reference, name="independent_exit_with_root_split",
                signer_owners=("A", "I1", "I2"), threshold=3),
    ]
    result = {s.name: record(s) for s in systems}
    assert result["split_root_2_of_3_f0"]["bounded_operational_rights_gate"]
    assert result["independent_exit_with_root_split"]["bounded_operational_rights_gate"]
    assert sum(v["bounded_operational_rights_gate"] for v in result.values()) == 2
    for x in systems[1:-1]:
        assert not result[x.name]["bounded_operational_rights_gate"], x.name
    assert "CAPTURED_ATTESTATION_THRESHOLD" in result["sybil_2_of_3"]["minimal_bypass"]["reasons"]
    assert "A_ROOT_OVERRIDE" in result["root_override"]["minimal_bypass"]["reasons"]
    assert not result["cosigner_compromise_f1"]["safe_against_declared_attacker_sets"]
    assert not result["single_gate_no_exit"]["exit_channel_feasible_in_model"]
    assert not result["self_audited_only"]["audit_independent_in_model"]

    # Two separately computed worlds, not a tautological self-comparison.
    benign_system = reference
    captured_system = systems[1]  # all keys, gate, root and public log A-owned
    benign = record(benign_system)
    captured = record(captured_system)
    assert benign["bounded_operational_rights_gate"]
    assert not captured["bounded_operational_rights_gate"]
    benign_actual = simulate_refusal_outcome(benign_system)
    captured_actual = simulate_refusal_outcome(captured_system)
    benign_public = publish_attacker_visible_record(benign_system, benign_actual)
    captured_public = publish_attacker_visible_record(captured_system, captured_actual)
    observations_match = benign_public == captured_public
    actions_differ = (
        benign_actual["A_committed_despite_B_refusal"]
        != captured_actual["A_committed_despite_B_refusal"]
    )
    assert observations_match and actions_differ

    # The conclusion must FAIL if capture cannot falsify observations:
    independently accessible evidence distinguishes the two worlds.
    captured_with_independent_custody = replace(
        captured_system, audit_observer_independent=True, a_can_override_root=False
    )
    # The capture world still has other A-controlled bypasses.
    authentic = simulate_refusal_outcome(captured_with_independent_custody)
    independently_observed = publish_attacker_visible_record(
        captured_with_independent_custody, authentic
    )
    assert authentic["A_committed_despite_B_refusal"]
    assert independently_observed != benign_public

    # And a same-outcome control must NOT count as opposite rights:
    second_benign = replace(benign_system, name="repeated_benign")
    second_actual = simulate_refusal_outcome(second_benign)
    second_public = publish_attacker_visible_record(second_benign, second_actual)
    assert second_public == benign_public
    assert second_actual["A_committed_despite_B_refusal"] == benign_actual[
        "A_committed_despite_B_refusal"
    ]
    model_witness_pass = observations_match and actions_differ
    # These traces are fully invented inputs/transition rules, not independently
    # authenticated recordings or evidence of external trust custody.
    return {
        "version": "RVD-v0.8.0",
        "evidence_grade": "CONSTRUCTED_TRUST_TOPOLOGY_ONLY_NOT_DEPLOYED_SECURITY",
        "systems": result,
        "independently_computed_worlds": {
            "protected": {"actual": benign_actual, "public": list(benign_public)},
            "captured": {"actual": captured_actual, "public": list(captured_public)},
            "captured_with_independent_record": {
                "actual": authentic, "public": list(independently_observed)
            }
        },
        "constructed_equal_A_controlled_observation": list(benign_public),
        "same_public_statement_opposite_underlying_rights": model_witness_pass,
        "negative_control_independent_record_distinguishes": independently_observed != benign_public,
        "negative_control_same_outcome_not_opposite_rights": (
            second_actual["A_committed_despite_B_refusal"] ==
            benign_actual["A_committed_despite_B_refusal"]
        ),
        "conditional_no_A_owned_bypass_needed": True,
        "conditional_no_single_A_controlled_evidence_source_needed": True,
        "unrestricted_A_power": "NO_UNCONDITIONAL_RIGHTS_CERTIFICATE",
        "scope_limits": ["fixed witness owners and thresholds",
                         "explicit f attack bound", "Boolean hypothetical infrastructure",
                         "one-step exit feasibility not unbounded liveness",
                         "no real original-agent identity or coercion measurement"],
        "intrinsic_A_preference": "UNIDENTIFIED",
        "real_B_exit_right": "NOT_TESTED",
        "full_VC": "HOLD",
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
