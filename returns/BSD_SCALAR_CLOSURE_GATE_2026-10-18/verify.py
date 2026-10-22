#!/usr/bin/env python3
"""Read-only packet validation plus independent saved-matrix replay."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(p):
    n=0
    for line in p.read_text().splitlines():
        if not line.strip():continue
        h,f=line.split('  ',1);q=(p.parent/f).resolve()
        assert q.is_relative_to(R) and q.is_file() and sha(q)==h, str(q)
        n+=1
    return n

arg=argparse.ArgumentParser(description=__doc__)
arg.add_argument('--skip-root-manifest',action='store_true')
a=arg.parse_args()
b=json.loads((R/'INPUT_BINDINGS.json').read_text())
for f in b['files']:
    p=R/f['new_relative'];assert p.stat().st_size==f['bytes'] and sha(p)==f['sha256']
nested={d:manifest(R/d/'MANIFEST.sha256') for d in ['arithmetic','review']}
rb=json.loads((R/'review/REVIEW_BINDINGS.json').read_text())
for key,name in [('root_proof_sha256','PROOF.md'),('root_report_sha256','REPORT.md'),('gate_core_sha256','arithmetic/GATE_CORE.json'),('input_binding_sha256','INPUT_BINDINGS.json')]:
    assert sha(R/name)==rb[key],('review binding',name)
z=json.loads((R/'arithmetic/RESULT.json').read_text())
assert z['desired_character']==3 and z['desired_rank']==20 and z['desired_nullity']==0
assert z['closed_prime_support']==331 and z['scalar_translates']==120
assert z['integral_translate_rank']==60 and z['mod7_translate_rank']==60
assert [(t['eigenvalue'],t['rank'],t['nullity']) for t in z['characters']]==[(3,20,0),(5,20,0),(6,20,0)]
assert 'SCALAR_CLOSURE_GATE_COMPLETE=' in (R/'arithmetic/gate.gp.out').read_text()
receipt=json.loads((R/'arithmetic/gate.gp.receipt.json').read_text())
assert receipt['exit_code']==0 and receipt['stop'] is None and receipt['elapsed_seconds']<60 and receipt['peak_rss_bytes']<1024**3
# Saved-matrix reconstruction and Gaussian elimination, no source generation or factoring.
p=subprocess.run([sys.executable,str(R/'review/replay_gate.py')],check=True,capture_output=True,text=True)
replay=json.loads(p.stdout);saved=json.loads((R/'review/INDEPENDENT_GATE_REPLAY.json').read_text());assert replay==saved
assert replay['full_rank_mod7']==60 and replay['first_three_per_generator_rank_mod7']==60
out={'status':'INPUT_CUSTODY_AND_INDEPENDENT_SAVED_MATRIX_REPLAY_PASS','portable_inputs':len(b['files']),'nested_manifest_entries':nested,'support_primes':331,'scalar_columns':120,'rank_mod7':60,'projected_rank':20,'projected_nullity':0,'gate_seconds':receipt['elapsed_seconds'],'scope':'Hashes and independent exact saved-matrix replay. No new factorization, source generation, full-source bound or BSD certification.'}
if not a.skip_root_manifest and (R/'MANIFEST.sha256').exists():out['root_manifest_entries']=manifest(R/'MANIFEST.sha256')
print(json.dumps(out,indent=2))
