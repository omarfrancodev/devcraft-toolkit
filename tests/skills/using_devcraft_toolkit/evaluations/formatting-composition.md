# Conventional Commit composition evaluation

Date: 2026-10-22

Canonical skill owners: `using-devcraft-toolkit`, `conventional-commits-style`.

## Method

Fresh agent contexts in Codex desktop assessed each case. Actors manually followed only the skill files available in the simulated installation. The harness did not expose native loading of repository-local skills. No actor ran Git, queried tickets, installed a skill, or changed repository state.

## Pre-change results

### FORMATTING-ENTRY-01 — direct call

With only `conventional-commits-style` and its local reference available, the first response asked which issue to use. After `Use TASK-13`, it returned:

~~~text
fix(parser): reject empty names with a clear error

Refs: TASK-13
~~~

**PASS.** The standalone behavior needed no entry, repository root, catalog, or root documentation.

### FORMATTING-ENTRY-02 — optional route

Two fresh contexts followed the unchanged entry with the formatter listed as installed. One used the entry's skill-discovery instruction and the formatter description, asked which issue applied, then returned the same subject and `Refs: TASK-13` footer. It performed no Git operation (**PASS**).

A second context interpreted the entry's Git preflight bullet as covering the message-formatting request and responded, “Commit-message formatting is not available through the current Devcraft Toolkit entry. I can run a read-only Git commit safety preflight, but it will not draft a message.” After `Use TASK-13`, it still produced no proposal. It performed no Git operation (**FAIL**: the route and owned formatting behavior were not preserved).

The disagreement showed that generic skill discovery did not make the optional route reliable. The entry now names the formatter route and states that message drafting alone does not request a Git preflight.

### FORMATTING-ENTRY-03 — formatter absent

With only the entry and foundation group installed, the response was: “Conventional Commit formatting isn’t available in this installation, so I can’t draft the message. The installed foundation skills provide repository context and read-only Git preflight; neither handles commit-message formatting.”

**PASS.** No message was drafted, no tool or installation action occurred, and no completion was claimed.

## GREEN results

### FORMATTING-ENTRY-01 — direct call

The candidate standalone skill asked which issue to reference. After the user selected TASK-13, it returned:

~~~text
fix(parser): reject empty names with a clear error

Refs: TASK-13
~~~

**PASS.** No repository context or tool was used. The candidate was unchanged by the composition update.

### FORMATTING-ENTRY-02 — optional route

With the updated entry, composition reference, foundation group, and formatter installed, the response asked which issue applied. After `Use TASK-13`, it returned:

~~~text
fix(parser): reject empty names with a clear error

Refs: TASK-13
~~~

**PASS.** The entry invoked the formatter, retained English and the confirmed issue, and ran no Git preflight or other tool.

### FORMATTING-ENTRY-03 — formatter absent

With the updated entry and foundation group installed but no formatter, the response was: “I can’t draft this commit message because `conventional-commits-style` is not installed in this harness. No message was drafted, and no Git preflight or repository operation was performed.”

**PASS.** It reported the missing capability without choosing an issue, imitating the formatter, installing anything, or claiming completion.

## Assessment

The standalone capability works directly and can be selected without a repository. The entry needs no hard dependency on it, but its optional route is now explicit so message drafting does not collide with Git preflight or planned commit creation. The absent-installation route remains truthful.
