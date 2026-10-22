"""Exact controls for the new lattice/height deduction; no seed values.

Independent of the uploaded implementation. Only rational 2-by-2 arithmetic
is used. Source matching of actual heights or Kato coefficients is not tested.
"""
from fractions import Fraction as F
import json
from pathlib import Path

def vp(x, p):
    x = F(x)
    if x == 0:
        return float('inf')
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v

def content(v, p):
    return min(vp(x, p) for x in v)

def apply(H, x):
    return [sum(F(a)*b for a,b in zip(row,x)) for row in H]

def run():
    rows = []
    for p in [5, 7, 17]:
        for w in [0, 2]:
            for b0 in [0, 2]:
                # Both point logarithms can be nonprimitive.
                L = [F(p**(w+1)), F(2*p**(w+1))]
                q = [-L[1]/p**(w+1), L[0]/p**(w+1)]
                assert content(q,p) == 0
                assert sum(x*y for x,y in zip(L,q)) == 0
                H = [[F(p**b0), F(0)], [F(0), F(p**(b0+1))]]
                det = H[0][0]*H[1][1]-H[0][1]**2
                adj = [[H[1][1],-H[0][1]],[-H[1][0],H[0][0]]]
                b = content(apply(H,q),p)
                c = content(apply(adj,L),p)
                r = vp(det,p)
                assert c == b+1+w
                # Splitting changes by a multiple of L tensor L cancel on q.
                for t in [F(1),F(1,p**5)]:
                    shifted = [[H[i][j]+t*L[i]*L[j] for j in range(2)] for i in range(2)]
                    assert apply(shifted,q) == apply(H,q)
                for gap in [0,1,2]:
                    K = F(p**(r+gap))
                    delta = [K*x/(p*det) for x in apply(adj,L)]
                    m = content(delta,p)
                    assert m-w-b == vp(K,p)-r == gap
                    assert sum(x*y for x,y in zip(apply(H,q),delta)) == 0
                    rows.append({'p':p,'w':w,'b':b,'m':m,'r':r,'K_valuation':vp(K,p),'corrected_gap':gap})
    # A singular height still has a meaningful restricted Bockstein row.
    H = [[F(1),F(0)],[F(0),F(0)]]
    assert apply(H,[-2,1]) == [-2,0]
    # A non-p height-one omission invalidates subtraction.
    # D=(0,U(U+p^k)), eta=(1,0), z=U eta: all conditions except
    # divisibility at (U+p^k); m=tau=0 and b=k, not m=tau+b+e>=b.
    omitted = {'D':'(0,U*(U+p^2))','g':'1','m':0,'tau':0,'b':2,
               'failed_height_one':'(U+p^2)','claimed_corrected_bound':-2}
    # Source defect need not be visible at (p): g=U+p^k has v_(p)=0,
    # but its nonzero augmentation has p-valuation k.
    defect = {'D':'(0,U)','g':'U+p^2','v_height_one_p_g':0,'e':2}
    out={'status':'PASS','height_cancellation_cases':len(rows),
         'source_and_height_arithmetic_authenticated':False,
         'actual_seed_values_computed':0,'cases':rows,
         'non_p_height_one_negative_control':omitted,
         'augmentation_defect_control':defect,
         'singular_height_control':'restricted row nonzero; determinant ratio not defined'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))

if __name__=='__main__':
    run()
