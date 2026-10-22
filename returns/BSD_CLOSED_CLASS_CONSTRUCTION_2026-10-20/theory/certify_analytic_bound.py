#!/usr/bin/env python3
"""Exact outward certificate; no floating-point acceptance and no class computation."""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
DEN = 10**18

def ceilq(x):
    return -(-x.numerator // x.denominator)

def down(x, den=DEN):
    return F(x.numerator * den // x.denominator, den)

def up(x, den=DEN):
    return F(ceilq(x * den), den)

def log_unit_interval(x, terms=32):
    """For 1<=x<=2: positive atanh series, with rigorous geometric tail."""
    assert 1 <= x <= 2
    y = (x - 1) / (x + 1)
    lower = 2 * sum((y**(2*k+1) / (2*k+1) for k in range(terms)), F(0))
    error = 2*y**(2*terms+1) / ((2*terms+1)*(1-y*y))
    return down(lower), up(lower + error)

def log_integer_interval(n):
    assert n >= 1
    k = n.bit_length() - 1
    a, b = log_unit_interval(F(n, 2**k))
    l2, u2 = log_unit_interval(F(2))
    return down(k*l2+a), up(k*u2+b)

def atan_interval(x, terms=20):
    """Even-length alternating truncation is a lower bound for 0<x<1."""
    assert 0 < x < 1 and terms % 2 == 0
    s = sum(((-1)**k * x**(2*k+1) / (2*k+1) for k in range(terms)), F(0))
    return s, s + x**(2*terms+1)/(2*terms+1)

def pair(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}

def main():
    source = HERE / "FIELD_INPUTS.json"
    inp = json.loads(source.read_text())
    DA, DK = int(inp["D_A"]), int(inp["D_Aplus"])
    delta = int(inp["norm_relative_discriminant"])
    assert delta == 2**4 * 5 * 4547**6
    assert DA == DK*DK*delta
    Q = DK*delta
    ld, ud = log_integer_interval(delta)
    l2, u2 = log_integer_interval(2)
    lQ, uQ = log_integer_interval(Q)
    # sqrt(5) and sqrt(Q) are bounded by integer squaring, not decimal evaluation.
    sqrt5_upper = F(223606797749979, 10**14)
    assert sqrt5_upper**2 > 5
    sqrtQ_upper = isqrt(Q) + 1
    assert (sqrtQ_upper-1)**2 <= Q < sqrtQ_upper**2
    lam = down((ld - 24*u2)/(2*sqrt5_upper))
    assert lam > 0
    a5, b5 = atan_interval(F(1,5))
    a239, b239 = atan_interval(F(1,239))
    # Machin's identity: pi = 16 atan(1/5) - 4 atan(1/239).
    pi_lower = down(16*a5 - 4*b239)
    pi_upper = up(16*b5 - 4*a239)
    e_upper = up(sum((F(1, factorial(k)) for k in range(21)), F(0))
                 + F(1, factorial(20)*20))
    reg_lower = pi_lower**3 * lam**6 / 768
    L_upper = 2*(e_upper*uQ/24)**12
    order_upper_fraction = sqrtQ_upper*L_upper/((2*pi_lower)**6*reg_lower)
    order_upper_integer = ceilq(order_upper_fraction)
    assert order_upper_integer < 5**98
    assert order_upper_integer >= 5**97
    # We deliberately report a convenient coarse exact integer, still below 5^98.
    coarse_integer = 262 * 10**66
    assert order_upper_integer <= coarse_integer < 5**98
    out = {
        "status": "EXACT_OUTWARD_RELATIVE_CLASS_ORDER_BOUND",
        "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "input_grade": "retained exact maximal-order discriminants and field signatures",
        "arithmetic_conductor_Q": str(Q),
        "log_delta_interval": [pair(ld), pair(ud)],
        "log_2_interval": [pair(l2), pair(u2)],
        "log_Q_interval": [pair(lQ), pair(uQ)],
        "sqrt5_upper": pair(sqrt5_upper),
        "sqrtQ_upper_integer": str(sqrtQ_upper),
        "lambda_lower": pair(lam),
        "pi_interval": [pair(pi_lower), pair(pi_upper)],
        "e_upper": pair(e_upper),
        "regulator_ratio_lower_floor": str(reg_lower.numerator//reg_lower.denominator),
        "L_value_upper_ceiling": str(ceilq(L_upper)),
        "relative_class_order_bound_exact_rounded": str(order_upper_integer),
        "relative_class_order_bound_coarse_integer": str(coarse_integer),
        "five_power_98": str(5**98),
        "five_primary_length_upper": 97,
        "sum_of_two_faithful_five_ranks_upper": 97,
        "no_GRH": True,
        "no_elliptic_Sha_or_BSD_input": True,
        "scope": "actual coefficient-five point field only; no sufficiently small seed bound or across-prime result",
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
