"""Exact construction of the Fisher Thm 5.3 quintic for d=43737.
Run with the retained sage-env Python. No Selmer or solubility assertion is
inferred merely from these symbolic checks.
"""
from sage.all import QQ, PolynomialRing, matrix, EllipticCurve, NumberField
import json
from pathlib import Path
out=Path(__file__).parent
P=PolynomialRing(QQ,names=['x0','x1','x2','x3','x4']); x0,x1,x2,x3,x4=P.gens()
d,r,s,lam=43737,1464,7,11
norm=r*r-d*s*s
M=matrix(P,5)
entries={(0,1):lam*x0,(0,2):d*(x2-x4),(0,3):-x1+x3,(0,4):-x3,
         (1,2):-x1-x3,(1,3):x2+x4,(1,4):x4,(2,3):norm*x0,
         (2,4):r*x1+s*d*x2,(3,4):s*x1+r*x2}
for (i,j),a in entries.items(): M[i,j]=a;M[j,i]=-a
q=[]
for i in range(5):
    inds=[j for j in range(5) if j!=i]; A=M.matrix_from_rows_and_columns(inds,inds)
    q.append((-1)**i*(A[0,1]*A[2,3]-A[0,2]*A[1,3]+A[0,3]*A[1,2]))
assert matrix(P,1,5,q)*M==0
K=NumberField(PolynomialRing(QQ,'t').gen()**2-d,'a');a=K.gen()
theta=(r+s*a)/(r-s*a)
assert theta==23423+112*a and theta.norm()==1
C=EllipticCurve([1-lam,-lam,-lam,-5*lam*(lam**2+2*lam-1),-lam*(lam**4+10*lam**3-5*lam**2+15*lam-1)])
D=EllipticCurve([1-lam,-lam,-lam,0,0])
Cmin=C.minimal_model(); Dmin=D.minimal_model()
assert list(Cmin.a_invariants())==[0,-1,1,-7820,-263580]
assert list(Dmin.a_invariants())==[0,-1,1,-10,-20]
Cd=C.quadratic_twist(d).minimal_model();Dd=D.quadratic_twist(d).minimal_model()
assert list(Cd.a_invariants())==[0,0,1,-14959712463303,-22270654620235278500]
assert list(Dd.a_invariants())==[0,0,1,-19766893413,-1937478573143510]
I=P.ideal(q)
hilbert=str(I.hilbert_polynomial())
result={"lambda":lam,"d":d,"r":r,"s":s,"norm_alpha":norm,"theta":str(theta),
 "matrix":[[str(v) for v in row] for row in M.rows()],"signed_pfaffians":[str(v) for v in q],
 "syzygy_qM_zero":True,"C_minimal_ainvs":[int(v) for v in Cmin.a_invariants()],
 "D_minimal_ainvs":[int(v) for v in Dmin.a_invariants()],
 "Jacobian_twist_F":[int(v) for v in Cd.a_invariants()],"base_twist_A":[int(v) for v in Dd.a_invariants()],
 "hilbert_polynomial":hilbert,"solubility_status":"NOT_CHECKED_BY_THIS_SCRIPT", "nontrivial_Sha_status":"NOT_CHECKED_BY_THIS_SCRIPT"}
(out/'FISHER_MODEL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
