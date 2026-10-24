"""Mutation tests: evidence assertion failures must be observable, not hardcoded PASS."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import pi_flr_mer_ei_source_guard as g

class EvidenceGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw=json.loads((ROOT/g.LEDGER).read_text(encoding="utf-8"))
        cls.ko=(ROOT/g.KO).read_text(encoding="utf-8")
        cls.en=(ROOT/g.EN).read_text(encoding="utf-8")

    def validate(self, obj=None, ko=None, en=None, ver="v0.7.0"):
        return g.audit(self.raw if obj is None else obj,
                       self.ko if ko is None else ko,
                       self.en if en is None else en,ver)

    def test_actual_source_ledger_contract(self):
        result=self.validate()
        self.assertEqual(result["status"],"SOURCE_TRANSCRIPTION_AND_SCOPE_ONLY")
        self.assertEqual(result["source_records"],5)
        self.assertEqual(result["participants_reanalyzed"],0)

    def test_wrong_coefficient_fails(self):
        data=copy.deepcopy(self.raw)
        data["estimates"][1]["coef"]=.999
        with self.assertRaisesRegex(g.EvidenceGuardError,"TRANSCRIPTION"):
            self.validate(data)

    def test_wrong_interval_fails(self):
        data=copy.deepcopy(self.raw)
        data["estimates"][3]["approx_normal_95_percent_points"]=[0,0]
        with self.assertRaisesRegex(g.EvidenceGuardError,"CI_ARITHMETIC"):
            self.validate(data)

    def test_source_claimed_replicated_fails(self):
        data=copy.deepcopy(self.raw)
        data["author_tables_rerun"]=1
        with self.assertRaisesRegex(g.EvidenceGuardError,"FABRICATED"):
            self.validate(data)

    def test_null_claim_cannot_be_promoted(self):
        data=copy.deepcopy(self.raw)
        data["estimates"][3]["significance"]="PROVEN_EQUIVALENT"
        with self.assertRaisesRegex(g.EvidenceGuardError,"MISCLASSIFIED"):
            self.validate(data)

    def test_rvd_version_upgrade_rejected(self):
        with self.assertRaisesRegex(g.EvidenceGuardError,"RVD_VERSION"):
            self.validate(ver="v0.8.0")

    def test_missing_bilingual_mirror_fails(self):
        with self.assertRaisesRegex(g.EvidenceGuardError,"MISSING_MIRROR"):
            self.validate(en=self.en.replace("<!-- PI-MIRROR: "+g.KO+" -->",""))

if __name__=="__main__":
    unittest.main()
