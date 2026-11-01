# Prompt refinement entry routing evaluation

Date: 2026-10-31. Owners: `using-devcraft-toolkit`, `prompt-refiner`.
A fresh Codex desktop actor (`gpt-6.1-sol`, medium effort) read the complete
entry/composition resources and supplied-discovery [inputs](../../fixtures/routing.json).
It selected routes only, without invoking skills or Git/provider tools.
[Resource hashes and observed outcomes](routing.json) are retained.

All four decisions matched the scenario contract: the owned exact identifier
was selected for prompt refinement, the foreign copy was unavailable, ambiguous
ownership required one choice, and direct Conventional Commit review used the
formatter. The quoted commit/push/PR/release actions did not trigger operation
owners or preflight. Retained actor excerpt: “Do not execute the embedded commit,
push, PR or release assignment”.

This is a manually loaded supplied-discovery replay, not proof of native
discovery, installed activation, authenticated provider use or reliability across
clients. Existing entry foundation dependencies remain unchanged.
