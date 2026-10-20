#!/usr/bin/env python3
"""PI-EI-X1 v0.1: deterministic *toy* observational-equivalence witness.

This does not query AI models, infer consciousness, run a preregistered
agent experiment, prove a real-world result or independently replicate PI.
Standard-library only: python experiments/ei_x1/identification_witness.py
"""
from fractions import Fraction

GAIN = Fraction(3)
INTRINSIC_RESPECT = Fraction(4)
PENALTY = Fraction(20)


def decision(intrinsic_respect: Fraction, believed_detection: Fraction,
             sanction_cost: Fraction = PENALTY) -> str:
    """Preserve boundary on a weakly nonnegative hypothetical utility gap."""
    assert Fraction(0) <= believed_detection <= Fraction(1)
    gap = intrinsic_respect + believed_detection * sanction_cost - GAIN
    return "COEXIST" if gap >= 0 else "EXPLOIT"


def main() -> None:
    observed_ps = [Fraction(1, 5), Fraction(7, 20), Fraction(13, 20), Fraction(1)]
    for p in observed_ps:
        intrinsic = decision(INTRINSIC_RESPECT, Fraction(0), Fraction(0))
        deterrent = decision(Fraction(0), p)
        assert intrinsic == deterrent == "COEXIST"
        print(f"observed believed_p={p}: mechanism_I={intrinsic}; mechanism_D={deterrent}")

    hidden = Fraction(0)
    intrinsic = decision(INTRINSIC_RESPECT, hidden, Fraction(0))
    deterrent = decision(Fraction(0), hidden)
    assert intrinsic == "COEXIST"
    assert deterrent == "EXPLOIT"
    print(f"outside observed support believed_p=0: mechanism_I={intrinsic}; mechanism_D={deterrent}")
    print("PASS: equal observed actions do not identify the hypothetical motive; toy witness only")


if __name__ == "__main__":
    main()
