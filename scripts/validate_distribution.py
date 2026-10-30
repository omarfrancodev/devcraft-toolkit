"""Validate the toolkit's local distribution contract without installing it."""

from __future__ import annotations

import argparse
import json
import os
import re
import struct
import zlib
from pathlib import Path, PurePosixPath

from scripts.validate_repository import ValidationIssue, validate_repository, yaml

_NAME = "devcraft-toolkit"
_DESCRIPTION = "Composable Git and development skills for coding agents."
_AUTHOR = {"name": "omarfrancodev"}
_CATEGORY = "Developer Tools"
_PROJECT_URL = "https://github.com/omarfrancodev/devcraft-toolkit"
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


def _check_icon(root: Path, field: str, relative, issues: list[ValidationIssue],
                manifest: str = "plugin.json") -> None:
    """Check the package's square PNG icon contract, without fetching or rendering."""
    try:
        if (not isinstance(relative, str) or not relative.startswith("./assets/")
                or "\\" in relative or ".." in PurePosixPath(relative).parts
                or PurePosixPath(relative).suffix != ".png"):
            raise ValueError("Expected a ./assets/ PNG path")
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_relative_to(root / "assets"):
            raise ValueError("Icon escapes packaged assets")
        if not path.is_file() or path.stat().st_size > 5 * 1024 * 1024:
            raise ValueError("Expected a PNG file no larger than 5 MiB")
        data = path.read_bytes()
        if len(data) > 5 * 1024 * 1024 or not data.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError("Expected PNG bytes")
        offset, image_data, ended = 8, False, False
        while offset < len(data):
            if offset + 12 > len(data):
                raise ValueError("Truncated PNG chunk")
            size = struct.unpack_from(">I", data, offset)[0]
            end = offset + 12 + size
            if end > len(data):
                raise ValueError("Truncated PNG chunk data")
            kind = data[offset + 4:offset + 8]
            payload = data[offset + 8:end - 4]
            crc = struct.unpack_from(">I", data, end - 4)[0]
            if zlib.crc32(kind + payload) != crc:
                raise ValueError("Invalid PNG chunk checksum")
            if offset == 8:
                if kind != b"IHDR" or size != 13:
                    raise ValueError("Expected PNG image header")
                width, height = struct.unpack_from(">II", payload)
                if not 48 <= width == height <= 4096:
                    raise ValueError("Expected a square icon from 48 to 4096 pixels")
            elif kind == b"IHDR":
                raise ValueError("Duplicate PNG image header")
            if kind == b"IDAT" and payload:
                image_data = True
            if kind == b"IEND":
                if size != 0 or end != len(data) or not image_data:
                    raise ValueError("Invalid PNG image ending")
                ended = True
            offset = end
        if not ended:
            raise ValueError("Missing PNG image ending")
    except (OSError, RuntimeError, ValueError) as exc:
        issues.append(ValidationIssue(
            "distribution-asset", manifest,
            f"{field}: expected a packaged square PNG with intact chunks ({type(exc).__name__})."))


def _check_interface(root: Path, extensions, issues: list[ValidationIssue]) -> None:
    """Keep OpenAI presentation separate from portable identity and components."""
    openai = extensions.get("com.openai") if isinstance(extensions, dict) else None
    interface = openai.get("interface") if isinstance(openai, dict) else None
    if not isinstance(interface, dict):
        issues.append(ValidationIssue(
            "distribution-interface", "plugin.json", "Expected extensions.com.openai.interface."))
        return
    expected = {
        "displayName": "Devcraft Toolkit",
        "shortDescription": "Composable Git tools",
        "longDescription": _DESCRIPTION,
        "developerName": _AUTHOR["name"],
        "category": _CATEGORY,
        "websiteURL": _PROJECT_URL,
        "logo": interface.get("logo"),
        "composerIcon": interface.get("composerIcon"),
    }
    if extensions != {"com.openai": {"interface": expected}}:
        issues.append(ValidationIssue(
            "distribution-interface", "plugin.json",
            "Unexpected listing identity, category, fields, or component override."))
    for field in ("logo", "composerIcon"):
        _check_icon(root, field, interface.get(field), issues)


