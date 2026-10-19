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
_MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")
_FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
_FENCE_CLOSE = re.compile(r"^ {0,3}(`+|~+)[ \t]*$")


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    path: str
    message: str


def _issue(code: str, message: str) -> ValidationIssue:
    return ValidationIssue(code=code, path="catalog.json", message=message)


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
            if candidate.is_dir() and candidate.name.casefold() == "tests":
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
    for match in _MARKDOWN_LINK.finditer(visible):
        raw_destination = match.group(1).strip()
        if raw_destination.startswith("<"):
            closing = raw_destination.find(">")
            if closing == -1:
                continue
            destination = raw_destination[1:closing]
        else:
            destination = raw_destination.split(maxsplit=1)[0] if raw_destination else ""
        parsed = urlsplit(destination)
        if parsed.scheme in {"http", "https", "mailto"} or not parsed.path:
            continue
        decoded = unquote(parsed.path)
        target = Path(decoded)
        candidate = target if target.is_absolute() else skill_root / target
        try:
            resolved = candidate.resolve(strict=False)
            resolved.relative_to(skill_root)
        except ValueError:
            issues.append(ValidationIssue("resource-escape", f"{relative_skill}/SKILL.md", f"Local link escapes the skill root: {destination!r}."))
            continue
        if not resolved.is_file():
            issues.append(ValidationIssue("missing-resource", f"{relative_skill}/SKILL.md", f"Linked skill resource does not exist: {destination!r}."))


def _mask_non_newlines(text: str, start: int, end: int) -> str:
    return "".join("\n" if character == "\n" else "\r" if character == "\r" else " " for character in text[start:end])


def _remove_fenced_code(body: str) -> str:
    """Mask fenced blocks, including an opening fence that runs to EOF."""
    lines = body.splitlines(keepends=True)
    masked = list(body)
    offset = 0
    index = 0
    while index < len(lines):
        line = lines[index].rstrip("\r\n")
        opening = _FENCE_OPEN.match(line)
        if opening is None or (opening.group(1)[0] == "`" and "`" in opening.group(2)):
            offset += len(lines[index])
            index += 1
            continue

        marker = opening.group(1)
        marker_char = marker[0]
        marker_size = len(marker)
        block_start = offset
        offset += len(lines[index])
        index += 1
        block_end = len(body)
        while index < len(lines):
            closing_line = lines[index].rstrip("\r\n")
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
