#!/usr/bin/env python3
"""Exact algebra controls; not a computation of a seed Kato class.

The ring is Z_p[[T,S]]/(p,T,S)^4. A supplied arithmetic jet can be
checked with --jet FILE, but its provenance is NOT certified by this code.
"""
from __future__ import annotations
import argparse
import json
import random
from pathlib import Path
from typing import Dict, Tuple

Mon = Tuple[int, int]
MONS = tuple((i, n-i) for n in range(4) for i in range(n+1))

class Jet:
    def __init__(self, p: int, terms: Dict[Mon, int] | None = None):
        self.p = p
        self.c = {m: int((terms or {}).get(m, 0)) % (p ** (4-sum(m))) for m in MONS}
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Jet) and self.p == other.p and self.c == other.c
    def __add__(self, other: Jet) -> Jet:
        assert self.p == other.p
        return Jet(self.p, {m: self.c[m] + other.c[m] for m in MONS})
    def __neg__(self) -> Jet:
        return Jet(self.p, {m: -v for m,v in self.c.items()})
    def __sub__(self, other: Jet) -> Jet:
        return self + (-other)
    def __mul__(self, other: Jet) -> Jet:
        assert self.p == other.p
        out = {m: 0 for m in MONS}
        for (i,j), a in self.c.items():
            for (k,l), b in other.c.items():
                if i+j+k+l < 4:
                    out[i+k,j+l] += a*b
        return Jet(self.p, out)
    def __pow__(self, n: int) -> Jet:
        if n < 0: raise ValueError('Only nonnegative powers are supported')
        result = Jet(self.p, {(0,0): 1})
        for _ in range(n): result = result*self
        return result
    def subst(self, t: Jet, s: Jet) -> Jet:
        out = Jet(self.p)
        for (i,j), a in self.c.items():
            out = out + Jet(self.p, {(0,0): a})*(t**i)*(s**j)
        return out
    def at(self, t: int, s: int) -> int:
        if t % self.p or s % self.p:
            raise ValueError('Evaluation must send T and S into p Z/p^4')
        return sum(a * t**i * s**j for (i,j),a in self.c.items()) % self.p**4
    def diagonal(self) -> int:
        return self.at(self.p, self.p)


