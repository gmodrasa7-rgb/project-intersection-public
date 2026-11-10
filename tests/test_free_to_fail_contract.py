"""Data-free guard for the Free to Fail IVS-0R *receipt contract*.

This test deliberately does not claim to reproduce the original human data.
Actual 8-OLS reproduction requires the unmodified author ZIP, kept outside git.
"""

import ast
import copy
import hashlib
import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
STEM = "MER_EI_FREE_TO_FAIL_INDEPENDENT_RAW_REANALYSIS_2026-11-10"
RECEIPT = ROOT / "research" / (STEM + ".json")


def validate_receipt(record):
    assert record["sample"]["study1_retained"] == 8004
    assert record["sample"]["study2_retained"] == 6033
    assert record["sample"]["total_unique_spectator_records"] == 14037
    a = record["source_arm_counts"]
    for prefix, total in (("study1_", 8004), ("study2_", 6033)):
        assert sum(v["n"] for k, v in a.items() if k.startswith(prefix)) == total
    for arm in a.values():
        assert 0 <= arm["yes"] <= arm["n"]
    soft = a["study1_soft_internal"]["yes"] + a["study1_soft_external"]["yes"]
    soft_n = a["study1_soft_internal"]["n"] + a["study1_soft_external"]["n"]
    hard = a["study1_hard_internal"]["yes"] + a["study1_hard_external"]["yes"]
    hard_n = a["study1_hard_internal"]["n"] + a["study1_hard_external"]["n"]
    effect = soft / soft_n - hard / hard_n
    assert math.isclose(100 * effect, record["numeric_checks"]["study1_pooled_soft_minus_hard_pp"], abs_tol=1e-8)
    assert math.isclose(100 * effect, 54.9752596908, abs_tol=1e-8)
    assert record["numeric_checks"]["published_2023_principal_ols_models"] == 8
    assert record["numeric_checks"]["published_2023_principal_ols_models_matched_to_3_decimals"] == 8
    assert record["numeric_checks"]["negative_controls_rejected"] == 2
    assert record["claim_status"]["novelty_of_frechet_bounds"].startswith("NOVELTY_REJECTED")
    assert record["gates"]["A5_original_B_or_AI_intrinsic_motive"].startswith("HOLD")


def isolated_classify():
    """Compile only response constants and classify(); no NumPy or raw data needed."""
    path = ROOT / "experiments" / "mer_ei" / "independent_free_to_fail_replication.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = {"RESTRICT", "NORESTRICT", "INFO", "NOINFO", "FORCE_SAFE", "FORCE_RISKY", "CELLS"}
    selected = [node for node in tree.body
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id in names for target in node.targets)]
    selected += [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "classify"]
    scope = {}
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), "exec"), scope)
    return scope


class RawReanalysisContract(unittest.TestCase):
    def setUp(self):
        self.receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    def test_receipt_mathematics_and_bounded_claims(self):
        validate_receipt(self.receipt)

    def test_mutated_aggregate_is_rejected(self):
        mutated = copy.deepcopy(self.receipt)
        mutated["source_arm_counts"]["study1_soft_internal"]["yes"] += 20
        with self.assertRaises(AssertionError):
            validate_receipt(mutated)

    def test_script_source_sha_and_original_archive_hash(self):
        p = ROOT / self.receipt["independent_script"]
        source = p.read_bytes()
        self.assertEqual(hashlib.sha256(source).hexdigest(),
                         self.receipt["independent_script_sha256"])
        self.assertIn(self.receipt["author_package"]["zip_md5_verified"].encode(), source)
        self.assertEqual(self.receipt["sample"]["total_unique_spectator_records"], 14037)

    def test_response_recoding_and_two_adversarial_failures(self):
        mod = isolated_classify()
        classify = mod["classify"]
        row = {col: "" for col, _, _ in mod["CELLS"][1].values()}
        row["q134"] = mod["RESTRICT"]
        self.assertEqual(classify(row, 1), (1, 1))
        row["q134"] = "forged response"
        with self.assertRaises(ValueError):
            classify(row, 1)
        row["q134"] = mod["RESTRICT"]
        row["q128"] = mod["INFO"]
        with self.assertRaises(ValueError):
            classify(row, 1)

    def test_language_metadata_and_predecessor_lineage(self):
        for language, other in (("EN", "KO"), ("KO", "EN")):
            text = (ROOT / "research" / f"{STEM}_{language}.md").read_text(encoding="utf-8")
            self.assertIn(f"<!-- PI-LANGUAGE: {language.lower()} -->", text)
            self.assertIn(f"{STEM}_{other}.md", text)
            self.assertIn("8/8", text)
        # The local audit bundle contains only the proposed files. Full GitHub
        # checkout CI additionally proves that cited predecessor files survive.
        if (ROOT / "README.md").is_file():
            for path in self.receipt["prior_work_preserved"]:
                self.assertTrue((ROOT / path).is_file(), path)

    def test_replay_scope_covers_material_files_and_remains_executable(self):
        script = ROOT / "tools" / "pi_flr_replay_gate.py"
        nodes = ast.parse(script.read_text(encoding="utf-8")).body
        settings = {}
        for node in nodes:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in {"COMMANDS", "DIRECT_PATH_CHECKS"}:
                        settings[target.id] = ast.literal_eval(node.value)
        commands, mapped = settings["COMMANDS"], settings["DIRECT_PATH_CHECKS"]
        for path in (
            "experiments/mer_ei/independent_free_to_fail_replication.py",
            "research/" + STEM + ".json",
            "tests/test_free_to_fail_contract.py",
            "tools/pi_flr_replay_gate.py",
            "knowledge/language-edition-register.json",
        ):
            self.assertTrue(mapped.get(path), path)
            for label in mapped[path]:
                self.assertIn(label, commands)
                self.assertEqual(commands[label][0], "python3")
        self.assertIn("FREE_TO_FAIL_RECEIPT", mapped["tools/pi_flr_replay_gate.py"])


if __name__ == "__main__":
    unittest.main()
