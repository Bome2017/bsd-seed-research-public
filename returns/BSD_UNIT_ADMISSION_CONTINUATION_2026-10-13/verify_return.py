#!/usr/bin/env python3
"""Fail-closed custody and optional portable arithmetic replay; no BNF producer."""
import argparse,hashlib,json,pathlib,re,shutil,subprocess,tempfile,time,sys
ap=argparse.ArgumentParser();ap.add_argument('--gp');args=ap.parse_args();root=pathlib.Path(__file__).resolve().parent
manifest=root/'MANIFEST.sha256';count=0
for row in manifest.read_text().splitlines():
 digest,name=row.split('  ',1);f=root/name
 if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:raise SystemExit('MANIFEST_MISMATCH '+name)
 count+=1
out={'manifest_verified':count,'mathematical_status':'written deductions under retained inputs; no BSD endpoint','replays':[]}
if args.gp:
 gp=str(pathlib.Path(args.gp).resolve())
 with tempfile.TemporaryDirectory(prefix='bsd-unit-admission-replay-') as td:
  copy=pathlib.Path(td)/'packet';shutil.copytree(root,copy)
  jobs=[('new_units','checks','verify_new_units.gp','NEW_UNITS_PORTABLE_PASS'),('exact_maps','checks','verify_exact_maps.gp','EXACT_MAP_REPLAY_PASS'),('previous_unit','inputs/previous/checks','verify_unit_portable.gp','PORTABLE_UNIT_CERTIFICATE_PASS')]
  for label,cwd,script,marker in jobs:
   st=time.monotonic();p=subprocess.run([gp,'-q','-s','128M','-D','parisizemax=1G',script],cwd=copy/cwd,capture_output=True,text=True,timeout=120)
   if p.returncode or p.stderr.strip() or marker not in p.stdout:raise SystemExit(f'GP_REPLAY_FAILED {label}\n{p.stderr}\n{p.stdout}')
   saved=root/cwd/(pathlib.Path(script).stem+'.out')
   identical=(not saved.exists()) or p.stdout==saved.read_text()
   if saved.exists() and not identical:raise SystemExit('OUTPUT_MISMATCH '+label)
   out['replays'].append({'label':label,'status':'PASS','saved_stdout_identical':identical,'seconds':round(time.monotonic()-st,3),'stdout':p.stdout})
  for script,result in [('check_admission_matrices.py','ADMISSION_MATRIX_CHECK.json'),('check_representation_screen.py','REPRESENTATION_CHECK.json')]:
   p=subprocess.run([sys.executable,script],cwd=copy/'reviewer',capture_output=True,text=True,timeout=30)
   if p.returncode:raise SystemExit(f'PYTHON_REPLAY_FAILED {script}\n{p.stderr}')
   if (copy/'reviewer'/result).read_bytes()!=(root/'reviewer'/result).read_bytes():raise SystemExit('PYTHON_OUTPUT_MISMATCH '+script)
   out['replays'].append({'label':script,'status':'PASS','saved_result_identical':True})
print(json.dumps(out,indent=2))
