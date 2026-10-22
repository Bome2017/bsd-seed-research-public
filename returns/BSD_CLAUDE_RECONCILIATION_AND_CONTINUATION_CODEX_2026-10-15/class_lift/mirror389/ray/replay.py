from pathlib import Path
import subprocess,json,re,time,hashlib
R=Path(__file__).resolve().parent;O=R/'clean_replay';
if O.exists():
 import shutil
 i=1
 while (R/f'prior_clean_replay_{i}').exists():i+=1
 shutil.move(str(O),str(R/f'prior_clean_replay_{i}'))
O.mkdir();GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
s=(R/'construct.gp').read_text()
q=(R/'quotient.gp').read_text()
results=[];start=time.monotonic()
for name,script,marker in [('construct',s,'ACTUAL_RAY_GROUP_AND_LIFT_PASS'),('quotient',q,'ACTUAL_CRT_TO_RAY_QUOTIENT_PASS')]:
 (O/(name+'.gp')).write_text(script);remaining=180-(time.monotonic()-start)
 a=subprocess.run([GP,'-s','100000000','-q','-f'],input=script.encode(),cwd=O,capture_output=True,timeout=remaining)
 (O/(name+'.out')).write_bytes(a.stdout);(O/(name+'.err')).write_bytes(a.stderr)
 bad=[l for l in a.stderr.decode().splitlines() if l.strip() and not re.match(r'\s*\*\*\*\s+(?:[A-Za-z_]+:\s+)?Warning: (new maximum stack size =|increasing stack size to)',l)]
 passed=a.returncode==0 and not bad and marker in a.stdout.decode();results.append({'stage':name,'pass':passed,'rc':a.returncode,'unexpected_stderr':bad,'output':a.stdout.decode()});assert passed,results[-1]
res={'status':'CLEAN_ACTUAL_RAY_REPLAY_PASS','seconds':time.monotonic()-start,'stages':results,'original_saved_bnf_sha256':hashlib.sha256(Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/bnf.bin').read_bytes()).hexdigest()}
(R/'REPLAY.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
