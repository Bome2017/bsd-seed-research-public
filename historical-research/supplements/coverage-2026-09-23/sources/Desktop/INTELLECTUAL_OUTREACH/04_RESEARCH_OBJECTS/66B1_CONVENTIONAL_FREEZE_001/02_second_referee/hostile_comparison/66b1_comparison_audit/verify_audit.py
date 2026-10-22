"""Independent, non-mutating audit of retained receipts and fresh point counts.
Run from anywhere: python verify_audit.py. Requires sympy for exact identities.
"""
from pathlib import Path
import csv, hashlib, json
from datetime import datetime, timezone
import sympy as s
ROOT=Path(__file__).resolve().parent
R=ROOT/'first_model_receipts'; T=R/'retained'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def leg(a,p):
    r=pow(a%p,(p-1)//2,p)
    return -1 if r==p-1 else r
def v2(n):
    if n<=0: raise ValueError('positive n required')
    return (n & -n).bit_length()-1
report={'checked_utc':datetime.now(timezone.utc).isoformat()}
checks={}
for parent,fn in [(R,'CONTINUATION_MANIFEST.json'),(T,'MANIFEST.json')]:
    manifest=json.loads((parent/fn).read_text())
    entries=manifest.get('files',manifest)
    checks[fn]={'entries':len(entries),'mismatches':[name for name,h in entries.items() if not (parent/name).exists() or sha(parent/name)!=h]}
for name in ['PRE_COMPARISON_RECONSTRUCTION.md','STAGE_II_LOCAL_DESCENT.md']:
    checks[name]={'sha256':sha(T/name),'matches_attachment':(T/name).read_bytes()==(ROOT/'supplied_inputs'/name).read_bytes()}
freeze=json.loads((T/'STAGE_I_FREEZE.json').read_text())
checks['freeze_receipt']=freeze
checks['opening_receipt']=json.loads((T/'STAGE_II_OPEN.json').read_text())
frozen=ROOT/'frozen_referee'/'FROZEN_PRE_COMPARISON_RECONSTRUCTION.md'
checks['referee_frozen_record']={'sha256':sha(frozen),'unchanged':sha(frozen)=='2a627f6574cf20f2a9f63f42dc8b19c4173985d902fa0762df7c562b105a27a4'}
report['custody']=checks
rows=list(csv.DictReader((T/'independent_counts.csv').open()))
fresh=list(csv.DictReader((ROOT/'referee_counts.csv').open()))
expected=list(s.primerange(5,100000));expected.remove(11)
assert [int(r['p']) for r in rows]==expected
assert [int(r['p']) for r in fresh]==expected
mismatch=[];criterion_errors=[];metadata_errors=[];family=[]
for r,f in zip(rows,fresh):
    p=int(r['p']); n=int(f['N_min']); c=int(f['N_descent'])
    if n!=c or n!=int(r['N_min']) or c!=int(r['N_descent']):mismatch.append(p)
    predicted=leg(-2,p)==-1 and leg(33,p)==-1
    if (v2(n)==2)!=predicted:criterion_errors.append(p)
    fam=p%8==5 and leg(p,3)==-1 and leg(p,11)==1
    if fam:family.append(p)
    actual={'trace':p+1-n,'v2':v2(n),'chi2':leg(2,p),'chi_neg2':leg(-2,p),'chi33':leg(33,p),'p_mod8':p%8,'q_over3':leg(p,3),'q_over11':leg(p,11),'family':int(fam)}
    for k,val in actual.items():
        if int(r[k])!=val:metadata_errors.append((p,k))
report['fresh_counts']={'algorithm':'Direct Horner/cubic polynomial evaluation and literal square-residue multiplicity; not the supplied finite differences', 'exclusive_bound':100000,'good_primes':len(rows),'family_primes':len(family),'family_below_4000':sum(p<4000 for p in family),'count_mismatches':mismatch,'criterion_counterexamples':criterion_errors,'metadata_errors':metadata_errors,'small_counts':{f['p']:f['N_min'] for f in fresh if int(f['p']) in [5,7,19]}}
# Symbolic identities are checked independently of numerical tables.
x,y,q,U,V,z,t=s.symbols('x y q U V z t')
f=x**3+17*x*x+64*x
Q=s.expand((x*x-64)**2+32*f)
factors=(x*x+(16+4*t)*x+64)*(x*x+(16-4*t)*x+64)
reduced=s.rem(s.expand(factors-Q),t*t+2,t)
A=(17*q-1)/4
E=z*z+x*z-x**3-A*x*x-4*q*q*x
M=V*V+U*V+V-U**3-(5*q-1)*U*U/4+(3*q*q+1)*U/2+(3*q**3+1)/4
base=y*y+x*y+y-x**3-x*x+2*x+1
X=4*(x-1);Y=8*y+4*x+4
model=s.expand(Y*Y-X**3-17*X**2-64*X-64*base)
Xq=4*(U-q);Yq=8*V+4*U+4
cont=s.expand(Yq**2-Xq**3-17*q*Xq**2-64*q*q*Xq-64*M)
equiv=s.simplify(E.subs({x:U-q,z:V+(q+1)/2})-M)
polycheck={'base_model_identity':model==0,'continuation_model_identity':cont==0,'two_minimal_models_integrally_equivalent':equiv==0,'halving_factorization_mod_s_squared_plus_2':reduced==0,'expanded_halving_quartic':str(Q),'exceptional_values':{str(v):int(Q.subs(x,v)) for v in [0,8,-8]},'discriminant_product':str(s.rem(s.expand((-32+128*t)*(-32-128*t)),t*t+2,t))}
for k in ['base_model_identity','continuation_model_identity','two_minimal_models_integrally_equivalent','halving_factorization_mod_s_squared_plus_2']:assert polycheck[k]
report['symbolic']=polycheck
report['integral_residue_checks']={'phi_d3_mod16':{str(a):{'even':sorted({(3-34*a*b*b+11*a*a*b**4)%16 for b in range(0,16,2)}),'odd':sorted({(3-34*a*b*b+11*a*a*b**4)%16 for b in range(1,16,2)})} for a in [5,13]},'dual_dminus1_mod3_q2':sorted({(-1+34*b*b-256*b**4)%3 for b in range(3)})}
assert not mismatch and not criterion_errors and not metadata_errors
assert all(not v['mismatches'] for k,v in checks.items() if k.endswith('MANIFEST.json'))
(ROOT/'AUDIT_VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
