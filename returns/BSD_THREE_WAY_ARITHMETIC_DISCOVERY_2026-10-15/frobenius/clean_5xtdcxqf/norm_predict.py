#!/usr/bin/env python3
"""Predict fresh outcomes from TWO evaluations of the fixed affine norm only."""
import json,hashlib,math,datetime
from pathlib import Path
R=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ev(poly,x,q):
 r=0
 for c in reversed(poly):
  if isinstance(c,int):a=c
  else:a=c[0]*pow(c[1],-1,q)
  r=(r*x+a)%q
 return r
def neg(P,q):return (P[0],(-P[1]-1)%q)
def add(P,Q,q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v+1)%q==0:return None
 if x==u:m=(3*x*x-21)*pow(2*y+1,-1,q)%q
 else:m=(v-y)*pow(u-x,-1,q)%q
 z=(m*m-x-u)%q
 return (z,(-y-1+m*(x-z))%q)
def on(P,q):
 x,y=P;return (y*y+y-x*x*x+21*x+27)%q==0
def omega(q):
 for u in range(2,q):
  v=pow(u,(q-1)//3,q)
  if v!=1:return v
 raise AssertionError('No cubic root of unity')
def norm_record(block,N):
 q=block['q'];pts=[tuple(p)for p in block['points']]
 assert q%3==1 and len(set(pts))==8 and len(set(block['roots']))==8
 assert all(ev(N['point_field'],r,q)==0 for r in block['roots'])
 assert all(on(P,q) and add(add(P,P,q),P,q) is None for P in pts)
 P=pts[0];Q=next(Q for Q in pts if Q!=P and Q!=neg(P,q));i=pts.index(P);j=pts.index(Q)
 om=omega(q);records=[]
 for Q0 in [Q,neg(Q,q)]:
  m=(Q0[1]-P[1])*pow(Q0[0]-P[0],-1,q)%q;z=6*m%q
  assert ev(N['line_field'],z,q)==0
  value=ev(N['line_norm'],z,q);assert value
  residue=pow(value,(q-1)//3,q);char=[1,om,om*om%q].index(residue)
  S=add(P,Q0,q);assert S is not None
  records.append(dict(point_indices=[i,pts.index(Q0),pts.index(neg(S,q))],line_coordinate=z,value=value,cubic_power=residue,cubic_character=char))
 return dict(q=q,chosen_independent_points=[i,j],omega=om,two_norms=records,predicted_survives=all(x['cubic_character']==0 for x in records))

def main():
 N=json.loads((R/'norm.json').read_text());blocks=[json.loads(s)for s in(R/'fresh_roots.jsonl').read_text().splitlines()]
 assert len(blocks)==40
 records=[norm_record(b,N)for b in blocks]
 out=dict(status='FROZEN_NORM_ONLY_PREDICTIONS',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),method='Two polynomial norm evaluations; no source-element values or characters read',norm_sha256=sha(R/'norm.json'),root_input_sha256=sha(R/'fresh_roots.jsonl'),predictor_sha256=sha(Path(__file__)),records=records)
 (R/'NORM_PREDICTIONS.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':out['status'],'survives':[r['q']for r in records if r['predicted_survives']],'count':len(records)}))
if __name__=='__main__':main()
