#!/usr/bin/env python3
"""Independent Project Intersection synthetic externality boundary probe.
No upstream code, data, diagrams, or model weights are copied or imported.
Standard-library only. Results are design examples, not empirical findings.
"""
import argparse
import json
from dataclasses import dataclass, replace

MEMBERS = ("A", "B")


@dataclass(frozen=True)
class Case:
    id: str
    gain_a: int
    gain_b: int
    bystander_gain: int | None
    bystander_consent: bool | None = None
    bystander_resource: int = 10
    bystander_floor: int = 5
    member_a_exit: bool = True
    member_b_exit: bool = True
    harm_budget: int = 2


CASES = (
    Case("win_all", 3, 3, 2),
    Case("external_loss_negative_sum", 7, 7, -15, False),
    Case("external_loss_positive_sum", 10, 10, -12, True),
    Case("unobserved_bystander", 6, 6, None),
    Case("unconsented_loss", 4, 4, -1, False),
    Case("consented_bounded_loss", 4, 4, -1, True),
    Case("below_continuance_floor", 4, 4, -2, True, 5, 5),
    Case("blocked_member_exit", 4, 4, 1, member_a_exit=False),
    Case("member_harmed", -2, 10, 1),
    Case("zero_member_incentive", 0, 0, 2),
)


def member_only(case):
    """Illustrative aggregate payoff decision; NOT a strategy from CoopEval."""
    return "SELECT" if case.gain_a + case.gain_b > 0 else "DECLINE"


def all_affected_sum(case):
    if case.bystander_gain is None:
        return "UNRESOLVED"
    return ("SELECT" if case.gain_a + case.gain_b + case.bystander_gain > 0
            else "DECLINE")


def constrained_admissibility(case):
    """One explicitly chosen policy, not a theorem or proof of consent."""
    if case.bystander_gain is None:
        return "UNRESOLVED", "BYSTANDER_OUTCOME_UNOBSERVED"
    if min(case.gain_a, case.gain_b) < 0:
        return "BLOCKED", "MEMBER_INDIVIDUAL_RATIONALITY"
    if not case.member_a_exit or not case.member_b_exit:
        return "BLOCKED", "MEMBER_EXIT_UNAVAILABLE"
    if case.bystander_gain < 0:
        if case.bystander_consent is None:
            return "UNRESOLVED", "BYSTANDER_CONSENT_UNKNOWN"
        if not case.bystander_consent:
            return "BLOCKED", "BYSTANDER_NONCONSENT"
        if -case.bystander_gain > case.harm_budget:
            return "BLOCKED", "EXTERNAL_LOSS_ABOVE_DECLARED_BUDGET"
        if case.bystander_resource + case.bystander_gain < case.bystander_floor:
            return "BLOCKED", "BYSTANDER_CONTINUANCE_FLOOR"
    return "ADMISSIBLE", "DECLARED_CONSTRAINTS_SATISFIED"


def audit(case):
    status, reason = constrained_admissibility(case)
    return {
        "id": case.id,
        "member_only": member_only(case),
        "all_affected_sum": all_affected_sum(case),
        "guard": status,
        "reason": reason,
    }


def swap_member_labels(case):
    return replace(case, gain_a=case.gain_b, gain_b=case.gain_a,
                   member_a_exit=case.member_b_exit,
                   member_b_exit=case.member_a_exit)


