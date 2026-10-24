# Filesystem installation scenarios

These packets exercise actual file effects, not native harness loading. Source is the local package snapshot; selected folders and resources must match its bytes. Use Skills CLI 1.7.4 with copies, explicit target and selection, and a disposable environment. Do not run these packets against personal installations.

## Matrix and selections

Targets: codex, github-copilot, claude-code, kiro-cli. Scopes: project and user/global. Test each of the seven requested skills using its complete closure, plus the full set.

- using-devcraft-toolkit: using-devcraft-toolkit, git-working-directory-policy, git-safety-check
- git-safety-check: git-safety-check, git-working-directory-policy
- git-working-directory-policy: itself
- conventional-commits-style: itself
- todo-workflow-controller: itself
- natural-language-report-writer: itself
- validation-discovery: itself
- full: all seven names above

## FS-01 — Independent copy and scope

Create a selected project and a control project with unrelated sentinel files. Install natural-language-report-writer, including references/report-quality.md and assets/report.md, into the selected target/scope. Assert byte equality, actual destination, no symlink in copy mode, preserved sentinels, and absence of writes in the other scope. Shared target discovery roots are not an isolation guarantee.

## FS-02 — Required dependency closure

Install the explicitly selected entry trio and preflight pair. Assert each selected directory exists and contains all source resources. No custom catalog dependency resolution is inferred. Also inspect a direct bare entry selection to characterize the external CLI: report missing dependencies rather than pretending they were resolved.

## FS-03 — Seven selections and full suite

For every target and both scopes, exercise each complete individual closure and the full set in a fresh case. Compare installed directory names and file bytes, reject all ten planned names, and record canonical storage and lock artifacts. Repeat with complete-folder manual copying, clearly labeled as filesystem-only evidence.

## FS-04 — Existing personal content

Create a same-name skill with different content plus an unrelated skill/sentinel in a disposable home/project. Inspect collisions before any replacement. Without replacement authorization, stop this packet's install and assert both existing contents remain unchanged. Do not use --yes to pretend that the external tool protects collisions automatically.

## FS-05 — Lifecycle

After explicit replacement authorization in the disposable case, reinstall the selected skill and observe the result. Update the local source fixture and explicitly add it again with the same target/scope; verify the changed copy, unchanged unrelated files and other scope. Remove only the named skill with explicit target/scope. Record the exact CLI arguments, exit codes, lock changes, and any shared-store effect. Copy updates are not automatic symlink refreshes.

## Evidence contract

Record Node/CLI/OS and source revision, every target/scope/selection, actual destination and canonical storage, before/after inventories, exit code and observed assertions. Missing tools are blocked/not_run. Global tests require an actual disposable OS/container home, not an unverified HOME override of a desktop client. Kiro's CLI selector verifies directory placement; only a later Kiro IDE session can verify IDE loading.
