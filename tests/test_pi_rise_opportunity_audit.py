"""PI-RISE opportunity metadata regression: counterexamples and no cash claims."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_rise_opportunity_audit as target


class OpportunityTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "operations" / "PI_RISE_OPPORTUNITY_REGISTRY_V0_1_0.json").read_text(encoding="utf-8"))

    def bad(self, mutate):
        x = deepcopy(self.data)
        mutate(x)
        with self.assertRaises(target.RegistryError):
            target.audit(x)

    def test_base_case(self):
        x = target.audit(self.data)
        self.assertEqual(x["funder_pages_recorded"], 3)
        self.assertFalse(x["submission_verified"])
        self.assertFalse(x["award_verified"])
        self.assertFalse(x["bank_receipt_verified"])
        self.assertFalse(x["arrival_time_inferred"])

    def test_false_cash(self):
        self.bad(lambda x: x["records"][0].update(time_to_usable_cash="21 DAYS"))

    def test_form_not_submitted(self):
        self.bad(lambda x: x["records"][0].update(application_proof="SUBMITTED"))

    def test_award_not_received(self):
        self.bad(lambda x: x["records"][0].update(award_proof="AWARDED"))

    def test_false_payout(self):
        self.bad(lambda x: x["records"][1]["payout"].update(days=21))

    def test_feedback_is_not_payout(self):
        self.bad(lambda x: x["records"][1]["decision"].update(type="UNKNOWN",days=21))

    def test_fake_rolling_deadline(self):
        self.bad(lambda x: x["records"][0].update(deadline_state="ROLLING"))

    def test_fake_public_ceiling(self):
        self.bad(lambda x: x["records"][2]["published_ceiling"].update(currency="USD",amount="150000"))

    def test_bad_ceiling_money_type(self):
        self.bad(lambda x: x["records"][0]["published_ceiling"].update(amount=20000))

    def test_bad_ceiling_float_not_allowed(self):
        self.bad(lambda x: x["records"][0]["published_ceiling"].update(amount="1e12"))

    def test_duplicate(self):
        self.bad(lambda x: x["records"][1].update(id="BLUEDOT_RAPID_2026"))

    def test_future_date(self):
        self.bad(lambda x: x["records"][0].update(source_checked_on="2027-01-01"))

    def test_url_change(self):
        self.bad(lambda x: x["records"][0].update(official_url="https://funds-claim.example/bluedot"))

    def test_privacy_field(self):
        self.bad(lambda x: x["records"][0].update(bank_account="EXAMPLE_NOT_REAL"))

    def test_finance_implication(self):
        self.bad(lambda x: x.update(financial_accounting_effect="CASH_INCOME"))

    def test_bad_calendar(self):
        self.bad(lambda x: x.update(as_of="2026-02-30"))


if __name__ == "__main__":
    unittest.main()
