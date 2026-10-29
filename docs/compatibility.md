# Compatibility and validation evidence

## Intended portability

The available skills use Markdown instructions, YAML frontmatter, relative resources, and Git commands. Their instructions prefer explicit command working directories or `git -C` and do not depend on a persistent shell. This design intent is not a compatibility claim for any untested harness.

## Observed in this implementation task

- Harness: Codex desktop, 2026-10-22. Fresh agent contexts evaluated behavior without the candidate skill, followed by fresh contexts manually following repository instructions for GREEN. A separate context assessed baseline results. This environment did not expose native activation of repository-local skills, so the results do not verify native skill discovery or loading.
- Conventional Commit standalone behavior: eight named cases covered ambiguity and correction, project-specific type/scope/body, breaking markers, shell-looking text, language changes without a repository, missing intent, and ticket placement. All final GREEN assertions passed under manual following; no Git or ticket tools were used.
- todo-workflow-controller behavior: five baseline and five manual GREEN cases covered required gates, unavailable tracking tools, unresolved decisions, independent and parallel work, handoffs, and language changes. Final baseline assertions passed, so the skill is not claimed to fix an observed baseline failure. GREEN contexts manually followed the candidate text; no native loader, actual tracker failure, other harness, or persistent side effect was exercised.
- Natural-language reporting: five baseline and five GREEN cases covered consolidation and numeric fidelity, empty/conflicting evidence, language overrides, custom technical structure, and content-only versus requested local-file output. The baseline failed the explicit Spanish override in RPT-03; all final GREEN assertions passed in fresh contexts manually following the actual candidate files. RPT-05 confirmed no file on the first request and one selected report file with matching readback on the second. Native skill loading was unavailable; the output test used an isolated ignored worktree folder because OS-temporary paths were not shared between evaluation contexts.
- Toolkit composition behavior: direct use, optional routing, and absent-installation cases were evaluated for both Conventional Commit formatting and portable progress control. The progress baseline did not reliably select the optional capability and could imitate progress behavior when it was absent. The entry now names and routes to `todo-workflow-controller` when installed, reports it unavailable when absent, and does not interpret a workflow step named `publish` as a Git request. All three manual GREEN cases passed.
- Natural-language report composition: direct use, optional route with the skill installed, and absent-skill behavior all passed in fresh contexts manually following the exact current resources. The installed case produced the requested Spanish report without a Git preflight; the absent case reported the missing capability without drafting or installing it. The entry and reference were unchanged because their existing in-scope-alternative and absent-capability rules covered both states. Native skill loading was unavailable.
- Project validation discovery: five named cases covered source-based discovery without execution, empty non-Git projects, lifecycle-hook effects, explicitly requested local checks and composites, independent required-check outcomes, unavailable execution, and unexpected files. Baseline VAL-04 omitted an explicit `not_run`/`blocked` state for unavailable execution. All GREEN assertions passed after adding that result state and requiring same-invocation capture when a shell wrapper can mask a process exit code. Fresh Codex agent contexts manually followed the exact candidate skill and local reference; the repository-local skill was not natively loaded. The no-tool variant was answered from its stated facts without invoking a command, but the harness could not physically remove its command tool. No other harness was tested.
- Python: 3.14.3; PyYAML: 6.0.3; Git for Windows: 2.45.0.windows.1.
- The automated suite discovered 57 tests and passed with one environmental skip. The Windows symlink escape fixture was skipped because the OS denied the required symlink privilege. The validator includes containment checks, but that symlink case was not dynamically exercised here.
- Read-only context/preflight queries preserved refs, HEAD, index bytes, Git metadata outside the object database, and working-file contents and modes in the fixture suites.

- Project validation composition: direct use, optional entry routing and absent-installation cases were evaluated. Baseline entry evaluation found no explicit route and one absent-skill response falsely described a route as existing; the entry now routes to the standalone capability only when installed and reports it unavailable when absent. Fresh contexts manually followed the entry and standalone instructions; native skill activation was unavailable.

## Distribution candidate: 2026-10-23

