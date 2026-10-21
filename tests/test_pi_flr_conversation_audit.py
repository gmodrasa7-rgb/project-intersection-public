"""PI-FLR conversation audit anti-overclaim, privacy, history and CI regressions.

These are deterministic tests of the registry's inference boundaries, not a
complete reread of all conversations or independent science.
"""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_flr_conversation_audit as audit


class ConversationAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / audit.LEDGER).read_text(encoding="utf-8"))
        cls.registry = json.loads((ROOT / audit.REGISTRY).read_text(encoding="utf-8"))

    def test_current_bounded_ledger_valid(self):
        result = audit.validate(self.data, self.registry)
        self.assertEqual(result["status"], "BOUNDED_AUDIT_VALID_NOT_EXHAUSTIVE")
        self.assertGreaterEqual(result["patterns"], 20)

    def test_english_must_precede_korean(self):
        d = copy.deepcopy(self.data)
        d["language_order"].reverse()
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "ENGLISH_FIRST_RULE"):
            audit.validate(d, self.registry)

    def test_unknown_chats_cannot_be_declared_absent(self):
        d = copy.deepcopy(self.data)
        d["coverage"]["missing_records_not_zero"] = False
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "UNKNOWN_HISTORY_WAS_ERASED"):
            audit.validate(d, self.registry)

    def test_total_chat_census_not_claimed(self):
        d = copy.deepcopy(self.data)
        d["status"] = "ALL_CHATS_VERIFIED"
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "FALSE_FULL_CHAT_AUDIT_CLAIM"):
            audit.validate(d, self.registry)

    def test_conversation_memory_cannot_become_technical_log(self):
        d = copy.deepcopy(self.data)
        row = next(x for x in d["records"]
                   if x["evidence_class"] == "CONVERSATION_SUMMARY_REPORTED")
        row["evidence_class"] = "GITHUB_LOG_CONFIRMED"
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "LOG_CONFIRMED_WITHOUT_A_RUN_RECEIPT"):
            audit.validate(d, self.registry)

    def test_bogus_external_evidence_blocked(self):
        d = copy.deepcopy(self.data)
        d["records"][0]["public_evidence"] = ["https://example.invalid/story"]
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "UNVERIFIED_EXTERNAL_EVIDENCE_DOMAIN"):
            audit.validate(d, self.registry)

    def test_existing_flr_case_link_must_exist(self):
        d = copy.deepcopy(self.data)
        d["records"][0]["linked_flr"] = ["FLR-9999"]
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "INVALID_CANONICAL_FLR_CROSSWALK"):
            audit.validate(d, self.registry)

    def test_private_email_rejected_from_public_ledger(self):
        d = copy.deepcopy(self.data)
        d["records"][0]["observation"] += " researcher@example.com"
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "PRIVATE_IDENTIFIER_IN_PUBLIC_LEDGER"):
            audit.validate(d, self.registry)

    def test_legacy_history_cannot_be_deleted(self):
        d = copy.deepcopy(self.data)
        d["release_version"] = "0.1.1"
        d["records"] = d["records"][1:]
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "HISTORICAL_PATTERN_DELETED"):
            audit.compare_history(d, self.data)

    def test_legacy_history_cannot_be_silently_reclassified(self):
        d = copy.deepcopy(self.data)
        d["release_version"] = "0.1.1"
        d["records"][0]["evidence_class"] = "HYPOTHESIS_ONLY"
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "HISTORICAL_PATTERN_MUTATED"):
            audit.compare_history(d, self.data)

    def test_unversioned_modification_rejected(self):
        d = copy.deepcopy(self.data)
        d["records"].append(copy.deepcopy(d["records"][0]))
        d["records"][-1]["id"] = "FLC-999"
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "UNVERSIONED_AUDIT_CHANGE"):
            audit.compare_history(d, self.data)

    def test_empty_version_promotion_rejected(self):
        d = copy.deepcopy(self.data)
        d["release_version"] = "0.1.1"
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "EMPTY_AUDIT_VERSION_BUMP"):
            audit.compare_history(d, self.data)

    def test_partial_green_cannot_certify_release(self):
        expected = ["README English-first language order",
                    "PI-RISE synthetic-only integrity"]
        actual = [{"name": expected[0], "conclusion": "success"},
                  {"name": expected[1], "conclusion": "failure"}]
        result = audit.validate_release_matrix(actual, expected)
        self.assertEqual(result["status"], "BLOCKED_FAILED")
        self.assertFalse(result["ready"])
        self.assertEqual(result["failed"], [expected[1]])

    def test_missing_required_workflow_remains_unknown(self):
        expected = ["readme", "rise"]
        observed = [{"name": "readme", "conclusion": "success"}]
        result = audit.validate_release_matrix(observed, expected)
        self.assertEqual(result["status"], "INCOMPLETE_UNOBSERVED")
        self.assertFalse(result["ready"])
        self.assertEqual(result["missing"], ["rise"])

    def test_pending_not_success(self):
        expected = ["readme", "rise"]
        observed = [{"name": "readme", "conclusion": "success"},
                    {"name": "rise", "conclusion": "in_progress"}]
        self.assertFalse(audit.validate_release_matrix(observed, expected)["ready"])

    def test_scoped_all_pass_still_not_branch_protection(self):
        names = ["readme", "rise"]
        actual = [{"name": n, "conclusion": "success"} for n in names]
        result = audit.validate_release_matrix(actual, names)
        self.assertTrue(result["ready"])
        self.assertIn("NOT_BRANCH_PROTECTION", result["scope"])

    def test_duplicate_or_unknown_workflow_rejected(self):
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "DUPLICATE_WORKFLOW_RESULT"):
            audit.validate_release_matrix(
                [{"name": "readme", "conclusion": "success"}] * 2, ["readme"])

    def test_competing_explanations_are_mandatory(self):
        d = copy.deepcopy(self.data)
        d["records"][0]["competing_explanation"] = ""
        with self.assertRaisesRegex(audit.ConversationAuditError,
                                    "INSUFFICIENT_PATTERN_FIELD:competing_explanation"):
            audit.validate(d, self.registry)


if __name__ == "__main__":
    unittest.main()
