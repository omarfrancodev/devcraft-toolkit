# Repository instructions

- Keep maintained source skills, documentation, examples, and default templates in English.
- All automated tests, scenarios, fixtures, and retained evaluations belong under the root `tests/` directory, grouped by skill and scope.
- Keep available skills self-contained. Declare cross-skill dependencies in `catalog.json`; do not link installed skills to root documentation.
- Planned catalog entries do not get placeholder `SKILL.md` files.
- Use explicit working directories for terminal commands. Inspect repository-local Git identity before Git writes; never change global identity.
- Milestone 1 skills perform no Git writes, network access, or credential changes.
- `natural-language-report-writer` may write only one explicitly requested, user-selected local report file and must read it back. It must not choose a destination, create extra files or directories, overwrite an existing file without explicit replacement authorization, or post externally; this exception grants no Git or network access.
- `validation-discovery` may execute only inspected local validation checks that the user or an authorized composing workflow requested, within the selected project or owned temporary fixture. Disclose expected local artifacts. Installation, update, autofix, cleanup, migration, deployment, publication, destructive operations and external business mutations need separate explicit authorization. Preserve unexpected changes and pause affected downstream writes; do not clean, reset, stage or rerun to hide them.
- Do not add plugin manifests, release automation, CCR integration, Jira integration, or a license without a separate approved design.
- Keep specifications, plans and skill instructions self-contained: define behavior, inputs, outputs, decisions and evidence without depending on conversations, personal paths, untracked material or unavailable projects.
- Describe capabilities through their current requirements and observable behavior. Use repository-local references and accessible official technical references; include all information needed to execute the design.
