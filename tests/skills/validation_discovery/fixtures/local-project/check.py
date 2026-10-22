"""Test-only command fixture for validation-discovery scenarios."""

from __future__ import annotations

import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    mode = args[0] if args else ""

    if mode == "pass":
        print("check ok")
        return 0
    if mode == "fail":
        print("check failed", file=sys.stderr)
        return 3
    if mode == "unexpected-write":
        Path.cwd().joinpath("unexpected.txt").write_text("unexpected output\n", encoding="utf-8")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
