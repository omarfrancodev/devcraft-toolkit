# Repository instructions

- Keep maintained source skills, documentation, examples, and default templates in English.
- All automated tests, scenarios, fixtures, and retained evaluations belong under the root `tests/` directory, grouped by skill and scope.
- Keep available skills self-contained. Declare cross-skill dependencies in `catalog.json`; do not link installed skills to root documentation.
- Planned catalog entries do not get placeholder `SKILL.md` files.
- Use explicit working directories for terminal commands. Inspect repository-local Git identity before Git writes; never change global identity.
- Milestone 1 skills perform no Git writes, network access, or credential changes.
- Do not add plugin manifests, release automation, CCR integration, Jira integration, or a license without a separate approved design.
