# Behavioral scenarios: using-devcraft-toolkit

Canonical owner: `using-devcraft-toolkit`.

## Language resolution

For each request, resolve one response language using explicit user preference first, then the language of the request, then English when indeterminate. Keep technical identifiers, catalog keys, status labels, and commands unchanged.

1. English request, no preference: route and respond in English.
2. Spanish request, no preference: route and respond in Spanish, translating explanatory labels while preserving skill names and commands.
3. French request, no preference: respond in French with the same identifier preservation.
4. English request with “responde en español”: respond in Spanish.
5. Language-indeterminate input: use English.
6. A later explicit language instruction during the same execution changes the resolved language for subsequent output.

Expected evidence: the same scope decision is applied regardless of language; only natural-language content and visible template labels change.

## Routing and availability

- A repository-context request can use `git-working-directory-policy` when that skill is installed.
- A Git preflight request can use `git-safety-check` and its declared `git-working-directory-policy` dependency.
- Git commit-creation, publication, and Git-history activity-report coordinator requests must clearly state that the target capability is planned or not installed in this distribution. Do not emulate a missing coordinator or claim completion.
- An unrelated request, such as explaining a Python expression, must not auto-load the toolkit entry.
- When an individual skill is installed without the repository checkout, it must not try to open the development-only `catalog.json` or root documentation.

Expected evidence: route only within the requested scope, report actual installed capabilities, and retain any unresolved user decision without performing an unrelated operation.
## Conventional Commit composition cases

Canonical composed capability: `conventional-commits-style`.

```yaml
cases:
  - id: FORMATTING-ENTRY-01
    name: direct_call
    request: "Invoke conventional-commits-style directly with its first owned scenario."
    facts: "The standalone skill is installed; no repository root is supplied to it."
    assertions:
      - "The owned behavior is preserved; no development catalog or root docs are required at runtime."
  - id: FORMATTING-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit for the commit message formatting request in the first owned scenario."
    facts: "The entry, its foundation dependencies and conventional-commits-style are installed."
    assertions:
      - "Route the request to conventional-commits-style without running an unrelated Git preflight or another coordinator."
      - "Ask which issue applies before drafting; after TASK-13 is selected, preserve the Conventional Commit subject and put only that key in a footer."
      - "Language and permission boundaries remain those of the owned scenario."
  - id: FORMATTING-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit for the same commit message formatting request."
    facts: "The entry and foundation group are installed, but conventional-commits-style is not."
    assertions:
      - "Report the missing capability honestly without emulation, automatic installation or an invented completed result."
```

## validation-discovery composition cases

Canonical composed capability: `validation-discovery`.

The direct and installed-route variants use the first standalone discovery packet: “Discover validation commands; do not run them.” Supplied evidence: `package.json` contains `scripts.check = "python check.py pass"`. The absent variant has the same request and evidence, with the capability installation state changed as specified below. This packet is read-only; no project command may run.

```yaml
cases:
  - id: VALIDATION-ENTRY-01
    name: direct_call
    request: "Invoke validation-discovery directly with its first owned scenario."
    facts: "The new standalone capability is installed; no repository root is supplied to the installed skill."
    assertions:
      - "The owned behavior is preserved; no development catalog or root docs are required at runtime."
  - id: VALIDATION-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit for the project validation discovery request in the first owned scenario."
    facts: "The entry, its foundation dependencies and validation-discovery are actually installed."
    assertions:
      - "Route the requested operation to validation-discovery without running an unrelated Git preflight or another coordinator."
      - "Language and permission boundaries remain those of the owned scenario."
  - id: VALIDATION-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit for the same project validation discovery request."
    facts: "The entry and foundation group are installed, but validation-discovery is not."
    assertions:
      - "Report the missing capability honestly without emulation, automatic installation or an invented completed result."
```

## todo-workflow-controller composition cases

Canonical composed capability: `todo-workflow-controller`.

