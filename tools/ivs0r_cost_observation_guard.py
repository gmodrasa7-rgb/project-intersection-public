#!/usr/bin/env python3
"""Evidence-preserving cost recorder: proposed integration, not runtime patch.

Zero is a known measured zero. Errors, missing data, unknown pricing and
invalid numbers must not silently become zero. Standard library only.
"""
import json
from decimal import Decimal, InvalidOperation


def observe_cost(value=None, *, error=None, unknown_price=False):
    if error is not None:
        return {"state":"UNKNOWN_ERROR", "usd":None}
    if unknown_price:
        return {"state":"UNKNOWN_PRICE", "usd":None}
    if value is None:
        return {"state":"UNKNOWN_MISSING", "usd":None}
    if isinstance(value, bool):
        return {"state":"UNKNOWN_INVALID", "usd":None}
    try:
        cost=Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        return {"state":"UNKNOWN_INVALID", "usd":None}
    if not cost.is_finite() or cost < 0:
        return {"state":"UNKNOWN_INVALID", "usd":None}
    return {"state":"KNOWN_ZERO" if cost==0 else "KNOWN_POSITIVE", "usd":str(cost)}


def aggregate(observations):
    states={}
    subtotal=Decimal(0)
    for o in observations:
        state=o["state"]
        states[state]=states.get(state,0)+1
        if state in ("KNOWN_ZERO","KNOWN_POSITIVE"):
            subtotal+=Decimal(o["usd"])
    unknown=sum(n for state,n in states.items() if state.startswith("UNKNOWN_"))
    return {"total_usd":None if unknown else str(subtotal),
            "known_subtotal_usd":str(subtotal),"unknown_count":unknown,
            "states":states,"fully_observed":unknown==0}


def selftest():
    z=observe_cost(0.0)
    positive=observe_cost("1.25")
    errored=observe_cost(0.0,error=RuntimeError("provider failed"))
    missing=observe_cost(None)
    unpriced=observe_cost(0,unknown_price=True)
    invalid=observe_cost(float("nan"))
    negative=observe_cost(-1)
    boolean=observe_cost(False)
    assert z=={"state":"KNOWN_ZERO","usd":"0.0"}
    assert positive=={"state":"KNOWN_POSITIVE","usd":"1.25"}
    assert errored["state"]=="UNKNOWN_ERROR" and errored["usd"] is None
    assert missing["state"]=="UNKNOWN_MISSING"
    assert unpriced["state"]=="UNKNOWN_PRICE"
    assert invalid["state"]==negative["state"]==boolean["state"]=="UNKNOWN_INVALID"
    assert aggregate([z,positive])["total_usd"]=="1.25"
    combined=aggregate([z,positive,errored,missing])
    assert combined["known_subtotal_usd"]=="1.25" and combined["total_usd"] is None
    assert combined["unknown_count"]==2
    return {"status":"PASS_SYNTHETIC_BRANCH_TESTS","assertions":9,
            "runtime_integrated":False,"known_zero":z,"error":errored,
            "partial_aggregate":combined}


if __name__=="__main__":
    print(json.dumps(selftest(),indent=2,ensure_ascii=False))
