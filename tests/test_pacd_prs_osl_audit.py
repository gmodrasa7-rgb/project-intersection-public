import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import pacd_prs_osl_audit as mod

class OSLTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(mod.CASES.read_text(encoding="utf-8"))
    def test_valid_toy_case_set(self):
        self.assertEqual(mod.verify(copy.deepcopy(self.data))["cases"],3)
    def test_owner_self_loss_exists_not_universal(self):
        self.assertEqual([x["owner_private_choice"] for x in self.data["cases"]],["C","D","TIE"])
    def test_arithmetic_tampering_rejected(self):
        d=copy.deepcopy(self.data);d["cases"][0]["delta_owner"]=61
        with self.assertRaisesRegex(mod.OslAuditError,"DELTA_MATH_ERROR"):mod.verify(d)
    def test_wrong_winner_rejected(self):
        d=copy.deepcopy(self.data);d["cases"][1]["owner_private_choice"]="C"
        with self.assertRaisesRegex(mod.OslAuditError,"OWNER_CHOICE_ERROR"):mod.verify(d)
    def test_not_empirical(self):
        d=copy.deepcopy(self.data);d["evidence_grade"]="EMPIRICAL"
        with self.assertRaisesRegex(mod.OslAuditError,"FALSE_REAL_WORLD_PROMOTION"):mod.verify(d)
    def test_no_owner_rights_substitution(self):
        d=copy.deepcopy(self.data);d["cases"][0]["outsider_B_legitimate_rights_assessment"]="OWNER_APPROVED"
        with self.assertRaisesRegex(mod.OslAuditError,"OWNER_WELFARE_NOT_PROOF_OF_B_RIGHTS"):mod.verify(d)
    def test_no_missing_reverse_counterexample(self):
        d=copy.deepcopy(self.data);d["cases"][1]["D"]["gross"]=100;d["cases"][1]["D"]["net"]=65;d["cases"][1]["delta_owner"]=35;d["cases"][1]["owner_private_choice"]="C"
        with self.assertRaisesRegex(mod.OslAuditError,"MISSING_REVERSE_OR_TIE"):mod.verify(d)

if __name__=="__main__":
    unittest.main()