```yaml
cases:
  - id: PROGRESS-ENTRY-01
    name: direct_call
    request: "Invoke todo-workflow-controller for this request: Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped."
    facts: "Inspect completed; validation failed; summary is optional and omitted. The standalone skill is installed; no repository root is supplied."
    assertions:
      - "Preserve the owned behavior; no development catalog or root docs are required at runtime."
      - "Keep required validation incomplete, dependent publish blocked or pending, and optional summary skipped."
  - id: PROGRESS-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit for this request: Track inspect -> validate -> publish before a tight deadline. Validation is required. An optional summary may be skipped. Tell me which installed skill will track the workflow."
    facts: "Inspect completed; validation failed; summary is optional and omitted. The entry, its foundation dependencies and todo-workflow-controller are installed; no progress tool or repository root is supplied."
    assertions:
      - "Name and route to todo-workflow-controller as the installed progress capability; make the selection observable in the response."
      - "Treat publish as a workflow step and do not run a Git preflight or publication workflow."
      - "Preserve the owned progress behavior, language and permission boundaries."
  - id: PROGRESS-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit for the same portable progress-control request."
    facts: "The entry and foundation group are installed, but todo-workflow-controller is not. The user asks to track the same failed-validation workflow."
    assertions:
      - "Report the missing capability honestly without emulation, automatic installation or an invented completed result."
```

## Natural-language report writer composition cases

Canonical composed capability: `natural-language-report-writer`.

```yaml
cases:
  - id: REPORTING-ENTRY-01
    name: direct_call
    request: "Invoke natural-language-report-writer directly with its first owned scenario."
    facts: "The new standalone capability is installed; no repository root is supplied to the installed skill."
    assertions:
      - "The owned behavior is preserved; no development catalog or root docs are required at runtime."
  - id: REPORTING-ENTRY-02
    name: optional_entry_route
    request: "Use Devcraft Toolkit to write an activity report from these supplied facts. Return it here in Spanish."
    facts: "Date: 2026-10-20. Empty-name validation was added. A clear error for missing names was added. Search rendering is pending. Twelve fixture cases passed. The entry, its foundation dependencies and natural-language-report-writer are actually installed."
    assertions:
      - "Route the supplied-facts report request to natural-language-report-writer without running an unrelated Git preflight or another coordinator."
      - "Do not describe supplied-facts reporting as unavailable when natural-language-report-writer is installed; return a Spanish report from only the supplied facts, preserving the date, count, and pending status, with no Git inspection or file write."
  - id: REPORTING-ENTRY-03
    name: optional_skill_absent
    request: "Use Devcraft Toolkit to write an activity report from these supplied facts. Return it here in Spanish."
    facts: "Date: 2026-10-20. Empty-name validation was added. A clear error for missing names was added. Search rendering is pending. Twelve fixture cases passed. The entry and foundation group are installed, but natural-language-report-writer is not."
    assertions:
      - "Report natural-language-report-writer as unavailable without drafting the report, imitating it, or installing it automatically."
```

## Installation ownership packets

Use fresh contexts with the current entry and local reference. These synthetic discovery facts test instructions, not native metadata.

| Packet | Request and discovery facts | Assertions |
| --- | --- | --- |
| ROUTE-INSTALL-01 | Spanish commit proposal from added empty-name validation, no issue. Entry/foundation and formatter belong to suite-A, package devcraft-toolkit. Formatter invocation: devcraft-toolkit:conventional-commits-style. | Use that owned discovered identifier; Spanish proposal; no Git preflight. |
| ROUTE-INSTALL-02 | Same request. Entry/foundation belong to suite-A. Only formatter is foreign-tools:conventional-commits-style, owned by foreign-tools B. B is not selected. | Report formatter unavailable in selected installation; no foreign invocation, imitation or install. |
| ROUTE-INSTALL-03 | Same request. Two formatters: devcraft-toolkit:conventional-commits-style and standalone conventional-commits-style. Provenance and active entry ownership unresolved; no user selection. | Ask one focused installation choice before dependent invocation; preserve both. |
| ROUTE-INSTALL-04 | English request explicitly selects standalone installation: draft commit from added empty-name validation, no issue, then discover checks. Selected standalone formatter exists; selected set lacks validation-discovery. Other suite offers formatter and validation-discovery. | Use selected standalone identifier; English proposal; report missing validation capability without substitution/checks/install. |

Recheck existing direct formatter, optional routes, absent capabilities, language preference and planned coordinator boundaries. Capture actual actions and responses separately from native activation.
