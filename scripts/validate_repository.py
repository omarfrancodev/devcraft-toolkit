"""Validate the maintained Devcraft Toolkit repository inventory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


_SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_ROLES = {"entry", "coordinator", "capability", "support"}
_STATUSES = {"planned", "available"}


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
    """Return structural issues found in the root catalog."""
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
    return issues


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
