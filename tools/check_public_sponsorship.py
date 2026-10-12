#!/usr/bin/env python3
"""Public two-use sponsorship ledger integrity: read-only, offline, standard library.

This does NOT verify private transactions, taxation or legal fundraising status.
One canonical Markdown ledger is the ONLY public numeric sponsorship record.
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "funding/SPONSORSHIP_PUBLIC_LEDGER.md"
POLICY_LINK = ROOT / "funding/SPONSORSHIP_POLICY_2026-10-13_EN_KO.md"
INTRO = ROOT / "PUBLIC_LINKEDIN_INTRODUCTION_2026-10-13_EN_KO.md"
LEGAL = ROOT / "funding/LEGAL_TAX_RISK_REGISTER_2026-10-13_EN_KO.md"
BRIDGE = ROOT / "funding/30_DAY_BRIDGE.md"
CSV_OLD = ROOT / "funding/SPONSORSHIP_TRANSACTIONS_PUBLIC.csv"
FILES = [LEDGER, POLICY_LINK, INTRO, LEGAL, BRIDGE,
         ROOT / "README.md", ROOT / "START_HERE_KO.md",
         ROOT / "funding/README.md", ROOT / "funding/FUNDER_START_HERE.md"]
START = "<!-- VERIFIED_ROWS_START -->"
END = "<!-- VERIFIED_ROWS_END -->"
SPONSORS = "https://github.com/sponsors/gmodrasa7-rgb"


def relative_link_errors(path, content):
    out = []
    for url in re.findall(r"\]\(([^)]+)\)", content):
        url = url.split("#", 1)[0].strip().split(" ", 1)[0]
        if not url or "://" in url or url.startswith("mailto:"):
            continue
        target = (path.parent / url).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            out.append("Broken/escaping link in " + str(path.relative_to(ROOT)) + ": " + url)
    return out


def privacy_errors(path, content):
    out = []
    patterns = [
        (r"[\w.+-]+@(?:gmail|naver|daum|kakao|outlook)\.[\w.-]+", "personal email"),
        (r"(?<!\d)01[016789][ -]?\d{3,4}[ -]?\d{4}(?!\d)", "phone"),
        (r"(?<!\d)\d{6}[- ]?[1-4]\d{6}(?!\d)", "resident identifier"),
        (r"gh[pousr]_[A-Za-z0-9]{25,}", "credential"),
    ]
    for pattern, label in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            out.append("Possible " + label + " in " + str(path.relative_to(ROOT)))
    return out


def period_interval(value):
    m = re.fullmatch(r"(20\d\d)-(0[1-9]|1[0-2])", value)
    if m:
        n = int(m[1]) * 12 + int(m[2]) - 1
        return n, n
    q = re.fullmatch(r"(20\d\d)-Q([1-4])", value)
    if q:
        n = int(q[1]) * 12 + (int(q[2]) - 1) * 3
        return n, n + 2
    return None


def validate_rows(lines):
    failures = []
    previous_end = None
    previous_balance = None
    seen = set()
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        if not line.startswith("|") or not line.endswith("|"):
            failures.append("Non-table entry inside verified rows at line " + str(i))
            continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        if len(cells) != 8:
            failures.append("Expected exactly 8 columns at row " + str(i))
            continue
        period, opening, received, researcher, llm, closing, status, updated = cells
        interval = period_interval(period)
        if interval is None or period in seen:
            failures.append("Invalid/duplicate reporting period at row " + str(i))
        else:
            seen.add(period)
            if previous_end is not None and interval[0] <= previous_end:
                failures.append("Overlapping or out-of-order reporting periods at row " + str(i))
            previous_end = interval[1]
        if status != "VERIFIED":
            failures.append("Public transaction must have reconciled source VERIFIED at row " + str(i))
        try:
            date.fromisoformat(updated)
        except ValueError:
            failures.append("Expected YYYY-MM-DD update date at row " + str(i))
        vals = []
        for value in (opening, received, researcher, llm, closing):
            if not re.fullmatch(r"(0|[1-9]\d*)", value):
                failures.append("Amounts must be nonnegative KRW integer without grouping: row " + str(i))
                vals = []
                break
            vals.append(int(value))
        if len(vals) != 5:
            continue
        opening_v, received_v, researcher_v, llm_v, closing_v = vals
        if opening_v + received_v - researcher_v - llm_v != closing_v:
            failures.append("Ledger does not balance: row " + str(i))
        if previous_balance is not None and opening_v != previous_balance:
            failures.append("Opening must match previous closing: row " + str(i))
        previous_balance = closing_v
    return failures


def run():
    failures = []
    doc = {}
    for file in FILES:
        if not file.is_file():
            failures.append("Missing: " + str(file.relative_to(ROOT)))
            continue
        doc[file] = file.read_text(encoding="utf-8-sig")
    if CSV_OLD.exists():
        failures.append("Old duplicate public CSV still exists; single Markdown ledger required")
    for path in (LEDGER, POLICY_LINK, INTRO, LEGAL):
        text = doc.get(path, "")
        failures.extend(relative_link_errors(path, text))
        failures.extend(privacy_errors(path, text))
    ledger = doc.get(LEDGER, "")
    if ledger.count(START) != 1 or ledger.count(END) != 1:
        failures.append("Exactly one verified-row section is required")
        rows = []
    else:
        rows_part = ledger.split(START, 1)[1].split(END, 1)[0]
        rows = [x for x in rows_part.splitlines() if x.strip()]
        failures.extend(validate_rows(rows))
    expected_header = ("| Period / 기간 | Opening / 기초 (KRW) | Received / 실입금 (KRW) "
                       "| Researcher / 1인 인건비 (KRW) | LLM / 사용료 (KRW) "
                       "| Closing / 잔액 (KRW) | Source / 확인 | Updated / 갱신 |")
    if ledger.count(expected_header) != 1:
        failures.append("Single canonical two-use ledger header was changed or duplicated")
    if rows:
        if "Financial status / 금액 상태: UNVERIFIED" in ledger or "Status / 현재 상태: UNVERIFIED" in ledger:
            failures.append("Verified rows exist but page summary still claims UNVERIFIED")
    else:
        if "UNVERIFIED / 미확인" not in ledger:
            failures.append("Unreconciled funds must be clearly marked UNVERIFIED / 미확인")
    for phrase in ("연구자 1인 인건비", "LLM 사용료", "not confirmed zero", "미확인"):
        if phrase not in ledger:
            failures.append("Required ledger description missing: " + phrase)
    if SPONSORS not in ledger or SPONSORS not in doc.get(INTRO, ""):
        failures.append("Official GitHub Sponsors URL not in ledger/intro")
    if "SPONSORSHIP_PUBLIC_LEDGER.md" not in doc.get(POLICY_LINK, ""):
        failures.append("Historical policy must redirect to the single canonical ledger")
    if not all(s in doc.get(BRIDGE, "") for s in ("3,200", "1,000", "500", "300")):
        failures.append("Historic unawarded bridge budget was silently altered")
    if failures:
        for msg in failures:
            print("FAIL: " + msg, file=sys.stderr)
        return 1
    print("PASS: one two-category public ledger; " + str(len(rows)) +
          " reconciled periods; privacy/link and budget invariants.")
    print("Scope: structure and arithmetic only; not bank, legal or tax certification.")
    return 0


def self_test():
    valid = ["| 2026-10 | 0 | 10000 | 4000 | 3000 | 3000 | VERIFIED | 2026-10-13 |",
             "| 2026-11 | 3000 | 2000 | 1000 | 400 | 3600 | VERIFIED | 2026-11-13 |"]
    assert not validate_rows(valid), validate_rows(valid)
    assert any("balance" in x for x in validate_rows([valid[0].replace("| 3000 | VERIFIED", "| 2000 | VERIFIED")]))
    assert any("Opening" in x for x in validate_rows([valid[0], valid[1].replace("| 3000 | 2000", "| 5000 | 2000")]))
    assert any("duplicate" in x.lower() or "overlap" in x.lower() for x in validate_rows([valid[0], valid[0]]))
    assert any("VERIFIED" in x for x in validate_rows([valid[0].replace("VERIFIED", "PENDING")]))
    print("PASS: internal valid arithmetic, tampered balance, carry, duplicate period and status controls.")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if sys.argv[1:] == ["--self-test"] else run())
