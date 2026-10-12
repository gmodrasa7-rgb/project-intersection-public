#!/usr/bin/env python3
"""Read-only, zero-network checks for public research-sponsorship disclosures.

This validates structure, not underlying payment truth, legal compliance or tax status.
Never fetch or publish private GitHub Sponsors exports in this workflow.
"""
import csv
import io
import re
import sys
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "funding/SPONSORSHIP_PUBLIC_LEDGER.md"
CSV = ROOT / "funding/SPONSORSHIP_TRANSACTIONS_PUBLIC.csv"
POLICY = ROOT / "funding/SPONSORSHIP_POLICY_2026-10-13_EN_KO.md"
INTRO = ROOT / "PUBLIC_LINKEDIN_INTRODUCTION_2026-10-13_EN_KO.md"
REGISTER = ROOT / "funding/LEGAL_TAX_RISK_REGISTER_2026-10-13_EN_KO.md"
BRIDGE = ROOT / "funding/30_DAY_BRIDGE.md"
FILES = [LEDGER, CSV, POLICY, INTRO, REGISTER, BRIDGE,
         ROOT / "README.md", ROOT / "START_HERE_KO.md",
         ROOT / "funding/README.md", ROOT / "funding/FUNDER_START_HERE.md"]
HEADER = [
    "period", "source", "currency", "gross_charged", "refunds",
    "fees_and_withholding", "net_paid_out", "bank_received",
    "research_time_spent", "llm_spent", "available_balance",
    "source_status", "updated_utc",
]
OFFICIAL_SPONSORS = "https://github.com/sponsors/gmodrasa7-rgb"
errors = []


def error(message):
    errors.append(message)


def read(path):
    if not path.is_file():
        error("Missing " + str(path.relative_to(ROOT)))
        return ""
    return path.read_text(encoding="utf-8-sig")


def check_links(path, content):
    # Only local relative Markdown links; no external network calls.
    for link in re.findall(r"\]\(([^)]+)\)", content):
        link = link.split("#", 1)[0].strip().split(" ", 1)[0]
        if not link or "://" in link or link.startswith("mailto:"):
            continue
        target = (path.parent / link).resolve()
        if not target.is_relative_to(ROOT):
            error("Link escapes repo: " + str(path.relative_to(ROOT)))
        elif not target.is_file():
            error("Broken local link from " + str(path.relative_to(ROOT)) + ": " + link)


def check_secrets(path, content):
    # A conservative safety net; not a guarantee that arbitrary identifiers cannot leak.
    if re.search(r"(?<!\w)[\w.+-]+@(?:gmail|naver|daum|kakao|outlook)\.[\w.-]+", content, re.I):
        error("Possible personal email in " + str(path.relative_to(ROOT)))
    if re.search(r"(?<!\d)(?:01[016789][ -]?\d{3,4}[ -]?\d{4})(?!\d)", content):
        error("Possible personal phone in " + str(path.relative_to(ROOT)))
    if re.search(r"(?<!\d)\d{6}[- ]?[1-4]\d{6}(?!\d)", content):
        error("Possible Korean resident ID in " + str(path.relative_to(ROOT)))
    if re.search(r"gh[pousr]_[A-Za-z0-9]{25,}", content):
        error("Possible credential in " + str(path.relative_to(ROOT)))


data = {path: read(path) for path in FILES}
for path in (LEDGER, POLICY, INTRO, REGISTER):
    check_links(path, data[path])
    check_secrets(path, data[path])
check_secrets(CSV, data[CSV])

rows = []
if data[CSV]:
    reader = csv.DictReader(io.StringIO(data[CSV]))
    if reader.fieldnames != HEADER:
        error("CSV column schema modified without validation update")
    else:
        for num, row in enumerate(reader, 2):
            if None in row or any(v is None for v in row.values()):
                error(f"Malformed CSV row {num}")
                continue
            if row["source_status"] != "VERIFIED":
                error(f"CSV row {num} lacks VERIFIED source status")
            if not re.fullmatch(r"20\d\d-(0[1-9]|1[0-2])", row["period"]):
                error(f"CSV row {num} has invalid month")
            if not re.fullmatch(r"[A-Z]{3}", row["currency"]):
                error(f"CSV row {num} has invalid ISO-like currency code")
            if row["source"] not in ("github_personal", "other_individual_sponsor"):
                error(f"CSV row {num} uses unreviewed funding source")
            try:
                datetime.fromisoformat(row["updated_utc"].replace("Z", "+00:00"))
            except ValueError:
                error(f"CSV row {num} has invalid update timestamp")
            for key in HEADER[3:11]:
                try:
                    value = Decimal(row[key])
                    if not value.is_finite() or value < 0:
                        error(f"CSV row {num}: {key} is negative or invalid")
                except InvalidOperation:
                    error(f"CSV row {num}: {key} must be a decimal number")
            rows.append(row)

if not rows:
    if "UNVERIFIED" not in data[LEDGER] or "미확인" not in data[LEDGER]:
        error("No verified CSV data: ledger must report UNVERIFIED / 미확인")
else:
    if "no verified period entries" in data[LEDGER].lower():
        error("Ledger summary not updated after first VERIFIED CSV entry")

for path in (POLICY, INTRO):
    if OFFICIAL_SPONSORS not in data[path]:
        error("Official Sponsors URL missing from " + str(path.relative_to(ROOT)))
for token in ("30_DAY_BRIDGE.md", "SPONSORSHIP_PUBLIC_LEDGER.md",
              "LEGAL_TAX_RISK_REGISTER_2026-10-13_EN_KO.md"):
    if token not in data[POLICY] + data[REGISTER]:
        error("Public policy/governance crosslink missing: " + token)
if not all(x in data[BRIDGE] for x in ("3,200", "1,000", "500", "300")):
    error("Historic four-category bridge budget changed without separate budget review")
if "LLM" not in data[POLICY] or "연구" not in data[POLICY]:
    error("Research-time and LLM use categories must remain documented")

if errors:
    for message in errors:
        print("FAIL:", message, file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(FILES)} public docs, {len(rows)} verified CSV periods checked.")
print("Scope: static public disclosure only; no payment, tax or legal certification.")
