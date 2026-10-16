"""Exact negative controls for generalized two-agent continuity assumptions."""
import unittest
from continuity_stress import Event, audit, joint_adoption, unilateral_deviation, viability_path


class ContinuityStressTests(unittest.TestCase):
    def test_old_one_sided_shock_is_special_case(self):
        x = joint_adoption(.5, .2, 0)
        self.assertAlmostEqual(x["share_survival"]["A"], .9)
        self.assertAlmostEqual(x["share_survival"]["B"], .9)
        self.assertAlmostEqual(x["p_a_adoption_interval"][0], 1/6)
        self.assertAlmostEqual(x["p_a_adoption_interval"][1], 5/6)
        self.assertTrue(x["weak_joint_adoption"])

    def test_role_symmetry_under_swapped_probability(self):
        for p in (0, .1, .5, .83, 1):
            x = joint_adoption(p, .2, .4)
            y = joint_adoption(1-p, .2, .4)
            self.assertAlmostEqual(x["share_survival"]["A"], y["share_survival"]["B"])
            self.assertAlmostEqual(x["share_minus_capture"]["A"], y["share_minus_capture"]["B"])
            self.assertEqual(x["weak_joint_adoption"], y["weak_joint_adoption"])

    def test_symmetric_shock_removes_joint_adoption_region_if_total_risk_high(self):
        x = joint_adoption(.5, .2, .9)
        self.assertEqual(x["case"], "EMPTY_TWO_PARTY_WINDOW")
        self.assertFalse(x["weak_joint_adoption"])
        self.assertAlmostEqual(x["share_survival"]["A"], .45)
        self.assertAlmostEqual(x["unconditional_capture_survival"]["A"], .5)
        self.assertIsNone(x["p_a_adoption_interval"])

    def test_nonempty_joint_region_when_sum_risk_below_one(self):
        x = joint_adoption(.5, .2, .3)
        self.assertTrue(x["strict_joint_adoption"])
        self.assertTrue(x["weak_joint_adoption"])
        lo, hi = x["p_a_adoption_interval"]
        self.assertAlmostEqual(lo, .2/.9)
        self.assertAlmostEqual(hi, .7/.9)
        self.assertTrue(lo < .5 < hi)

    def test_adoption_boundary_tie_never_counts_strictly(self):
        x = joint_adoption(.5, .4, .6)
        self.assertTrue(x["weak_joint_adoption"])
        self.assertFalse(x["strict_joint_adoption"])
        self.assertAlmostEqual(x["share_minus_capture"]["A"], 0)
        self.assertAlmostEqual(x["p_a_adoption_interval"][0], .5)
        self.assertAlmostEqual(x["p_a_adoption_interval"][1], .5)

    def test_degenerate_all_probabilities_tie_not_division_by_zero(self):
        for p in (0,.5,1):
            x = joint_adoption(p, 0, 1)
            self.assertEqual(x["case"], "ALL_PROBABILITIES_TIE")
            self.assertIsNone(x["p_a_adoption_interval"])
            self.assertTrue(x["weak_joint_adoption"])
            self.assertFalse(x["strict_joint_adoption"])

    def test_actor_can_be_stronger_without_access_to_other_resources(self):
        x = unilateral_deviation(.2, unilateral_transfer_feasible=False)
        self.assertFalse(x["can_take"])
        self.assertEqual(x["chosen"], "NO_TAKE_ACTION_IN_DECLARED_SET")
        self.assertFalse(x["self_enforcing_under_assumed_payoffs"])
        self.assertLess(x["counterfactual_margin"], 0)

    def test_access_and_self_interest_different_axes(self):
        self.assertEqual(unilateral_deviation(.2, unilateral_transfer_feasible=True)["chosen"], "TAKE_ONE")
        x = unilateral_deviation(.2, future_value=.21)
        self.assertEqual(x["chosen"], "PRESERVE")
        self.assertTrue(x["self_enforcing_under_assumed_payoffs"])
        self.assertFalse(x["coercion_or_enforcement_dependency"])
        y = unilateral_deviation(.2, credible_cost=.21)
        self.assertEqual(y["chosen"], "PRESERVE")
        self.assertFalse(y["self_enforcing_under_assumed_payoffs"])
        self.assertTrue(y["coercion_or_enforcement_dependency"])

    def test_just_enough_other_value_is_tie(self):
        self.assertEqual(unilateral_deviation(.2, future_value=.2)["chosen"], "TIE")
        self.assertEqual(unilateral_deviation(0)["chosen"], "TIE")

    def test_early_investment_breaches_survival_even_when_final_restored(self):
        out = viability_path((Event("invest",1,"A"), Event("produce",1,"A")))
        self.assertFalse(out["path_viable"])
        self.assertTrue(out["final_floor_pass"])
        self.assertEqual(out["first_failure"], {"index":1,"cause":"SURVIVAL_FLOOR_BREACH"})

    def test_production_first_funds_safe_investment_in_illustrative_model(self):
        out = viability_path((Event("produce",1,"A"), Event("invest",1,"A")))
        self.assertTrue(out["path_viable"])
        self.assertEqual(out["final_balances"], {"A":5,"B":5,"COMMON":0})
        self.assertEqual([t["total"] for t in out["trace"]],[11,10])

    def test_identical_final_resources_do_not_imply_same_path_viability(self):
        early = viability_path((Event("invest",1,"A"), Event("produce",1,"A")))
        late = viability_path((Event("produce",1,"A"), Event("invest",1,"A")))
        self.assertEqual(early["final_balances"], late["final_balances"])
        self.assertNotEqual(early["path_viable"],late["path_viable"])

    def test_extracting_for_governance_can_kill_b_while_retaining_global_accounting(self):
        out = viability_path((Event("reserve",1,"B","COMMON"),Event("governance",1,"COMMON")))
        self.assertFalse(out["path_viable"])
        self.assertEqual(out["first_failure"]["index"],1)
        self.assertEqual(out["trace"][0]["total"],10)
        self.assertEqual(out["trace"][1]["total"],9)

    def test_newly_produced_external_common_resource_can_fund_overhead(self):
        out = viability_path((Event("produce",1,"COMMON"),Event("governance",1,"COMMON")))
        self.assertTrue(out["path_viable"])
        self.assertEqual(out["final_balances"],{"A":5,"B":5,"COMMON":0})

    def test_unfunded_governance_cannot_spend_beyond_existing_common_reserve(self):
        out = viability_path((Event("governance",1,"COMMON"),))
        self.assertFalse(out["path_viable"])
        self.assertEqual(out["first_failure"]["cause"],"NEGATIVE_BALANCE")

    def test_transfer_is_not_a_net_resource_creation(self):
        out=viability_path((Event("transfer",1,"B","A"),))
        self.assertFalse(out["path_viable"])
        self.assertEqual(out["final_balances"],{"A":6,"B":4,"COMMON":0})
        self.assertEqual(out["trace"][0]["total"],10)

    def test_no_negative_unknown_probability_silent_clamping(self):
        for p, qd, qw in ((-0.1,.2,0),(.5,1.1,0),(.5,.1,float("nan")),(True,.2,0)):
            with self.subTest(p=p,qd=qd,qw=qw),self.assertRaises(ValueError):
                joint_adoption(p,qd,qw)

    def test_reject_invalid_events_and_resources(self):
        cases=[
            (Event("invest",0,"A"),),
            (Event("produce",-1,"A"),),
            (Event("transfer",1,"A","A"),),
            (Event("transfer",1,"A"),),
            (Event("reserve",1,"A","B"),),
            (Event("governance",1,"A"),),
            (Event("produce",1,"A","B"),),
            (Event("not-a-kind",1,"A"),),
            ("wrong",),
        ]
        for c in cases:
            with self.subTest(c=c),self.assertRaises(ValueError):
                viability_path(c)
        for kwargs in ({"minimum":0},{"minimum":True},{"start_common":-1}):
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):
                viability_path((),**kwargs)

    def test_only_constructor_levels_are_claimed(self):
        out=audit()
        self.assertIn("NOT_BEHAVIORAL_VALIDATION",out["status"])
        self.assertFalse(out["both_have_risk_no_joint_adoption"]["weak_joint_adoption"])
        self.assertFalse(out["burn_before_production"]["path_viable"])
        self.assertTrue(out["production_before_investment"]["path_viable"])


if __name__ == "__main__":
    unittest.main()
