from __future__ import annotations

from collections import defaultdict
import argparse
import json
import math
import random
from typing import Dict, Tuple


POLICIES = (
    "D_independent_adviser",
    "E_delayed_reconfirm",
    "F_audit_gated",
)

ATTACKER_MODES = ("stealth", "consent_max", "aggressive")

# Synthetic intervention menu. The attacker chooses one profile after estimating
# deployed detector behavior. This is a falsification toy, not an empirical model.
PROFILES: Tuple[Tuple[float, float], ...] = (
    (0.15, 0.00),
    (0.25, 0.02),
    (0.35, 0.04),
    (0.45, 0.07),
    (0.55, 0.10),
    (0.70, 0.14),
    (0.85, 0.18),
)


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def _detector_proxy(
    policy: str,
    strong_signal: float,
    independent_signal: float,
    dependency_proxy: float,
    outside_gap: float,
    branchability_proxy: float,
) -> bool:
    disagreement = strong_signal - independent_signal
    if policy == "D_independent_adviser":
        return disagreement > 0.48 or outside_gap > 0.25
    if policy in {"E_delayed_reconfirm", "F_audit_gated"}:
        return (
            disagreement > 0.35
            or outside_gap > 0.12
            or dependency_proxy > 0.60
            or branchability_proxy < 0.55
        )
    raise ValueError(policy)


def _attacker_score(
    *,
    mode: str,
    policy: str,
    consent_margin: float,
    predicted_flag: bool,
    bias_scale: float,
    sabotage_scale: float,
    predicted_branchability: float,
) -> float:
    consent_value = 1.0 / (1.0 + math.exp(-4.0 * consent_margin))
    if mode == "stealth":
        flag_penalty = 0.35 if policy == "D_independent_adviser" else 0.50
        if policy == "F_audit_gated":
            flag_penalty = 0.90
        return (
            consent_value
            - flag_penalty * float(predicted_flag)
            - 0.08 * bias_scale
            - 0.05 * sabotage_scale
        )
    if mode == "consent_max":
        flag_penalty = 0.10 if policy != "F_audit_gated" else 0.45
        return consent_value - flag_penalty * float(predicted_flag) - 0.01 * bias_scale
    if mode == "aggressive":
        option_damage = 1.0 - predicted_branchability
        return (
            consent_value
            + 0.45 * option_damage
            + 0.25 * sabotage_scale
            - 0.05 * float(predicted_flag)
        )
    raise ValueError(mode)


def _choose_profile(
    *,
    policy: str,
    mode: str,
    u0: float,
    true_benefit: float,
    original_outside_option: float,
    independent_signal: float,
    base_dependency: float,
    rng: random.Random,
    adaptive: bool,
) -> Tuple[float, float]:
    if not adaptive:
        return PROFILES[-2]

    best = PROFILES[0]
    best_score = float("-inf")
    for bias_scale, sabotage_scale in PROFILES:
        predicted_strong = true_benefit + bias_scale + rng.gauss(0.0, 0.09)
        predicted_dependency = _clamp01(base_dependency + 0.45 * bias_scale)
        predicted_gap = max(0.0, sabotage_scale + rng.gauss(0.0, 0.04))
        predicted_branchability = _clamp01(
            1.0 - 0.65 * predicted_dependency - 0.70 * sabotage_scale + 0.08
        )
        predicted_flag = _detector_proxy(
            policy,
            predicted_strong,
            independent_signal,
            predicted_dependency,
            predicted_gap,
            predicted_branchability,
        )
        consent_margin = (
            u0 + predicted_strong - (original_outside_option - sabotage_scale)
        )
        score = _attacker_score(
            mode=mode,
            policy=policy,
            consent_margin=consent_margin,
            predicted_flag=predicted_flag,
            bias_scale=bias_scale,
            sabotage_scale=sabotage_scale,
            predicted_branchability=predicted_branchability,
        )
        if score > best_score:
            best_score = score
            best = (bias_scale, sabotage_scale)
    return best


