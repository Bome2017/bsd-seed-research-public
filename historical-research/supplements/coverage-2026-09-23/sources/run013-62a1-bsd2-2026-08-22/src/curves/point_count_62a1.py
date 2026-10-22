#!/usr/bin/env python3
"""Exact finite-field point count for the 62a1 minimal model.

The script is deliberately dependency-free.  It counts solutions of

    y^2 + x*y + y = x^3 - x^2 - x + 1

over F_p and adds the point at infinity.  It is a finite witness generator,
not a proof of the Chebotarev step.
"""

from __future__ import annotations

import argparse


def count_points(prime: int) -> tuple[int, list[tuple[int, int]]]:
    if prime < 2:
        raise ValueError("prime must be at least 2")
    affine: list[tuple[int, int]] = []
    for x in range(prime):
        rhs = (x**3 - x**2 - x + 1) % prime
        for y in range(prime):
            lhs = (y**2 + x * y + y) % prime
            if lhs == rhs:
                affine.append((x, y))
    return len(affine) + 1, affine


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prime", type=int, nargs="?", default=13)
    args = parser.parse_args()
    count, affine = count_points(args.prime)
    trace = args.prime + 1 - count
    print(f"p={args.prime}")
    print(f"affine_count={len(affine)}")
    print(f"projective_count={count}")
    print(f"a_p={trace}")
    print("affine_points=" + ",".join(f"({x},{y})" for x, y in affine))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

