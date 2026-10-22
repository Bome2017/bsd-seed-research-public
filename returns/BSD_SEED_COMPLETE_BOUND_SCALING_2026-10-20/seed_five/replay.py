"""Regenerate accepted seed arithmetic, without repeating the failed BNF."""
import argparse,hashlib,json,shutil,subprocess,tempfile,time
from pathlib import Path
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser()
ap.add_argument("--gp",default="/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp")
ap.add_argument("--output")
a=ap.parse_args()
out=Path(a.output) if a.output else Path(tempfile.mkdtemp(prefix="bsd_seed5_replay_"))
if a.output:
 out.mkdir(parents=True,exist_ok=False)
stages=[("construct","ACTUAL_SEED_P5_FIELD_AND_SCALAR_PASS",120),
        ("divisors","ACTUAL_SEED_P5_DIVISOR_ACTION_PASS",35),
        ("local_seed","SEED_LOCAL_BINDING_PASS",15)]
receipts=[]
for name,marker,cap in stages:
 shutil.copy2(root/(name+".gp"),out/(name+".gp"))
 t=time.monotonic()
 p=subprocess.run([a.gp,"-q","-f","-s","512M",name+".gp"],cwd=out,capture_output=True,timeout=cap)
 (out/(name+".out")).write_bytes(p.stdout)
 (out/(name+".err")).write_bytes(p.stderr)
 good=p.returncode==0 and not p.stderr.strip() and marker.encode() in p.stdout
 receipts.append({"stage":name,"accepted":good,"elapsed_seconds":time.monotonic()-t})
 if not good:raise RuntimeError(receipts[-1])
shutil.copy2(root/"local_divisor.py",out/"local_divisor.py")
p=subprocess.run(["python3",str(out/"local_divisor.py")],cwd=out,capture_output=True,timeout=10)
assert p.returncode==0 and not p.stderr.strip()
bindings={}
for name in ["raw_field.gp","field.gp","divisors.gpout","LOCAL_DIVISOR_CHECK.json"]:
 h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 assert h(root/name)==h(out/name),name
 bindings[name]=h(out/name)
result={"status":"PASS","scope":"Accepted seed field, scalar, divisor and local model only; no BNF rerun","stages":receipts,"byte_identical_bindings":bindings}
(out/"REPLAY_RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
