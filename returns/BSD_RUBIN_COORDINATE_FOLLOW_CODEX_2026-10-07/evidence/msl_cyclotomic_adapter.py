#!/usr/bin/env python3
"""Read retained arbcore XB candidates; extract low cyclotomic coefficients mod p.

This is a downstream reader, not a replacement for the interval, lattice,
coefficient-corpus or primitive-period certificates. A successful parse does
not certify the producer. Output stays in the producer's real-period convention.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, isqrt
from pathlib import Path
import json
import re


def require_prime(p):
    if p < 5 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError('an ordinary coefficient prime p >= 5 is required')


def read_plus(path, m, p):
    text = Path(path).read_text()
    expected = {a for a in range(1, m) if gcd(a, m) == 1}
    values = {}
    for line in text.splitlines():
        if not line.startswith('XB '):
            continue
        hit = re.search(r'^XB (\d+) plus .*? cand (-?\d+/\d+) contains ([01]) unique ([01]) minus ', line)
        if not hit or hit.group(3) != '1' or hit.group(4) != '1':
            raise ValueError('an XB candidate lacks successful containment/uniqueness flags')
        a = int(hit.group(1))
        if a in values:
            raise ValueError('duplicate residue')
        value = Fraction(hit.group(2))
        if value.denominator % p == 0:
            raise ValueError('p is not a unit in the symbol denominator')
        values[a] = value
    if set(values) != expected:
        raise ValueError('incomplete or wrong-modulus unit residue table')
    if not all(values[a] == values[m-a] for a in values):
        raise ValueError('plus symmetry fails')
    return values


def u(a, p):
    return ((pow(a, p-1, p*p)-1)//p) * pow(p-1, -1, p) % p


def residue(value, p):
    return value.numerator * pow(value.denominator, -1, p) % p


def extract(p, ap, high, low=None):
    require_prime(p)
    if ap % p == 0:
        raise ValueError('supersingular prime: ordinary measure formula not applicable')
    ai = pow(ap, -1, p)
    # For i <= p-2, sum_{u in F_p} binom(u,i) = binom(p,i+1) = 0 mod p.
    # In each fixed residue class mod p, u(a) runs over F_p. This kills the
    # alpha^-3 lower-level contribution without assuming any value for it.
    degrees = list(range(min(3, p-2)+1))
    out = [sum(ai*ai*residue(v,p)*comb(u(a,p),i) for a,v in high.items()) % p for i in degrees]
    full = None
    if low is not None:
        full = [sum((ai*ai*residue(v,p)-ai**3*residue(low[a%p],p))*comb(u(a,p),i)
                    for a,v in high.items()) % p for i in degrees]
        if full != out:
            raise AssertionError('full measure and high-level-only formula differ')
    return {'p':p, 'a_p':ap, 'unit_root_mod_p':ap%p, 'degrees':degrees,
            'coefficients_mod_p':out, 'ell_2_mod_p':out[2],
            'full_measure_coefficients_mod_p':full,
            'normalization':'unchanged arbcore real-period convention',
            'scope':'cyclotomic weight-two residues only; no Hida weight derivatives or BSD promotion'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--ap',type=int,required=True)
    parser.add_argument('--high',required=True)
    parser.add_argument('--low')
    args=parser.parse_args()
    require_prime(args.p)
    high=read_plus(args.high,args.p**2,args.p)
    low=read_plus(args.low,args.p,args.p) if args.low else None
    result=extract(args.p,args.ap,high,low)
    result['files']=[{'path':str(Path(f).resolve()),'sha256':sha256(Path(f).read_bytes()).hexdigest()}
                     for f in [args.high,args.low] if f]
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
