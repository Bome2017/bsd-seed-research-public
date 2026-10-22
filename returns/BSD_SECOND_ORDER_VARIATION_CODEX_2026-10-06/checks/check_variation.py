#!/usr/bin/env python3
"""Exact algebra controls; no seed Selmer or arithmetic-character evaluation."""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import random

COUNTS = Counter()
RNG = random.Random(20261006)

def check(name, statement):
    assert statement, name
    COUNTS[name] += 1

MON = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
POS = {m: i for i, m in enumerate(MON)}

def mul(x, y, p):
    out = [0]*6
    for i, (a,b) in enumerate(MON):
        for j, (c,d) in enumerate(MON):
            if a+b+c+d < 3:
                out[POS[a+c,b+d]] += x[i]*y[j]
    return tuple(v % p for v in out)

def exp2(a,b,p):
    h = pow(2,-1,p)
    return (1,a%p,b%p,a*a*h%p,a*b%p,b*b*h%p)

def e(x,y,p):
    return (x[0]*y[1]-x[1]*y[0]) % p

def J(x,y,p):
    return (e(x[2:],y[:2],p)-e(x[:2],y[2:],p)) % p

def tv(x):
    return (0,0,x[0],x[1])

def matvec(g,v,p):
    return ((g[0]*v[0]+g[1]*v[1])%p,(g[2]*v[0]+g[3]*v[1])%p)

def act(g,a,x,p):
    lo=matvec(g,x[:2],p)
    hi=matvec(g,x[2:],p)
    return lo+tuple((hi[i]+a*lo[i])%p for i in range(2))

def rank(rows,p):
    a=[list(r) for r in rows]
    r=0
    for j in range(len(a[0])):
        at=next((i for i in range(r,len(a)) if a[i][j]%p),None)
        if at is None:
            continue
        a[r],a[at]=a[at],a[r]
        inv=pow(a[r][j]%p,-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                c=a[i][j]%p
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):
            break
    return r

def commutator_control(p):
    # Actual class-2 group with central law dictated by the primitive equation.
    d=3
    def beta(v,w):
        lifted=[J(v[i],w[j],p) for i in range(d) for j in range(d)]
        old=[e(w[j][:2],v[i][:2],p) for i in range(d) for j in range(d)]
        return tuple(lifted+old)
    zero=tuple((0,0,0,0) for _ in range(d))
    z0=(0,)*(2*d*d)
    def times(x,y):
        v,a=x; w,b=y
        u=tuple(tuple((r+s)%p for r,s in zip(vi,wi)) for vi,wi in zip(v,w))
        return u,tuple((r+s-t)%p for r,s,t in zip(a,b,beta(v,w)))
    def inverse(x):
        v,a=x
        return tuple(tuple(-r%p for r in vi) for vi in v),tuple((-r-s)%p for r,s in zip(a,beta(v,v)))
    v=((0,0,1,0),(0,0,0,0),(0,0,0,0))
    w=((0,0,0,0),(0,1,0,0),(0,0,0,0))
    a=(v,z0); b=(w,z0)
    c=times(times(times(a,b),inverse(a)),inverse(b))
    check('commutator_zero_evaluation',c[0]==zero)
    check('commutator_all_old_rows_zero',all(z==0 for z in c[1][d*d:]))
    check('commutator_lifted_12_is_minus_one',c[1][1]==p-1)
    check('commutator_lifted_21_is_plus_one',c[1][d]==1)
    check('commutator_formula',c[1]==tuple((-r+s)%p for r,s in zip(beta(v,w),beta(w,v))))
    for _ in range(80):
        x=(tuple(tuple(RNG.randrange(p) for _ in range(4)) for _ in range(d)),tuple(RNG.randrange(p) for _ in z0))
        y=(tuple(tuple(RNG.randrange(p) for _ in range(4)) for _ in range(d)),tuple(RNG.randrange(p) for _ in z0))
        z=(tuple(tuple(RNG.randrange(p) for _ in range(4)) for _ in range(d)),tuple(RNG.randrange(p) for _ in z0))
        check('class2_associativity',times(times(x,y),z)==times(x,times(y,z)))
        check('class2_inverse',times(x,inverse(x))==(zero,z0))

