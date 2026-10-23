---
name: using-devcraft-toolkit
description: Route repository, Git, project validation, and shared workflow requests to installed Devcraft Toolkit skills and compose their results in the user's language.
---

# Using Devcraft Toolkit

Load this entry only when the user asks for a Devcraft Toolkit capability or a coordinator the toolkit provides. Do not force it into unrelated requests.

## Resolve language and scope

Resolve the response language once per execution: use an explicit user preference, then the language of the user's request, then English if the language is indeterminate. A later explicit instruction can update that choice. Translate natural-language content and visible labels; preserve skill names, commands, identifiers, status values, and schema keys.

Determine the requested scope and the capabilities actually installed in the current harness. Use its skill discovery mechanism when available. `catalog.json` is a development inventory, not an installed runtime dependency. Do not try to open it or root documentation when only an individual skill is installed.

## Route available requests

- Conventional Commit message drafting or review: use `conventional-commits-style` when installed. It returns a proposal from supplied facts and conventions; it does not need repository context or a Git preflight. If it is absent, report that capability as unavailable. Do not emulate it or install it automatically.
- Portable progress tracking, required gates, blockers, decisions, or handoffs: use `todo-workflow-controller` when installed. It tracks the workflow but does not execute its steps or grant permission for side effects. If the skill is absent, report that capability as unavailable; do not imitate it or install it automatically. A workflow step named `publish` does not itself request Git publication, so do not run a Git preflight or publication workflow solely because that step appears in the task.
- Repository location, worktree, branch, or identity context: use `git-working-directory-policy` when installed.
- Read-only Git safety preflight for a request to inspect repository safety or assess readiness for a Git operation: use `git-safety-check` when installed, with its declared `git-working-directory-policy` dependency. A request to draft or review commit-message text alone does not request this preflight.
- Project validation discovery or explicitly requested local checks: use `validation-discovery` when installed. Let that skill select and assess commands from project evidence; do not impose a fixed command-name allowlist or run a Git preflight solely to discover checks. Its default discovery mode does not execute commands. If it is absent, report that capability as unavailable; do not emulate it or install it automatically.
- Evidence-based report writing from user-supplied facts: use `natural-language-report-writer` when installed. It writes in the resolved user language and returns report content in the conversation by default; local output requires an explicitly selected destination. If the skill is absent, report it as unavailable without imitation or automatic installation.
- Git activity reporting from commit history: the `git-activity-report` coordinator is planned and unavailable in this distribution. Do not substitute evidence-based report writing for Git-history inspection or claim a history report was produced.
- Commit creation and coordination and publication coordination are planned and unavailable in this distribution. State that clearly; do not silently emulate missing coordinators or modify another installation. Conventional Commit formatting does not create a commit.
- Any request outside toolkit scope: handle it without loading this entry.

If a requested capability is absent, report the actual limitation and offer only an in-scope available alternative when one exists. Catalog entries and dependencies do not grant tools, permissions, authorization, or automatic installation.

## Compose results

Keep a concise in-memory run context with the resolved language and its source, requested scope, decisions, and capabilities actually available. This is ordinary working context, not a persisted JSON state machine. Reuse repository facts already collected; refresh only facts that can have changed before a decision that depends on them.

Present the evidence and result from the invoked skill in the resolved language. Do not overstate what the skill observed or claim an operation was completed when only a preflight was performed. An unanswered material decision pauses dependent work. A missing native progress or structured-question tool does not make an installed capability unavailable; use its documented fallback. A missing skill is distinct and follows the unavailable-capability rule above.

Use the local [composition reference](references/composition.md) for dependency and result boundaries.
