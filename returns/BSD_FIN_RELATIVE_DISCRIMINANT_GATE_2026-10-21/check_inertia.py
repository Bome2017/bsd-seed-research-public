#!/usr/bin/env python3
"""Exact orbit checks only; actual elliptic local inertia is a retained input."""
from math import isqrt

PRIMES = [5, 7, 11, 13, 17, 23, 31, 53, 83]

def prime(p):
    return p >= 5 and all(p%d for d in range(2,isqrt(p)+1))

def canon(v,p):
    return min(v,(-v[0]%p,-v[1]%p))

def j(v,p):
    return (-v[1]%p,v[0])

def u(v,p):
    return ((v[0]+v[1])%p,v[1])

def orbits(vertices,fn):
    unseen=set(vertices)
    count=0
    while unseen:
        v0=next(iter(unseen));v=v0
        while True:
            assert v in unseen or v==v0
            unseen.discard(v)
            v=fn(v)
            if v==v0: break
        count+=1
    return count

def test(p):
    assert prime(p) and p!=4547
    X={(x,y) for x in range(p) for y in range(p) if x or y}
    Y={canon(v,p) for v in X}
    n=p*p-1
    assert len(X)==n and len(Y)==n//2
    assert all(j(j(v,p),p)==(-v[0]%p,-v[1]%p) for v in X)
    jA=orbits(X,lambda v:j(v,p))
    jK=orbits(Y,lambda v:canon(j(v,p),p))
    uA=orbits(X,lambda v:u(v,p))
    uK=orbits(Y,lambda v:canon(u(v,p),p))
    assert (jA,jK,uA,uK)==(n//4,n//4,2*(p-1),p-1)
    expA=n-jA
    expK=n//2-jK
    mulA=n-uA
    mulK=n//2-uK
    assert expA==3*n//4 and expK==n//4 and expA-2*expK==n//4
    assert mulA==(p-1)**2 and mulK==(p-1)**2//2 and mulA-2*mulK==0
    assert 4547>16
    return p,n,expA,expK,expA-2*expK,mulA-2*mulK

if __name__=="__main__":
    print("p n v4547(DA) v4547(DK) v4547(delta) v_mult(delta)")
    rows=[test(p) for p in PRIMES]
    assert rows[0]==(5,24,18,6,6,0)
    for r in rows: print(*r)
    print("PASS: nine independent finite-group orbit checks; no Sha or class-group conclusion")
