#!/usr/bin/env python3
"""Exact p-torsion packing test. Neither class orders nor Sha are supplied."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent

def ceil(x): return -(-x.numerator//x.denominator)
def qj(x): return [str(x.numerator),str(x.denominator)]
def cosh_square_upper(z,terms=16):
    # cosh(sqrt(z)); positive series with exact geometric-tail majorant.
    assert 0<=z<=8
    s=sum((z**k/F(factorial(2*k)) for k in range(terms)),F(0))
    first=z**terms/F(factorial(2*terms))
    ratio=z/F((2*terms+1)*(2*terms+2))
    return s+first/(1-ratio)
def sep_upper(X,R,p=5):
    sinh4=((cosh_square_upper(8*R*R)-1)/2)**2
    cosh16=cosh_square_upper(R*R)**16
    return 2**24*X**(4*p)*sinh4*cosh16

def floor_log(n,p):
    k=0
    while p**(k+1)<=n:k+=1
    return k

def main():
    a=json.loads((H/'RETAINED_ANALYTIC_INPUT.json').read_text())
    data=json.loads((H.parent/'arithmetic/RESULT.json').read_text())
    rows=next(r for r in data['range_results'] if r['source_variant']=='original_EV_absolute_class_range')['pairs']
    assert len(rows)==26 and len({(x['q'],x['prime_index'],x['conjugate_index']) for x in rows})==26
    delta=int(data['relative_discriminant_norm'])
    assert delta==2**4*5*4547**6
    pi=F(int(a['pi_interval'][0]['numerator']),int(a['pi_interval'][0]['denominator']))
    # Conservative exact replay of h_relative * R_A/R_K analytic bound.
    C=F(int(a['sqrtQ_upper_integer'])*int(a['L_value_upper_ceiling']))/(2*pi)**6
    assert C<42*10**71
    v6=pi**3/6
    outputs=[]
    for X in sorted(set(x['norm'] for x in rows)):
        M=sum(x['norm']<=X for x in rows)
        lo=F(0); hi=F(7,X)**5
        assert sep_upper(X,hi)>delta
        for _ in range(24):
            mid=(lo+hi)/2
            if sep_upper(X,mid)<delta:lo=mid
            else:hi=mid
        assert 0<lo<1 and sep_upper(X,lo)<delta
        # 2*R<2<lambda_lower verifies each ball's unit-lattice injectivity.
        B=4*C/(M*v6*lo**6)
        N=ceil(B)
        outputs.append({'max_norm':X,'pairs':M,'radius_lower':qj(lo),'radius_upper_for_this_test':qj(hi),'separation_upper_over_delta':qj(F(ceil(sep_upper(X,lo)/delta*10**12),10**12)),'torsion_order_upper_integer':str(N),'five_torsion_rank_upper':floor_log(N,5)})
    best=min(outputs,key=lambda r:int(r['torsion_order_upper_integer']))
    assert best['max_norm']==7 and best['pairs']==2
    out={'status':'EXPLICIT_PRIMARY_PACKING_BOUND_WEAKER_THAN_RETAINED_BOUND','complete_relative_5_torsion':True,'counts':'tau-pairs over distinct K primes, not individual A prime ideals','analytic_product_upper_coarse_integer':str(42*10**71),'analytic_input_sha256':hashlib.sha256((H/'RETAINED_ANALYTIC_INPUT.json').read_bytes()).hexdigest(),'arithmetic_input_sha256':hashlib.sha256((H.parent/'arithmetic/RESULT.json').read_bytes()).hexdigest(),'best':best,'all_prefixes':outputs,'retained_better_rank_bound':97,'new_small_bound':False,'hypotheses':'written compact group and separation proof; retained field and analytic inputs; no GRH or Sha input','scope':'bound on p-torsion rank, NOT total p-primary length'}
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
