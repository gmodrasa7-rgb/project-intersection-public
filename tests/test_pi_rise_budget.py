"""PI-RISE-BUDGET: deterministic synthetic scenario regressions only."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pi_rise_budget import budget, bridge_gap, demonstration

def minimum(**kw):
    args=dict(net_target_usd=3000, reserve_rate="0.20",
              subscription_usd=20, power_usd=15)
    args.update(kw)
    return budget(**args)

class BudgetTests(unittest.TestCase):
    def test_base(self):
        x=minimum()
        self.assertEqual(x["monthly_usd"],"3785.00")
        self.assertEqual(x["quarter_3_months_usd"],"11355.00")
        self.assertEqual(x["annual_usd"],"45420.00")
        self.assertEqual(x["daily_annual_average_usd"],"124.44")
        self.assertEqual(x["monthly_krw_ceiling"],"5018910")

    def test_zero_reserve(self):
        self.assertEqual(minimum(reserve_rate="0")["monthly_usd"],"3035.00")

    def test_ten_percent_rounds_up(self):
        x=minimum(reserve_rate="0.10")
        self.assertEqual(x["monthly_usd"],"3368.34")
        self.assertEqual(x["annual_usd"],"40420.08")

    def test_thirty_percent_rounds_up(self):
        self.assertEqual(minimum(reserve_rate="0.30")["monthly_usd"],"4320.72")

    def test_pro_is_substitution_not_plus_plus_pro(self):
        self.assertEqual(minimum(subscription_usd=100)["monthly_usd"],"3865.00")

    def test_api_and_external_are_both_added_not_implicit(self):
        x=minimum(subscription_usd=100,api_usd=100,external_review_usd=300)
        self.assertEqual(x["monthly_usd"],"4265.00")
        self.assertEqual(x["annual_usd"],"51180.00")
        self.assertEqual(x["monthly_krw_ceiling"],"5655390")

    def test_contingency_only_on_operating_lines(self):
        x=minimum(subscription_usd=100,api_usd=100,external_review_usd=300,
                  contingency_rate="0.10")
        self.assertEqual(x["monthly_usd"],"4316.50")

    def test_monotonicity_reserve_and_api_and_fx(self):
        a=minimum()
        self.assertGreater(
            float(minimum(reserve_rate=".30")["monthly_usd"]), float(a["monthly_usd"]))
        self.assertGreater(
            float(minimum(api_usd=1)["monthly_usd"]), float(a["monthly_usd"]))
        self.assertEqual(minimum(fx_krw_per_usd=1450)["monthly_krw_ceiling"],"5488250")

    def test_bridge_shortfall_and_equal_service_allocations(self):
        x=bridge_gap()
        self.assertEqual(x["current_person_net_after_hypothetical_reserve_usd"],"2560.00")
        self.assertEqual(x["personal_net_shortfall_usd"],"440.00")
        self.assertEqual(x["person_line_needed_usd"],"3750.00")
        self.assertEqual(x["total_bridge_needed_same_nonperson_allocations_usd"],"5550.00")

    def test_no_real_grants_inferred(self):
        x=demonstration()
        self.assertEqual(x["status"],"SYNTHETIC_SCENARIO_NOT_FUNDS")
        self.assertIn("NO_GRANT_OR_INCOME_VERIFIED", x["minimum_20pc"]["claims"])

    def test_banned_float(self):
        with self.assertRaises(ValueError):
            minimum(reserve_rate=.2)

    def test_invalid_rates(self):
        for bad in ["-0.01","1","1.01"]:
            with self.subTest(rate=bad):
                with self.assertRaises(ValueError):
                    minimum(reserve_rate=bad)
        with self.assertRaises(ValueError):
            minimum(contingency_rate="2")

    def test_negative_costs_and_fx(self):
        with self.assertRaises(ValueError):
            minimum(api_usd="-1")
        with self.assertRaises(ValueError):
            minimum(fx_krw_per_usd=0)

    def test_no_reviewer_no_independent_validation(self):
        x=minimum(external_review_usd=0)
        self.assertIn("REVIEW_BUDGET_NOT_INDEPENDENT_REPLICATION",x["claims"])

if __name__=="__main__":
    unittest.main()
