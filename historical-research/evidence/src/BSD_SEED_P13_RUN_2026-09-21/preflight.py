"""P13: bind and reuse the 2333 sealed C11 coefficient segments, then symlink them into this run."""
import json, hashlib, os, shutil, sys, time
from pathlib import Path
root=Path(__file__).resolve().parent; run=root/'run'
P11=Path.home()/'BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p11'
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda: f.read(1<<20), b''): h.update(b)
    return h.hexdigest()
b=json.load(open(P11/'CERTIFICATE_BINDINGS.json')); segs=b['segments']
print(f"binding file segments: {len(segs)}")
t0=time.time(); bad=[]; recs=[]; nbytes=0
for i,item in enumerate(segs):
    ap=Path(item['coefficients']['path']); lg=Path(item['verifier_record']['path'])
    for p,meta in ((ap,item['coefficients']),(lg,item['verifier_record'])):
        if not p.exists(): bad.append((i,'missing',str(p))); continue
        if p.stat().st_size!=meta['bytes']: bad.append((i,'size',str(p))); continue
        if sha(p)!=meta['sha256']: bad.append((i,'sha256',str(p))); continue
    nbytes+=item['coefficients']['bytes']
    for dest,src in ((run/f'ap/ap_{i:06d}.bin',ap.resolve()),(run/f'logs/ver_{i}.log',lg.resolve())):
        if dest.is_symlink():
            if dest.resolve()!=src: bad.append((i,'symlink-mismatch',str(dest)))
        elif dest.exists(): bad.append((i,'exists-not-symlink',str(dest)))
        else: dest.symlink_to(src)
    recs.append({'segment':i,'ap_sha256':item['coefficients']['sha256'],'custody':'REUSED_SEALED_C11_CERTIFICATE'})
    if (i+1)%500==0: print(f"  rehashed {i+1}/{len(segs)}  ({time.time()-t0:.1f}s)",flush=True)
dt=time.time()-t0
print(f"rehashed {len(segs)} segments, {nbytes/2**30:.2f} GiB of coefficients, in {dt:.1f}s")
print("FAILURES:",len(bad))
for x in bad[:10]: print("  ",x)
free=shutil.disk_usage(root).free
json.dump({'time_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
 'reused_segments':len(segs),'failures':bad,'coefficient_bytes':nbytes,
 'rehash_seconds':round(dt,2),'free_disk_gib':round(free/2**30,2),
 'source_bindings_sha256':sha(P11/'CERTIFICATE_BINDINGS.json'),'records':recs},
 open(root/'PREFLIGHT.json','w'),indent=1)
print(f"free disk: {free/2**30:.1f} GiB")
sys.exit(1 if bad else 0)
