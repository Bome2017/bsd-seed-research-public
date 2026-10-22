#!/usr/bin/env python3
"""Re-normalize retained anchored numerator balls using the elliptic period area.

Standard library only. No Brandt eigenvector, M, expected answer, or Petersson
self-pairing is used by normalize(). The supplied input balls retain the
mathematical/error-bound dependency grade of their source calculation.
"""
from __future__ import annotations
import argparse
import json
import math
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Any

BITS = 256
GRID = 1 << BITS

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")
    @classmethod
    def point(cls, x: int | F) -> 'I':
        return cls(F(x), F(x))
    def __add__(self, b: 'I') -> 'I':
        return I(self.lo+b.lo,self.hi+b.hi)
    def __neg__(self) -> 'I':
        return I(-self.hi,-self.lo)
    def __sub__(self,b: 'I') -> 'I':
        return self+-b
    def __mul__(self,b: 'I') -> 'I':
        t=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(t),max(t))
    def inv(self) -> 'I':
        if self.lo <= 0 <= self.hi:
            raise ValueError("cannot divide by interval containing zero")
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,b: 'I') -> 'I':
        return self*b.inv()
    def square(self) -> 'I':
        return I(F(0) if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),
                 max(self.lo**2,self.hi**2))
    def rounded(self) -> 'I':
        a=self.lo*GRID; b=self.hi*GRID
        return I(F(a.numerator//a.denominator,GRID),
                 F(-((-b.numerator)//b.denominator),GRID))
    def sqrt(self) -> 'I':
        if self.lo < 0:
            raise ValueError("negative square-root input")
        def lower(q: F) -> int:
            return math.isqrt((q.numerator*GRID*GRID)//q.denominator)
        l=lower(self.lo); h=lower(self.hi)
        if F(h*h,GRID*GRID) != self.hi: h+=1
        return I(F(l,GRID),F(h,GRID))
    def serial(self) -> list[str]:
        return [str(self.lo),str(self.hi)]

def agm(a: I,b: I, target_bits: int=180) -> tuple[I,int]:
    if min(a.lo,b.lo) <= 0:
        raise ValueError("AGM requires positive inputs")
    # For positive arguments AGM lies between the geometric and arithmetic mean.
    # All operations below enclose those exact iterates; no stopping heuristic.
    for n in range(1,40):
        olda,oldb=a,b
        a=((olda+oldb)/I.point(2)).rounded()
        b=(olda*oldb).sqrt()
        bound=I(b.lo,a.hi)
        if bound.hi-bound.lo <= F(1,1<<target_bits):
            return bound,n
    raise RuntimeError("AGM interval did not meet its target")

def period_area_multiplier(a2: int,a4: int) -> tuple[I,dict[str,Any]]:
    """4*pi^2/area(E(C), dx/(2y)), for y^2=x(x^2+a2*x+a4).

    The model must have three distinct real roots and the requested Neron
    differential must be dx/(2y). Formula uses the actual complex period area,
    NOT the integral over both real components.
    """
    disc=a2*a2-4*a4
    if disc<=0 or a4==0:
        raise ValueError("need three distinct real roots")
    sd=I.point(disc).sqrt()
    roots=[I.point(0),(I.point(-a2)-sd)/I.point(2),
           (I.point(-a2)+sd)/I.point(2)]
    roots.sort(key=lambda x:x.lo)
    if any(roots[i].hi >= roots[i+1].lo for i in range(2)):
        raise ValueError("root intervals not separated")
    e3,e2,e1=roots
    a=(e1-e3).sqrt(); b=(e1-e2).sqrt(); c=(e2-e3).sqrt()
    ar,nr=agm(a,b); ai,ni=agm(a,c)
    # omega_1=pi/ar; omega_2=i*pi/ai, since the discriminant is positive.
    mult=(I.point(4)*ar*ai).rounded()
    return mult,{'agm_steps':[nr,ni], 'precision_bits':BITS,
                 'target_width_bits':180, 'root_intervals':[x.serial() for x in roots],
                 'real_agm':ar.serial(),'imaginary_agm':ai.serial()}

def read_ball(x: list[str]) -> I:
    if len(x)!=2: raise ValueError("expected interval endpoints")
    return I(F(x[0]),F(x[1]))

def decimal_enclosure(x: I,digits: int=12) -> list[str]:
    scale=10**digits
    def s(v: int) -> str:
        sign='-' if v<0 else ''; v=abs(v)
        return f'{sign}{v//scale}.{v%scale:0{digits}d}'
    a=x.lo*scale;b=x.hi*scale
    return [s(a.numerator//a.denominator),s(-((-b.numerator)//b.denominator))]

def normalize(data: dict[str,Any]) -> dict[str,Any]:
    a2,a4=data['curve_a2_a4']
    mult,proof=period_area_multiplier(a2,a4)
    out={'scope':'Certified interval transformation only; no rational/integer reconstruction.',
         'period_multiplier':mult.serial(),'period_multiplier_display':decimal_enclosure(mult,20),
         'agm_record':proof,'results':{}}
    for label,row in data['numerator_balls'].items():
        A=read_ball(row['anchor']);R=read_ball(row['weighted_row'])
        if A.lo<=0: raise ValueError("positive raw anchor required")
        V=mult*R.square()/A
        results={'normalized_anchor':(mult*A).serial(),
                 'normalized_row':(mult*R).serial(),
                 'normalized_packet':V.serial(),
                 'display':{'anchor':decimal_enclosure(mult*A),
                            'row':decimal_enclosure(mult*R),
                            'packet':decimal_enclosure(V)}}
        out['results'][label]=results
    return out

def checks() -> dict[str,Any]:
    for q in [F(0),F(1),F(2),F(3,5),F(297),F(91790289)]:
        t=I.point(q).sqrt();assert t.lo**2<=q<=t.hi**2
    assert I(F(-1),F(2)).square()==I(F(0),F(4))
    try:I(F(-1),F(1)).inv()
    except ValueError:pass
    else:raise AssertionError('zero denominator accepted')
    # Raw kernel can fail p-integrality even when the rescaled kernel is useful.
    psi=[1,2];M=sum(x*x for x in psi);d=M;p=5
    assert F(psi[0]**2,M).denominator % p==0
    assert F(d*psi[0]**2,M)==1
    # A unit ratio alone cannot certify primitive p-nonvanishing.
    assert F(5,5)==1 and 5%5==0
    # Known denominator support alone is not a real reconstruction lattice.
    for k in [10,30,100,300]:
        power=1<<k
        n=5*((3*power+2)//5)
        x=F(n,power)
        assert abs(x-3)<=F(5,2*power)
        assert x.numerator%5==0 and x.denominator%5!=0
    return {'sqrt_enclosures':6,'interval_controls':'PASS',
            'nonintegral_raw_kernel_control':'PASS',
            'unit_ratio_counterexample':'PASS',
            'unbounded_S_denominator_controls':4}

def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    data=json.loads(args.input.read_text())
    out=normalize(data);out['checks']=checks()
    seed,seedproof=period_area_multiplier(-22735,106272484)
    out['seed_period_multiplier']={'ball':seed.serial(),
                                  'display':decimal_enclosure(seed,15),
                                  'agm_record':seedproof,
                                  'not_a_seed_kernel_value':True}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print('NORM_INTERVAL_REASSEMBLY_PASS')
    for label,r in out['results'].items():print(label,json.dumps(r['display']))
    print('seed multiplier',out['seed_period_multiplier']['display'])
if __name__=='__main__':main()
