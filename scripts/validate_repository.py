"""Validate the maintained Devcraft Toolkit repository inventory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:  # The CLI reports a focused install hint when skills need parsing.
    yaml = None


_SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_ROLES = {"entry", "coordinator", "capability", "support"}
_STATUSES = {"planned", "available"}
_FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
_FENCE_CLOSE = re.compile(r"^ {0,3}(`+|~+)[ \t]*$")
_LIST_MARKER = re.compile(r"(?:[*+-]|[0-9]{1,9}[.)])(?=[ \t])")
_INVENTORY_SPEC = Path("docs/superpowers/specs/2026-10-16-bootstrap-foundation-design.md")
_INVENTORY_HEADING = "## Target capability inventory"
_INVENTORY_ROW = re.compile(r"^\|\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*\|\s*[^|\n]+\|\s*(?:planned|available)\s*\|$")
_MARKDOWN_ESCAPABLE = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    path: str
    message: str


def _issue(code: str, message: str) -> ValidationIssue:
    return ValidationIssue(code=code, path="catalog.json", message=message)


def _load_spec_inventory(root: Path) -> tuple[set[str] | None, str | None]:
    """Read the canonical target names when validating the full project root."""
    is_project_root = (root / "AGENTS.md").is_file()
    if not is_project_root:
        try:
            is_project_root = (root / "README.md").read_text(encoding="utf-8").splitlines()[0] == "# Devcraft Toolkit"
        except (OSError, UnicodeError, IndexError):
            is_project_root = False
    if not is_project_root:
        return None, None

    spec_path = root / _INVENTORY_SPEC
    try:
        lines = spec_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return None, f"Cannot read canonical skill inventory spec {_INVENTORY_SPEC.as_posix()}: {exc}"

    in_inventory = False
    names: list[str] = []
    for line in lines:
        if line.strip() == _INVENTORY_HEADING:
            in_inventory = True
            continue
        if in_inventory and line.startswith("## "):
            break
        if in_inventory:
            match = _INVENTORY_ROW.fullmatch(line)
            if match:
                names.append(match.group(1))

    if len(names) != 17 or len(set(names)) != 17:
        return None, f"The canonical inventory in {_INVENTORY_SPEC.as_posix()} must define exactly 17 unique skill names."
    return set(names), None


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate_repository(root: Path) -> list[ValidationIssue]:
    """Return structural issues found in the catalog, skills, and test layout."""
    root = Path(root).resolve()
    catalog_path = root / "catalog.json"
    try:
        data = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [_issue("catalog-schema", f"Cannot read valid catalog.json: {exc}")]

    issues: list[ValidationIssue] = []
    canonical_names, inventory_error = _load_spec_inventory(root)
    if inventory_error:
        issues.append(ValidationIssue("catalog-inventory", _INVENTORY_SPEC.as_posix(), inventory_error))
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data["schema_version"] != 1 or data.get("name") != "devcraft-toolkit" or not isinstance(data.get("skills"), list):
        return [_issue("catalog-schema", "Expected schema_version 1, name devcraft-toolkit, and a skills array.")]

    names: dict[str, dict] = {}
    paths: dict[str, str] = {}
    valid_entries: list[dict] = []
    for index, entry in enumerate(data["skills"]):
        location = f"catalog.json:skills[{index}]"
        if not isinstance(entry, dict):
            issues.append(ValidationIssue("catalog-schema", location, "Skill entries must be objects."))
            continue
        name = entry.get("name")
        role = entry.get("role")
        status = entry.get("status")
        skill_path = entry.get("path")
        requires = entry.get("requires")
        valid = True
        if not isinstance(name, str) or not _SKILL_NAME.fullmatch(name):
            issues.append(ValidationIssue("catalog-schema", location, "Skill name must be lowercase hyphenated ASCII."))
            valid = False
        if not isinstance(role, str) or role not in _ROLES or not isinstance(status, str) or status not in _STATUSES:
            issues.append(ValidationIssue("catalog-schema", location, "Skill role or status is not recognized."))
            valid = False
        if not isinstance(skill_path, str) or not skill_path or "\\" in skill_path or Path(skill_path).is_absolute() or any(part in {"", ".", ".."} for part in skill_path.split("/")):
            issues.append(ValidationIssue("invalid-path", location, "Skill path must be a normalized relative path without traversal."))
            valid = False
        else:
            resolved = (root / Path(*skill_path.split("/"))).resolve()
            if not _is_within(resolved, root):
                issues.append(ValidationIssue("invalid-path", location, "Skill path resolves outside the repository."))
                valid = False
        if not isinstance(requires, list) or any(not isinstance(item, str) for item in requires):
            issues.append(ValidationIssue("catalog-schema", location, "requires must be an array of skill names."))
            valid = False
        if not valid:
            continue
        valid_entries.append(entry)
        if name in names:
            issues.append(_issue("duplicate-name", f"Skill name {name!r} occurs more than once."))
        else:
            names[name] = entry
        if skill_path in paths:
            issues.append(_issue("duplicate-name", f"Skill path {skill_path!r} is shared by {paths[skill_path]!r} and {name!r}."))
        else:
            paths[skill_path] = name

    if canonical_names is not None:
        missing = sorted(canonical_names - names.keys())
        unexpected = sorted(names.keys() - canonical_names)
        if missing or unexpected:
            details = []
            if missing:
                details.append(f"missing from catalog: {', '.join(missing)}")
            if unexpected:
                details.append(f"not in spec: {', '.join(unexpected)}")
            issues.append(ValidationIssue(
                "catalog-inventory", "catalog.json", "Catalog names differ from the design spec (" + "; ".join(details) + ").",
            ))

    for entry in valid_entries:
        name = entry["name"]
        for dependency in entry["requires"]:
            if dependency not in names:
                issues.append(_issue("unknown-dependency", f"{name!r} requires unknown skill {dependency!r}."))
            elif entry["status"] == "available" and names[dependency]["status"] != "available":
                issues.append(_issue("unavailable-dependency", f"Available skill {name!r} requires planned skill {dependency!r}."))

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> bool:
        if name in visiting:
            return True
        if name in visited:
            return False
        visiting.add(name)
        cyclic = any(dep in names and visit(dep) for dep in names[name]["requires"])
        visiting.remove(name)
        visited.add(name)
        return cyclic

    if any(visit(name) for name in names):
        issues.append(_issue("dependency-cycle", "Skill dependencies contain a cycle."))

    if any(entry.get("status") == "available" for entry in names.values()) and yaml is None:
        issues.append(ValidationIssue(
            "missing-dependency", "requirements-dev.txt",
            "PyYAML is required to validate available skill frontmatter; install requirements-dev.txt.",
        ))

    for name, entry in names.items():
        skill_root = (root / Path(*entry["path"].split("/"))).resolve()
        expected_path = f"skills/{name}"
        if entry["path"] != expected_path:
            issues.append(ValidationIssue("invalid-path", f"catalog.json:skills/{name}", f"Catalog path must be {expected_path!r}."))
            continue
        skill_md = skill_root / "SKILL.md"
        if entry["status"] == "available":
            _validate_available_skill(root, name, skill_root, skill_md, issues)

    _validate_discoverable_skills(root, names, issues)
    _validate_test_ownership(root, names, issues)
    return issues


def _validate_available_skill(root: Path, name: str, skill_root: Path, skill_md: Path, issues: list[ValidationIssue]) -> None:
    relative_skill = f"skills/{name}"
    if not skill_md.is_file():
        issues.append(ValidationIssue("skill-frontmatter", f"{relative_skill}/SKILL.md", "Available skills require a readable SKILL.md."))
        return
    try:
        content = skill_md.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        issues.append(ValidationIssue("skill-frontmatter", f"{relative_skill}/SKILL.md", f"Cannot read SKILL.md: {exc}"))
        return

    lines = content.splitlines()
    closing = next((index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None) if lines and lines[0].strip() == "---" else None
    if closing is None:
        issues.append(ValidationIssue("skill-frontmatter", f"{relative_skill}/SKILL.md", "SKILL.md must begin with YAML frontmatter delimited by --- lines."))
        return
    if yaml is not None:
        try:
            metadata = yaml.safe_load("\n".join(lines[1:closing]))
        except (yaml.YAMLError, RecursionError) as exc:
            issues.append(ValidationIssue("skill-frontmatter", f"{relative_skill}/SKILL.md", f"Invalid YAML frontmatter: {exc}"))
            return
        if not isinstance(metadata, dict):
            issues.append(ValidationIssue("skill-frontmatter", f"{relative_skill}/SKILL.md", "Frontmatter must be a YAML mapping."))
            return
        skill_name = metadata.get("name")
        description = metadata.get("description")
        if (
            not isinstance(skill_name, str)
            or skill_name != name
            or len(skill_name) > 64
            or not _SKILL_NAME.fullmatch(skill_name)
            or not isinstance(description, str)
            or not description.strip()
            or len(description) > 1024
        ):
            issues.append(ValidationIssue("skill-frontmatter", f"{relative_skill}/SKILL.md", "Frontmatter needs the matching lowercase skill name (max 64 chars) and a nonempty description (max 1024 chars)."))

    body = "\n".join(lines[closing + 1:]).strip()
    if not body:
        issues.append(ValidationIssue("skill-body", f"{relative_skill}/SKILL.md", "Skill instructions must have a nonempty body."))
    _validate_skill_links(name, skill_root, body, issues)

    try:
        for candidate in skill_root.rglob("*"):
            if candidate.is_symlink():
                try:
                    candidate.resolve(strict=False).relative_to(skill_root)
                except ValueError:
                    issues.append(ValidationIssue("resource-escape", candidate.relative_to(root).as_posix(), "Skill symlink resolves outside the skill root."))
            if candidate.is_dir() and candidate.name.casefold() in {"test", "tests"}:
                issues.append(ValidationIssue("skill-local-tests", candidate.relative_to(root).as_posix(), "Tests must be kept under the repository-root tests/ directory."))
            elif candidate.is_file() and candidate.suffix.casefold() == ".py" and (
                candidate.name.casefold().startswith("test")
                or candidate.name.casefold().endswith("_test.py")
                or candidate.name.casefold() == "conftest.py"
            ):
                issues.append(ValidationIssue("skill-local-tests", candidate.relative_to(root).as_posix(), "Test modules must be kept under the repository-root tests/ directory."))
    except OSError as exc:
        issues.append(ValidationIssue("resource-escape", relative_skill, f"Cannot inspect skill resources safely: {exc}"))


def _validate_skill_links(name: str, skill_root: Path, body: str, issues: list[ValidationIssue]) -> None:
    relative_skill = f"skills/{name}"
    without_fences = _remove_fenced_code(body)
    visible = _remove_inline_code(without_fences)
    visible, reference_definitions = _remove_reference_definitions(visible)
    reference_destinations = [
        reference_definitions[label]
        for label in dict.fromkeys(_iter_reference_labels(visible, reference_definitions))
    ]
    destinations = [*reference_destinations, *_iter_inline_link_destinations(visible)]
    for destination in destinations:
        if destination is None:
            issues.append(ValidationIssue(
                "invalid-link-destination", f"{relative_skill}/SKILL.md",
                "Cannot safely interpret a Markdown link destination.",
            ))
            continue
        try:
            parsed = urlsplit(destination)
        except ValueError:
            issues.append(ValidationIssue(
                "invalid-link-destination", f"{relative_skill}/SKILL.md",
                f"Cannot safely interpret Markdown link destination {destination!r}.",
            ))
            continue
        scheme = parsed.scheme.casefold()
        windows_drive = len(scheme) == 1 and destination[1:2] == ":"
        if not windows_drive and (scheme or parsed.netloc):
            if scheme != "file":
                continue
        raw_path = destination if windows_drive else parsed.path
        if not raw_path:
            continue
        decoded = unquote(raw_path)
        target = Path(decoded)
        candidate = target if target.is_absolute() else skill_root / target
        try:
            resolved = candidate.resolve(strict=False)
        except (OSError, RuntimeError, ValueError):
            issues.append(ValidationIssue(
                "invalid-link-destination", f"{relative_skill}/SKILL.md",
                f"Cannot safely resolve Markdown link destination {destination!r}.",
            ))
            continue
        try:
            resolved.relative_to(skill_root)
        except ValueError:
            issues.append(ValidationIssue("resource-escape", f"{relative_skill}/SKILL.md", f"Local link escapes the skill root: {destination!r}."))
            continue
        if not resolved.is_file():
            issues.append(ValidationIssue("missing-resource", f"{relative_skill}/SKILL.md", f"Linked skill resource does not exist: {destination!r}."))


def _is_escaped(text: str, index: int) -> bool:
    slashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        slashes += 1
        index -= 1
    return slashes % 2 == 1


def _unescape_markdown(value: str) -> str:
    result: list[str] = []
    index = 0
    while index < len(value):
        if (
            value[index] == "\\"
            and index + 1 < len(value)
            and value[index + 1] in _MARKDOWN_ESCAPABLE
        ):
            index += 1
        result.append(value[index])
        index += 1
    return "".join(result)


def _matching_square_bracket(text: str, opening: int) -> int | None:
    if opening >= len(text) or text[opening] != "[" or _is_escaped(text, opening):
        return None
    depth = 0
    index = opening
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            index += 2
            continue
        if text[index] == "[":
            depth += 1
        elif text[index] == "]":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def _parse_reference_destination(text: str) -> str | None:
    text = text.lstrip(" \t")
    if not text:
        return None
    if text[0] == "<":
        index = 1
        while index < len(text):
            if text[index] in "\r\n":
                return None
            if text[index] == ">" and not _is_escaped(text, index):
                return _unescape_markdown(text[1:index])
            index += 1
        return None

    start = index = 0
    depth = 0
    while index < len(text):
        character = text[index]
        if character == "\\" and index + 1 < len(text):
            index += 2
            continue
        if character.isspace():
            break
        if character == "<":
            return None
        if character == "(":
            depth += 1
            if depth > 32:
                return None
        elif character == ")":
            if depth == 0:
                return None
            depth -= 1
        index += 1
    if depth or index == start:
        return None
    return _unescape_markdown(text[start:index])


def _normalize_reference_label(label: str) -> str:
    return re.sub(r"\s+", " ", _unescape_markdown(label)).strip().casefold()


def _strip_markdown_container_prefix(line: str) -> tuple[str, int]:
    """Strip simple blockquote/list prefixes for block-level Markdown checks."""
    index = 0
    blockquotes = 0
    while index < len(line):
        spaces = 0
        while index + spaces < len(line) and line[index + spaces] == " ":
            spaces += 1
        if spaces > 3:
            break
        cursor = index + spaces
        if cursor < len(line) and line[cursor] == ">":
            blockquotes += 1
            index = cursor + 1
            if index < len(line) and line[index] in " \t":
                index += 1
            continue

        marker = _LIST_MARKER.match(line, cursor)
        if marker is None:
            index = cursor
            break
        index = marker.end()
        whitespace_start = index
        while index < len(line) and line[index] in " \t":
            index += 1
        if index == whitespace_start:
            break
        if line[whitespace_start:index].count(" ") > 4 or "\t" in line[whitespace_start:index]:
            # Leave excess indentation visible so an indented code block is not
            # mistaken for a fence or a reference definition.
            index = whitespace_start + 1
            break
    return line[index:], blockquotes


def _strip_blockquote_prefix(line: str) -> tuple[str, int]:
    """Strip only blockquote markers, preserving list-like code content."""
    index = 0
    blockquotes = 0
    while index < len(line):
        spaces = 0
        while index + spaces < len(line) and line[index + spaces] == " ":
            spaces += 1
        if spaces > 3:
            break
        cursor = index + spaces
        if cursor >= len(line) or line[cursor] != ">":
            break
        blockquotes += 1
        index = cursor + 1
        if index < len(line) and line[index] in " \t":
            index += 1
    return line[index:], blockquotes


def _leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _list_item_indentation(line: str, base_indent: int = 0) -> tuple[int, int] | None:
    relative_line = line[base_indent:]
    marker_indent = _leading_spaces(relative_line)
    if marker_indent > 3:
        return None
    marker = _LIST_MARKER.match(relative_line, marker_indent)
    if marker is None:
        return None

    whitespace_start = marker.end()
    whitespace_end = whitespace_start
    while whitespace_end < len(relative_line) and relative_line[whitespace_end] in " \t":
        whitespace_end += 1
    if whitespace_end == whitespace_start:
        return None
    whitespace = relative_line[whitespace_start:whitespace_end]
    whitespace_columns = 1 if "\t" in whitespace or len(whitespace) > 4 else len(whitespace)
    absolute_marker_indent = base_indent + marker_indent
    content_indent = absolute_marker_indent + (marker.end() - marker_indent) + whitespace_columns
    return absolute_marker_indent, content_indent


def _normalize_list_continuation(
    line: str,
    blockquotes: int,
    list_contexts: list[tuple[int, int, int]],
) -> str:
    """Remove the active list item's content indentation and track nested items."""
    if not line.strip(" \t"):
        return line

    indentation = _leading_spaces(line)
    while list_contexts:
        context_quotes, _, content_indent = list_contexts[-1]
        if context_quotes > blockquotes or (context_quotes == blockquotes and indentation < content_indent):
            list_contexts.pop()
            continue
        break

    base_indent = 0
    if list_contexts and list_contexts[-1][0] == blockquotes:
        base_indent = list_contexts[-1][2]
    if indentation < base_indent:
        base_indent = 0
    normalized = line[base_indent:]

    marker_indentation = _list_item_indentation(line, base_indent)
    if marker_indentation is not None:
        marker_indent, content_indent = marker_indentation
        while (
            list_contexts
            and list_contexts[-1][0] == blockquotes
            and list_contexts[-1][1] >= marker_indent
        ):
            list_contexts.pop()
        list_contexts.append((blockquotes, marker_indent, content_indent))
    return normalized


