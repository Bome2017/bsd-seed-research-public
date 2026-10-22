"""Audit retained receipts without altering the Stage-I reconstruction."""
from pathlib import Path
import csv, hashlib, json, math
from collections import Counter
import sympy as s
root=Path('/mnt/data/pk66_continuation')
r=root/'retained'
freeze=Path('/mnt/data/pk66_independent/PRE_COMPARISON_RECONSTRUCTION.md')
expected='0f9468a2747c98794e3c7ff3991439cd8f2355095fd2b370b6c641daaca19050'
assert hashlib.sha256(freeze.read_bytes()).hexdigest()==expected
rows=[{k:int(v) for k,v in d.items()} for d in csv.DictReader((r/'independent_counts.csv').open())]
B=100000
sieve=bytearray(b'\1')*B;sieve[:2]=b'\0\0'
for p in range(2,math.isqrt(B-1)+1):
    if sieve[p]: sieve[p*p:B:p]=b'\0'*(((B-1-p*p)//p)+1)
assert [z['p'] for z in rows]==[p for p in range(3,B) if sieve[p] and p not in (3,11)]
def chi(a,p):
    t=pow(a%p,(p-1)//2,p)
    return -1 if t==p-1 else t
fam=[]; control=Counter()
for z in rows:
    p=z['p'];N=z['N_min'];v=(N & -N).bit_length()-1
    assert z['N_descent']==N and z['trace']==p+1-N and z['v2']==v
    assert z['chi2']==chi(2,p) and z['chi_neg2']==chi(-2,p) and z['chi33']==chi(33,p)
    assert z['q_over3']==chi(p,3) and z['q_over11']==chi(p,11)
    f=int(p%8==5 and chi(p,3)==-1 and chi(p,11)==1)
    assert z['family']==f
    assert (v==2)==(chi(-2,p)==chi(33,p)==-1)
    assert chi(33,p)==chi(p,3)*chi(p,11)
    control[(chi(2,p),chi(33,p),v)]+=1
    if f:
        assert v==2 and z['trace']%8==2
        fam.append(z)
# Independent direct enumeration of the two small, contrasting controls.
literal={}
for p in (5,19):
    n=1+sum((v*v+u*v+v-u**3-u*u+2*u+1)%p==0 for u in range(p) for v in range(p))
    c=1+sum((y*y-x**3-17*x*x-64*x)%p==0 for x in range(p) for y in range(p))
    assert n==c==next(z['N_min'] for z in rows if z['p']==p)
    literal[str(p)]={'minimal_count':n,'descent_count':c,'chi2':chi(2,p),'chi33':chi(33,p)}
# Independently check the new integral minimal twist model algebra.
q,U,V=s.symbols('q U V')
a1,a2,a3,a4,a6=1,(5*q-1)/4,1,-(3*q*q+1)/2,-(3*q**3+1)/4
M=V**2+U*V+V-U**3-a2*U**2-a4*U-a6
x,y=4*(U-q),8*V+4*U+4
assert s.expand(y*y-x**3-17*q*x*x-64*q*q*x-64*M)==0
b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=s.expand(b2*b2-24*b4);c6=s.expand(-b2**3+36*b2*b4-216*b6)
D=s.expand(-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
assert (c4,c6,D)==(97*q*q,-17*q**3,528*q**6)
supplied_identical=(r/'supplied_rerun.txt').read_bytes()==(r/'PK66/03_arithmetic_receipts/counts_66b1_output.txt').read_bytes()
assert supplied_identical
out={'stage_I_sha256_unchanged':expected,'retained_prime_coverage_checked':len(rows),
 'retained_family_count_checked':len(fam),'family_below4000':sum(z['p']<4000 for z in fam),
 'what_was_not_repeated':'The full 100000-bound point count was retained, not rerun. All stored rows, exact sieve coverage, characters, valuations, traces, model agreement, and criterion consistency were rechecked. Only p=5,19 were newly point-counted by literal pair enumeration.',
 'new_literal_controls':literal,'new_minimal_twist_identity':'verified symbolically',
 'new_minimal_twist_invariants':{'c4':str(c4),'c6':str(c6),'Delta':str(D)},
 'supplied_prior_rerun_matches_supplied_output':supplied_identical,'exceptions':[]}
(root/'CONTINUATION_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
assert hashlib.sha256(freeze.read_bytes()).hexdigest()==expected
print(json.dumps(out,indent=2))
