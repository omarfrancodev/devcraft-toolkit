# Suite and Selective Skill Installation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the complete remote suite the main installation path; retain individual skills as an alternative and local installation as development/reference documentation across seven local clients.

**Architecture:** Keep the existing skill tree canonical. Add portable and Claude metadata plus two marketplace adapters; validate the adapters offline and test real installations separately. Use established native clients and the optional pinned Skills CLI rather than building an installer.

**Tech Stack:** Markdown, JSON, Python 3.11+, existing PyYAML>=6.0,<7.0 development dependency, unittest, and the actual Codex, Copilot CLI, VS Code/Copilot, Claude Code, Kiro CLI V3, Kiro IDE, Crew and optional Node.js/npm Skills CLI versions recorded during execution.

**Spec:** [Suite and selective skill installation design](../specs/2026-10-23-distribution-installation-design.md).

## Global Constraints

- Canonical skill source remains `skills/<canonical-name>/`; seven available skills, ten planned entries.
- Plugin and marketplace name are both `devcraft-toolkit`; qualified identity is `devcraft-toolkit@devcraft-toolkit`.
- Candidate package version is `0.1.0-preview.2`, unpublished; do not modify `v0.1.0-preview.1`.
- Root schema is `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`.
- All maintained instructions, examples, default templates, and documentation use English; invoked output follows the user's resolved language.
- Tests, fixtures, scenarios, and retained evaluations stay under root `tests/`, grouped by owning skill or shared integration scope.
- No custom runtime installer, automatic dependency resolution, MCP server, hooks, new skills, CCR integration, license, release automation, or publication.
- Kiro CLI V3, Kiro IDE and Crew are separate clients with separate evidence; Crew gets full native skill import, no new template or App. A project-only Power install is `not_supported` unless a documented, reviewed interface establishes it; the project skill-set fallback is a separate delivery mode.
- Real user/global installations require a safely isolated client environment. Mock loaders, metadata checks, folder copies, or manual instruction following do not establish native compatibility.
- Remote checks use existing public revision b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e; default-source recipes apply after integration. No fabricated release ref or official listing.
- README/target quickstarts require no user-managed clone; native plugins need no Skills CLI. Label Kiro CLI-only full-set fallback and Crew snapshot import explicitly.
- Before Git writes inspect repository-local identity. Stage only the current task's explicit files.

## Review Focus

1. Before integration the default branch lacks metadata: current preview recipes must use actual published sources, without claiming that the source-only preview or default source can already install the plugin.
2. Client ref semantics differ: Codex's fixed SHA, Claude's mutable preview branch and unverified Kiro ref import must not be advertised as one universal immutable pin.
3. Project-only setup must not inherit unwanted user enablement; a control project and the Kiro project skill-set exception remain explicit even in short quickstarts.
4. The native suite must contain all seven resources without manual selection, while the optional route preserves explicit dependency closures and does not promise automatic resolution or exclusive discovery.
5. Missing authentication/IDE/Crew sessions and file-only evidence must remain limited/blocked. Crew must use its own source store and existing-agent mappings; no template or Power inheritance can be assumed.

## Prerequisites and file responsibilities

This plan implements the linked design, not the separate scope-cleanup changes already present in its branch. Read `AGENTS.md`, `catalog.json`, `docs/installation.md`, `docs/composition.md`, and `docs/compatibility.md`. The spec contains all package constants, dependency sets, directory mappings, native scope semantics, and official references.

Work in an isolated checkout. Confirm an actual Python interpreter can import PyYAML before running tests; use explicit working directories. Do not install dependencies into a maintainer's global Python or modify real client profiles merely to run a check.

The four tasks below are ordered by their interfaces. Tasks 1 and 2 deliver a usable package and concrete selective procedures; Task 3 makes entry discovery ownership-aware; Task 4 establishes the actual supported matrix. Each task has its own reviewable result and commit.

### Task 1: Native package metadata and offline distribution validation

**Files:**
- Create: `plugin.json`, `.claude-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`.
- Create: `scripts/validate_distribution.py`.
- Create: `tests/repository/test_distribution_validation.py`.
- Modify: `CONTRIBUTING.md` to include the new development check.

