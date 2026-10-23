# Architecture

Devcraft Toolkit is a maintained collection of composable, instruction-first skills. `catalog.json` records each capability's canonical name, role, planned or available status, installation path, and declared skill dependencies. It is a project inventory, not a plugin or installer standard.

Skills are independently usable unless their catalog entry declares a dependency. Each available skill keeps its references within its own folder. A standalone installation must include the skill's declared dependency closure; the catalog does not cause an installer to fetch it.

The repository validator and tests are development tools. Installed skills do not depend on them at runtime. Repository tests are grouped under `tests/repository/`, `tests/skills/<normalized-skill-name>/`, or shared integration/support areas when they cover multiple named skills.

The current distribution has seven available skills and ten planned entries. The available set is `using-devcraft-toolkit`, `git-working-directory-policy`, `git-safety-check`, `conventional-commits-style`, `todo-workflow-controller`, `natural-language-report-writer`, and `validation-discovery`; the entry depends on both supporting skills; the formatter, progress controller, report writer, and validation discovery remain independently usable with no dependencies. Centralized structural validation and behavioral scenarios live under the repository root's `scripts/` and `tests/` directories.

CCR workflows, a custom automatic installer, and release automation remain deferred. Native plugin packaging and selective installation have a proposed [design](superpowers/specs/2026-10-23-distribution-installation-design.md); metadata and native compatibility remain unimplemented and unverified by this documentation increment. See [installation](installation.md), [composition](composition.md), and [compatibility evidence](compatibility.md) for user-facing constraints.

See the [capability roadmap](roadmap.md) for the sequence of product increments.
