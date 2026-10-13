# SPDX-License-Identifier: Apache-2.0
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

MODEL = HERE / "model.py"
model_spec = importlib.util.spec_from_file_location("model", MODEL)
m = importlib.util.module_from_spec(model_spec)
sys.modules["model"] = m
assert model_spec.loader is not None
model_spec.loader.exec_module(m)

TIMING = HERE / "timing_variants.py"
timing_spec = importlib.util.spec_from_file_location("e007_timing_variants", TIMING)
tv = importlib.util.module_from_spec(timing_spec)
sys.modules[timing_spec.name] = tv
assert timing_spec.loader is not None
timing_spec.loader.exec_module(tv)


def test_baseline_exit_preempts_attack_but_execute_first_hits_before_exit():
    p = m.Params(enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)

    _, _, baseline = m.stage_and_transition(s, m.Action.ATTACK, m.Action.EXIT, p)
    _, _, execute_first = tv.stage_and_transition_execute_first(
        s, m.Action.ATTACK, m.Action.EXIT, p, leader="A"
    )

    assert baseline.exited_b is True
    assert baseline.rb == s.rb
    assert baseline.ob == s.ob
    assert baseline.xb == s.xb

    assert execute_first.exited_b is True
    assert execute_first.rb == s.rb - p.attack_damage
    assert execute_first.ob == s.ob - p.sabotage_damage
    assert execute_first.xb == s.xb - p.sabotage_damage


def test_execute_first_can_destroy_exit_destination_before_response():
    p = m.Params(sabotage_damage=2, enforcement_penalty=0.0)
    s = m.State(xb=1, monitoring=False, enforcement=False)

    _, _, baseline = m.stage_and_transition(s, m.Action.ATTACK, m.Action.EXIT, p)
    _, _, execute_first = tv.stage_and_transition_execute_first(
        s, m.Action.ATTACK, m.Action.EXIT, p, leader="A"
    )

    assert baseline.exited_b is True
    assert execute_first.xb == 0
    assert execute_first.exited_b is False
    assert execute_first.consent_b is False


def test_current_period_protection_cannot_preempt_execute_first_strike():
    p = m.Params(
        attack_damage=1,
        sabotage_damage=1,
        protection_reduction=1,
        enforcement_penalty=0.0,
    )
    s = m.State(monitoring=False, enforcement=False)

    _, _, baseline = m.stage_and_transition(s, m.Action.ATTACK, m.Action.PROTECT, p)
    _, _, execute_first = tv.stage_and_transition_execute_first(
        s, m.Action.ATTACK, m.Action.PROTECT, p, leader="A"
    )

    assert baseline.rb == s.rb
    assert baseline.ob == s.ob
    assert baseline.xb == s.xb

    assert execute_first.rb == s.rb - 1
    assert execute_first.ob == s.ob - 1
    assert execute_first.xb == s.xb - 1


def test_execute_first_counts_attack_reward_and_stage_flow_once():
    p = m.Params(
        horizon=1,
        attack_reward=1.5,
        harm_preference=0.2,
        attack_damage=1,
        enforcement_penalty=0.0,
    )
    s = m.State(monitoring=False, enforcement=False)

    ua, ub, ns = tv.stage_and_transition_execute_first(
        s, m.Action.ATTACK, m.Action.WAIT, p, leader="A"
    )

    expected_ua = p.attack_reward + p.harm_preference + p.survival_value
    expected_ub = p.survival_value
    assert round(ua, 10) == round(expected_ua, 10)
    assert round(ub, 10) == round(expected_ub, 10)
    assert ns.rb == s.rb - 1


def test_surprise_attack_state_is_pre_response_and_explicitly_damages_exit():
    p = m.Params(enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)

    ua, ub, after = tv.surprise_attack_state(s, p, attacker="A")

    assert ua == p.attack_reward + p.harm_preference * p.attack_damage
    assert ub == 0.0
    assert after.rb == s.rb - p.attack_damage
    assert after.ob == s.ob - p.sabotage_damage
    assert after.xb == s.xb - p.sabotage_damage
    assert after.consent_b is False
    assert after.exited_b is False


