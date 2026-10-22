#!/usr/bin/env python3
"""
Forbidden-construct scanner for this project, WITH A MANDATORY INJECTED POSITIVE CONTROL.

Usage:   python3 verify/scan_constructs.py            (run from the project root)

What it does.

1.  It writes a temporary positive-control file OUTSIDE the project tree, in a fresh
    temporary directory.  That file genuinely declares `axiom controlFalse : False`
    and genuinely contains `sorry`, `admit`, `native_decide`, `unsafe`,
    `@[implemented_by ...]` and `@[extern ...]` in code position.
2.  It scans every `.lean` file of the project *plus* the control file, after stripping
    Lean comments (`--` to end of line, and nested `/- ... -/`), so that documentation
    prose is not confused with code.
3.  It prints the hits per file and then asserts the control was detected.  If the
    control is NOT detected the scan aborts with FAIL: a scanner that cannot see a
    genuine `axiom` is not evidence of anything.
4.  The control file is deleted afterwards, so no prohibited construct is left in the
    delivered tree.

The scanner also reports the RAW (comment-included) matches separately, because
`RequestProject/GateR/Assembly.lean` contains the word `sorry` twice inside its frozen
opening doc comment.  Those are documentation text in frozen bytes, not code.
"""

from __future__ import annotations

import os
import re
import sys
import tempfile

TOKENS = {
    "sorry":           r"\bsorry\b",
    "admit":           r"\badmit\b",
    "axiom":           r"(?m)^\s*axiom\b",
    "native_decide":   r"\bnative_decide\b",
    "ofReduceBool":    r"\bofReduceBool\b",
    "trustCompiler":   r"\btrustCompiler\b",
    "implemented_by":  r"implemented_by",
    "unsafe":          r"(?m)^\s*unsafe\b",
    "extern":          r"@\[\s*extern",
}

CONTROL = r'''
/- POSITIVE CONTROL for the construct scanner.  This file is deliberately dirty. -/
axiom controlFalse : False

theorem controlThm : True := by sorry

theorem controlThm2 : True := by admit

example : 2 + 2 = 4 := by native_decide

unsafe def controlUnsafe : Nat := 0

@[implemented_by controlUnsafe] def controlImpl : Nat := 0

@[extern "c_control"] opaque controlExtern : Nat

example := @Lean.ofReduceBool

example := @Lean.trustCompiler
'''


def strip_comments(src: str) -> str:
    """Remove Lean line comments and (nested) block comments."""
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if depth == 0 and src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j == -1 else j
        elif src.startswith("/-", i):
            depth += 1
            i += 2
        elif depth > 0 and src.startswith("-/", i):
            depth -= 1
            i += 2
        else:
            if depth == 0:
                out.append(src[i])
            i += 1
    return "".join(out)


def scan(path: str) -> tuple[dict[str, int], dict[str, int]]:
    src = open(path, encoding="utf-8").read()
    code = strip_comments(src)
    raw_hits = {k: len(re.findall(p, src)) for k, p in TOKENS.items()}
    code_hits = {k: len(re.findall(p, code)) for k, p in TOKENS.items()}
    return ({k: v for k, v in raw_hits.items() if v},
            {k: v for k, v in code_hits.items() if v})


def main() -> int:
    root = os.getcwd()
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".lake", ".git"}]
        for f in sorted(filenames):
            if f.endswith(".lean"):
                files.append(os.path.join(dirpath, f))
    files.sort()

    tmpdir = tempfile.mkdtemp(prefix="scan_control_")
    control = os.path.join(tmpdir, "POSITIVE_CONTROL.lean")
    with open(control, "w", encoding="utf-8") as fh:
        fh.write(CONTROL)

    print("=== forbidden-construct scan ===")
    print(f"project root      : {root}")
    print(f"lean files scanned: {len(files)} (+1 injected positive control)")
    print(f"injected control  : {control}\n")

    dirty_code = []
    for path in files + [control]:
        raw, code = scan(path)
        if raw or code:
            rel = os.path.relpath(path, root)
            print(f"{rel}")
            print(f"    raw (comments included): {raw if raw else '{}'}")
            print(f"    code (comments stripped): {code if code else '{}'}")
            if code:
                dirty_code.append(rel)

    _, control_code = scan(control)
    print("\n--- positive control check ---")
    print(f"control code hits: {control_code}")
    ok = all(t in control_code for t in TOKENS)
    if not ok:
        print("FAIL: the scanner did not detect every construct in the positive control.")
        os.remove(control)
        os.rmdir(tmpdir)
        return 1
    print("PASS: the scanner detects a genuine `axiom`/`sorry`/`admit`/`native_decide`/"
          "`unsafe`/`implemented_by`/`extern` file.")

    os.remove(control)
    os.rmdir(tmpdir)

    project_dirty = [f for f in dirty_code if "POSITIVE_CONTROL" not in f]
    print("\n--- project verdict ---")
    if project_dirty:
        print(f"files with forbidden constructs in CODE position: {project_dirty}")
        return 1
    print("no forbidden construct in code position in any project .lean file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