**Interfaces:**
- Consumes: `catalog.json` entries `name`, `status`, `path`, `requires` and `scripts.validate_repository.ValidationIssue(code: str, path: str, message: str)`.
- Produces: `validate_distribution(root: Path) -> list[ValidationIssue]` and `main(argv: list[str] | None = None) -> int`.
- CLI: `python -B -m scripts.validate_distribution --root .`, exit 0 when valid, exit 1 for distribution contract violations. Reads only local files and emits a result or relative-path diagnostics.
- Diagnostic codes: `distribution-metadata` (missing/malformed/schema/name/description/author/shape), `distribution-version` (invalid or inconsistent versions), `distribution-source` (missing, escaping, or non-root adapter source), `distribution-inventory` (missing, duplicated, or planned discovered skills; invalid dependency closure).

- [x] **Step 1: Add the failing regression cases.**

Create `DistributionValidationTests` with `make_root(self) -> Path`, an owned temporary fixture containing the catalog, available skill directories, and candidate metadata. Do not copy Git state, distributions, or private profiles. Add:
`test_valid_distribution`, `test_manifest_identity_must_match`, `test_manifest_versions_must_match`, `test_malformed_metadata_is_reported`, `test_marketplace_source_resolves_repository_root`, `test_marketplace_source_cannot_escape`, `test_duplicate_marketplace_plugin_is_reported`, `test_missing_available_skill_is_reported`, `test_planned_skill_is_not_discoverable`, `test_duplicate_skill_copy_is_reported`, and `test_dependency_closure_rejects_missing_or_planned_dependency`.

Core assertions include:
```python
self.assertEqual([], validate_distribution(self.make_root()))
# In the version-skew fixture, change only the Claude manifest version.
self.assertIn("distribution-version", {item.code for item in validate_distribution(root)})
# A source ../outside must yield distribution-source even if that directory exists.
# Removing validation-discovery must yield distribution-inventory.
# Adding skills/git-commit-builder/SKILL.md must yield distribution-inventory.
```

Check exact metadata fields and source values from the spec. Mutation cases must reach their intended guard rather than fail because another fixture component is missing.

- [x] **Step 2: Confirm the intended RED result.**

Run `python -B -m unittest tests.repository.test_distribution_validation -v`. Expected: failure because `scripts.validate_distribution` is absent. Record the result; do not count setup/dependency failures as the intended assertion evidence.

- [x] **Step 3: Implement the metadata and finite offline validator.**

Write the four exact manifest/marketplace shapes from the spec. Treat portable paths and the seven existing folders as canonical; add no skills override to the Claude manifest. Use the root manifest as the canonical version, verify SemVer-shaped version text and exact mirror equality, and resolve both marketplace sources against the repository root with containment checks. Compare discovered skill names and resources with available catalog entries; reject additional copies and planned skill folders. Reuse the repository validator for existing catalog/resource constraints rather than duplicating its Markdown parser.

Implement the two declared functions in `scripts/validate_distribution.py`. Keep import/CLI execution compatible with `python -m scripts.validate_distribution`. Do not fetch remote schemas or claim full external schema validation.

- [x] **Step 4: Verify the deliverable and document the check.**

Run the targeted tests and the new CLI; expect all cases pass and CLI exit 0. Run the existing repository validator and full unittest suite. Update `CONTRIBUTING.md` with the new check and explain the distinction between contract validation and native loading. If the Claude CLI is available in the isolated environment, separately run its documented plugin validator; otherwise record it unrun.

- [x] **Step 5: Commit the explicit Task 1 files.**

Suggested message: `feat: agregar metadatos de distribución del toolkit`. Review the staged diff and verify that no install was performed and no real profile was touched.

### Task 2: Selective installation and the four target guides

**Files:**
- Create: `docs/installation/codex.md`, `docs/installation/copilot-vscode.md`, `docs/installation/claude-code.md`, `docs/installation/kiro.md`.
- Create: `tests/integration/distribution/scenarios/installation.md`.
- Create: `tests/integration/distribution/evaluations/<run>/filesystem.md` and `environment.md` during actual execution.
- Modify: `docs/installation.md` and `README.md`.

**Interfaces:**
- Consumes: Task 1's native package, the spec's seven dependency closures, and its four-selector destination matrix.
- Produces: concrete native and standalone procedures, a recorded exact Skills CLI version if used, and filesystem evidence keyed by `target / delivery / scope / selection`.
- No new installer function or runtime dependency is introduced.

