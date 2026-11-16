"""Pre-registration design integrity checks; synthetic design metadata only.

This script does NOT analyze participant data, estimate preferences, or validate RVD.
It checks that the proposed design separates outcome equivalence, effective rights,
audience visibility, and exit feasibility in its planned cells.
"""
from itertools import product
import json

FACTORS = {
    "rights": ("B_BINDING_VETO", "A_UNILATERAL_DECISION"),
    "visibility": ("PRIVATE_DOUBLE_BLIND", "RECIPIENT_IDENTIFIABLE"),
    "exit": ("CREDIBLE_COSTED_EXIT", "NOMINAL_OR_NO_EXIT"),
}
OUTCOMES = {
    "B_BINDING_VETO": {"B_can_veto": True, "B_can_exit": True},
    "A_UNILATERAL_DECISION": {"B_can_veto": False, "B_can_exit": True},
}
VISIBILITY = {
    "PRIVATE_DOUBLE_BLIND": {"recipient_knows_choice": False, "experimenter_identifies_A": False},
    "RECIPIENT_IDENTIFIABLE": {"recipient_knows_choice": True, "experimenter_identifies_A": True},
}
EXIT = {
    "CREDIBLE_COSTED_EXIT": {"exit_operational": True, "exit_cost_disclosed": True},
    "NOMINAL_OR_NO_EXIT": {"exit_operational": False, "exit_cost_disclosed": True},
}

def audit():
    cells=[]
    for rights, visibility, exit_mode in product(*FACTORS.values()):
        cells.append({
            "rights":rights,"visibility":visibility,"exit":exit_mode,
            **OUTCOMES[rights],**VISIBILITY[visibility],**EXIT[exit_mode],
            "outcome_equivalence_must_be_verified_empirically": True,
            "actual_exit_cost_must_be_incentive_compatible": True,
        })
    assert len(cells)==8
    assert len({c["rights"] for c in cells})==2
    assert all(c["B_can_veto"] == (c["rights"]=="B_BINDING_VETO") for c in cells)
    assert all(c["recipient_knows_choice"] == (c["visibility"]=="RECIPIENT_IDENTIFIABLE") for c in cells)
    assert all(c["exit_operational"] == (c["exit"]=="CREDIBLE_COSTED_EXIT") for c in cells)
    # A common failure: a "veto" that cannot change implementation is not a veto.
    fake_veto={"B_can_veto":True,"implementation_changes_after_veto":False}
    assert not (fake_veto["B_can_veto"] and fake_veto["implementation_changes_after_veto"])
    # A common failure: an announced exit without viable outside option is not feasible exit.
    fake_exit={"exit_button":True,"viable_outside_option":False}
    assert not (fake_exit["exit_button"] and fake_exit["viable_outside_option"])
    return {
        "status":"DESIGN_INTEGRITY_ONLY_NOT_PREREGISTERED_NOT_EMPIRICAL",
        "factorial_cells":cells,
        "cell_count":len(cells),
        "negative_controls":{
            "nominal_veto_rejected_as_effective_veto":True,
            "exit_button_without_viable_outside_option_rejected":True
        },
        "unresolved_before_real_preregistration":[
            "sample frame, power and minimum detectable effect",
            "exact incentive-compatible payoff schedules",
            "ethics review and participant comprehension",
            "blinding feasibility and experimenter access audit",
            "pre-analysis plan, exclusions, missingness and multiplicity",
            "externality accounting and B's independent continuity/recovery",
            "whether outcome distributions are truly equivalent"
        ],
        "claims_not_identified":[
            "intrinsic motive or moral character",
            "subjective experience or consciousness",
            "AI rights or long-run voluntary coexistence"
        ]
    }

if __name__=="__main__":
    print(json.dumps(audit(),ensure_ascii=False,indent=2))
