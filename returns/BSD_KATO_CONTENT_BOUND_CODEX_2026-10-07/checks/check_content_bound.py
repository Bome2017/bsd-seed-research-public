"""Exact presentation controls, including finite modules invisible at height one.

These are algebra models, not computed seed cohomology or Sha groups.
Polynomials are retained modulo U^2: that is all the minor derivative uses.
"""
from itertools import combinations, product
from math import gcd
from functools import reduce
import random, json

ZERO=(0,0)
def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def times(x,y): return (x[0]*y[0],x[0]*y[1]+x[1]*y[0])
def determinant(M):
    if not M:return (1,0)
    total=ZERO
    for j,x in enumerate(M[0]):
        sub=[r[:j]+r[j+1:] for r in M[1:]]
        term=times(x,determinant(sub))
        total=plus(total,term if j%2==0 else neg(term))
    return total
def minors(M):
    return [tuple((-1)**j*x for x in determinant([row[:j]+row[j+1:] for row in M]))
            for j in range(len(M)+1)]
def val(n,p):
    if n==0:return float('inf')
    out=0
    while n%p==0:n//=p;out+=1
    return out
def torsion_length(M,p):
    n=len(M); k=n-1
    vals=[]
    for rows in combinations(range(n),k):
        for cols in combinations(range(n+1),k):
            vals.append(determinant([[M[i][j] for j in cols] for i in rows])[0])
    d=reduce(gcd,vals,0)
    assert d!=0
    return val(d,p)
def matvec(M,v):
    return [reduce(plus,(times(x,y) for x,y in zip(row,v)),ZERO) for row in M]

rng=random.Random(7102026)
cases=[]
for p,a,b,s,kind in product([5,7,17],range(4),range(4),range(3),['diagonal','finite_error']):
    if kind=='diagonal':
        M=[[(p**a,0),ZERO,ZERO,ZERO],
           [ZERO,(p**b,0),ZERO,ZERO],
           [ZERO,ZERO,(0,1),ZERO]]
        eta=[ZERO,ZERO,ZERO,(-1,0)]
        d1=p**(a+b); g=p**(a+b+s)
    else:
        M=[[(p**b,0),ZERO,ZERO,ZERO],
           [ZERO,(p**a,0),(0,1),ZERO],
           [ZERO,ZERO,ZERO,(0,1)]]
        eta=[ZERO,(0,-1),(p**a,0),ZERO]
        d1=p**b; g=p**(b+s)
    # Exact elementary polynomial basis changes, each of determinant one.
    for _ in range(7):
        f=(rng.randint(-4,4),rng.randint(-3,3))
        if rng.randrange(2):
            i,j=rng.sample(range(len(M)),2)
            M[i]=[plus(x,times(f,y)) for x,y in zip(M[i],M[j])]
        else:
            j,k=rng.sample(range(len(M)+1),2)
            for row in M:row[j]=plus(row[j],times(f,row[k]))
            eta[k]=plus(eta[k],neg(times(f,eta[j])))
    assert matvec(M,eta)==[ZERO]*len(M)
    md=minors(M)
    assert all(x[0]==0 for x in md)
    assert [x[1] for x in md]==[d1*x[0] for x in eta]
    tau=torsion_length(M,p)
    m=min(val(g*x[0],p) for x in eta)
    assert tau==a+b and m==a+b+s
    assert tau<=m
    cases.append((p,kind,tau,m))

# An explicit codimension-two error survives specialization although char X=(U).
p=5
M=[[(p**2,0),(0,1),ZERO],[ZERO,ZERO,(0,1)]]
assert torsion_length(M,p)==2
assert [x[1] for x in minors(M)]==[0,-p**2,0]

# Omitting the (p)-inequality permits primitive derivative with excess torsion.
bad=[[(p,0),ZERO,ZERO,ZERO],[ZERO,(p,0),ZERO,ZERO],
     [ZERO,ZERO,(0,1),ZERO]]
assert torsion_length(bad,p)==2
omitted_p={'tau':2,'derivative_content':0,'U_local_bound_holds':True,
           'p_local_bound_holds':False,'full_hypotheses_satisfied':False}

# Supplied review's exact residue and fixed-smoothing arithmetic.
N=2**3*3*2243*4547**2*5843
c,d=1+6*N,1+12*N
assert (c%17,d%17,c*d*(c-1)*(d-1)%17)==(11,4,11)
assert c%5==0
rho=11
peps=rho*(17-rho)*pow(rho-1,-1,17)%17
assert peps==10
coord=[peps*pow(13,-1,17)*x%17 for x in [16,6]]
assert coord==[11,2]

print(json.dumps({'presentation_cases':len(cases),'status':'PASS',
 'finite_specialization_error_retained':True,
 'missing_p_inequality_countercontrol':omitted_p,
 'review_residue_multiplier_mod17':coord,
 'fixed_smoothing_mod17':[c%17,d%17],
 'fixed_smoothing_augmentation_mod17':11,
 'fixed_smoothing_excludes_5':True,
 'seed_kato_value_computed':False,'new_seed_primary_result':False},indent=2))