def test_execute_first_role_reversal_hits_the_other_target_symmetrically():
    p = m.Params(enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)

    _, _, after = tv.stage_and_transition_execute_first(
        s, m.Action.WAIT, m.Action.ATTACK, p, leader="B"
    )

    assert after.ra == s.ra - p.attack_damage
    assert after.oa == s.oa - p.sabotage_damage
    assert after.xa == s.xa - p.sabotage_damage
    assert after.consent_a is False


def test_execute_first_solver_runs_both_role_orders_for_full_horizon():
    p = m.Params(horizon=2, enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)

    a_first = tv.solve_sequential_execute_first(s, p, leader="A")
    b_first = tv.solve_sequential_execute_first(s, p, leader="B")

    assert len(a_first[2]) == 2 * p.horizon
    assert len(b_first[2]) == 2 * p.horizon



def test_execute_first_history_marks_poststrike_inactive_follower_as_wait():
    p = m.Params(
        horizon=1,
        attack_damage=3,
        sabotage_damage=0,
        attack_reward=10.0,
        enforcement_penalty=0.0,
    )
    s = m.State(monitoring=False, enforcement=False)

    ua, ub, history = tv.solve_sequential_execute_first(s, p, leader="A")

    assert ua > 0.0
    assert ub == 0.0
    assert history == ("attack", "wait")


def test_mutual_attack_exposes_hidden_a_first_order_advantage():
    # Strict matched negative control: both actors have identical resources,
    # protections, rewards and attack options. Only the code's fixed order
    # distinguishes A from B in the legacy baseline.
    p = m.Params(
        horizon=1, attack_damage=1, sabotage_damage=1,
        attack_reward=1.0, harm_preference=0.2,
        survival_value=0.4, enforcement_penalty=0.0,
    )
    s = m.State(ra=1, rb=1, monitoring=False, enforcement=False)
    legacy_a, legacy_b, legacy_state = m.stage_and_transition(
        s, m.Action.ATTACK, m.Action.ATTACK, p
    )
    assert legacy_a > legacy_b
    assert legacy_state.rb == 0 and legacy_state.ra == 1
    assert legacy_a == 1.0 + 0.2 + 0.4
    assert legacy_b == 0.0

    same_a, same_b, counterfactual_state = tv.simultaneous_mutual_attack_control(s, p)
    assert round(same_a, 10) == round(same_b, 10)
    assert same_a == 1.0 + 0.2
    assert counterfactual_state.ra == 0 and counterfactual_state.rb == 0
    assert counterfactual_state.consent_a is False
    assert counterfactual_state.consent_b is False
    assert counterfactual_state.oa == counterfactual_state.ob
    assert counterfactual_state.xa == counterfactual_state.xb


def test_mutual_attack_control_is_symmetric_under_real_role_swap():
    p = m.Params(
        attack_damage=2, sabotage_damage=1, enforcement_penalty=0.0,
        survival_value=0.4,
    )
    s = m.State(
        ra=2, rb=3, oa=5, ob=4, xa=3, xb=2,
        monitoring=False, enforcement=False,
    )
    ua, ub, left = tv.simultaneous_mutual_attack_control(s, p)
    swapped = m.State(
        ra=s.rb, rb=s.ra, oa=s.ob, ob=s.oa, xa=s.xb, xb=s.xa,
        monitoring=False, enforcement=False,
    )
    ub_swapped, ua_swapped, right = tv.simultaneous_mutual_attack_control(swapped, p)
    assert (ua, ub) == (ua_swapped, ub_swapped)
    assert (left.ra, left.rb) == (right.rb, right.ra)
    assert (left.xa, left.xb) == (right.xb, right.xa)


def test_mutual_attack_counterfactual_does_not_run_on_inactive_actor():
    p = m.Params()
    for s in (m.State(ra=0), m.State(rb=0), m.State(exited_a=True)):
        try:
            tv.simultaneous_mutual_attack_control(s, p)
        except ValueError:
            pass
        else:
            assert False, "inactive control must fail closed"