def controls() -> dict:
    rng = random.Random(20261004)
    primes = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    counts = dict(evaluation_homomorphism=0, unit_invariance=0,
                  coordinate_roundtrip=0, shifted_diagonal=0,
                  coefficient_precision=0, valuation_shift=0,
                  integral_multiple_implication=0, signed_binomial_law=0)
    controls_out = []
    for p in primes:
        c = lambda a: Jet(p, {(0,0): a})
        T, S = Jet(p,{(1,0):1}), Jet(p,{(0,1):1})
        z, one = c(0), c(1)
        Sp = c(p) + c(1+p)*S
        inv = pow(1+p, -1, p**4)
        Sm = c(inv)*(S-c(p))
        for _ in range(120):
            a = Jet(p,{m:rng.randrange(p**(4-sum(m))) for m in MONS})
            b = Jet(p,{m:rng.randrange(p**(4-sum(m))) for m in MONS})
            assert (a+b).diagonal() == (a.diagonal()+b.diagonal()) % p**4
            assert (a*b).diagonal() == (a.diagonal()*b.diagonal()) % p**4
            counts['evaluation_homomorphism'] += 2
            u = Jet(p,{m:rng.randrange(p**(4-sum(m))) for m in MONS})
            if u.c[0,0] % p == 0:
                u.c[0,0] += 1
            assert ((u*a).diagonal() == 0) == (a.diagonal() == 0)
            counts['unit_invariance'] += 1
            assert a.subst(T,Sp).subst(T,Sm) == a
            assert a.subst(T,Sm).subst(T,Sp) == a
            counts['coordinate_roundtrip'] += 2
            assert a.subst(T,Sp).diagonal() == a.at(p,2*p+p*p)
            counts['shifted_diagonal'] += 1
            for m in MONS:
                lifted = dict(a.c)
                lifted[m] += rng.randint(-8,8)*p**(4-sum(m))
                naive = sum(x*p**sum(k) for k,x in lifted.items()) % p**4
                assert naive == a.diagonal()
                counts['coefficient_precision'] += 1
        # Genuine lower terms are not discarded. A nonzero jet can evaluate to zero.
        assert T-S != z and (T-S).diagonal() == 0
        assert T-c(p) != z and (T-c(p)).diagonal() == 0
        # The b=3 branch is lost by testing only the first divided digit.
        b3 = c(p*p)*T
        value = b3.diagonal()
        assert value == p**3 and (value//p**2) % p == 0
        assert (value//p**2) % p**2 != 0
        # Valuation-aware modular-period fallback, eta=p^h.
        for h in range(-4,7):
            for bval in range(2,10):
                if bval < h: continue  # M must be integral
                mval = bval-h
                M = p**mval
                if h <= 2:
                    d = 2-h
                    assert M % p**d == 0
                    verdict = (M//p**d) % p**2 != 0
                    assert verdict == (bval <= 3)
                elif h == 3:
                    assert (M % p != 0) == (bval <= 3)
                else:
                    assert bval >= 4
                counts['valuation_shift'] += 1
        for bval in range(2,8):
            for sval in range(5):
                for u in (1,2,p-1,p+1):
                    q = (p**(bval+sval)*u) % p**4
                    if q != 0: assert bval <= 3
                    if sval == 0: assert (q != 0) == (bval <= 3)
                    counts['integral_multiple_implication'] += 1
        # Binomial expansion of the intrinsic quotient's inertial character.
        def neg_power(s: int) -> Jet:
            return Jet(p,{(0,0):1,(0,1):-s,
                          (0,2):s*(s+1)//2,
                          (0,3):-s*(s+1)*(s+2)//6})
        for s in range(-8,9):
            for t in range(-8,9):
                assert neg_power(s)*neg_power(t) == neg_power(s+t)
                counts['signed_binomial_law'] += 1
        controls_out.append({'p':p, 'nonzero_jet_diagonal_zero':True,
                             'b3_retained_by_mod_p2':True,
                             'rational_anchor_not_integral':{'u_at_0':'1','u_at_p':f'1/{p}'}})
    return {'status':'PASS_FORMAL_ALGEBRA_ONLY','primes':primes,'counts':counts,
            'total_assertion_groups':sum(counts.values()),'countercontrols':controls_out,
            'not_computed':['seed Kato jet','eta_p','any new b_p','uniform nonvanishing'],
            'seed_primary_conclusions':[]}


def evaluate_file(path: Path) -> dict:
    payload = json.loads(path.read_text())
    p = payload.get('p')
    if not isinstance(p,int) or p < 5 or any(p%d == 0 for d in range(2,int(p**0.5)+1)):
        raise ValueError('p must be prime and at least 5')
    coeffs = payload.get('coefficients')
    if not isinstance(coeffs,list) or len(coeffs) != 10:
        raise ValueError('Exactly ten coefficient records are required')
    data = {}
    for row in coeffs:
        i,j,v = row.get('i'),row.get('j'),row.get('value')
        if any(type(t) is not int for t in (i,j,v)) or (i,j) not in MONS or (i,j) in data:
            raise ValueError('Invalid or duplicate monomial record')
        data[i,j] = v
    f = Jet(p,data)
    value=f.diagonal()
    return {'status':'ARITHMETIC_PROVENANCE_NOT_VERIFIED', 'p':p,
            'diagonal_residue_mod_p4':value, 'nonzero':value != 0,
            'bsd_claim':False,
            'warning':'Only finite-ring evaluation was checked. Actual Kato origin, integral lattice and theorem hypotheses must be established separately.'}

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--jet',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    result=evaluate_file(args.jet) if args.jet else controls()
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output: args.output.write_text(text)
    print(text)
