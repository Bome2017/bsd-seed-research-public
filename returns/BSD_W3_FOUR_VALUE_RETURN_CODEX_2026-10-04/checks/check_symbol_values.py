"""Exact coefficient and precision controls; no seed symbols supplied."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import symbol_values as sv
from fractions import Fraction
from math import comb
import random,json,copy

def run():
    rng=random.Random(40603); cases=0; rejects=0
    for p in [17,23,29,53]:
        m=p**4
        for _ in range(12):
            data={'p':p,'N':sv.N_SEED,'convention':'source_phi_X_minus_zY_path_a_over_p_to_infinity','fibers':{}}
            expected={}
            for w in (3,4):
                alpha=rng.randrange(1,m)
                while alpha%p==0:alpha=rng.randrange(1,m)
                rows=[]; full={}
                for a in range(1,p):
                    c=[rng.randrange(m) for h in range(w+1)];full[a]=c
                    rows.append({'a':a,'coefficients':[c[h]%(p**(4-h)) for h in range(4)]})
                data['fibers'][str(w)]={'alpha_mod_p4':alpha,'modular_weight':w+2,'tame_character_exponent':-w,'symbols':rows}
                for s in ([2,3] if w==3 else [3,4]):
                    total=0
                    for a,c in full.items():
                        # Independent rational expansion of (a-pz)^s against
                        # moments recovered from coefficients of (X-zY)^w.
                        term=sum(Fraction(comb(s,h)*a**(s-h)*(-p)**h*((-1)**h)*c[h],comb(w,h)) for h in range(s+1))
                        term_mod=term.numerator*pow(term.denominator,-1,m)%m
                        total+=pow(pow(a,p**4,m),-s,m)*term_mod
                    expected[w,s]=(-1)**s*total*pow(alpha,-1,m)%m
            out=sv.evaluate(data)
            assert out['values']==[expected[q] for q in sv.NODES]
            assert not out['source_verified'] and not out['seed_primary_certificate']
            unknown_alpha=copy.deepcopy(data)
            for f in unknown_alpha['fibers'].values():f.pop('alpha_mod_p4')
            ua=sv.evaluate(unknown_alpha)
            assert ua['values']==[None]*4
            assert ua['certificate_residues']==out['certificate_residues']
            assert ua['any_nonzero']==out['any_nonzero']
            cases+=4
            for kind in range(4):
                bad=copy.deepcopy(data)
                if kind==0:bad['fibers']['3']['alpha_mod_p4']=p
                elif kind==1:bad['fibers']['4']['symbols'].pop()
                elif kind==2:bad['fibers']['3']['symbols'][0]['coefficients'][3]=p
                else:bad['convention']='unrecorded'
                try:sv.evaluate(bad)
                except ValueError:rejects+=1
                else:raise AssertionError('malformed input accepted')
    return {'status':'PASS','rational_expansion_comparisons':cases,'malformed_inputs_rejected':rejects,
            'scope':'formula/precision/input checks, no seed arithmetic provenance', 'seed_values_computed':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
