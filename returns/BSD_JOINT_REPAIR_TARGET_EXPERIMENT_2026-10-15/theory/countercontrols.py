#!/usr/bin/env python3
"""Small explicit algebra countercontrols and fail-closed input tests.

These are not elliptic-curve realizations. No old exhaustive checker is used.
"""
import copy,json,tempfile
from pathlib import Path
import dual_overlap as d

def case(n,U,H,W,V,G,L,name):
    data=dict(n=n,U=U,H0=H,W=W,V=V,protected=W)
    return d.profile(data,G,L,name)

out=[]
x=case(2,[[1],[0]],d.eye(2),[[],[]],[],[[1,0]],[[1,1]],'separate_repairs_incompatible')
assert (x['separately_repairable_class_dimension'],x['compatibility_defect_rank'],x['full_joint_dimension'])==(1,1,0)
out.append(x)
x=case(2,[[1],[0]],d.eye(2),[[1],[1]],[],[[1,2]],[[1,2]],'repaired_class_is_point')
assert x['joint_admitted_class_dimension']==x['point_class_image_dimension']==1
assert x['point_relative_dimensions']==dict(unit=0,ordinary_class=0,valuation=0)
out.append(x)
x=case(3,d.eye(3),d.eye(3),[[1,0],[0,1],[0,0]],[],[],[],'zero_class_source_leaves_unit_excess')
assert x['point_relative_dimensions']==dict(unit=1,ordinary_class=0,valuation=0)
out.append(x)
x=case(3,[[1],[0],[0]],[[1,0],[0,1],[0,0]],[[1],[0],[0]],[[0,0,1]],[[0,1,0]],[],'valuation_direction_must_be_retained')
assert x['point_relative_dimensions']==dict(unit=0,ordinary_class=0,valuation=1)
out.append(x)

seedpath=Path('/Users/bsm/BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13/data/MATRICES.json')
seed=d.adapt(json.loads(seedpath.read_text()))
bad=next(([int(j==i) for j in range(seed['n'])] for i,row in enumerate(seed['protected']) if any(row)),None)
assert bad is not None
try:d.profile(seed,seed['G0']+[bad],seed['L'],'deliberately_reject_protected_class')
except AssertionError as ex:
    assert 'Protected actual class rejected' in str(ex)
else:raise AssertionError('Protected positive source was not enforced')

with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'wrong.json';p.write_text(json.dumps({'source_sha256':'wrong','blocks':[]}))
    try:d.run(seedpath,p)
    except AssertionError as ex:
        assert 'not bound' in str(ex)
    else:raise AssertionError('Wrong source binding accepted')

result=dict(status='COUNTERCONTROLS_PASS',synthetic_algebra_cases=out,
    protected_positive_seed_rejection_guard=True,wrong_source_binding_guard=True,
    scope='Abstract algebra examples and input guards, not new arithmetic or Selmer computations.')
Path(__file__).with_name('COUNTERCONTROLS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'synthetic_cases':len(out),'input_guards':2}))
