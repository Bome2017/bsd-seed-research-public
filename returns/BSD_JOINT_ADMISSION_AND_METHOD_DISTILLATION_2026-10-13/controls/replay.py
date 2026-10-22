#!/usr/bin/env python3
"""Fresh complete-source replays: certified BNF, maps, matrices, precision checks."""
import argparse,json,shutil,subprocess,tempfile,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--gp',required=True);args=p.parse_args()
root=Path(__file__).resolve().parent
out=[]
for name in ['389a1','433a1','655a1']:
 with tempfile.TemporaryDirectory(prefix='bsd-joint-'+name+'-') as td:
  r=Path(td);shutil.copytree(root/'lib',r/'lib');d=r/name;d.mkdir()
  rr=[]
  for script,marker in [('run.gp','CONTROL_COMPLETE'),('analyze.gp','ANALYSIS_COMPLETE')]:
   payload=(root/name/script).read_bytes()
   x=subprocess.run([args.gp,'-s','100000000','-q','-f'],input=payload,cwd=d,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=100)
   stdout=x.stdout.decode();stderr=x.stderr.decode()
   unexpected=[line for line in stderr.splitlines() if line.strip() and not line.strip().startswith('***   Warning: new maximum stack size =')]
   assert x.returncode==0 and marker in stdout and not unexpected,(name,script,x.returncode,stdout,stderr)
   if script=='run.gp':assert 'BNF_CERTIFIED=1' in stdout and 'POINT_CLASS_RANK=2' in stdout,(name,stdout)
   rr.append({'script':script,'marker':marker,'stderr_only_expected_stack_warning':not unexpected})
  actual=json.loads((d/'matrices.json').read_text());saved=json.loads((root/name/'matrices.json').read_text())
  assert actual==saved,(name,'matrix replay differs')
  out.append({'curve':name,'complete_source_rebuilt_and_bnfcertified':True,'matrices_identical':True,'checks':rr,'matrix_sha256':hashlib.sha256((d/'matrices.json').read_bytes()).hexdigest()})
print(json.dumps({'status':'COMPLETE_SOURCE_REPLAY_PASS','controls':out},indent=2))
