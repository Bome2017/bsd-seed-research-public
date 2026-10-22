from sage.all import *
from pathlib import Path
import json
root=Path(__file__).parent
r=json.loads((root/'RESULT.json').read_text());q=ZZ(r['q']);P=PolynomialRing(GF(q),'X');X=P.gen();K=GF(q**4,'a',modulus=X**4+X+3);a=K.gen()
def el(v):return sum(K(z)*a**i for i,z in enumerate(v))
E=EllipticCurve(K,[0,-1,0,-66020924,-65074271436]);T=E(1591,1089);S=E([el(v) for v in r['frobenius_eigen3_point']]);assert E(S[0]**q,S[1]**q)==3*S
R=PolynomialRing(K,'Y');Y=R.gen();h=prod(Y-(T+j*S)[1] for j in range(5));assert all(z**q==z for z in h)
coeff=[int(z) for z in h];print(coeff)
# Assuming simple valuation1 at the5 selected points, compare inertia profiles.
pts=[(i,j) for i in range(5) for j in range(5) if (i,j)!=(0,0)]
def projected(mask,i,j):return sum(e*mask((pow(2,k,5)*i)%5,(pow(2,k,5)*j)%5) for k,e in enumerate([1,3,4,2]))%5
old=lambda i,j:int((i,j)==(1,0));new=lambda i,j:int(i==1)
prof_old={v:projected(old,*v) for v in pts};prof_new={v:projected(new,*v) for v in pts}
lines=[[(i,j) for i,j in pts if (u*i+v*j)%5==1] for u,v in pts]
def defects(prof):return [sum(prof[P] for P in L)%5 for L in lines]
assert any(defects(prof_old));assert not any(defects(prof_new));assert all(prof_new[i,j]==i for i,j in pts)
out={'q':int(q),'h_ascending_coefficients':coeff,'affine_line_size':5,'scalar_projection_weights':[1,3,4,2],'old_line_defects':defects(prof_old),'new_line_defects':defects(prof_new),'new_profile_equals_first_coordinate':True,'valuation_hypothesis':'Each of the five selected points has valuation1; exact resultant norm valuation5 is required to certify this.','global_incidence_norm_verified':False}
(root/'LINE_SOURCE.json').write_text(json.dumps(out,indent=2)+'\n')
