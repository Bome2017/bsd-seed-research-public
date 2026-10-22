from sage.all import *
import json
from pathlib import Path
q,p=1783,5
k=GF(q)
R=PolynomialRing(k,'X'); X=R.gen()
E=EllipticCurve(k,[0,-1,0,-66020924,-65074271436])
psi=E.division_polynomial(5)
factors=list(psi.factor())
modulus=next(f for f,m in factors if f.degree()==4)
K=GF(q**4,'a',modulus=modulus); a=K.gen()
EK=E.change_ring(K)
P=EK([1591,1089]); assert p*P==EK(0) and P!=EK(0)
roots=psi.change_ring(K).roots(multiplicities=False)
points=[]
for x in roots:
 for y in (x**3-x**2-K(66020924)*x-K(65074271436)).sqrt(all=True):
  points.append(EK([x,y]))
def frob(T):
 return EK([T[0]**q,T[1]**q]) if T!=EK(0) else T
Q=next(T for T in points if frob(T)==3*T and T!=EK(0))
z=P.weil_pairing(Q,5)
assert z!=1 and z**5==1
assert frob(P)==P and frob(Q)==3*Q
# After defining z=e_5(P,Q), the torsion Weil form is [[0,1],[-1,0]].
# Standard local reciprocity identifies unramified/ramified classes with a,b.
# The H^1 cup-Weil form is symmetric; its hyperbolic matrix is established
# by the primary local duality theorem, not inferred merely by this check.
F=matrix(GF(5),[[1,0],[0,3]])
Weil=matrix(GF(5),[[0,1],[-1,0]])
assert F.transpose()*Weil*F==3*Weil
assert (F-3).right_kernel().basis_matrix()==matrix(GF(5),[[0,1]])
assert (F-1).right_kernel().basis_matrix()==matrix(GF(5),[[1,0]])
# Explicit cocycles on a finite quotient C5(tau) semidirect C20(Frob).
# Coordinates denote Frob^j tau^i, multiplication is verified below.
G=[(j,i) for j in range(20) for i in range(5)]
def mult(g,h):
 j,i=g; k,l=h
 return ((j+k)%20,(pow(3,-k,5)*i+l)%5)
def act(g,v): return (v[0]%5,pow(3,g[0],5)*v[1]%5)
def coc(g,u,v): return (g[0]*u%5,pow(3,g[0],5)*g[1]*v%5)
checks=0
for u,v in [(1,0),(0,1),(1,1)]:
 for g in G:
  for h in G:
   L=coc(mult(g,h),u,v); cg=coc(g,u,v); gh=act(g,coc(h,u,v))
   assert L==((cg[0]+gh[0])%5,(cg[1]+gh[1])%5)
   checks+=1
serialize=lambda x: [int(c) for c in x.polynomial().list()]
out={
 'status':'PASS_EXACT_LOCAL_ARITHMETIC_ONLY',
 'q':q,'p':p,'cardinality':int(E.cardinality()),'trace':int(q+1-E.cardinality()),
 'division_polynomial_factor_degrees':[int(f.degree()) for f,m in factors for _ in range(m)],
 'extension_modulus':[int(c) for c in modulus.list()],
 'torsion_eigenvectors':{'P':[serialize(P[0]),serialize(P[1])], 'Q':[serialize(Q[0]),serialize(Q[1])]},
 'P_frobenius_eigenvalue':1,'Q_frobenius_eigenvalue':3,
 'weil_pairing_coefficients':serialize(z), 'weil_pairing_order':int(z.multiplicative_order()),
 'weil_matrix':[[0,1],[4,0]],
 'H1_tate_matrix_in_normalized_dual_bases':[[0,1],[1,0]],
 'tate_matrix_status':'THEOREM_NORMALIZATION_NOT_A_NUMERICAL_GLOBAL_CLASS',
 'finite_quotient_cocycle_checks':checks,
 'global_obstruction_class_constructed':False,
 'BD_local_eligibility':{'positive_sign':(int(q+1-E.cardinality())-(q+1))%5==0,'q_squared_not_one':(q*q-1)%5!=0,'minus7_inert':kronecker(-7,q)==-1},
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
