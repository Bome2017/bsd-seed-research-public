#!/usr/bin/env python3
"""Parser/adversarial controls, plus historical output calibration. No producer run."""
import argparse,json,re
from pathlib import Path
from independent_verifier import verify,Invalid,ball

parser=argparse.ArgumentParser()
parser.add_argument('--calibration',type=Path,default=Path('/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/seed_runs/p43_l173/msl.txt'))
parser.add_argument('--out',type=Path)
a=parser.parse_args()
s=a.calibration.read_text()
results=[]

def rejected(name,text,**kw):
    try:
        verify(text,43,173,**kw)
    except Invalid as e:
        results.append({'name':name,'outcome':'REJECTED','reason':str(e)})
        return
    raise AssertionError(name+' was accepted')

def replace_ball(text,label,new):
    pat=rf'(^XB {label} plus )\[[^\]]+\]'
    out,n=re.subn(pat,lambda m:m.group(1)+'['+new+']',text,flags=re.M)
    assert n==1
    return out

base=verify(s,43,173)
assert base['coefficients_exact']==['0','-13072','-227412']
assert base['coefficients_mod_p']==[0,0,15]
assert base['alternate_coefficients_mod_p']==[0,0,16]
results.append({'name':'historical43_calibration','outcome':'PASS','c2':15,'alternate_c2':16})
# Candidate text is deliberately false and even nonnumeric. It is not consumed.
flags=re.sub(r'cand [-\d]+/1024 contains 1 unique 1','cand FABRICATED contains 0 unique 0',s)
assert verify(flags,43,173)['coefficients_exact']==base['coefficients_exact']
results.append({'name':'printed_candidates_and_flags_ignored','outcome':'PASS'})
line=next(x for x in s.splitlines() if x.startswith('XB 1 plus '))
rejected('duplicate_label',s+'\n'+line+'\n')
rejected('missing_label',s.replace(line+'\n',''))
rejected('out_of_range_label',s.replace('XB 1 plus ','XB 173 plus ',1))
rejected('malformed_symbol_line',s.replace('XB 1 plus ','XB -1 plus ',1))
rejected('multiple_lattice_candidates',replace_ball(s,1,'-14 +/- 0.001'))
rejected('no_lattice_candidate',replace_ball(s,1,'-14.0002 +/- 0.00000001'))
rejected('negative_radius',replace_ball(s,1,'-14 +/- -0.001'))
rejected('nonfinite_number',replace_ball(s,1,'nan +/- 0.001'))
rejected('symmetry_broken',replace_ball(s,1,'-13 +/- 0.000001'))
changed=replace_ball(replace_ball(s,1,'-13 +/- 0.000001'),172,'-13 +/- 0.000001')
rejected('nonzero_c0',changed)
changed=replace_ball(replace_ball(changed,2,'-103 +/- 0.000001'),171,'-103 +/- 0.000001')
rejected('nonzero_c1_after_exact_c0',changed)
rejected('nonprimitive_generator',s,g=1)
rejected('nonintegral_lattice',s,den=43)
rejected('nonprimitive_generator_power',s,gpower=2)
zero='\n'.join(f'XB {k} plus [+/- 1e-6]' for k in range(1,167))+'\n'
x=verify(zero,83,167,g=5)
assert x['mathematical_witness']=='INCONCLUSIVE_ZERO' and x['labels']==166
results.append({'name':'synthetic83_zero_is_inconclusive','outcome':'PASS'})
assert ball('1.25e-2 +/- 0.0005')==ball('0.0125 +/- 5e-4')
assert ball('0')==ball('+/- 0')
results.append({'name':'exact_decimal_syntax','outcome':'PASS'})
out={'status':'PASS','scope':'output arithmetic/parser controls; synthetic cases are not seed values',
     'count':len(results),'checks':results}
t=json.dumps(out,sort_keys=True,indent=2)+'\n'
if a.out:a.out.write_text(t)
print(t,end='')
