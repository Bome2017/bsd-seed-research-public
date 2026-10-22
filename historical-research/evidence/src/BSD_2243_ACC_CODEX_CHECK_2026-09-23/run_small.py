from pathlib import Path
import subprocess,resource,time,json,datetime,os
r=Path(__file__).parent
cmd=[str(r/'acc2243v2_codex'),'run','0','-22735','0','106272484','0','27','2167729337579528','1','4831838207','16777216','/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap','8',str(r/'m27'),'500000000','40']
env={k:v for k,v in os.environ.items() if not k.startswith('ACC_')}
def limits(): resource.setrlimit(resource.RLIMIT_CPU,(6000,6050))
start=time.monotonic()
with (r/'m27_run.log').open('w') as out, (r/'m27_run.err').open('w') as err:
 p=subprocess.Popen(cmd,stdout=out,stderr=err,env=env,preexec_fn=limits)
 st=json.loads((r/'STATE.json').read_text()); st.update(phase='M27_REPLAY_RUNNING',pid=p.pid,command=cmd); (r/'STATE.json').write_text(json.dumps(st,indent=2)+'\n')
 try: rc=p.wait(timeout=2400)
 except subprocess.TimeoutExpired:
  p.terminate(); p.wait(timeout=20); rc=124
usage=resource.getrusage(resource.RUSAGE_CHILDREN)
res={'exit_code':rc,'wall_seconds':time.monotonic()-start,'user_seconds':usage.ru_utime,'system_seconds':usage.ru_stime,'max_rss_bytes':usage.ru_maxrss,'command':cmd}
(r/'M27_RUNTIME.json').write_text(json.dumps(res,indent=2)+'\n')
st=json.loads((r/'STATE.json').read_text()); st.update(phase='M27_REPLAY_DONE' if rc==0 else 'M27_REPLAY_FAILED',replay_result=res); (r/'STATE.json').write_text(json.dumps(st,indent=2)+'\n')
with (r/'CHECKPOINTS.jsonl').open('a') as out: out.write(json.dumps({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'event':'m27 replay finished','result':res})+'\n')
print(json.dumps(res),flush=True)
raise SystemExit(rc)
