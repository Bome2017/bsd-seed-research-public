#!/usr/bin/env python3
"""Independent printed-Arb-interval arithmetic checker for an Ota singleton.

Uses no producer candidates, unique flags, prediction, or frozen checker code.
This does NOT independently produce modular symbols, certify the coefficient
corpus, or establish that the printed balls enclose the true symbols.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path
import re
import sys

class Invalid(ValueError):
    pass

def demand(condition, reason):
    if not condition:
        raise Invalid(reason)

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def decimal(s):
    demand(bool(re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',s)),
           'not a finite decimal: '+s)
    return Fraction(s)

def ball(s):
    """Printed midpoint +/- radius, zero-centered, or exact singleton."""
    s=s.strip()
    if '+/-' in s:
        a=s.split('+/-')
        demand(len(a)==2,'multiple +/- tokens')
        m=decimal(a[0].strip()) if a[0].strip() else Fraction(0)
        r=decimal(a[1].strip())
        demand(r>=0,'negative radius')
    else:
        m,r=decimal(s),Fraction(0)
    return m-r,m+r,r

def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)

def identify(text,ell,den):
    rows={}
    radii=[]
    for lineno,line in enumerate(text.splitlines(),1):
        if not re.match(r'^XB(?:\s|$)',line):
            continue
        m=re.match(r'^XB\s+(\d+)\s+plus\s+\[([^\]]+)\](?:\s|$)',line)
        demand(m is not None,f'malformed XB symbol line {lineno}')
        a=int(m.group(1))
        demand(1<=a<ell,f'out-of-range symbol label {a}')
        demand(a not in rows,f'duplicate symbol label {a}')
        lo,hi,r=ball(m.group(2))
        lo,hi=lo*den,hi*den
        low=ceil_fraction(lo)
        high=hi.numerator//hi.denominator
        demand(low==high,f'label {a}: lattice interval contains {max(0,high-low+1)} candidates')
        rows[a]=Fraction(low,den)
        radii.append(r)
    demand(set(rows)==set(range(1,ell)),
           'incomplete label set: missing '+str(sorted(set(range(1,ell))-set(rows))))
    for a in range(1,ell):
        demand(rows[a]==rows[ell-a],f'plus symmetry failed at {a}')
    return rows,max(radii)

def log_table(g,ell):
    table={}
    a=1
    for k in range(ell-1):
        demand(a not in table,f'generator {g} is not primitive modulo {ell}')
        table[a]=k
        a=a*g%ell
    demand(a==1 and len(table)==ell-1,'generator cycle incomplete')
    return table

def residue(x,p):
    demand(x.denominator%p!=0,'nonintegral coefficient at p')
    return x.numerator*pow(x.denominator,-1,p)%p

def coefficients(rows,logs,p):
    c=[Fraction(0),Fraction(0),Fraction(0)]
    for a,s in rows.items():
        x=logs[a]%p
        c[0]+=s
        c[1]+=x*s
        c[2]+=(x*(x-1)//2)*s
    return c

def verify(text,p,ell,g=None,den=1024,gpower=3):
    demand(is_prime(p) and p>=5,'p must be a prime at least five')
    demand(is_prime(ell) and ell!=p,'ell must be a distinct prime')
    demand((ell-1)%p==0 and (ell-1)%(p*p)!=0,'requires v_p(ell-1)=1')
    demand(den>0 and gcd(den,p)==1,'lattice denominator not a positive p-unit')
    demand(gcd(gpower,ell-1)==1,'generator power is not coprime to ell-1')
    if g is None:
        for candidate in range(2,ell):
            try:
                logs=log_table(candidate,ell)
                g=candidate
                break
            except Invalid:
                pass
        demand(g is not None,'no primitive root found')
    else:
        demand(1<g<ell,'generator out of range')
        logs=log_table(g,ell)
    rows,maxradius=identify(text,ell,den)
    c=coefficients(rows,logs,p)
    demand(c[0]==0,'c0 is not exactly zero')
    demand(residue(c[1],p)==0,'c1 is not zero modulo p')
    altg=pow(g,gpower,ell)
    alt=coefficients(rows,log_table(altg,ell),p)
    demand(alt[0]==0 and residue(alt[1],p)==0,'alternate generator lower terms fail')
    scaling=pow(gpower,-2,p)
    demand(residue(alt[2],p)==scaling*residue(c[2],p)%p,
           'generator-change c2 scaling failed')
    lattice_numerators=[int(rows[a]*den) for a in range(1,ell)]
    canonical=json.dumps(lattice_numerators,separators=(',',':')).encode()
    return {
      'status':'OUTPUT_INTERVAL_ARITHMETIC_PASS',
      'scope':'printed interval arithmetic only; not independent coefficient production or source authentication',
      'mathematical_witness':'NONZERO' if residue(c[2],p) else 'INCONCLUSIVE_ZERO',
      'p':p,'ell':ell,'lattice_denominator':den,'labels':len(rows),
      'generator':g,'coefficients_exact':[str(x) for x in c],
      'coefficients_mod_p':[residue(x,p) for x in c],
      'alternate_generator_power':gpower,'alternate_generator':altg,
      'alternate_coefficients_exact':[str(x) for x in alt],
      'alternate_coefficients_mod_p':[residue(x,p) for x in alt],
      'c2_expected_scaling_mod_p':scaling,'generator_scaling_pass':True,
      'max_printed_radius':str(maxradius),
      'lattice_numerators_sha256':sha256(canonical).hexdigest(),
      'lattice_numerators_in_label_order':lattice_numerators,
      'printed_candidates_and_unique_flags':'NOT_READ',
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('msl',type=Path)
    parser.add_argument('--p',required=True,type=int)
    parser.add_argument('--ell',required=True,type=int)
    parser.add_argument('--generator',type=int)
    parser.add_argument('--denominator',default=1024,type=int)
    parser.add_argument('--generator-power',default=3,type=int)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    payload=args.msl.read_bytes()
    try:
        result=verify(payload.decode(),args.p,args.ell,args.generator,
                      args.denominator,args.generator_power)
        code=0
    except (Invalid,UnicodeError) as error:
        result={'status':'INVALID_OUTPUT_INTERVAL_ARITHMETIC','reason':str(error),
                'p':args.p,'ell':args.ell}
        code=2
    result['msl_sha256']=sha256(payload).hexdigest()
    result['verifier_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    result['input_path']=str(args.msl.resolve())
    output=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:
        args.out.write_text(output)
    print(output,end='')
    return code

if __name__=='__main__':
    sys.exit(main())
