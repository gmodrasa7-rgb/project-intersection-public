#!/usr/bin/env python3
"""Reproduce C18 basic data checks from the original Hung (2025) ResearchBox ZIP.

Download: https://zenodo.org/records/15040071/files/ResearchBox_2291.zip
Run: python3 tools/verify_c18_hung_2025_raw.py path/to/ResearchBox_2291.zip
This is an independent basic arithmetic check, not a complete author-code rerun.
"""

import argparse
import csv
import hashlib
import io
import math
import zipfile
from collections import Counter
from pathlib import Path


EXPECTED_SHA256 = "48b977eee77ccf46d41fdb023161af1a159b421de6435da6774205b2306a7e7f"
EXPECTED_MD5 = "4ff43151200a5de547243e06452eba61"  # Zenodo record 15040071
DATA_FOLDER = "ResearchBox 2291/ Data/"


def read_csv(archive, filename):
    with archive.open(DATA_FOLDER + filename) as binary:
        return list(csv.DictReader(io.TextIOWrapper(binary, encoding="utf-8-sig", newline="")))


def pearson_2x2_p(success_a, total_a, success_b, total_b):
    """Uncorrected Pearson chi-square (df=1), upper-tail p-value."""
    a, b = success_a, total_a - success_a
    c, d = success_b, total_b - success_b
    n = a + b + c + d
    chi_sq = n * (a * d - b * c) ** 2 / ((a + b) * (c + d) * (a + c) * (b + d))
    return chi_sq, math.erfc(math.sqrt(chi_sq / 2))


def verify(zip_path):
    data = Path(zip_path).read_bytes()
    sha256 = hashlib.sha256(data).hexdigest()
    md5 = hashlib.md5(data).hexdigest()  # noqa: S324; provenance check only
    assert sha256 == EXPECTED_SHA256, f"SHA-256 mismatch: {sha256}"
    assert md5 == EXPECTED_MD5, f"Zenodo MD5 mismatch: {md5}"
    print(f"ZIP: {len(data)} bytes; SHA-256 and Zenodo MD5 matched")

    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        field = read_csv(archive, "FieldExperiment.csv")
        online_1 = read_csv(archive, "OnlineExperiment1.csv")
        online_2 = read_csv(archive, "OnlineExperiment2.csv")

    assert (len(field), len(online_1), len(online_2)) == (660, 1043, 1670)
    assigned = [row for row in field if row["assigned"] == "1"]
    assert len(assigned) == 658

    # Codebook: 1=control, 2=altruistic, 3=civic responsibility, 4=safety assurance.
    expected = {1: (164, 104, 116), 2: (167, 102, 115),
                3: (162, 106, 116), 4: (165, 78, 89)}
    counts = {}
    for code, (want_n, want_calls, want_scans) in expected.items():
        group = [row for row in assigned if int(row["treatment"]) == code]
        n = len(group)
        calls = sum(int(row["firstcall"]) for row in group)
        scans = sum(int(row["scan"]) for row in group)
        assert (n, calls, scans) == (want_n, want_calls, want_scans)
        counts[code] = (n, calls, scans)
        print(f"Field arm {code}: N={n}, calls={calls} ({calls/n:.4%}), "
              f"scans={scans} ({scans/n:.4%})")

    quality_1 = [row for row in online_1 if
                 row["duplicateIPpass1"] == "1" and row["moneycheckinteger10"] == "1"]
    quality_2 = [row for row in online_2 if
                 row["duplicateIPpass1"] == "1.00" and row["moneycheckinteger10"] == "1.00"]
    assert len(quality_1) == 960
    assert Counter(row["treatment"] for row in quality_1) == {
        "1": 246, "2": 231, "3": 235, "4": 248}
    assert len(quality_2) == 1496
    print("Online 1: raw=1043, quality-filtered=960; Figure 1 cell counts matched")
    print("Online 2: raw=1670, quality-filtered=1496; Figure 2 analysis N matched")
    print("Unresolved publication label: Online 1 Figure 1 says N=1052")

    control_n, control_calls, control_scans = counts[1]
    safe_n, safe_calls, safe_scans = counts[4]
    for label, safe_yes, control_yes in (
            ("phone call", safe_calls, control_calls),
            ("QR scan", safe_scans, control_scans)):
        chi_sq, p_value = pearson_2x2_p(safe_yes, safe_n, control_yes, control_n)
        effect_pp = 100 * (safe_yes / safe_n - control_yes / control_n)
        print(f"Safety vs control {label}: {effect_pp:+.4f} pp; "
              f"Pearson chi-square={chi_sq:.6f}; p={p_value:.9f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", help="Original ResearchBox_2291.zip from Zenodo")
    verify(parser.parse_args().zip_path)
