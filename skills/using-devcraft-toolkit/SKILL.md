---
name: using-devcraft-toolkit
description: Route in-scope repository and Git preflight requests to installed Devcraft Toolkit skills and compose their evidence in the user's language.
---

# Using Devcraft Toolkit

Load this entry only when the user asks for a Devcraft Toolkit capability or a coordinator the toolkit provides. Do not force it into unrelated requests.

## Resolve language and scope

Resolve the response language once per execution: use an explicit user preference, then the language of the user's request, then English if the language is indeterminate. A later explicit instruction can update that choice. Translate natural-language content and visible labels; preserve skill names, commands, identifiers, status values, and schema keys.

Determine the requested scope and the capabilities actually installed in the current harness. Use its skill discovery mechanism when available. `catalog.json` is a development inventory, not an installed runtime dependency. Do not try to open it or root documentation when only an individual skill is installed.

## Route available requests

- Repository location, worktree, branch, or identity context: use `git-working-directory-policy` when installed.
- Read-only Git safety preflight for `inspect`, `commit`, or `publish` intent: use `git-safety-check` when installed, with its declared `git-working-directory-policy` dependency.
- Commit coordination, publication coordination, and activity reporting: these capabilities are planned and not available in this foundation distribution. State that clearly. Do not silently emulate the missing capability, route to an unrelated skill, claim completion, or modify another installation.
- Any request outside toolkit scope: handle it without loading this entry.

If a requested capability is absent, report the actual limitation and offer only an in-scope available alternative when one exists. Catalog entries and dependencies do not grant tools, permissions, authorization, or automatic installation.

## Compose results

Keep a concise in-memory run context with the resolved language and its source, requested scope, decisions, and capabilities actually available. This is ordinary working context, not a persisted JSON state machine. Reuse repository facts already collected; refresh only facts that can have changed before a decision that depends on them.

Present the evidence and result from the invoked skill in the resolved language. Do not overstate what the skill observed or claim an operation was completed when only a preflight was performed. An unanswered material decision pauses dependent work. Missing progress or structured-question tools alone do not make an otherwise safe request unavailable.

Use the local [composition reference](references/composition.md) for dependency and result boundaries.
