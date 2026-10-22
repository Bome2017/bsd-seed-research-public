#!/usr/bin/env python3
"""Read-only verification and isolated replay of this bounded research packet."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tempfile

ROOT=Path(__file__).resolve().parent

def check_manifest(path):
    count=0
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        h, rel=line.split('  ', 1)
        f=(path.parent/rel).resolve()
        if not f.is_relative_to(path.parent.resolve()):
            raise ValueError('manifest path escapes packet')
        if hashlib.sha256(f.read_bytes()).hexdigest()!=h:
            raise ValueError('hash mismatch: '+str(f))
        count+=1
    return count

counts={str(p.relative_to(ROOT)):check_manifest(p)
        for p in [ROOT/'MANIFEST.sha256',ROOT/'arithmetic/MANIFEST.sha256']}
with tempfile.TemporaryDirectory(prefix='bsd-joint-class-replay-') as td:
    temp=Path(td)/ROOT.name
    shutil.copytree(ROOT,temp)
    steps=[]
    for script in ['arithmetic/replay.py','theory/check_incidence_gate.py',
                   'sources/check_reconstruction_gate.py']:
        r=subprocess.run([sys.executable,str(temp/script)],cwd=temp,
                         capture_output=True,text=True,timeout=150)
        if r.returncode or r.stderr.strip():
            raise RuntimeError(script+'\n'+r.stdout+'\n'+r.stderr)
        steps.append({'script':script,'status':'PASS'})
    for rel in ['theory/INCIDENCE_GATE_RESULT.json',
                'sources/RECONSTRUCTION_GATE_CHECK.json']:
        if json.loads((temp/rel).read_text())!=json.loads((ROOT/rel).read_text()):
            raise ValueError('saved checker result differs: '+rel)
print(json.dumps({'status':'PASS','manifest_entries':counts,'replays':steps,
                  'new_seed_class_bound':False,'endpoints_changed':False},indent=2))
