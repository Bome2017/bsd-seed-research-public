from pathlib import Path
import subprocess,json,time,sys
p=Path(sys.argv[1]);stage=sys.argv[2];marker=sys.argv[3];t=time.time()
try:
 r=subprocess.run(['/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp','-s100000000','-q','-f'],cwd=p,input=(p/(stage+'.gp')).read_bytes(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=130)
 out,err,rc=r.stdout,r.stderr,r.returncode
except subprocess.TimeoutExpired as e:out,err,rc=e.stdout or b'',e.stderr or b'',-999
(p/(stage+'.out')).write_bytes(out);(p/(stage+'.err')).write_bytes(err)
okay=rc==0 and marker.encode() in out and all(not s.strip() or 'Warning: new maximum stack size' in s for s in err.decode().splitlines())
(p/(stage+'_receipt.json')).write_text(json.dumps({'passed':okay,'seconds':time.time()-t,'returncode':rc},indent=2)+'\n')
print(out.decode());print(err.decode());sys.exit(0 if okay else 1)
