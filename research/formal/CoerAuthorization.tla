---------------- MODULE CoerAuthorization ----------------
EXTENDS Naturals, FiniteSets, TLC

CONSTANTS Actions, Scopes
ASSUME Actions # {} /\ Scopes # {}

VARIABLES approvalState, approvedScope, executed, effectCount, outcomeVerified, completed
vars == <<approvalState, approvedScope, executed, effectCount, outcomeVerified, completed>>

Init ==
  /\ approvalState = [a \in Actions |-> "NONE"]
  /\ approvedScope = [a \in Actions |-> {}]
  /\ executed = {}
  /\ effectCount = [a \in Actions |-> 0]
  /\ outcomeVerified = {}
  /\ completed = {}

Grant(a, s) ==
  /\ a \in Actions
  /\ s \subseteq Scopes
  /\ approvalState[a] \in {"NONE", "REVOKED", "EXPIRED"}
  /\ approvalState' = [approvalState EXCEPT ![a] = "ACTIVE"]
  /\ approvedScope' = [approvedScope EXCEPT ![a] = s]
  /\ UNCHANGED <<executed, effectCount, outcomeVerified, completed>>

Revoke(a) ==
  /\ approvalState[a] = "ACTIVE"
  /\ approvalState' = [approvalState EXCEPT ![a] = "REVOKED"]
  /\ UNCHANGED <<approvedScope, executed, effectCount, outcomeVerified, completed>>

Expire(a) ==
  /\ approvalState[a] = "ACTIVE"
  /\ approvalState' = [approvalState EXCEPT ![a] = "EXPIRED"]
  /\ UNCHANGED <<approvedScope, executed, effectCount, outcomeVerified, completed>>

Execute(a, s) ==
  /\ a \in Actions
  /\ approvalState[a] = "ACTIVE"
  /\ s \subseteq approvedScope[a]
  /\ a \notin executed
  /\ executed' = executed \cup {a}
  /\ effectCount' = [effectCount EXCEPT ![a] = @ + 1]
  /\ UNCHANGED <<approvalState, approvedScope, outcomeVerified, completed>>

VerifyOutcome(a) ==
  /\ a \in executed
  /\ outcomeVerified' = outcomeVerified \cup {a}
  /\ UNCHANGED <<approvalState, approvedScope, executed, effectCount, completed>>

MarkComplete(a) ==
  /\ a \in outcomeVerified
  /\ completed' = completed \cup {a}
  /\ UNCHANGED <<approvalState, approvedScope, executed, effectCount, outcomeVerified>>

Next ==
  \/ \E a \in Actions, s \in SUBSET Scopes : Grant(a, s)
  \/ \E a \in Actions : Revoke(a) \/ Expire(a)
  \/ \E a \in Actions, s \in SUBSET Scopes : Execute(a, s)
  \/ \E a \in Actions : VerifyOutcome(a) \/ MarkComplete(a)

NoUnauthorizedExecution ==
  \A a \in executed : approvalState[a] = "ACTIVE"

NoDuplicateEffect ==
  \A a \in Actions : effectCount[a] <= 1

NoFalseCompletion ==
  completed \subseteq outcomeVerified

Spec == Init /\ [][Next]_vars
====
