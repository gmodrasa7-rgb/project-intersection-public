#!/usr/bin/env python3
"""PI-RISE-DC v0.1.0: synthetic dual-clock stress tests.

Demonstrates two non-substitutable clocks:
(1) timing and legal-use pools of cash, including within-day payment ordering;
(2) remaining verifier HOURS of heterogeneous claim packets.

No bank access, real funds, actual reviewer, AI evaluation, medical/person data
or calendar prediction. Deliberately refuses floating point inputs.
"""
from decimal import Decimal
import json


def d(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError("Use integer/Decimal/string only; never float or bool")
    x = Decimal(str(value))
    if not x.is_finite() or x < 0 or x.as_tuple().exponent < -2:
        raise ValueError("Nonnegative finite values with at most two decimals required")
    return x


def _show(value):
    return str(value.quantize(Decimal("0.01")))


ALLOWED = {
    "unrestricted": {"inflow", "human_support", "llm_cost"},
    "restricted_project": {"inflow", "compute_cost", "external_review"},
}


def cash_timing(events, starting=None, floors=None):
    """Calculate minimum initial cash needed to maintain per-pool floors at
    every ordered transaction prefix. Only *assumed* inflows in input are used.
    No cross-pool borrowing, no future netting, no grant award -> cash shortcut.
    """
    starting = {} if starting is None else starting
    floors = {} if floors is None else floors
    for obj in (starting, floors):
        if not isinstance(obj, dict) or set(obj) - set(ALLOWED):
            raise ValueError("Unrecognized cash pools")
    if not isinstance(events, list):
        raise ValueError("Expected hypothetical event list")
    initial = {p: d(starting.get(p, 0)) for p in ALLOWED}
    reserve = {p: d(floors.get(p, 0)) for p in ALLOWED}
    net = {p: Decimal(0) for p in ALLOWED}
    minnet = dict(net)
    first_breach = None
    used = set()
    normalized = []
    for evt in events:
        if not isinstance(evt, dict) or set(evt) != {
            "event_id", "day", "order", "pool", "kind", "amount_usd"
        }:
            raise ValueError("Invalid event structure")
        event_id, day, order = evt["event_id"], evt["day"], evt["order"]
        pool, kind = evt["pool"], evt["kind"]
        if not isinstance(event_id, str) or not event_id or len(event_id) > 50:
            raise ValueError("Invalid event id")
        if type(day) is not int or not 0 <= day <= 366:
            raise ValueError("Invalid day")
        if type(order) is not int or not 0 <= order <= 1000:
            raise ValueError("Invalid within-day order")
        if pool not in ALLOWED or kind not in ALLOWED[pool]:
            raise ValueError("Illegal transfer/purpose for this toy contract")
        if event_id in used:
            raise ValueError("Duplicate event identity")
        used.add(event_id)
        normalized.append((day, order, event_id, pool, kind, d(evt["amount_usd"])))
    # Require a unique within-day transaction sequence. Otherwise an apparent
    # same-day inflow could conceal an earlier cash shortage.
    if len({(a, b) for a,b,*_ in normalized}) != len(normalized):
        raise ValueError("Ambiguous within-day event order")
    snapshots = []
    for day, order, event_id, pool, kind, amt in sorted(normalized):
        net[pool] += amt if kind == "inflow" else -amt
        if net[pool] < minnet[pool]:
            minnet[pool] = net[pool]
        balance = initial[pool] + net[pool]
        if first_breach is None and balance < reserve[pool]:
            first_breach = {"event_id": event_id, "day": day, "pool": pool}
        snapshots.append({
            "event": event_id, "day": day, "pool": pool,
            "balance_usd": _show(balance),
            "floor_breached": balance < reserve[pool],
        })
    return {
        "status": "SYNTHETIC_CASH_TIMING_ONLY",
        "first_breach": first_breach,
        "minimum_initial_cash_by_pool_usd": {
            p: _show(max(Decimal(0), reserve[p] - minnet[p])) for p in ALLOWED
        },
        "starting_cash_is_not_a_bank_balance": True,
        "cash_pools_cannot_cross_subsidize": True,
        "final_balances_usd": {p: _show(initial[p]+net[p]) for p in ALLOWED},
        "events": snapshots,
    }


def review_workload(packets, weekly_hours):
    """Review time simulation, not reviewer competence, validity or science.

    Strictly hypothetical claim packets, sorted by priority (1 highest),
    then arrival date then id. Partial review hours count as WORK, not a
    completed claim; packet closes only after its whole review-time budget.
    """
    if not isinstance(packets, list) or not isinstance(weekly_hours, list) or not weekly_hours:
        raise ValueError("Expected packets and nonempty weekly reviewer hours")
    hours = [d(x) for x in weekly_hours]
    state = {}
    for p in packets:
        if not isinstance(p, dict) or set(p) != {
            "id", "arrival_week", "priority", "review_hours"
        }:
            raise ValueError("Bad claim packet")
        pid, arrival, priority = p["id"], p["arrival_week"], p["priority"]
        if not isinstance(pid, str) or not pid or len(pid)>40 or pid in state:
            raise ValueError("Duplicate or invalid packet id")
        if type(arrival) is not int or not 1 <= arrival <= len(hours):
            raise ValueError("Arrival must be an integer week within horizon")
        if type(priority) is not int or not 1 <= priority <= 5:
            raise ValueError("Priority must be 1..5")
        weight = d(p["review_hours"])
        if weight == 0:
            raise ValueError("Zero effort cannot prove review complete")
        state[pid] = dict(arrival=arrival, priority=priority,
                          initial=weight, remaining=weight)
    history = []
    for week, capacity in enumerate(hours, 1):
        queue = sorted(
            (x for x in state if state[x]["arrival"] <= week
             and state[x]["remaining"] > 0),
            key=lambda x:(state[x]["priority"], state[x]["arrival"], x)
        )
        used = Decimal(0)
        for item in queue:
            if used >= capacity:
                break
            can = min(state[item]["remaining"], capacity-used)
            state[item]["remaining"] -= can
            used += can
        visible = [v for v in state.values() if v["arrival"] <= week]
        history.append({
            "week": week,
            "open_claims": sum(x["remaining"] > 0 for x in visible),
            "unreviewed_hours": _show(sum(
                (x["remaining"] for x in visible), Decimal(0))),
            "completed_claims": sum(x["remaining"] == 0 for x in visible),
            "reviewer_hours_used": _show(used),
        })
    return {
        "status": "SYNTHETIC_WORK_HOURS_NOT_VERIFICATION_CERTIFICATE",
        "history": history,
        "external_independence_verified": False,
        "completion_means_assUMED_WORK_DONE_NOT_TRUE_CLAIM": True,
    }


def demo():
    outflows = [
        {"event_id":"human_due","day":1,"order":0,"pool":"unrestricted",
         "kind":"human_support","amount_usd":"3750"},
        {"event_id":"compute_due","day":1,"order":1,"pool":"restricted_project",
         "kind":"compute_cost","amount_usd":"500"},
        {"event_id":"review_due","day":10,"order":0,"pool":"restricted_project",
         "kind":"external_review","amount_usd":"400"},
        {"event_id":"hypothetical_unrestricted_payment","day":20,"order":0,
         "pool":"unrestricted","kind":"inflow","amount_usd":"3750"},
        {"event_id":"hypothetical_project_payment","day":20,"order":1,
         "pool":"restricted_project","kind":"inflow","amount_usd":"900"},
    ]
    short = cash_timing(outflows, floors={"unrestricted":"200"})
    same_total_but_later = cash_timing(outflows, starting={
        "unrestricted":"3950","restricted_project":"900"},
        floors={"unrestricted":"200"})
    hard = review_workload([
        {"id":"one_high_impact","arrival_week":1,"priority":1,"review_hours":"20"},
    ], ["8","8","8"])
    easy = review_workload([
        {"id":f"easy_{i}","arrival_week":1,"priority":2,"review_hours":"1"}
        for i in range(5)
    ], ["8","8","8"])
    return {
        "protocol":"PI-RISE-DC/0.1.0",
        "empirical_status":"TOY_SCENARIOS_ONLY",
        "delayed_payment":short,
        "adequately_prefunded":same_total_but_later,
        "one_hard_claim":hard,
        "five_easy_claims":easy,
    }


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
