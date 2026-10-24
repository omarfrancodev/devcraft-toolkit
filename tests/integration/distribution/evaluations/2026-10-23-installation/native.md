# Native distribution evaluation

Date: 2026-10-23. Package snapshot: 72e190f0cceed4f42d70fca95213660fcb8fd9aa, version 0.1.0-preview.2 (unpublished). Environment: disposable Linux containers using the image in [environment.md](environment.md); native tools installed only in an owned tool prefix with npm lifecycle scripts disabled. Native runs had no network and no host profile, credentials, or personal plugin store mounted.

This matrix is **partially validated**. No row passed authenticated invocation, bundled-resource reads and all applicable scope/lifecycle assertions. Registration, component inventory and filesystem evidence do not establish those outcomes.

## Per-target matrix

All sixteen primary cells were initially not_run, except the unsupported Kiro project Power cell. The final states below retain the exact missing gates. Selected-skill filesystem passes refer to the separate Task 2 snapshot and do not change native states.

| Target | Delivery | Scope | Native state | Observed evidence and missing gates |
| --- | --- | --- | --- | --- |
| Codex CLI 0.162.0 | native suite | user | limited | Local marketplace add, plugin add/list/remove passed. No authenticated invocation/resource read or cross-project activation test. |
| Codex CLI 0.162.0 | native suite | project | limited | Registry regression verified user-disabled/project-enabled precedence and a disabled control project. Authenticated session activation, resources and lifecycle remain blocked. |
| Codex CLI 0.162.0 | standalone | user | blocked | Folder/resource copying passed separately; authenticated direct invocation and scope visibility pending. |
| Codex CLI 0.162.0 | standalone | project | blocked | Same missing native checks; no native-loader substitution from manual following. |
| Copilot in VS Code | native suite | user | blocked | No isolated authenticated Copilot session; VS Code host inventory alone is insufficient. |
| Copilot in VS Code | native suite | project | blocked | Workspace activation/control-project checks pending. |
| Copilot in VS Code | standalone | user | blocked | CLI/manual filesystem passed; native discovery, resource read and language pending. |
| Copilot in VS Code | standalone | project | blocked | Same native gates pending; shared root does not prove harness exclusivity. |
| Claude Code 2.1.300 | native suite | user | limited | Registered, installed, listed from both projects, inspected seven actual components, update reported local source, uninstall passed. Invocation/resource/lifecycle-version-change gates pending authentication. |
| Claude Code 2.1.300 | native suite | project | limited | Installed and listed enabled in selected project, disabled in control; local-source update and scoped uninstall passed. Active-session scope/invocation and complete lifecycle pending. |
| Claude Code 2.1.300 | standalone | user | blocked | CLI/manual filesystem passed; authenticated invocation/resource/scope checks pending. |
| Claude Code 2.1.300 | standalone | project | blocked | Same missing native gates; suite registry observations do not cover standalone loading. |
| Kiro IDE | native Power | user | blocked | No isolated Kiro IDE session or executable available. |
| Kiro IDE | native Power | project | not_supported | Approved interface does not establish project-only Power isolation. Use the separate skill-set fallback. |
| Kiro IDE | standalone | user | blocked | CLI selector copied files; IDE activation not tested. |
| Kiro IDE | standalone | project | blocked | CLI/manual copying passed; IDE discovery/resource/scope checks pending. |
| Kiro IDE | complete skill-set fallback | project | blocked | Seven-folder project fallback passed filesystem checks; native IDE activation remains blocked. |

## Observed client operations

[Raw command results and before/after hashes](native-cli-results.json), [runner](native-cli.mjs), [component/authentication observations](native-inventory-corrected-results.json), [inventory runner](native-inventory.mjs), and [initial diagnostic probe](native-inventory-results.json) are retained. The diagnostic probe incorrectly added --json to plugin details; help showed it unsupported, and the corrected command was run without it. The failed probe is not hidden.

Codex accepted the root marketplace and returned installed/enabled candidate metadata from plugin list. Removal succeeded. Marketplace upgrade exited 1 because the source is a local directory, not a Git marketplace. The guide now distinguishes local-source reload from Git refresh. This command result does not invalidate package registration, nor does registration prove runtime activation.

Claude's native manifest validator accepted both files. The marketplace validator reported one advisory: no marketplace description. It reported no errors. Marketplace registration and user/project installs succeeded. The project list reported enabled=true/projectEnabled=true in the selected project and enabled=false/projectEnabled=false in the control; the control sentinel hash stayed unchanged. This is registry/settings scope evidence, not proof of behavior in an active model session.

Claude plugin details enumerated exactly conventional-commits-style, git-safety-check, git-working-directory-policy, natural-language-report-writer, todo-workflow-controller, using-devcraft-toolkit and validation-discovery. It reported zero agents, hooks, MCP and LSP servers. No planned names appeared.

Claude update returned: the plugin is read from /source, with nothing to update; source edits apply next session or /reload-plugins. Both scoped uninstalls succeeded. There was no version-changing update, simultaneous other-scope installation, unrelated native plugin sentinel, or native invocation, so NATIVE-04 is not fully passed. No internal plugin cache was manually changed.

Claude auth status returned loggedIn=false/authMethod=none. No credentials were supplied. Codex invocation credentials were not provisioned either. No attempt was made to copy personal authentication, loosen trust/approvals, or call a remote model in an unauthenticated container.

## Remaining execution

- NATIVE-01/02: authenticated standalone and owned-entry invocation, actual discovered identifiers, one bundled reference/template read and English/Spanish output per applicable row.
- NATIVE-03: actual selected/control sessions, Codex activation with the verified project enablement, project-disabled global installation where supported, and standalone visibility.
- NATIVE-04: repeated native install, real updated source/version and resource verification, scoped removal with unrelated native plugins/settings and another scope present, plus required reload observations.
- Copilot: record the actual extension/harness version in the isolated session and test the inventory interface used for installation.
- Kiro: install/observe the IDE and test the user Power plus independent workspace skill-set fallback. CLI placement remains a different evidence level.

Task 4's native execution step remains incomplete/blocked. The implementation and documentation can be reviewed with these limitations; no all-four-harness compatibility claim, release, tag or public listing follows from this evidence.

## Codex project enablement regression

The final branch reviewer found that installing at user scope and adding project enabled=true leaves inherited user enablement active elsewhere. A real Codex CLI 0.162.0 probe in another disposable container reproduced the defect before the guide fix: plugin list reported selected=true and control=true. With only this plugin disabled in user config and enabled in the selected trusted project's config, it reported selected=true and control=false. The control sentinel survived; both owned fixture projects were explicitly trusted through normal trust-level configuration, without disabling global trust/approval protections.

[Raw RED-to-GREEN results](codex-project-scope-results.json) and [runner](codex-project-scope.mjs) retain settings and command outputs. Package files are the 72e190f snapshot, unchanged in 14bead6; the source field 14bead6 identifies the recipe revision being reproduced. The guide now separates global and project-only enablement and preserves unrelated preferences. An explicit enablement in another project remains that project's independent choice.

This adds registry precedence evidence only. Actual authenticated selected/control sessions and skill resource reads are still incomplete; the project native row is limited, not passed. The full automated suite was rerun after the documentation correction.
