#!/usr/bin/env python3
"""Portable exact custody and count audit of every completed work unit."""
import argparse
import hashlib
import json
from pathlib import Path
import re

def audit(units, custody):
    rows = json.loads(custody.read_text())['rows']
    ap = {r['segment']:r['sha256'] for r in rows}
    assert set(ap) == set(range(3420))
    want = {f'lseg_{i:06d}.txt' for i in range(3420)} | {f'blk_{i:06d}.txt' for i in range(13680)}
    found = {p.name for p in units.glob('*.txt')}
    assert found == want, ('unit coverage mismatch',len(found),len(want),sorted(want-found)[:8])
    total_smooth = total_pairs = total_bytes = 0
    inventory = []
    for name in sorted(want):
        data = (units/name).read_bytes()
        body, end = data.rsplit(b'END ',1)
        assert end.endswith(b'\n') and len(end)==65, name
        assert hashlib.sha256(body).hexdigest() == end[:-1].decode(), name
        lines = body.decode().splitlines()
        assert len(lines)==168, (name,len(lines))
        assert [int(s.split(' ',2)[1]) for s in lines[1:]] == list(range(167)), name
        assert all(s.startswith('S ') and len(s.split())==6 for s in lines[1:]), name
        if name.startswith('lseg_'):
            m = re.fullmatch(r'LSEG (\d+) lo (\d+) hi (\d+) apsha ([0-9a-f]{64}) bigprimes (\d+) pairs (\d+) nnz (\d+)',lines[0])
            assert m, name
            i,lo,hi,sha,nq,pairs,nnz = m.groups()
            i,lo,hi,nq,pairs,nnz = map(int,[i,lo,hi,nq,pairs,nnz])
            assert name==f'lseg_{i:06d}.txt' and lo==i*16777216 and hi==(i+1)*16777216, name
            assert sha==ap[i] and 0<=nnz<=pairs and nq>=0, name
            total_pairs += pairs
        else:
            m = re.fullmatch(r'BLK (\d+) lo (\d+) hi (\d+) leaf ([0-9a-f]{64}) nnz (\d+) smooth (\d+)',lines[0])
            assert m, name
            i,lo,hi,leaf,nnz,smooth=m.groups()
            i,lo,hi,nnz,smooth=map(int,[i,lo,hi,nnz,smooth])
            assert name==f'blk_{i:06d}.txt' and lo==i*4194304+1 and hi==min(lo+4194304,57378078720),name
            assert 0<=nnz<=smooth<=hi-lo,name
            total_smooth += smooth
        total_bytes += len(data)
        inventory.append({'file':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    assert total_pairs+total_smooth==57378078719, (total_pairs,total_smooth)
    return {'status':'COMPLETE_UNIT_CUSTODY_AND_COUNT_PASS','units':len(inventory),
            'lseg':3420,'blocks':13680,'pairs':total_pairs,'smooth':total_smooth,
            'sum':total_pairs+total_smooth,'T':57378078719,'bytes':total_bytes,
            'scope':'Self hashes, receipt binding, exact labels/ranges and count identity; no independent Fourier coefficient or Arb-sum regeneration.',
            'files':inventory}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('units',type=Path)
    p.add_argument('custody',type=Path)
    p.add_argument('--out',required=True,type=Path)
    a=p.parse_args()
    result=audit(a.units,a.custody)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))
