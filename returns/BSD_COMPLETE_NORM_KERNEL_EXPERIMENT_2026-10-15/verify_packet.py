#!/usr/bin/env python3
"""Verify hashes, cross-packet dimensions, and reviewed-proof identity.

For mathematical replay use the separately documented subpacket commands.
This verifier does not substitute for those arithmetic replays.
"""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parent

def rank(a,p=3):
    if not a:return 0
    a=[[x%p for x in row] for row in a];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];v=pow(a[r][j],-1,p)
        a[r]=[v*x%p for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][j];a[k]=[(x-v*y)%p for x,y in zip(a[k],a[r])]
        r+=1
    return r

def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*b)] for row in a]

def load(name):return json.loads((R/name).read_text())

manifests=[]
for m in sorted(R.rglob('MANIFEST.sha256')):
    n=0
    for line in m.read_text().splitlines():
        h,name=line.split(maxsplit=1);path=m.parent/name.lstrip('*')
        assert path.is_file(),str(path)
        assert hashlib.sha256(path.read_bytes()).hexdigest()==h,str(path)
        n+=1
    manifests.append({'path':str(m.relative_to(R)),'entries_verified':n})

cases=[]
for name in ['1913b1','389a1']:
    d=load(f'norm_controls/{name}/norm_kernel.json')
    k=d['norm_kernel_in_scalar_basis']
    assert rank(k)==d['kernel_dimension']
    assert rank(d['norm_rows'])+rank(k)==d['scalar_dimension']
    assert not any(any(row) for row in matmul(d['norm_rows'],k))
    cases.append({'case':name,'scalar_dimension':d['scalar_dimension'],
                  'norm_image_rank':rank(d['norm_rows']),'norm_kernel_dimension':rank(k)})

for folder,name in [('norm433','433a1'),('norm_mirror','mirror389')]:
    d=load(folder+'/norm_map.json');c=load(folder+'/complete_certificate.json')
    k=c['exact_global_kernel'];loc=c['local_authenticated_rows']
    assert rank(k)==3
    assert matmul(loc,k)==c['local_restricted_to_global_kernel']
    assert rank(d['residue_map'])==d['norm_image_rank']
    assert rank(k)+d['norm_image_rank']==d['scalar_dimension']
    cases.append({'case':name,'scalar_dimension':d['scalar_dimension'],
                  'norm_image_rank':d['norm_image_rank'],'norm_kernel_dimension':rank(k),
                  'local_kernel_dimension':rank(k)-rank(matmul(loc,k))})

proof=R/'review/SPLIT_PRIME_COMPLETENESS.md'
review=(R/'review/INDEPENDENT_COMPLETENESS_REVIEW.md').read_text()
assert hashlib.sha256(proof.read_bytes()).hexdigest() in review
assert load('review/HOMOGENEOUS_MODULE_CHECKS.json')['status']=='PASS'
print(json.dumps({'status':'PACKET_HASH_AND_CROSS_CERTIFICATE_PASS','manifests':manifests,
 'cases':cases,'review_binds_current_proof':True,
 'scope':'Identity and cross-certificate finite algebra. Does not replay number fields or certify retained arithmetic inputs.'},indent=2,sort_keys=True))
