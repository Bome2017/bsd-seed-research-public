"""Independent exact integer/permutation and F7 linear algebra on saved gate data."""
from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent.parent
j=json.loads((r/'arithmetic/GATE_CORE.json').read_text())
ps,pp,da,db,full,chars,weights,proj,kernels,recorded_ranks=j
n=len(pp);assert n==331 and sorted(pp)==list(range(1,n+1))
p=[x-1 for x in pp]
assert all(len(row)==20 for row in da+db)
assert all(len(row)==120 for row in full)

def push(a):
    out=[None]*n
    for i,row in enumerate(a):out[p[i]]=row[:]
    return out

def sub(a,b):return [[x-y for x,y in zip(u,v)] for u,v in zip(a,b)]
def mod(a):return [[x%7 for x in row] for row in a]
def rank(a):
    a=mod(a); rows=len(a);cols=len(a[0]);rk=0; ids=list(range(rows)); pivrows=[];pivcols=[]
    for col in range(cols):
        ix=next((i for i in range(rk,rows) if a[i][col]),None)
        if ix is None:continue
        a[rk],a[ix]=a[ix],a[rk];ids[rk],ids[ix]=ids[ix],ids[rk]
        pivrows.append(ids[rk]);pivcols.append(col)
        iv=pow(a[rk][col],-1,7);a[rk]=[iv*x%7 for x in a[rk]]
        for i in range(rk+1,rows):
            t=a[i][col]
            if t:a[i]=[(x-t*y)%7 for x,y in zip(a[i],a[rk])]
        rk+=1
        if rk==rows:break
    return rk,pivrows,pivcols

t=da
for _ in range(3):t=push(t)
assert sub(da,t)==db
t=db
for _ in range(3):t=push(t)
assert t==[[-x for x in row] for row in db]
tr=[db]
for _ in range(5):tr.append(push(tr[-1]))
assert push(tr[-1])==db
expected_full=[[tr[k%6][i][k//6] for k in range(120)] for i in range(n)]
assert expected_full==full
assert chars==[3,5,6]
results=[]
for h,ch in enumerate(chars):
    w=[6*pow(ch,-k,7)%7 for k in range(6)];assert w==weights[h]
    q=[[sum(w[k]*tr[k][i][col] for k in range(6))%7 for col in range(20)] for i in range(n)]
    assert q==proj[h]
    assert mod(push(q))==[[ch*x%7 for x in row] for row in q]
    rk,pr,pc=rank(q);assert rk==20==recorded_ranks[h]
    assert len(kernels[h])==20 and all(row==[] for row in kernels[h])
    results.append({'character':ch,'weights':w,'rank':rk,'pivot_rows_zero_based':pr,'pivot_columns_zero_based':pc})
assert [[sum(proj[h][i][col] for h in range(3))%7 for col in range(20)] for i in range(n)]==mod(db)
rk,pr,pc=rank(full);assert rk==60
half=[[row[6*i+k] for i in range(20) for k in range(3)] for row in full]
hrk,_,_=rank(half);assert hrk==60
for i in range(20):
    for k in range(3):assert all(row[6*i+k+3]==-row[6*i+k] for row in full)
seen=set();orbit_lengths=[]
for i in range(n):
    if i in seen:continue
    a=i;orb=[]
    while a not in orb:orb.append(a);seen.add(a);a=p[a]
    assert a==i and len(orb) in [1,2,3,6]
    orbit_lengths.append(len(orb))
assert all((lambda q:q)(p[p[p[p[p[p[i]]]]]])==i for i in range(n))
print(json.dumps({'status':'SCALAR_GATE_INDEPENDENT_REPLAY_PASS','support_size':n,'prime_orbit_counts':{str(k):orbit_lengths.count(k) for k in [1,2,3,6]},'projected_results':results,'full_scalar_columns':120,'full_rank_mod7':rk,'first_three_per_generator_rank_mod7':hrk,'all_integer_kernel_relations':'equal exponents on each exact tau inverse pair','source_hash':hashlib.sha256((r/'arithmetic/GATE_CORE.json').read_bytes()).hexdigest(),'scope':'Saved actual-support/divisor data and independent Python algebra. Field and ideal bindings checked separately; no fresh factorization.'},indent=2))
