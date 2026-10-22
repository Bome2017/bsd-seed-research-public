from pathlib import Path
import ast,json,math,time,signal,collections
R=Path(__file__).resolve().parent
start=time.monotonic();signal.alarm(115)
rows=[ast.literal_eval(l) for l in Path('/Users/bsm/BSD_RELATIVE_UNIT_EXECUTION_2026-10-18/source/norm_trials.gp').read_text().splitlines()]
ps=[p for p in range(2,1001) if all(p%d for d in range(2,math.isqrt(p)+1))]
res=[]; small=[]
for row in rows:
 n=abs(row[-1]); f={}
 for p in ps:
  e=0
  while n%p==0: n//=p;e+=1
  if e:f[p]=e
 res.append(n);small.append(f)
# Bernstein product/remainder-tree batch GCD, including duplicate cofactors.
tree=[res]
while len(tree[-1])>1:
 a=tree[-1];tree.append([math.prod(a[i:i+2]) for i in range(0,len(a),2)])
rem=tree[-1]
for a in reversed(tree[:-1]):rem=[rem[i//2]%(n*n) if n>1 else 0 for i,n in enumerate(a)]
shared=[math.gcd(n,r//n) if n>1 else 1 for n,r in zip(res,rem)]
private=[n//g for n,g in zip(res,shared)]
records=[]
for i,row in enumerate(rows):
 records.append({'id':i+1,'reconstruction':row,'small_factors':small[i],'cofactor':res[i],'shared_gcd':shared[i],'private':private[i]})
ranked=sorted(records,key=lambda x:(x['private'].bit_length(),x['cofactor'].bit_length(),abs(x['reconstruction'][-1]).bit_length(),x['id']))
# deterministic panel; exact shared-support analysis precedes final graph ordering
panel=ranked[:80]
(R/'NORM_SUPPORT.json').write_text(json.dumps({'count':len(rows),'base_bound':1000,'private_one':sum(x==1 for x in private),'fully_smooth':sum(x==1 for x in res),'shared_nontrivial':sum(x>1 for x in shared),'all_norms_distinct':len({abs(x[-1]) for x in rows})==len(rows),'elapsed_seconds':time.monotonic()-start,'records':records},separators=(',',':'))+'\n')
(R/'SELECTED.json').write_text(json.dumps(panel,indent=2)+'\n')
(R/'selected.gp').write_text(str([x['reconstruction'] for x in panel])+'\n')
print(json.dumps({'count':len(rows),'private_one':sum(x==1 for x in private),'fully_smooth':sum(x==1 for x in res),'shared_nontrivial':sum(x>1 for x in shared),'elapsed_seconds':time.monotonic()-start,'best':[{k:x[k] for k in ('id','cofactor','shared_gcd','private')} for x in panel[:12]]},indent=2))
