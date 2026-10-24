"""Negative mutation tests: literature transfer cannot self-certify field efficacy."""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import pi_flr_action_gate as gate


class ActionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / gate.ACTION).read_text(encoding="utf-8"))
        cls.registry = json.loads((ROOT / gate.REGISTRY).read_text(encoding="utf-8"))
        cls.workflow = (ROOT / gate.WORKFLOW).read_text(encoding="utf-8")

    def validate(self, data):
        return gate.validate(data, self.registry, self.workflow)

    def reject(self, data, code):
        with self.assertRaisesRegex(gate.ActionError, code):
            self.validate(data)

    def test_current_design_valid_without_effectiveness_claim(self):
        report = self.validate(self.data)
        self.assertEqual(report["status"], "DESIGN_TRANSFER_ONLY_NOT_FIELD_VERIFIED")
        self.assertEqual(report["pilot_actions"], 2)
        self.assertEqual(report["metric_contract_count"], 2)
        self.assertFalse(report["rate_efficacy_certified"])
        self.assertFalse(report["population_completeness_certified"])
        self.assertEqual(report["census_event_count"], 0)
        self.assertEqual(report["untriaged_case_count"], len(self.registry["cases"]) - 2)
        self.assertEqual(report["field_effectiveness_verified"], 0)

    def test_no_false_field_success(self):
        d = copy.deepcopy(self.data)
        d["status_policy"]["field_effectiveness_certified"] = True
        self.reject(d, "FALSE_CERTIFICATION")

    def test_unknown_denominator_not_zero(self):
        d = copy.deepcopy(self.data)
        d["status_policy"]["no_exposure"] = "ZERO"
        self.reject(d, "MISSINGNESS")

    def test_no_imaginary_confidential_channel(self):
        d = copy.deepcopy(self.data)
        d["status_policy"]["near_miss_channel"] = "CONFIDENTIAL_ACTIVE"
        self.reject(d, "MISSINGNESS")

    def test_correlated_sources_not_independent_support(self):
        d = copy.deepcopy(self.data)
        d["intersection"][0]["sources"] = ["A01", "A01"]
        self.reject(d, "NOT_INDEPENDENT")

    def test_counterexample_must_survive(self):
        d = copy.deepcopy(self.data)
        d["intersection"][0]["counterexample_ko"] = ""
        self.reject(d, "COUNTEREXAMPLE_LOST")

    def test_pilot_must_map_true_case_control(self):
        d = copy.deepcopy(self.data)
        d["pilot_actions"][0]["control_id"] = "FLR-C12"
        self.reject(d, "INCORRECT_CONTROL")

    def test_pilot_must_keep_real_numerator_definition(self):
        d = copy.deepcopy(self.data)
        d["pilot_actions"][1]["eligible_denominator_ko"] = ""
        self.reject(d, "ACTION_NOT_TESTABLE")

    def test_observation_without_exposure_is_rejected(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["eligible"] = 0
        obs["event_census"] = []
        d["observations"].append(obs)
        self.reject(d, "MISSING_EXPOSURE_DENOMINATOR")

    def test_observation_without_receipt_is_rejected(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["eligible"] = 5
        obs["evidence_urls"] = []
        d["observations"].append(obs)
        self.reject(d, "UNVERIFIABLE_OBSERVATION_RECEIPT")

    def test_historical_observations_cannot_be_deleted(self):
        prior = copy.deepcopy(self.data)
        prior["observations"] = [{"id": "FLR-O0001", "historic": True}]
        newer = copy.deepcopy(self.data)
        newer["release_version"] = "0.2.0"
        with self.assertRaisesRegex(gate.ActionError, "ACTION_HISTORY_REWRITTEN"):
            gate.compare_history(newer, prior)

    def test_same_version_change_fails(self):
        newer = copy.deepcopy(self.data)
        newer["source_limit"] += " 임의의 수정"
        with self.assertRaisesRegex(gate.ActionError, "UNVERSIONED_ACTION_CHANGE"):
            gate.compare_history(newer, self.data)

    def test_cannot_remove_recognized_p0_pilot(self):
        d = copy.deepcopy(self.data)
        d["pilot_actions"] = d["pilot_actions"][:1]
        self.reject(d, "P0_FALSE_GREEN_PILOTS_REMOVED")


    def _sample_observation(self):
        return {
            "id": "FLR-O0001", "action_id": "FLR-A001",
                        "unit": "RELEASE_READINESS_DECISION",
            "status": "OBSERVED_NOT_EFFECTIVENESS_CERTIFIED",
            "window": "2026-10", "eligible": 1, "recurrences": 0,
            "false_blocks": None, "human_review_minutes": None,
            "evidence_urls": [
                "https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/123"
            ],
            "census_coverage": "BOUNDED_SAMPLE_POPULATION_UNKNOWN",
            "event_census": [{
                "event_id": "claim:PR123:decision-1",
                "unit": "RELEASE_READINESS_DECISION",
                "outcome": "NO_FALSE_GREEN_OBSERVED",
                "evidence_url":
                    "https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/123"
            }],
            "limitation": "외부 실행이 존재해도 효과와 노출 분모는 독립 검증되지 않았다."
        }

    def test_forged_run_url_never_passes_just_by_shape(self):
        d = copy.deepcopy(self.data)
        d["observations"].append(self._sample_observation())
        with patch.object(gate, "_verified_github_run", return_value=False):
            self.reject(d, "OBSERVED_RECEIPT_REMOTE_UNVERIFIED_NOT_ABSENT")

    def test_synthetic_positive_receipt_never_certifies_effectiveness(self):
        d = copy.deepcopy(self.data)
        d["observations"].append(self._sample_observation())
        with patch.object(gate, "_verified_github_run", return_value=True):
            report = self.validate(d)
        self.assertEqual(report["observations"], 1)
        self.assertEqual(report["field_effectiveness_verified"], 0)
        self.assertEqual(report["status"], "DESIGN_TRANSFER_ONLY_NOT_FIELD_VERIFIED")

    def test_remote_receipt_checks_id_repo_date_and_completed_status(self):
        url = self._sample_observation()["evidence_urls"][0]
        valid = {
            "id": 123, "repository": {"full_name": "gmodrasa7-rgb/project-intersection-public"},
            "html_url": url, "status": "completed",
            "created_at": "2026-10-24T03:00:00Z"
        }
        class Response:
            status = 200
            def __init__(self, payload):
                self.payload = payload
            def __enter__(self):
                return self
            def __exit__(self, *_):
                return False
            def read(self, n):
                return json.dumps(self.payload).encode("utf-8")

        with patch.object(gate, "urlopen", return_value=Response(valid)):
            self.assertTrue(gate._verified_github_run(url, "2026-10"))
        for key, altered in (("id", 124),
                             ("repository", {"full_name": "another/repo"}),
                             ("status", "in_progress"),
                             ("created_at", "2026-09-24T03:00:00Z"),
                             ("html_url", "https://github.com/another/repo/actions/runs/123")):
            bad = copy.deepcopy(valid)
            bad[key] = altered
            with patch.object(gate, "urlopen", return_value=Response(bad)):
                self.assertFalse(gate._verified_github_run(url, "2026-10"))

    def test_api_denial_is_unverified_not_fabricated_absence(self):
        url = self._sample_observation()["evidence_urls"][0]
        with patch.object(gate, "urlopen", side_effect=OSError("403 or 429")):
            self.assertFalse(gate._verified_github_run(url, "2026-10"))
        self.assertFalse(gate._verified_github_run(
            "https://github.com/gmodrasa7-rgb/project-intersection-public/pull/123",
            "2026-10"))
        self.assertFalse(gate._verified_github_run(url + "?spoof=1", "2026-10"))



    def test_receipt_network_target_fixed_and_lookalike_hosts_blocked(self):
        url = self._sample_observation()["evidence_urls"][0]
        with patch.object(gate, "urlopen", side_effect=OSError("temporary outage")) as net:
            self.assertFalse(gate._verified_github_run(url, "2026-10"))
            req = net.call_args.args[0]
            self.assertEqual(req.full_url,
                "https://api.github.com/repos/gmodrasa7-rgb/"
                "project-intersection-public/actions/runs/123")
            self.assertEqual(net.call_args.kwargs["timeout"], 10)
        with patch.object(gate, "urlopen") as net:
            self.assertFalse(gate._verified_github_run(
                "https://github.com.evil.example/gmodrasa7-rgb/"
                "project-intersection-public/actions/runs/123", "2026-10"))
            self.assertFalse(gate._verified_github_run(
                "https://github.com@evil.example/gmodrasa7-rgb/"
                "project-intersection-public/actions/runs/123", "2026-10"))
            self.assertFalse(gate._verified_github_run(url + "/attempts/1", "2026-10"))
            net.assert_not_called()


    def test_former_workflow_count_denominator_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["metric_contracts"][0]["denominator_unit"] = "WORKFLOW_CHECK"
        self.reject(d, "INCOMMENSURATE_RATE_UNITS")

    def test_mixed_unit_numerator_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["metric_contracts"][0]["numerator_unit"] = "FAILED_RELEASE_CLAIM"
        self.reject(d, "INCOMMENSURATE_RATE_UNITS")

    def test_missing_metric_contract_and_legacy_mislabel_rejected(self):
        d = copy.deepcopy(self.data)
        d["metric_contracts"].pop()
        self.reject(d, "RATE_CONTRACTS_INCOMPLETE")
        d = copy.deepcopy(self.data)
        d["metric_contracts"][0]["legacy_denominator_status"] = (
            "COMPATIBLE_UNIT_NOT_FIELD_VALIDATED")
        self.reject(d, "LEGACY_DENOMINATOR_MISLABELED")

    def test_observation_must_use_action_specific_event_units(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["unit"] = "WORKFLOW_CHECK"
        d["observations"].append(obs)
        self.reject(d, "OBSERVATION_DENOMINATOR_UNIT_MISMATCH")
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["action_id"] = "FLR-A002"
        d["observations"].append(obs)
        self.reject(d, "OBSERVATION_DENOMINATOR_UNIT_MISMATCH")

    def test_metric_contract_history_is_append_only(self):
        old = copy.deepcopy(self.data)
        newer = copy.deepcopy(old)
        newer["release_version"] = "0.3.0"
        newer["metric_contracts"][0]["denominator_definition_ko"] = (
            "워크플로 수로 계산하라 — 잘못된 단위 변경")
        with self.assertRaisesRegex(gate.ActionError,
                                    "ACTION_HISTORY_REWRITTEN"):
            gate.compare_history(newer, old)


    def test_huge_free_form_denominator_fails_without_event_census(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["eligible"] = 1000000
        d["observations"].append(obs)
        self.reject(d, "CENSUS_COUNT_MISMATCH")

    def test_false_zero_when_event_marks_recurrence_is_rejected(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["event_census"][0]["outcome"] = "FALSE_GREEN_OBSERVED"
        d["observations"].append(obs)
        self.reject(d, "CENSUS_OUTCOME_COUNT_MISMATCH")

    def test_duplicate_event_identifier_cannot_inflate_denominator(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["eligible"] = 2
        obs["event_census"].append(copy.deepcopy(obs["event_census"][0]))
        d["observations"].append(obs)
        self.reject(d, "CENSUS_DUPLICATE_OR_REUSED_EVENT")

    def test_duplicate_event_across_observations_is_not_new_exposure(self):
        d = copy.deepcopy(self.data)
        one = self._sample_observation()
        two = copy.deepcopy(one)
        two["id"] = "FLR-O0002"
        d["observations"] = [one, two]
        with patch.object(gate, "_verified_github_run", return_value=True):
            self.reject(d, "CENSUS_DUPLICATE_OR_REUSED_EVENT")

    def test_census_event_must_be_backed_by_declared_receipt(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["event_census"][0]["evidence_url"] = (
            "https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/999")
        d["observations"].append(obs)
        self.reject(d, "CENSUS_EVENT_MISSING_SOURCE")

    def test_unsupported_outcome_and_cross_action_units_rejected(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["event_census"][0]["outcome"] = "UNMAPPED_FAILURE"
        d["observations"].append(obs)
        self.reject(d, "CENSUS_OUTCOME_INCOMPATIBLE")
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["event_census"][0]["unit"] = "MATERIAL_CHANGED_PATH"
        d["observations"].append(obs)
        self.reject(d, "CENSUS_UNIT_MISMATCH")

    def test_claimed_complete_population_is_not_certified(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["census_coverage"] = "COMPLETE_POPULATION"
        d["observations"].append(obs)
        self.reject(d, "CENSUS_POPULATION_FALSE_COMPLETENESS")
        d = copy.deepcopy(self.data)
        d["census_policy"]["rate_permission"] = "RATE_VERIFIED"
        self.reject(d, "CENSUS_PROVENANCE_OVERCLAIM")

    def test_enumerated_events_with_matching_counts_remain_noncausal(self):
        d = copy.deepcopy(self.data)
        obs = self._sample_observation()
        obs["eligible"] = 2
        obs["recurrences"] = 1
        extra = copy.deepcopy(obs["event_census"][0])
        extra["event_id"] = "claim:PR124:decision-2"
        extra["outcome"] = "FALSE_GREEN_OBSERVED"
        obs["event_census"].append(extra)
        d["observations"].append(obs)
        with patch.object(gate, "_verified_github_run", return_value=True):
            report = self.validate(d)
        self.assertEqual(report["census_event_count"], 2)
        self.assertEqual(report["field_effectiveness_verified"], 0)
        self.assertFalse(report["population_completeness_certified"])
        self.assertFalse(report["rate_efficacy_certified"])


if __name__ == "__main__":
    unittest.main()
