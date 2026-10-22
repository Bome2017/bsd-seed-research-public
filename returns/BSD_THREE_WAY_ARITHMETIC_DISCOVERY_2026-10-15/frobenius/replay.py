#!/usr/bin/env python3
"""Portable replay. Override BSD_GP if gp is not on PATH; no BNF/source jobs."""
import os,sys,json,shutil,hashlib,tempfile,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
GP=os.environ.get('BSD_GP') or shutil.which('gp') or '/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=json.loads((R/'SOURCE_BINDINGS.json').read_text())
for x in bind:assert sha(R/x['local'])==x['sha256']
work=Path(tempfile.mkdtemp(prefix='clean_',dir=R));logs=[]
def gp(script,outname=None):
 s=(R/script).read_text()
 for b in bind:s=s.replace(b['original'],str(R/b['local']))
 (work/script).write_text(s)
 x=subprocess.run([GP,'-D','parisizemax=1000000000','-q','-f'],input=s,text=True,cwd=work,capture_output=True,timeout=120)
 (work/(script+'.out')).write_text(x.stdout);(work/(script+'.err')).write_text(x.stderr)
 assert x.returncode==0 and 'at top-level'not in x.stderr and 'user error'not in x.stderr and 'syntax error'not in x.stderr,(script,x.stderr)
 if outname:(work/outname).write_text(x.stdout)
 logs.append(dict(script=script,exit=x.returncode,stdout_sha256=sha(work/(script+'.out'))))
gp('construct_norm.gp')
for f in ['norm.json','affine_norm_certificate.gp','odd_cube_certificate.gp']:assert (work/f).read_bytes()==(R/f).read_bytes(),f
gp('bind_source.gp','source_exact.json');assert (work/'source_exact.json').read_bytes()==(R/'source_exact.json').read_bytes()
gp('check_genuine_controls.gp')
assert 'ALL_GENUINE_CONTROL_AND_NORM_CHECKS_PASS' in (work/'check_genuine_controls.gp.out').read_text()
gp('select_fresh.gp');assert (work/'fresh_roots.jsonl').read_bytes()==(R/'fresh_roots.jsonl').read_bytes()
gp('splitting_polynomial.gp')
for f in ['splitting_polynomial.json','splitting_polynomial.gp.data']:assert (work/f).read_bytes()==(R/f).read_bytes()
gp('check_polynomial.gp');assert (work/'POLYNOMIAL_ROOT_COUNTS.json').read_bytes()==(R/'POLYNOMIAL_ROOT_COUNTS.json').read_bytes()
for f in ['NORM_PREDICTIONS.json','PREDICTION_OUTPUT_SEAL.json','norm_predict.py']:shutil.copyfile(R/f,work/f)
s=(R/'validate_predictions.py').read_text().replace("Path('/Users/bsm/BSD_JOINT_REPAIR_TARGET_EXPERIMENT_2026-10-15/heldout')",repr(str(R/'inputs/heldout')))
s=s.replace("OLD='/", "OLD=Path('/") if False else s
# Preserve the Path type after replacing the fixed historical path.
s=s.replace("OLD="+repr(str(R/'inputs/heldout')), "OLD=Path("+repr(str(R/'inputs/heldout'))+")")
(work/'validate_predictions.py').write_text(s)
x=subprocess.run([sys.executable,str(work/'validate_predictions.py')],cwd=work,capture_output=True,text=True,timeout=60)
(work/'validation.out').write_text(x.stdout);(work/'validation.err').write_text(x.stderr);assert x.returncode==0,x.stderr
for f in ['FRESH_RESULTS.json','CALIBRATION_RESULTS.json']:
 a=json.loads((work/f).read_text());b=json.loads((R/f).read_text());assert a['records']==b['records']
assert (work/'NONCUBE_WITNESS.json').read_bytes()==(R/'NONCUBE_WITNESS.json').read_bytes()
out=dict(status='PORTABLE_EXACT_REPLAY_PASS',workdir=work.name,input_files=len(bind),gp_jobs=logs,fresh_predictions=40,old_calibration_cases=72,local_source_coverage='All computation inputs copied into inputs; historical source grades remain retained.')
(R/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
