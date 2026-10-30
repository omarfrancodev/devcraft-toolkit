# Devcraft Toolkit

A modular toolkit of composable skills for repository context, Git inspection and planning, exact authorized staging, requested local commits, scoped branch synchronization and publication, hosted PR/MR management and explicit promotion, project validation, reporting, and portable progress tracking. Compatibility is recorded only for harnesses actually exercised.

Release preview.9 contains eighteen skills with client-specific plugin presentation and explicit Codex selector labels, including independent work-branch creation and full publication coordination. CCR integration remains deferred.

Skill definitions and default templates use English. User-facing content follows an explicit language preference or the language of the user's request, defaulting to English when neither can be determined. Tests are maintained outside individual skill directories, grouped by the owning skill and then by test scope; repository infrastructure and cross-skill coverage have separate shared groups.

The [approved inventory](docs/capability-inventory.md) and [catalog](catalog.json) contain eighteen available capabilities, with no planned placeholders. Current source retains those capabilities from `0.1.0-preview.8` and adds presentation metadata in `0.1.0-preview.9`. See [installation](docs/installation.md), [architecture](docs/architecture.md), [language behavior](docs/language.md), and [compatibility evidence](docs/compatibility.md).

The [capability roadmap](docs/roadmap.md) links the self-contained designs and plans for upcoming increments.

## Install the complete suite

Install the complete toolkit directly from GitHub using your client's documented route. Native plugins/Powers deliver all available skills from the selected source; Crew imports the complete skill set. Kiro CLI without an IDE has an explicit full-set alternative. No user-managed clone is needed.

Choose [Codex](docs/installation/codex.md), [Copilot CLI](docs/installation/copilot-cli.md), [Copilot in VS Code](docs/installation/copilot-vscode.md), [Claude Code](docs/installation/claude-code.md), [Kiro CLI V3](docs/installation/kiro-cli.md), [Kiro IDE](docs/installation/kiro.md), or [Kiro Crew](docs/installation/kiro-crew.md). The [installation overview](docs/installation.md) explains scope and the Kiro project fallback.

Default remote recipes deliver all eighteen skills after this increment is integrated. See [preview.9 release details](docs/releases/v0.1.0-preview.9.md) for version-pinned source options; [earlier preview sources](docs/installation/preview.md) are historical evidence. Native activation remains partially validated; no official catalog listing is claimed.

Need selected capabilities instead? Use [individual skill installation](docs/installation/individual-skills.md). Package contributors and manual-copy users can use [local development/reference](docs/installation/development.md).

## Preview release

[v0.1.0-preview.9](https://github.com/omarfrancodev/devcraft-toolkit/releases/tag/v0.1.0-preview.9) adds plugin branding, supported per-client metadata and explicit skill labels to the complete eighteen-skill suite. See the [changelog](CHANGELOG.md), [release details](docs/releases/v0.1.0-preview.9.md) and [installation guide](docs/installation.md). Native compatibility remains partial.

Preview.6 introduced independent synchronization and push. Synchronization performs an explicitly requested one-branch fetch and eligible fast-forward only. Publication sends one pinned commit to one branch and verifies its effective endpoint. Each has an independent context/safety closure of three skills and defaults to offline inspection. Ignored-file collisions and symbolic tracking destinations stop affected writes. Requested upstream setup requires an existing usable mapping/ref and actual resolution; incomplete setup preserves verified publication and actual state. See the [design](docs/superpowers/specs/2026-10-25-git-sync-publish-design.md), [plan](docs/superpowers/plans/2026-10-25-git-sync-publish.md) and [roadmap](docs/roadmap.md).

Earlier [preview.8](docs/releases/v0.1.0-preview.8.md) introduced work branches/publication coordination with eighteen skills; [preview.7](docs/releases/v0.1.0-preview.7.md) retains sixteen skills; [preview.6](docs/releases/v0.1.0-preview.6.md) retains fourteen skills, and [preview.5](docs/releases/v0.1.0-preview.5.md) retains twelve skills with local-history reporting. [Preview.4](docs/releases/v0.1.0-preview.4.md) retains eleven skills with staging and local commit construction, [preview.3](docs/releases/v0.1.0-preview.3.md) has nine, [preview.2](docs/releases/v0.1.0-preview.2.md) has seven, and preview.1 is source-only. Historical native registration/resource evidence does not establish activation of added skills.

## Hosted requests and explicit promotion

`git-manage-pull-request` proposes or observes a selected PR/MR and may create it or edit selected title/body fields when explicitly requested. Its direct closure has two folders: management and context. `git-promote` adds a third folder and may perform one expressly requested source-conditional normal merge of an existing request after current policy/review/check gates. Both default to offline assessment, preserve local work and do not imply push, branch cleanup, release or deployment.

See the [approved design](docs/superpowers/specs/2026-10-25-git-pr-promotion-design.md), [plan](docs/superpowers/plans/2026-10-25-git-pr-promotion.md), [standalone selections](docs/installation/individual-skills.md) and [evidence limits](docs/compatibility.md). The changelog and release preparation belong to PR #9; its exact merge commit is the tag/asset source. Preview.6 retains fourteen skills and historical native probes keep their original scope.

## Work branches and publication coordination

`git-create-work-branch` can independently create and select a new local branch at the current committed HEAD while preserving partial staging and all local work. `git-publish-work` coordinates only the selected goal: necessary branch creation, full commit preparation, normal push and optional PR/MR work, with synchronization and merge only when explicitly requested. It forecasts known blockers before earlier writes and preserves actual partial effects.

Standalone branch creation needs two folders; basic coordination needs five. Additional owners are conditional on the selected flow. See the [design](docs/superpowers/specs/2026-10-26-git-work-publication-design.md), [plan](docs/superpowers/plans/2026-10-26-git-work-publication.md), [composition](docs/composition.md) and [exact installation selections](docs/installation/individual-skills.md). Native activation and authenticated provider validation remain open.