for p in (5,7,11,13,17):
    if p<=7:
        for a,b,c,d in product(range(p),repeat=4):
            check('actual_truncated_character_law',mul(exp2(a,b,p),exp2(c,d,p),p)==exp2(a+c,b+d,p))
    for a,b in product(range(p),repeat=2):
        v=exp2(a,b,p)
        check('diagonal_second_coefficient',sum(v[3:])%p==(a+b)**2*pow(2,-1,p)%p)
        check('mixed_pointwise_product',v[4]==a*b%p)
        # pi=u+u^2/2, hence (1+pi)^a=exp(a*u) modulo u^3.
        check('root_of_unity_coordinate', (a*pow(2,-1,p)+a*(a-1)*pow(2,-1,p))%p==a*a*pow(2,-1,p)%p)
    for _ in range(350):
        x=tuple(RNG.randrange(p) for _ in range(4))
        y=tuple(RNG.randrange(p) for _ in range(4))
        z=tuple(RNG.randrange(p) for _ in range(2))
        check('J_symmetric',J(x,y,p)==J(y,x,p))
        check('t_skew_adjoint',(J(tv(x),y,p)+J(x,tv(y),p))%p==0)
        check('diagram_dual_pullback_sign',J(y,(0,0)+z,p)==-e(y[:2],z,p)%p)
        g=tuple(RNG.randrange(p) for _ in range(4)); a=RNG.randrange(p)
        det=(g[0]*g[3]-g[1]*g[2])%p
        if det:
            check('J_Galois_equivariance',J(act(g,a,x,p),act(g,a,y,p),p)==det*J(x,y,p)%p)
    commutator_control(p)
    for d in (2,3,5):
        # Arbitrary top corrections; add actual t-images as required by (I,1).
        for _ in range(40):
            rows=[]
            for j in range(2*d):
                lo=[int(i==j) for i in range(2*d)]
                hi=[RNG.randrange(p) for _ in range(2*d)]
                rows.extend([lo+hi,[0]*(2*d)+lo])
            check('Nakayama_full_evaluation_model',rank(rows,p)==4*d)
        constants=[[int(i==j) for i in range(4*d)] for j in range(2*d)]
        check('without_t_stability_countercontrol',rank(constants,p)==2*d<4*d)
    for a,b in product(range(1,p),repeat=2):
        values={(a*x*x+b*y*y)%p for x,y in product(range(p),repeat=2)}
        check('every_binary_nondegenerate_diagonal_form_surjective',values==set(range(p)))
    for _ in range(100):
        a,b=RNG.randrange(1,p),RNG.randrange(1,p)
        l,m,c=(RNG.randrange(p) for _ in range(3))
        values={(a*x*x+b*y*y+l*x+m*y+c)%p for x,y in product(range(p),repeat=2)}
        check('affine_fiber_all_values_attained',values==set(range(p)))
        v,w=l*pow(2*a,-1,p)%p,m*pow(2*b,-1,p)%p
        x,y=RNG.randrange(p),RNG.randrange(p)
        check('completing_square_sign',(a*x*x+b*y*y+l*x+m*y+c-a*(x+v)**2-b*(y+w)**2+a*v*v+b*w*w-c)%p==0)
    # A fixed b-map with kernel of dimension two and a mixed polar form.
    for _ in range(150):
        a,b=RNG.randrange(1,p),RNG.randrange(1,p)
        c,d,e0=(RNG.randrange(p) for _ in range(3))
        def q(v):
            z,x,y=v
            return (a*x*x+b*y*y+c*z*x+d*z*y+e0*z*z)%p
        def polar(v,w):
            return (q(tuple(x+y for x,y in zip(v,w)))-q(v)-q(w))%p
        l=tuple(RNG.randrange(p) for _ in range(3))
        mu=(0,RNG.randrange(p),RNG.randrange(p))
        nu=(0,RNG.randrange(p),RNG.randrange(p))
        check('polar_bilinearity',polar(l,tuple(x+y for x,y in zip(mu,nu)))==(polar(l,mu)+polar(l,nu))%p)
        check('fixed_b_fiber_has_zero',any(q((l[0],x,y))==0 for x,y in product(range(p),repeat=2)))
    check('nonzero_isotropic_ternary',any(x*x+y*y+z*z!=0 and (x*x+y*y+z*z)%p==0 for x,y,z in product(range(p),repeat=3)))

check('variation_alone_not_sufficient',0 not in {(x*x+2)%5 for x in range(5)})

result={'status':'PASS','total_assertions':sum(COUNTS.values()),'counts':dict(sorted(COUNTS.items())),
        'domain':'exact finite algebra at p=5,7,11,13,17',
        'not_checked':['seed Selmer classes','Chebotarev field realization','global or local Galois cohomology','full-S Stage-A theorem','independent mathematical proof acceptance'],
        'seed_character_computed':False,'FIN_changed':False,'ORDER9_changed':False,'Q36_changed':False}
out=Path(__file__).with_name('RESULTS.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'total_assertions':result['total_assertions'],'output':str(out)}))
