"""C11 replay: real-check invocation and metamorphic counterexamples.

Tests execute a fake subprocess to check orchestration, not the real tools.
The deployed CI invokes those tools on the actual changed repository.
"""
import copy
import json
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import pi_flr_replay_gate as rg


class ReplayGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/rg.TRANSFER_PATH).read_text(encoding="utf-8"))
        cls.workflow=(ROOT/".github/workflows/pi-flr-integrity.yml").read_text(encoding="utf-8")

    def test_readme_replays_real_language_l0_and_manifest_commands(self):
        plan=rg.planned_replay(self.data,["README.md"])
        self.assertEqual(plan["check_ids"],
                         ["LANGUAGE","README_L0","RISE_MANIFEST"])
        self.assertEqual(plan["matched_paths"],["README.md"])

    def test_workflow_change_replays_flr_validation_and_mutations(self):
        plan=rg.planned_replay(self.data,[".github/workflows/pi-flr-integrity.yml"])
        self.assertEqual(plan["check_ids"],["FLR_META","FLR_MUTANTS"])

    def test_flr_tool_changes_replay_flr_controls(self):
        plan=rg.planned_replay(self.data,["tools/pi_flr_replay_gate.py"])
        self.assertIn("FLR_META",plan["check_ids"])
        self.assertIn("FLR_MUTANTS",plan["check_ids"])

    def test_case_coverage_must_be_monotonic_under_added_paths(self):
        a=rg.planned_replay(self.data,["README.md"])
        b=rg.planned_replay(self.data,["README.md","experiments/e010/README_EN.md"])
        self.assertTrue(set(a["check_ids"])<=set(b["check_ids"]))
        self.assertIn("E010_LINEAGE",b["check_ids"])

    def test_input_permutation_and_duplication_do_not_change_checks(self):
        paths=["README.md",".github/workflows/pi-flr-integrity.yml"]
        a=rg.planned_replay(self.data,paths)
        b=rg.planned_replay(self.data,list(reversed(paths))+paths)
        self.assertEqual(a,b)

    def test_unmatched_scope_not_misreported_as_verified(self):
        plan=rg.planned_replay(self.data,["new/irrelevant.bin"])
        self.assertEqual(plan["check_ids"],[])
        result=rg.execute(plan,run=lambda *a,**k: self.fail("No check should run"))
        self.assertEqual(result["status"],"NO_KNOWN_RISK_MATCHED")
        self.assertEqual(result["executed"],[])

    def test_any_failed_replay_blocks_and_keeps_all_receipts(self):
        plan=rg.planned_replay(self.data,["README.md"])
        called=[]
        def runner(cmd,**kwargs):
            called.append(cmd)
            return SimpleNamespace(returncode=1 if "tools/check_readme_l0.py" in cmd else 0)
        outcome=rg.execute(plan,run=runner)
        self.assertEqual(outcome["status"],"BLOCKED_FAILED")
        self.assertEqual(outcome["failed_checks"],["README_L0"])
        self.assertEqual(len(called),3)
        self.assertEqual(len(outcome["executed"]),3)

    def test_only_actual_subprocess_zero_counts_pass(self):
        plan=rg.planned_replay(self.data,["README.md"])
        seen=[]
        def runner(cmd,**kwargs):
            seen.append(cmd)
            return SimpleNamespace(returncode=0)
        out=rg.execute(plan,run=runner)
        self.assertEqual(out["status"],"SCOPED_REPLAY_PASS")
        self.assertEqual(len(seen),3)
        self.assertTrue(all(not isinstance(c,str) for c in seen))

    def test_no_shell_interpolation_of_path_inputs(self):
        plan=rg.planned_replay(self.data,["README.md; echo PWNED"])
        self.assertEqual(plan["check_ids"],[])
        self.assertEqual(plan["matched_paths"],[])

    def test_mutating_a_rule_without_executor_fails_closed(self):
        d=copy.deepcopy(self.data)
        d["preflight"].append({
            "id":"R99","match":"README.md","cases":["FLR-0005"],
            "controls":["FLR-C02"],"checkpoints":["bad unregistered risk"]})
        with self.assertRaisesRegex(rg.ReplayError,"RULE_AND_EXECUTOR_DRIFT"):
            rg.planned_replay(d,["README.md"])

    def test_missing_git_base_never_means_no_changed_files(self):
        with self.assertRaisesRegex(rg.ReplayError,"BASELINE_COMMIT_NOT_OBSERVED"):
            rg.git_changed_paths("")
        with self.assertRaisesRegex(rg.ReplayError,"BASELINE_COMMIT_NOT_OBSERVED"):
            rg.git_changed_paths("HEAD")

    def test_missing_commit_rejected_before_diff(self):
        def reject(*args,**kwargs):
            return SimpleNamespace(returncode=1,stdout="")
        with self.assertRaisesRegex(rg.ReplayError,"BASELINE_COMMIT_NOT_ACCESSIBLE"):
            rg.git_changed_paths("a"*40,run=reject)

    def test_git_diff_failure_never_returns_empty_scope(self):
        def runner(cmd,**kwargs):
            return SimpleNamespace(returncode=0 if "rev-parse" in cmd else 1,stdout="")
        with self.assertRaisesRegex(rg.ReplayError,"CHANGED_PATHS_NOT_OBSERVED"):
            rg.git_changed_paths("a"*40,run=runner)

    def test_deleting_execution_hook_is_detectable(self):
        b=self.workflow.replace('python3 tools/pi_flr_replay_gate.py --baseline-commit "$BASE"',
                                'python3 -c "print(1)"')
        self.assertNotEqual(b,self.workflow)
        with self.assertRaisesRegex(rg.ReplayError,"CI_REPLAY_INVOCATION_MISSING"):
            rg.verify_contract(self.data,b)

    def test_missing_receipt_artifact_fails(self):
        b=self.workflow.replace("if-no-files-found: error","if-no-files-found: warn")
        self.assertNotEqual(b,self.workflow)
        with self.assertRaisesRegex(rg.ReplayError,"REPLAY_RECEIPT_NOT_PERSISTED"):
            rg.verify_contract(self.data,b)

    def test_no_field_effectiveness_claim_from_replay(self):
        out=rg.execute(rg.planned_replay(self.data,["README.md"]),
            run=lambda *a,**k:SimpleNamespace(returncode=0))
        self.assertIn("NOT_FIELD_EFFECTIVENESS",out["scope"])


    def test_unmapped_python_change_blocks_scoped_success(self):
        plan=rg.planned_replay(self.data,["tools/unclassified_analysis.py"])
        self.assertEqual(plan["unmapped_material_paths"],["tools/unclassified_analysis.py"])
        result=rg.execute(plan,run=lambda *a,**k:self.fail("No allowed command"))
        self.assertEqual(result["status"],"BLOCKED_UNMAPPED_MATERIAL")

    def test_unmapped_json_cannot_be_cleared_by_other_green_check(self):
        plan=rg.planned_replay(self.data,["README.md","experiments/e009/NEW_RESULT.json"])
        result=rg.execute(plan,run=lambda *a,**k:SimpleNamespace(returncode=0))
        self.assertEqual(result["status"],"BLOCKED_UNMAPPED_MATERIAL")
        self.assertEqual(len(result["executed"]),3)
        self.assertEqual(plan["unmapped_material_paths"],["experiments/e009/NEW_RESULT.json"])

    def test_unmapped_markdown_cannot_disappear_into_no_risk(self):
        plan=rg.planned_replay(self.data,["funding/NEW_RESEARCH_CLAIM.md"])
        self.assertEqual(rg.execute(plan,run=lambda *a,**k:self.fail("no run"))["status"],
                         "BLOCKED_UNMAPPED_MATERIAL")

    def test_flr_registry_json_change_has_full_flr_test_selection(self):
        p=rg.planned_replay(self.data,["knowledge/PI_FLR_CASES_V0_1_0.json"])
        self.assertEqual(p["check_ids"],["FLR_ALL_TESTS","FLR_META"])
        self.assertFalse(p["unmapped_material_paths"])

    def test_language_registry_change_runs_full_inventory_and_cannot_false_green(self):
        path = "knowledge/language-edition-register.json"
        plan = rg.planned_replay(self.data, [path])
        self.assertEqual(plan["check_ids"], ["BILINGUAL_INVENTORY"])
        self.assertEqual(plan["unmapped_material_paths"], [])
        bad = copy.deepcopy(self.data)
        bad["preflight"] = [r for r in bad["preflight"] if r["id"] != "R09"]
        with self.assertRaisesRegex(rg.ReplayError, "RULE_AND_EXECUTOR_DRIFT"):
            rg.planned_replay(bad, [path])

    def test_flr_test_file_change_is_mapped(self):
        p=rg.planned_replay(self.data,["tests/test_pi_flr_replay_gate.py"])
        self.assertEqual(p["check_ids"],["FLR_ALL_TESTS","FLR_META"])

    def test_delete_and_rename_both_ends_observed(self):
        transcript="D\0README.md\0R100\0research/old.md\0research/new.md\0"
        seen=[]
        def fake(args,**kwargs):
            seen.append(args)
            return SimpleNamespace(returncode=0,
                  stdout=transcript if "--name-status" in args else "hash")
        result=rg.git_changed_paths("a"*40,run=fake)
        self.assertEqual(result,sorted(["README.md","research/old.md","research/new.md"]))
        self.assertIn("--name-status",seen[1])
        self.assertIn("-z",seen[1])
        self.assertNotIn("--diff-filter=ACMR",seen[1])

    def test_git_rename_missing_second_path_fails_closed(self):
        def fake(args,**kwargs):
            return SimpleNamespace(returncode=0,stdout="R100\0old.py\0" if
                                   "--name-status" in args else "hash")
        with self.assertRaisesRegex(rg.ReplayError,"DIFF_RECORD_TRUNCATED"):
            rg.git_changed_paths("a"*40,run=fake)

    def test_no_git_diff_claim_without_nul_terminator(self):
        def fake(args,**kwargs):
            return SimpleNamespace(returncode=0,stdout="M\0tools/script.py" if
                                   "--name-status" in args else "hash")
        with self.assertRaisesRegex(rg.ReplayError,"DIFF_FORMAT_INVALID"):
            rg.git_changed_paths("a"*40,run=fake)

    def test_material_changes_monotone_risk_under_union(self):
        a=rg.planned_replay(self.data,["README.md"])
        b=rg.planned_replay(self.data,["README.md","new/unmapped_data.json"])
        self.assertTrue(set(a["check_ids"])<=set(b["check_ids"]))
        self.assertEqual(rg.execute(b,run=lambda *a,**k:SimpleNamespace(returncode=0))["status"],
                         "BLOCKED_UNMAPPED_MATERIAL")



if __name__=="__main__":
    unittest.main()
