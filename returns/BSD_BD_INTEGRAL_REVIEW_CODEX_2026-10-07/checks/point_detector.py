"""Bounded local-detector control. No Gross values or Sha computation."""
import json, math
A2,A4,A6=-1,-66020924,-65074271436
POINTS=[(-3031,327384),(-2394,281520)]
N=6503188012738584

def prime(n): return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def rhs(x,q):return (x*x*x+A2*x*x+A4*x+A6)%q

def add(P,Q,q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v)%q==0:return None
    slope=((v-y)*pow(u-x,-1,q) if x!=u else (3*x*x+2*A2*x+A4)*pow(2*y,-1,q))%q
    xx=(slope*slope-A2-x-u)%q
    return xx,(slope*(x-xx)-y)%q

def mul(n,P,q):
    r=None
    while n:
        if n&1:r=add(r,P,q)
        P=add(P,P,q);n//=2
    return r

def count(q):return 1+sum(1 if rhs(x,q)==0 else 2 if pow(rhs(x,q),(q-1)//2,q)==1 else 0 for x in range(q))
def coords(q,order,p):
    images=[mul(order//p,(x%q,y%q),q) for x,y in POINTS]
    G=next((X for X in images if X is not None),None)
    if G is None:return [0,0]
    assert mul(p,G,q) is None
    table={mul(k,G,q):k for k in range(p)}
    return [table[X] for X in images]

for x,y in POINTS:assert y*y==x*x*x+A2*x*x+A4*x+A6
q=283;order=count(q)
assert order==288
negative={'ell':q,'a_ell':q+1-order,'order_Fell':order,'coefficient_primes':[5,7],'epsilon':-1,'rational_point_classes':'zero: order_Fell prime to 5 and 7'}
assert all(math.gcd(order,p)==1 and (q+1+(q+1-order))%p==0 and (q*q-1)%p for p in (5,7))
pairs={}
for p, qs in [(5,[73,223]),(7,[173,367]),(11,[47,271])]:
    entries=[]
    for q in qs:
        assert prime(q) and N%q and pow((-7)%q,(q-1)//2,q)==q-1 and (q*q-1)%p
        order=count(q);assert order%p==0
        entries.append({'ell':q,'a_ell':q+1-order,'order_Fell':order,'epsilon':1,'row':coords(q,order,p)})
    a,b=(e['row'] for e in entries)
    determinant=(a[0]*b[1]-a[1]*b[0])%p
    pairs[str(p)]={'entries':entries,'determinant':determinant}
print(json.dumps({'status':'PASS' if all(x['determinant'] for x in pairs.values()) else 'SOME_PAIR_DEGENERATE','negative_control':negative,'positive_controls':pairs,'meaning':'local point detector only; no Gross value, C invariant, or Sha computation'},indent=2))
