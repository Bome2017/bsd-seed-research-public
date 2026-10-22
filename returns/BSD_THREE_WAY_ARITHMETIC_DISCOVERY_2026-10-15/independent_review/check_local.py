#!/usr/bin/env python3
"""Recompute local characters from literal rational field polynomials.
No imported producer code, source-coordinate matrix, or cached rank is used.
"""
from pathlib import Path
from fractions import Fraction
import json,itertools,hashlib,math
BASE=Path(__file__).resolve().parents[1]
def ev(poly,x,q):
 y=0
 for c in reversed(poly):
  z=Fraction(c);y=(y*x+z.numerator*pow(z.denominator,-1,q))%q
 return y

def rank(A):
 if not A:return 0
 A=[[x%3 for x in r] for r in A];r=0
 for j in range(len(A[0])):
  k=next((k for k in range(r,len(A)) if A[k][j]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];d=pow(A[r][j],-1,3);A[r]=[x*d%3 for x in A[r]]
  for k in range(len(A)):
   if k!=r:
    d=A[k][j];A[k]=[(x-d*y)%3 for x,y in zip(A[k],A[r])]
  r+=1
 return r

def add(P,Q,a,q):
 if P is None:return Q
 if Q is None:return P
 a1,a2,a3,a4,a6=[x%q for x in a];x,y=P;u,v=Q
 if x==u and (y+v+a1*x+a3)%q==0:return None
 if P==Q:
  lam=(3*x*x+2*a2*x+a4-a1*y)*pow((2*y+a1*x+a3)%q,-1,q)%q
 else:lam=(v-y)*pow((u-x)%q,-1,q)%q
 nu=(y-lam*x)%q
 xx=(lam*lam+a1*lam-a2-x-u)%q
 return (xx,(-(lam+a1)*xx-nu-a3)%q)

def multiply(A,B):return [[sum(x*y for x,y in zip(r,c))%3 for c in zip(*B)] for r in A]
def vq(n,q):
 n=abs(n);v=0
 if n==0:raise ValueError('exact zero')
 while n%q==0:n//=q;v+=1
 return v

def local_value(poly,field,root,q):
 coeffs=list(map(Fraction,poly));den=math.lcm(*(a.denominator for a in coeffs));nums=[int(a*den) for a in coeffs]
 dv=vq(den,q);r=root;mod=q
 def ieval(cs,r,mod):
  ans=0
  for a in reversed(cs):ans=(ans*r+a)%mod
  return ans
 field=[int(Fraction(c)) for c in field];der=[i*field[i] for i in range(1,len(field))]
 for precision in range(1,25):
  num=ieval(nums,r,mod)
  if num and precision>dv:
   vn=vq(num,q);v=vn-dv
   return v,(num//(q**vn))*pow(den//(q**dv),-1,q)%q,precision
  mod*=q;r=(r-ieval(field,r,mod)*pow(ieval(der,r,mod),-1,mod))%mod
 raise ValueError(('insufficient local precision',q,root))

results=[];bound=[];total=0;checks=0;nonunit_literals=[]
for name in ['1913b1','28042a1','seed3','389a1','mirror389_false']:
 d=BASE/'local_signatures'/name
 for f in ['actual_polynomials.json','SIGNATURES.json','coordinates.json']:
  p=d/f;bound.append({'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 lit=json.loads((d/'actual_polynomials.json').read_text());saved=json.loads((d/'SIGNATURES.json').read_text());coords=json.loads((d/'coordinates.json').read_text())
 r=saved['summary']['point_dimension'];allrows=[];case=[]
 for block in saved['fresh_primes']:
  q=block['prime'];roots=block['roots'];omega=block['cubic_root']
  assert q>3 and q%3==1 and len(set(roots))==8
  assert all(ev(lit['field'],x,q)==0 for x in roots)
  assert omega!=1 and pow(omega,3,q)==1
  points=[tuple(ev(poly,x,q) for poly in lit['T']) for x in roots]
  assert points==list(map(tuple,block['torsion_points']))
  for P in points:
   x,y=P;a1,a2,a3,a4,a6=coords['ainvariants']
   assert (y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%q==0
   assert add(add(P,P,coords['ainvariants'],q),P,coords['ainvariants'],q) is None
  lookup={1:0,omega:1,pow(omega,2,q):2}
  local=[[local_value(poly,lit['field'],x,q) for poly in lit['classes']] for x in roots]
  for ix,row in enumerate(local):
   for ik,(v,unit,prec) in enumerate(row):
    assert v%3==0,(name,q,ix,ik,'ramified class valuation',v)
    if v:nonunit_literals.append({'case':name,'q':q,'root_index':ix,'class_index':ik,'valuation':v,'unit':unit,'precision':prec})
  values=[[lookup[pow(unit,(q-1)//3,q)] for v,unit,prec in row] for row in local]
  assert values==block['known_values']
  # The whole matrix is tested for additivity from elliptic point addition.
  defects=[]
  for i,P in enumerate(points):
   for j,Q in enumerate(points):
    T=add(P,Q,coords['ainvariants'],q)
    if T is None:assert all((a+b)%3==0 for a,b in zip(values[i],values[j]))
    else:
     k=points.index(T);defects.extend((a+b-c)%3 for a,b,c in zip(values[i],values[j],values[k]))
  if name!='mirror389_false':assert not any(defects)
  annih=block['annihilator_rows'];sig=multiply(annih,values)
  assert sig==block['quotient_signatures']
  assert all(all(x==0 for x in row[:r]) for row in sig)
  pointrows=[v[:r] for v in values]
  point_rank=rank(pointrows)
  assert rank(annih)==8-point_rank
  assert point_rank==block['point_image_rank']
  assert rank(sig)==block['known_quotient_rank']
  # All changes by rational-point classes preserve quotient signatures.
  for a in itertools.product(range(3),repeat=r):
   for k in range(r,len(lit['classes'])):
    modified=[[(row[k]+sum(c*x for c,x in zip(a,row[:r])))%3] for row in values]
    assert [x[0] for x in multiply(annih,modified)]==[row[k] for row in sig];checks+=1
  # Literal multiplying by a cube gives the same cubic character.
  for localrow in local:
   for value,unit,prec in localrow:
    v=unit
    for z in [1,2,3,q-1]:
     assert lookup[pow(v*pow(z,3,q)%q,(q-1)//3,q)]==lookup[pow(v,(q-1)//3,q)];checks+=1
  allrows.extend(sig);case.append({'q':q,'point_image_rank':point_rank,'quotient_rank':rank(sig),'additivity_passes':not any(defects)});total+=1
 assert rank(allrows)==len(lit['classes'])-r
 results.append({'case':name,'primes':case,'aggregate_known_quotient_rank':rank(allrows),'known_quotient_dimension':len(lit['classes'])-r,'false_candidate_not_Selmer':name=='mirror389_false'})
out={'status':'LITERAL_LOCAL_ARITHMETIC_REPLAY_PASSED','nonunit_literal_representatives':nonunit_literals,'blocks':total,'representative_and_point_shift_checks':checks,'cases':results,'inputs':bound,'scope':'Literal polynomial arithmetic and finite-field quotient verification; retained class admission, point ranks and saturation are not recomputed here.'}
p=Path(__file__).with_name('LOCAL_REPLAY.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','blocks','representative_and_point_shift_checks']}))