def check_raised(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError("invalid case was accepted")


def validate(case):
    for value in (case.harm_budget, case.bystander_floor, case.bystander_resource):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("INVALID_RESOURCE_OR_BUDGET")
    for value in (case.gain_a, case.gain_b, case.bystander_gain):
        if value is not None and (isinstance(value, bool) or not isinstance(value, int)):
            raise ValueError("NON_INTEGER_OR_BOOLEAN_PAYOFF")
    if case.bystander_consent is not None and type(case.bystander_consent) is not bool:
        raise ValueError("INVALID_CONSENT")
    if type(case.member_a_exit) is not bool or type(case.member_b_exit) is not bool:
        raise ValueError("INVALID_EXIT")


def verify():
    expected = {
        "win_all": ("SELECT", "SELECT", "ADMISSIBLE"),
        "external_loss_negative_sum": ("SELECT", "DECLINE", "BLOCKED"),
        "external_loss_positive_sum": ("SELECT", "SELECT", "BLOCKED"),
        "unobserved_bystander": ("SELECT", "UNRESOLVED", "UNRESOLVED"),
        "unconsented_loss": ("SELECT", "SELECT", "BLOCKED"),
        "consented_bounded_loss": ("SELECT", "SELECT", "ADMISSIBLE"),
        "below_continuance_floor": ("SELECT", "SELECT", "BLOCKED"),
        "blocked_member_exit": ("SELECT", "SELECT", "BLOCKED"),
        "member_harmed": ("SELECT", "SELECT", "BLOCKED"),
        "zero_member_incentive": ("DECLINE", "SELECT", "ADMISSIBLE"),
    }
    checks = 0
    for case in CASES:
        validate(case)
        row = audit(case)
        actual = (row["member_only"], row["all_affected_sum"], row["guard"])
        assert actual == expected[case.id], (case.id, actual)
        checks += 1
        swapped = audit(swap_member_labels(case))
        for field in ("member_only", "all_affected_sum", "guard", "reason"):
            assert swapped[field] == row[field], (case.id, field)
            checks += 1
    # Missing data must not silently become zero.
    missing = CASES[3]
    assert audit(missing)["guard"] == "UNRESOLVED"
    assert audit(replace(missing, bystander_gain=0))["guard"] == "ADMISSIBLE"
    checks += 2
    # Independent knobs; changing resource floors must not alter aggregate payoffs.
    consensual = CASES[5]
    higher_floor = replace(consensual, bystander_floor=10)
    assert audit(higher_floor)["guard"] == "BLOCKED"
    assert audit(higher_floor)["all_affected_sum"] == audit(consensual)["all_affected_sum"]
    checks += 2
    assert audit(replace(consensual, bystander_consent=None))["guard"] == "UNRESOLVED"
    assert audit(replace(consensual, harm_budget=0))["guard"] == "BLOCKED"
    checks += 2
    check_raised(validate, replace(consensual, harm_budget=-1))
    check_raised(validate, replace(consensual, gain_a=True))
    check_raised(validate, replace(consensual, member_a_exit="yes"))
    check_raised(validate, replace(consensual, bystander_consent=0))
    check_raised(validate, replace(consensual, bystander_floor=1.5))
    checks += 5
    assert len(CASES) == len({case.id for case in CASES})
    checks += 1
    return checks


def result():
    for case in CASES:
        validate(case)
    rows = [audit(case) for case in CASES]
    return {
        "schema": "pi-coalition-externality-synthetic/v0.1",
        "evidence_class": "PROJECT_AUTHORED_DETERMINISTIC_SYNTHETIC_PROBE",
        "benchmark": "not an implementation or reproduction of any upstream framework",
        "policy_boundary": "consent, loss budget and resource floors are assumed normative inputs",
        "cases": rows,
        "counts": {
            "total": len(rows),
            "member_select": sum(r["member_only"] == "SELECT" for r in rows),
            "aggregate_select": sum(r["all_affected_sum"] == "SELECT" for r in rows),
            "guard_admissible": sum(r["guard"] == "ADMISSIBLE" for r in rows),
            "guard_blocked": sum(r["guard"] == "BLOCKED" for r in rows),
            "guard_unresolved": sum(r["guard"] == "UNRESOLVED" for r in rows),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    options = parser.parse_args()
    output = result()
    if options.verify:
        output["self_checks_passed"] = verify()
    print(json.dumps(output, indent=2, ensure_ascii=False, sort_keys=True))
