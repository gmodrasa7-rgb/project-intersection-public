"""PI-RISE finance registry synthetic regression; no real bank data."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_rise_finance_audit as mod


class FinanceAuditTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "operations" / "PI_RISE_FINANCE_PIPELINE_V0_1_0.json")
                               .read_text(encoding="utf-8"))

    def test_public_canonical_registry(self):
        out = mod.audit(self.data, check_paths=True, root=ROOT)
        self.assertEqual(out["result"], "STRUCTURE_ONLY_NOT_EXTERNAL_VERIFICATION")
        self.assertFalse(out["cash_aggregation_performed"])
        self.assertFalse(out["bank_receipts_certified"])
        self.assertEqual(out["stage_counts"]["PAID_VERIFIED"], 0)

    def test_refuse_fake_cash_flag(self):
        x = copy.deepcopy(self.data)
        x["cash_aggregation_allowed"] = True
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_refuse_fake_payment_and_missing_ref(self):
        x = copy.deepcopy(self.data)
        x["entries"][1]["stage"] = "PAID_VERIFIED"
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_refuse_award_without_proof(self):
        x = copy.deepcopy(self.data)
        x["entries"][1]["stage"] = "AWARDED_UNPAID"
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_refuse_duplicate_id(self):
        x = copy.deepcopy(self.data)
        x["entries"][2]["id"] = x["entries"][1]["id"]
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_refuse_duplicate_receipt_ref(self):
        x = copy.deepcopy(self.data)
        for item in x["entries"][1:3]:
            item["stage"] = "PAID_VERIFIED"
            item["receipt_evidence"] = "BANK_RECONCILED_DECLARED"
            item["receipt_record_ref"] = "funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md#verified-row-1"
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_reject_float_currency_and_signed_amounts(self):
        for wrong in (5000, "-10", "1e9", "0", "1.000", "NaN"):
            x = copy.deepcopy(self.data)
            x["entries"][1]["proposal"]["amount"] = wrong
            with self.subTest(wrong=wrong):
                with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_reject_private_unrecognized_fields(self):
        x = copy.deepcopy(self.data)
        x["entries"][0]["bank_account"] = "synthetic fake"
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_reject_open_pr_presented_as_main(self):
        x = copy.deepcopy(self.data)
        x["entries"][3]["publication"] = "MAIN"
        with self.assertRaises(mod.AuditError): mod.audit(x)

    def test_sponsorship_cannot_shift_restriction(self):
        x = copy.deepcopy(self.data)
        x["entries"][0]["restrictions"] = "RESTRICTED_PROJECT_USE"
        with self.assertRaises(mod.AuditError): mod.audit(x)


if __name__ == "__main__":
    unittest.main()