The 0.1.0-preview.2 distribution adds native package metadata and explicit selected-skill recipes; preview.1 remains source-only. [Filesystem evidence](../tests/integration/distribution/evaluations/2026-10-23-installation/filesystem.md) records 64 pinned-CLI cases, 64 independent manual-copy cases, eight CLI lifecycle cases and their actual before/after inventories. No personal skill store was used.

[Ownership evaluation](../tests/skills/using_devcraft_toolkit/evaluations/2026-10-23-installation-routing/installation-routing.md) found two initial routing failures, corrected them through explicit selected-installation rules, and passed four final fresh-context packets plus twelve existing-behavior observations. Discovery fixtures and manual instruction following do not prove native metadata or invocation.

[Native evidence](../tests/integration/distribution/evaluations/2026-10-23-installation/native.md) separates registration, file placement, discovery, invocation, scope and lifecycle. Codex CLI 0.162.0 registered, installed/listed and removed the local package; a separate RED-to-GREEN registry probe confirmed user-disabled/project-enabled precedence against a control project. This is configuration evidence, not active-session isolation. Claude Code 2.1.300 accepted metadata, registered and installed the suite in user/project scopes, and reported the project installation disabled in the control project. Local-directory update semantics differed from a Git marketplace. Authenticated skill invocation/resource reads and complete native lifecycle remain pending; Copilot and Kiro IDE sessions were not available in an isolated authenticated environment. The matrix is explicitly partial, not all-four-harness compatibility.

Preview.2 automated checks: 78 tests discovered, 77 passed and one Windows symlink privilege skip. Both repository and distribution validators pass. Structural tests do not establish client activation or model instruction following.

## Remote-first suite validation

