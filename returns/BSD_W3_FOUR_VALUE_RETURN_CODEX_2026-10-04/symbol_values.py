#!/usr/bin/env python3
"""Compute four residues from supplied integral symbols, not their provenance.

This is an arithmetic extraction stage, not a modular-symbol constructor.
It never certifies seed Sha vanishing from input arrays alone.
See ARITHMETIC_EXTRACTION.md for the mandatory source and normalization.
"""
import argparse
import hashlib
import json
from math import comb, isqrt
from pathlib import Path

N_SEED=6503188012738584
NODES=((3,2),(3,3),(4,3),(4,4))

def prime(n):
    return isinstance(n,int) and not isinstance(n,bool) and n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def canonical(x,modulus,label):
    if type(x) is not int or not 0<=x<modulus:
        raise ValueError(f'{label}: require an integer in [0,{modulus})')
    return x

def evaluate(data):
    p=data['p']
    if type(p) is not int or not 17<=p<=1000000 or not prime(p):
        raise ValueError('p must be a prime between 17 and 1000000')
    if N_SEED%p==0:raise ValueError('bad seed prime; outside this formula domain')
    if p in (19,59,487):raise ValueError('retained exceptional prime; outside the seed implication')
    if data.get('convention')!='source_phi_X_minus_zY_path_a_over_p_to_infinity':
        raise ValueError('missing exact source symbol convention')
    if data.get('N')!=N_SEED:raise ValueError('wrong seed conductor')
    m=p**4; fibers=data['fibers']; outputs=[]
    if set(fibers)!= {'3','4'}:raise ValueError('require exactly the two weight fibers 3,4')
    clean={}
    for w in (3,4):
        f=fibers[str(w)]; alpha=f.get('alpha_mod_p4')
        if alpha is not None:
            alpha=canonical(alpha,m,f'alpha_{w}')
            if alpha%p==0:raise ValueError('U_p value must be a unit')
        if f.get('modular_weight')!=w+2:raise ValueError('weight mismatch')
        if f.get('tame_character_exponent')!=-w:raise ValueError('nebentype mismatch')
        rows=f['symbols']; seen={}
        if len(rows)!=p-1:raise ValueError('require every cusp a/p exactly once')
        for row in rows:
            a=row['a']
            if type(a) is not int or not 1<=a<p or a in seen:raise ValueError('invalid or repeated cusp')
            c=row['coefficients']
            if len(c)!=4:raise ValueError('require h=0,1,2,3 at mixed precision')
            seen[a]=[canonical(c[h],p**(4-h),f'w={w},a={a},h={h}') for h in range(4)]
        clean[w]=(alpha,seen)
    for w,s in NODES:
        alpha,rows=clean[w]; value=0
        for a,c in rows.items():
            omega=pow(a,p**4,m)
            assert (omega-a)%p==0 and pow(omega,p-1,m)==1
            moment=sum(comb(s,h)*pow(comb(w,h),-1,m)*pow(a,s-h,m)*p**h*c[h]
                       for h in range(min(s,3)+1))%m
            value=(value+pow(omega,-s,m)*moment)%m
        raw=((-1)**s*value)%m
        J=value*pow(alpha,-1,m)%m if alpha is not None else None
        outputs.append({'w':w,'s':s,'unit_scaled_source_residue':raw,
                        'moment_residue':J,'source_residue':((-1)**s*J)%m if J is not None else None})
    return {'status':'ARITHMETIC_EXTRACTION_ONLY_SOURCE_NOT_AUTHENTICATED',
            'p':p,'modulus':m,'values':[x['source_residue'] for x in outputs],
            'details':outputs,'certificate_residues':[x['unit_scaled_source_residue'] for x in outputs],
            'any_nonzero':any(x['unit_scaled_source_residue'] for x in outputs),
            'all_divisible_p2':all(x['unit_scaled_source_residue']%(p*p)==0 for x in outputs),
            'source_verified':False,'seed_primary_certificate':False,
            'uniform_bound':False,
            'input_scope':'shape, precision and unit checks only; Hida, Hecke, primitivity, common frame and exceptional set require independent evidence'}

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('input',type=Path);ns=ap.parse_args()
    try:
        raw=ns.input.read_bytes(); result=evaluate(json.loads(raw)); result['input_sha256']=hashlib.sha256(raw).hexdigest()
        print(json.dumps(result,indent=2,sort_keys=True))
    except (ValueError,KeyError,TypeError,OSError) as e:ap.exit(2,f'INVALID_INPUT: {e}\n')

if __name__=='__main__':main()
