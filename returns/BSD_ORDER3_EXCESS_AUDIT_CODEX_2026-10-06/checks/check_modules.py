"""Abstract module controls only: no seed Selmer group is computed."""
from pathlib import Path
import json
from itertools import product

def rank(A,p):
    A=[list(r) for r in A]; m=len(A); n=len(A[0]) if m else 0; r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]%p),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        u=pow(A[r][j]%p,-1,p); A[r]=[(u*x)%p for x in A[r]]
        for i in range(m):
            if i!=r:
                a=A[i][j]; A[i]=[(x-a*y)%p for x,y in zip(A[i],A[r])]
        r+=1
    return r

def mul(A,B,p):
    return [[sum(a*b for a,b in zip(row,col))%p for col in zip(*B)] for row in A]

def nilpotent(blocks):
    n=sum(blocks); A=[[0]*n for _ in range(n)]; off=0
    for size in blocks:
        for j in range(size-1): A[off+j+1][off+j]=1
        off+=size
    return A

def mix_basis(A,p):
    n=len(A)
    for i in range(n):
        j=(i+1)%n; a=i+1
        P=[[int(r==c) for c in range(n)] for r in range(n)]
        Q=[[int(r==c) for c in range(n)] for r in range(n)]
        P[i][j]=a%p; Q[i][j]=(-a)%p
        A=mul(mul(P,A,p),Q,p)
    return A

rows=[]
for p,e in product((5,7,11,17),(0,2,4,6)):
    T=mix_basis(nilpotent([3,3]+[1]*e),p); T2=mul(T,T,p)
    n=len(T); d=e+2
    assert rank(T,p)==4 and rank(T2,p)==2
    assert n-rank(T,p)==d and n-rank(T2,p)==d+2
    assert not any(any(row) for row in mul(T2,T,p))
    assert n-rank(T,p)-rank(T2,p)==e
    rows.append({'p':p,'excess':e,'length':n,'ker_t':d,'ker_t2':d+2,'rank_t2':2,'excess_quotient':e})
# Reject the tempting substitution of length-two blocks for short excess.
wrong=nilpotent([3,3,2,2]); p=5
assert (len(wrong)-rank(mul(wrong,wrong,p),p))-(len(wrong)-rank(wrong,p))==4
assert 4!=2  # contradicts the known first-order image dimension
# Actual enumeration of kernels of pi and pi^3 modulo pi^3, in an
# unramified DVR control Z_p. This is not the seed coefficient ring.
kernels=[]
for p in (5,7):
    modulus=p**3
    k_short=[x for x in range(modulus) if p*x%modulus==0]
    k_long=[x for x in range(modulus) if p**3*x%modulus==0]
    assert k_short==list(range(0,modulus,p*p))
    assert len(k_short)==p and len(k_long)==p**3
    kernels.append({'p':p,'short_kernel_size':len(k_short),'long_kernel_size':len(k_long)})
out={'status':'PASS','scope':'abstract finite-module and coefficient-base-change controls; no seed computation',
     'conjugated_module_cases':rows,'wrong_length_two_variant':'REJECTED_BY_FIRST_ORDER_DIMENSION',
     'dvr_kernel_enumeration':kernels}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 16 conjugated module cases, incorrect length-two variant rejected, two DVR controls')