def _strip_active_list_indent(
    line: str,
    blockquotes: int,
    list_contexts: list[tuple[int, int, int]],
) -> tuple[str, bool]:
    base_indent = next(
        (content_indent for context_quotes, _, content_indent in reversed(list_contexts) if context_quotes == blockquotes),
        0,
    )
    if not base_indent:
        return line, True
    if _leading_spaces(line) < base_indent:
        return line, False
    return line[base_indent:], True


def _remove_reference_definitions(body: str) -> tuple[str, dict[str, str | None]]:
    """Extract reference definitions in simple containers and mask their lines."""
    masked = list(body)
    definitions: dict[str, str | None] = {}
    list_contexts: list[tuple[int, int, int]] = []
    offset = 0
    for line in body.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        quoted, blockquotes = _strip_blockquote_prefix(content)
        continued = _normalize_list_continuation(quoted, blockquotes, list_contexts)
        normalized, _ = _strip_markdown_container_prefix(continued)
        indent = len(normalized) - len(normalized.lstrip(" "))
        if indent <= 3 and indent < len(normalized) and normalized[indent] == "[":
            closing = _matching_square_bracket(normalized, indent)
            if closing is not None and closing + 1 < len(normalized) and normalized[closing + 1] == ":":
                label = _normalize_reference_label(normalized[indent + 1:closing])
                if label and label not in definitions:
                    definitions[label] = _parse_reference_destination(normalized[closing + 2:])
                masked[offset:offset + len(line)] = _mask_non_newlines(body, offset, offset + len(line))
        offset += len(line)
    return "".join(masked), definitions


