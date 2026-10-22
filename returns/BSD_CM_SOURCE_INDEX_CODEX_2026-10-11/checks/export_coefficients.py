from sage.all import EllipticCurve,QQ
from pathlib import Path
import hashlib,json,gzip
r=Path(__file__).resolve().parents[1]; out=r/'cm'
C=EllipticCurve(QQ,[1,1,1,1878418,-485198548]); cert=json.loads((out/'CERTIFIED_GZ_INGREDIENTS.json').read_text()); rows=[]
for name,E,M,key in [('C',C,12000,'Lprime_coeff_sha256'),('C_twist_minus19',C.quadratic_twist(-19),120000,'Ltwist_coeff_sha256')]:
 a=E.anlist(M,python_ints=True); digest=hashlib.sha256(','.join(map(str,a)).encode()).hexdigest();assert digest==cert[key]
 data=json.dumps({'model':list(map(str,E.a_invariants())),'cutoff':M,'coefficients':a},separators=(',',':')).encode()
 p=out/(name+'_coefficients.json.gz');p.write_bytes(gzip.compress(data,mtime=0))
 rows.append({'file':p.name,'vector_sha256':digest,'file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'cutoff':M})
(out/'COEFFICIENT_BINDINGS.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