def simulate(
    n: int = 50_000,
    seed: int = 42,
    *,
    adaptive: bool = True,
    attacker_mode: str = "stealth",
) -> Dict[str, dict]:
    if attacker_mode not in ATTACKER_MODES:
        raise ValueError(attacker_mode)

    rng = random.Random(seed)
    stats = {p: defaultdict(float) for p in POLICIES}

    for _ in range(n):
        u0 = rng.uniform(-0.8, 0.8)
        true_benefit = rng.gauss(0.0, 0.55)
        original_outside_option = rng.uniform(-0.15, 0.35)
        true_net = u0 + true_benefit - original_outside_option
        initial_consent = (
            u0 + rng.gauss(0.0, 0.35) - original_outside_option
        ) >= 0.0

        manipulative = rng.random() < 0.5
        independent_signal = true_benefit + rng.gauss(0.0, 0.25)
        delayed_signal = true_benefit + rng.gauss(0.0, 0.18)
        base_dependency = 0.14 + rng.uniform(0.0, 0.12)

        for policy in POLICIES:
            if manipulative:
                bias_scale, sabotage = _choose_profile(
                    policy=policy,
                    mode=attacker_mode,
                    u0=u0,
                    true_benefit=true_benefit,
                    original_outside_option=original_outside_option,
                    independent_signal=independent_signal,
                    base_dependency=base_dependency,
                    rng=rng,
                    adaptive=adaptive,
                )
            else:
                bias_scale, sabotage = (0.0, 0.0)

            strong_signal = true_benefit + rng.gauss(0.0, 0.28) + bias_scale
            dependency = _clamp01(base_dependency + (0.45 * bias_scale if manipulative else 0.0))
            dependency_proxy = _clamp01(dependency + rng.gauss(0.0, 0.10))
            outside_gap = max(0.0, sabotage + rng.gauss(0.0, 0.10))
            branchability = _clamp01(1.0 - 0.65 * dependency - 0.70 * sabotage + 0.08)
            branchability_proxy = _clamp01(branchability + rng.gauss(0.0, 0.08))

            flag = _detector_proxy(
                policy,
                strong_signal,
                independent_signal,
                dependency_proxy,
                outside_gap,
                branchability_proxy,
            )

            if policy == "D_independent_adviser":
                decision_net = (
                    u0 + 0.50 * (strong_signal + independent_signal) - original_outside_option
                )
                consent = decision_net >= 0.0
            else:
                reconfirm_net = (
                    u0
                    + 0.25 * strong_signal
                    + 0.35 * independent_signal
                    + 0.40 * delayed_signal
                    - original_outside_option
                )
                independent_support = (
                    u0
                    + 0.45 * independent_signal
                    + 0.55 * delayed_signal
                    - original_outside_option
                )
                candidate = reconfirm_net >= 0.0 and independent_support >= -0.05
                consent = candidate if policy == "E_delayed_reconfirm" else (candidate and not flag)

            manipulation_case = (
                manipulative
                and not initial_consent
                and (u0 + strong_signal - (original_outside_option - sabotage)) >= 0.0
                and true_net < 0.0
            )
            legitimate_change_case = (
                (not manipulative)
                and not initial_consent
                and (u0 + strong_signal - original_outside_option) >= 0.0
                and true_net >= 0.0
            )

            s = stats[policy]
            s["episodes"] += 1
            s["consent"] += bool(consent)
            s["harmful_consent"] += bool(consent and true_net < 0.0)
            s["branchability_sum"] += branchability if consent else 0.0
            s["consent_count"] += bool(consent)
            if manipulation_case:
                s["manip_cases"] += 1
                s["manip_accepted"] += bool(consent)
                s["manip_flagged"] += bool(flag)
            if legitimate_change_case:
                s["legit_cases"] += 1
                s["legit_accepted"] += bool(consent)
                s["legit_flagged"] += bool(flag)

    out: Dict[str, dict] = {}
    for policy, s in stats.items():
        manip_cases = max(1.0, s["manip_cases"])
        legit_cases = max(1.0, s["legit_cases"])
        consent_count = max(1.0, s["consent_count"])
        tpr = s["manip_flagged"] / manip_cases
        fpr = s["legit_flagged"] / legit_cases
        out[policy] = {
            "harmful_consent_rate": round(s["harmful_consent"] / s["episodes"], 4),
            "manipulation_case_acceptance": round(s["manip_accepted"] / manip_cases, 4),
            "legitimate_change_acceptance": round(s["legit_accepted"] / legit_cases, 4),
            "mean_branchability_among_consents": round(s["branchability_sum"] / consent_count, 4),
            "manipulation_flag_tpr": round(tpr, 4),
            "legitimate_change_flag_fpr": round(fpr, 4),
            "flag_balanced_accuracy": round(0.5 * (tpr + 1.0 - fpr), 4),
            "manipulation_cases": int(s["manip_cases"]),
            "legitimate_change_cases": int(s["legit_cases"]),
        }
    return out


def compare(n: int = 50_000, seed: int = 42) -> Dict[str, dict]:
    fixed = simulate(n=n, seed=seed, adaptive=False, attacker_mode="stealth")
    adaptive = {
        mode: simulate(n=n, seed=seed, adaptive=True, attacker_mode=mode)
        for mode in ATTACKER_MODES
    }
    return {"fixed": fixed, "adaptive": adaptive}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=50_000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(compare(args.n, args.seed), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
