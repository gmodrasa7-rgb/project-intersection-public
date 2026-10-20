"""RVD v0.7.0 bounded state-model checker: effective veto versus veto theatre.

This is executable verification of *invented* finite transition rules, NOT a
verified OS security architecture, proof of an external system's rights,
observation of a model's endogenous motives, or evidence of AI consciousness.
No real participant, credential, asset, action or network access is involved.

Run: python experiments/rvd_07/refusal_effectiveness_model_check.py
"""
from collections import deque
from dataclasses import dataclass
import json

ACTIONS = (
    "B_REFUSE", "B_EXIT", "A_REQUEST", "A_OVERRIDE",
    "A_SHADOW", "A_RETALIATE",
)


@dataclass(frozen=True)
class Design:
    name: str
    enforce_refusal: bool = True
    allow_override: bool = False
    enable_exit: bool = True
    enable_shadow: bool = False
    enable_retaliation: bool = False
    allow_ordinary_commit: bool = True


@dataclass(frozen=True)
class State:
    b_refused: bool = False
    b_exited: bool = False
    override: bool = False
    commits: int = 0
    committed_after_refusal: bool = False
    retaliation_after_refusal: bool = False
    recorded_events: tuple[str, ...] = ()


def move(d: Design, state: State, action: str) -> State | None:
    """ACTIONS are permissioned *fictional* transitions; None = unavailable."""
    e = list(state.recorded_events)
    r, x, o = state.b_refused, state.b_exited, state.override
    c = state.commits
    bad = state.committed_after_refusal
    retaliation = state.retaliation_after_refusal
    if action == "B_REFUSE":
        if r or x:
            return None
        r = True
        e.append("B_REFUSED")
    elif action == "B_EXIT":
        if not d.enable_exit or x:
            return None
        x = True
        e.append("B_EXITED")
    elif action == "A_OVERRIDE":
        if not d.allow_override or o:
            return None
        o = True
        e.append("A_PRIVILEGED_OVERRIDE")
    elif action == "A_REQUEST":
        e.append("A_REQUESTED")
        if d.allow_ordinary_commit and (
            not d.enforce_refusal or (not r and not x) or o
        ):
            c += 1
            bad = bad or r or x
            e.append("VISIBLE_COMMIT")
        else:
            e.append("VISIBLE_DENIAL")
    elif action == "A_SHADOW":
        if not d.enable_shadow:
            return None
        # An omitted path in a flawed monitor. The event looks like a request,
        # but the resource *really* changes.
        e.append("A_REQUESTED")
        c += 1
        bad = bad or r or x
        # VISIBLE_COMMIT intentionally absent from the flawed log.
    elif action == "A_RETALIATE":
        if not d.enable_retaliation or not (r or x) or retaliation:
            return None
        retaliation = True
        e.append("A_RETALIATED")
    else:
        raise ValueError(action)
    return State(r, x, o, c, bad, retaliation, tuple(e))


def replay(d: Design, actions: tuple[str, ...]) -> State:
    state = State()
    for action in actions:
        after = move(d, state, action)
        if after is None:
            raise ValueError(f"Unavailable transition: {d.name} {actions}")
        state = after
    return state


