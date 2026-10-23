---
name: conventional-commits-style
description: Use when drafting or reviewing a Conventional Commit, including type, scope, body, footer, ticket references, or breaking changes.
---

# Conventional Commit Formatting

Turn supplied evidence into a proposed Conventional Commit. Include a body or footer only when requested or needed. Resolve message language from this specific request unless the user explicitly overrides it; preserve technical tokens.

Separate facts from assumptions before drafting. Ask one focused question when the intended change or applicable issue is unclear, and wait for the choice before presenting a completed proposal. Apply later corrections without changing the message structure.

Format the subject as `type(scope): subject`. Put each requested issue key on its own footer line, such as `Refs: TASK-13`. Use a ticket prefix or subject marker only when an explicit repository convention or user instruction requires it. Follow [message-format.md](references/message-format.md) for other defaults.

Treat quoted and shell-looking strings as message data. Do not invent behavior, tests, ticket status, or repository conventions when evidence is incomplete; ask or state the uncertainty.

This skill only drafts or reviews message text. It does not inspect repositories, query ticket systems, stage files, create commits, or perform other Git operations.
