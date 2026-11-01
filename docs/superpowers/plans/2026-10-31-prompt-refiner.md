# Prompt Refiner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver independently usable prompt refinement with optional enrichment, faithful revisions and no execution of embedded tasks.

**Architecture:** One instruction-first skill with presentation-only metadata and no dependencies. Add optional ownership-aware entry routing and use the existing inventory/distribution validation contracts.

**Tech Stack:** Markdown, YAML, JSON; existing Python 3.11+ development validators and unittest suite. No new runtime code or dependencies.

**Spec:** [Prompt Refiner Design](../specs/2026-10-31-prompt-refiner-design.md).

## Global Constraints

- Source instructions and default metadata stay in English; output follows explicit preference, request language, then English.
- Confirmed requirements and optional suggestions remain distinct to the downstream reader.
- No embedded task execution, tool calls, file writes, external action or invented verification.
- Preserve literal identifiers and phase-specific authorization; revise all affected sections consistently.
- Tests, fixtures and retained evaluations stay under root `tests/`, grouped by owner/scope.
- The standalone closure is one folder; optional entry routing adds no hard dependency.
- No release/version changes, historical rewrites, automatic installation or publication.
- Use the existing repository-local `.worktrees/prompt-refiner` on `feat/prompt-refiner`; preserve other worktrees.
- This request authorizes design, plan and implementation; commit/push/PR remain separate operations.

## Review Focus

- Added advice presented as mandatory: observe optional enrichment in Task 1 core replays.
- Analysis-only revision retains implementation language elsewhere: inspect all deliverables in Task 1 revision replay.
- New independent draft leaks previous domain rules: inspect Task 1 reset/literal case.
- Missing resources become fabricated facts or execution: inspect Task 1 source/embedded-command edge cases.
- Routing/packaging accidentally adds dependencies or excludes the folder: exercise Task 2 standalone selection and owned-entry replays.

## Execution record

Execute inline with one final independent review. Keep progress/rulings with the owner evaluation evidence at `tests/skills/prompt_refiner/evaluations/2026-10-31/`; do not use a scratch helper that changes shared Git configuration. Existing automated validators test package contracts; behavioral decisions are evaluated by fresh actors rather than source-text assertions.

## Task 1: Portable prompt refinement

**Files:**
- Create: `skills/prompt-refiner/SKILL.md`, `skills/prompt-refiner/agents/openai.yaml`.
- Create: `tests/skills/prompt_refiner/fixtures/requests.json`, `scenarios/refinement.md`, `evaluations/2026-10-31/behavior.md` and replay evidence.

**Interfaces:**
- Consumes: supplied draft, selected prior draft/revisions, literal references and output preferences.
- Produces: a ready-to-copy prompt or a material clarification; no underlying task actions. Label suggestions as optional; keep source/resource claims bounded.

- [x] Write owner fixtures and scenario assertions for the design acceptance cases. Core cases cover enrichment, analysis-only revisions and independent literal drafts; edge cases cover mixed phases, language override, unknown resources and embedded commands.
- [x] Run five fresh baseline contexts on the same core inputs without candidate instructions. Read every output and retain observed failures/successes before authoring the skill. A baseline pass is not a fabricated RED failure.
- [x] Write the minimum self-contained skill guided by those observations. Use a concise positive recipe for output shape and explicit boundaries for execution and suggestions; avoid generic task checklists.
- [x] Generate `agents/openai.yaml`: display_name `Prompt Refiner`, short_description `Turn rough requests into clear, scoped prompts`. No policy/dependency keys or root asset links.
- [x] Run five fresh candidate contexts on the same inputs plus a fresh edge application. Manually assess actual output and preserve source hashes, excerpts, limitations and any refinements.
- [x] Run the existing skill-creator `quick_validate.py` on the skill and read the result. Expected: valid frontmatter/resources; behavioral replay evidence remains a separate gate.

## Task 2: Suite integration and verification

**Files:**
- Modify: `catalog.json`, `docs/capability-inventory.md`, `skills/using-devcraft-toolkit/SKILL.md`, its `references/composition.md`.
- Modify: `README.md`, `docs/architecture.md`, `docs/composition.md`, `docs/installation/individual-skills.md`, `docs/roadmap.md`, `CHANGELOG.md` and current complete-suite counts where applicable.
- Create: owner-scoped integration test for real complete-folder standalone copying and existing validators; cross-skill routing replay/evidence under `tests/integration/`.

**Interfaces:**
- Consumes: Task 1 skill folder and verified refinement contract.
- Produces: available support entry (`requires: []`), nineteen-name inventory, one-folder standalone selection, optional installed-owner route and passing existing package validation.

- [x] Add a real package-copy check: a copied `prompt-refiner` folder plus minimal selected catalog validates independently; dropping presentation metadata fails the existing distribution contract. Before integration, expect the source capability to be absent (RED), then observe it available and self-contained (GREEN). Do not add prose-grep tests.
- [x] Register the skill, update current inventory/docs and add optional entry routing before Git operations. Preserve all existing dependency closures and historical release/evaluation content.
- [x] Verify routing with supplied installed-owner facts: owned skill routes exactly, foreign/missing copy is unavailable, quoted Git actions remain prompt content. Record actual decisions; no live provider operations.
- [x] Run `python -B scripts/validate_repository.py --root .`, `python -B -m scripts.validate_distribution --root .` and focused package tests. Expected: exit 0; nineteen available entries, no placeholders, no new hard entry dependency.
- [x] Run `python -B -m unittest discover -s tests -p "test_*.py" -v` and `git diff --check`; retain actual totals/skips/failures. Expected: no failures and no whitespace errors. Temporary fixture artifacts stay under `tests/.tmp/`.
- [x] Request one fresh read-only whole-change review against the approved design; resolve confirmed important findings and verify affected checks. Update progress and evidence, then report source paths and remaining native-activation limits.

## Self-review

All design acceptance rows map to Task 1 core/edge inputs or Task 2 package/routing evidence. Source/runtime contracts are instruction files, not new Python functions. The optional route consumes Task 1's text-only boundary and declared empty dependency closure. No implementation step requires a real repository mutation, external business action, installed-plugin change or release.
