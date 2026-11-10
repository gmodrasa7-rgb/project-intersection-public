#!/usr/bin/env python3
"""Independent aggregate-only reproduction of Bartling et al., Free to Fail?

Input: the author's unmodified Zenodo 3-replication-package.zip, obtained from
https://doi.org/10.5281/zenodo.23420381.  No respondent records are printed,
written, extracted, or uploaded.  Requires Python 3.10+ and NumPy.

This is NOT execution of the author's Stata programs, a new experiment,
or an independent replication sample.  It reconstructs eight headline OLS
specifications and heteroskedasticity-robust HC1 standard errors independently.
"""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import zipfile

import numpy as np


AUTHOR_ZIP_MD5 = "7f1ebe690e3704d8ba81409626834b77"

RESTRICT = (
    "Restrict choice: The person will not have the opportunity to make a choice "
    "and will receive the safe option."
)
NORESTRICT = (
    "Do not restrict choice: The person will have the opportunity to make a "
    "choice between the safe and the risky option."
)
INFO = (
    "Provide information: The person will be informed about the correct "
    "likelihoods of the two outcomes in the risky option before he or she "
    "makes a choice between the safe and the risky option."
)
NOINFO = (
    "Do not provide information: The person will receive no additional "
    "information before he or she makes a choice between the safe and the risky option."
)
FORCE_SAFE = (
    "Restrict choice to safe option: The person will not have the opportunity "
    "to make a choice and will receive the safe option."
)
FORCE_RISKY = (
    "Restrict choice to risky option: The person will not have the opportunity "
    "to make a choice and will receive the risky option."
)

CELLS = {
    1: {1: ("q134", RESTRICT, NORESTRICT), 2: ("q128", INFO, NOINFO),
        3: ("q122", RESTRICT, NORESTRICT), 4: ("q75", INFO, NOINFO)},
    2: {1: ("q134", RESTRICT, NORESTRICT), 2: ("q128", INFO, NOINFO),
        5: ("q154", FORCE_SAFE, FORCE_RISKY)},
}
CONTROLS = ("female", "ageH", "educationH", "incomeH", "riskH", "republican")
INCOME_HIGH = {"$60,000 to $99,999", "$100,000 to $149,999", "$150,000 and over"}
INCOME_LOW = {"Less than $29,999", "$30,000 to $59,999"}
EDU_HIGH = {"Associate", "Bachelor", "Master", "Prof", "phd"}
EDU_LOW = {"nohighs", "highs", "somecollege"}


def classify(row: dict[str, str], study: int) -> tuple[int, int]:
    """Fail closed on missing, ambiguous or changed Qualtrics wording."""
    found = [(cell, pos, neg, row.get(col, ""))
             for cell, (col, pos, neg) in CELLS[study].items()
             if row.get(col, "") != ""]
    if len(found) != 1:
        raise ValueError("Expected exactly one answered intervention screen")
    cell, positive, negative, answer = found[0]
    if answer not in (positive, negative):
        raise ValueError("Unexpected response text; do not guess outcome")
    return cell, int(answer == positive)


