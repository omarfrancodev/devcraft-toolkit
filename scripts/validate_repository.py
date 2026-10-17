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
_FENCED_CODE = re.compile(r"(?m)^\s*(```+|~~~+).*?^\s*\1\s*$", re.DOTALL)
_INLINE_CODE = re.compile(r"(`+).*?\1", re.DOTALL)


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
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("name") != "devcraft-toolkit" or not isinstance(data.get("skills"), list):
        return [_issue("catalog-schema", "Expected schema_version 1, name devcraft-toolkit, and a skills array.")]

    names: dict[str, dict] = {}
    paths: dict[str, str] = {}
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
        if name in names:
            issues.append(_issue("duplicate-name", f"Skill name {name!r} occurs more than once."))
        else:
            names[name] = entry
        if skill_path in paths:
            issues.append(_issue("duplicate-name", f"Skill path {skill_path!r} is shared by {paths[skill_path]!r} and {name!r}."))
        else:
            paths[skill_path] = name

    for name, entry in names.items():
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

    if any(visit(name) for name in names) and not any(item.code == "dependency-cycle" for item in issues):
        issues.append(_issue("dependency-cycle", "Skill dependencies contain a cycle."))

    if any(entry.get("status") == "available" for entry in names.values()) and yaml is None:
        issues.append(ValidationIssue(
            "missing-dependency", "requirements-dev.txt",
            "PyYAML is required to validate available skill frontmatter; install requirements-dev.txt.",
        ))
        return issues

    for name, entry in names.items():
        skill_root = (root / Path(*entry["path"].split("/"))).resolve()
        expected_path = f"skills/{name}"
        if entry["path"] != expected_path:
            issues.append(ValidationIssue("invalid-path", f"catalog.json:skills/{name}", f"Catalog path must be {expected_path!r}."))
            continue
        skill_md = skill_root / "SKILL.md"
        if entry["status"] == "planned":
            if skill_md.exists():
                issues.append(ValidationIssue("planned-placeholder", f"{entry['path']}/SKILL.md", "Planned skills must not expose SKILL.md."))
            continue
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
    try:
        metadata = yaml.safe_load("\n".join(lines[1:closing]))
    except yaml.YAMLError as exc:
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
            if candidate.is_dir() and candidate.name == "tests":
                issues.append(ValidationIssue("skill-local-tests", candidate.relative_to(root).as_posix(), "Tests must be kept under the repository-root tests/ directory."))
            elif candidate.is_file() and candidate.name.startswith("test_") and candidate.suffix == ".py":
                issues.append(ValidationIssue("skill-local-tests", candidate.relative_to(root).as_posix(), "Test modules must be kept under the repository-root tests/ directory."))
    except OSError as exc:
        issues.append(ValidationIssue("resource-escape", relative_skill, f"Cannot inspect skill resources safely: {exc}"))


def _validate_skill_links(name: str, skill_root: Path, body: str, issues: list[ValidationIssue]) -> None:
    relative_skill = f"skills/{name}"
    without_fences = _FENCED_CODE.sub("", body)
    visible = _INLINE_CODE.sub("", without_fences)
    for match in _MARKDOWN_LINK.finditer(visible):
        destination = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
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


def _validate_discoverable_skills(root: Path, names: dict[str, dict], issues: list[ValidationIssue]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return
    for candidate in skills_root.iterdir():
        if candidate.is_dir() and (candidate / "SKILL.md").exists() and candidate.name not in names:
            issues.append(ValidationIssue("unlisted-skill", candidate.relative_to(root).as_posix(), "Discoverable skill directory is absent from catalog.json."))


def _validate_test_ownership(root: Path, names: dict[str, dict], issues: list[ValidationIssue]) -> None:
    skill_tests = root / "tests" / "skills"
    if not skill_tests.is_dir():
        return
    known_packages = {name.replace("-", "_") for name in names}
    for package in skill_tests.iterdir():
        if package.is_dir() and package.name not in known_packages:
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
