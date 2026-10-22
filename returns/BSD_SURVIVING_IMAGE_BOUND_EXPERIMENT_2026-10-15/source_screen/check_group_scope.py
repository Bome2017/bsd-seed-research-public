#!/usr/bin/env python3
"""Exact finite-group checks; no field, Selmer or class-number inputs."""
import itertools, json
from fractions import Fraction
from pathlib import Path

def mm(g,h,p):
 a,b,c,d=g; e,f,i,j=h
 return ((a*e+b*i)%p,(a*f+b*j)%p,(c*e+d*i)%p,(c*f+d*j)%p)
def inv(g,p):
 a,b,c,d=g; z=pow((a*d-b*c)%p,-1,p)
 return (z*d%p,-z*b%p,-z*c%p,z*a%p)
def mv(g,v,p):
 a,b,c,d=g;x,y=v
 return ((a*x+b*y)%p,(c*x+d*y)%p)
def rowmv(v,g,p):
 x,y=v;a,b,c,d=g
 return ((x*a+y*c)%p,(x*b+y*d)%p)
def det(A):
 A=[[Fraction(x) for x in row] for row in A]; ans=Fraction(1)
 for j in range(len(A)):
  k=next(k for k in range(j,len(A)) if A[k][j])
  if k!=j:A[k],A[j]=A[j],A[k];ans=-ans
  d=A[j][j];ans*=d
  for k in range(j+1,len(A)):
   c=A[k][j]/d
   A[k]=[x-c*y for x,y in zip(A[k],A[j])]
 return ans

def one(p):
 G=[g for g in itertools.product(range(p),repeat=4) if (g[0]*g[3]-g[1]*g[2])%p]
 e=(1,0); ell=(0,1)
 Hprojective=[g for g in G if mv(g,e,p)[1]==0]
 HA=[g for g in G if mv(g,e,p)==e]
 HB=[g for g in G if rowmv(ell,inv(g,p),p)==ell]
 J=[g for g in HA if g in HB]
 assert len(J)==p and len(Hprojective)==p*(p-1)**2
 assert all(mm(mm(g,j,p),inv(g,p),p) in J for g in Hprojective for j in J)
 diagonal={(g[0],g[3]) for g in Hprojective}
 assert len(diagonal)==(p-1)**2
 # An incident pair instead has stabilizer p-1, hence degree p(p^2-1).
 incident=(1,0)
 Hincident=[g for g in HA if rowmv(incident,inv(g,p),p)==incident]
 assert len(Hincident)==p-1
 # Odd functions fixed by complex conjugation; representative coordinates
 V=[v for v in itertools.product(range(p),repeat=2) if v!=(0,0)]
 neg=lambda v:((-v[0])%p,(-v[1])%p)
 reps=[];seen=set()
 for v in V:
  if v not in seen: reps.append(v);seen.update((v,neg(v)))
 coords={}
 for j,v in enumerate(reps):coords[v]=(j,1);coords[neg(v)]=(j,-1)
 cc=lambda v:(v[0],-v[1]%p)
 basis=[];used=set()
 for j,v in enumerate(reps):
  if j in used:continue
  k,s=coords[cc(v)];used.update((j,k))
  if j==k:
   if s==1:
    b=[0]*len(reps);b[j]=1;basis.append(b)
  else:
   b=[0]*len(reps);b[j]=1;b[k]=s;basis.append(b)
 U=[]
 for lam in reps:
  U.append([sum((1 if (lam[0]*v[0]+lam[1]*v[1])%p==1 else 0)*s
                for v,(k,s) in coords.items() if k==j) for j in range(len(reps))])
 # Each invariant basis uses a unique leading coordinate equal to1.
 piv=[next(i for i,x in enumerate(b) if x) for b in basis]
 T=[]
 for i in piv:T.append([sum(U[i][k]*b[k] for k in range(len(reps))) for b in basis])
 for col,b in enumerate(basis):
  image=[sum(U[i][k]*b[k] for k in range(len(reps))) for i in range(len(reps))]
  recon=[sum(basis[j][i]*T[j][col] for j in range(len(basis))) for i in range(len(reps))]
  assert image==recon
 d=det(T)
 assert abs(d)==p**((p*p-1)//8)
 return {'p':p,'G_order':len(G),'projective_field_degree':len(G)//len(Hprojective),
   'point_field_degree':len(G)//len(HA),'compatible_compositum_degree':len(G)//len(J),
   'compositum_over_projective_order':len(diagonal),'unipotent_stabilizer_order':len(J),
   'incident_compositum_degree':len(G)//len(Hincident),
   'full_minus_archimedean_rank':len(basis),'incidence_determinant':int(d),
   'not_a_class_or_Selmer_computation':True}
result={'status':'PASS','checks':[one(p) for p in (3,5,7)],'claim':'group geometry and real incidence determinant only'}
Path(__file__).with_name('GROUP_SCOPE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
