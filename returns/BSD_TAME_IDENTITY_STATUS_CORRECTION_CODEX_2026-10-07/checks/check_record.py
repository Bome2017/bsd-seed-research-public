#!/usr/bin/env python3
"""Check stored residues and endpoint arithmetic; not an independent producer replay."""
from pathlib import Path
from fractions import Fraction
import json
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'context/EXACTNESS_EVALUATION.json').read_text())['rows']
defined=[r for r in rows if r['defined']]
clean=[r for r in rows if r.get('clean_depth')]
constants={}
fail=[]
for r in rows:
    constants.setdefault(r['curve'],set()).add(r['K_E'])
for r in defined:
    modulus=r['q']**r['e']
    if (r['C2']-r['K_E']*(r['a_l']-2)*r['R'])%modulus:
        fail.append([r['curve'],r['l'],r['q'],r['e']])
expected={'389a1':[8],'433a1':[4],'664a1':[16],'655a1':[8],'1615a1':[16],'194040co6':[32]}
constants={c:sorted(v) for c,v in sorted(constants.items())}
assert constants==expected
assert len(rows)==338 and len(defined)==275 and len(clean)==104 and not fail
radius=Fraction(573,100000)
assert Fraction(1,174)>radius and Fraction(1,175)<radius
assert 9*53**2==25281
result={
    'scope':'stored-data arithmetic only; no independent modular-symbol, regulator, source-theorem, or seed replay',
    'rows':len(rows),'defined_odd_rows':len(defined),'clean_depth_rows':len(clean),
    'stored_equation_mismatches':fail,'curve_constants':constants,
    'seed_in_panel':False,'288_factorization':'2^5 * 3^2',
    'conditional_order_lower_alternative':9*53**2,
    'Q36_denominator_check':{'retained_interval_radius':str(radius),'one_over_174':str(Fraction(1,174)),
                             'one_over_175':str(Fraction(1,175)),'174_sufficient':True,'175_not_sufficient':True},
}
print(json.dumps(result,indent=2,sort_keys=True))
