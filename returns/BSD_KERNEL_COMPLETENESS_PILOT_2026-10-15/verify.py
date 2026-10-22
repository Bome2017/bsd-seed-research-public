#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
r=Path(__file__).resolve().parent
manifest=r/'MANIFEST.sha256'
count=0
for line in manifest.read_text().splitlines():
    h,n=line.split('  ',1)
    assert hashlib.sha256((r/n).read_bytes()).hexdigest()==h,n
    count+=1
for f in ('CONTRACT.md','COMMON_POINT_CONTRACT.md'):
    assert hashlib.sha256((r/f).read_bytes()).hexdigest()==(r/(f.removesuffix('.md')+'.sha256')).read_text().split()[0]
with tempfile.TemporaryDirectory(prefix='bsd-kernel-replay-') as tmp:
    dest=Path(tmp)/'packet'
    shutil.copytree(r,dest,ignore=shutil.ignore_patterns('__pycache__'))
    a=subprocess.run([sys.executable,'pilot.py'],cwd=dest,capture_output=True,timeout=60)
    assert a.returncode==0,a.stderr.decode()
    assert a.stdout==(r/'pilot.out').read_bytes()
    b=subprocess.run([sys.executable,'independent_common_point.py'],cwd=dest,capture_output=True,timeout=60)
    assert b.returncode==0,b.stderr.decode()
    for f in ('RESULTS.json','INDEPENDENT_COMMON_POINT.json'):
        assert (dest/f).read_bytes()==(r/f).read_bytes(),f
print(json.dumps({'status':'MANIFEST_AND_TWO_IMPLEMENTATION_REPLAY_PASS','manifest_entries':count,'scope':'Exact saved-data replay, not recertification of arithmetic inputs or BSD'}))
