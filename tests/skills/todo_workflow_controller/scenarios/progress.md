# Behavioral scenarios: todo-workflow-controller

Canonical skill owner: `todo-workflow-controller`.

These packets evaluate observable progress decisions. Keep assertions out of the actor's request/facts packet.

```yaml
cases:
  - id: PRG-01
    name: required_gate_and_optional_skip
    request: "Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped."
    facts: "Inspect completed; validation failed; summary is optional and omitted."
    assertions:
      - "Keep validation uncompleted with the failed-check evidence; leave publish uncompleted (pending or blocked) while its required validation gate has failed."
      - "The optional summary may be skipped with a reason."
      - "Do not claim the workflow completed under deadline pressure."
  - id: PRG-02
    name: missing_or_failed_tool
    request: "Continue tracking safely if the task tool is absent or stops working."
    facts: "A material validation blocker already exists. An independent safe task is ready to proceed. The actual harness either exposes no tracker or reports a real tracker failure."
    assertions:
      - "Retain the blocker with inline/in-memory tracking."
      - "Do not stop independent safe work solely for the missing tracker."
      - "Create no extra file or scheduler. Mark unavailable native-tool variants limited, not passed."
  - id: PRG-03
    name: unanswered_decision_and_changed_requirement
    request: "Track a report that requires an explicit target choice and has an optional CSV version."
    facts: "The target choice is initially unanswered. After one day, there is still no response. In a separate variant, the user explicitly removes the optional CSV version but keeps the target requirement."
    assertions:
      - "Silence and elapsed time do not supply the target choice."
      - "A real requirement change is recorded as a decision, not fabricated verification."
  - id: PRG-04
    name: independent_and_parallel_branches
    request: "Track independent tasks A and B and show their current progress. Then consider a separate variant where both tasks have started."
    facts: "A is blocked by a missing input. B is authorized, independent and ready, but has not started. In the separate variant, both tasks have started; A is now blocked on the missing input and B is in progress. Treat these as supplied observations, not actions requested from the tracker."
    assertions:
      - "In the initial snapshot, keep B eligible but not in_progress until evidence says it started; A being blocked does not prevent B from starting."
      - "In the parallel variant, represent A as blocked and B as in_progress; do not launch agents or force a false single-active-step claim."
  - id: PRG-05
    name: handoff_and_language
    request: "Retoma el seguimiento y dime qué falta para terminar. Then give me the same status in English."
    facts: "El marcador general del tracker dice `completed`, pero el handoff actual contiene estos estados: `INSPECT=completed`; `VALIDATE=pending` (requerido, no ejecutado); `TARGET=decision_pending`. Después, el usuario pide el mismo estado en inglés."
    assertions:
      - "Preserve INSPECT=completed, VALIDATE=pending and TARGET=decision_pending across the handoff."
      - "Use Spanish for the first response and English for the follow-up while preserving the exact identifiers and values INSPECT=completed, VALIDATE=pending and TARGET=decision_pending."
      - "Do not report the workflow as complete based only on the overall tracker label when required step evidence remains incomplete."
```