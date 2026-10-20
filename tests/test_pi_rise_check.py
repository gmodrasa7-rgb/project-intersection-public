"""PI-RISE v0.1.0 unit tests: all inputs are synthetic, no user data."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from pi_rise_check import assess, InputError


class RISETests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "operations" / "PI_RISE_SYNTHETIC_EXAMPLE_V0_1_0.json"
        self.s = json.loads(path.read_text(encoding="utf-8"))

    def test_synthetic_2_month_runway_is_conserve(self):
        x = assess(self.s)
        self.assertEqual(x["overall"], "CONSERVE")
        self.assertFalse(x["pipeline_counted_as_cash"])

    def test_awarded_unpaid_large_proposal_never_adds_to_cash(self):
        s = copy.deepcopy(self.s)
        s["funding_pipeline"][0]["proposed_amount_krw"] = 999999999999
        self.assertEqual(assess(s)["overall"], "CONSERVE")

    def test_unverified_cash_is_unknown_not_zero(self):
        s = copy.deepcopy(self.s)
        s["finance"]["liquid_cash_krw"] = {"status": "UNVERIFIED", "amount": None}
        self.assertEqual(assess(s)["overall"], "UNKNOWN")

    def test_mislabelled_unverified_amount_fails_closed(self):
        s = copy.deepcopy(self.s)
        s["finance"]["liquid_cash_krw"]["status"] = "UNVERIFIED"
        with self.assertRaises(InputError):
            assess(s)

    def test_zero_monthly_burn_is_unknown_not_infinite(self):
        s = copy.deepcopy(self.s)
        s["finance"]["essential_monthly_burn_krw"]["amount"] = 0
        self.assertEqual(assess(s)["overall"], "UNKNOWN")

    def test_double_count_unknown(self):
        s = copy.deepcopy(self.s)
        s["no_double_count_verified"] = False
        self.assertEqual(assess(s)["overall"], "UNKNOWN")

    def test_real_input_must_be_private(self):
        s = copy.deepcopy(self.s)
        s["synthetic"] = False
        with self.assertRaises(InputError):
            assess(s)

    def test_capacity_no_overrides_healthy_runway(self):
        s = copy.deepcopy(self.s)
        s["finance"]["liquid_cash_krw"]["amount"] = 10000000
        s["capacity"]["researcher_can_work"] = "NO"
        self.assertEqual(assess(s)["overall"], "PAUSE_NONESSENTIAL")

    def test_funder_conclusion_control_blocks_expansion(self):
        s = copy.deepcopy(self.s)
        s["finance"]["liquid_cash_krw"]["amount"] = 10000000
        s["independence"]["sponsor_conclusion_control"] = "YES"
        self.assertEqual(assess(s)["overall"], "HOLD_EXPANSION")

    def test_local_restore_missing_blocks_expansion(self):
        s = copy.deepcopy(self.s)
        s["finance"]["liquid_cash_krw"]["amount"] = 10000000
        s["continuity"]["local_restore_tested"] = False
        self.assertEqual(assess(s)["overall"], "HOLD_EXPANSION")

    def test_unverified_and_paused_researcher_still_pauses(self):
        s = copy.deepcopy(self.s)
        s["finance"]["liquid_cash_krw"] = {"status": "UNVERIFIED", "amount": None}
        s["capacity"]["researcher_can_work"] = "NO"
        self.assertEqual(assess(s)["overall"], "PAUSE_NONESSENTIAL")


if __name__ == "__main__":
    unittest.main()