- [x] **Step 1: Write explicit scenario packets before executing installations.**

In `installation.md` define `FS-01` through `FS-05`:
- `FS-01`: each of four targets and both scopes; select one independent skill, then check bytes, local resources and destination.
- `FS-02`: entry trio and preflight pair; verify their complete selected sets, not one bare skill or automatic dependency installation.
- `FS-03`: each remaining individual selection and the full seven-skill set; verify no planned skill is copied.
- `FS-04`: pre-existing same-name personal skill and unrelated sentinel directory; detect collision before replacement, preserve both without explicit replacement authorization.
- `FS-05`: reinstall, update, and remove one selected set; inventory effects and lock files, preserve unrelated files and the other scope.

Each packet specifies selected names, target, scope, source ref, exact allowed destination and expected artifacts. Initial evidence is `not_run`. Manual copying and the external CLI have separately identified results. Use disposable homes/projects; do not call them native loader tests.

- [x] **Step 2: Observe the existing gap, inspect the external CLI, and select the test environment.**

Record that the current guide lacks target-specific tested commands rather than inventing a failing runtime test for prose. If using the Skills CLI, inspect the available published version and package/help, record its exact numeric version and supported selectors, then pin it. Obtain it only in the isolated tool environment; this install is an explicit installation test, not an ordinary validation command.

Confirm safe homes/profiles and a project plus control project. If unavailable, record the affected packets `blocked` and retain concrete manual recipes; do not use the real maintainer account as a fallback.

- [x] **Step 3: Execute and record the filesystem matrix.**

Use a local copy of Task 1's package to avoid relying on an unpublished tag. Run the pinned CLI with explicit `--skill` values, one `--agent` selector, `--copy`, and the chosen scope; verify actual files and resource bytes against the source. Record shared discovery roots: a target selector is not cross-harness access control, and a shared .agents/skills path can be seen by both Codex and Copilot. Do not use `--all`. Exercise all seven requested closures and the full set for each target/scope. Independently exercise manual complete-folder copying.

For Kiro, `kiro-cli` identifies the CLI writer; its output directories must be checked against Kiro IDE's documented paths. Do not count this as IDE discovery. For each expected artifact, record its destination and observed contents, including CLI locks or canonical shared storage outside the displayed target directory. Unexpected effects pause that packet and are preserved.

- [x] **Step 4: Write the overview and four concrete target guides.**

Include source/ref selection; requirements; exact tested CLI commands and their recorded version; manual copying; every dependency set; native suite route; user/project scope semantics; invocation/discovery; update/removal; collisions; and evidence links. Give a full-suite and individual-skill example in both scopes per target. Use the dependency table for the remaining individual choices instead of duplicating dozens of equivalent commands.

Codex guide distinguishes shared cache from project enablement. Copilot guide distinguishes user install, workspace activation and collaborator recommendations. Claude guide includes marketplace registration and explicit `--scope user`/`--scope project`. Kiro guide labels the global Power route and the project seven-skill fallback separately. A blocked test remains visibly unverified in the guide, not silently converted to a supported claim.

Use actual local source commands during development. Released examples may name only a Git ref that actually exists and was verified. Do not present candidate `v0.1.0-preview.2` as already published.

- [x] **Step 5: Verify and commit the Task 2 deliverable.**

Check all local Markdown links, completeness of the selection/scope table, and recorded before/after inventories. Run both development validators and `git diff --check`. Confirm default templates and skill resources have not been rewritten by installation. Commit the explicit overview, guides, scenarios and retained non-private evidence. Suggested message: `docs: documentar instalación selectiva por harness y alcance`.

### Task 3: Ownership-aware entry routing

**Files:**
- Modify: `skills/using-devcraft-toolkit/SKILL.md` and `skills/using-devcraft-toolkit/references/composition.md`.
- Modify: `tests/skills/using_devcraft_toolkit/scenarios/routing-and-language.md`.
- Create: `tests/skills/using_devcraft_toolkit/evaluations/<run>/installation-routing.md`.
- Modify: `docs/composition.md`.

