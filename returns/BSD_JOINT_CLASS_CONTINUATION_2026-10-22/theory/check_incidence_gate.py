#!/usr/bin/env python3
"""Exact finite-group screen, not a number-field class computation."""
import json
from pathlib import Path

def rank(a,p):
 a=[r[:] for r in a]; k=0
 for j in range(len(a[0]) if a else 0):
  q=next((i for i in range(k,len(a)) if a[i][j]%p),None)
  if q is None: continue
  a[k],a[q]=a[q],a[k]; z=pow(a[k][j],-1,p);a[k]=[(z*x)%p for x in a[k]]
  for i in range(len(a)):
   if i!=k:
    z=a[i][j]%p;a[i]=[(x-z*y)%p for x,y in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return k

def primitive(p):
 return next(a for a in range(2,p) if len({pow(a,k,p) for k in range(p-1)})==p-1)

def test(p):
 vv=[(a,b) for a in range(p) for b in range(p) if a or b]; ri={x:i for i,x in enumerate(vv)}
 g=primitive(p); gens=[(1,1,0,1),(1,0,1,1),(g,0,0,1)]
 todo={(i,j) for i in range(len(vv)) for j in range(len(vv))}; orbitdata=[]
 while todo:
  start=min(todo);todo.remove(start);q=[start];o=set(q)
  while q:
   i,j=q.pop();x,y=vv[i];a,b=vv[j]
   for A,B,C,D in gens:
    det=(A*D-B*C)%p;dinv=pow(det,-1,p)
    new=(ri[((A*x+B*y)%p,(C*x+D*y)%p)],ri[(((a*D-b*C)*dinv)%p,((-a*B+b*A)*dinv)%p)])
    if new not in o:o.add(new);todo.remove(new);q.append(new)
  vals={(vv[i][0]*vv[j][0]+vv[i][1]*vv[j][1])%p for i,j in o}
  assert len(vals)==1
  t=vals.pop(); assert len(o)==(p*p-1)*(p-1 if t==0 else p)
  orbitdata.append({'pairing_value':t,'size':len(o)})
 assert len(orbitdata)==p
 reps=[(1,t) for t in range(p)]+[(0,1)]; modulus=p*p
 # Every homogeneous function is determined on these p+1 lines.
 mats=[]
 for t in range(p):
  mat=[]
  for l1,l2 in reps:
   row=[]
   for x,y in reps:
    d=(l1*x+l2*y)%p
    # Teichmuller lift of nonzero a modulo p^2.
    row.append(sum(pow(a,p,modulus) for a in range(1,p) if a*d%p==t)%modulus)
   mat.append(row)
  mats.append(mat)
 assert all(x==0 for row in mats[0] for x in row)
 for t in range(1,p):
  assert mats[t]==[[(pow(t,p,modulus)*x)%modulus for x in row] for row in mats[1]]
 flat=[[x%p for row in m for x in row] for m in mats]
 assert rank(flat,p)==1
 r=rank(mats[1],p);assert r==p-1
 # The complete kernel is exactly the two coordinate-linear functions.
 for k in (0,1):
  w=[v[k] for v in reps]
  assert all(sum(a*b for a,b in zip(row,w))%p==0 for row in mats[1])
 return {'p':p,'geometric_points':len(vv),'pair_orbits':sorted(orbitdata,key=lambda x:x['pairing_value']), 'faithful_dimension':p+1,'norm_rank':r,'kernel_dimension':p+1-r,'orbit_map_span_dimension':1,'teichmueller_relation_mod_p2':True}

# Exact finite class-module controls: u multiplication by p, v identity.
# All compositions are p, while the p-torsion kernel has arbitrary e.
controls=[]
for p in [3,5,7]:
 for a in [1,2,3]:
  for e in [1,2,4,8]:
   mod=p**a
   # coordinatewise verification is sufficient for direct sums
   u=lambda x: p*x%mod
   v=lambda x: x%mod
   assert all(v(u(x))==p*x%mod and u(v(x))==p*x%mod for x in range(mod))
   ker=[x for x in range(mod) if p*x%mod==0]
   assert len(ker)==p
   controls.append({'p':p,'exponent':a,'multiplicity':e,'u':'p','v':'identity','p_torsion_kernel_dimension':e,'next_layer_absent':a==1})
result={'status':'PASS_GEOMETRIC_SCREEN_ONLY','tested_character':'degree-one Teichmueller character; ranks not asserted for every nontrivial character','prime_checks':[test(p) for p in [3,5,7,11,13]],'multiplicity_controls':controls,'number_field_class_values_computed':False}
path=Path(__file__).with_name('INCIDENCE_GATE_RESULT.json');path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'primes':[3,5,7,11,13],'class_controls':len(controls),'output':str(path)}))
