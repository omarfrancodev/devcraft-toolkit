# Git Activity Report Formats and File Output Design

## Intent

Make a Git activity report usable as a local Markdown deliverable and let the user choose how to read it. A report must identify the period actually inspected. The daily format must show the entire selected period, including days with no matching commits.

## Scope and approaches

The existing coordinator owns the verified local history scope and delegates language and prose to the report writer. Keep the three-skill installation closure and keep runtime instructions self-contained. No new runtime dependency, installation mechanism, provider integration or release change is needed.

- **Selected design: coordinator owns Git report choices and its default destination.** The coordinator supplies a format and verified day buckets to the writer. It persists the default file itself under a narrow repository-local rule. The writer retains its established exact-path save contract for explicit destinations.
- **Extend the shared writer with a default location and daily history rules.** This would place Git-specific path policy and completeness decisions in a capability that also handles supplied-facts reports.
- **Require an explicit destination and format in the initial request.** This retains the current file boundary but leaves the requested default location and guided format choice unmet.

## Format selection

For each new report, ask the user to choose **General** or **Grouped by day (includes days without commits)** before composing or writing, even when the initial request names one of the formats. When a format was already requested, present it as the suggested choice. Use the request language for the question and labels, falling back to English when indeterminate. Use the harness question tool when available and an ordinary chat question otherwise. If other material inputs need clarification, ask for them in the same turn where possible.

A response to this question resumes the same request and satisfies the format gate. Carry its answer alongside the original scope and output intent. Without a choice, return `needs_decision` without a report or file. An unanswered question does not select a default format.

## Period, evidence and presentation

Require a positive-duration instant range before inspection or default naming. Keep the existing Git defaults: pinned local HEAD, today in a trustworthy user/session timezone when no period is supplied, author timestamp, exact configured author email, merge records excluded while traversing all parents, and a 1,000-commit examination budget plus one probe. Preserve existing explicit options and missing-scope behavior. Git access remains read-only and offline.

- Both layouts show the inclusive calendar period or requested instant interval, timezone, date basis and author selection. Include the repository/revision and any coverage limitation. Keep concise traceability from reported activities to verified evidence.
- **General:** consolidate activities across the whole period. Show scope, a synthesis of the activities and any relevant coverage notes. A report with no confirmed activity states the observed result.
- **Grouped by day:** render a Markdown table with exactly two columns, `Date` and `Activities`, localized for the report. Render one chronological row per local calendar date in scope, with ISO dates. Convert selected commits to the resolved timezone using the selected date basis before assigning them to rows. For an instant interval include the local dates it actually intersects, including partial days. An exclusive endpoint exactly at local midnight adds no new date. If midnight repeats and an earlier instant was on that date, keep its row. For instant intervals, omit any calendar date skipped entirely by an offset change. Preserve the existing timezone and DST rules. If no named timezone is resolved, equal explicit endpoint offsets may define a fixed reporting offset. Different endpoint offsets without an established reporting zone require clarification before daily grouping or default filename derivation.
- For a complete scan, each empty row says `No matching commits for this day.` A complete all-empty range still renders every date and retains the `no_op` history status. In a limited scan, an empty row says `No matching commits observed in the inspected history.` and the report explains the limitation. A blocked history query yields no report file. If a full daily table cannot be rendered within available capacity, ask for a shorter period or for the general format before writing.
- Escape table-breaking characters from derived content and keep line breaks inside their cells. Do not repeat raw commit messages as activities or infer implementation, validation or deployment from a message. The coordinator supplies the layout, ordered rows, evidence and scope. The writer follows that layout instead of its general-purpose starter template.
- Maintained text and the new report layout reference use English. User-facing report language follows an explicit report-language instruction, then the request language, then English. Translate visible labels, dates' surrounding prose, empty-row messages and the save receipt. Preserve ISO dates, identifiers and literal paths.

## Destination and write authority

| Request | Outcome |
| --- | --- |
| Report content only or chat-only explicitly selected | Return the selected layout in the conversation. Create no files or directories. |
| Explicit local file request with no path | Use `activities-report/` directly under the selected worktree root. Create that single directory if absent. Write one Markdown report there and verify it by reading it back. |
| Explicit local file request with an exact path | Use the exact selected Markdown path, resolving repository-relative paths from the selected worktree root. A permitted absolute path is supported. Delegate the write and matching readback to the writer. The parent must already exist. |
| Ambiguous or unsupported explicit destination | Ask for an exact usable path or report the applicable permission/tool limit. Keep the default folder unused. |

Use stable filenames `activity-report-YYYY-MM-DD.md` for a one-day period and `activity-report-YYYY-MM-DD-to-YYYY-MM-DD.md` for multiple local dates. For instant ranges use the first and last intersected local dates, with the exact interval in the report. Filename collisions require explicit authorization to replace the exact target or a new user-selected path. Never silently add a suffix, overwrite, or fall back to a different destination.

The coordinator's default write exception covers the direct child directory and one Markdown file only, after explicit file intent, a resolved format and usable evidence. Use literal paths and require a host capability that keeps the default directory and target within the selected worktree during writing. Bind a missing directory to a protected handle in its creation operation or establish an equivalent uninterrupted identity guarantee. A conflicting entry or an unproven creation identity stops the save before the report write. Verify the reported path still names the read-back file. Reject symlinks, junctions or other indirection for the default directory and target. Check for collisions with a no-clobber creation primitive and require an authorized replacement to still match the previously inspected regular file. Before a default save, require a host guarantee that no additional hard link can expose the report bytes through the last write, for a new file as well as an authorized replacement. An unavailable hard-link guarantee blocks before filesystem mutation. A missing safe host primitive or changed target blocks the write. Preserve actual partial effects and report them. Do not create explicit-path parents, temporary/companion files, stage, commit, publish or change Git configuration. Runtime use requires no Python or other new installed dependency.

The shared writer's standalone write rules stay intact. Amend the repository policy to document the coordinator's narrow default-output exception. Track history status separately from output outcome. After a verified save, return the exact path and status in the chat, with any material coverage limitation. Include the full report inline only if requested. A failed write or readback never counts as a verified save.

## Acceptance

1. A new report asks for the format, even when the user supplied a preference. A follow-up choice resumes once. An unanswered question leaves the filesystem untouched.
2. For November 2–4, 2026, the daily layout shows three ordered local dates and preserves the no-match row for November 3 when coverage is complete. A limited run uses the qualified wording. The general layout still states the period.
3. A Spanish request produces a Spanish question, labels and report, with dates and identifiers preserved. An explicit report-language override applies to the rendered report.
4. An explicit file request without a path creates and verifies the deterministic Markdown in the selected worktree when the host can meet the write guards. An exact path takes precedence and a content-only request has no filesystem effects.
5. Existing files, missing explicit-path parents, unsafe default links, concurrent path conflicts and failed readback receive the defined outcomes. Git state and unrelated paths remain untouched.
