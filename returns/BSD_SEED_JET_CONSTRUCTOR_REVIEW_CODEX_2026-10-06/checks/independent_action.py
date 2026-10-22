#!/usr/bin/env python3
"""Independent logarithm-series and rational Mobius controls; no global symbols."""
from pathlib import Path
from fractions import Fraction
from random import Random
import json,sys
base=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(base/'input/BSD_SEED_JET_CONSTRUCTOR_2026-10-06'))
from jet_module import JetModule,COORDS,moments

def ratmod(x,p,k):
    return x.numerator*pow(x.denominator,-1,p**k)%p**k

def logarithm(x,p):
    v=x**(p-1)-1
    numerator=sum((Fraction((-1)**(n+1)*v**n,n*p) for n in range(1,25)),Fraction(0))
    denominator=sum((Fraction((-1)**(n+1)*p**(n-1),n) for n in range(1,25)),Fraction(0))
    return ratmod(numerator,p,4)*pow((p-1)*ratmod(denominator,p,4),-1,p**4)%p**4

def run():
    rng=Random(1040601);count=0
    for p in [17,31,101]:
        module=JetModule(p)
        for gamma in [(1,3,p,1),(2,-4,2*p,3),(-1,1,p,p),(1,2,0,p)]:
            action=module.action(gamma);a,b,c,d=gamma
            for _ in range(8):
                u,z=rng.randrange(p*p),rng.randrange(p*p)
                v=a+c*z;up=u+logarithm(v,p);zp=Fraction(b+d*z,v)
                want=[]
                for i,j in COORDS:
                    choose=Fraction(1)
                    for t in range(i):choose*=Fraction(up-t,t+1)
                    want.append(ratmod(choose*zp**j,p,4-i-j))
                assert module.apply(action,moments(u,z,p))==want
                count+=1
    return {'status':'PASS','independent_log_series_and_rational_mobius_controls':count,'primes':[17,31,101],'note':'Local coefficient/action checks, not global symbol authentication or a seed bound.'}

if __name__=='__main__':
    actual=run();expected=json.loads((base/'checks/INDEPENDENT_ACTION.json').read_text())
    assert actual==expected
    print(json.dumps(actual,indent=2))
