#!/usr/bin/env python3
"""Evaluate a conditional, finite-precision BSD content criterion.

This program checks valuation arithmetic only. It does NOT authenticate a Kato
class, a Bockstein map, a point basis, or an elliptic-curve cohomology complex.
Consequently it never reports an actual seed primary component as certified.
Standard library only; Python 3.10+.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

BAD_REDUCTION = {2, 3, 2243, 4547, 5843}
EXTRA_EXCLUSIONS = {19, 59, 487}


def checked_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label} must be an integer, not a boolean or float")
    return value


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    return all(p % d for d in range(3, math.isqrt(p) + 1, 2))


def truncated_valuation(residue: int, p: int, precision: int) -> int:
    """Zero mod p^precision gives a LOWER bound, never infinite valuation."""
    if residue == 0:
        return precision
    v = 0
    while residue % p == 0:
        residue //= p
        v += 1
    return v


def read_row(data: Any, p: int, label: str) -> dict[str, Any]:
    if not isinstance(data, dict) or set(data) != {"precision", "residues"}:
        raise ValueError(f"{label} must contain exactly precision and residues")
    n = checked_int(data["precision"], f"{label}.precision")
    if not 1 <= n <= 128:
        raise ValueError(f"{label}.precision must be between 1 and 128")
    residues = data["residues"]
    if not isinstance(residues, list) or len(residues) != 2:
        raise ValueError(f"{label}.residues must be a list of two integers")
    modulus = p**n
    checked = []
    for i, x in enumerate(residues):
        x = checked_int(x, f"{label}.residues[{i}]")
        if not 0 <= x < modulus:
            raise ValueError(f"{label} residues must be canonical modulo p^precision")
        checked.append(x)
    lower = min(truncated_valuation(x, p, n) for x in checked)
    return {"precision": n, "content_lower_bound": lower,
            "content_is_exact": lower < n,
            "nonzero_detected": any(checked)}


def evaluate(packet: Any) -> dict[str, Any]:
    if not isinstance(packet, dict):
        raise ValueError("The packet must be a JSON object")
    required = {"case_id", "kind", "p", "delta", "bockstein", "local_log"}
    optional = {"source_notes"}
    if not required <= set(packet) or set(packet) - required - optional:
        raise ValueError("Unexpected or missing packet fields")
    if not isinstance(packet["case_id"], str):
        raise ValueError("case_id must be a string")
    if packet["kind"] not in {"abstract_control", "candidate_seed_input"}:
        raise ValueError("kind must be abstract_control or candidate_seed_input")
    p = checked_int(packet["p"], "p")
    # This cap concerns this small verifier, not the mathematical theorem.
    if not 5 <= p <= 2**31 - 1 or not is_prime(p):
        raise ValueError("p must be a prime in [5, 2^31-1]")
    out: dict[str, Any] = {
        "case_id": packet["case_id"], "kind": packet["kind"], "p": p,
        "source_authentication": "NOT_PERFORMED",
        "actual_seed_primary_vanishing_certified": False,
        "arithmetic_grade": "VALUATION_CHECK_ONLY",
    }
    if p in BAD_REDUCTION | EXTRA_EXCLUSIONS:
        out["status"] = "OUTSIDE_RETAINED_PRIME_DOMAIN"
        return out
    delta = read_row(packet["delta"], p, "delta")
    beta = read_row(packet["bockstein"], p, "bockstein")
    logs = read_row(packet["local_log"], p, "local_log")
    out.update({"delta_observation": delta, "bockstein_observation": beta,
                "local_log_observation": logs})
    if not delta["nonzero_detected"]:
        out["status"] = "INCONCLUSIVE_DERIVATIVE_PRECISION"
        out["note"] = "Zero residues do not prove that the actual derivative is zero."
        return out
    m = delta["content_lower_bound"]  # exact: at least one residue is nonzero
    b_lower = beta["content_lower_bound"]
    w_lower = logs["content_lower_bound"]
    upper = m - b_lower - w_lower
    out.update({"derivative_content_exact": m,
                "bockstein_content_lower_bound": b_lower,
                "local_index_lower_bound": w_lower,
                "corrected_length_upper_bound_conditional": upper,
                "old_length_upper_bound_conditional": m - w_lower})
    if upper < 0:
        out["status"] = "REJECT_INCONSISTENT_VALUATION_INPUTS"
        out["note"] = "These bounds cannot all describe the matched objects under the theorem's hypotheses."
        return out
    out["even_length_upper_bound_conditional"] = 2 * (upper // 2)
    out["old_criterion_met"] = m - w_lower <= 1
    out["corrected_criterion_met"] = upper <= 1
    out["status"] = ("CONDITIONAL_VANISHING_CRITERION_MET" if upper <= 1
                     else "CONDITIONAL_CONTENT_BOUND_ONLY")
    out["note"] = (
        "A seed conclusion additionally needs the actual transported Kato class, "
        "the all-height-one integral inequality, saturated point basis, primitive "
        "H^2_tf Bockstein normalization, and the retained arithmetic identifications. "
        "A source_notes field is not authentication."
    )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="JSON residue packet")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        with args.packet.open(encoding="utf-8") as stream:
            result = evaluate(json.load(stream))
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Input rejected: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
