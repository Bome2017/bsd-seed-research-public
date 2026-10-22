#!/usr/bin/env python3
"""Standalone interval height certificate; no Sage/PARI, no L-series recomputation.

Exact curve arithmetic and exact polynomial bounds use Fraction. Decimal basic
operations round outwards; ln/sqrt (correctly rounded by Decimal) are widened by
one representable number in each direction. See REGULATOR_CERTIFICATE.md.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from math import comb, isqrt
import argparse, json, platform

A2, A4 = -22735, 106272484
BAD = (2, 3, 2243, 4547, 5843)
PREC = 100

def op(a, b, name, rounding):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = rounding
        return getattr(a, name)(b)

class I:
    def __init__(self, a, b=None):
        if isinstance(a, I): self.lo, self.hi = a.lo, a.hi; return
        if isinstance(a, F):
            self.lo = op(D(a.numerator), D(a.denominator), '__truediv__', ROUND_FLOOR)
            self.hi = op(D(a.numerator), D(a.denominator), '__truediv__', ROUND_CEILING)
        else:
            self.lo, self.hi = D(a), D(a if b is None else b)
        assert self.lo <= self.hi
    def __add__(self, other):
        y = I(other)
        return I(op(self.lo,y.lo,'__add__',ROUND_FLOOR),op(self.hi,y.hi,'__add__',ROUND_CEILING))
    __radd__ = __add__
    def __neg__(self): return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self, other): return self + (-I(other))
    def __rsub__(self, other): return I(other) + (-self)
    def __mul__(self, other):
        y=I(other); pairs=[(a,b) for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(op(a,b,'__mul__',ROUND_FLOOR) for a,b in pairs),max(op(a,b,'__mul__',ROUND_CEILING) for a,b in pairs))
    __rmul__=__mul__
    def __truediv__(self, other):
        y=I(other); assert y.lo>0 or y.hi<0
        return self*I(op(D(1),y.hi,'__truediv__',ROUND_FLOOR),op(D(1),y.lo,'__truediv__',ROUND_CEILING))
    def __rtruediv__(self, other): return I(other)/self
    def __pow__(self, n):
        assert n>=0
        r=I(1)
        for _ in range(n): r=r*self
        return r
    def monotone(self, name):
        assert self.lo>0
        with localcontext() as c:
            c.prec=PREC
            lo=getattr(self.lo,name)().next_minus()
            hi=getattr(self.hi,name)().next_plus()
        return I(lo,hi)
    def log(self): return self.monotone('ln')
    def sqrt(self): return self.monotone('sqrt')
    def pair(self): return [str(self.lo),str(self.hi)]

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P; u,v=Q
    if x==u and y==-v:return None
    m=(3*x*x+2*A2*x+A4)/(2*y) if P==Q else (v-y)/(u-x)
    xx=m*m-A2-x-u
    return (xx,-y+m*(x-xx))

def on_curve(P):
    x,y=P
    return y*y==x*x*x+A2*x*x+A4*x

def smooth(P,p):
    x,y=P
    if x.denominator%p==0:
        # Weighted primitive coordinates reduce to the nonsingular infinity.
        d=isqrt(x.denominator)
        assert d*d==x.denominator and y.denominator==d**3
        assert x.numerator%p and y.numerator%p
        return True
    xx=x.numerator*pow(x.denominator,-1,p)%p
    yy=y.numerator*pow(y.denominator,-1,p)%p
    return ((2*yy)%p)!=0 or ((3*xx*xx+2*A2*xx+A4)%p)!=0

# x_t=x+2, hence x=x_t-2.
at2=A2-6; at4=A4-4*A2+12; at6=-8+4*A2-2*A4
b2=4*at2; b4=2*at4; b6=4*at6; b8=4*at2*at6-at4*at4
Z=[F(1),F(0),F(-b4),F(-2*b6),F(-b8)]

def poly(cs,x):
    r=0
    for c in cs[::-1]: r=r*x+c
    return r

def bernstein(cs,a,b):
    d=len(cs)-1
    cp=[sum(cs[i]*comb(i,j)*a**(i-j)*(b-a)**j for i in range(j,d+1)) for j in range(d+1)]
    return [sum(cp[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]

def atan_inverse(d,n=90):
    s=sum(F((-1)**j,(2*j+1)*d**(2*j+1)) for j in range(n))
    next_term=F((-1)**n,(2*n+1)*d**(2*n+1))
    a,b=sorted([s,s+next_term])
    return I(I(a).lo,I(b).hi)

def prove_bounds():
    # The two nonzero roots satisfy e2+2<6600<16000<e1+2.
    assert poly([A4,A2,1],F(6598))<0
    assert poly([A4,A2,1],F(15998))<0
    assert A4>0 and -A2>0
    minima=[]
    for j in range(8):
        beta=bernstein(Z,F(j,128000),F(j+1,128000))
        minima.append(min(beta)); assert min(beta)>F(1,4)
    # z'/t=-2b4-6b6*t-4b8*t^2 increases for t>=0.
    assert b6<0 and b8<0
    assert -2*b4-6*b6*F(1,6600)-4*b8*F(1,6600)**2>0
    assert poly(Z,F(1,6600))>F(1,4)
    upper=sum(abs(Z[i])*F(1,2)**i for i in range(5))
    assert upper<2**50
    # Therefore 1/4<z<2^50 on E(R); |log z|<50 since log 2<1.
    delta=16*A4*A4*(A2*A2-4*A4)
    product=2**8*3**2*2243*4547**3*5843**2
    assert delta==product
    return {'z_lower':'1/4','z_upper':'2^50','log_bound':50,
            'bernstein_minima':[str(a) for a in minima],
            'upper_polynomial_bound':str(upper),'discriminant':str(delta),
            'minimality':'Every discriminant valuation is less than 12.'}

def height(P,n):
    assert on_curve(P)
    Q=add(P,P); assert Q is not None and on_curve(Q)
    assert all(smooth(Q,p) for p in BAD)
    xt=Q[0]+2; assert xt>0
    t=1/I(xt); s=I(0)
    for j in range(n):
        z=1-b4*t**2-2*b6*t**3-b8*t**4
        assert z.lo>0
        s=s+z.log()/4**j
        t=(4*t+b2*t**2+2*b4*t**3+b6*t**4)/z
    lam=I(xt).log()/2+s/8
    tail=I(F(50,6*4**n))
    lam=lam+I(tail.hi.copy_negate(),tail.hi)
    h=(2*lam+I(Q[0].denominator).log())/4
    return h,{'twice_point':[[str(a.numerator),str(a.denominator)] for a in Q],
              'smooth_at_bad_primes':list(BAD),'lambda_tail_upper':str(tail.hi)}

def main():
    global PREC
    pa=argparse.ArgumentParser();pa.add_argument('--precision',type=int,default=100);pa.add_argument('--terms',type=int,default=30)
    args=pa.parse_args();PREC=args.precision
    proof=prove_bounds()
    P=(F(4547),F(327384));Q=(F(5184),F(281520));PQ=add(P,Q)
    hs=[];details=[]
    for R in (P,Q,PQ):
        h,d=height(R,args.terms); hs.append(h);details.append(d)
    h1,h2,h12=hs;pair=(h12-h1-h2)/2;reg=h1*h2-pair*pair
    # Retained rigorous P3/stream-core period, widened at the last decimal.
    omega=2*I('0.02804490151943640444830940180786','0.02804490151943640444830940180800')
    # Independent real-period AGM with the exact quadratic roots.
    root=I(2243*4547).sqrt();e2=(22735-3*root)/2;e1=(22735+3*root)/2
    aa=e1.sqrt();bb=(e1-e2).sqrt()
    for _ in range(18):aa,bb=(aa+bb)/2,(aa*bb).sqrt()
    # Machin's identity and alternating-series rational bounds certify pi.
    pi=16*atan_inverse(5)-4*atan_inverse(239)
    agm=I(min(aa.lo,bb.lo),max(aa.hi,bb.hi));omega_check=2*pi/agm
    assert max(omega.lo,omega_check.lo)<=min(omega.hi,omega_check.hi)
    q=I('35.929604','35.941023')/(omega_check*reg)
    gap=I(1)/174
    assert q.lo> (36-gap).hi and q.hi<(36+gap).lo
    # Round outwards to a compact decimal interval used in the report.
    assert q.lo>D('35.99427') and q.hi<D('36.00573')
    print(json.dumps({'python':platform.python_version(),'precision':PREC,'terms':args.terms,
          'proof_bounds':proof,'heights':[h.pair() for h in hs],'pairing':pair.pair(),
          'regulator':reg.pair(),'omega_imported':omega.pair(),'omega_agm_crosscheck':omega_check.pair(),
          'omega_times_regulator':(omega_check*reg).pair(),'q_interval':q.pair(),
          'q_compact_interval':['35.99427','36.00573'],
          'denominator_174_spacing_pass':True,'exact_point_checks':details},indent=2))

if __name__=='__main__':main()
