from pathlib import Path
import os,sys,json,time,subprocess,signal
r=Path(__file__).parent/'restart_probe';r.mkdir(exist_ok=True)
ap=r/'ap';ap.mkdir(exist_ok=True)
f=ap/'ap_000000.bin'
if not f.exists(): f.symlink_to('/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap/ap_000000.bin')
events=r/'events.jsonl'
stub=r/'delayed_stream.py'
stub.write_text('#!'+sys.executable+'\nimport os,sys,time,json\nfrom pathlib import Path\nwith Path('+repr(str(events))+').open("a") as f:\n f.write(json.dumps({"pid":os.getpid(),"segment":sys.argv[1],"directory":sys.argv[2]})+"\\n"); f.flush(); os.fsync(f.fileno())\ntime.sleep(60)\nraise SystemExit(17)\n')
stub.chmod(0o755)
cmd=[str(r.parent/'acc2243v2_codex'),'run','0','-22735','0','106272484','0','27','2167729337579528','1','33554431','16777216',str(ap),'1',str(r/'out'),'500000000','40']
env={k:v for k,v in os.environ.items() if not k.startswith('ACC_')};env.update(ACC_SELECT='L1',ACC_STREAM_CMD=str(stub))
procs=[];handles=[]
def start(i):
 out=(r/f'run{i}.log').open('w');err=(r/f'run{i}.err').open('w');handles.extend([out,err]);p=subprocess.Popen(cmd,stdout=out,stderr=err,env=env,start_new_session=True);procs.append(p);return p
def wait_events(n):
 until=time.monotonic()+10
 while time.monotonic()<until:
  rows=[json.loads(x) for x in events.read_text().splitlines()] if events.exists() else []
  if len(rows)>=n:return rows
  time.sleep(.05)
 raise RuntimeError('stream did not start')
try:
 p=start(1);rows=wait_events(1);p.kill();p.wait();assert not list((r/'out').glob('ckpt_g*.bin'))
 old_alive=True
 try: os.kill(rows[0]['pid'],0)
 except ProcessLookupError: old_alive=False
 q=start(2);rows=wait_events(2)
 res={'same_stream_directory':rows[0]['directory']==rows[1]['directory'],'old_stream_alive_after_parent_kill':old_alive,'checkpoint_count_at_restart':0,'events':rows,'cmd':cmd}
 (r/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
finally:
 for p in procs:
  try:os.killpg(p.pid,signal.SIGKILL)
  except ProcessLookupError:pass
  p.wait()
 for h in handles:h.close()