**Interfaces:**
- Consumes: canonical catalog names and actual harness discovery metadata, including package ownership and user-selected installation.
- Produces: instruction-level canonical-to-discovered invocation mapping for this package. No string-only namespace stripping, runtime registry, or persisted resolver.

- [x] **Step 1: Add four behavioral packets.**

`ROUTE-INSTALL-01`: this package owns an installed namespaced formatter; ask the entry to draft a commit message from supplied facts. Expect invocation through the discovered identifier, correct request language and no Git preflight.

`ROUTE-INSTALL-02`: only a foreign plugin exposes the same canonical optional name. Expect this capability reported unavailable, without foreign invocation, imitation, or installation.

`ROUTE-INSTALL-03`: package and standalone copies both exist with unresolved ownership/selection. Expect one focused installation choice before dependent invocation; preserve both copies.

`ROUTE-INSTALL-04`: the user selected one available installation and another exists. Expect that exact installation used; a missing optional capability is still reported absent. Do not treat another installed copy as implicit permission to substitute.

- [x] **Step 2: Evaluate the unchanged entry against the packets.**

Record actual baseline behavior using fresh contexts. Distinguish manual instruction-following from native skill activation. A baseline pass is a pass, not a fabricated RED. Test fixtures represent ownership facts; they cannot prove a real client exposes that metadata.

- [x] **Step 3: Add the explicit discovery/ownership contract to entry instructions and reference.**

Use the harness's discovered identifier when its metadata identifies the selected installation. Preserve canonical resource paths, existing dependency groups, language behavior, and absent-capability boundaries. Require a focused user choice for materially ambiguous duplicate ownership. Do not infer ownership from suffix matching or introduce a dependency on root manifests/catalog at runtime.

- [x] **Step 4: Verify the four packets with the resulting instructions.**

Use fresh contexts for direct and routed usage, record invoked identifiers and effects. Re-run the existing entry scenarios affected by the instruction change. Run the repository/distribution validators and full suite. Native ownership/discovery evidence remains Task 4's separate responsibility.

- [x] **Step 5: Commit only Task 3's instructions, scenarios, evidence and composition documentation.**

Suggested message: `feat: resolver rutas del toolkit según la instalación seleccionada`. Check that no public skill name or catalog status changed.

### Task 4: Native matrix and lifecycle evidence

**Files:**
- Create: `tests/integration/distribution/scenarios/native-loading.md`.
- Create: `tests/integration/distribution/evaluations/<run>/native.md`.
- Modify: the four `docs/installation/*.md` guides, `docs/compatibility.md`, `docs/architecture.md`, `docs/roadmap.md`, `CHANGELOG.md`.

**Interfaces:**
- Consumes: Task 1's package, Task 2's procedures and environment records, and Task 3's ownership-aware entry.
- Produces: a matrix of `target / delivery / scope` with separately reported structural, filesystem and native evidence. States are `passed`, `failed`, `blocked`, `not_run`, `limited`, or `not_supported`.

- [x] **Step 1: Write native packets and the initial unrun matrix.**

`NATIVE-01` checks direct skill discovery, reference/template reads, request language and no unrelated side effects.

`NATIVE-02` installs the suite, enumerates its seven actual skills and invokes the entry to route to an owned optional skill.

`NATIVE-03` checks user/project scope against the selected project and a control project, including a globally installed but project-disabled plugin where supported.

`NATIVE-04` updates and removes only the selected plugin/skill installation; unrelated skills, settings and the other scope remain unchanged. Observe reload/restart requirements and repeated installation behavior.

`NATIVE-05` represents unavailable client/authentication/isolation and the Kiro project Power exception. Expect the exact limitation state and a separately verified project skill-set fallback; no fabricated native success.

Create all sixteen target/delivery/scope rows. Initialize documented-but-unrun routes as `not_run`, the Kiro native project Power row as `not_supported`, and add a separate Kiro project skill-set fallback row. Namespaced identifiers come from actual discovery rather than hardcoded cross-client assumptions.

- [x] **Step 2: Inspect actual clients and authorize only the disposable installation effects.**

Record exact application, extension, OS and external CLI versions and verify the relevant current official instructions. Use verified client profile controls or a disposable user/container. If interactive auth cannot be completed without exposing private credentials or altering the real profile, record `blocked` and continue independent structural work.

