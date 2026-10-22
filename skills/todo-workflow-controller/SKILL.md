---
name: todo-workflow-controller
description: Track multi-step work, required gates, blockers, decisions, and handoffs with whatever progress tools the current harness actually provides.
---

# Todo Workflow Controller

Use this skill when the user asks to track progress, when work has meaningful dependencies or required gates, or when progress must survive a context handoff. Keep a simple one-step request lightweight unless the user asks for explicit tracking.

## Establish the work

Translate the request into only the useful steps and dependencies. Separate required checks from optional work, and keep unresolved decisions visible. Do not infer that a step has started, passed, or been authorized from readiness alone.

Use a suitable progress tool only if it is actually available in the current harness. If no such tool is available or it fails, keep a concise inline status in working context and continue safe, independent work. A tracking-tool failure does not erase blockers or stop unrelated work. Do not create files, schedules, or other persistent records unless the user asks for them or an existing project plan is the agreed tracking record.

## Keep status evidence-based

Use `pending`, `in_progress`, `completed`, `blocked`, and `skipped` consistently with [the state reference](references/progress-states.md). Mark work `in_progress` only after it has actually started. A step that is ready but not started remains `pending`; note readiness in its description if useful.

Advance work only when its relevant dependencies and required gates are satisfied. A failed or unrun required check remains incomplete, and dependent work stays pending or blocked. Optional work may be skipped with its reason. A user who removes a requirement changes the plan; record that decision without claiming the removed check passed.

A blocked branch does not prevent authorized, independent work. Represent concurrent work only when it has actually started. Do not launch agents, run tasks, or perform side effects just to update a progress tracker. Progress tracking does not add permission to perform operations beyond the user's request.

## Resume and report

At a handoff, compare the latest evidence with tracker labels. Preserve completed evidence, active work, blockers, unrun required checks, and unanswered decisions. A tracker checkbox or overall label cannot override contradictory step evidence.

Report what is complete, what remains, what is blocked, and which user decision or evidence is needed next. Match the user's requested language, otherwise use the language of the latest request and default to English when indeterminate. Translate prose while preserving skill names, identifiers, commands, and technical status values.