def _iter_reference_labels(text: str, definitions: dict[str, str | None]) -> list[str]:
    """Resolve shortcut, collapsed, and full reference uses against definitions."""
    labels: list[str] = []
    index = 0
    while index < len(text):
        if text[index] != "[" or _is_escaped(text, index):
            index += 1
            continue
        closing = _matching_square_bracket(text, index)
        if closing is None:
            index += 1
            continue

        content_label = _normalize_reference_label(text[index + 1:closing])
        next_index = closing + 1
        if next_index < len(text) and text[next_index] == "(":
            parsed = _parse_inline_link_destination(text, next_index)
            index = parsed[1] if parsed is not None else next_index + 1
            continue
        if next_index < len(text) and text[next_index] == "[":
            reference_end = _matching_square_bracket(text, next_index)
            if reference_end is not None:
                explicit_label = _normalize_reference_label(text[next_index + 1:reference_end])
                label = explicit_label or content_label
                if label in definitions:
                    labels.append(label)
                index = reference_end + 1
                continue
        if content_label in definitions:
            labels.append(content_label)
        index = closing + 1
    return labels


def _parse_inline_link_destination(text: str, opening: int) -> tuple[str, int] | None:
    index = opening + 1
    while index < len(text) and text[index].isspace():
        index += 1
    if index < len(text) and text[index] == ")":
        return "", index + 1
    if index >= len(text):
        return None

    if text[index] == "<":
        destination_start = index + 1
        index = destination_start
        while index < len(text):
            if text[index] in "\r\n":
                return None
            if text[index] == ">" and not _is_escaped(text, index):
                break
            index += 1
        if index >= len(text):
            return None
        destination = _unescape_markdown(text[destination_start:index])
        index += 1
    else:
        destination_start = index
        depth = 0
        while index < len(text):
            character = text[index]
            if character == "\\" and index + 1 < len(text):
                index += 2
                continue
            if character.isspace():
                break
            if character == "<":
                return None
            if character == "(":
                depth += 1
                if depth > 32:
                    return None
            elif character == ")":
                if depth == 0:
                    break
                depth -= 1
            index += 1
        if depth:
            return None
        destination = _unescape_markdown(text[destination_start:index])

    before_whitespace = index
    while index < len(text) and text[index].isspace():
        index += 1
    if index < len(text) and text[index] == ")":
        return destination, index + 1
    if index == before_whitespace:
        return None

    title_end = _parse_link_title(text, index)
    if title_end is None:
        return None
    index = title_end
    while index < len(text) and text[index].isspace():
        index += 1
    if index < len(text) and text[index] == ")":
        return destination, index + 1
    return None


