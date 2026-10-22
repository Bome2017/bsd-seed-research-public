from pathlib import Path
import subprocess,time,json,os,signal,sys
R=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
name=sys.argv[1];budget=float(sys.argv[2]);start=time.monotonic();peak=0;stop=None
with (R/name).open() as inp,(R/(name+'.out')).open('w') as out,(R/(name+'.err')).open('w') as err:
 p=subprocess.Popen([GP,'-s','64000000','-D','parisizemax=1000000000','-q','-f'],stdin=inp,stdout=out,stderr=err,cwd=R,start_new_session=True)
 while p.poll() is None:
  if time.monotonic()-start>budget:stop='WALL_BUDGET';os.killpg(p.pid,signal.SIGKILL);break
  r=subprocess.run(['ps','-o','rss=','-p',str(p.pid)],capture_output=True,text=True)
  try:rss=int(r.stdout.strip())*1024;peak=max(peak,rss)
  except ValueError:pass
  if peak>1073741824:stop='RSS_BUDGET';os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.1)
 code=p.wait()
result={'script':name,'budget_seconds':budget,'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':peak,'exit_code':code,'stop':stop};(R/(name+'.receipt.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
