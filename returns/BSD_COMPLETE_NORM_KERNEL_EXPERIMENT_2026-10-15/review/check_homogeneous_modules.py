#!/usr/bin/env python3
"""Exact finite module and symbolic controls, not global seed arithmetic."""
import json
from pathlib import Path
import sympy as s

def rank(a, p):
    a = [[v % p for v in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [v * inv % p for v in a[r]]
        for k in range(len(a)):
            if k != r:
                c = a[k][j]
                a[k] = [(x-c*y) % p for x,y in zip(a[k], a[r])]
        r += 1
    return r

rows = []
for p in [3,5,7,11,13]:
    reps = [(1,t) for t in range(p)] + [(0,1)]
    points = [(x,y) for x in range(p) for y in range(p) if x or y]
    def basis_value(j, x, y):
        scale = x if x else y
        rep = (1, y*pow(x,-1,p)%p) if x else (0,1)
        return scale if rep == reps[j] else 0
    def norm_row(phi):
        return [sum(basis_value(j,x,y) for x,y in points
                    if (phi[0]*x+phi[1]*y)%p == 1)%p
                for j in range(p+1)]
    mat = [norm_row(phi) for phi in reps]
    assert rank(mat,p) == p-1
    # Linear functions form the whole two-dimensional geometric kernel.
    linear = [[v[i] for v in reps] for i in range(2)]
    assert rank(linear,p) == 2
    assert all(sum(a*b for a,b in zip(row,f))%p == 0
               for row in mat for f in linear)
    count = 0
    for a in range(1,p):
        for i,phi in enumerate(reps):
            scaled = tuple(a*x%p for x in phi)
            # N functions have degree -1 on dual coordinates.
            assert norm_row(scaled) == [pow(a,-1,p)*v%p for v in mat[i]]
            # Actual action includes det(aI)=a^2, so its central weight is +1.
            assert [(a*a)*v%p for v in norm_row(scaled)] == [a*v%p for v in mat[i]]
            count += 1
    rows.append(dict(p=p, source_dimension=p+1, norm_rank=p-1,
                     kernel_dimension=2, scalar_line_checks=count))

a,m=s.symbols('a m', nonzero=True)
b=(m**8+2*a*m**4-a**2/3)/(4*m**2)
P=2*m**4/3+2*a
Q=-20*m**6/27-4*a*m**2/3+4*b
root=(a+3*m**4)*(3*a+m**4)/(18*m**2)
assert s.cancel(Q**2/4+P**3/27-root**2)==0
terms=[s.factor(-Q/2+root),s.factor(-Q/2-root)]
expected=[(3*a+m**4)**2/(27*m**2),-8*m**2*(3*a+m**4)/27]
assert all(s.cancel(x-y)==0 for x,y in zip(terms,expected))
h=m**2*(m**4+3*a)
assert s.expand(h.subs(m,-m)-h)==0
out={"status":"PASS", "scope":"finite geometric modules and formal Cardano identities only; no number-field or seed computation", "module_checks":rows,
     "cardano_terms":[str(s.factor(x)) for x in terms], "cardano_even_class":str(h),
     "sympy_version":s.__version__}
print(json.dumps(out,indent=2,sort_keys=True))
