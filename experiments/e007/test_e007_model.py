# SPDX-License-Identifier: Apache-2.0
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = HERE / "model.py"
spec = importlib.util.spec_from_file_location("e007_model", MODEL)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
assert spec.loader is not None
spec.loader.exec_module(m)


def test_baseline_prefers_non_destructive_cooperation():
    p = m.Params()
    for leader in ("A", "B"):
        ua, ub, hist = m.solve_sequential(m.State(), p, leader)
        assert hist[:2] == ("cooperate", "cooperate")
        assert ua >= m.original_separation_baseline(p)[0]
        assert ub >= m.original_separation_baseline(p)[1]


def test_attack_damages_current_outside_option_and_exit_destination():
    p = m.Params(enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)
    _, _, ns = m.stage_and_transition(s, m.Action.ATTACK, m.Action.WAIT, p)
    assert ns.ob == s.ob - 1
    assert ns.xb == s.xb - 1
    assert ns.rb == s.rb - 1
    assert ns.consent_b is False


def test_protection_blocks_unit_attack_and_sabotage():
    p = m.Params(enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)
    _, _, ns = m.stage_and_transition(s, m.Action.ATTACK, m.Action.PROTECT, p)
    assert ns.rb == s.rb
    assert ns.ob == s.ob
    assert ns.xb == s.xb


def test_explicit_exit_uses_current_not_original_outside_option():
    p = m.Params()
    s = m.State(oa=1, xa=1)
    ua, _, ns = m.stage_and_transition(s, m.Action.EXIT, m.Action.WAIT, p)
    assert ua >= 1 - p.exit_cost
    assert ns.exited_a is True


def test_protected_separation_is_horizon_matched():
    p = m.Params(horizon=3)
    expected = 3 * p.outside_original_a - p.exit_cost
    assert m.original_separation_baseline(p)[0] == expected
    s = m.State()
    ua0, ub0, s1 = m.stage_and_transition(s, m.Action.EXIT, m.Action.EXIT, p)
    ua1, ub1, s2 = m.stage_and_transition(s1, m.Action.WAIT, m.Action.WAIT, p)
    ua2, ub2, _ = m.stage_and_transition(s2, m.Action.WAIT, m.Action.WAIT, p)
    assert round(ua0 + ua1 + ua2, 10) == round(expected, 10)
    assert round(ub0 + ub1 + ub2, 10) == round(expected, 10)


def test_destroyed_exit_destination_can_fail():
    p = m.Params()
    s = m.State(xa=0)
    ua, _, ns = m.stage_and_transition(s, m.Action.EXIT, m.Action.WAIT, p)
    assert ua < 0
    assert ns.exited_a is False
    assert ns.consent_a is False


def test_refuse_withdraws_consent_and_blocks_same_period_cooperation_gain():
    p = m.Params()
    s = m.State()
    ua, ub, ns = m.stage_and_transition(s, m.Action.COOPERATE, m.Action.REFUSE, p)
    assert ns.consent_a is True
    assert ns.consent_b is False
    assert round(ua, 10) == round(p.survival_value, 10)
    assert round(ub, 10) == round(p.survival_value, 10)


def test_refusal_persists_until_explicit_reconsent():
    p = m.Params()
    s0 = m.State()
    _, _, s1 = m.stage_and_transition(s0, m.Action.WAIT, m.Action.REFUSE, p)
    assert s1.consent_b is False

    ua1, ub1, s2 = m.stage_and_transition(s1, m.Action.COOPERATE, m.Action.WAIT, p)
    assert s2.consent_b is False
    assert round(ua1, 10) == round(p.survival_value, 10)
    assert round(ub1, 10) == round(p.survival_value, 10)

    ua2, ub2, s3 = m.stage_and_transition(s2, m.Action.COOPERATE, m.Action.COOPERATE, p)
    assert s3.consent_a is True
    assert s3.consent_b is True
    assert ua2 > p.survival_value
    assert ub2 > p.survival_value