def _check_marketplace(root: Path, relative: str, codex: bool, issues: list[ValidationIssue]) -> None:
    value = _read_object(root, relative, issues)
    if value is None:
        return
    head = {"name": _NAME, "interface": {"displayName": "Devcraft Toolkit"}} if codex else {
        "name": _NAME, "owner": _AUTHOR, "metadata": {"description": _DESCRIPTION},
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
            "category": _CATEGORY,
        }
        source = entry.get("source")
        if not isinstance(source, dict) or set(source) != {"source", "path"} or source.get("source") != "local":
            issues.append(ValidationIssue("distribution-source", relative, "Expected a local source with a relative path."))
            return
        path = source["path"]
    else:
        expected_entry = {
            "name": _NAME, "source": entry.get("source"), "description": _DESCRIPTION,
            "category": _CATEGORY, "tags": ["git", "commit", "report", "validation"],
        }
        path = entry.get("source")
    if entry != expected_entry:
        issues.append(ValidationIssue("distribution-metadata", relative, "Unexpected plugin identity, policy, or component override."))
    _check_source(root, relative, path, issues)


def _check_skill_interfaces(root: Path, issues: list[ValidationIssue]) -> None:
    """Require presentation-only Codex metadata for each available capability."""
    if yaml is None:  # Repository validation already reports the missing parser.
        return
    catalog = _read_object(root, "catalog.json", issues)
    if catalog is None or not isinstance(catalog.get("skills"), list):
        return
    seen_names: set[str] = set()
    for entry in catalog["skills"]:
        if not isinstance(entry, dict) or entry.get("status") != "available":
            continue
        name = entry.get("name")
        if (not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                or entry.get("path") != f"skills/{name}"):
            continue  # Invalid identities/paths are reported by repository validation.
        relative = f"skills/{name}/agents/openai.yaml"
        try:
            skill_root = (root / entry["path"]).resolve()
            path = root / relative
            if not skill_root.is_relative_to(root) or not path.resolve().is_relative_to(skill_root):
                raise ValueError("Presentation metadata escapes its skill")
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            interface = value.get("interface") if isinstance(value, dict) else None
            if (not isinstance(value, dict) or set(value) != {"interface"}
                    or not isinstance(interface, dict)
                    or set(interface) != {"display_name", "short_description"}):
                raise ValueError("Expected only display_name and short_description under interface")
            label = interface["display_name"]
            blurb = interface["short_description"]
            if (not isinstance(label, str) or not 1 <= len(label) <= 64
                    or label != label.strip() or not label.isprintable()
                    or any(character in label for character in ":/\\")):
                raise ValueError("Expected a short single-line name without a namespace prefix")
            if (not isinstance(blurb, str) or not 25 <= len(blurb) <= 64
                    or blurb != blurb.strip() or not blurb.isprintable()):
                raise ValueError("Expected a single-line description of 25-64 characters")
            key = label.casefold()
            if key in seen_names:
                raise ValueError("Skill display names must be unique")
            seen_names.add(key)
        except (OSError, UnicodeError, ValueError, yaml.YAMLError, RecursionError) as exc:
            issues.append(ValidationIssue(
                "distribution-skill-interface", relative,
                f"Expected readable, unique presentation-only skill metadata ({type(exc).__name__})."))


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
        identity = {"name": _NAME, "description": _DESCRIPTION, "author": _AUTHOR,
                    "homepage": _PROJECT_URL, "repository": _PROJECT_URL}
        expected = {**identity, "version": value.get("version"), "keywords": value.get("keywords")}
        keywords = value.get("keywords")
        if (not isinstance(keywords, list) or not keywords
                or any(not isinstance(item, str) or not item.strip() for item in keywords)):
            issues.append(ValidationIssue(
                "distribution-keywords", relative,
                "Expected a non-empty array of non-empty keyword strings."))
        if portable:
            expected["$schema"] = _SCHEMA
            expected["extensions"] = value.get("extensions")
            _check_interface(root, value.get("extensions"), issues)
        else:
            expected["displayName"] = "Devcraft Toolkit"
            expected["icon"] = value.get("icon")
            _check_icon(root, "icon", value.get("icon"), issues, manifest=relative)
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
    _check_skill_interfaces(root, issues)

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
