# Architecture

Devcraft Toolkit is a maintained collection of composable, instruction-first skills. `catalog.json` records each capability's canonical name, role, planned or available status, installation path, and declared skill dependencies. It is a project inventory, not a plugin or installer standard.

Skills are independently usable unless their catalog entry declares a dependency. Each available skill keeps its references within its own folder. A standalone installation must include the skill's declared dependency closure; the catalog does not cause an installer to fetch it.

The repository validator and tests are development tools. Installed skills do not depend on them at runtime. Repository tests are grouped under `tests/repository/`, `tests/skills/<normalized-skill-name>/`, or shared integration/support areas when they cover multiple named skills.

The current distribution has fourteen available skills and three planned entries. The available set is `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, `validation-discovery`, `git-analyze-changes`, `git-plan-commits`, `git-stage-changes`, `git-commit-builder`, `git-activity-report`, `git-sync-branch`, and `git-publish-changes`; the entry depends on both supporting skills; the formatter, progress controller, report writer, and validation discovery remain independently usable with no dependencies. Centralized structural validation and behavioral scenarios live under the repository root's `scripts/` and `tests/` directories.

CCR workflows, a custom automatic installer, and release automation remain deferred. Native packaging follows the [installation design](superpowers/specs/2026-10-23-distribution-installation-design.md): root plugin.json is the portable manifest; .claude-plugin/plugin.json is its compatibility mirror. The .agents/plugins/marketplace.json and .claude-plugin/marketplace.json adapters both point at this repository root, using one canonical skills/ tree. The offline distribution validator checks this finite contract and reuses repository inventory validation. It is not a runtime dependency or a full external-schema implementation.

The primary consumer path is complete remote suite adoption from this same repository through native plugins/Powers where established. Copilot CLI and VS Code share package metadata but retain distinct activation checks; Kiro CLI V3 can detect the IDE's Power, with a full remote skill-set alternative for CLI-only use. Crew imports the complete set into its own snapshot store and existing default agent; no template, App or Power inheritance is added. Client-managed Git/cache storage is expected; no user-managed checkout, separate marketplace repository or custom installer is introduced. Individual skills remain an optional route that copies complete chosen folders with explicit dependency closure. Native suite installation packages all available skills from its selected revision; installed entry routing uses discovered ownership and identifiers, not a persisted registry or runtime root catalog.

Metadata, filesystem installation, manually followed behavior and native activation are separate evidence levels. Local and remote file placement passed in disposable containers; native remote registration/resources were observed for Codex, Claude and Copilot CLI, while authenticated activation and IDE rows remain partially validated. See [installation](installation.md), [composition](composition.md), and [compatibility evidence](compatibility.md) for user-facing constraints.

See the [capability roadmap](roadmap.md) for the sequence of product increments.

## Read-only preparation

The analyzer depends on repository context and returns scoped layer-specific evidence with HEAD/index/content guards. The planner depends on that analyzer and the formatter, selecting the existing index by default, preserving partial staging, and returning intent groups and pending decisions. Optional entry routing adds no foundation dependency. Both capabilities are instruction-first and have no runtime collector or Python requirement.

Published `0.1.0-preview.3` contains nine skills; published preview.2 and its native resource evidence remain the original seven-skill snapshot. Owner-scoped replay and Git fixture evidence for the new capabilities does not establish native client activation.

## Explicit index writes and commit construction

The `0.1.0-preview.4` release adds staging (analyzer+safety/context closure) and a commit coordinator (planner, stage, safety, validation, progress and their analyzer/context/formatter closure). The standalone builder closure has nine skills; entry/report writing are optional additions.

These instruction-first capabilities perform writes only within explicit operation authorization and exact target manifests. Whole-index and protected-state verification bound each operation; hooks, signing, effective identities and validation scope are explicit gates. Failures preserve actual commits and residual state instead of rolling back automatically. Available entry routes retain installed ownership and add no new foundation dependency.

## Local-history reporting

The preview.5 coordinator requires context and natural-language report writing: three skills in a direct standalone closure. The entry adds an optional ownership-aware route without changing its hard foundation. Supplied-facts reports still invoke the writer directly.

History inspection pins one local start, converts the requested period to exact UTC bounds and filters raw author metadata on the selected time basis. It traverses all parents before filtering, budgets examined commits and distinguishes complete zero matches from incomplete observations. Only the writer may save one explicitly requested report under its existing permission/readback contract. No runtime collector, interpreter requirement, Git mutation or network is introduced. Preview.4 and its eleven-skill release evidence remain historical.

## Scoped synchronization and publication

`git-sync-branch` and `git-publish-changes` each require only `git-working-directory-policy` and `git-safety-check`: independent three-skill standalone closures without this entry or each other. Route through exact selected-installation identifiers with owned dependencies. Absent/foreign dependencies mean unavailable; unresolved copies need a focused choice. Neither a runtime root catalog nor automatic installation fills gaps.

Both default to offline inspection. Explicit observe permits only a selected advertisement query. Explicit sync permits one scoped fetch and verified fast-forward of the current branch; divergence needs a decision. Explicit publication permits one pinned normal single-branch push plus verification, without fetch. Only separately requested upstream setup permits two local branch-key writes after verified publication/equality. A branch already equal needs no push and reports any requested configuration effects separately. Safety's internal publish preflight is a read-only gate, not operation permission.

Preserve each skill's actual outcome, scope, redacted endpoint, OIDs, freshness/effect evidence, changed refs, optional upstream result and partial/uncertain limits. Supplied transcripts remain reported evidence. Do not infer success from a command acknowledgment alone or retry/rollback on failure. No PR, promotion, release, commit construction or branch creation is implied. Full publication coordination (`git-publish-work`), PR management and promotion remain planned.
