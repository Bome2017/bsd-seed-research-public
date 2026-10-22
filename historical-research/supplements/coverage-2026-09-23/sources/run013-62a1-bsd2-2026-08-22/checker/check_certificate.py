#!/usr/bin/env python3
"""Fail-closed checker for the Run013 62a1 finite replay certificate.

This program deliberately distinguishes exact finite replay from a proof of
the uniform Selmer theorem.  Protocol v1 can certify the former.  It refuses
the latter while any symbolic obligation is open or any required local row
lacks a checker-implemented rule.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple


PROTOCOL = "run013.62a1.finite-local-replay.v1"
SCOPE = "finite-replay-only"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
TARGET_RELATIVE_PATH = "../TARGET.md"

CLASS_IDS = tuple(f"{n:04b}" for n in range(16))
PHI_TARGET = ("0000", "0001", "1010", "1011")
DUAL_TARGET = ("0000",)
PLACES = ("infinity", "2", "31", "q", "outside_S")

OBLIGATION_IDS = (
    "SUPPORT_RESTRICTION",
    "KUMMER_LOWER_BOUND_PHI",
    "KUMMER_LOWER_BOUND_DUAL",
    "LOCAL_2_UNIFORM",
    "LOCAL_31_UNIFORM",
    "LOCAL_Q_UNIFORM",
    "UNRAMIFIED_OUTSIDE_S",
)

TOP_KEYS = {
    "protocol",
    "scope",
    "target_binding",
    "curve",
    "family_signature",
    "family_witness",
    "ambient",
    "claimed_selmer",
    "finite_checks",
    "local_replay",
    "symbolic_obligations",
}


class CertificateError(ValueError):
    """Raised when a certificate is malformed, stale, or mathematically false."""


def _reject_duplicate_keys(pairs: Sequence[Tuple[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CertificateError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(
                handle,
                object_pairs_hook=_reject_duplicate_keys,
                parse_constant=lambda token: (_ for _ in ()).throw(
                    CertificateError(f"non-finite JSON number: {token}")
                ),
            )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot parse certificate: {exc}") from exc
    _reject_floats(value, "$")
    return value


def _reject_floats(value: Any, where: str) -> None:
    if isinstance(value, float):
        raise CertificateError(f"floating-point value forbidden at {where}")
    if isinstance(value, list):
        for index, child in enumerate(value):
            _reject_floats(child, f"{where}[{index}]")
    elif isinstance(value, dict):
        for key, child in value.items():
            _reject_floats(child, f"{where}.{key}")


def _expect_dict(value: Any, where: str, keys: Iterable[str]) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise CertificateError(f"{where} must be an object")
    expected = set(keys)
    actual = set(value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        raise CertificateError(f"{where} keys mismatch; missing={missing}, extra={extra}")
    return value


def _expect_int(value: Any, where: str) -> int:
    if type(value) is not int:
        raise CertificateError(f"{where} must be an integer")
    return value


def _expect_bool(value: Any, where: str) -> bool:
    if type(value) is not bool:
        raise CertificateError(f"{where} must be a boolean")
    return value


def _expect_str(value: Any, where: str) -> str:
    if not isinstance(value, str):
        raise CertificateError(f"{where} must be a string")
    return value


def _expect_string_list(value: Any, where: str) -> List[str]:
    if not isinstance(value, list):
        raise CertificateError(f"{where} must be an array")
    result = []
    for index, item in enumerate(value):
        result.append(_expect_str(item, f"{where}[{index}]"))
    if len(result) != len(set(result)):
        raise CertificateError(f"{where} contains duplicates")
    return result


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_digest(text: Any, where: str) -> str:
    value = _expect_str(text, where)
    if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise CertificateError(f"{where} must be a lowercase SHA-256 digest")
    return value


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    factor = 3
    while factor <= limit:
        if n % factor == 0:
            return False
        factor += 2
    return True


def _legendre(a: int, p: int) -> int:
    if not _is_prime(p) or p == 2:
        raise CertificateError("Legendre denominator must be an odd prime")
    residue = a % p
    if residue == 0:
        return 0
    value = pow(residue, (p - 1) // 2, p)
    if value == 1:
        return 1
    if value == p - 1:
        return -1
    raise CertificateError("Euler criterion returned an impossible value")


def _v2(n: int) -> int:
    if n == 0:
        raise CertificateError("v2(0) is not finite")
    n = abs(n)
    value = 0
    while n % 2 == 0:
        n //= 2
        value += 1
    return value


def _point_count_62a1(q: int) -> int:
    """Count y^2=x^3-15x^2+64x over F_q, including infinity."""
    total = 1
    for x in range(q):
        rhs = (x * x * x - 15 * x * x + 64 * x) % q
        total += 1 + _legendre(rhs, q)
    return total


def _xor(a: str, b: str) -> str:
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))


def _check_subgroup(classes: Sequence[str], where: str) -> None:
    values = set(classes)
    if "0000" not in values:
        raise CertificateError(f"{where} omits the identity")
    for left in values:
        for right in values:
            if _xor(left, right) not in values:
                raise CertificateError(f"{where} is not closed under squareclass multiplication")


def _class_integer(class_id: str, q: int) -> int:
    if class_id not in CLASS_IDS:
        raise CertificateError(f"invalid squareclass id: {class_id!r}")
    sign, two, thirty_one, moving = (int(bit) for bit in class_id)
    value = -1 if sign else 1
    if two:
        value *= 2
    if thirty_one:
        value *= 31
    if moving:
        value *= q
    return value


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _quartic_bytes(q: int) -> bytes:
    lines: List[str] = []
    for descent, middle, constant in (
        ("phi", 30 * q, -31 * q * q),
        ("dual_phi", -15 * q, 64 * q * q),
    ):
        for class_id in CLASS_IDS:
            d = _class_integer(class_id, q)
            coefficients = (Fraction(d), Fraction(middle), Fraction(constant, d))
            lines.append(
                "|".join(
                    [descent, class_id, str(d)]
                    + [_fraction_text(coefficient) for coefficient in coefficients]
                )
            )
    return ("\n".join(lines) + "\n").encode("ascii")


def _quartic_digest(q: int) -> str:
    return hashlib.sha256(_quartic_bytes(q)).hexdigest()


# A tiny exact Laurent-polynomial ring in q and x.  Exponents may be negative
# in x because the isogeny formulas contain x^{-1}.
Poly = Dict[Tuple[int, int], Fraction]


def _poly_clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def _poly_add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return _poly_clean(result)


def _poly_neg(poly: Poly) -> Poly:
    return {monomial: -coefficient for monomial, coefficient in poly.items()}


def _poly_sub(left: Poly, right: Poly) -> Poly:
    return _poly_add(left, _poly_neg(right))


def _poly_mul(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (lq, lx), lc in left.items():
        for (rq, rx), rc in right.items():
            monomial = (lq + rq, lx + rx)
            result[monomial] = result.get(monomial, Fraction(0)) + lc * rc
    return _poly_clean(result)


def _poly_pow(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        raise CertificateError("negative polynomial power")
    result: Poly = {(0, 0): Fraction(1)}
    base = poly
    power = exponent
    while power:
        if power & 1:
            result = _poly_mul(result, base)
        base = _poly_mul(base, base)
        power >>= 1
    return result


def _monomial(coefficient: int | Fraction, q_exp: int, x_exp: int) -> Poly:
    return {(q_exp, x_exp): Fraction(coefficient)} if coefficient else {}


def _verify_isogeny_identity(
    source_a: Poly,
    source_b: Poly,
    target_a: Poly,
    target_b: Poly,
    x_scale: Fraction,
    y_scale: Fraction,
) -> None:
    x = _monomial(1, 0, 1)
    x_inverse = _monomial(1, 0, -1)
    y_squared = _poly_add(_poly_add(_poly_pow(x, 3), _poly_mul(source_a, _poly_pow(x, 2))), _poly_mul(source_b, x))
    raw_x_image = _poly_add(_poly_add(x, source_a), _poly_mul(source_b, x_inverse))
    x_image = {m: x_scale * c for m, c in raw_x_image.items()}
    b_minus_x2 = _poly_sub(source_b, _poly_pow(x, 2))
    raw_y_image_squared = _poly_mul(y_squared, _poly_mul(b_minus_x2, b_minus_x2))
    raw_y_image_squared = _poly_mul(raw_y_image_squared, _monomial(1, 0, -4))
    y_image_squared = {m: y_scale * y_scale * c for m, c in raw_y_image_squared.items()}
    target_rhs = _poly_add(
        _poly_add(_poly_pow(x_image, 3), _poly_mul(target_a, _poly_pow(x_image, 2))),
        _poly_mul(target_b, x_image),
    )
    if _poly_clean(_poly_sub(y_image_squared, target_rhs)):
        raise CertificateError("isogeny formula does not satisfy the target curve equation")


def _machine_curve_checks() -> None:
    # The change X=4(u+1), Y=8v+4u+4 gives both sides
    # 64u^3-48u^2-32u+80 after eliminating v^2.
    lhs = (64, -48, -32, 80)
    rhs = (
        64,
        3 * 64 - 15 * 16,
        3 * 64 - 2 * 15 * 16 + 64 * 4,
        64 - 15 * 16 + 64 * 4,
    )
    if lhs != rhs:
        raise CertificateError("minimal-to-descent model identity failed")

    q = _monomial(1, 1, 0)
    q2 = _monomial(1, 2, 0)
    a = {m: -15 * c for m, c in q.items()}
    b = {m: 64 * c for m, c in q2.items()}
    a_prime = {m: 30 * c for m, c in q.items()}
    b_prime = {m: -31 * c for m, c in q2.items()}

    _verify_isogeny_identity(a, b, a_prime, b_prime, Fraction(1), Fraction(1))
    _verify_isogeny_identity(a_prime, b_prime, a, b, Fraction(1, 4), Fraction(1, 8))
    _verify_composition_identity(a, b, b_prime)


def _verify_composition_identity(
    source_a: Poly,
    source_b: Poly,
    quotient_b: Poly,
    phi_y_sign: int = 1,
    dual_y_sign: int = 1,
) -> None:
    """Check the signed composition against the duplication law exactly.

    The separate curve-equation checks only see squares of the two
    y-coordinate formulas.  This identity retains their signs.  For

        y^2 = x(x^2 + a*x + b),

    the target formulas use ``y*(b-x^2)/x^2`` followed by
    ``Y*(B-X^2)/(8*X^2)``, where ``B=a^2-4b``.  Cross multiplication avoids
    division and proves that their composition is the signed duplication
    map in the rational-function field Q(q,x,y)/(y^2-x(x^2+a*x+b)).
    """
    if phi_y_sign not in (-1, 1) or dual_y_sign not in (-1, 1):
        raise CertificateError("isogeny y-coordinate sign must be +1 or -1")

    x = _monomial(1, 0, 1)
    x2 = _poly_pow(x, 2)
    two_x = {m: 2 * c for m, c in x.items()}
    f = _poly_add(_poly_add(x2, _poly_mul(source_a, x)), source_b)
    tangent_numerator = _poly_add(
        _poly_add({m: 3 * c for m, c in x2.items()}, {m: 2 * c for m, c in _poly_mul(source_a, x).items()}),
        source_b,
    )
    x2_minus_b = _poly_sub(x2, source_b)

    # x-coordinate: composition and tangent duplication both have
    # denominator 4*x*f.
    tangent_x_numerator = _poly_sub(
        _poly_pow(tangent_numerator, 2),
        {
            m: 4 * c
            for m, c in _poly_mul(_poly_mul(x, f), _poly_add(source_a, two_x)).items()
        },
    )
    composition_x_numerator = _poly_pow(x2_minus_b, 2)
    if _poly_clean(_poly_sub(tangent_x_numerator, composition_x_numerator)):
        raise CertificateError("isogeny composition x-coordinate is not duplication")

    # Divide both y-coordinate formulas by y.  After cross multiplication,
    # both have denominator 8*x^2*f^2.  The sign product is deliberately
    # retained, so negating either isogeny formula fails this check.
    signed_composition_y_numerator = _poly_mul(
        _poly_sub(source_b, x2),
        _poly_sub(_poly_mul(quotient_b, x2), _poly_pow(f, 2)),
    )
    sign_product = phi_y_sign * dual_y_sign
    signed_composition_y_numerator = {
        m: sign_product * c for m, c in signed_composition_y_numerator.items()
    }
    four_x2_f = {m: 4 * c for m, c in _poly_mul(x2, f).items()}
    duplication_y_numerator = _poly_add(
        {m: -8 * c for m, c in _poly_mul(x2, _poly_pow(f, 2)).items()},
        _poly_mul(
            tangent_numerator,
            _poly_sub(four_x2_f, _poly_pow(x2_minus_b, 2)),
        ),
    )
    if _poly_clean(_poly_sub(signed_composition_y_numerator, duplication_y_numerator)):
        raise CertificateError("signed isogeny composition y-coordinate is not duplication")


def _real_has_point(a: Fraction, b: Fraction, c: Fraction) -> bool:
    """Whether a*z^2+b*z+c is nonnegative for some real z>=0."""
    if c >= 0:
        return True
    if a > 0:
        return True
    if a == 0:
        return b > 0
    # Concave parabola.  Its vertex must lie in z>0 and have value >=0.
    if b <= 0:
        return False
    vertex_numerator = 4 * a * c - b * b
    # At z=-b/(2a), value=(4ac-b^2)/(4a); denominator is negative.
    return vertex_numerator <= 0


def _real_acceptance(q: int, descent: str) -> Tuple[str, ...]:
    if descent == "phi":
        middle = Fraction(30 * q)
        constant = -31 * q * q
    elif descent == "dual_phi":
        middle = Fraction(-15 * q)
        constant = 64 * q * q
    else:
        raise CertificateError(f"unknown descent: {descent}")
    accepted = []
    for class_id in CLASS_IDS:
        d = _class_integer(class_id, q)
        if _real_has_point(Fraction(d), middle, Fraction(constant, d)):
            accepted.append(class_id)
    return tuple(accepted)


def _signature_local_acceptance(place: str, descent: str) -> Tuple[str, ...]:
    """Replay the proved-to-be-needed F_2 predicates, not their local proof.

    Bits are (s,e,f,g) for (-1)^s 2^e 31^f q^g.  These predicates are the
    finite interface exported by the local lemmas.  Checking the predicates
    and their intersection is not a proof that the predicates equal the local
    Kummer images; those statements remain explicit symbolic obligations.
    """
    accepted: List[str] = []
    for class_id in CLASS_IDS:
        s, e, f, g = (int(bit) for bit in class_id)
        if descent == "phi":
            predicate = {
                "2": e == 0 and s == f,
                "31": True,
                "q": True,
                "outside_S": True,
            }.get(place)
        elif descent == "dual_phi":
            predicate = {
                "2": e == 0,
                "31": f == 0 and s == g,
                "q": g == 0 and e == f,
                "outside_S": True,
            }.get(place)
        else:
            raise CertificateError(f"unknown descent: {descent}")
        if predicate is None:
            raise CertificateError(f"no signature rule for place {place}")
        if predicate:
            accepted.append(class_id)
    return tuple(accepted)


def _check_target_binding(value: Any, certificate_path: Path) -> str:
    binding = _expect_dict(value, "$.target_binding", {"path", "sha256"})
    relative = _expect_str(binding["path"], "$.target_binding.path")
    if relative != TARGET_RELATIVE_PATH:
        raise CertificateError("target binding path must be exactly ../TARGET.md")
    expected = _validate_digest(binding["sha256"], "$.target_binding.sha256")
    resolved = (certificate_path.parent / relative).resolve()
    required = (PROJECT_ROOT / "TARGET.md").resolve()
    if resolved != required:
        raise CertificateError("target binding resolves outside the Run013 project")
    if not resolved.is_file():
        raise CertificateError("bound TARGET.md is missing")
    actual = _sha256(resolved)
    if actual != expected:
        raise CertificateError(f"stale TARGET.md binding: expected {expected}, got {actual}")
    return actual


def _check_curve(value: Any) -> None:
    curve = _expect_dict(
        value,
        "$.curve",
        {"cremona_label", "lmfdb_label", "A", "B", "D", "phi_middle", "dual_middle"},
    )
    if _expect_str(curve["cremona_label"], "$.curve.cremona_label") != "62a1":
        raise CertificateError("wrong Cremona label")
    if _expect_str(curve["lmfdb_label"], "$.curve.lmfdb_label") != "62.a4":
        raise CertificateError("wrong LMFDB label")
    numbers = {key: _expect_int(curve[key], f"$.curve.{key}") for key in ("A", "B", "D", "phi_middle", "dual_middle")}
    if numbers != {"A": -15, "B": 64, "D": -31, "phi_middle": 30, "dual_middle": -15}:
        raise CertificateError("curve or covering constants do not match the frozen target")
    if numbers["D"] != numbers["A"] ** 2 - 4 * numbers["B"]:
        raise CertificateError("D != A^2-4B")
    if numbers["phi_middle"] != -2 * numbers["A"]:
        raise CertificateError("phi covering middle coefficient has wrong orientation")
    if numbers["dual_middle"] != numbers["A"]:
        raise CertificateError("dual covering middle coefficient has wrong orientation")
    _machine_curve_checks()


def _check_signature(value: Any) -> None:
    signature = _expect_dict(
        value,
        "$.family_signature",
        {"q_symbol", "prime", "positive", "q_not_divides", "q_mod_8", "legendre_q_31", "point_count_v2", "trace_nonzero"},
    )
    typed = {
        "q_symbol": _expect_str(signature["q_symbol"], "$.family_signature.q_symbol"),
        "prime": _expect_bool(signature["prime"], "$.family_signature.prime"),
        "positive": _expect_bool(signature["positive"], "$.family_signature.positive"),
        "q_not_divides": _expect_int(signature["q_not_divides"], "$.family_signature.q_not_divides"),
        "q_mod_8": _expect_int(signature["q_mod_8"], "$.family_signature.q_mod_8"),
        "legendre_q_31": _expect_int(signature["legendre_q_31"], "$.family_signature.legendre_q_31"),
        "point_count_v2": _expect_int(signature["point_count_v2"], "$.family_signature.point_count_v2"),
        "trace_nonzero": _expect_bool(signature["trace_nonzero"], "$.family_signature.trace_nonzero"),
    }
    expected = {
        "q_symbol": "q",
        "prime": True,
        "positive": True,
        "q_not_divides": 372,
        "q_mod_8": 5,
        "legendre_q_31": -1,
        "point_count_v2": 2,
        "trace_nonzero": True,
    }
    if typed != expected:
        raise CertificateError("family signature does not literally match frozen F_62")


def _check_witness(value: Any) -> Tuple[int, int, int]:
    witness = _expect_dict(
        value,
        "$.family_witness",
        {"q", "point_count", "trace", "v2_point_count", "legendre_q_31"},
    )
    q = _expect_int(witness["q"], "$.family_witness.q")
    if not _is_prime(q):
        raise CertificateError("family witness q is not prime")
    if q <= 0 or 372 % q == 0 or q % 8 != 5:
        raise CertificateError("family witness violates an elementary F_62 condition")
    legendre = _legendre(q, 31)
    if legendre != -1:
        raise CertificateError("family witness violates (q/31)=-1")
    count = _point_count_62a1(q)
    trace = q + 1 - count
    if _v2(count) != 2 or trace == 0:
        raise CertificateError("family witness violates the point-count conditions")
    expected_values = {
        "point_count": count,
        "trace": trace,
        "v2_point_count": _v2(count),
        "legendre_q_31": legendre,
    }
    for key, expected in expected_values.items():
        actual = _expect_int(witness[key], f"$.family_witness.{key}")
        if actual != expected:
            raise CertificateError(f"wrong witness field {key}: expected {expected}, got {actual}")
    return q, count, trace


def _check_ambient(value: Any) -> None:
    ambient = _expect_dict(value, "$.ambient", {"basis", "classes"})
    basis = _expect_string_list(ambient["basis"], "$.ambient.basis")
    if basis != ["-1", "2", "31", "q"]:
        raise CertificateError("ambient basis order must be [-1,2,31,q]")
    classes = _expect_string_list(ambient["classes"], "$.ambient.classes")
    if tuple(classes) != CLASS_IDS:
        raise CertificateError("ambient class enumeration is incomplete or noncanonical")


def _check_claimed_selmer(value: Any) -> None:
    claimed = _expect_dict(value, "$.claimed_selmer", {"phi", "dual_phi"})
    phi = _expect_string_list(claimed["phi"], "$.claimed_selmer.phi")
    dual = _expect_string_list(claimed["dual_phi"], "$.claimed_selmer.dual_phi")
    if tuple(phi) != PHI_TARGET:
        raise CertificateError("phi target is wrong, incomplete, or reverses the orientation")
    if tuple(dual) != DUAL_TARGET:
        raise CertificateError("dual-phi target is wrong, incomplete, or reverses the orientation")
    _check_subgroup(phi, "$.claimed_selmer.phi")
    _check_subgroup(dual, "$.claimed_selmer.dual_phi")


def _check_finite_checks(value: Any, q: int) -> str:
    checks = _expect_dict(
        value,
        "$.finite_checks",
        {
            "curve_change_rule",
            "isogeny_rule",
            "point_count_rule",
            "ambient_rule",
            "quartic_rule",
            "quartic_coefficients_sha256",
            "quartic_data_binding",
        },
    )
    expected_rules = {
        "curve_change_rule": "exact_polynomial_identity_v1",
        "isogeny_rule": "exact_laurent_polynomial_identity_v1",
        "point_count_rule": "exact_finite_field_enumeration_v1",
        "ambient_rule": "complete_f2_enumeration_v1",
        "quartic_rule": "exact_fraction_coefficients_v1",
    }
    for key, expected in expected_rules.items():
        if _expect_str(checks[key], f"$.finite_checks.{key}") != expected:
            raise CertificateError(f"unsupported finite rule in {key}")
    expected_digest = _quartic_digest(q)
    supplied_digest = _validate_digest(
        checks["quartic_coefficients_sha256"],
        "$.finite_checks.quartic_coefficients_sha256",
    )
    if supplied_digest != expected_digest:
        raise CertificateError(
            f"quartic coefficient digest mismatch: expected {expected_digest}, got {supplied_digest}"
        )
    binding = _expect_dict(
        checks["quartic_data_binding"],
        "$.finite_checks.quartic_data_binding",
        {"path", "sha256"},
    )
    relative = _expect_str(binding["path"], "$.finite_checks.quartic_data_binding.path")
    if relative != "q13-quartic-coefficients.txt":
        raise CertificateError("quartic data path must be exactly q13-quartic-coefficients.txt")
    bound_digest = _validate_digest(
        binding["sha256"],
        "$.finite_checks.quartic_data_binding.sha256",
    )
    if bound_digest != expected_digest:
        raise CertificateError("quartic data binding digest disagrees with exact recomputation")
    data_path = (PROJECT_ROOT / "certificates" / relative).resolve()
    if data_path.parent != (PROJECT_ROOT / "certificates").resolve() or not data_path.is_file():
        raise CertificateError("bound quartic data file is missing or outside certificates")
    actual_bytes = data_path.read_bytes()
    if actual_bytes != _quartic_bytes(q):
        raise CertificateError("quartic data bytes differ from exact recomputation")
    if hashlib.sha256(actual_bytes).hexdigest() != bound_digest:
        raise CertificateError("quartic data SHA-256 binding failed")
    return expected_digest


def _check_local_replay(value: Any, q: int) -> Dict[str, str]:
    replay = _expect_dict(value, "$.local_replay", set(PLACES))
    statuses: Dict[str, str] = {}
    for place in PLACES:
        row = _expect_dict(
            replay[place],
            f"$.local_replay.{place}",
            {"status", "machine_rule", "phi_accept", "dual_phi_accept"},
        )
        status = _expect_str(row["status"], f"$.local_replay.{place}.status")
        statuses[place] = status
        if place == "infinity":
            if status != "MACHINE_CHECKED":
                raise CertificateError("the archimedean row must be machine checked")
            if row["machine_rule"] != "exact_real_binary_quartic_v1":
                raise CertificateError("unsupported archimedean machine rule")
            phi = _expect_string_list(row["phi_accept"], "$.local_replay.infinity.phi_accept")
            dual = _expect_string_list(row["dual_phi_accept"], "$.local_replay.infinity.dual_phi_accept")
            if tuple(phi) != _real_acceptance(q, "phi"):
                raise CertificateError("incorrect archimedean phi local row")
            if tuple(dual) != _real_acceptance(q, "dual_phi"):
                raise CertificateError("incorrect archimedean dual-phi local row")
        else:
            if status != "TABLE_REPLAYED":
                raise CertificateError(
                    f"{place} must be TABLE_REPLAYED; protocol v1 does not permit promotion to a proved local lemma"
                )
            expected_rules = {
                "2": "signature_bits_at_2_v1",
                "31": "signature_bits_at_31_v1",
                "q": "signature_bits_at_q_v1",
                "outside_S": "ambient_unramified_table_v1",
            }
            if row["machine_rule"] != expected_rules[place]:
                raise CertificateError(f"unsupported finite table rule at {place}")
            phi = _expect_string_list(row["phi_accept"], f"$.local_replay.{place}.phi_accept")
            dual = _expect_string_list(row["dual_phi_accept"], f"$.local_replay.{place}.dual_phi_accept")
            if tuple(phi) != _signature_local_acceptance(place, "phi"):
                raise CertificateError(f"incorrect phi finite table at {place}")
            if tuple(dual) != _signature_local_acceptance(place, "dual_phi"):
                raise CertificateError(f"incorrect dual-phi finite table at {place}")

    phi_intersection = set(CLASS_IDS)
    dual_intersection = set(CLASS_IDS)
    for place in PLACES:
        phi_intersection.intersection_update(replay[place]["phi_accept"])
        dual_intersection.intersection_update(replay[place]["dual_phi_accept"])
    if tuple(sorted(phi_intersection)) != PHI_TARGET:
        raise CertificateError("finite local phi intersection does not equal the frozen target")
    if tuple(sorted(dual_intersection)) != DUAL_TARGET:
        raise CertificateError("finite local dual-phi intersection does not equal the frozen target")
    return statuses


def _check_obligations(value: Any) -> Dict[str, str]:
    if not isinstance(value, list):
        raise CertificateError("$.symbolic_obligations must be an array")
    seen: Dict[str, str] = {}
    for index, raw in enumerate(value):
        row = _expect_dict(
            raw,
            f"$.symbolic_obligations[{index}]",
            {"id", "status", "statement", "machine_binding"},
        )
        obligation_id = _expect_str(row["id"], f"$.symbolic_obligations[{index}].id")
        if obligation_id in seen:
            raise CertificateError(f"duplicate symbolic obligation: {obligation_id}")
        if obligation_id not in OBLIGATION_IDS:
            raise CertificateError(f"unknown symbolic obligation: {obligation_id}")
        statement = _expect_str(row["statement"], f"$.symbolic_obligations[{index}].statement")
        if not statement.strip():
            raise CertificateError(f"empty statement for symbolic obligation {obligation_id}")
        status = _expect_str(row["status"], f"$.symbolic_obligations[{index}].status")
        if status != "OPEN":
            raise CertificateError(
                f"symbolic obligation {obligation_id} claims {status}; protocol v1 accepts no prose proof bindings"
            )
        if row["machine_binding"] is not None:
            raise CertificateError(f"open obligation {obligation_id} must have null machine_binding")
        seen[obligation_id] = status
    if tuple(row["id"] for row in value) != OBLIGATION_IDS:
        raise CertificateError("symbolic obligations are incomplete or out of canonical order")
    return seen


def verify_certificate(certificate_path: Path, require_theorem: bool = False) -> Dict[str, Any]:
    certificate_path = certificate_path.resolve()
    raw = load_json(certificate_path)
    cert = _expect_dict(raw, "$", TOP_KEYS)
    if cert["protocol"] != PROTOCOL:
        raise CertificateError(f"unsupported protocol: {cert['protocol']!r}")
    if cert["scope"] != SCOPE:
        raise CertificateError("protocol v1 permits finite-replay-only scope")

    target_digest = _check_target_binding(cert["target_binding"], certificate_path)
    _check_curve(cert["curve"])
    _check_signature(cert["family_signature"])
    q, point_count, trace = _check_witness(cert["family_witness"])
    _check_ambient(cert["ambient"])
    _check_claimed_selmer(cert["claimed_selmer"])
    quartic_digest = _check_finite_checks(cert["finite_checks"], q)
    local_statuses = _check_local_replay(cert["local_replay"], q)
    obligation_statuses = _check_obligations(cert["symbolic_obligations"])

    complete = all(status == "MACHINE_CHECKED" for status in local_statuses.values()) and all(
        status == "MACHINE_CHECKED" for status in obligation_statuses.values()
    )
    if require_theorem and not complete:
        open_items = [f"local:{place}" for place, status in local_statuses.items() if status != "MACHINE_CHECKED"]
        open_items += [f"symbolic:{item}" for item, status in obligation_statuses.items() if status != "MACHINE_CHECKED"]
        raise CertificateError(
            "uniform theorem certification refused; open machine-checkable obligations: "
            + ", ".join(open_items)
        )

    return {
        "protocol": PROTOCOL,
        "certificate_structure": "PASS",
        "target_binding": target_digest,
        "exact_curve_and_isogeny_replay": "PASS",
        "family_witness": {"q": q, "point_count": point_count, "trace": trace, "status": "PASS"},
        "ambient_and_target_subgroups": "PASS",
        "quartic_coefficients": {"sha256": quartic_digest, "status": "PASS"},
        "local_replay": local_statuses,
        "finite_local_intersection": {
            "phi": list(PHI_TARGET),
            "dual_phi": list(DUAL_TARGET),
            "status": "PASS_AS_TABLE_REPLAY_ONLY",
        },
        "symbolic_obligations": obligation_statuses,
        "finite_replay": "PASS",
        "uniform_theorem_certified": "YES" if complete else "NO",
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, help="certificate JSON to verify")
    parser.add_argument(
        "--require-theorem",
        action="store_true",
        help="fail unless every uniform symbolic/local obligation is machine checked",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = verify_certificate(args.certificate, require_theorem=args.require_theorem)
    except CertificateError as exc:
        print(json.dumps({"certificate": "FAIL", "error": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
