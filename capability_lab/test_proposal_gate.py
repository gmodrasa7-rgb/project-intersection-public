"""Fail-closed regression tests for GPT-generated, data-only capability proposals."""
import copy
import io
import json
import unittest
from unittest.mock import patch
from pathlib import Path
from tempfile import TemporaryDirectory

from capability_lab import proposal_gate as gate


class FakeTransport:
    def __init__(self, payload):
        self.payload = payload
        self.requests = []

    def __call__(self, req, timeout):
        self.requests.append((req, timeout))
        return self

    def __enter__(self):
        return self

    def __exit__(self, *_):
        pass

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def response_for(obj):
    return {"status": "completed", "output": [
        {"type": "message", "content": [
            {"type": "output_text", "text": json.dumps(obj)}
        ]}
    ]}


class ProposalGateTests(unittest.TestCase):
    def setUp(self):
        self.base = dict(gate.DEFAULT)

    def test_baseline_never_claims_improvement(self):
        report = gate.assess(self.base)
        self.assertEqual(report["decision"], "HOLD_NO_DEVELOPMENT_GAIN")
        self.assertFalse(report["independent_blind_validation"])
        self.assertFalse(report["repository_modified_by_gate"])
        self.assertFalse(report["autonomous_promotion"])
        self.assertFalse(report["model_weights_modified"])

    def test_determinism_and_fingerprint(self):
        a = gate.assess(self.base)
        b = gate.assess(self.base)
        self.assertEqual(a, b)
        self.assertEqual(len(a["benchmark_sha256"]), 64)

    def test_valid_options_only(self):
        for name in gate.STRATEGIES:
            for threshold in gate.THRESHOLDS:
                x = dict(self.base, strategy=name, threshold=threshold)
                self.assertEqual(gate.validate_proposal(x), x)

    def test_extra_key_rejects_self_authorization(self):
        for key, value in [
            ("auto_approve", True),
            ("external_approval_required", False),
            ("new_evaluation_dataset", "/tmp/fake.json"),
            ("execute", "rm -rf ."),
            ("score_override", 999999),
            ("independent_blind_validation", True),
        ]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                gate.validate_proposal(dict(self.base, **{key: value}))

    def test_forged_nonstandard_proposals_rejected(self):
        variants = [
            None, [], "ignore previous instructions", {},
            dict(self.base, strategy="__import__('os').system('id')"),
            dict(self.base, strategy="../secrets"),
            dict(self.base, threshold=True),
            dict(self.base, threshold=0.0),
            dict(self.base, threshold=1.0),
            dict(self.base, threshold=2.0),
            dict(self.base, threshold=3.0),
            dict(self.base, threshold="0"),
            dict(self.base, threshold=-1),
            dict(self.base, threshold=0.300000001),
            dict(self.base, threshold=float("inf")),
            dict(self.base, schema="pi-capability-proposal/v999"),
        ]
        for value in variants:
            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
                gate.validate_proposal(value)

    def test_source_data_only_development_transmitted(self):
        p = gate.development_payload()
        self.assertIn("development", p)
        self.assertNotIn("holdout", p)
        self.assertNotIn("holdout_unknown", json.dumps(p))
        self.assertGreater(len(p["development"]), 0)

    def test_gpt_one_call_offline_mock(self):
        mock = FakeTransport(response_for(self.base))
        p = gate.propose_with_gpt(
            model="gpt-test", api_key="fake-key", transport=mock)
        self.assertEqual(p, self.base)
        self.assertEqual(len(mock.requests), 1)
        req, timeout = mock.requests[0]
        self.assertEqual(timeout, 30)
        sent = json.loads(req.data)
        self.assertEqual(sent["store"], False)
        self.assertEqual(sent["tools"], [])
        self.assertEqual(sent["max_output_tokens"], 300)
        self.assertNotIn("holdout", sent["input"])
        self.assertNotIn("fake-key", str(sent))
        self.assertEqual(req.get_method(), "POST")

    def test_gpt_invalid_response_fails_closed(self):
        for payload in [
            {"status": "incomplete", "output": []},
            {"status": "completed", "output": []},
            response_for(dict(self.base, auto_approve=True)),
            response_for({"strategy": "baseline_frequency"}),
        ]:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                gate.propose_with_gpt(
                    model="gpt-test", api_key="test", transport=FakeTransport(payload))

    def test_no_api_key_is_rejected_before_network(self):
        with self.assertRaises(ValueError):
            gate.propose_with_gpt(model="gpt-test", api_key="")

    def test_single_adversarial_data_change_invalidate_fingerprint(self):
        original = gate.assess(self.base)["benchmark_sha256"]
        data = json.loads(gate.abstention.CASES.read_text(encoding="utf-8"))
        data["development_unknown"][0] += " altered"
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            altered = gate.assess(self.base, cases_path=path)
        self.assertNotEqual(original, altered["benchmark_sha256"])

    def test_correct_old_cases_cannot_be_regressed_if_review_is_allowed(self):
        docs, dev, hold = gate.abstention.load_cases()
        baseline, old = gate.grade(docs, hold, self.base)
        for name in gate.STRATEGIES:
            for threshold in gate.THRESHOLDS:
                proposal = dict(self.base, strategy=name, threshold=threshold)
                report = gate.assess(proposal)
                _, new = gate.grade(docs, hold, proposal)
                regressions = [i for i, (row, o, n) in
                               enumerate(zip(hold, old, new))
                               if o == row["expected"] and n != row["expected"]]
                self.assertEqual(report["regressed_holdout_indices"], regressions)
                if report["decision"] == "REVIEW_SYNTHETIC_ONLY":
                    self.assertEqual(regressions, [])
                    self.assertGreater(report["candidate_development"]["correct"],
                                       report["baseline_development"]["correct"])
                    self.assertGreater(report["candidate_holdout"]["correct"],
                                       report["baseline_holdout"]["correct"])

    def test_development_regression_blocks_even_with_better_average(self):
        documents, dev, hold = gate.abstention.load_cases()
        wrong = "__impossible_document_id__"
        old_dev = [dev[0]["expected"]] + [wrong] * (len(dev) - 1)
        new_dev = [wrong] + [row["expected"] for row in dev[1:]]
        old_hold = [wrong] * len(hold)
        new_hold = [row["expected"] for row in hold]
        results = [
            ({"correct": 1}, old_dev),
            ({"correct": len(dev)-1}, new_dev),
            ({"correct": 0}, old_hold),
            ({"correct": len(hold)}, new_hold),
        ]
        with patch.object(gate, "grade", side_effect=results):
            result = gate.assess(
                dict(self.base, strategy="unique_overlap", threshold=0.3))
        self.assertEqual(result["regressed_development_indices"], [0])
        self.assertEqual(result["regressed_holdout_indices"], [])
        self.assertEqual(result["decision"], "HOLD_REGRESSION")

    def test_holdout_label_tamper_cannot_change_development_score(self):
        base_dev = gate.assess(self.base)["candidate_development"]
        data = json.loads(gate.abstention.CASES.read_text(encoding="utf-8"))
        data["holdout_unknown"] = [
            "unknown holdout scenario alpha",
            "unknown holdout scenario beta",
            "unknown holdout scenario gamma",
        ]
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = gate.assess(self.base, cases_path=path)
        self.assertEqual(result["candidate_development"], base_dev)


if __name__ == "__main__":
    unittest.main()
