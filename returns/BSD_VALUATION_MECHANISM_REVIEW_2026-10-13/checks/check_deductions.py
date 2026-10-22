#!/usr/bin/env python3
"""Exact operations on retained digits; not a theorem or producer verifier."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def valuation(x, p):
    assert x != 0, 'zero residue gives no exact valuation'
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v

def digit_value(digit, p):
    x, n = digit
    x %= p ** n
    assert x != 0, 'insufficient precision'
    v = valuation(x, p)
    assert v < n
    return v

def quotient_first_digit(num, den, euler, tamagawa, p):
    vn, vd, ve = [digit_value(x,p) for x in (num,den,euler)]
    vc = valuation(tamagawa,p)
    qv = vn-vd-ve-vc
    unit = (num[0]//p**vn) * pow((den[0]//p**vd)*(euler[0]//p**ve)*(tamagawa//p**vc),-1,p)%p
    return {'valuation':qv,'leading_unit':unit}

def main():
    data=json.loads((ROOT/'evidence/DIGIT_COMPARISON.json').read_text())
    rows=[]
    for d, F in [(43737,data['d43737']['F']), (329233,data['d329233_n8'])]:
        assert pow(d%5,2,5)==4
        vf=digit_value(F['direct_L2'],5)
        vr=digit_value(F['digits']['HU'],5)
        fq=quotient_first_digit(F['direct_L2'],F['digits']['HU'],F['digits']['Euler'],4,5)
        assert fq=={'valuation':2,'leading_unit':1}
        # Division is the exact source-matched isogeny identity between curves,
        # not an allowed rescaling of an arbitrary Kato class.
        af=[F['direct_L2'][0]//5,F['direct_L2'][1]-1]
        assert F['direct_L2'][0]%5==0
        aq=quotient_first_digit(af,F['digits']['HU'],F['digits']['Euler'],20,5)
        assert aq=={'valuation':0,'leading_unit':1}
        if d==43737:
            aa=data['d43737']['A']['direct_L2']
            assert (aa[0]-af[0])%5**min(aa[1],af[1])==0
        rows.append({'d':d,'F_L2_valuation':vf,'regulator_valuation':vr,
                     'F_corrected':fq,'A_L2_valuation':digit_value(af,5),
                     'A_numerator_independently_computed':d==43737,
                     'A_corrected':aq,
                     'conditional_primary_groups':{'A':'0','F':'(Z/5)^2'}})
    # Groups of order 25: nontrivial invariant-factor partitions of length two.
    types=[(2,),(1,1)]
    surviving=[a for a in types if len(a)>=2]
    assert surviving==[(1,1)]
    p=17
    a,b,c=13*p+16*p*p,5*p+7*p*p,15*p+12*p*p
    det=(a*c-b*b)%p**4
    assert valuation(det,p)==3 and det//p**3%p==13
    assert 46298%17==7
    rejects=[]
    for pair in ([0,4],[5**4,4]):
        try: digit_value(pair,5)
        except AssertionError: rejects.append(pair)
        else: raise AssertionError('zero at stated precision accepted')
    return {'grade':'exact arithmetic on retained data, theorem application conditional on written audits',
            'controls':rows,'length2_with_residual_dimension_at_least2':surviving,
            'seed17':{'native_regulator_valuation':3,'U_regulator_valuation':1,
                      'regulator_leading_unit':13,'Ota_residue':7,
                      'L2_valuation_derived_from_old_Sha_certificate':1,
                      'L2_computed':False},
            'precision_negative_controls_rejected':rejects,
            'new_seed_primes':0,'FIN':'UNCHANGED','ORDER9':'UNCHANGED','Q36':'UNCHANGED'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
