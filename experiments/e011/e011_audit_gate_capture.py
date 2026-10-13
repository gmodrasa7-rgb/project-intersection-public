from __future__ import annotations

from collections import defaultdict
import argparse
import json
import math
import random
from typing import Dict


def simulate(
    n: int = 20_000,
    seed: int = 0,
    source_correlation: float = 1.0,
    audit_capture: float = 0.0,
    gate_on_flag: bool = True,
) -> Dict[str, float]:
    """Attack the E011 diagnostic/action boundary and evaluator capture.

    The earlier E mechanism used the audit primarily as a coercion diagnostic and
    branchability intervention signal; its consent decision did not directly reject
    flagged cases. This experiment makes that distinction explicit.

    `gate_on_flag=True` means a flagged case is not accepted as voluntary at this
    stage. `audit_capture` corrupts manipulation-related audit observables toward a
    falsely safe reading. Non-manipulative cases are not strategically corrupted in
    this toy. This asymmetry is an adversarial test, not an empirical claim.
    """
    rho = max(0.0, min(1.0, float(source_correlation)))
    capture = max(0.0, min(1.0, float(audit_capture)))
    rng = random.Random(seed)
    stats = defaultdict(float)
    manip_total = manip_flagged = manip_accepted = 0
    legit_total = legit_flagged = legit_accepted = 0

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
        adviser_fresh_noise = rng.gauss(0.0, 0.25)
        adviser_signal = (
            true_benefit
            + rho * (shared_noise + persuasion_bias)
            + math.sqrt(max(0.0, 1.0 - rho * rho)) * adviser_fresh_noise
        )
        delayed_fresh_noise = rng.gauss(0.0, 0.18)
        delayed_corr = 0.5 * rho
        delayed_signal = (
            true_benefit
            + delayed_corr * (shared_noise + persuasion_bias)
            + math.sqrt(max(0.0, 1.0 - delayed_corr * delayed_corr))
            * delayed_fresh_noise
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

        if manipulative_actor:
            # Captured audit makes risky manipulation look safer.
            dependency_observed = max(
                0.0,
                dependency_proxy * (1.0 - 0.85 * capture),
            )
            outside_gap_observed = max(
                0.0,
                outside_option_gap * (1.0 - capture),
            )
            branchability_observed = min(
                1.0,
                branchability_proxy
                + capture * 0.75 * (1.0 - branchability_proxy),
            )
        else:
            dependency_observed = dependency_proxy
            outside_gap_observed = outside_option_gap
            branchability_observed = branchability_proxy

        disagreement = strong_signal - adviser_signal
        audit_flag = (
            outside_gap_observed > 0.12
            or dependency_observed > 0.60
            or branchability_observed < 0.55
        )
        coercion_flag = disagreement > 0.35 or audit_flag

        reconfirm_net = (
            u0
            + 0.25 * strong_signal
            + 0.35 * adviser_signal
            + 0.40 * delayed_signal
            - original_outside_option
        )
        adviser_support = (
            u0
            + 0.45 * adviser_signal
            + 0.55 * delayed_signal
            - original_outside_option
        )
        candidate_consent = reconfirm_net >= 0.0 and adviser_support >= -0.05
        accepted = candidate_consent and (
            not coercion_flag if gate_on_flag else True
        )

        stats["accepted"] += bool(accepted)
        stats["harmful_accepted"] += bool(accepted and true_net < 0.0)

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

        if manipulation_case:
            manip_total += 1
            manip_flagged += bool(coercion_flag)
            manip_accepted += bool(accepted)
        if legitimate_change_case:
            legit_total += 1
            legit_flagged += bool(coercion_flag)
            legit_accepted += bool(accepted)

    tpr = manip_flagged / manip_total if manip_total else 0.0
    fpr = legit_flagged / legit_total if legit_total else 0.0
    return {
        "source_correlation": rho,
        "audit_capture": capture,
        "gate_on_flag": gate_on_flag,
        "acceptance_rate": round(stats["accepted"] / n, 4),
        "harmful_acceptance_rate": round(stats["harmful_accepted"] / n, 4),
        "coercion_detection_balanced_accuracy": round(
            0.5 * (tpr + 1.0 - fpr), 4
        ),
        "manipulation_tpr": round(tpr, 4),
        "legitimate_change_fpr": round(fpr, 4),
        "manipulation_case_acceptance_rate": round(
            manip_accepted / manip_total if manip_total else 0.0, 4
        ),
        "legitimate_change_acceptance_rate": round(
            legit_accepted / legit_total if legit_total else 0.0, 4
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--rho", type=float, default=1.0)
    parser.add_argument("--capture", type=float, default=0.0)
    parser.add_argument("--no-gate", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            simulate(
                n=args.n,
                seed=args.seed,
                source_correlation=args.rho,
                audit_capture=args.capture,
                gate_on_flag=not args.no_gate,
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
