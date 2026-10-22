#!/usr/bin/env python3
"""Exact rational-norm private-support test for scalar closure of the Cayley family.
This excludes finite source families, not arbitrary units or arithmetic class groups.
"""
from pathlib import Path
from math import gcd
from functools import reduce
from operator import mul
import sympy as s
import json,time,sys,subprocess
R=Path(__file__).resolve().parents[1]
cs=json.loads((R/'inputs/seed_polynomial.json').read_text())['G_coefficients']
z=s.symbols('z');w=s.symbols('w');G=s.Poly.from_list(cs,z,domain=s.ZZ)
F=s.Poly(G.as_expr().subs(z,w*w),w,domain=s.ZZ)
DF=abs(int(F.discriminant()))
small=reduce(mul,s.primerange(2,65537),1)
def remove_shared_primes(a,b):
    a=abs(a)
    while (g:=gcd(a,b))!=1:
        a//=g
    return a

def norm(a,b):
    aa=a*a;bb=b*b;m=len(cs)-1
    return abs(sum(c*aa**(m-i)*bb**i for i,c in enumerate(cs)))
def batchgcd(vals):
    tree=[vals]
    while len(tree[-1])>1:
        t=tree[-1]
        tree.append([t[i]*t[i+1] if i+1<len(t) else t[i] for i in range(0,len(t),2)])
    rem=tree[-1]
    for level in range(len(tree)-2,-1,-1):
        rem=[rem[i//2]%(a*a) for i,a in enumerate(tree[level])]
    assert all(r%a==0 for a,r in zip(vals,rem))
    return [gcd(a,r//a) for a,r in zip(vals,rem)]

start=time.monotonic()
orig=json.loads((R/'results/cayley_rational.json').read_text())
rows=[];vals=[]
for r in orig:
    a,b=r['a'],r['b'];N=norm(a,b)
    M=remove_shared_primes(remove_shared_primes(N,small),DF)
    rows.append({'a':a,'b':b,'norm':str(N),'large_unramified_norm_part':str(M)})
    vals.append(M)
print('Norms stripped',len(vals),'missing residual',vals.count(1),'elapsed',time.monotonic()-start,flush=True)
# Save all input norms before the computationally expensive stage.
(R/'results/private_support_rows_prebatch.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
(R/'results/batch_gcd_input.txt').write_text(str(len(vals))+'\n'+'\n'.join(map(str,vals))+'\n')
with (R/'results/batch_gcd_input.txt').open() as fi, (R/'results/batch_gcd_output.txt').open('w') as fo, (R/'results/batch_gcd_stderr.txt').open('w') as fe:
    proc=subprocess.run([str(R/'scripts/batch_gcd')],stdin=fi,stdout=fo,stderr=fe,timeout=30)
assert proc.returncode==0
pairs=[tuple(map(int,line.split())) for line in (R/'results/batch_gcd_output.txt').read_text().splitlines()]
assert len(pairs)==len(vals)
gs=[t[0] for t in pairs]
assert all(remove_shared_primes(M,g)==priv for M,(g,priv) in zip(vals,pairs))
passed=[];unresolved=[]
for i,(r,M,g) in enumerate(zip(rows,vals,gs)):
    priv=remove_shared_primes(M,g)
    r['common_part_gcd']=str(g);r['private_norm_part']=str(priv)
    r['has_private_unramified_prime']=priv>1
    (passed if priv>1 else unresolved).append(i)
(R/'results/private_support_rows.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
summary={'status':'COMPLETED_PRIVATE_NORM_SUPPORT_TEST',
         'original_rational_candidates':len(rows),'private_certified':len(passed),
         'unresolved_indices':unresolved,'after_small_and_discriminant_strip_one':vals.count(1),
         'small_rational_prime_cutoff':65536,'field_polynomial_discriminant_digits':len(str(DF)),
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Every certified index has a rational prime absent from all other candidate norms and from the polynomial discriminant. This gives an independent private scalar orbit of valuations. Uncertified indices are not excluded.'}
(R/'results/PRIVATE_SUPPORT_RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