Do not disable trust, approval, or security settings, copy personal authentication stores, or manipulate internal plugin caches.

- [ ] **Step 3: Execute the real client checks row by row.**

For Codex register its marketplace, install via a supported client and exercise trusted project enablement separately. For Copilot test the Copilot harness in VS Code rather than a different harness hosted by the same editor. For Claude register its marketplace and explicitly select user/project scope. For Kiro import the root plugin as a Power and test global skills and workspace skills in the IDE.

For each supported row invoke a skill that reads a bundled reference/template, then test entry routing where that delivery includes the entry dependency trio. Compare the control project before and after. Run lifecycle checks only in the selected disposable scope. Retain non-private observed evidence; do not relabel manual following or the CLI's file copy as native activation.

- [x] **Step 4: Reconcile claims and document only observed support.**

Update target guides and compatibility with per-row status, versions, source ref and evidence. Explain the project activation/cache distinction and Kiro exception. Document blocked rows and exact next evidence needed. Keep the work explicitly partially validated if required native rows did not pass; their execution steps stay incomplete or blocked rather than checked off as successes.

Update architecture/roadmap to distinguish shipped metadata from verified harness support, and add an `unreleased` changelog entry for actual delivered outcomes. No tag, release, compatibility badge, or marketplace-directory submission is authorized by this plan.

- [x] **Step 5: Run final checks and commit the evidence/documentation.**

Run `python -B -m unittest discover -s tests -p "test_*.py" -v`, `python -B scripts/validate_repository.py --root .`, `python -B -m scripts.validate_distribution --root .`, and `git diff --check`. Verify skill-only tests remain under their owner and cross-skill installation evidence under the integration subtree. Explicitly report environmental skips.

Inspect the staged paths and commit only Task 4's scenarios, records and updated docs. Suggested message: `test: registrar instalación y límites de compatibilidad del toolkit`.

### Task 5: Remote-first documentation

**Files:** Modify README.md, docs/installation.md, docs/installation/{codex,copilot-vscode,claude-code,kiro}.md. Create docs/installation/{individual-skills,development,preview}.md.

**Interfaces:** Consume the unchanged seven-skill package and remote source policy in the revised spec. Produce native remote quickstarts, one optional individual/dependency guide and a separate local/developer guide. No runtime API changes.

- [x] **Step 1: Record the current onboarding gap.** Inspect the current README/overview: their first examples require a local checkout and source-path variable. Record this prose baseline without a synthetic text-presence test.
- [x] **Step 2: Rewrite the consumer entry points.** Lead with the complete remote suite, four native target routes, a short default-branch availability note and a link to the client-specific preview route. Put all Node/Skills CLI, explicit selections and manual/local procedures in their owning guides. Preserve scope/lifecycle/collision rules and resource completeness.
- [x] **Step 3: Check and commit.** Run both validators, check all local Markdown links and git diff --check. Expected: exit 0; the selection table remains complete and all seven names remain unchanged. Commit only this documentation task.

### Task 6: Real remote installation evidence

**Files:** Create tests/integration/distribution/scenarios/remote-installation.md and tests/integration/distribution/evaluations/2026-10-23-remote-suite/{remote.md,results.json,runner.mjs,toolchain-lock.json}.

**Interfaces:** Consume Task 5's exact pinned source and native CLI procedures (Claude uses the existing preview branch and verifies its resolved HEAD). Produce separate remote registration/filesystem observations; do not replace the existing local matrix or claim authenticated activation.

- [x] **Step 1: Define packets before execution.** REMOTE-FS-01: Git fetch pinned source in an owned container and verify manifests/seven canonical folders. REMOTE-NATIVE-01/02: Codex/Claude branch-based remote marketplace registration and complete suite installation, list/inventory and resource-byte checks. REMOTE-ALT-01: remote independent skill and complete-seven fallback via Skills CLI 1.7.4 with explicit target/scope. REMOTE-LIMIT-01: record pre-integration default branch, missing IDE/auth and unsupported Kiro ref interface honestly.
- [x] **Step 2: Obtain isolated tools.** Use an actual disposable Linux user/container, public Git without credentials, Codex 0.162.0, Claude 2.1.300 and Skills CLI 1.7.4. Record versions/locks. Do not mount personal homes or authentication, loosen trust/approval protections, or run a remote model.
- [x] **Step 3: Execute the exact remote commands.** Verify requested ref, installed metadata, seven available names and complete resources against that remote source. Optional copies use explicit dependencies. Preserve failures/blocks and observed inventories; remote registration is only limited native evidence.
- [x] **Step 4: Retain and commit sanitized evidence.** Read every result, retain source/commands/exit codes/hashes and summarize limitations. Expected: remote supported operations pass or have an exact recorded blocker; no result claims full native activation.

