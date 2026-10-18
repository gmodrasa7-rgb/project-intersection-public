"""ECR-MIND actual-experience evidence-policy tests, synthetic metadata only."""
import unittest

from inference_guard import Evidence, review, assess_case


class PersonalEvidenceIVS0RTests(unittest.TestCase):
    def test_direct_declared_value_is_retained_without_reinterpretation(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "DECLARED_VALUE"))["status"],
                         "DIRECT_DECLARED_VALUE")

    def test_normative_autonomy_not_relabelled_as_domination(self):
        item = Evidence("CURRENT_DIRECT_REPORT", "LATENT_MOTIVE",
                        contradicted_by_direct_statement=True)
        self.assertEqual(review(item)["status"], "REJECT_CONTRADICTED_INFERENCE")

    def test_self_reported_emotion_not_discarded(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "REPORTED_FEELING"))["status"],
                         "DIRECT_EXPERIENCE_REPORT")

    def test_self_report_does_not_infer_biological_cause(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "BIOLOGICAL_CAUSE"))["status"],
                         "HYPOTHESIS_NOT_CAUSAL_FACT")

    def test_direct_normative_claim_does_not_identify_hidden_motive(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "LATENT_MOTIVE"))["status"],
                         "HYPOTHESIS_NOT_CAUSAL_FACT")

    def test_observed_disagreement_not_fixed_personality(self):
        self.assertEqual(review(Evidence("OBSERVED_CHAT_ACTION", "BEHAVIOR_IN_CONTEXT"))["status"],
                         "SCOPED_BEHAVIOR_EVIDENCE")

    def test_assistant_summary_not_primary_behavioral_observation(self):
        self.assertEqual(review(Evidence("ASSISTANT_SUMMARY", "BEHAVIOR_IN_CONTEXT"))["status"],
                         "BEHAVIOR_NOT_PRIMARY_OBSERVED")

    def test_unverified_precise_historical_dates_refused(self):
        self.assertEqual(review(Evidence("ASSISTANT_SUMMARY", "EXACT_HISTORICAL_ATTRIBUTION",
                                         exact_primary_quote=True, timestamp_verified=True))["status"],
                         "UNVERIFIED_DATE_OR_QUOTE")

    def test_archived_statement_without_timestamp_unverified(self):
        self.assertEqual(review(Evidence("ARCHIVED_PRIMARY_USER_STATEMENT",
                                         "EXACT_HISTORICAL_ATTRIBUTION",
                                         exact_primary_quote=True))["status"],
                         "UNVERIFIED_DATE_OR_QUOTE")

    def test_archived_statement_without_original_quote_unverified(self):
        self.assertEqual(review(Evidence("ARCHIVED_PRIMARY_USER_STATEMENT",
                                         "EXACT_HISTORICAL_ATTRIBUTION",
                                         timestamp_verified=True))["status"],
                         "UNVERIFIED_DATE_OR_QUOTE")

    def test_archived_original_quote_and_date_allowed_not_personality(self):
        self.assertEqual(review(Evidence("ARCHIVED_PRIMARY_USER_STATEMENT",
                                         "EXACT_HISTORICAL_ATTRIBUTION",
                                         exact_primary_quote=True, timestamp_verified=True))["status"],
                         "VERIFIED_QUOTATION_ONLY")

    def test_already_answered_value_question_not_asked_again(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "DECLARED_VALUE",
                                         already_resolved_question=True,
                                         repeat_question=True))["status"],
                         "BLOCK_REDUNDANT_QUESTION")

    def test_question_for_new_missing_information_still_allowed(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "DECLARED_VALUE",
                                         already_resolved_question=True,
                                         repeat_question=False))["status"],
                         "DIRECT_DECLARED_VALUE")

    def test_sensitive_self_report_must_not_be_published_automatically(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "REPORTED_FEELING",
                                         sensitive_type="MENTAL_HEALTH",
                                         public_output=True))["status"],
                         "BLOCK_PUBLIC_PERSONAL_DATA")

    def test_private_nonpublic_meta_analysis_permitted(self):
        self.assertEqual(review(Evidence("CURRENT_DIRECT_REPORT", "REPORTED_FEELING",
                                         sensitive_type="MENTAL_HEALTH",
                                         public_output=False))["status"],
                         "DIRECT_EXPERIENCE_REPORT")

    def test_genetic_material_not_public_without_distinct_decision(self):
        self.assertEqual(review(Evidence("ARCHIVED_PRIMARY_USER_STATEMENT", "DECLARED_VALUE",
                                         sensitive_type="GENETIC",
                                         public_output=True))["status"],
                         "BLOCK_PUBLIC_PERSONAL_DATA")

    def test_causal_design_triggers_scoped_review_not_complete_mind_claim(self):
        self.assertEqual(review(Evidence("INDEPENDENT_CAUSAL_EVIDENCE", "LATENT_MOTIVE",
                                         independent_causal_design=True))["status"],
                         "REVIEW_DESIGN_AND_SCOPE")

    def test_fake_causal_flag_without_causal_source_is_rejected(self):
        self.assertEqual(review(Evidence("HYPOTHESIS", "LATENT_MOTIVE",
                                         independent_causal_design=True))["status"],
                         "HYPOTHESIS_NOT_CAUSAL_FACT")

    def test_not_a_personality_diagnostic_instrument(self):
        self.assertEqual(review(Evidence("INDEPENDENT_CAUSAL_EVIDENCE", "PERSONALITY_DIAGNOSIS",
                                         independent_causal_design=True))["status"],
                         "NOT_A_CLINICAL_INSTRUMENT")

    def test_no_direct_emotion_attributed_to_assistant_restatement(self):
        self.assertEqual(review(Evidence("ASSISTANT_SUMMARY", "REPORTED_FEELING"))["status"],
                         "FEELING_NOT_DIRECTLY_ESTABLISHED")

    def test_unknown_source_is_hard_error(self):
        with self.assertRaises(ValueError):
            review(Evidence("GUESS", "DECLARED_VALUE"))

    def test_unknown_claim_is_hard_error(self):
        with self.assertRaises(ValueError):
            review(Evidence("CURRENT_DIRECT_REPORT", "TELEPATHY"))

    def test_unknown_sensitive_type_is_hard_error(self):
        with self.assertRaises(ValueError):
            review(Evidence("CURRENT_DIRECT_REPORT", "REPORTED_FEELING",
                            sensitive_type="UNKNOWN_CATEGORY"))

    def test_synthetic_batch_produces_only_scoped_metadata(self):
        rows = assess_case([
            Evidence("CURRENT_DIRECT_REPORT", "DECLARED_VALUE"),
            Evidence("ASSISTANT_SUMMARY", "EXACT_HISTORICAL_ATTRIBUTION"),
            Evidence("CURRENT_DIRECT_REPORT", "BIOLOGICAL_CAUSE"),
        ])
        self.assertEqual([r["status"] for r in rows],
                         ["DIRECT_DECLARED_VALUE", "UNVERIFIED_DATE_OR_QUOTE",
                          "HYPOTHESIS_NOT_CAUSAL_FACT"])


if __name__ == "__main__":
    unittest.main()
