from sage.all import *
from pathlib import Path
import json,time
root=Path(__file__).resolve().parent
t0=time.monotonic();B=BrandtModule(3,847);h=B.dimension();print('DIM',h,flush=True)
E=EllipticCurve(QQ,[1,1,1,3,12]);QW=QQ**h;FW=GF(5)**h;rows=[];matrices=[]
for q in [2,13,17,19,23,29,31]:
 t=time.monotonic();T=B.hecke_matrix(q).change_ring(ZZ);a=E.ap(q)
 QW=QW.intersection((T-a).right_kernel());FW=FW.intersection((T-a).change_ring(GF(5)).right_kernel())
 print('q',q,'a',a,'dims',QW.dimension(),FW.dimension(),'sec',time.monotonic()-t,flush=True)
 rows.append({'q':q,'a_q':int(a),'Q_dimension':int(QW.dimension()),'F5_dimension':int(FW.dimension())})
 matrices.append({'q':q,'matrix':[list(map(int,r)) for r in T.rows()]})
 if QW.dimension()==1 and FW.dimension()==1:break
assert QW.dimension()==FW.dimension()==1
v=QW.basis()[0];v*=v.denominator();v/=gcd(list(v));v=vector(ZZ,v)
if next(c for c in v if c)!=abs(next(c for c in v if c)):v=-v
print('VECTOR',v,flush=True)
weights=list(B.monodromy_weights());print('WEIGHTS',weights,flush=True)
result={'status':'BASE_MOD5_HEKKE_QUOTIENT_RANK_ONE','h':int(h),'rows':rows,'primitive_right_eigenvector':list(map(int,v)),'weights':list(map(str,weights)),'elapsed_seconds':time.monotonic()-t0}
(root/'BASE_BRANDT.json').write_text(json.dumps(result,indent=2)+'\n')
import gzip
with gzip.open(root/'BASE_BRANDT_MATRICES.json.gz','wt') as f:json.dump(matrices,f)
