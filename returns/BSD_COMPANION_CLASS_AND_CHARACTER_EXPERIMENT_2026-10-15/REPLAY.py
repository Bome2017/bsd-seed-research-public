"""Bounded, read-only verification. Does not rerun BNF or certification timeouts."""
from pathlib import Path
import subprocess, tempfile, shutil, hashlib, json, sys
R=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def run(cmd,cwd,timeout=60):
    q=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=timeout)
    if q.returncode:raise RuntimeError(q.stdout+'\n'+q.stderr)
    return q
with tempfile.TemporaryDirectory(prefix='.verify-',dir=R) as tmp:
    T=Path(tmp)
    shutil.copy2(R/'p5_norm_upper/export.gp',T/'export.gp')
    with (T/'export.gp').open() as f:
        p=subprocess.run([GP,'-q','-f','-s','160000000'],stdin=f,cwd=T,capture_output=True,text=True,timeout=60)
    assert p.returncode==0 and 'COMPACT_UNIT_EXPORT_PASS' in p.stdout and '***' not in p.stderr
    assert sha(T/'eval_data.json')==sha(R/'p5_norm_upper/eval_data.json')
    checks.append('exact_export_binds_authenticated_compact_units_to_residue_input')
    shutil.copy2(R/'p5_norm_upper/evaluate.py',T/'evaluate.py')
    shutil.copy2(R/'p5_norm_upper/split_primes.json',T/'split_primes.json')
    run([sys.executable,'-B','evaluate.py'],T)
    assert (T/'NORM_UPPER.json').read_bytes()==(R/'p5_norm_upper/NORM_UPPER.json').read_bytes()
    checks.append('complete_unit_projection_and_norm_residue_matrices_byte_identical')
    for name,out in [('check_characters.py','CHARACTER_CHECKS.json'),('check_local_divisors.py','LOCAL_DIVISOR_CHECK.json')]:
        shutil.copy2(R/'general_character'/name,T/name)
        run([sys.executable,'-B',name],T)
        assert (T/out).read_bytes()==(R/'general_character'/out).read_bytes()
        checks.append(name+'_byte_identical')
# Independent minimal witness checker writes its deterministic output; comparison
# is saved before/after so no changed evidence can silently pass.
f=R/'character_review/MINIMAL_NORM_WITNESS.json'; before=f.read_bytes()
run([sys.executable,'-B','check_minimal_norm_witness.py'],f.parent)
assert f.read_bytes()==before
checks.append('independent_minimal_direct_product_witness_byte_identical')
manifest_count=0
for mf in sorted(R.rglob('MANIFEST.sha256')):
    for line in mf.read_text().splitlines():
        h,rel=line.split('  ',1);p=mf.parent/rel
        assert p.is_file() and sha(p)==h,(str(mf),rel)
        manifest_count+=1
checks.append('all_root_and_nested_manifest_entries_match')
print(json.dumps({'status':'PASS','checks':checks,'manifest_entries':manifest_count,
                  'no_BNF_or_class_certification_rerun':True},indent=2))
