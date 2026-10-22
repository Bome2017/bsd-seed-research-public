"""Exact abstract polynomial control; no seed arithmetic or proof certification."""
import itertools
import json

def add(a,b):
    c=a.copy()
    for k,v in b.items():
        c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}

def mul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            c[(i+k,j+l)]=c.get((i+k,j+l),0)+x*y
    return {k:v for k,v in c.items() if v}

def scale(a,s): return {k:s*v for k,v in a.items() if s*v}
def det(A):
    ans={}
    for perm in itertools.permutations(range(len(A))):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(len(A)) for j in range(i+1,len(A)))
        term={(0,0):sign}
        for i,j in enumerate(perm): term=mul(term,A[i][j])
        ans=add(ans,term)
    return ans

P={(1,0):1}; U={(0,1):1}; Z={}
D=[[P,U,Z,Z],[Z,P,U,Z],[Z,Z,Z,U]]
eta=[mul(U,U),scale(mul(P,U),-1),mul(P,P),Z]
assert all(not sumrow for sumrow in [__import__('functools').reduce(add,(mul(x,y) for x,y in zip(row,eta)),{}) for row in D])
minors=[scale(det([[x for k,x in enumerate(row) if k!=j] for row in D]),(-1)**j) for j in range(4)]
assert minors==[mul(U,x) for x in eta]
upper=D[:2]
ideals=[det([[row[i],row[j]] for row in upper]) for i,j in [(0,1),(0,2),(1,2)]]
assert ideals==[mul(P,P),mul(P,U),mul(U,U)]
print(json.dumps({'status':'PASS','ring':'Z[P,U]','checks':['D eta = 0','signed maximal minors = U eta','upper-block minors = P^2, P U, U^2'],'scope':'abstract identities only; no seed value or independent proof certification'},indent=2))
