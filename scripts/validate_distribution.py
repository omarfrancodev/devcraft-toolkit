"""Validate the toolkit's local distribution contract without installing it."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

from scripts.validate_repository import ValidationIssue, validate_repository

_NAME = "devcraft-toolkit"
_DESCRIPTION = "Composable Git and development skills for coding agents."
_AUTHOR = {"name": "omarfrancodev"}
_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
_NUMBER = r"(?:0|[1-9][0-9]*)"
_IDENTIFIER = r"(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
_VERSION = re.compile(
    rf"{_NUMBER}\.{_NUMBER}\.{_NUMBER}"
    rf"(?:-{_IDENTIFIER}(?:\.{_IDENTIFIER})*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)


def _read_object(root: Path, relative: str, issues: list[ValidationIssue]) -> dict | None:
    path = root / relative
    try:
        if not path.resolve().is_relative_to(root):
            issues.append(ValidationIssue("distribution-source", relative, "Metadata escapes the package root."))
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object")
        return data
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        issues.append(ValidationIssue("distribution-metadata", relative, f"Cannot read metadata ({type(exc).__name__})."))
        return None


def _check_source(root: Path, relative: str, source, issues: list[ValidationIssue]) -> None:
    try:
        if not isinstance(source, str) or not source or Path(source).is_absolute():
            raise ValueError("Expected a relative source")
        resolved = (root / source).resolve()
        if resolved != root or not resolved.is_dir():
            raise ValueError("Source must resolve to the repository-root plugin")
    except (OSError, RuntimeError, ValueError):
        issues.append(ValidationIssue("distribution-source", relative, "Source must resolve to this package root."))


def _check_marketplace(root: Path, relative: str, codex: bool, issues: list[ValidationIssue]) -> None:
    value = _read_object(root, relative, issues)
    if value is None:
        return
    head = {"name": _NAME, "interface": {"displayName": "Devcraft Toolkit"}} if codex else {
        "name": _NAME, "owner": _AUTHOR,
    }
    expected = {**head, "plugins": value.get("plugins")}
    entries = value.get("plugins")
    if value != expected or not isinstance(entries, list) or len(entries) != 1:
        issues.append(ValidationIssue("distribution-metadata", relative, "Expected one named plugin and the declared marketplace shape."))
        return
    entry = entries[0]
    if not isinstance(entry, dict):
        issues.append(ValidationIssue("distribution-metadata", relative, "Plugin entries must be objects."))
        return
    if codex:
        expected_entry = {
            "name": _NAME,
            "source": entry.get("source"),
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Productivity",
        }
        source = entry.get("source")
        if not isinstance(source, dict) or set(source) != {"source", "path"} or source.get("source") != "local":
            issues.append(ValidationIssue("distribution-source", relative, "Expected a local source with a relative path."))
            return
        path = source["path"]
    else:
        expected_entry = {"name": _NAME, "source": entry.get("source"), "description": _DESCRIPTION}
        path = entry.get("source")
    if entry != expected_entry:
        issues.append(ValidationIssue("distribution-metadata", relative, "Unexpected plugin identity, policy, or component override."))
    _check_source(root, relative, path, issues)


def validate_distribution(root: Path) -> list[ValidationIssue]:
    """Return finite local packaging-contract issues; never install or fetch."""
    root = Path(root).resolve()
    issues: list[ValidationIssue] = []
    manifests = {}
    for relative, portable in (("plugin.json", True), (".claude-plugin/plugin.json", False)):
        value = _read_object(root, relative, issues)
        if value is None:
            continue
        manifests[relative] = value
        identity = {"name": _NAME, "description": _DESCRIPTION, "author": _AUTHOR}
        expected = {**identity, "version": value.get("version")}
        if portable:
            expected["$schema"] = _SCHEMA
            expected["keywords"] = value.get("keywords")
            keywords = value.get("keywords")
            if (not isinstance(keywords, list) or not keywords
                    or any(not isinstance(item, str) or not item.strip() for item in keywords)):
                issues.append(ValidationIssue(
                    "distribution-keywords", relative,
                    "Expected a non-empty array of non-empty activation keyword strings."))
        if value != expected:
            issues.append(ValidationIssue("distribution-metadata", relative, "Manifest identity, schema, or fields differ from the package contract."))
        version = value.get("version")
        if not isinstance(version, str) or not _VERSION.fullmatch(version):
            issues.append(ValidationIssue("distribution-version", relative, "Expected a semantic version without a tag prefix."))
    if len(manifests) == 2 and manifests["plugin.json"].get("version") != manifests[".claude-plugin/plugin.json"].get("version"):
        issues.append(ValidationIssue("distribution-version", ".claude-plugin/plugin.json", "Manifest versions must agree."))

    _check_marketplace(root, ".agents/plugins/marketplace.json", True, issues)
    _check_marketplace(root, ".claude-plugin/marketplace.json", False, issues)

    for issue in validate_repository(root):
        issues.append(ValidationIssue("distribution-inventory", issue.path, f"{issue.code}: {issue.message}"))

    # Developer fixtures and ignored build/worktree areas are not package components.
    excluded = {".git", ".worktrees", "worktrees", ".superpowers", ".venv", "dist", "tests", "__pycache__", "node_modules"}
    try:
        for current, directories, files in os.walk(root, followlinks=False):
            directories[:] = [name for name in directories if name not in excluded]
            directory = Path(current)
            if "SKILL.md" in files and not directory.is_relative_to(root / "skills"):
                issues.append(ValidationIssue("distribution-inventory", (directory / "SKILL.md").relative_to(root).as_posix(), "Skill copies outside the canonical skills tree are not package components."))
    except OSError as exc:
        issues.append(ValidationIssue("distribution-inventory", "skills", f"Cannot inspect package inventory ({type(exc).__name__})."))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="Package repository root")
    args = parser.parse_args(argv)
    issues = validate_distribution(args.root)
    for issue in issues:
        print(f"{issue.code}: {issue.path}: {issue.message}")
    if not issues:
        print("Distribution contract is valid (native loading is not verified).")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
