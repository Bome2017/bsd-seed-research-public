#!/usr/bin/env python3
"""Independent exhaustive check: no imports of producer elimination code."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib,json

ROOT=Path('/Users/bsm/BSD_CLAUDE_RECONCILIATION_AND_CONTINUATION_CODEX_2026-10-15')
OLD=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14')
HERE=Path(__file__).resolve().parent

def mv(A,v):
    return tuple(sum(a*b for a,b in zip(row,v))%3 for row in A)
def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def sub(a,b):return tuple((x-y)%3 for x,y in zip(a,b))
def null(A,v):return not any(mv(A,v))
def dimension(s):
    n=len(s);d=0
    while n>1 and n%3==0:n//=3;d+=1
    assert n==1
    return d
def valuation(x,p):
    if not x:return None
    a,b=x.numerator,x.denominator;v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v

def inspect(path):
    d=json.loads(path.read_text());U=d['units'];nu=len(U[0]);n=d['source_dimension']
    allu=list(product(range(3),repeat=nu));S=d['scalar'];A=d['additivity'];G=S+A;L=d['local'];H=d['valuation_zero_basis'];C=d['class_lifts']
    beta=tuple(row[0] for row in C)
    units={u:mv(U,u) for u in allu}
    assert len(set(units.values()))==3**nu
    assert all(null(d['valuation'],v) for v in units.values())
    assert null(d['valuation'],beta)
    hg={mv(H,v) for v in product(range(3),repeat=len(H[0]))}
    uc={add(v,tuple(c*x%3 for x in beta)) for v in units.values() for c in range(3)}
    assert hg==uc and len(hg)==3**(nu+1)
    KG={u for u,v in units.items() if null(G,v)}
    KL={u for u,v in units.items() if null(L,v)}
    summed={add(u,v) for u in KG for v in KL}
    rows=[]
    for c in range(3):
        base=tuple(c*x%3 for x in beta)
        g={u for u,v in units.items() if null(G,add(base,v))}
        l={u for u,v in units.items() if null(L,add(base,v))}
        common=g&l
        assert g and l, 'separate admissibility required for compatibility map'
        ug=min(g);ul=min(l);delta=sub(ug,ul)
        assert (delta in summed)==bool(common)
        # All pairs of choices define exactly the same quotient coset.
        assert {sub(u,v) for u in g for v in l}=={add(delta,k) for k in summed}
        detector=None
        if not common:
            detector=next(z for z in allu if all(sum(a*b for a,b in zip(z,k))%3==0 for k in summed)
                          and sum(a*b for a,b in zip(z,delta))%3==1)
        gv=add(base,units[ug]);lv=add(base,units[ul])
        defects=[]
        for b in d['local_blocks']:
            defect=mv(b['rows'],gv)
            assert null(b['rows'],lv)
            defects.append({'prime':b['prime'],'global_repair_nonzero_local_rows_0based':
                            [[i,a] for i,a in enumerate(defect) if a]})
        rows.append({'class_coordinate':c,'global_repair_count':len(g),'local_repair_count':len(l),
                     'common_repair_count':len(common),'selected_global_repair':ug,
                     'selected_local_repair':ul,'difference_global_minus_local':delta,
                     'separating_functional':detector,'local_defects':defects})
    reported=next(x for x in json.loads((ROOT/'class_lift/repair_compatibility.json').read_text()) if x['curve']==path.parent.name)
    assert reported['units_dimension']==nu
    assert reported['compatibility_quotient_dimension']==nu-dimension(summed)
    for r in reported['class_lifts']:
        ug=tuple(r['global_repair']);ul=tuple(r['local_repair'])
        assert null(G,add(beta,units[ug])) and null(L,add(beta,units[ul]))
        assert sub(ug,ul)==tuple(r['difference_global_minus_local'])
        assert r['compatible']==(sub(ug,ul) in summed)
    short=None
    if path.parent.name=='mirror389':
        chosen=[G[7],G[12],G[44],d['local_blocks'][0]['rows'][1]]
        weights=[1,1,1,2]
        row=tuple(sum(w*r[j] for w,r in zip(weights,chosen))%3 for j in range(n))
        assert null([row],units[allu[-1]])
        assert all(null([row],v) for v in units.values())
        assert mv([row],beta)==(1,)
        short={'rows':['G[7]','G[12]','G[44]','local_at_3[1]'],'zero_based':True,
               'weights':weights,'restricted_row_on_units_then_class':[0,0,0,0,1],
               'full_source_row':row}
    return {'curve':path.parent.name,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'unit_corrections_enumerated':len(allu),'valuation_zero_classes_enumerated':len(hg),
            'dim_kernel_global_on_units':dimension(KG),'dim_kernel_local_on_units':dimension(KL),
            'dim_sum_of_repair_kernels':dimension(summed),'compatibility_quotient_dimension':nu-dimension(summed),
            'class_fibers':rows,'short_joint_certificate':short}

def hensel():
    pth=ROOT/'class_lift/mirror389/local_precision.json'
    out=[]
    for r in json.loads(pth.read_text()):
        p=r['prime'];x=Fraction(r['x']);y=Fraction(r['y'])
        F=y*y+y-x**3+21*x+27;Fp=2*y+1
        assert F==Fraction(r['F']) and Fp==Fraction(r['Fp'])
        assert F and valuation(F,p)>2*valuation(Fp,p)
        precision=valuation(F,p)-valuation(Fp,p)
        assert precision==r['certified_precision']
        margins=[]
        for e,v,depth,oldmargin in r['prime_ideal_data']:
            margin=e*precision-v-depth
            # Exact Hensel evaluation can certify one more digit than the
            # conservative working-precision margin logged by the producer.
            assert margin>=oldmargin>=0
            assert depth==(3*e//2+1 if p==3 else 1)
            margins.append(margin)
        out.append({'prime':p,'hensel_precision':precision,'cube_margins':margins})
    return {'samples':len(out),'minimum_margin':min(m for r in out for m in r['cube_margins']),
            'input_sha256':hashlib.sha256(pth.read_bytes()).hexdigest(),'rows':out,
            'retained_input':'Prime-ideal valuations of tangent values; not recomputed by this rational checker.'}

def main():
    labels=['718b1','997c1','1070a1','1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh']
    paths=[OLD/f'arithmetic/{label}/matrices.json' for label in labels]
    paths.append(ROOT/'class_lift/mirror389/matrices.json')
    out={'status':'EXHAUSTIVE_COMPATIBILITY_CHECK_PASS',
         'scope':'Exact exported-matrix algebra and rational Hensel checks; source descent theorem and number-field certifications retained.',
         'cases':[inspect(p) for p in paths],'mirror389_hensel':hensel()}
    (HERE/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'cases':[{k:c[k] for k in ['curve','unit_corrections_enumerated','compatibility_quotient_dimension']}|{'nonzero_class_common_repairs':c['class_fibers'][1]['common_repair_count']} for c in out['cases']],
                      'mirror389_hensel_samples':out['mirror389_hensel']['samples'],'minimum_hensel_cube_margin':out['mirror389_hensel']['minimum_margin']},indent=2))

if __name__=='__main__':main()
