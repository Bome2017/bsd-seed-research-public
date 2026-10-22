"""Independent literal-coordinate checks and non-certifying real-period cross-check."""
from pathlib import Path
import csv,json,math
import mpmath as mp
B=Path(__file__).resolve().parent
rows=[{k:int(v) for k,v in r.items()} for r in csv.DictReader((B/'independent_counts.csv').open())]
checked=affine=duplications=0;errors=[]
for r in rows:
    p=r['p']
    if p>=500: break
    e={(u,v) for u in range(p) for v in range(p) if (v*v+u*v+v-u*u*u-u*u+2*u+1)%p==0}
    c={(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x-17*x*x-64*x)%p==0}
    image={((4*(u-1))%p,(8*v+4*u+4)%p) for u,v in e}
    inv4=pow(4,-1,p);inv8=pow(8,-1,p)
    back={((x*inv4+1)%p,((y-x-8)*inv8)%p) for x,y in c}
    if len(e)+1!=r['N_min'] or len(c)+1!=r['N_descent'] or image!=c or back!=e:errors.append(('models',p))
    T=(-8%p,8%p)
    if T not in c:errors.append(('T_on_curve',p))
    half=False
    for x,y in c:
        if not y: continue
        lam=((3*x*x+34*x+64)*pow(2*y,-1,p))%p
        xd=(lam*lam-17-2*x)%p;yd=(-y+lam*(x-xd))%p
        xp=((x*x-64)*pow(2*y,-1,p))**2%p
        if xp!=xd:errors.append(('duplication',p,x,y))
        if (x,y)==T and (xd,yd)!=(0,0):errors.append(('T_order',p))
        if (xd,yd)==T:half=True
        duplications+=1
    if r['chi33']==-1 and half!=(r['chi_neg2']==1):errors.append(('halving',p))
    checked+=1;affine+=len(e)
mp.mp.dps=100
ap={r['p']:r['trace'] for r in rows};ap.update({2:1,3:-1,11:-1})
limit=700
spf=list(range(limit+1))
for p in range(2,math.isqrt(limit)+1):
    if spf[p]==p:
        for n in range(p*p,limit+1,p):
            if spf[n]==n:spf[n]=p
coeff=[0]*(limit+1);coeff[1]=1
for n in range(2,limit+1):
    p=spf[n];t=n;e=0
    while t%p==0:t//=p;e+=1
    u,v=1,ap[p]
    if e==1:z=v
    elif p in (2,3,11):z=v**e
    else:
        for _ in range(2,e+1):u,v=v,ap[p]*v-p*u
        z=v
    coeff[n]=z*coeff[t]
L=2*mp.fsum(mp.mpf(coeff[n])/n*mp.exp(-2*mp.pi*n/mp.sqrt(66)) for n in range(1,limit+1))
s=mp.sqrt(33);e2=(-17+s)/2;e3=(-17-s)/2
omega_plus_C=2*mp.ellipk((e2-e3)/(-e3))/mp.sqrt(-e3)
omega_plus_E=2*omega_plus_C;omega_full_E=2*omega_plus_E
out={'literal_checks':{'primes_below500':checked,'affine_points_per_model':affine,'nonzero_y_duplications':duplications,'errors':errors},'period_numerical_crosscheck':{'precision_decimal_digits':100,'fourier_cutoff':limit,'assumed_functional_equation_sign':1,'L_at_1':str(L),'least_period_E':str(omega_plus_E),'full_period_E':str(omega_full_E),'L_over_least':str(L/omega_plus_E),'L_over_full':str(L/omega_full_E),'warning':'Numerical cross-check only; exact rational L-ratio remains established curve data, not proved by floating-point coincidence.'}}
(B/'independent_literal_and_period.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
