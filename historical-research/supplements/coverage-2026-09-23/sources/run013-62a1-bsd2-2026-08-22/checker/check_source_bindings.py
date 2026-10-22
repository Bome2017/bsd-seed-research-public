#!/usr/bin/env python3
"""Strict SHA-256 replay for Run013 inherited source bindings."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


EXPECTED_HEADER = ("sha256", "path", "role")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "bindings",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "evidence" / "SOURCE_BINDINGS.tsv",
    )
    args = parser.parse_args()

    try:
        lines = args.bindings.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"source_bindings": "FAIL", "error": str(exc)}, sort_keys=True))
        return 2
    if not lines or tuple(lines[0].split("\t")) != EXPECTED_HEADER:
        print(json.dumps({"source_bindings": "FAIL", "error": "wrong TSV header"}, sort_keys=True))
        return 2

    seen_paths: set[str] = set()
    failures: list[dict[str, str]] = []
    count = 0
    for line_number, line in enumerate(lines[1:], start=2):
        fields = line.split("\t")
        if len(fields) != 3:
            failures.append({"line": str(line_number), "error": "expected exactly three fields"})
            continue
        expected, path_text, role = fields
        count += 1
        if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
            failures.append({"line": str(line_number), "path": path_text, "error": "invalid SHA-256"})
            continue
        if path_text in seen_paths:
            failures.append({"line": str(line_number), "path": path_text, "error": "duplicate path"})
            continue
        seen_paths.add(path_text)
        path = Path(path_text)
        if not path.is_absolute():
            failures.append({"line": str(line_number), "path": path_text, "error": "path is not absolute"})
            continue
        if not role:
            failures.append({"line": str(line_number), "path": path_text, "error": "empty role"})
            continue
        if not path.is_file():
            failures.append({"line": str(line_number), "path": path_text, "error": "missing file"})
            continue
        actual = sha256(path)
        if actual != expected:
            failures.append(
                {
                    "line": str(line_number),
                    "path": path_text,
                    "error": "digest mismatch",
                    "expected": expected,
                    "actual": actual,
                }
            )

    report = {
        "source_bindings": "FAIL" if failures else "PASS",
        "bindings": count,
        "mismatches": len(failures),
        "failures": failures,
    }
    print(json.dumps(report, sort_keys=True))
    return 2 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
