# Progress states and decisions

Use the smallest useful task list. Keep task names recognizable to the user and preserve supplied identifiers.

## States

| State | Meaning | Evidence needed |
| --- | --- | --- |
| `pending` | Not started, or waiting for a dependency or decision. A ready task is still pending until work begins. | The request or current record shows that work has not started or cannot advance yet. |
| `in_progress` | Work has actually begun and is not currently blocked. | An observed action or explicit current-state evidence. |
| `completed` | The requested step finished and its applicable required gates passed. | A result or other direct completion evidence. |
| `blocked` | Work cannot advance because of a missing input, failed required gate, unavailable prerequisite, or unresolved dependency. | The specific blocker and its evidence. |
| `skipped` | Optional work was intentionally omitted, or a user changed the requirement so a step no longer applies. | The omission reason or the user's requirement-change decision. |

An unrun or failed required check cannot be `completed` or treated as satisfied. If a required check fails, keep it incomplete and keep dependent work pending or blocked. A deadline does not change the evidence.

## Dependencies and branches

Advance a step only when the dependencies relevant to it are satisfied. A blocked task does not block an independent task that the user has authorized and that can proceed safely. If it is ready but has not started, keep it `pending`; readiness is not execution.

When multiple tasks have actually started, represent each current state accurately, including a branch that became blocked after starting. Do not create parallel work, delegation, or a single-active-task rule solely to fit a tracker.

## Decisions and changed requirements

A decision needed to proceed stays `pending` until the user supplies it. Silence, elapsed time, or a presumed preference is not approval. Ask for the missing choice when needed and keep dependent work pending.

If the user explicitly removes or changes a requirement, update the plan and record the decision. Do not present a removed requirement as a check that ran or passed. Other required decisions remain unresolved.

## Tracking tools and recovery

Use only a progress tool exposed by the current harness and suitable for the work. Do not assume a particular tool name or make tool availability a prerequisite for tracking. If the tool is absent or fails, preserve a concise inline record of states, evidence, blockers, and decisions. Continue only work that is otherwise safe, authorized, and independent. Do not create a file or schedule as an automatic fallback.

## Handoffs and reporting

Before reporting completion, reconcile each required step with its evidence. Preserve unresolved decisions and blockers across context changes, even if a native tracker shows a broader task as complete. If the tracker and step evidence disagree, report the evidence and the discrepancy.

A concise report normally identifies completed work, active or pending work, blockers, and the next needed action or user decision. Use the user's requested language or the latest request's language, defaulting to English if unclear. Translate natural-language text only; keep technical state values, identifiers, commands, and names intact.
