# Certify every EXCLUSION made by descent2.py with an independent brute-force cover of Z_p (and of pZ_p for z=1/t).
import time
from itertools import combinations
src=open('descent2.py').read().split('# controls')[0]
exec(src)
def brute_cover(h,p,kmax=80):
    """exists z in Z_p with h(z) in (Q_p^*)^2 ∪ {0}?  Content stripped first: h = p^c H1."""
    c=min(vp(x,p) for x in h if x!=0); H1=[x//p**c for x in h]
    pending=[(0,0)]
    while pending:
        new=[]
        for z0,k in pending:
            for t0 in range(p):
                z=z0+t0*p**k; kk=k+1
                val=polyval(H1,z)
                if val==0: return True
                v=vp(val,p); margin=3 if p==2 else 1
                if v+margin<=kk:
                    u=val//p**v
                    if (c+v)%2==0 and (u%8==1 if p==2 else pow(u%p,(p-1)//2,p)==1): return True
                else:
                    if kk>=kmax: raise RuntimeError("undecided at depth %d"%kk)
                    new.append((z,kk))
        if len(new)>2_000_000: raise RuntimeError("pending blowup")
        pending=new
    return False
def brute_local(d,a,b,p):
    h=[d*d*d,0,d*d*a,0,d*b]
    hrev_sub=[d*b,0,d*d*a*p*p,0,d*d*d*p**4]      # d*t^4 g(1/t) with t = p*s, as a polynomial in s in Z_p
    return brute_cover(h,p) or brute_cover(hrev_sub,p)
def run(a,b,name):
    a2,b2=-2*a,a*a-4*b
    bad=sorted(set(primes_of(2*16*b*b*(a*a-4*b))))
    print(f"== {name}: bad primes {bad}",flush=True)
    nex=0; bad_cert=0
    for (aa,bb,side) in ((a,b,"phihat(d|b)"),(a2,b2,"phi(d|a2-4b)")):
        ps=primes_of(bb); kept=[]
        for r in range(len(ps)+1):
            for sub in combinations(ps,r):
                m=1
                for q in sub: m*=q
                for d in (m,-m):
                    if not real_soluble(d,aa,bb):
                        print(f"   {side} d={d:>12}: excluded at inf",flush=True); nex+=1; continue
                    excl=None
                    for p in bad:
                        if not locally_soluble(d,aa,bb,p): excl=p; break
                    if excl is None: kept.append(d); continue
                    nex+=1; t=time.time()
                    try: cert = (brute_local(d,aa,bb,excl)==False)
                    except RuntimeError as e: cert=str(e)
                    if cert is not True: bad_cert+=1
                    print(f"   {side} d={d:>12}: excluded at p={excl}; brute-force certifies insoluble: {cert}  ({time.time()-t:.1f}s)",flush=True)
        print(f"   {side}: kept {kept}",flush=True)
    print(f"   exclusions {nex}, uncertified {bad_cert}",flush=True)
run(159145,5207351716,"twist E^{-7}")
run(-22735,106272484,"seed E")