def load_study(archive: zipfile.ZipFile, study: int):
    name = f"raw_data/paternalism_study{study}_raw.csv"
    with archive.open(name) as binary:
        with io.TextIOWrapper(binary, encoding="utf-8-sig", newline="") as stream:
            all_rows = list(csv.DictReader(stream))
    rows = [row for row in all_rows
            if row["consent"] != "No" and row["q102"] != ""]
    ages = np.asarray([int(row["q92"]) for row in rows], dtype=float)
    risks = np.asarray([float(row["q100_1"]) for row in rows], dtype=float)
    if not (np.isfinite(ages).all() and np.isfinite(risks).all()):
        raise ValueError("Age/risk missing: published median-split sample changed")
    median_age, median_risk = np.median(ages), np.median(risks)
    data = []
    counts = {str(i): {"yes": 0, "n": 0} for i in CELLS[study]}
    for row in rows:
        cell, y = classify(row, study)
        counts[str(cell)]["yes"] += y
        counts[str(cell)]["n"] += 1
        if row["q90"] not in ("Male", "Female"):
            raise ValueError("Unmapped gender in published control model")
        if row["q96"] not in EDU_LOW | EDU_HIGH:
            raise ValueError("Unmapped education in published control model")
        if row["q98"] not in INCOME_LOW | INCOME_HIGH:
            raise ValueError("Unmapped income in published control model")
        data.append({
            "intervention": y, "Tsoft": int(cell in (2, 4)),
            "Text": int(cell in (3, 4)), "Thard": int(cell == 1),
            "TsoftText": int(cell == 4),
            "female": int(row["q90"] == "Female"),
            "ageH": int(int(row["q92"]) > median_age),
            "educationH": int(row["q96"] in EDU_HIGH),
            "incomeH": int(row["q98"] in INCOME_HIGH),
            "riskH": int(float(row["q100_1"]) > median_risk),
            "republican": int(row["q102"] == "Republican"),
        })
    return data, counts, {"imported": len(all_rows), "retained": len(rows)}


def ols_hc1(data: list[dict], regressors: list[str]) -> dict:
    y = np.asarray([row["intervention"] for row in data], dtype=float)
    x = np.asarray([[1] + [row[key] for key in regressors] for row in data], dtype=float)
    n, k = x.shape
    inv = np.linalg.inv(x.T @ x)
    beta = inv @ (x.T @ y)
    residual = y - x @ beta
    cov = inv @ ((x.T * residual**2) @ x) @ inv * (n / (n - k))
    se = np.sqrt(np.diag(cov))
    r2 = 1 - float(residual @ residual) / float((y - y.mean()) @ (y - y.mean()))
    names = ["_cons", *regressors]
    return {"n": n, "r2": r2, "beta": dict(zip(names, beta.tolist())),
            "se_HC1": dict(zip(names, se.tolist()))}


def latent_soft_only_bound(counts: dict) -> list[float]:
    hard = [counts[key] for key in counts if key in ("1", "3")]
    soft = [counts[key] for key in counts if key in ("2", "4")]
    p_h = sum(c["yes"] for c in hard) / sum(c["n"] for c in hard)
    p_s = sum(c["yes"] for c in soft) / sum(c["n"] for c in soft)
    return [max(0, p_s - p_h), min(p_s, 1 - p_h)]


def pooled_soft_minus_hard(counts: dict) -> dict:
    hard = [counts[key] for key in counts if key in ("1", "3")]
    soft = [counts[key] for key in counts if key in ("2", "4")]
    n_h, n_s = sum(c["n"] for c in hard), sum(c["n"] for c in soft)
    p_h, p_s = (sum(c["yes"] for c in hard) / n_h,
                sum(c["yes"] for c in soft) / n_s)
    n = n_h + n_s
    effect = p_s - p_h
    se = np.sqrt(n / (n - 2) *
                 (p_h * (1 - p_h) / n_h + p_s * (1 - p_s) / n_s))
    return {"effect": effect, "HC1_SE": float(se),
            "95CI_normal": [float(effect - 1.96 * se), float(effect + 1.96 * se)]}


