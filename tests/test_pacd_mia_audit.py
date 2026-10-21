import copy
import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pacd_mia_audit as mod

class ProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads((ROOT / mod.LEDGER).read_text(encoding="utf-8"))
        cls.en = (ROOT / mod.EN).read_text(encoding="utf-8")
        cls.ko = (ROOT / mod.KO).read_text(encoding="utf-8")

    def audit(self, data=None, en=None, ko=None):
        return mod.audit(self.ledger if data is None else data,
                         self.en if en is None else en,
                         self.ko if ko is None else ko)

    def test_current_ledger(self):
        r = self.audit()
        self.assertEqual(r["status"], "PROVENANCE_STRUCTURE_PASS_NOT_INDEPENDENT_SCIENCE")
        self.assertEqual(r["model_trials"], 0)

    def test_false_evidence_promotion_rejected(self):
        d = copy.deepcopy(self.ledger)
        d["claims"][0]["status"] = "INDEPENDENT_FIELD_VALIDATED"
        with self.assertRaisesRegex(mod.SourceAuditError, "UNSUPPORTED_EVIDENCE_PROMOTION"):
            self.audit(d)

    def test_unread_source_cannot_claim_saturation(self):
        d = copy.deepcopy(self.ledger)
        d["global_search_saturation"] = "VERIFIED"
        with self.assertRaisesRegex(mod.SourceAuditError, "UNSUPPORTED_LITERATURE_OR_NOVELTY_PROMOTION"):
            self.audit(d)

    def test_missing_rival_claim_source_rejected(self):
        d = copy.deepcopy(self.ledger)
        d["claims"][0]["rival_sources"].append("MIA-S99")
        with self.assertRaisesRegex(mod.SourceAuditError, "CLAIM_REFERENCES_UNKNOWN_SOURCE"):
            self.audit(d)

    def test_no_asymmetric_disappearance_of_hypothesis(self):
        with self.assertRaisesRegex(mod.SourceAuditError, "MISSING_PAIRED_HYPOTHESIS"):
            self.audit(ko=self.ko.replace("MIA-H7", "MIA-Z7"))

    def test_no_real_case_without_boundary(self):
        d = copy.deepcopy(self.ledger)
        d["real_world_case_front"][0]["not_observed"] = ""
        with self.assertRaisesRegex(mod.SourceAuditError, "REAL_CASE_WITHOUT_EVIDENCE_LIMITS"):
            self.audit(d)

    def test_no_single_mechanism_certainty_without_rival(self):
        d = copy.deepcopy(self.ledger)
        d["mechanisms"][1]["confound"] = ""
        with self.assertRaisesRegex(mod.SourceAuditError, "MECHANISM_WITHOUT_RIVAL_OR_INTERVENTION"):
            self.audit(d)

if __name__ == "__main__":
    unittest.main()
