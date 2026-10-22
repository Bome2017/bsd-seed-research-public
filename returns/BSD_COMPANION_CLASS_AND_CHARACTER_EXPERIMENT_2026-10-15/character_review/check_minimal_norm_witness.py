"""Independent direct-product extraction of one actual candidate's norm residue.
Does not read NORM_UPPER.json, use its logarithms, or use producer group functions.
Actual global unit identity is separately authenticated in p5_arithmetic.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
F,XP,YP,SIG,UNITS=json.loads((R/'p5_norm_upper/eval_data.json').read_text())
splits=json.loads((R/'p5_norm_upper/split_primes.json').read_text())
q=1831; roots=dict(splits)[q]
assert all(q%d for d in range(2,44))
def val(A,r):
    cs,d=A
    assert d%q
    return sum((c%q)*pow(r,j,q) for j,c in enumerate(cs))*pow(d,-1,q)%q
assert len(roots)==24 and len(set(roots))==24
assert all(sum(c*pow(r,i,q) for i,c in enumerate(F))%q==0 for r in roots)
points=[(val(XP,r),val(YP,r)) for r in roots]
assert len(set(points))==24
assert all((y*y+y-x*x*x-x*x+2*x)%q==0 for x,y in points)
# Work instead with Y=2y+1. The short vertical reflection is Y -> -Y.
P=[(x,(2*y+1)%q) for x,y in points]
def plus(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,Y=P;z,Z=Q
    if x==z and (Y+Z)%q==0:return None
    slope=((3*x*x+2*x-2)*pow(Y,-1,q) if P==Q else (Z-Y)*pow(2*(z-x),-1,q))%q
    w=(slope*slope-x-z-1)%q
    return w,(2*slope*(x-w)-Y)%q

def times(P,n):
    Q=None
    for _ in range(n):Q=plus(Q,P)
    return Q
assert all(times(t,5) is None for t in P)
first=P[0];line={times(first,a) for a in range(5)}
second=next(t for t in P if t not in line)
coordinates={plus(times(first,a),times(second,b)):(a,b) for a in range(5) for b in range(5)}
assert len(coordinates)==25
index={t:i for i,t in enumerate(P)}
assert all(P[roots.index(val(SIG,r))]==times(P[i],2) for i,r in enumerate(roots))
# The affine line through first basis vector with first coordinate one.
coset=[index[t] for t,(a,b) in coordinates.items() if a==1]
assert len(coset)==5
j=8
raw=[]
for r in roots:
    x=1
    for A,e in UNITS[j]:
        a=val(A,r);assert a
        x=x*pow(a,int(e),q)%q
    raw.append(x)
coeff=[pow(4,-1,5)*pow(pow(2,k,5),-1,5)%5 for k in range(4)]
assert coeff==[4,2,1,3]
projected=[]
for t in P:
    z=1
    for k,c in enumerate(coeff):z=z*pow(raw[index[times(t,pow(2,k,5))]],c,q)%q
    projected.append(z)
# Direct product, followed by a fifth-power-residue test. No discrete-log sum.
witness=1
for i in coset:witness=witness*projected[i]%q
residue=pow(witness,(q-1)//5,q)
assert pow(residue,5,q)==1 and residue!=1
# It really is the chi=omega component as a mod-fifth-power class.
assert all(pow(projected[index[times(t,2)]]*pow(projected[i],-2,q)%q,(q-1)//5,q)==1 for i,t in enumerate(P))
result={'status':'PASS','q':q,'candidate_zero_based':j,'candidate_one_based':j+1,'point_basis_original_coordinates':[points[index[first]],points[index[second]]], 'coset_indices':coset,'coset_points':[points[i] for i in coset], 'projector_coefficients':coeff,'projected_values_on_coset':[projected[i] for i in coset], 'norm_product_mod_q':witness,'fifth_power_residue':residue,'conclusion':'incidence norm of this projected candidate is not a fifth power, conditional only on its authenticated global unit identity and field source','input_sha256':hashlib.sha256((R/'p5_norm_upper/eval_data.json').read_bytes()).hexdigest(),'not_inputs':['NORM_UPPER.json','known Sha','computed class group','fundamental-unit completeness']}
Path(__file__).with_name('MINIMAL_NORM_WITNESS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