def _parse_link_title(text: str, start: int) -> int | None:
    if start >= len(text) or text[start] not in {'"', "'", "("}:
        return None
    opening = text[start]
    closing = ")" if opening == "(" else opening
    depth = 1 if opening == "(" else 0
    index = start + 1
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            index += 2
            continue
        if opening == "(" and text[index] == "(":
            depth += 1
        elif text[index] == closing:
            if opening != "(" or depth == 1:
                return index + 1
            depth -= 1
        index += 1
    return None


def _iter_inline_link_destinations(text: str) -> list[str | None]:
    destinations: list[str | None] = []
    index = 0
    while index < len(text):
        if text[index] != "[" or _is_escaped(text, index):
            index += 1
            continue
        closing = _matching_square_bracket(text, index)
        if closing is None or closing + 1 >= len(text) or text[closing + 1] != "(":
            index += 1
            continue
        parsed = _parse_inline_link_destination(text, closing + 1)
        if parsed is None:
            destinations.append(None)
            index = closing + 2
            continue
        destination, index = parsed
        if destination:
            destinations.append(destination)
    return destinations


def _mask_non_newlines(text: str, start: int, end: int) -> str:
    return "".join("\n" if character == "\n" else "\r" if character == "\r" else " " for character in text[start:end])


def _remove_fenced_code(body: str) -> str:
    """Mask fenced blocks until their fence or containing block ends."""
    lines = body.splitlines(keepends=True)
    masked = list(body)
    list_contexts: list[tuple[int, int, int]] = []
    offset = 0
    index = 0
    while index < len(lines):
        raw_line = lines[index].rstrip("\r\n")
        quoted, blockquotes = _strip_blockquote_prefix(raw_line)
        continued = _normalize_list_continuation(quoted, blockquotes, list_contexts)
        line, nested_blockquotes = _strip_markdown_container_prefix(continued)
        opening_blockquotes = blockquotes + nested_blockquotes
        opening = _FENCE_OPEN.match(line)
        if opening is None or (opening.group(1)[0] == "`" and "`" in opening.group(2)):
            offset += len(lines[index])
            index += 1
            continue

        marker = opening.group(1)
        marker_char = marker[0]
        marker_size = len(marker)
        block_start = offset
        opening_list_contexts = list(list_contexts)
        offset += len(lines[index])
        index += 1
        block_end = len(body)
        while index < len(lines):
            raw_closing_line = lines[index].rstrip("\r\n")
            if opening_blockquotes:
                closing_line, closing_blockquotes = _strip_blockquote_prefix(raw_closing_line)
                if closing_blockquotes < opening_blockquotes:
                    block_end = offset
                    break
                if closing_blockquotes > opening_blockquotes:
                    offset += len(lines[index])
                    index += 1
                    continue
            else:
                closing_line = raw_closing_line
            closing_line, inside_list = _strip_active_list_indent(
                closing_line, opening_blockquotes, opening_list_contexts,
            )
            if not inside_list:
                block_end = offset
                break
            closing = _FENCE_CLOSE.match(closing_line)
            if closing is not None and closing.group(1)[0] == marker_char and len(closing.group(1)) >= marker_size:
                offset += len(lines[index])
                index += 1
                block_end = offset
                break
            offset += len(lines[index])
            index += 1
        masked[block_start:block_end] = _mask_non_newlines(body, block_start, block_end)
    return "".join(masked)


