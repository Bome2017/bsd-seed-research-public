#!/usr/bin/env python3
"""Two exact evaluations of C11 from the existing certified symbol pipeline.

Only one digit of the infinite L-function is claimed. Higher precision is
used internally for the finite depth-two measure, never confused with it.
"""
from pathlib import Path
from fractions import Fraction
from math import comb
import hashlib, json, struct, sys

root=Path(__file__).resolve().parent
replay=sys.argv[1:]==['--check-p7']
assert not sys.argv[1:] or replay
p=7 if replay else 11
run=(root.parent/'p7' if replay else root)/'run'
k=20; modulus=p**k
checks=[]

def check(ok,name):
    checks.append({'name':name,'passed':bool(ok)})
    if not ok: raise AssertionError(name)
def read_symbols(m):
    pos,neg={},{}
    for line in (run/f'SYMBOLS_m{m}.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'): continue
        b,a,c=line.split(); b=int(b)
        check(b not in pos,f'unique row b={b} at denominator {m}')
        pos[b],neg[b]=Fraction(a),Fraction(c)
    return pos,neg
def residue(q,mod=modulus):
    q=Fraction(q)
    assert q.denominator%p
    return q.numerator*pow(q.denominator,-1,mod)%mod

high,nhigh=read_symbols(p*p)
low,nlow=read_symbols(p)
primes=[n for n in range(2,p+1) if all(n%d for d in range(2,int(n**.5)+1))]
with (run/'ap/ap_000000.bin').open('rb') as f:
    ap=struct.unpack('<'+'i'*len(primes),f.read(4*len(primes)))[-1]
card=1+sum(y*y%p==(x**3-22735*x*x+106272484*x)%p for x in range(p) for y in range(p))
check(card==(10 if replay else 14) and ap==p+1-card==-2,'point count agrees with verified coefficient')
for m,pos,neg in [(p*p,high,nhigh),(p,low,nlow)]:
    check(set(pos)==set(neg)=={b for b in range(1,m) if b%p},f'complete unit symbols at {m}')
    check(all(pos[b]==pos[m-b] and neg[b]==-neg[m-b] for b in pos),f'conjugation at {m}')
    check(all((1024*x).denominator==1 and x.denominator%p for x in [*pos.values(),*neg.values()]),f'lattice and p-integrality at {m}')
check(sum(low.values())==0,'Hecke relation at zero cusp')
check(all(ap*l[c]==sum(h[c+p*j] for j in range(p))
          for h,l in [(high,low),(nhigh,nlow)] for c in l),'all two-level Hecke relations for both signs')

# Route A: integer Fermat quotients, with no p-adic root or Teichmuller lift.
weights={}
for b in high:
    fq=(pow(b,p-1,p*p)-1)//p
    j=fq*pow(p-1,-1,p)%p
    weights[b]=pow(ap%p,-2,p)*comb(j,2)%p
full=sum(weights[b]*high[b] for b in high)
route_a=residue(full,p)
groups=({5:[2,4,11,13,22,23],4:[6,9,10,15,16,24],3:[12,17,20]} if replay else
        {2:[2,6,18,41,54],3:[5,14,15,17,25,32,42,45,46,51],
         5:[8,20,24,26,43,47,49,56,59,60],6:[10,16,23,28,30,31,35,37,48,52],
         7:[7,19,21,29,34,38,50,53,57,58]})
declared={b:w for w,bs in groups.items() for b in bs}
folded_weights={b:(weights[b]+weights[p*p-b])%p for b in high if b<(p*p)/2}
check({b:w for b,w in folded_weights.items() if w}==declared,'predeclared folded formula exactly matches all weights')
folded=sum(w*sum(high[b] for b in bs) for w,bs in groups.items())
check(residue(folded,p)==route_a,'folded and unfolded Fermat-quotient residues agree')

# Route B: finite depth-two measure, keeping its lower-level contribution.
alpha=ap%p
for _ in range(2*k):
    alpha=(alpha-(alpha*alpha-ap*alpha+p)*pow(2*alpha-ap,-1,modulus))%modulus
check((alpha*alpha-ap*alpha+p)%modulus==0 and alpha%p==ap%p,'Hensel unit root')
omega={a:pow(a,p**k,modulus) for a in range(1,p)}
check(all(pow(w,p-1,modulus)==1 and w%p==a for a,w in omega.items()),'Teichmuller lifts')
ia=pow(alpha,-1,modulus); coef=[0,0,0]; correction_total=0; seen=[]
for a,w in omega.items():
    for j in range(p):
        b=w*pow(1+p,j,p*p)%(p*p); seen.append(b)
        check(weights[b]==pow(ap%p,-2,p)*comb(j,2)%p,f'independent exponent at b={b}')
        correction=ia**3*residue(low[b%p])%modulus
        measure=(ia**2*residue(high[b])-correction)%modulus
        for degree in range(3): coef[degree]=(coef[degree]+measure*comb(j,degree))%modulus
        correction_total=(correction_total+correction*comb(j,2))%modulus
check(sorted(seen)==sorted(high),'each unit at depth two occurs once')
check(coef[0]==0,'finite P2 constant term is zero')
check(coef[1]%p==0,'finite P2 linear term vanishes modulo p')
check(correction_total%p==0 and sum(comb(j,2) for j in range(p))==(35 if replay else 165),'lower-level quadratic contribution vanishes modulo p')
check(coef[2]%p==route_a,'two independent coefficient evaluations agree')
if replay:
    check(route_a==1 and str(folded)=='-1931','matches retained p7 result exactly')
    print(json.dumps({'status':'P7_REGRESSION_PASS','residue':route_a,'folded':str(folded),'checks':len(checks)}))
    sys.exit(0)

answer={'status':'P11_COEFFICIENT_UNIT_PROVED' if route_a else 'P11_UNIT_TEST_INCONCLUSIVE',
 'p':p,'a11':ap,'point_count_F11':card,'finite_P2_precision_exponent':k,
 'finite_P2_coefficients_mod_11pow20':coef,'infinite_L11_leading_coefficient_certified_digits':1,
 'residue_omega1':route_a,'residue_neron_full_period':route_a*pow(2,-1,p)%p,
 'folded_exact_integer_or_rational':str(folded),'lower_contribution_mod_11':correction_total%p,
 'alpha_mod_121':alpha%121,'all_checks_passed':all(c['passed'] for c in checks),'checks':checks,
 'symbol_file_sha256':{f'SYMBOLS_m{m}.txt':hashlib.sha256((run/f'SYMBOLS_m{m}.txt').read_bytes()).hexdigest() for m in [121,11]},
 'plus_symbols_121':{str(b):str(q) for b,q in sorted(high.items())},
 'plus_symbols_11':{str(b):str(q) for b,q in sorted(low.items())},
 'folded_weights':{str(b):w for b,w in sorted(declared.items())}}
tmp=root/'DOWNSTREAM.json.tmp'; tmp.write_text(json.dumps(answer,indent=2)+'\n'); tmp.replace(root/'DOWNSTREAM.json')
print(json.dumps({k:v for k,v in answer.items() if k not in ['checks','plus_symbols_121','plus_symbols_11','folded_weights']},indent=2))
