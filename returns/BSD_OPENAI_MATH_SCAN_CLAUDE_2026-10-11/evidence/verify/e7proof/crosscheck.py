# Independent brute-force local solubility: refine residue classes z mod p^k; a class is decided once
# v_p(value) < k - (2 if p==2 else 0): then every z in the class has the same valuation and the same
# square class of unit part (mod 8 for p=2, mod p for odd p).  No Hensel/shift polynomial machinery.
import sys
from itertools import combinations
src=open('descent2.py').read().split('# controls')[0]
exec(src)   # reuse polyval, vp, primes_of, real_soluble, locally_soluble (the recursive one) for comparison
def brute_has_sq(h,p,kmax=60):
    # classes: list of (z0,k) undecided; start with all z mod p
    pending=[(0,0)]
    while pending:
        new=[]
        for z0,k in pending:
            for t0 in range(p):
                z=z0+t0*p**k; kk=k+1
                val=polyval(h,z)
                if val==0: return True
                v=vp(val,p)
                margin = 3 if p==2 else 1
                if v + margin <= kk:
                    u=val//p**v
                    if v%2==0 and (u%8==1 if p==2 else pow(u%p,(p-1)//2,p)==1): return True
                else:
                    if kk<kmax: new.append((z,kk))
                    else: raise RuntimeError("undecided")
        pending=new
    return False
def brute_local(d,a,b,p):
    h=[d*d*d,0,d*d*a,0,d*b]; hrev=[d*b,0,d*d*a,0,d*d*d]
    # z in Z_p  OR  z = 1/t with t in pZ_p  (classes t ≡ 0 mod p: start pending at (0,1))
    if brute_has_sq(h,p): return True
    # reversed, restricted to t in pZ_p
    pending=[(0,1)]
    while pending:
        new=[]
        for z0,k in pending:
            for t0 in range(p):
                z=z0+t0*p**k; kk=k+1
                val=polyval(hrev,z)
                if val==0: return True
                v=vp(val,p); margin=3 if p==2 else 1
                if v+margin<=kk:
                    u=val//p**v
                    if v%2==0 and (u%8==1 if p==2 else pow(u%p,(p-1)//2,p)==1): return True
                else:
                    if kk<60: new.append((z,kk))
                    else: raise RuntimeError("undecided")
        pending=new
    return False
def compare(a,b,name):
    a2,b2=-2*a,a*a-4*b
    bad=sorted(set(primes_of(2*16*b*b*(a*a-4*b))))
    print(f"== {name}: bad primes {bad}")
    mism=0
    for (aa,bb,side) in ((a,b,"Sel^phihat side d|b"),(a2,b2,"Sel^phi side d|a^2-4b")):
        ps=primes_of(bb); kept=[]
        for r in range(len(ps)+1):
            for sub in combinations(ps,r):
                m=1
                for q in sub: m*=q
                for d in (m,-m):
                    fails=[]
                    if not real_soluble(d,aa,bb): fails.append("inf")
                    for p in bad:
                        r1=locally_soluble(d,aa,bb,p); r2=brute_local(d,aa,bb,p)
                        if r1!=r2: mism+=1; print("   MISMATCH",side,d,p,r1,r2)
                        if not r2: fails.append(p)
                    if fails: print(f"   {side}: d={d:>12} excluded at {fails}")
                    else: kept.append(d)
        print(f"   {side}: kept {kept}")
    print("   mismatches between recursive and brute-force:",mism)
compare(-22735,106272484,"seed E")
compare(159145,5207351716,"twist E^{-7}")
