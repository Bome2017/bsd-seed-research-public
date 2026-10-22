"""Actual finite-prime evaluation of authenticated compact ordinary units.

No unit or class completeness is inferred from the compact source list.
"""
import json, time, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else HERE / 'compact_units_batch1.json'
OUTPUT = Path(sys.argv[2]).resolve() if len(sys.argv)>2 else HERE / 'split_unit_rows.json'
CURVE = list(map(int,sys.argv[3].split(','))) if len(sys.argv)>3 else [0,1,1,-2,0]
SPLIT = Path(sys.argv[4]).resolve() if len(sys.argv)>4 else HERE/'split_primes.json'
A1,A2,A3,A4,A6=CURVE
P = 7

def rank(rows, p=P):
    a = [[x % p for x in r] for r in rows]
    if not a:
        return 0
    n, m, k = len(a), len(a[0]), 0
    for j in range(m):
        pivot = next((i for i in range(k,n) if a[i][j]),None)
        if pivot is None:
            continue
        a[k],a[pivot] = a[pivot],a[k]
        inv = pow(a[k][j],-1,p)
        a[k] = [x*inv%p for x in a[k]]
        for i in range(n):
            if i != k and a[i][j]:
                z = a[i][j]
                a[i] = [(x-z*y)%p for x,y in zip(a[i],a[k])]
        k += 1
        if k == n:
            break
    return k

def poly(c,x,q):
    ans=0
    for a in reversed(c):
        ans=(ans*x+a)%q
    return ans

def evaluate(v,x,q):
    return poly(v[0],x,q)*pow(v[1],-1,q)%q

def add(a,b,q):
    if a is None:return b
    if b is None:return a
    x,y=a; z,w=b
    if x==z and (y+w+A1*x+A3)%q==0:return None
    if a==b:
        s=(3*x*x+2*A2*x+A4-A1*y)*pow(2*y+A1*x+A3,-1,q)%q
    else:
        s=(w-y)*pow(z-x,-1,q)%q
    v=(y-s*x)%q
    u=(s*s+A1*s-A2-x-z)%q
    return u,(-(s+A1)*u-v-A3)%q

def mul(a,n,q):
    r=None
    while n:
        if n&1:r=add(r,a,q)
        a=add(a,a,q);n//=2
    return r

def primitive(q):
    n=q-1; fac=[];d=2
    while d*d<=n:
        if n%d==0:
            fac.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:fac.append(n)
    return next(g for g in range(2,q) if all(pow(g,(q-1)//r,q)!=1 for r in fac))

def main():
    started=time.monotonic()
    f,xp,yp,sig,bases,K=json.loads(SRC.read_text())
    split=json.loads(SPLIT.read_text())
    count=len(K[0]);weights=[6,2,3,1,5,4]
    outputs=[]
    for q,roots in split:
        assert len(roots)==48 and len(set(roots))==48
        assert all(poly(f,r,q)==0 for r in roots)
        points=[(evaluate(xp,r,q),evaluate(yp,r,q)) for r in roots]
        assert len(set(points))==48
        assert all((y*y+A1*x*y+A3*y-x*x*x-A2*x*x-A4*x-A6)%q==0 for x,y in points)
        assert all(mul(T,7,q) is None for T in points)
        index={r:i for i,r in enumerate(roots)}
        sigma=[index[evaluate(sig,r,q)] for r in roots]
        assert all(points[sigma[i]]==mul(points[i],3,q) for i in range(48))
        T=points[0]; multiples={mul(T,a,q) for a in range(7)}
        U=next(t for t in points if t not in multiples)
        labels={add(mul(T,a,q),mul(U,b,q),q):(a,b) for a in range(7) for b in range(7)}
        assert len(labels)==49
        labs=[labels[t] for t in points]
        g=primitive(q);z=pow(g,(q-1)//7,q)
        log7={pow(z,j,q):j for j in range(7)}
        def dl(v):
            assert v
            return log7[pow(v,(q-1)//7,q)]
        logs=[]
        for base in bases:
            vals=[dl(evaluate(base,r,q)) for r in roots]
            for j in range(6):
                logs.append(vals)
                vals=[vals[sigma[i]] for i in range(48)]
        assert len(logs)==len(K)
        raw=[[sum(logs[j][i]*K[j][c] for j in range(len(K)))%7 for i in range(48)] for c in range(count)]
        projected=[]
        for row in raw:
            accum=[0]*48;tmp=row
            for weight in weights:
                accum=[(x+weight*y)%7 for x,y in zip(accum,tmp)]
                tmp=[tmp[sigma[i]] for i in range(48)]
            assert all(accum[sigma[i]]==3*accum[i]%7 for i in range(48))
            projected.append(accum)
        ti=points.index(T);ui=points.index(U)
        defects=[[(row[i]-a*row[ti]-b*row[ui])%7 for i,(a,b) in enumerate(labs)] for row in projected]
        # Positive local allowance: every genuinely linear function is killed.
        for ca in range(7):
            for cb in range(7):
                row=[(ca*a+cb*b)%7 for a,b in labs]
                assert all((row[i]-a*row[ti]-b*row[ui])%7==0 for i,(a,b) in enumerate(labs))
        outputs.append({'q':q,'roots':roots,'points':points,'torsion_basis':[T,U],'labels':labs,'primitive_root':g,'sigma_permutation':sigma,'raw_unit_logs':raw,'chi_unit_logs':projected,'additivity_defects':defects,'raw_rank':rank(raw),'chi_rank':rank(projected),'defect_rank':rank(defects)})
    # Stack independent local maps on the same compact source coordinate.
    combined=[[x for row in outputs for x in row['additivity_defects'][j]] for j in range(count)]
    result={'source':str(SRC),'source_columns':count,'coefficient_prime':7,'curve':CURVE,'complete_unit_basis_claim':False,'rows':outputs,'combined_defect_rank':rank(combined),'elapsed_seconds':time.monotonic()-started}
    OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'source_columns':count,'ranks':[(r['q'],r['raw_rank'],r['chi_rank'],r['defect_rank']) for r in outputs],'combined_defect_rank':result['combined_defect_rank'],'elapsed_seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
