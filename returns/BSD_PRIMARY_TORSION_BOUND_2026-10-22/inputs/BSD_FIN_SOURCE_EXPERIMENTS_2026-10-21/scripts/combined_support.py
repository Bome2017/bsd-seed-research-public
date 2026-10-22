#!/usr/bin/env python3
"""Adaptive scalar-closed exclusion including the quadratic Cayley candidates."""
from pathlib import Path
from fractions import Fraction
from math import gcd,isqrt
from functools import reduce
from operator import mul
import sympy as s,json,time,subprocess
R=Path(__file__).resolve().parents[1];start=time.monotonic()
cs=json.loads((R/'inputs/seed_polynomial.json').read_text())['G_coefficients']
z,w=s.symbols('z w');G=s.Poly.from_list(cs,z,domain=s.ZZ);F=s.Poly(G.as_expr().subs(z,w*w),w,domain=s.ZZ)
DF=abs(int(F.discriminant())); small=reduce(mul,s.primerange(2,65537),1)
def strip(a,b):
    a=abs(a)
    while (g:=gcd(a,b))!=1: a//=g
    return a
base=json.loads((R/'results/private_support_rows_prebatch.json').read_text())
keys={(r['a'],r['b']) for r in base}
rows=[{'kind':'rational','key':[r['a'],r['b']],'norm':r['norm'],
       'large_unramified_norm_part':r['large_unramified_norm_part']} for r in base]
reductions=[]
for r in json.loads((R/'results/cayley_quadratic.json').read_text()):
    a,b,c=r['a'],r['b'],r['c'];D=c*c-4*a*b
    if D>=0 and isqrt(D)**2==D:
        k=isqrt(D);rs=[Fraction(c+k,2*b),Fraction(c-k,2*b)]
        assert s.Poly(b*(w-s.Rational(rs[0].numerator,rs[0].denominator))*(w-s.Rational(rs[1].numerator,rs[1].denominator)),w)==s.Poly(a+b*w*w-c*w,w)
        refs=[]
        for rt in rs:
            assert rt!=0
            key=(abs(rt.numerator),rt.denominator)
            assert key in keys
            refs.append({'a':key[0],'b':key[1],'exponent':1 if rt>0 else -1})
        reductions.append({'a':a,'b':b,'c':c,'rational_cayley_factors':refs,'polynomial_identity_checked':True})
    else:
        N=abs(int(s.resultant(G.as_expr(),(a+b*z)**2-c*c*z,z)))
        assert N>0
        M=strip(strip(N,small),DF)
        rows.append({'kind':'quadratic','key':[a,b,c],'norm':str(N),'large_unramified_norm_part':str(M)})
vals=[int(r['large_unramified_norm_part']) for r in rows]
(R/'results/combined_norms.txt').write_text(str(len(vals))+'\n'+'\n'.join(map(str,vals))+'\n')
with (R/'results/combined_norms.txt').open() as fi,(R/'results/combined_certificate.txt').open('w') as fo,(R/'results/combined_stderr.txt').open('w') as fe:
    pr=subprocess.run([str(R/'scripts/batch_gcd')],stdin=fi,stdout=fo,stderr=fe,timeout=30)
assert pr.returncode==0
pairs=[tuple(map(int,x.split())) for x in (R/'results/combined_certificate.txt').read_text().splitlines()]
assert len(pairs)==len(rows)
bad=[]
for i,(r,M,(g,priv)) in enumerate(zip(rows,vals,pairs)):
    assert strip(M,g)==priv
    r['common_part_gcd']=str(g);r['private_norm_part']=str(priv)
    if priv<=1:bad.append(i)
(R/'results/combined_support_rows.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
(R/'results/quadratic_reductions.json').write_text(json.dumps(reductions,indent=2)+'\n')
summary={'status':'COMPLETE_SCALAR_CLOSURE_CERTIFICATE' if not bad else 'PARTIAL_PRIVATE_SUPPORT',
 'rational_candidates':len(base),'quadratic_candidates':272,
 'quadratic_reduced_exactly_to_rational_family':len(reductions),
 'remaining_quadratic_generators':len(rows)-len(base),
 'independent_private_scalar_orbits':len(rows)-len(bad),
 'unresolved_indices':bad,'ordinary_unit_image_from_this_family':'TRIVIAL' if not bad else 'NOT_DETERMINED',
 'conditional_rational_anti_divisor_rank':2*len(rows) if not bad else None,
 'elapsed_seconds':time.monotonic()-start,
 'scope':'This finite scalar-closed multiplicative family only; field identity and scalar action retained. Class groups and arbitrary units are not bounded.'}
(R/'results/COMBINED_SUPPORT_RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
