import pathlib,subprocess,sys,json,time,hashlib,datetime
R=pathlib.Path(__file__).resolve().parent; name=sys.argv[1]; cap=int(sys.argv[2]);marker=sys.argv[3]
gp='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
p=R/name;start=time.monotonic();timed=False
try:
 c=subprocess.run([gp,'-q','-f','-s','256M',str(p)],cwd=R,capture_output=True,timeout=cap);out,err,rc=c.stdout,c.stderr,c.returncode
except subprocess.TimeoutExpired as e: out,err,rc=e.stdout or b'',e.stderr or b'',None;timed=True
p.with_suffix(p.suffix+'.out').write_bytes(out);p.with_suffix(p.suffix+'.err').write_bytes(err)
r=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),script=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),cap_seconds=cap,elapsed=time.monotonic()-start,timeout=timed,returncode=rc,stdout_sha256=hashlib.sha256(out).hexdigest(),stderr_sha256=hashlib.sha256(err).hexdigest(),accepted=rc==0 and not err and marker.encode() in out)
p.with_suffix(p.suffix+'.receipt.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));print(out.decode()[-3000:]);print(err.decode()[-1000:]);sys.exit(0 if r['accepted'] else 1)
