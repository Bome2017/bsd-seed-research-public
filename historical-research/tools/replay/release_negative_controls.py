from pathlib import Path
import tempfile,shutil,subprocess,sys,json
R=Path(__file__).resolve().parents[2]
results=[]
with tempfile.TemporaryDirectory() as td:
 t=Path(td)/'release';shutil.copytree(R,t,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
 p=t/'claims/spec/part1_core.py';original=p.read_text();p.write_text(original.replace('E has no complex multiplication','NEGATIVE CONTROL: edited title',1))
 r=subprocess.run([sys.executable,'-B','tools/build_index.py','--check'],cwd=t,capture_output=True,text=True)
 assert r.returncode!=0 and 'stale' in r.stdout+r.stderr
 results.append({'test':'spec drift','result':'REJECTED'})
 p.write_text(original)
 p=t/'claims/spec/__init__.py';original=p.read_text();p.write_text(original+"\nCLAIMS[0]['depends_on'] = [CLAIMS[0]['id']]\n")
 r=subprocess.run([sys.executable,'-B','tools/build_index.py','--check'],cwd=t,capture_output=True,text=True)
 assert r.returncode!=0 and 'dependency cycle' in r.stdout+r.stderr
 results.append({'test':'dependency self-cycle','result':'REJECTED'})
 p.write_text(original)
 # Imported VERIFICATION.json still says PASS, but this fake verifier writes nothing.
 p=t/'evidence/src/BSD_2243_D5_INDEPENDENT_2026-09-23/verify_d5.py';p.write_text('pass\n')
 r=subprocess.run([sys.executable,'-B','tools/verify_release.py'],cwd=t,capture_output=True,text=True,timeout=60)
 assert r.returncode!=0 and 'FAIL  replay 2243-adic height verifier' in r.stdout
 results.append({'test':'no fresh D5 verifier output despite imported PASS','result':'REJECTED'})
# Results are printed; the release and its retained result log remain unchanged.
print(json.dumps(results))
