"""Aggregate 600-second execution cap; capture resource usage and exact outputs."""
from pathlib import Path
import json, resource, subprocess, sys, time
root=Path(__file__).resolve().parents[1]
record=root/'evidence'/'execution_budget.json'
history=json.loads(record.read_text()) if record.exists() else []
remaining=600-sum(x['wall_seconds'] for x in history)
if remaining<=0: raise SystemExit('Execution budget exhausted')
label=sys.argv[1]
if not label.replace('_','').isalnum(): raise SystemExit('Invalid run label')
start=time.monotonic()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (root/'evidence'/(label+'.log')).open('w') as out:
    p=subprocess.Popen(sys.argv[2:],stdout=out,stderr=subprocess.STDOUT,cwd=root)
    try: code=p.wait(timeout=remaining)
    except subprocess.TimeoutExpired:
        p.kill();p.wait();code=124
after=resource.getrusage(resource.RUSAGE_CHILDREN)
row={'label':label,'command':sys.argv[2:],'exit_code':code,
     'wall_seconds':time.monotonic()-start,
     'cpu_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
     'peak_rss_bytes':after.ru_maxrss}
history.append(row);record.write_text(json.dumps(history,indent=2)+'\n')
print(json.dumps(row,indent=2))
if after.ru_maxrss>2_000_000_000: raise SystemExit('Memory budget exceeded')
raise SystemExit(code)
