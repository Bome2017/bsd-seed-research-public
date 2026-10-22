"""Small independent group-algebra checks; no elliptic-curve arithmetic."""
from itertools import product, combinations_with_replacement
from fractions import Fraction
import json
from pathlib import Path


def rank_mod_p(rows, p):
    basis = {}
    for original in rows:
        row = [x % p for x in original]
        for j in sorted(basis):
            if row[j]:
                a = row[j]
                row = [(x - a*y) % p for x,y in zip(row,basis[j])]
        lead = next((i for i,x in enumerate(row) if x), None)
        if lead is not None:
            u = pow(row[lead], -1, p)
            basis[lead] = [(u*x) % p for x in row]
    return len(basis)


def augmentation_power_rank(p, orders, degree):
    group = list(product(*(range(q) for q in orders)))
    index = {g:i for i,g in enumerate(group)}
    identity = (0,)*len(orders)
    generators = []
    for i in range(len(orders)):
        g = tuple(int(j==i) for j in range(len(orders)))
        generators.append({identity:-1,g:1})
    def mul(v,w):
        ans = {}
        for a,x in v.items():
            for b,y in w.items():
                c = tuple((ai+bi)%q for ai,bi,q in zip(a,b,orders))
                ans[c] = ans.get(c,0)+x*y
        return {g:c%p for g,c in ans.items() if c%p}
    rows = []
    for choice in combinations_with_replacement(range(len(orders)), degree):
        v = {identity:1}
        for j in choice: v = mul(v,generators[j])
        for h in group:
            row = [0]*len(group)
            for a,x in v.items():
                b = tuple((ai+hi)%q for ai,hi,q in zip(a,h,orders))
                row[index[b]] = x
            rows.append(row)
    return rank_mod_p(rows,p)


def finite_depth(x,p,k):
    x %= p**k
    if x==0: return None
    j=0
    while x%p==0:
        x//=p
        j+=1
    return j


def main():
    cases=[]
    for p,orders in [(7,(7,)),(7,(7,7)),(7,(49,)),(3,(3,3,3)),(7,(2,7))]:
        r2=augmentation_power_rank(p,orders,2)
        r3=augmentation_power_rank(p,orders,3)
        n=sum(q%p==0 for q in orders)
        expected=n*(n+1)//2
        assert r2-r3==expected
        cases.append(dict(p=p,group_orders=orders,rank_I2=r2,rank_I3=r3,dim_gr2=r2-r3,expected=expected))
    checked=0
    for p,k in [(3,2),(5,2),(7,2)]:
        q=p**k
        for a,b in product(range(q),repeat=2):
            d=finite_depth(a*b,p,k)
            if d is not None:
                e=finite_depth(b,p,k)
                assert e is not None and e<=d
            checked+=1
        assert finite_depth(q,p,k) is None
    # Exhaust all ideals in these chain rings: nonzero + A annihilates coker
    # is equivalent to their generator having depth <= v_p(A), including k<=v_p(A).
    chain_cases=0
    for p in [3,5,7]:
        for k in range(1,5):
            for d in range(k+1):
                for v in range(6):
                    q=p**k
                    D={(p**d*x)%q for x in range(q)}
                    D_nonzero=D!={0}
                    killed=all((p**v*x)%q in D for x in range(q))
                    valid=D_nonzero and killed
                    assert valid==(d<k and d<=v)
                    chain_cases+=1
    eps=Fraction(573,100000)
    assert 174*eps<1
    lo,hi=Fraction(3599427,100000)/4,Fraction(3600573,100000)/4
    integers=[n for n in range(7,12) if lo<n<hi]
    assert integers==[9]
    out={
      'grade':'BOUNDED_ALGEBRA_CHECKS_ONLY',
      'augmentation_group_ring_checks':cases,
      'nonzero_product_depth_cases':checked,
      'chain_ring_ideal_cases':chain_cases,
      'rational_reconstruction_margin':str(174*eps),
      'common_B_interval':[str(lo),str(hi)],
      'integer_candidates':[9],
      'elliptic_curve_or_new_prime_computations':False,
      'proves_UC_or_FIN':False,
      'limitation':'Checks finite examples and scalar identities; general proofs and arithmetic imports are in the reports.'
    }
    target=Path(__file__).with_name('FINITE_ALGEBRA_CHECKS.json')
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','group_cases':len(cases),'scalar_cases':checked,'ideal_cases':chain_cases}))

if __name__=='__main__': main()
