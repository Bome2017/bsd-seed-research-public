from sage.all import *
from pathlib import Path
import json
q=1783
pol=PolynomialRing(GF(q),'X'); X=pol.gen()
for c in range(1,q):
    f=X**4+X+c
    if f.is_irreducible(): break
K=GF(q**4,'a',modulus=f); a=K.gen()
E=EllipticCurve(K,[0,-1,0,-66020924,-65074271436])
O=E(0)
def vec(x): return [int(z) for z in K(x).list()]+[0]*(4-len(K(x).list()))
def coords(P): return None if P==O else [vec(P[0]),vec(P[1])]
def frob(P): return O if P==O else E(P[0]**q,P[1]**q)
T=[]
for x,mul in E.division_polynomial(5).roots():
    for P in E.lift_x(x,all=True):
        assert 5*P==O
        T.append(P)
assert len(T)==24
T=sorted(T,key=lambda P:coords(P))
S=next(P for P in T if frob(P)==3*P)
T1=E(1591,1089); assert frob(T1)==T1 and T1.weil_pairing(S,5)!=1
R=E(3,872); P1=E(535,1095);P2=E(1172,1589)
def miller5(P,Q):
    # Independent line/tangent evaluation for y²=x³-x²+a4*x+a6.
    def g(A,B):
        if A==-B:return Q[0]-A[0]
        lam=(3*A[0]**2-2*A[0]+E.a4())/(2*A[1]) if A==B else (B[1]-A[1])/(B[0]-A[0])
        C=A+B
        return (Q[1]-A[1]-lam*(Q[0]-A[0]))/(Q[0]-C[0])
    V=P; value=K(1)
    for bit in bin(5)[3:]:
        value=value**2*g(V,V);V=2*V
        if bit=='1':value=value*g(V,P);V+=P
    assert V==O
    return value**((q**4-1)//5)
values=[]
for P in [R,P1,P2]:
    s=S.tate_pairing(P,5,4,q=q);m=miller5(S,P);assert s==m
    values.append(s)
assert values[0]!=1 and values[0]**5==1 and values[1:]==[K(1),K(1)]
# Test all scalar multiples without introducing possible Miller zero/pole values.
scalar_checks=0
for i in range(1,5):
 for j in range(1,5):
    got=(i*S).tate_pairing(j*R,5,4,q=q)
    assert got==values[0]**(i*j);scalar_checks+=1
out={'status':'PASS','q':q,'p':5,'field_polynomial':str(f),'frobenius_eigen3_point':coords(S),'rational_order5_point':coords(T1),'weil_pairing':vec(T1.weil_pairing(S,5)),'R':coords(R),'reduced_Tate_values_R_P1_P2':[vec(z) for z in values],'normalized_exponents':[1,0,0],'full_torsion_points_checked':len(T),'bilinearity_checks':scalar_checks,'global_dual_class_constructed':False}
p=Path(__file__).parent/'RESULT.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
