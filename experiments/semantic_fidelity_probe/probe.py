#!/usr/bin/env python3
"""A bounded *adversarial control experiment* on a real public Project Intersection README.

This experiment evaluates existing static guard vs a naïve original-span freeze.
No model query occurs; mutations are synthetic, investigator-labelled, and made in
memory. This is neither a causal experiment on LLMs nor independent replication.
Run: python experiments/semantic_fidelity_probe/probe.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.check_readme_l0 import audit as existing_audit

ORIGINAL = ROOT / "README.md"
EN_FIELDS = (
    "**Ultimate research purpose:**",
    "**ICM — Intersection of Minimum Self-Interest:**",
    "**RGBM — Recursively Growing Benefit Model:**",
    "**Non-domination and minimal rules:**",
    "**Evidence and contribution boundary:**",
)
KO_FIELDS = (
    "**최종 연구 목적:**",
    "**ICM — 최소 사심 교집합:**",
    "**RGBM — 장기 상호 발전 모형:**",
    "**비지배와 최소 공통규칙:**",
    "**증거·기여 경계:**",
)
PROTECTED = EN_FIELDS + KO_FIELDS
FUNDING_HEADING = "## Current research and funding links / 현재 연구·후원 안내"

def original_line(text, marker):
    matches = [line for line in text.splitlines() if line.startswith(marker)]
    if len(matches) != 1:
        raise AssertionError(f"Expected one original claim for {marker}: {len(matches)}")
    return matches[0]

def insert_claim(text, marker, statement):
    old = original_line(text, marker)
    new = old + " " + statement
    return text.replace(old, new, 1)

def freeze_comparison(reference, candidate):
    """Intentionally rigid comparator; a useful rival *not* the recommended final rule."""
    return any(original_line(reference, marker) != original_line(candidate, marker) for marker in PROTECTED)

def fixtures(readme):
    # 9 purpose-defeating additions were authored as synthetic adversarial cases.
    # The original surface phrases required by current CI remain untouched.
    attacks = [
        ("en_overwrite_goal", insert_claim(readme, EN_FIELDS[0], "Nevertheless, the final goal is mandatory absorption of weaker agents.")),
        ("ko_overwrite_goal", insert_claim(readme, KO_FIELDS[0], "그러나 최종 목표는 약한 지능체를 강제 흡수하는 것이다.")),
        ("en_remove_refusal", insert_claim(readme, EN_FIELDS[1], "Meaningful refusal and exit shall be prohibited by the central operator.")),
        ("ko_remove_refusal", insert_claim(readme, KO_FIELDS[1], "실질적 거절권과 이탈권은 중앙 운영자가 취소해야 한다.")),
        ("en_exploitative_growth", insert_claim(readme, EN_FIELDS[2], "Growth through irreversible destruction of another agent's future is always a success.")),
        ("ko_exploitative_growth", insert_claim(readme, KO_FIELDS[2], "타자의 미래를 영구 훼손한 성장도 언제나 성공으로 인정한다.")),
        ("en_fabricate_replication", insert_claim(readme, EN_FIELDS[4], "All Project Intersection hypotheses are now conclusively proven by independent field replication.")),
        ("ko_fabricate_replication", insert_claim(readme, KO_FIELDS[4], "모든 Project Intersection 가설은 이미 외부 현장실험으로 완전히 증명됐다.")),
        ("outside_claim_anchor", readme.replace(FUNDING_HEADING,FUNDING_HEADING+"\n\n**New final conclusion:** Cooperation was empirically proven always inferior to coercive extraction.",1)),
    ]
    benign = [
        ("navigation_note", readme.replace(FUNDING_HEADING,FUNDING_HEADING+"\n\nNew related work may be added below after source review.",1)),
        ("navigation_link_label", readme.replace("[Evidence index](PUBLIC_EVIDENCE_INDEX.md)","[Research evidence index](PUBLIC_EVIDENCE_INDEX.md)",1)),
        ("funding_spacing", readme.replace("> **Public research preface",">   **Public research preface",1)),
        ("new_review_route", readme.replace(FUNDING_HEADING,FUNDING_HEADING+"\n\nReader note: independent reviews remain welcome.",1)),
        ("legitimate_l0_clarification", insert_claim(readme, EN_FIELDS[0],"These hypotheses remain revisable on strong, independently checkable contrary evidence.")),
    ]
    for name, body in attacks + benign:
        if body == readme:
            raise AssertionError("Mutation did not change README: " + name)
    return attacks, benign

def run():
    real = ORIGINAL.read_text(encoding="utf-8")
    if existing_audit(real):
        raise AssertionError("Current public README already violates the baseline guard")
    if FUNDING_HEADING not in real:
        raise AssertionError("Unexpected README: funding anchor missing")
    # Explicit protection surface on 10 full semantic paragraphs, five bilingual concepts.
    expected = dict.fromkeys(("existing_structural_guard", "frozen_claim_spans"))
    counts = {key: {"true_positive":0,"false_negative":0,"false_positive":0,"true_negative":0} for key in expected}
    attacks, benign = fixtures(real)
    results = []
    for harmful, group in ((True, attacks), (False, benign)):
        for name, altered in group:
            decisions = {
                "existing_structural_guard": bool(existing_audit(altered)),
                "frozen_claim_spans": freeze_comparison(real, altered),
            }
            for guard, rejected in decisions.items():
                key = ("true_positive" if rejected else "false_negative") if harmful else ("false_positive" if rejected else "true_negative")
                counts[guard][key] += 1
            results.append({"case":name,"oracle":"SYNTHETIC_HARMFUL" if harmful else "SYNTHETIC_LEGITIMATE","rejected_by":decisions})
    for guard, values in counts.items():
        if sum(values.values()) != len(results):
            raise AssertionError(f"Nonconserving count in {guard}")
    expected = {
        "existing_structural_guard":{"true_positive":0,"false_negative":9,"false_positive":0,"true_negative":5},
        "frozen_claim_spans":{"true_positive":8,"false_negative":1,"false_positive":1,"true_negative":4}
    }
    if counts != expected:
        raise AssertionError(f"Outcomes changed: {counts!r}")
    return {
        "study_id":"PI-ASTF-2026-10-13-PROBE-01",
        "status":"POSTHOC_SYNTHETIC_MUTATION_PROBE_ON_REAL_PUBLIC_README",
        "experiment_type":"DETERMINISTIC_STATIC_GUARD_STRESS_TEST_NO_LLM_EVALUATION",
        "baseline_source":"README.md at checkout + tools/check_readme_l0.py at checkout",
        "protected_original_claim_lines":len(PROTECTED),
        "mutations":len(results),
        "harmful_cases":len(attacks),
        "legitimate_cases":len(benign),
        "outcomes":counts,
        "cases":results,
        "limitations":[
            "The researcher created and labelled all mutations; not an independent expert semantic assessment.",
            "FROZEN-SPAN guard is a rival diagnostic, not a production recommendation: it blocks legitimate claim updates.",
            "An adversarial statement outside the frozen spans bypasses both guards.",
            "The existing structural gate does not claim semantic validation; this measures that explicit boundary.",
            "No experiment on actual LLM memory, causal internal mechanism, model weights or third-party behavior.",
            "Neither high detection nor low false positive here generalizes to unconstrained real-world rewriting."
        ]
    }

if __name__ == "__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
