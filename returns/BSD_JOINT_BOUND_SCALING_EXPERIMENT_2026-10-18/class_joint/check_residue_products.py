from pathlib import Path
import json,time
R=Path(__file__).resolve().parent
S=R.parent/'p7_new_source'
F,XP,YP,SIG,bases,K=json.loads((S/'compact_units_eval.json').read_text())
qs=json.loads((R.parent/'local_rank/split_primes.json').read_text())
p=7;coef=[6,2,3,1,5,4]
def ev(pair,r,q):
 a,d=pair; z=0
 for c in reversed(a):z=(z*r+c)%q
 assert d%q
 return z*pow(d,-1,q)%q
out=[];start=time.monotonic()
for q,roots in qs:
 assert len(set(roots))==48 and q%7==1
 assert all(sum(c*pow(r,j,q) for j,c in enumerate(F))%q==0 for r in roots)
 ix={r:i for i,r in enumerate(roots)}; perm=[ix[ev(SIG,r,q)] for r in roots]
 factors=[[pow(ev(b,r,q),(q-1)//7,q) for b in bases] for r in roots]
 assert all(x for row in factors for x in row)
 checked=0
 for i in range(48):
  orbit=[i]
  for _ in range(5):orbit.append(perm[orbit[-1]])
  assert perm[orbit[-1]]==i and len(set(orbit))==6
  projected=[]
  for k in range(26):
   for j in range(6):
    z=1
    for t,c in enumerate(coef):z=z*pow(factors[orbit[(j+t)%6]][k],c,q)%q
    projected.append(z)
  for h in range(99):
   z=1
   for n,v in enumerate(projected):z=z*pow(v,K[n][h]%7,q)%q
   assert z==1,(q,i,h,z)
   checked+=1
 out.append({'q':q,'root_count':48,'direct_projected_unit_character_products':checked,'all_equal_one':True})
result={'status':'PASS','method':'direct multiplicative products; no discrete logs or producer row/rank outputs','rows':out,'elapsed_seconds':time.monotonic()-start,'scope':'finite residues only; no proof that character components globally zero or seventh powers'}
(R/'RESIDUE_PRODUCT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