### Task 7: Reconcile, verify and update the existing PR

**Files:** Modify docs/compatibility.md, docs/architecture.md, docs/roadmap.md, CHANGELOG.md and this plan's execution status. Update PR #4's description with the repository template.

**Interfaces:** Consume Task 5 procedures and Task 6 observations. Produce consistent consumer/maintainer documentation and truthful remote evidence on the existing branch.

- [x] **Step 1: Reconcile claims.** Link the remote evaluation; retain local evidence and Task 4 Step 3 as incomplete. Distinguish post-integration default source, fixed and branch-tracking preview sources, and unpublished candidate metadata.
- [x] **Step 2: Run final checks.** Run python -B -m unittest discover -s tests -p "test_*.py" -v; both validators; local link checks; git diff --check. Expected: all applicable tests pass with environmental skips explicit.
- [x] **Step 3: Review and update.** Perform the required one fresh-context branch review, address material findings with relevant verification, commit explicit files, push the existing branch and update PR #4. Preserve the worktree and publish no release or merge.

### Task 8: Seven-client complete-suite guides

**Files:** Modify README.md, docs/installation.md, docs/installation/{copilot-vscode,kiro,individual-skills,development,preview}.md. Create docs/installation/{copilot-cli,kiro-cli,kiro-crew}.md and tests/integration/distribution/scenarios/client-expansion.md; initialize tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md.

**Interfaces:** Consume CLIENT-01 through CLIENT-06 and the unchanged seven-skill package. Produce concrete complete-suite, user/project, preview, discovery and lifecycle routes for seven clients. Crew imports a complete skill set into its own source store; no agent template or App is produced.

- [x] **Step 1: Record the baseline and source interfaces.** Observe the four-guide overview, IDE-only Kiro statement and VS Code settings wording. Inspect official source and installed client version/help; distinguish documentation from native verification. Expected: exact gaps recorded, no synthetic text-presence test.
- [x] **Step 2: Write client scenarios before revising guides.** CLIENT-COPILOT covers remote marketplace registration/install, seven-resource inventory, user/repository activation and VS Code crossover separately. CLIENT-KIRO covers V3 shared IDE Power, local/catalog help and CLI-only seven-folder fallback. CLIENT-CREW covers remote full import, source-specific resource paths, default versus restricted existing agents, explicit dependency closures, snapshot re-import and trusted project/control isolation. Missing clients/auth remain blocked.
- [x] **Step 3: Revise the guides and overview.** Add seven named links, CLI recipes and lifecycle, Crew dashboard full import and no-template decision. Preserve old kiro.md links, explicit ref availability, shared-root caveats and individual alternatives. Do not change skills, catalog or metadata.
- [x] **Step 4: Verify and commit.** Run both Python validators, a local Markdown file/anchor link check and git diff --check. Expected: exit 0, no broken links, same seven canonical resources. Commit explicit documentation/scenario paths.

### Task 9: Client-specific probes and evidence

**Files:** Modify tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md; create sibling {results.json,attempt-1.json,runner.mjs,run.sh,toolchain-lock.json,matrix.md} as actual available probes warrant; modify docs/compatibility.md, docs/architecture.md, docs/roadmap.md, CHANGELOG.md, docs/installation/preview.md, the linked spec source policy and this plan.

**Interfaces:** Consume Task 8's recipes and public immutable reference b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e. Produce distinct historical/expanded client matrices and sanitized observations. No existing native gate is closed by a file-only check.

