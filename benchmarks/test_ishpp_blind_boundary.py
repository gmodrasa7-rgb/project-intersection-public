"""Negative controls for information leakage in the ISHPP public blind-phase file."""
import copy
import json
from pathlib import Path
import unittest

from validate_ishpp_blind import read_jsonl, validate

HERE = Path(__file__).resolve().parent


class BlindBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.blind = read_jsonl(HERE / "ISHPP_REAL_WORLD_BLIND_SET_v0_2.jsonl")
        cls.legacy = read_jsonl(HERE / "ISHPP_REAL_WORLD_BLIND_SET_v0_1.jsonl")
        cls.mapping = json.loads((HERE / "ISHPP_REAL_WORLD_CASE_SOURCES_v0_2.json").read_text(encoding="utf-8"))
        cls.registry = json.loads((HERE / "ISHPP_REAL_WORLD_SOURCE_MAP_v0_1.json").read_text(encoding="utf-8"))

    def errors(self, blind=None, mapping=None):
        return validate(
            self.blind if blind is None else blind,
            self.legacy,
            self.mapping if mapping is None else mapping,
            self.registry
        )

    def test_frozen_ten_cases_have_no_structural_source_leak(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(len(self.blind), 10)

    def test_source_ids_inside_blind_record_rejected(self):
        data = copy.deepcopy(self.blind)
        data[0]["source_ids"] = ["S001"]
        self.assertTrue(self.errors(blind=data))

    def test_hidden_source_id_in_case_text_rejected(self):
        data = copy.deepcopy(self.blind)
        data[0]["blind_case"] += " S001"
        self.assertTrue(self.errors(blind=data))

    def test_source_url_inside_blind_case_rejected(self):
        data = copy.deepcopy(self.blind)
        data[0]["blind_case"] += " https://example.org"
        self.assertTrue(self.errors(blind=data))

    def test_missing_case_rejected(self):
        self.assertTrue(self.errors(blind=self.blind[:-1]))

    def test_cherrypicked_rewording_rejected(self):
        data = copy.deepcopy(self.blind)
        data[0]["blind_case"] = "favorable simplified account"
        self.assertTrue(self.errors(blind=data))

    def test_missing_post_reveal_lineage_rejected(self):
        mapping = copy.deepcopy(self.mapping)
        del mapping["case_sources"]["RW001"]
        self.assertTrue(self.errors(mapping=mapping))

    def test_fabricated_source_rejected(self):
        mapping = copy.deepcopy(self.mapping)
        mapping["case_sources"]["RW001"] = ["S999"]
        self.assertTrue(self.errors(mapping=mapping))


if __name__ == "__main__":
    unittest.main()
