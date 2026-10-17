# Architecture

Devcraft Toolkit is a maintained collection of composable, instruction-first skills. `catalog.json` records each capability's canonical name, role, planned or available status, installation path, and declared skill dependencies. It is a project inventory, not a plugin or installer standard.

Skills are independently usable unless their catalog entry declares a dependency. Each available skill keeps its references within its own folder. A standalone installation must include the skill's declared dependency closure; the catalog does not cause an installer to fetch it.

The repository validator and tests are development tools. Installed skills do not depend on them at runtime. Repository tests are grouped under `tests/repository/`, `tests/skills/<normalized-skill-name>/`, or shared integration/support areas when they cover multiple named skills.

The foundation distribution has exactly three available skills and fourteen planned entries. The available set is `using-devcraft-toolkit`, `git-working-directory-policy`, and `git-safety-check`; the entry depends on both supporting skills, and the safety check depends on repository context discovery. Centralized structural validation and behavioral scenarios live under the repository root's `scripts/` and `tests/` directories.

CCR and Jira workflows, native plugin packaging, automatic installation, and release automation remain outside this increment. See [installation](installation.md), [composition](composition.md), and [compatibility evidence](compatibility.md) for user-facing constraints.