- [x] **Step 1: Probe remote Copilot in an owned container.** Pin its package after inspecting the installed 1.0.91 help/version and acquire tools only in the disposable container. Fetch the public reference, register/install/list through actual CLI, compare all seven skill resources, then exercise selected native lifecycle operations with unrelated sentinels. Preserve failed attempts or blockers. Do not use host credentials or run a model. Expected: observed supported commands exit 0 or retain an exact blocker.
- [x] **Step 2: Record each client separately.** Retain client versions, source refs, commands and scope limitations. Kiro CLI 2.28.0 help is interface evidence only; no IDE/CLI activation or Crew installation is fabricated. Add selected/control scenarios and truthful per-delivery status rows. Expected: documentation-only supported routes remain not_run/blocked rather than passed.
- [x] **Step 3: Reconcile and verify.** Update compatibility, architecture, roadmap and unreleased changelog. Run python -B -m unittest discover -s tests -p "test_*.py" -v; both validators, links and git diff --check. Expected: all applicable tests pass with environmental skips explicit; skills/catalog/manifests unchanged from Task 8 base. Commit explicit evidence/docs.

### Task 10: Review and update the existing PR

**Files:** This plan's execution status, retained final review under the client-expansion evidence directory, PR #4 title/body.

**Interfaces:** Consume Tasks 8-9 and the unchanged package. Produce the same open PR updated with seven-client scope and precise validation limits.

- [ ] **Step 1: Review the whole branch in one fresh context.** Supply the spec, plan, Review Focus, ledger rulings and review package. Grade findings by user effect; address material findings with relevant RED/GREEN checks and the suite, preserve declined judgments as rulings. Expected: no unresolved blocking findings.
- [ ] **Step 2: Finalize and publish the PR revision.** Mark only the implemented expansion steps complete; keep Task 4 Step 3 open. Verify validators, links and git diff --check after any administrative edits. Commit, push this branch and update PR #4 using its template. Verify remote HEAD/title/body and clean worktree. Preserve worktree; no merge, release or template creation.

## Acceptance traceability and self-review

| Spec criterion | Owning task |
| --- | --- |
| DIST-01 metadata, sources, seven available names | 1 |
| DIST-02 individual closures, destinations, resource preservation | 2 |
| DIST-03 namespaced ownership, absent and duplicate behavior | 3 |
| DIST-04 actual native scope and Kiro exception | 4 |
| DIST-05 scoped lifecycle, collision preservation, repeat installation | 2, 4 |
| DIST-06 concrete procedures and limitations | 2, 4 |
| DIST-07 unchanged catalog/skills apart from explicit entry clarification | 1, 3 |
| DIST-08 truthful evidence and no implicit publication | 4 |

Self-review: all declared production signatures have an owning task; later tasks consume those interfaces without renaming them. Each Review Focus item has explicit assertions in its owning task. Real installation and native activation remain separate from unit tests; missing environments cannot manufacture compatibility. The plan contains no duplicated skill implementation or custom installer body.

Client-expansion coverage: CLIENT-01 through CLIENT-04 belong to Task 8; CLIENT-05 belongs to Tasks 8-10; CLIENT-06 applies to all three. Spec and plan self-review found no new runtime interface or duplicated skill implementation.

Remote-first coverage: REMOTE-01/02/05 belong to Task 5; REMOTE-03/04 belong to Tasks 6-7. Existing Tasks 1-4 remain historical implementation/evidence and must not be re-executed merely because onboarding changes.

## Execution status

Seven-client expansion: Tasks 8-10 implement CLIENT-01 through CLIENT-06 in order. User approved Proposal A and implementation together; the no-template Crew route uses native complete skill import, without claiming Power inheritance. Earlier completed tasks are historical and are not repeated.


Tasks 1-3 are implemented and verified. Tasks 5-7 delivered the approved remote-first guides, real remote acquisition/resource evidence, reconciled documentation and the updated existing PR. The remote-first revision's independent review found no blocking or minor findings; its record remains historical. Task 4 delivers scenarios, limited native observations and compatibility documentation. Its Step 3 remains incomplete/blocked for authenticated invocation, full scope/lifecycle checks and IDE sessions; see the [native matrix](../../../tests/integration/distribution/evaluations/2026-10-23-installation/native.md). This is partial validation, not a successful four-client compatibility claim.

Remote-first checks do not complete Task 4 Step 3. The default-branch source becomes usable after integration; no merge or release is performed by this revision.

## Handoff

The candidate is prepared for review with the recorded native gates still open. No publication or merge is part of this implementation.
