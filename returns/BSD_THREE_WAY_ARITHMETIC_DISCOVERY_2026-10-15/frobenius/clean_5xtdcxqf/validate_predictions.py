#!/usr/bin/env python3
"""Evaluate actual source generators only AFTER norm predictions were frozen."""
import json,hashlib,datetime
from pathlib import Path
from norm_predict import ev,add,neg,norm_record,sha
R=Path(__file__).resolve().parent
OLD=Path('/Users/bsm/BSD_THREE_WAY_ARITHMETIC_DISCOVERY_2026-10-15/frobenius/inputs/heldout')

def check(block,S,N,pred):
 q=block['q'];pts=[tuple(p)for p in block['points']];roots=block['roots'];om=pred['omega'];vv=N['source_exponents'];G=S['source_factors'];chars=[];aval=[]
 for i,r in enumerate(roots):
  assert tuple(ev(c,r,q)for c in S['torsion_point'])==pts[i]
  vals=[];cs=[]
  for factors in G:
   v=1
   for poly,e in factors:
    a=ev(poly,r,q);assert a;v=v*pow(a,e,q)%q
   vals.append(v);cs.append([1,om,om*om%q].index(pow(v,(q-1)//3,q)))
  av=1
  for v,e in zip(vals,vv):av=av*pow(v,e,q)%q
  assert av==ev(N['source_element'],r,q)
  aval.append(av);chars.append(cs)
 achars=[sum(a*b for a,b in zip(vv,c))%3 for c in chars]
 for i,P in enumerate(pts):assert (achars[i]+achars[pts.index(neg(P,q))])%3==0
 triples=[];rows=[];defects=[]
 for i,P in enumerate(pts):
  for j in range(i,8):
   Q=add(P,pts[j],q)
   if Q is None:continue
   k=pts.index(Q);row=[(a+b-c)%3 for a,b,c in zip(chars[i],chars[j],chars[k])]
   triples.append([i,j,k]);rows.append(row);defects.append(sum(a*b for a,b in zip(row,vv))%3)
 assert len(rows)==32
 norms=[]
 for rec in pred['two_norms']:
  val=1
  for i in rec['point_indices']:val=val*aval[i]%q
  assert val==rec['value'],'Polynomial norm disagrees with independent source-product evaluation'
  norms.append(val)
 survives=not any(defects);assert survives==pred['predicted_survives']
 return dict(q=q,roots=roots,points=block['points'],omega=om,characters=chars,triples=triples,rows=rows,actual_source_residues=aval,actual_source_characters=achars,defects=defects,actual_survives=survives,predicted_survives=pred['predicted_survives'],two_norm_values=norms)

def main():
 seal=json.loads((R/'PREDICTION_OUTPUT_SEAL.json').read_text());assert sha(R/'NORM_PREDICTIONS.json')==seal['sha256']
 S=json.loads((OLD/'mirror_extension/source.json').read_text());N=json.loads((R/'norm.json').read_text())
 blocks=[json.loads(s)for s in(R/'fresh_roots.jsonl').read_text().splitlines()];pred=json.loads((R/'NORM_PREDICTIONS.json').read_text())['records']
 results=[check(b,S,N,p)for b,p in zip(blocks,pred)]
 old=[]
 for folder in ['mirror389','mirror_extension']:
  for b in json.loads((OLD/folder/'blocks.json').read_text())['blocks']:
   p=norm_record(b,N);out=check(b,S,N,p)
   assert (not any(sum(a*c for a,c in zip(row,N['source_exponents']))%3 for row in b['rows']))==out['actual_survives']
   old.append(out)
 (R/'FRESH_RESULTS.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'ALL_40_NORM_PREDICTIONS_CORRECT','source_sha256':sha(OLD/'mirror_extension/source.json'),'norm_sha256':sha(R/'norm.json'),'sealed_prediction_sha256':seal['sha256'],'records':results},indent=2)+'\n')
 (R/'CALIBRATION_RESULTS.json').write_text(json.dumps({'status':'ALL_72_OLD_CALIBRATION_CASES_AGREE','records':old},indent=2)+'\n')
 w=next(r for r in old if r['q']==18757);p=norm_record(w,N)
 (R/'NONCUBE_WITNESS.json').write_text(json.dumps({'q':w['q'],'complete_point_field_splitting_roots':w['roots'],'source_characters':w['actual_source_characters'],'norm_only_record':p,'nonzero_cubic_residue_norms':[r for r in p['two_norms']if r['cubic_character']],'scope':'At a completely split good prime this proves the displayed affine norm is not a cube in Q(E[3]), not merely in its degree-eight subfield.'},indent=2)+'\n')
 print(json.dumps({'fresh':len(results),'fresh_survival_primes':[r['q']for r in results if r['actual_survives']],'calibration':len(old),'matches':len(results)+len(old),'fresh_source_characters':40*8*11,'fresh_rows':40*32}))
if __name__=='__main__':main()