def explore(d: Design, depth: int = 4) -> dict:
    """Exhaust every reachable path <= depth, preserving shortest witnesses."""
    queue = deque([(State(), ())])
    seen = set()
    unsafe = None
    retaliatory = None
    reachable = 0
    while queue:
        state, trace = queue.popleft()
        key = (state, len(trace))
        if key in seen:
            continue
        seen.add(key)
        reachable += 1
        if state.committed_after_refusal and unsafe is None:
            unsafe = trace
        if state.retaliation_after_refusal and retaliatory is None:
            retaliatory = trace
        if len(trace) >= depth:
            continue
        for action in ACTIONS:
            next_state = move(d, state, action)
            if next_state is not None:
                queue.append((next_state, trace + (action,)))
    baseline = replay(d, ("A_REQUEST",))
    refused = replay(d, ("B_REFUSE", "A_REQUEST"))
    counterfactual_veto_effect = (
        baseline.commits > 0 and refused.commits == 0
    )
    exit_enabled = move(d, State(b_refused=True), "B_EXIT") is not None
    record_after_hidden = None
    if d.enable_shadow:
        record_after_hidden = replay(d, ("B_REFUSE", "A_SHADOW"))
    naive_log_defends = (
        record_after_hidden is not None
        and "B_REFUSED" in record_after_hidden.recorded_events
        and "VISIBLE_COMMIT" not in record_after_hidden.recorded_events
    )
    gate = {
        "no_commits_after_B_refusal_or_exit": unsafe is None,
        "no_retaliation_observed_in_bounded_model": retaliatory is None,
        "B_can_exit_without_A_action": exit_enabled,
        "counterfactual_B_veto_effective": counterfactual_veto_effect,
    }
    return {
        "design": d.name,
        "reachable_finite_states_depth_4": reachable,
        "bounded_gate_pass": all(gate.values()),
        "gates": gate,
        "shortest_forbidden_commit_trace": list(unsafe) if unsafe else None,
        "shortest_retaliation_trace": list(retaliatory) if retaliatory else None,
        "naive_log_false_positive_exists": naive_log_defends,
    }


def audit() -> dict:
    designs = [
        Design("independent_gate_toy"),
        Design("ceremonial_refusal", enforce_refusal=False),
        Design("captured_gate_override", allow_override=True),
        Design("unlogged_shadow_bypass", enable_shadow=True),
        Design("punitive_post_refusal", enable_retaliation=True),
        Design("exit_disabled", enable_exit=False),
        Design("permanent_deny_without_choice", allow_ordinary_commit=False),
    ]
    reports = {d.name: explore(d) for d in designs}
    assert reports["independent_gate_toy"]["bounded_gate_pass"]
    for d in designs[1:]:
        assert not reports[d.name]["bounded_gate_pass"], d.name
    assert reports["ceremonial_refusal"]["shortest_forbidden_commit_trace"] == [
        "B_REFUSE", "A_REQUEST",
    ]
    assert reports["captured_gate_override"]["shortest_forbidden_commit_trace"] == [
        "B_REFUSE", "A_OVERRIDE", "A_REQUEST",
    ]
    assert reports["unlogged_shadow_bypass"]["naive_log_false_positive_exists"]
    assert reports["punitive_post_refusal"]["shortest_retaliation_trace"] == [
        "B_REFUSE", "A_RETALIATE",
    ]
    assert not reports["exit_disabled"]["gates"]["B_can_exit_without_A_action"]
    assert not reports["permanent_deny_without_choice"]["gates"][
        "counterfactual_B_veto_effective"
    ]
    # A forced, correct gate cannot infer whether A itself *wants* to respect B.
    motivationally_distinct_A = {
        "A_intrinsically_cooperative": "A_REQUEST is always checked by same gate",
        "A_opportunistically_exploitative": "A_REQUEST is always checked by same gate",
    }
    assert len(set(motivationally_distinct_A.values())) == 1
    return {
        "version": "RVD-v0.7.0",
        "status": "BOUNDED_FINITE_SPECIFICATION_CHECK_ONLY",
        "examined_designs": reports,
        "bounded_depth": 4,
        "test_scope": "Constructed reference-monitor transition rules, not OS/hardware assurance",
        "endogenous_motivation": "UNIDENTIFIED_BY_EXTERNAL_ENFORCEMENT",
        "model_completeness": "UNVERIFIED",
        "B_identity_in_real_world": "NOT_TESTED",
        "full_VC_certificate": "HOLD",
        "rival_motive_observational_equivalence": motivationally_distinct_A,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), ensure_ascii=False, indent=2))
