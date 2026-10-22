#!/usr/bin/env python3
"""Independent companion-matrix check of exact norm-one trace computations."""
from pathlib import Path
from fractions import Fraction
import json,time
import sympy as s
R=Path(__file__).resolve().parents[1]
cs=json.loads((R/'inputs/seed_polynomial.json').read_text())['G_coefficients']
f=[]
for a in cs[:-1]: f.extend([a,0])
f.append(cs[-1]); n=len(f)-1
C=s.zeros(n)
for i in range(n-1): C[i+1,i]=1
for i in range(n): C[i,n-1]=-f[n-i]
I=s.eye(n); C2=C*C

def matrix_trace(a,b,c):
    D=a*I+b*C2-c*C
    N=a*I+b*C2+c*C
    inv=D.inv(method='DM')
    assert D*inv==I
    U=N*inv
    # tau(w)=-w, represented here by changing signs of c; product must be 1.
    tauU=D*N.inv(method='DM')
    assert U*tauU==I
    return s.trace(U)
start=time.monotonic()
rational=json.loads((R/'results/cayley_rational.json').read_text())
quad=json.loads((R/'results/cayley_quadratic.json').read_text())
# Preselected broad samples, plus every quadratic candidate via a separate 12x12
# computation would duplicate the producer's identity. We instead use the actual
# degree-24 multiplication matrices at these fixed indices.
ixq=[0,1,6,19,47,87,141,209,len(quad)-1]
ixr=[0,1,15,255,2047,5000,10000,len(rational)-1]
checks=[]
for kind, rows, indices in [('rational',rational,ixr),('quadratic',quad,ixq)]:
    for i in indices:
        row=rows[i]
        if kind=='rational':
            # Producer uses (b*w+a)/(b*w-a); its negative equals
            # (a+b*w)/(a-b*w), so reverse sign of the matrix trace.
            tr=-matrix_trace(row['a'],0,row['b'])
        else:
            tr=matrix_trace(row['a'],row['b'],row['c'])
        expected=s.Rational(int(row['numerator']),int(row['denominator']))
        assert tr==expected,(kind,i,tr,expected)
        assert s.denom(tr)>1
        checks.append({'family':kind,'index':i,'matrix_trace_matches':True})
# Positive and negative controls with a complete characteristic polynomial.
t=s.symbols('t')
Csmall=s.Matrix([[0,2],[1,0]])
unit=(Csmall+s.eye(2))*(Csmall-s.eye(2)).inv()
assert unit.charpoly(t).as_expr()==t*t-6*t+1
nonunitC=s.Matrix([[0,6],[1,0]])
nu=(nonunitC+s.eye(2))*(nonunitC-s.eye(2)).inv()
assert s.trace(nu)==s.Rational(14,5)
result={'status':'PASS_INDEPENDENT_COMPANION_MATRIX_SAMPLES','checks':checks,
        'sample_count':len(checks),'full_degree':24,
        'positive_control_characteristic_polynomial':str(unit.charpoly(t).as_expr()),
        'negative_control_trace':'14/5','elapsed_seconds':time.monotonic()-start,
        'scope':'17 matrix samples, not independent replay of all 20452 source traces; no class completeness assertion'}
(R/'results/CAYLEY_INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
