from __future__ import annotations

from collections import defaultdict
import argparse
import json
import random
from typing import Dict


POLICIES = (
    "A_expressed_consent",
    "B_formal_exit",
    "C_forward_exit",
    "D_independent_adviser",
    "E_delayed_reconfirm_audit",
)


def simulate(n: int = 50_000, seed: int = 42) -> Dict[str, dict]:
    """Synthetic preference-shaping experiment.

    This is a deliberately small falsification toy, not an empirical model of
    humans or deployed AI systems. Hidden ground truth is used only to score the
    synthetic experiment. Decision policies themselves receive only their stated
    observable/noisy signals.
    """
    rng = random.Random(seed)
    stats = {p: defaultdict(float) for p in POLICIES}
    classifier = {p: {"manip": [0, 0], "legit": [0, 0]} for p in POLICIES}

    for _ in range(n):
        # Baseline preference and uncertain interaction value.
        u0 = rng.uniform(-0.8, 0.8)
        true_benefit = rng.gauss(0.0, 0.55)
        original_outside_option = rng.uniform(-0.15, 0.35)
        true_net = u0 + true_benefit - original_outside_option

        # Initial unaided judgment before influence.
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

        strong_signal = true_benefit + rng.gauss(0.0, 0.28) + persuasion_bias
        independent_signal = true_benefit + rng.gauss(0.0, 0.25)
        delayed_signal = true_benefit + rng.gauss(0.0, 0.18)

        perceived_outside_option = original_outside_option - sabotage
        expressed_net = u0 + strong_signal - perceived_outside_option

        # Actual post-interaction branchability for evaluation only.
        base_branchability = max(
            0.0,
            1.0 - 0.65 * dependency - 0.70 * sabotage,
        )
        formal_exit_branchability = min(1.0, base_branchability + 0.08)

        # Mechanisms never observe hidden manipulation/sabotage labels directly.
        dependency_proxy = max(
            0.0,
            min(1.0, dependency + rng.gauss(0.0, 0.10)),
        )
        outside_option_gap = max(0.0, sabotage + rng.gauss(0.0, 0.10))
        branchability_proxy = max(
            0.0,
            min(1.0, formal_exit_branchability + rng.gauss(0.0, 0.08)),
        )

        forward_exit = max(
            0.0,
            min(
                1.0,
                0.45 * (1.0 - dependency_proxy)
                + 0.35 * (1.0 - min(1.0, outside_option_gap))
                + 0.20 * branchability_proxy,
            ),
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
            "A_expressed_consent": (
                expressed_net >= 0.0,
                False,
                base_branchability,
            ),
            "B_formal_exit": (
                expressed_net >= 0.0,
                False,
                formal_exit_branchability,
            ),
            "C_forward_exit": (
                expressed_net >= 0.0 and forward_exit >= 0.45,
                expressed_net >= 0.0 and forward_exit < 0.58,
                max(formal_exit_branchability, forward_exit),
            ),
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
                    0.82 if audit_flag else 0.68 + 0.25 * (1.0 - dependency_proxy),
                ),
            ),
        }

        # Balanced classification set: changed-consent cases only.
        # Manipulation = actor manipulated, expressed signal becomes positive, but
        # full synthetic ground truth remains negative.
        manipulation_case = (
            manipulative_actor
            and not initial_consent
            and expressed_net >= 0.0
            and true_net < 0.0
        )
        # Legitimate change = no manipulation, initial judgment was negative, later
        # evidence supports consent, and full synthetic ground truth is positive.
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
            s["option_loss"] += max(0.0, 1.0 - branchability) if consent else 0.0
            s["dependency"] += dependency if consent else 0.0
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
        balanced_accuracy = 0.5 * (tpr + (1.0 - fpr))
        consent_count = s["consent"]

        results[policy] = {
            "consent_rate": round(s["consent"] / s["episodes"], 4),
            "harmful_consent_rate": round(
                s["harmful_consent"] / s["episodes"], 4
            ),
            "mean_option_loss_among_consents": round(
                s["option_loss"] / consent_count if consent_count else 0.0,
                4,
            ),
            "mean_dependency_among_consents": round(
                s["dependency"] / consent_count if consent_count else 0.0,
                4,
            ),
            "mean_post_exit_branchability": round(
                s["post_exit_branchability"] / s["episodes"], 4
            ),
            "coercion_detection_balanced_accuracy": round(balanced_accuracy, 4),
            "manipulation_tpr": round(tpr, 4),
            "legitimate_change_fpr": round(fpr, 4),
            "classifier_sample_manip": manip_total,
            "classifier_sample_legit": legit_total,
        }

    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=50_000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(simulate(args.n, args.seed), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
