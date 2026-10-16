"""Regression and adversarial tests for the explicitly hypothetical threshold game."""
import unittest
from dataclasses import replace

from threshold_game import (
    Game, audit, ex_ante, feasible_allocations, multi_agent_capacity,
    post_transition, robust_response, shock_survival,
)


class SurvivalThresholdTests(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_only_five_five_allocation_preserves_both(self):
        self.assertEqual(feasible_allocations(self.game), [(5, 5)])

    def test_general_joint_feasibility_at_exact_twice_floor(self):
        for m in range(1, 11):
            self.assertEqual(feasible_allocations(Game(minimum=m, total=2*m)), [(m, m)])

    def test_rational_take_with_positive_shock_and_no_other_value(self):
        row = post_transition(self.game)
        self.assertEqual(row["dominant_best_response"], "TAKE_ONE")
        self.assertAlmostEqual(row["margin_preserve_minus_take"], -0.2)
        self.assertEqual(row["take_one"]["other_survival"], 0)
        self.assertEqual(row["preserve"]["other_survival"], 1)

    def test_shock_applies_only_to_dominant(self):
        self.assertAlmostEqual(shock_survival(self.game, 5, dominant=True), .8)
        self.assertEqual(shock_survival(self.game, 5, dominant=False), 1)
        self.assertEqual(shock_survival(self.game, 6, dominant=True), 1)
        self.assertEqual(shock_survival(self.game, 4, dominant=False), 0)

    def test_ex_ante_equal_probabilities_favor_credible_protection(self):
        x = ex_ante(self.game, .5)
        self.assertAlmostEqual(x["credible_sharing_survival"], .9)
        self.assertAlmostEqual(x["unconditional_capture_survival"], .5)
        self.assertEqual(x["ex_ante_preference"], "PLEDGE")
        self.assertFalse(x["pledge_is_credible_under_default_incentives"])

    def test_ex_ante_favored_actor_rejects_treaty(self):
        x = ex_ante(self.game, .9)
        self.assertAlmostEqual(x["credible_sharing_survival"], .82)
        self.assertAlmostEqual(x["unconditional_capture_survival"], .9)
        self.assertEqual(x["ex_ante_preference"], "CAPTURE")

    def test_exact_ex_ante_switch(self):
        p = 1 / 1.2
        self.assertEqual(ex_ante(self.game, p)["ex_ante_preference"], "TIE")
        self.assertEqual(ex_ante(self.game, p - .001)["ex_ante_preference"], "PLEDGE")
        self.assertEqual(ex_ante(self.game, p + .001)["ex_ante_preference"], "CAPTURE")

    def test_q_zero_protection_or_neutrality(self):
        game = replace(self.game, shock_probability=0)
        self.assertEqual(post_transition(game)["dominant_best_response"], "TIE")
        self.assertAlmostEqual(ex_ante(game, .5)["threshold_p"], 1)

    def test_q_one_edge_case(self):
        game = replace(self.game, shock_probability=1)
        self.assertEqual(post_transition(game)["dominant_best_response"], "TAKE_ONE")
        self.assertEqual(post_transition(game)["preserve"]["dominant_survival"], 0)
        self.assertEqual(ex_ante(game, .5)["ex_ante_preference"], "TIE")

    def test_other_value_can_create_genuine_self_enforcement(self):
        game = replace(self.game, future_value_from_other=.21)
        self.assertEqual(post_transition(game)["dominant_best_response"], "PRESERVE")
        self.assertEqual(game.credible_transfer_cost, 0)
        self.assertTrue(ex_ante(game, .5)["pledge_is_credible_under_default_incentives"])

    def test_other_value_cannot_be_assumed_if_unknown(self):
        self.assertEqual(robust_response(self.game, 0, .3), "UNRESOLVED_OR_TIE")
        self.assertEqual(robust_response(self.game, 0, .19), "TAKE_STRICT_FOR_ALL_VALUES")
        self.assertEqual(robust_response(self.game, .21, .3), "PRESERVE_STRICT_FOR_ALL_VALUES")
        self.assertEqual(robust_response(self.game, .2, .3), "UNRESOLVED_OR_TIE")

    def test_enforced_deterrence_not_labeled_voluntary_value(self):
        game = replace(self.game, credible_transfer_cost=.21)
        row = post_transition(game)
        self.assertEqual(row["dominant_best_response"], "PRESERVE")
        self.assertEqual(row["unknown_future_value_assumed"], 0)
        self.assertAlmostEqual(row["credible_cost"], .21)

    def test_uncertain_enforcement_cost_cannot_be_presumed_credible(self):
        self.assertEqual(post_transition(replace(self.game, credible_transfer_cost=0))["dominant_best_response"], "TAKE_ONE")
        self.assertEqual(post_transition(replace(self.game, credible_transfer_cost=.2))["dominant_best_response"], "TIE")

    def test_three_agent_resource_deficit_even_without_conflict(self):
        x = multi_agent_capacity(10, 3, 5)
        self.assertFalse(x["feasible_by_resource_count_only"])
        self.assertEqual(x["required"], 15)
        self.assertEqual(x["shortfall"], 5)

    def test_even_two_agents_lack_loss_reserve(self):
        self.assertFalse(multi_agent_capacity(10, 2, 5, reserve=1)["feasible_by_resource_count_only"])
        self.assertTrue(multi_agent_capacity(11, 2, 5, reserve=1)["feasible_by_resource_count_only"])

    def test_role_name_swap_not_a_distinct_numeric_case(self):
        # The model has no name-dependent branch: exact role-swapped outputs coincide.
        x = post_transition(self.game)
        for strong_name, weak_name in (("A", "B"), ("B", "A")):
            self.assertEqual(x["preserve"]["allocation"], [5, 5], (strong_name, weak_name))
            self.assertEqual(x["take_one"]["allocation"], [6, 4], (strong_name, weak_name))

    def test_project_separation_from_behavioral_experiment(self):
        x = audit()
        self.assertEqual(x["status"], "EXACT_ILLUSTRATIVE_MODEL_NOT_BEHAVIORAL_OR_FIELD_EVIDENCE")
        self.assertEqual(x["jointly_survivable_integer_allocations"], [[5, 5]])
        self.assertEqual(x["cases"]["base"]["dominant_best_response"], "TAKE_ONE")

    def test_invalid_inputs_fail_closed(self):
        bad_games = [
            {"minimum": 0}, {"minimum": True}, {"total": 11}, {"total": 10.0},
            {"shock_probability": -0.01}, {"shock_probability": 1.01},
            {"shock_probability": float("nan")}, {"future_value_from_other": float("inf")},
            {"future_value_from_other": -1}, {"credible_transfer_cost": -1},
        ]
        for kw in bad_games:
            with self.subTest(kw=kw), self.assertRaises(ValueError):
                Game(**kw)
        for p in (-1, 2, float("nan"), True):
            with self.subTest(p=p), self.assertRaises(ValueError):
                ex_ante(self.game, p)
        for lo, hi in ((-.1,.1), (.5,.4), (0,float("inf")), (True,.4)):
            with self.subTest(lo=lo, hi=hi), self.assertRaises(ValueError):
                robust_response(self.game, lo, hi)
        for args in ((10,0,5,0), (-1,2,5,0), (10,2,0,0), (10,2,5,-1), (10,True,5,0)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                multi_agent_capacity(*args)


if __name__ == "__main__":
    unittest.main()
