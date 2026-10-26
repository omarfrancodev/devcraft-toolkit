# Current capability inventory

This is the approved current set of canonical product names. Development validation requires a nonempty unique inventory and exact catalog-name equality, without a fixed numeric ceiling. Catalog entries retain validated roles, availability, paths and mandatory dependencies. Inventory changes require an approved design; editing this document is not runtime authorization.

Installed capabilities do not read this document or the root catalog. Historical designs and released inventories remain version-specific records.

## Target capability inventory

| Capability | Role | Status |
| --- | --- | --- |
| using-devcraft-toolkit | entry | available |
| git-commit-builder | coordinator | available |
| git-publish-work | coordinator | available |
| git-activity-report | coordinator | available |
| git-analyze-changes | capability | available |
| git-plan-commits | capability | available |
| git-stage-changes | capability | available |
| git-create-work-branch | capability | available |
| git-sync-branch | capability | available |
| git-publish-changes | capability | available |
| git-manage-pull-request | capability | available |
| git-promote | capability | available |
| git-safety-check | support | available |
| git-working-directory-policy | support | available |
| conventional-commits-style | support | available |
| validation-discovery | support | available |
| natural-language-report-writer | support | available |
| todo-workflow-controller | support | available |

## Current delivery

Eighteen available capabilities, zero planned names. Work-branch creation and publication coordination are candidate `0.1.0-preview.8`, not yet published. Preview.7 retains sixteen capabilities. See the [roadmap](roadmap.md), [design](superpowers/specs/2026-10-26-git-work-publication-design.md) and [installation selections](installation/individual-skills.md) for scope and source requirements.
