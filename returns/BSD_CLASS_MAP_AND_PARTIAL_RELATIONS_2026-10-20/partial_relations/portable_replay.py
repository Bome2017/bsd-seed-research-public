"""Replay only the sealed selected panel, in a fresh directory, with bundled inputs."""
from pathlib import Path
import argparse,json,gzip,hashlib,subprocess,sys,time
ap=argparse.ArgumentParser();ap.add_argument('--gp',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
R=Path(__file__).resolve().parent;out=a.output.resolve()
if out.exists():raise SystemExit('Refusing existing output directory')
out.mkdir(parents=True);I=out/'inputs';I.mkdir()
bind=json.loads((R/'INPUT_BINDINGS.json').read_text());changes={}
for x in bind['inputs']:
 b=(R/x['bundle_path']).read_bytes();assert hashlib.sha256(b).hexdigest()==x['bundle_sha256']
 if x['bundle_encoding']=='gzip':b=gzip.decompress(b)
 assert hashlib.sha256(b).hexdigest()==x['sha256']
 dest=I/Path(x['path']).name;dest.write_bytes(b);changes[x['path']]=str(dest)
for name in ['selected.gp','private.gp','SELECTED.json']:(out/name).write_bytes((R/name).read_bytes())
for name in ['reconstruct.gp','private_pivots.gp','scalar_pivots.gp','verify_support.py']:
 s=(R/name).read_text()
 for old,new in changes.items():s=s.replace(old,new)
 (out/name).write_text(s)
receipts=[]
for name,marker in [('reconstruct.gp','RECONSTRUCTION_COMPLETE'),('private_pivots.gp','PRIVATE_PIVOT_COMPLETE=[80, 80]'),('scalar_pivots.gp','SCALAR_PIVOT_COMPLETE=')]:
 t=time.monotonic()
 with (out/name).open() as f:
  run=subprocess.run([a.gp,'-s','64000000','-D','parisizemax=1000000000','-q','-f'],stdin=f,cwd=out,capture_output=True,text=True,timeout=120)
 (out/(name+'.out')).write_text(run.stdout);(out/(name+'.err')).write_text(run.stderr)
 ok=run.returncode==0 and marker in run.stdout and not run.stderr.strip()
 receipts.append({'script':name,'seconds':time.monotonic()-t,'exit_code':run.returncode,'marker_present':marker in run.stdout,'stderr_empty':not run.stderr.strip(),'accepted':ok})
 (out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n')
 if not ok:raise SystemExit('Failed required arithmetic marker: '+name)
subprocess.run([sys.executable,str(out/'verify_support.py')],cwd=out,check=True)
print('PORTABLE_SELECTED_PANEL_REPLAY_COMPLETE')
