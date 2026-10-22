#!/usr/bin/env python3
"""Replay packet coefficient identities and sealed predictions, using stdlib."""
import gzip,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ad=json.loads((ROOT/'admission/RESULT.json').read_text())
coeff=[]
for i,receipt in enumerate(ad['coefficients']):
    raw=(ROOT/f'admission/coeff_{i}.json.gz').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==receipt['gzip_sha256']
    text=gzip.decompress(raw)
    assert hashlib.sha256(text).hexdigest()==receipt['uncompressed_sha256']
    a=json.loads(text); assert len(a)==receipt['count']; coeff.append(a)
sturm=[]
for i,ell in enumerate((113,167),1):
    bound=ad['sturm_comparisons'][i-1]['Sturm_bound']
    assert math.prod((q+1)*q**(e-1) for q,e in [(3,1),(7,1),(11,2),(ell,1)])//6==bound
    assert all((coeff[0][n-1]-(ell*coeff[0][n//ell-1] if n%ell==0 else 0)-coeff[i][n-1])%5==0 for n in range(1,bound+1))
    assert coeff[0][12]-coeff[i][12]==-5
    sturm.append({'ell':ell,'coefficients_checked':bound,'all_mod5_equal':True,'mod25_trace_obstruction_at13':True})
pred=json.loads((ROOT/'checks/HELD_OUT_PREDICTIONS.json').read_text())
assert hashlib.sha256((ROOT/'checks/MIXED_INSTRUMENT_DISCOVERY.json').read_bytes()).hexdigest()==pred['discovery_data_sha256']
rows=[]
for name in ['MIXED_INSTRUMENT_DISCOVERY.json','MIXED_INSTRUMENT_HELD_OUT.json']:
    for rec in json.loads((ROOT/'checks'/name).read_text())['records']:
        p=pred['predictions'][str(rec['ell1'])]; cs=p['cohomology_coordinates']; a=rec['ell1_pairing_coordinates_frob_q_squared']
        for row in rec['tests']:
            b=row['point_coordinates']; assert row['Y_coordinate']==sum(c*x for c,x in zip(cs,b))%5
            r=(a[0]*b[1]-a[1]*b[0])%5; assert r==row['detector']
            if r: assert row['instrument_scalar']==p['instrument_scalar_mod5']
            else: assert row['Y_coordinate']==0 and row['instrument_scalar'] is None
            rows.append({'dataset':name,'ell1':rec['ell1'],'ell2':row['ell2'],'detector_nonzero':bool(r),'matches':True})
out={'grade':'replay of saved exact evidence; not independent coefficient generation or global proof','sturm':sturm,'sealed_discovery_hash_matches':True,'rows':rows,'total_rows':len(rows),'nonzero_detector_rows':sum(r['detector_nonzero'] for r in rows),'held_out_rows':sum(r['dataset']=='MIXED_INSTRUMENT_HELD_OUT.json' for r in rows)}
(ROOT/'checks/SAVED_EVIDENCE_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