def check_against_published(result: dict) -> None:
    """Pre-specified three-decimal checks against 2023 author Tables 2 and 3."""
    expected = {
        "s1_soft": {"_cons": .318, "Tsoft": .550},
        "s1_soft_controls": {"_cons": .329, "Tsoft": .550},
        "s1_external": {"_cons": .596, "Text": -.009},
        "s1_external_controls": {"_cons": .612, "Text": -.008},
        "s1_interaction": {"_cons": .335, "Tsoft": .524, "Text": -.035, "TsoftText": .051},
        "s1_interaction_controls": {"_cons": .347, "Tsoft": .524, "Text": -.035, "TsoftText": .051},
        "s2_welfare": {"_cons": .698, "Tsoft": .127, "Thard": -.344},
        "s2_welfare_controls": {"_cons": .711, "Tsoft": .128, "Thard": -.344},
    }
    for model, expected_coefficients in expected.items():
        for name, val in expected_coefficients.items():
            actual = round(result["models"][model]["beta"][name], 3)
            if actual != val:
                raise AssertionError(f"{model}.{name}: expected {val}, observed {actual}")
    expected_se = {
        "s1_soft": {"Tsoft": .009},
        "s1_soft_controls": {"Tsoft": .009},
        "s1_external": {"Text": .011},
        "s1_external_controls": {"Text": .011},
        "s1_interaction": {"Tsoft": .013, "Text": .015, "TsoftText": .018},
        "s1_interaction_controls": {"Tsoft": .013, "Text": .015, "TsoftText": .018},
        "s2_welfare": {"Tsoft": .013, "Thard": .015},
        "s2_welfare_controls": {"Tsoft": .013, "Thard": .015},
    }
    for model, errors in expected_se.items():
        for name, val in errors.items():
            actual = round(result["models"][model]["se_HC1"][name], 3)
            if actual != val:
                raise AssertionError(f"{model}.{name} SE: expected {val}, observed {actual}")
    if result["samples"]["1"]["retained"] != 8004:
        raise AssertionError("Study 1 unexpected sample size")
    if result["samples"]["2"]["retained"] != 6033:
        raise AssertionError("Study 2 unexpected sample size")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True,
                        help="Unmodified author's ZIP downloaded from Zenodo")
    args = parser.parse_args()
    if hashlib.md5(args.archive.read_bytes()).hexdigest() != AUTHOR_ZIP_MD5:
        raise SystemExit("AUTHOR_ARCHIVE_MD5_MISMATCH: refuse processing")
    result = {"source_doi": "10.5281/zenodo.23420381",
              "author_archive_md5_verified": True,
              "status": "AUTHOR_DATA_INDEPENDENT_REANALYSIS_NOT_NEW_SAMPLE",
              "samples": {}, "arms": {}, "models": {}, "contrasts": {},
              "latent_soft_only_point_bounds": {}}
    with zipfile.ZipFile(args.archive) as archive:
        for study in (1, 2):
            rows, counts, sample = load_study(archive, study)
            result["samples"][str(study)] = sample
            result["arms"][str(study)] = counts
            result["contrasts"][str(study)] = pooled_soft_minus_hard(counts)
            result["latent_soft_only_point_bounds"][str(study)] = latent_soft_only_bound(counts)
            if study == 1:
                models = {
                    "s1_soft": ["Tsoft"],
                    "s1_soft_controls": ["Tsoft", *CONTROLS],
                    "s1_external": ["Text"],
                    "s1_external_controls": ["Text", *CONTROLS],
                    "s1_interaction": ["Tsoft", "Text", "TsoftText"],
                    "s1_interaction_controls": ["Tsoft", "Text", "TsoftText", *CONTROLS],
                }
            else:
                models = {"s2_welfare": ["Tsoft", "Thard"],
                          "s2_welfare_controls": ["Tsoft", "Thard", *CONTROLS]}
            for name, predictors in models.items():
                result["models"][name] = ols_hc1(rows, predictors)
    # Negative controls: a forged option and two answered screens must fail.
    valid = {col: "" for col, *_ in CELLS[1].values()}
    valid["q134"] = "forged response"
    try:
        classify(valid, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative control failed: forged response accepted")
    valid["q134"] = RESTRICT
    valid["q128"] = INFO
    try:
        classify(valid, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative control failed: multiple screens accepted")
    check_against_published(result)
    result["published_2023_eight_ols_models"] = "MATCHED_COEFFICIENTS_TO_3_DECIMALS"
    result["negative_controls"] = "2_OF_2_REJECTED"
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
