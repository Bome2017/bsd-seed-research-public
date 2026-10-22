#!/usr/bin/env python3
"""Refresh STATE.json artifacts (path->sha256), CPU total and last_checkpoint; regenerate the sha256 block in RESUME.md."""
import json, hashlib, os, subprocess, re, datetime
D='/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants'
os.chdir(D)
arts={}
for root,_,files in os.walk('.'):
    for f in sorted(files):
        p=os.path.join(root,f)[2:]
        if p in ('STATE.json','RESUME.md') or p.endswith('.sobj.tmp'): continue
        arts[p]=hashlib.sha256(open(p,'rb').read()).hexdigest()
arts=dict(sorted(arts.items()))
cpu=0.0
for l in open('cpu_log.tsv'):
    for k in ('user=','sys='):
        m=re.search(k+r'([0-9.]+)',l)
        if m: cpu+=float(m.group(1))
st=json.load(open('STATE.json'))
st['artifacts']=arts
st['cpu_seconds_used']=round(cpu,1)
st['last_checkpoint']=datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump(st,open('STATE.json','w'),indent=1,ensure_ascii=False)
r=open('RESUME.md').read()
block='\n'.join(f'- `{p}` {h}' for p,h in arts.items())
r=re.sub(r'<!-- SHA-BEGIN -->.*<!-- SHA-END -->', '<!-- SHA-BEGIN -->\n'+block+'\n<!-- SHA-END -->', r, flags=re.S)
r=re.sub(r'Last checkpoint: .*', 'Last checkpoint: '+st['last_checkpoint']+f' ; CPU used so far: {cpu:.1f} s (cap 1800 s)', r)
open('RESUME.md','w').write(r)
print('checkpoint', st['last_checkpoint'], 'cpu', round(cpu,1), 'artifacts', len(arts))