The consumer path now starts with the complete native suite from the public repository. [Individual skills](installation/individual-skills.md) are an alternative; [local/developer installation](installation/development.md) is separate. Default-source recipes use integrated metadata; [release-pinned sources](releases/v0.1.0-preview.7.md#version-pinned-sources) are separate from [historical pre-integration sources](installation/preview.md).

The [remote evaluation](../tests/integration/distribution/evaluations/2026-10-23-remote-suite/remote.md) fetched public reference b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e, installed the suite through Codex and Claude's actual remote marketplace flows, and compared every installed skill resource against that source. It also copied an independent formatter for Codex and the complete project fallback for Kiro through the pinned external CLI. The corrected run's 29 commands exited 0; its native outcomes remain limited.

Claude 2.1.300 rejected a commit SHA in the marketplace clone URL. The working preview uses a mutable existing branch whose resolved HEAD was recorded and verified. Codex accepted the immutable SHA. The failed attempt is retained. This is a version-specific observed difference, not a claim that all clients accept the same ref syntax.

No authenticated native invocation, model-driven resource read, full version-changing lifecycle, Copilot session or Kiro IDE session passed. Existing native gates remain open; remote acquisition/resource hashes do not close them.

## Seven local clients

The approved extension documents Codex, Copilot CLI, Copilot in VS Code,
Claude Code, Kiro CLI V3, Kiro IDE and Kiro Crew independently. The same seven
canonical skills and existing manifests are reused; there is no new Crew
template, App, crewmate or runtime installer.

[Expanded client evidence](../tests/integration/distribution/evaluations/2026-10-23-client-expansion/clients.md)
records the Copilot CLI 1.0.91 remote probe: 20 successful corrected commands,
all seven installed resource sets matching the immutable payload, repeated
install, user enable/disable, same-ref refresh/update and selected removal with
sentinels preserved. The original rejected SHA is retained; the working preview
uses a verified mutable branch. This is limited registration/filesystem evidence,
not authenticated invocation or repository auto-install/active-session scope.

Kiro CLI 2.28.0 version/help was inspected without installing into its real user.
The V3 shared IDE-Power route and catalog/local management are documented; the
CLI-only full remote set is a separate delivery. Crew uses its own native GitHub
skill snapshot importer and trusted-project route; it does not inherit a proven
Power installation. The existing default agent needs no toolkit template, while
restricted agent mappings remain user-controlled.

The [expanded matrix](../tests/integration/distribution/evaluations/2026-10-23-client-expansion/matrix.md)
keeps 28 native client/delivery/scope rows and three distinct Kiro full-set
fallback rows. Copilot VS Code crossover, Kiro CLI/IDE activation, Crew imports,
resource reads, trust, scope and lifecycle remain blocked/unrun. Historical
four-client observations are retained; Task 4 Step 3 remains open.

## Kiro keywords correction F001

Root plugin.json now includes activation keywords to follow Kiro's authoring
guidance, although the portable schema makes them optional. The local contract
requires a non-empty string array and keeps the minimal Claude metadata
unchanged. [F001 evidence](../tests/integration/distribution/evaluations/2026-10-23-kiro-keywords/keywords.md)
records the validator regression and correction.

Earlier b05a8c4/218aea8 acquisition/resource observations describe the previous
manifest. They remain historical and must not be presented as acceptance of the
corrected root metadata. Canonical skills/resources, common identity/version
and marketplace sources are unchanged. No isolated Kiro IDE/CLI activation was
performed for this correction; Task 4 Step 3 remains open.

## Limits

The skill behavior evaluations are manual instruction-following assessments in fresh agent contexts, not native skill-loader tests. The earlier Python dependency-installation attempt was blocked by PyPI DNS/network access; the later isolated Skills CLI filesystem evaluation above is a separate, observed operation. The submodule scenario, isolated missing-Git executable, authenticated native skill loading, other harness sessions, and mid-run progress-tracker failure were not dynamically exercised. Native registration observations above do not establish full compatibility with any target harness; blocked activation rows remain open. Structural tests prove repository checks and fixture state, not language quality or instruction following.

## Read-only preparation preview.3: 2026-10-24

The `0.1.0-preview.3` release adds `git-analyze-changes` and `git-plan-commits`, bringing the inventory to nine available/eight planned. [Analyzer evidence](../tests/skills/git_analyze_changes/evaluations/2026-10-24.md), [planner evidence](../tests/skills/git_plan_commits/evaluations/2026-10-24.md) and [entry composition](../tests/skills/using_devcraft_toolkit/evaluations/git-preparation-composition.md) distinguish supplied-fact instruction following from real disposable Git command controls.

Five fresh no-guidance samples and five complete-instruction samples per new capability were manually assessed; baseline judgment successes are retained. New command fixtures cover partial staging, freshness, exact paths and helper/filter boundaries. Neither these replays nor structural checks establish native activation or authenticated resource reads. Existing seven-skill preview.2 registration/resource/lifecycle results above remain historical; do not apply them to the release's two added skills.

Preview.3 preparation verification: 89 tests discovered, 88 passed, one existing Windows symlink privilege skip; repository and finite distribution validators pass. Git for Windows 2.45.0.windows.1 was used for the added fixture controls. This does not close native invocation gates.

## Scoped staging and commit construction preview.4: 2026-10-24

The `0.1.0-preview.4` release adds `git-stage-changes` and `git-commit-builder`, bringing the inventory to eleven available/six planned. [Staging evidence](../tests/skills/git_stage_changes/evaluations/2026-10-24.md) and [coordinator evidence](../tests/skills/git_commit_builder/evaluations/2026-10-24.md) retain baseline/candidate records, precision failures and corrections, edge/gap cases and independent parent verification.

One owned live fixture performed exact partial staging; another created one requested commit while preserving excluded working content. Both manually loaded the local source skills and dependency closure; neither establishes native discovery. Disposable Git controls additionally cover literal transport, stale patches, initial commits, effective identity overrides, hooks and partial multi-commit failure. Native client invocation/lifecycle gates remain open.

Implementation verification: 100 tests discovered, 99 passed and one existing Windows symlink privilege skip; both validators and complete-base whitespace checks pass. The first full run retained two stale planned-status fixture assumptions; explicit fixture setup corrected them without changing validator rejection assertions.

The independent branch review found an index-write hook gate omission. The fix now inspects post-index-change before staging/deferral/restore or commit preparation; a pinned pre-fix live actor reproduced an excluded-file rewrite, while the corrected actor blocked before mutation with unchanged guards. Default/custom hook recipe controls and nine-folder-only closure evidence retain their exact procedure limitations in the owner evaluations.

## Local-history reporting preview.5: 2026-10-25

The preview.5 release adds `git-activity-report`, bringing current-source inventory to twelve available/five planned. [Owner evidence](../tests/skills/git_activity_report/evaluations/2026-10-24.md) separates five baseline/candidate supplied-fact samples, Git recipe controls and an actual three-folder application. Two initial calibration samples saw evaluator assertions and were excluded/replaced; one baseline saw field names only and disclosed it. Source attribution and numeric-fidelity failures are retained rather than claiming every baseline failed.

A fresh actor manually loaded only copied coordinator/context/writer resources, inspected four real commits, selected the expected author-date OID despite its next-day committer timestamp, and saved/read back one explicitly requested report. Parent checks confirmed the exact OID, unchanged repository snapshot and no extra container files. Initial shell-profile attempts and a sandbox-denied write are disclosed with the corrected profile-free/retry procedure; these checks do not establish absence of every possible external profile effect.

[Entry composition](../tests/skills/using_devcraft_toolkit/evaluations/git-activity-report-composition.md) covers installed, absent, foreign, ambiguous, direct standalone and supplied-fact routes. Recipe controls exercise non-monotonic dates, half-open boundaries, raw emails, merges/duplicates/reverts, budget/shallow/missing/grafted history, ignored replacement refs, detached/unborn states, profile/helper limits and 23/25-hour DST intervals. They test Git recipes and fixture state, not native discovery or universal instruction adherence. Full branch verification is recorded in the [integration evaluation](../tests/integration/evaluations/2026-10-24-git-activity-report/final.md).

No authenticated native invocation or cross-client lifecycle gate is closed by these manual evaluations. Preview.4 remains its original eleven-skill snapshot. The [preview.5 release](releases/v0.1.0-preview.5.md) preserves these validation boundaries; publication does not establish native compatibility.

## Scoped synchronization/publication preview.6: 2026-10-25

The preview.6 release adds two independent context/safety closures, bringing the distribution to fourteen available/three planned. [Sync evidence](../tests/skills/git_sync_branch/evaluations/2026-10-25.md) and [publication evidence](../tests/skills/git_publish_changes/evaluations/2026-10-25.md) retain five no-guidance and five candidate supplied-fact samples each, raw outcomes, gaps and owner Git recipe controls. Baseline successes and fixture corrections remain visible.

Actual actors manually used copied three-folder resources against owned local bare repositories. Parent verification checked exact fast-forward tree/index and protected references/config, then a separate exact branch push with only requested upstream keys and preserved local state. These are local Git applications, not authenticated SSH/HTTPS, native loader activation, hosting APIs or IDE sessions. The discarded acknowledgment recipe demonstrates missing observation after an actual push, not a fault-injected broken transport. Raw pinned-source controls do not authorize proceeding after detected source movement.

Entry routing uses supplied discovery/ownership facts, not native metadata. Historical preview.5 remains twelve skills, and prior native evidence does not establish activation of these additions. See the [final verification record](../tests/integration/evaluations/2026-10-25-git-sync-publish/verification.md) for exact automated results and retained limits.

Final candidate verification discovered 138 tests: 137 passed and one existing Windows symlink privilege skip. Both validators and new-skill quick validations passed. One independent review found two Important preservation defects; ignored-file and symbolic tracking regressions failed before the single fix pass and passed afterward with the full suite. No minor findings remain deferred. Actual copied-resource applications preceded these last guards; the added real Git controls and supplied-fact behavior test them without claiming repeated native or authenticated application.

The subsequent [upstream review follow-up](../tests/skills/git_publish_changes/evaluations/upstream-mapping-review.md) requires a usable existing fetch mapping/tracking ref before setup and actual upstream resolution after two-key writes. A fresh run with declared PyYAML available passed 139 of 140 tests, with the existing Windows skip; the reviewer's separate environment failures remain separately reported. No authenticated/native claim is added.

## Preview.6 release preparation

The [release page](releases/v0.1.0-preview.6.md) and [pre-merge preparation](../tests/integration/distribution/evaluations/2026-10-25-preview6-release/preparation.md) retain same-merge source preparation and exact-revision archive validation. The approving PR re-review resolved the upstream defect and passed its repeat suite with declared local environment limits. Publishing does not close native or authenticated activation gates, and historical client probes remain revision-specific.

## Hosted request/promotion preview.7

Preview.7 adds two instruction-first closures, bringing current source to sixteen available/one planned. [Management evaluation](../tests/skills/git_manage_pull_request/evaluations/2026-10-25.md) and [promotion evaluation](../tests/skills/git_promote/evaluations/2026-10-25.md) retain five fresh baselines and five candidates per owner, separate assertion/input resources, gap decisions and exact application receipts. Baseline successes are preserved. Management application attempt 1 exposed persisted Unicode corruption despite a visually correct console receipt; a forced-locale RED/GREEN transport regression and independently checked fresh application retain that limitation and fix.

The management actor manually loaded two copied folders and performed one emulated creation/body update. The promotion actor loaded three and made one source-conditional normal merge through owned transport; parent checks compared operation ledgers, real prepared Git parents/ancestry and unchanged dirty local Git snapshots. The provider state points at a merge object prepared before the application: this is not an actual hosted merge. Protocol controls preserve unknown state, pagination/fork identities, interpreted GitLab text, source rejection, pending/lost receipts and descendant/rewritten target evidence. They do not prove installed client policy enforcement.

No authenticated GitHub/GitLab operation, native activation or seven-client lifecycle claim is added. Preview.6 remains fourteen skills; preview.7 and the integrated default source contain sixteen. [Final verification](../tests/integration/evaluations/2026-10-25-git-pr-promotion/verification.md) records the final branch checks and review. Full publication coordination and native/authenticated provider validation remain separate next tracks.

## Preview.7 release preparation

The [release page](releases/v0.1.0-preview.7.md) and [same-PR preparation](../tests/integration/distribution/evaluations/2026-10-26-preview7-release/preparation.md) keep changelog and publication sources in PR #9 before merge. The approving review and fresh preparation checks preserve environment/fixture limits. Assets/tag target the exact merge; older release metadata and native evidence remain unchanged. Publication adds no native or authenticated skill-execution claim.

## Work publication candidate: 2026-10-26

Current unpublished preview.8 resources contain eighteen available skills. The new branch capability uses a two-folder context closure; coordination uses five mandatory folders plus selected conditional owners (fifteen-folder complete optional union). Source selection, installation and permission remain separate; default remote/preview.7 sources lack the additions until integration.

Five fresh no-guidance and five exact-resource supplied-fact actors per new skill are retained under each owner. Actual copied applications used two branch folders and thirteen selected publication folders, owned real Git repositories and emulated hosting connected to the actual published SHA. Parent inspections verified refs, semantic index/files/configuration and publication command/provider ledgers. These are manually followed instruction applications, not native invocation, authenticated SSH/HTTPS or real GitHub/GitLab operations. Native and authenticated coverage stays open. See the [final verification record](../tests/integration/evaluations/2026-10-26-git-work-publication/verification.md) for executed gates and evidence limits.

## Preview.8 release preparation

Versioned changelog, release notes, consumer pointers and fresh verification are prepared in PR #10 before merge. The release/tag/assets use that exact merged tree. Eighteen skills are available with unchanged reviewed instruction resources and dependency closures. [Release details](releases/v0.1.0-preview.8.md) and [preparation evidence](../tests/integration/distribution/evaluations/2026-10-29-preview8-release/preparation.md) preserve the distinction between packaging and native/authenticated compatibility. Historical probe rows retain their original scope.
