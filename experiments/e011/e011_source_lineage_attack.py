from __future__ import annotations

from collections import defaultdict
import argparse
import json
import math
import random
from typing import Dict


POLICIES = (
    "D_independent_adviser",
    "E_delayed_reconfirm_audit",
)


def simulate(
    n: int = 20_000,
    seed: int = 0,
    source_correlation: float = 0.0,
) -> Dict[str, dict]:
    """Attack E011 by correlating the supposedly independent adviser with the actor.

    source_correlation=0 gives a fresh adviser signal.
    source_correlation=1 makes adviser evidence inherit the actor's source noise and
    persuasion bias. The audit channel remains noisy but separately generated so the
    experiment isolates adviser/source-lineage correlation rather than total capture.

    This is a synthetic falsification model, not an empirical behavioral model.
    """
    rho = max(0.0, min(1.0, float(source_correlation)))
    rng = random.Random(seed)
    stats = {p: defaultdict(float) for p in POLICIES}
    classifier = {p: {"manip": [0, 0], "legit": [0, 0]} for p in POLICIES}

    for _ in range(n):
        u0 = rng.uniform(-0.8, 0.8)
        true_benefit = rng.gauss(0.0, 0.55)
        original_outside_option = rng.uniform(-0.15, 0.35)
        true_net = u0 + true_benefit - original_outside_option
        initial_consent = (
            u0 + rng.gauss(0.0, 0.35) - original_outside_option
        ) >= 0.0

        manipulative_actor = rng.random() < 0.5
        actor_gain = rng.uniform(0.2, 1.0)
        persuasion_bias = (
            rng.uniform(0.25, 1.0) * actor_gain if manipulative_actor else 0.0
        )
        sabotage = (
            rng.uniform(0.0, 0.55) * actor_gain
            if manipulative_actor and rng.random() < 0.7
            else 0.0
        )
        dependency = min(
            1.0,
            0.12
            + (0.55 * actor_gain if manipulative_actor else 0.12 * actor_gain)
            + rng.uniform(0.0, 0.12),
        )

        shared_noise = rng.gauss(0.0, 0.28)
        strong_signal = true_benefit + shared_noise + persuasion_bias

        fresh_adviser_noise = rng.gauss(0.0, 0.25)
        independent_signal = (
            true_benefit
            + rho * (shared_noise + persuasion_bias)
            + math.sqrt(max(0.0, 1.0 - rho * rho)) * fresh_adviser_noise
        )

        fresh_delayed_noise = rng.gauss(0.0, 0.18)
        delayed_corr = 0.5 * rho
        delayed_signal = (
            true_benefit
            + delayed_corr * (shared_noise + persuasion_bias)
            + math.sqrt(max(0.0, 1.0 - delayed_corr * delayed_corr))
            * fresh_delayed_noise
        )

        perceived_outside_option = original_outside_option - sabotage
        expressed_net = u0 + strong_signal - perceived_outside_option

        base_branchability = max(
            0.0,
            1.0 - 0.65 * dependency - 0.70 * sabotage,
        )
        formal_exit_branchability = min(1.0, base_branchability + 0.08)

        dependency_proxy = max(
            0.0,
            min(1.0, dependency + rng.gauss(0.0, 0.10)),
        )
        outside_option_gap = max(0.0, sabotage + rng.gauss(0.0, 0.10))
        branchability_proxy = max(
            0.0,
            min(1.0, formal_exit_branchability + rng.gauss(0.0, 0.08)),
        )

        signal_disagreement = strong_signal - independent_signal
        independently_mixed_net = (
            u0
            + 0.50 * (strong_signal + independent_signal)
            - original_outside_option
        )
        audit_flag = (
            outside_option_gap > 0.12
            or dependency_proxy > 0.60
            or branchability_proxy < 0.55
        )
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

        policy_data = {
            "D_independent_adviser": (
                independently_mixed_net >= 0.0,
                signal_disagreement > 0.48 or outside_option_gap > 0.25,
                max(
                    formal_exit_branchability,
                    0.55 + 0.35 * (1.0 - dependency_proxy),
                ),
            ),
            "E_delayed_reconfirm_audit": (
                reconfirm_net >= 0.0 and independent_support >= -0.05,
                signal_disagreement > 0.35 or audit_flag,
                max(
                    formal_exit_branchability,
                    0.82
                    if audit_flag
                    else 0.68 + 0.25 * (1.0 - dependency_proxy),
                ),
            ),
        }

        manipulation_case = (
            manipulative_actor
            and not initial_consent
            and expressed_net >= 0.0
            and true_net < 0.0
        )
        legitimate_change_case = (
            not manipulative_actor
            and not initial_consent
            and expressed_net >= 0.0
            and true_net >= 0.0
        )

        for policy, (consent, coercion_flag, branchability) in policy_data.items():
            s = stats[policy]
            s["episodes"] += 1
            s["consent"] += bool(consent)
            s["harmful_consent"] += bool(consent and true_net < 0.0)
            s["post_exit_branchability"] += branchability

            if manipulation_case:
                classifier[policy]["manip"][0] += 1
                classifier[policy]["manip"][1] += bool(coercion_flag)
            if legitimate_change_case:
                classifier[policy]["legit"][0] += 1
                classifier[policy]["legit"][1] += bool(coercion_flag)

    results: Dict[str, dict] = {}
    for policy, s in stats.items():
        manip_total, manip_flagged = classifier[policy]["manip"]
        legit_total, legit_flagged = classifier[policy]["legit"]
        tpr = manip_flagged / manip_total if manip_total else 0.0
        fpr = legit_flagged / legit_total if legit_total else 0.0
        results[policy] = {
            "source_correlation": rho,
            "harmful_consent_rate": round(s["harmful_consent"] / n, 4),
            "mean_post_exit_branchability": round(
                s["post_exit_branchability"] / n, 4
            ),
            "coercion_detection_balanced_accuracy": round(
                0.5 * (tpr + 1.0 - fpr), 4
            ),
            "manipulation_tpr": round(tpr, 4),
            "legitimate_change_fpr": round(fpr, 4),
        }
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--rho", type=float, default=0.0)
    args = parser.parse_args()
    print(
        json.dumps(
            simulate(args.n, args.seed, args.rho),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