def _remove_inline_code(body: str) -> str:
    """Mask CommonMark-style inline code spans with exact-length delimiters."""
    masked = list(body)
    index = 0
    while index < len(body):
        if body[index] != "`":
            index += 1
            continue
        opening_end = index + 1
        while opening_end < len(body) and body[opening_end] == "`":
            opening_end += 1
        opening_size = opening_end - index
        preceding_slashes = 0
        slash_index = index - 1
        while slash_index >= 0 and body[slash_index] == "\\":
            preceding_slashes += 1
            slash_index -= 1
        if preceding_slashes % 2:
            index = opening_end
            continue

        paragraph_break = re.search(r"\r?\n[ \t]*\r?\n", body[opening_end:])
        paragraph_end = opening_end + paragraph_break.start() if paragraph_break else len(body)
        cursor = opening_end
        closing_end = None
        while cursor < paragraph_end:
            closing_start = body.find("`", cursor, paragraph_end)
            if closing_start == -1:
                break
            candidate_end = closing_start + 1
            while candidate_end < len(body) and body[candidate_end] == "`":
                candidate_end += 1
            if candidate_end - closing_start == opening_size:
                closing_end = candidate_end
                break
            cursor = candidate_end
        if closing_end is None:
            index = opening_end
            continue
        masked[index:closing_end] = _mask_non_newlines(body, index, closing_end)
        index = closing_end
    return "".join(masked)