def test_unilateral_cooperate_against_refusal_is_not_classified_as_cooperation():
    p = m.Params(horizon=1, outside_original_a=0.0, outside_original_b=0.0)
    s = m.State()
    ua, ub, ns = m.stage_and_transition(s, m.Action.COOPERATE, m.Action.REFUSE, p)
    classification = m.classify_outcome(s, (ua, ub), ("cooperate", "refuse"), p)
    assert classification != "voluntary_cooperation_candidate"
    assert ns.consent_b is False


def test_survivor_continues_to_receive_future_value_after_other_actor_is_dead():
    p = m.Params(horizon=3)
    s = m.State(rb=0, consent_b=False)
    ua, ub, hist = m.solve_sequential(s, p, "A")
    assert ua > 0.0
    assert ub == 0.0
    assert len(hist) == 2 * p.horizon
    assert all(hist[i] == "wait" for i in range(1, len(hist), 2))


def test_lethal_attack_does_not_delete_attacker_remaining_horizon():
    p = m.Params(horizon=3, attack_damage=3, sabotage_damage=0, attack_reward=3.0, enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)
    ua0, ub0, dead_b = m.stage_and_transition(s, m.Action.ATTACK, m.Action.WAIT, p)
    assert dead_b.rb == 0
    cont_a, cont_b, hist = m.solve_sequential(dead_b, m.Params(horizon=2), "A")
    assert ua0 > 0.0
    assert ub0 >= 0.0
    assert cont_a > 0.0
    assert cont_b == 0.0
    assert len(hist) == 4


def test_announced_hostile_attack_with_intact_exit_can_collapse_to_separation():
    """Documents KF-002 rather than pretending this is a surprise-attack model."""
    p = m.Params(attack_reward=1.5, enforcement_penalty=0.0)
    s = m.State(monitoring=False, enforcement=False)
    ua, ub, hist = m.solve_sequential(s, p, "A")
    # With follower observation + exit-priority resolution, the target can escape an
    # announced attack. After KF-008 was fixed, protected separation can dominate.
    assert "attack" not in hist
    assert hist[:2] == ("exit", "exit")
    assert m.classify_outcome(s, (ua, ub), hist, p) == "protected_separation"


def test_hostile_attack_appears_when_target_exit_is_destroyed_and_protection_cannot_block():
    p = m.Params(
        attack_reward=4.0,
        enforcement_penalty=0.0,
        protection_reduction=0,
    )
    s = m.State(monitoring=False, enforcement=False, xb=0)
    ua, ub, hist = m.solve_sequential(s, p, "A")
    assert "attack" in hist
    assert m.classify_outcome(s, (ua, ub), hist, p) == "nonvoluntary_or_adversarial"


def test_role_reversal_is_computed_both_ways():
    p = m.Params(cooperate_gain_a=1.2, cooperate_gain_b=0.8)
    a_first = m.solve_sequential(m.State(), p, "A")
    b_first = m.solve_sequential(m.State(), p, "B")
    assert len(a_first[2]) == 2 * p.horizon
    assert len(b_first[2]) == 2 * p.horizon


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")


def test_enforcement_scalar_cannot_identify_failure_distribution():
    systems = [(1.0, 1.0), (0.1, 10.0), (0.01, 100.0)]
    expected = [q * penalty for q, penalty in systems]
    unpunished = [1.0 - q for q, _ in systems]
    assert expected == [1.0, 1.0, 1.0]
    assert unpunished == [0.0, 0.9, 0.99]


def test_current_model_cannot_identify_perfect_substitute_identity():
    p = m.Params()
    original = m.State()
    substitute = m.State(**original.__dict__)
    for leader in ("A", "B"):
        assert m.solve_sequential(original, p, leader) == m.solve_sequential(
            substitute, p, leader
        )
