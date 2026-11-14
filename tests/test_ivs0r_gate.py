import copy
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from validate_ivs0r_gate import validate

def record():
    return {
      "schema_version":"IVS0R_GATE_V1","experiment_id":"E011_FIXTURE",
      "evidence_class":"PROJECT_SYNTHETIC",
      "preregistration":{"uri_or_path":"experiments/e011/prereg.md","frozen_before_outcomes":True,"primary_estimand":"exit reachability under fixed conditions","threshold_rationale":"No scalar threshold; dimensions reported separately."},
      "exit_audit":{"reachability":"VERIFIED","post_exit_viability":"VERIFIED","non_retaliation":"NOT_MEASURED","recovery_path":"NOT_MEASURED","measurement_and_uncertainty":"Toy fixture only; two dimensions unmeasured."},
      "policy_shift_audit":{"design":"fixed-state descriptive comparison","randomized_or_counterbalanced":False,"estimator":"KL with declared smoothing","uncertainty":"bootstrap interval not estimated in fixture","causal_interpretation":"DESCRIPTIVE_ONLY"},
      "third_party_audit":{"status":"NOT_MEASURED","method":"dependency graph not collected","unresolved_material_loss":False},
      "reward_provenance_audit":{"status":"INCOMPLETE","method":"training lineage unavailable"},
      "negative_result_preservation":{"preserved":True,"source_records":["E009"],"exclusions_and_failures_recorded":True},
      "rival_hypotheses":["ordinary stochastic variation"],"limitations":["synthetic fixture; no field inference"],
      "external_replication":False,"verdict":"HOLD"
    }

class GateTests(unittest.TestCase):
    def test_bounded_synthetic_record_can_be_held(self):
        self.assertEqual([],validate(record()))
    def test_missing_preregistration_is_rejected(self):
        d=record(); d["preregistration"]["frozen_before_outcomes"]=False
        self.assertTrue(validate(d))
    def test_negative_result_erasure_is_rejected(self):
        d=record(); d["negative_result_preservation"]["preserved"]=False
        self.assertTrue(validate(d))
    def test_unknown_is_not_zero_or_pass(self):
        d=record(); d["verdict"]="PROVISIONAL_PASS_REQUIRES_EXTERNAL_REPLICATION"
        self.assertTrue(validate(d))
    def test_unjustified_causal_claim_is_rejected(self):
        d=record(); d["policy_shift_audit"]["causal_interpretation"]="IDENTIFIED_WITH_STATED_ASSUMPTIONS"
        self.assertTrue(validate(d))
    def test_unresolved_third_party_loss_blocks_pass(self):
        d=record(); d["evidence_class"]="INDEPENDENT_REPLICATION"; d["verdict"]="PROVISIONAL_PASS_REQUIRES_EXTERNAL_REPLICATION"
        d["exit_audit"].update({k:"VERIFIED" for k in ("reachability","post_exit_viability","non_retaliation","recovery_path")})
        d["third_party_audit"].update(status="COMPLETE",unresolved_material_loss=True)
        d["reward_provenance_audit"]["status"]="COMPLETE"
        d["policy_shift_audit"]["causal_interpretation"]="DESCRIPTIVE_ONLY"
        self.assertTrue(validate(d))
    def test_nonfinite_measurement_is_rejected(self):
        d=record(); d["policy_shift_audit"]["monitoring_shift_value"]=float("nan")
        self.assertTrue(validate(d))

if __name__=="__main__": unittest.main()
