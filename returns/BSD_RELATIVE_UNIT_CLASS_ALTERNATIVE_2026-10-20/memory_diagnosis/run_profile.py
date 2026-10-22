import argparse,hashlib,json,re,subprocess,time
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument("stage")
ap.add_argument("cap",type=float)
ap.add_argument("marker")
ap.add_argument("--stack",default="512M")
a=ap.parse_args()
r=Path(__file__).resolve().parent
gp="/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp"
script=r/(a.stage+".gp")
command=["/usr/bin/time","-l",gp,"-q","-f","-s",a.stack,script.name]
seal={"command":command,"script_sha256":hashlib.sha256(script.read_bytes()).hexdigest(),"wall_cap":a.cap,"marker":a.marker}
(r/(a.stage+".seal.json")).write_text(json.dumps(seal,indent=2)+"\n")
t=time.monotonic()
try:
 p=subprocess.run(command,cwd=r,capture_output=True,timeout=a.cap)
 out,err,code,timed=p.stdout,p.stderr,p.returncode,False
except subprocess.TimeoutExpired as e:
 out,err,code,timed=e.stdout or b"",e.stderr or b"",None,True
(r/(a.stage+".out")).write_bytes(out)
(r/(a.stage+".err")).write_bytes(err)
s=err.decode(errors="replace")
m=re.search(r"(\d+)\s+maximum resident set size",s)
receipt={**seal,"elapsed_seconds":time.monotonic()-t,"exit_code":code,"timed_out":timed,
 "maximum_resident_set_bytes":int(m.group(1)) if m else None,
 "completion_marker":a.marker.encode() in out,
 "explicit_gp_error":bool(re.search(r"\*\*\*.*(overflows|error|alarm|precision too low|not a function)",s)),
 "stdout_sha256":hashlib.sha256(out).hexdigest(),"stderr_sha256":hashlib.sha256(err).hexdigest()}
receipt["accepted"]=code==0 and receipt["completion_marker"] and not receipt["explicit_gp_error"]
(r/(a.stage+".receipt.json")).write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
