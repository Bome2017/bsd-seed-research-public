import hashlib,json,subprocess,time,sys
from pathlib import Path
root=Path(__file__).resolve().parent
gp="/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp"
stage=sys.argv[1]
marker=sys.argv[2]
cap=float(sys.argv[3])
script=root/(stage+".gp")
seal={"script":script.name,"sha256":hashlib.sha256(script.read_bytes()).hexdigest(),"marker":marker,"wall_cap_seconds":cap,"started_unix":time.time()}
(root/(stage+".seal.json")).write_text(json.dumps(seal,indent=2)+"\n")
t=time.monotonic()
try:
 p=subprocess.run([gp,"-q","-f","-s","2G",script.name],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=cap)
 out,err,code,timed=p.stdout,p.stderr,p.returncode,False
except subprocess.TimeoutExpired as e:
 out,err,code,timed=e.stdout or b"",e.stderr or b"",None,True
(root/(stage+".out")).write_bytes(out)
(root/(stage+".err")).write_bytes(err)
r={**seal,"elapsed_seconds":time.monotonic()-t,"exit_code":code,"timed_out":timed,"accepted":code==0 and not err.strip() and marker.encode() in out,"stdout_sha256":hashlib.sha256(out).hexdigest(),"stderr_sha256":hashlib.sha256(err).hexdigest()}
(root/(stage+".receipt.json")).write_text(json.dumps(r,indent=2)+"\n")
print(json.dumps(r,indent=2))
