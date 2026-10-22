#!/usr/bin/env python3
"""Literal element/norm and all-triple replay, without producer code."""
import json,itertools,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
D=BASE/'frobenius';N=json.loads((D/'norm.json').read_text());R=json.loads((D/'FRESH_RESULTS.json').read_text());P=json.loads((D/'NORM_PREDICTIONS.json').read_text())
P={a['q']:a for a in P['records']}
def ev(cs,x,q):
 v=0
 for a in reversed(cs):
  if isinstance(a,list):a=a[0]*pow(a[1],-1,q)
  v=(v*x+a)%q
 return v

def neg(P,q):return (P[0],(-1-P[1])%q)
def add(P,Q,q):
 if P is None:return Q
 if Q is None:return P
 if Q==neg(P,q):return None
 x,y=P;u,v=Q
 l=((3*x*x-21)*pow(2*y+1,-1,q) if P==Q else (v-y)*pow(u-x,-1,q))%q
 xx=(l*l-x-u)%q
 return xx,(-y-1+l*(x-xx))%q
out=[];normcount=0;triplecount=0
for b in R['records']:
 q=b['q'];pts=list(map(tuple,b['points']));roots=b['roots'];omega=b['omega']
 assert len(set(roots))==len(set(pts))==8
 assert all(ev(N['point_field'],r,q)==0 for r in roots)
 for T in pts:
  x,y=T;assert (y*y+y-x**3+21*x+27)%q==0
  assert add(add(T,T,q),T,q) is None
 vals=[ev(N['source_element'],r,q) for r in roots]
 assert all(vals) and vals==b['actual_source_residues']
 charmap={1:0,omega:1,omega*omega%q:2};chars=[charmap[pow(v,(q-1)//3,q)] for v in vals]
 assert chars==b['actual_source_characters']
 assert all((chars[i]+chars[pts.index(neg(T,q))])%3==0 for i,T in enumerate(pts))
 defects=[]
 for i,T in enumerate(pts):
  for j in range(i,8):
   S=add(T,pts[j],q)
   if S is not None:
    k=pts.index(S);defects.append((chars[i]+chars[j]-chars[k])%3);triplecount+=1
 assert defects==b['defects']
 lines=[]
 for ids in itertools.combinations(range(8),3):
  i,j,k=ids
  if add(add(pts[i],pts[j],q),pts[k],q) is not None:continue
  assert pts[i][0]!=pts[j][0]
  slope=(pts[j][1]-pts[i][1])*pow(pts[j][0]-pts[i][0],-1,q)%q;z=6*slope%q
  assert ev(N['line_field'],z,q)==0
  val=ev(N['line_norm'],z,q)
  assert val==vals[i]*vals[j]*vals[k]%q
  lines.append(pow(val,(q-1)//3,q)==1);normcount+=1
 assert len(lines)==8
 survives=not any(defects)
 assert survives==all(lines)==b['actual_survives']==P[q]['predicted_survives']
 # Independently verify both sealed norm evaluations, not only the Boolean.
 for a in P[q]['two_norms']:
  val=ev(N['line_norm'],a['line_coordinate'],q)
  assert val==a['value'];assert pow(val,(q-1)//3,q)==a['cubic_power']
 out.append({'q':q,'survives':survives})
assert len(out)==40
result={'status':'ALL_FRESH_LITERAL_NORMS_AND_ROWS_REPLAYED','count':len(out),'affine_norm_products':normcount,'nonzero_sum_triples':triplecount,'survivor_primes':[a['q'] for a in out if a['survives']],'inputs':[{'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [D/'norm.json',D/'FRESH_RESULTS.json',D/'NORM_PREDICTIONS.json']],'scope':'Exact rational-polynomial reductions and finite-field arithmetic; the number-field norm identity and Chebotarev theorem are separate written arguments.'}
Path(__file__).with_name('FROBENIUS_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
