"""Strict wrapper for the independent fixed-data audit; no BNF certification."""
from pathlib import Path
import argparse, hashlib, json, subprocess
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--gp',required=True);args=ap.parse_args()
receipts=[]
for stem,rootfile,need in [('independent','independent_scalar_roots.gp','TRUE_SEL3_DIM=2'),('independent_28042','independent_28042_scalar_roots.gp','TRUE_SEL3_DIM_AT_LEAST=3')]:
 (P/rootfile).unlink(missing_ok=True)
 r=subprocess.run([args.gp,'-fq','-s','128000000','--default','parisizemax=1000000000',stem+'.gp'],cwd=P,capture_output=True,timeout=65)
 (P/(stem+'.out')).write_bytes(r.stdout);(P/(stem+'.err')).write_bytes(r.stderr)
 ok=r.returncode==0 and not r.stderr and b'INDEPENDENT_COMPLETE;' in r.stdout and need.encode() in r.stdout
 receipts.append({'script':stem+'.gp','status':'PASS' if ok else 'REJECTED','returncode':r.returncode,'stderr_bytes':len(r.stderr),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest()})
 if not ok:
  (P/'AUDIT_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n');raise SystemExit('rejected GP audit: '+stem)
(P/'AUDIT_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n')
print(json.dumps(receipts,indent=2))
