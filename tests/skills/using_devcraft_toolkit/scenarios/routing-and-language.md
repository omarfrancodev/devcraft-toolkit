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
- Commit, publish, and activity-report requests must clearly state that the target capability is planned or not installed in this distribution. Do not emulate a missing coordinator or claim completion.
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
