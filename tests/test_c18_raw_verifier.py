"""Adversarial checks of C18 code using generated, explicitly synthetic data.

Fixture hash pins are overridden ONLY inside individual tests. Passing these
tests is not a download, provenance attestation or replication of the source ZIP.
The public verifier and its original source-package hashes remain unchanged.
"""
import contextlib
import csv
import hashlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import verify_c18_hung_2025_raw as verifier


def synthetic_tables():
    field = []
    for code, n, calls, scans in (
        (1, 164, 104, 116), (2, 167, 102, 115),
        (3, 162, 106, 116), (4, 165, 78, 89),
    ):
        field.extend({"assigned": "1", "treatment": str(code),
                      "firstcall": str(int(i < calls)),
                      "scan": str(int(i < scans))} for i in range(n))
    # Deliberately extreme outcomes must be excluded by assigned=0.
    field.extend({"assigned": "0", "treatment": str(code),
                  "firstcall": "1", "scan": "1"} for code in (1, 3))
    online1 = []
    for code, n in ((1, 246), (2, 231), (3, 235), (4, 248)):
        online1.extend({"treatment": str(code), "duplicateIPpass1": "1",
                        "moneycheckinteger10": "1"} for _ in range(n))
    online1.extend({"treatment": "1", "duplicateIPpass1": "0" if i % 2 else "1",
                    "moneycheckinteger10": "1" if i % 2 else "0"} for i in range(83))
    online2 = [{"duplicateIPpass1": "1.00", "moneycheckinteger10": "1.00"}
               for _ in range(1496)]
    online2.extend({"duplicateIPpass1": "0.00" if i % 2 else "1.00",
                    "moneycheckinteger10": "1.00" if i % 2 else "0.00"}
                   for i in range(174))
    return {"FieldExperiment.csv": field, "OnlineExperiment1.csv": online1,
            "OnlineExperiment2.csv": online2}


def synthetic_zip(tables):
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as archive:
        for name, rows in tables.items():
            text = io.StringIO(newline="")
            writer = csv.DictWriter(text, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
            archive.writestr(verifier.DATA_FOLDER + name,
                             text.getvalue().encode("utf-8-sig"))
    return data.getvalue()


class C18RawVerifierTests(unittest.TestCase):
    def check_fixture(self, tables):
        payload = synthetic_zip(tables)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "SYNTHETIC_TEST_ONLY.zip"
            path.write_bytes(payload)
            with mock.patch.object(verifier, "EXPECTED_SHA256", hashlib.sha256(payload).hexdigest()), \
                 mock.patch.object(verifier, "EXPECTED_MD5", hashlib.md5(payload).hexdigest()), \
                 contextlib.redirect_stdout(io.StringIO()) as output:
                verifier.verify(path)
            return output.getvalue()

    def test_pearson_known_independent_reference(self):
        chi, p = verifier.pearson_2x2_p(30, 50, 20, 50)
        self.assertAlmostEqual(chi, 4.0, places=12)
        self.assertAlmostEqual(p, 0.04550026389635842, places=12)

    def test_pearson_arm_and_outcome_reversal_preserve_significance(self):
        result = verifier.pearson_2x2_p(78, 165, 104, 164)
        for args in ((104, 164, 78, 165), (87, 165, 60, 164)):
            chi, p = verifier.pearson_2x2_p(*args)
            self.assertAlmostEqual(chi, result[0], places=12)
            self.assertAlmostEqual(p, result[1], places=12)

    def test_valid_synthetic_counts_and_adverse_directions(self):
        output = self.check_fixture(synthetic_tables())
        self.assertIn("phone call: -16.1419 pp", output)
        self.assertIn("QR scan: -16.7923 pp", output)
        self.assertIn("raw=1043, quality-filtered=960", output)
        self.assertIn("raw=1670, quality-filtered=1496", output)
        self.assertIn("Unresolved publication label", output)

    def test_real_package_sha_pin_rejects_bytes_before_zip_parsing(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "not-the-original.zip"
            path.write_bytes(b"synthetic tampered bytes")
            with mock.patch.object(verifier.zipfile, "ZipFile") as parser:
                with self.assertRaisesRegex(AssertionError, "SHA-256 mismatch"):
                    verifier.verify(path)
                parser.assert_not_called()

    def test_md5_is_checked_even_when_sha_matches(self):
        payload = synthetic_zip(synthetic_tables())
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "synthetic.zip"
            path.write_bytes(payload)
            with mock.patch.object(verifier, "EXPECTED_SHA256", hashlib.sha256(payload).hexdigest()):
                with self.assertRaisesRegex(AssertionError, "Zenodo MD5 mismatch"):
                    verifier.verify(path)

    def test_missing_field_row_rejected(self):
        data = synthetic_tables()
        data["FieldExperiment.csv"].pop()
        with self.assertRaises(AssertionError):
            self.check_fixture(data)

    def test_unassigned_row_cannot_enter_analysis(self):
        data = synthetic_tables()
        data["FieldExperiment.csv"][-1]["assigned"] = "1"
        with self.assertRaises(AssertionError):
            self.check_fixture(data)

    def test_arm_denominator_drift_rejected(self):
        data = synthetic_tables()
        data["FieldExperiment.csv"][0]["treatment"] = "4"
        with self.assertRaises(AssertionError):
            self.check_fixture(data)

    def test_phone_numerator_drift_rejected(self):
        data = synthetic_tables()
        data["FieldExperiment.csv"][0]["firstcall"] = "0"
        with self.assertRaises(AssertionError):
            self.check_fixture(data)

    def test_qr_numerator_drift_rejected(self):
        data = synthetic_tables()
        data["FieldExperiment.csv"][0]["scan"] = "0"
        with self.assertRaises(AssertionError):
            self.check_fixture(data)

    def test_online1_both_quality_filters_are_required(self):
        for index, column in ((960, "moneycheckinteger10"), (961, "duplicateIPpass1")):
            with self.subTest(column=column):
                data = synthetic_tables()
                data["OnlineExperiment1.csv"][index][column] = "1"
                with self.assertRaises(AssertionError):
                    self.check_fixture(data)

    def test_online1_cell_counts_cannot_hide_behind_total(self):
        data = synthetic_tables()
        data["OnlineExperiment1.csv"][0]["treatment"] = "2"
        with self.assertRaises(AssertionError):
            self.check_fixture(data)

    def test_online2_both_quality_filters_are_required(self):
        for index, column in ((1496, "moneycheckinteger10"), (1497, "duplicateIPpass1")):
            with self.subTest(column=column):
                data = synthetic_tables()
                data["OnlineExperiment2.csv"][index][column] = "1.00"
                with self.assertRaises(AssertionError):
                    self.check_fixture(data)

    def test_missing_csv_member_rejected(self):
        data = synthetic_tables()
        del data["OnlineExperiment2.csv"]
        with self.assertRaises(KeyError):
            self.check_fixture(data)


if __name__ == "__main__":
    unittest.main()
