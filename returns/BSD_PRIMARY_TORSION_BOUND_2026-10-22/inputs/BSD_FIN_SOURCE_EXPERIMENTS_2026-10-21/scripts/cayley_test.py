#!/usr/bin/env python3
"""Exact necessary ordinary-unit admission for two new finite norm-one families."""
from fractions import Fraction
from math import gcd
from pathlib import Path
import json, hashlib, time
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
INP=ROOT/'inputs/seed_polynomial.json'
cs=json.loads(INP.read_text())['G_coefficients']
z=s.symbols('z'); G=s.Poly.from_list(cs,z,domain=s.QQ); m=G.degree(); n=2*m
# Newton sums for the trace on Q[z]/G, valid independently of an integral basis.
powtrace=[s.Integer(m)]
for k in range(1,m):
    powtrace.append(-sum(s.Integer(cs[j])*powtrace[k-j] for j in range(1,k))-k*cs[k])
def h_eval(a,b,coefs):
    d=len(coefs)-1
    return sum(c*a**(d-i)*b**i for i,c in enumerate(coefs))
def trace_cayley(a,b):
    aa=a*a;bb=b*b
    N=h_eval(aa,bb,cs)
    D=h_eval(aa,bb,[(m-i)*cs[i] for i in range(m)])
    if N==0: raise ValueError('zero denominator: invalid algebraic source')
    return Fraction(n)-Fraction(4*aa*D,N)
def trace_quadratic(a,b,c):
    # u=(a+b z+c w)/(a+b z-c w); its two w-conjugates sum to
    # 2+4 c^2 z/((a+b z)^2-c^2 z). Relative norm is exactly one.
    q=s.Poly((a+b*z)**2-c*c*z,z,domain=s.QQ)
    inv=s.invert(q,G)
    h=(s.Poly(z,z,domain=s.QQ)*inv).rem(G)
    tr=sum(h.nth(i)*powtrace[i] for i in range(m))
    t=s.Rational(n)+4*c*c*tr
    return Fraction(int(s.numer(t)),int(s.denom(t)))
def rec(t):
    return {'numerator':str(t.numerator),'denominator':str(t.denominator),
            'trace_integral':t.denominator==1}
start=time.monotonic()
rational=[]
for b in range(1,17):
    for a in range(1,2049):
        if gcd(a,b)!=1: continue
        t=trace_cayley(a,b)
        rational.append({'a':a,'b':b,**rec(t)})
(ROOT/'results/cayley_rational.json').write_text(json.dumps(rational,separators=(',',':'))+'\n')
print('RATIONAL',len(rational),'trace passes',sum(r['trace_integral'] for r in rational),flush=True)
quad=[];seen=set()
for a in (1,2,4,8,16,32,64,128,256,512):
  for b in (-8,-4,-2,-1,1,2,4,8):
    for c in (1,4,16,64,256):
      g=gcd(gcd(a,abs(b)),c); triple=(a//g,b//g,c//g)
      if triple in seen: continue
      seen.add(triple)
      t=trace_quadratic(*triple)
      quad.append({'a':triple[0],'b':triple[1],'c':triple[2],**rec(t)})
(ROOT/'results/cayley_quadratic.json').write_text(json.dumps(quad,separators=(',',':'))+'\n')
result={'status':'COMPLETED_EXACT_NECESSARY_INTEGRALITY_SCREEN','input_sha256':hashlib.sha256(INP.read_bytes()).hexdigest(),
        'rational_candidates':len(rational),'rational_integral_trace_passes':sum(r['trace_integral'] for r in rational),
        'quadratic_candidates':len(quad),'quadratic_integral_trace_passes':sum(r['trace_integral'] for r in quad),
        'elapsed_seconds':time.monotonic()-start,
        'scope':'Finite families only. Passing trace integrality would NOT certify an ordinary unit; a failure rigorously rejects it.',
        'new_unit_rank':0,'new_class_bound':None,'FIN':'UNCHANGED_OPEN'}
(ROOT/'results/CAYLEY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