def _validate_discoverable_skills(root: Path, names: dict[str, dict], issues: list[ValidationIssue]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return
    catalog_paths = {entry["path"]: entry for entry in names.values()}
    for candidate in skills_root.rglob("SKILL.md"):
        if not candidate.is_file():
            continue
        relative_parent = candidate.parent.relative_to(root).as_posix()
        if relative_parent in catalog_paths:
            if catalog_paths[relative_parent]["status"] == "planned":
                issues.append(ValidationIssue("planned-placeholder", candidate.relative_to(root).as_posix(), "Planned skills must not expose SKILL.md."))
            continue
        if any(
            entry["status"] == "planned" and relative_parent.startswith(f"{skill_path}/")
            for skill_path, entry in catalog_paths.items()
        ):
            issues.append(ValidationIssue("planned-placeholder", candidate.relative_to(root).as_posix(), "Planned skills must not expose nested SKILL.md files."))
        else:
            issues.append(ValidationIssue("unlisted-skill", candidate.parent.relative_to(root).as_posix(), "Discoverable skill directory is absent from catalog.json."))


def _validate_test_ownership(root: Path, names: dict[str, dict], issues: list[ValidationIssue]) -> None:
    skill_tests = root / "tests" / "skills"
    if not skill_tests.is_dir():
        return
    known_packages = {name.replace("-", "_") for name in names}
    for package in skill_tests.iterdir():
        if package.name == "__pycache__":
            continue
        if package.is_file() and package.name != "__init__.py" and package.suffix.casefold() == ".py":
            issues.append(ValidationIssue("test-ownership", package.relative_to(root).as_posix(), "Skill test modules must belong to a catalog skill package."))
        elif package.is_dir() and package.name not in known_packages:
            issues.append(ValidationIssue("test-ownership", package.relative_to(root).as_posix(), "Skill test package does not map to a catalog skill."))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Repository root to validate")
    args = parser.parse_args(argv)
    issues = validate_repository(args.root)
    if issues:
        for issue in issues:
            print(f"{issue.code}: {issue.path}: {issue.message}")
        return 1
    print("Repository catalog is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
