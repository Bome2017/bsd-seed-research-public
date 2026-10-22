#!/usr/bin/env python3
"""Run exactly the frozen singleton once; preserve every resource stop."""
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time

BASE = Path(__file__).resolve().parent
FREEZE = BASE / 'FROZEN_RUN_PACKAGE_p83_l167'
CFG = json.loads((FREEZE / 'config/RUN_CONFIG.json').read_text())
OUT = Path(CFG['outdir'])

def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def save(path, obj):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(obj, indent=2) + '\n')
    temporary.replace(path)

def cpu_seconds(value):
    if '-' in value:
        days, value = value.split('-', 1)
    else:
        days = 0
    fields = list(map(float, value.split(':')))
    return int(days)*86400 + sum(x*60**i for i, x in enumerate(reversed(fields)))

def resources(group):
    rows = subprocess.check_output(['ps','-axo','pgid=,pid=,time=,rss=,command='], text=True)
    processes = []
    for row in rows.splitlines():
        values = row.split(None, 4)
        if len(values) == 5 and int(values[0]) == group:
            processes.append({'pid':int(values[1]),'cpu_seconds':cpu_seconds(values[2]),
                              'rss_bytes':int(values[3])*1024,'command':values[4]})
    return processes

def output_inventory():
    size = 0
    large = smooth = 0
    if OUT.exists():
        for path in OUT.rglob('*'):
            if path.is_file():
                size += path.stat().st_size
                large += path.name.startswith('lseg_') and path.suffix == '.txt'
                smooth += path.name.startswith('blk_') and path.suffix == '.txt'
    return size, large, smooth

def main():
    if OUT.exists():
        raise SystemExit('Refusing existing output directory')
    if (BASE/'MONITOR_START.json').exists():
        raise SystemExit('Refusing a second launch')
    if shutil.disk_usage(BASE).free < CFG['caps']['minimum_free_bytes']:
        raise SystemExit('Available-space floor not met')
    env = os.environ.copy()
    env.update(C=str(FREEZE/'runtime'), PARI=CFG['PARI'], LATDEN=str(CFG['LATDEN']),
               SEGQ=str(CFG['SEGQ']), SIGN=str(CFG['sign']), SINGLETON_AUTHORIZED='yes')
    cmd = ['/usr/bin/caffeinate','-i',str(FREEZE/'checker/run_singleton.sh'), CFG['curve'],
           str(CFG['N']),str(CFG['p']),str(CFG['l']),str(CFG['T']),CFG['apdir'],
           CFG['receipts_glob'],str(OUT),str(CFG['workers']),CFG['pinned_segroot']]
    start = time.monotonic()
    with (BASE/'LAUNCH_STDOUT.txt').open('w') as stdout, (BASE/'LAUNCH_STDERR.txt').open('w') as stderr:
        child = subprocess.Popen(cmd, env=env, stdout=stdout, stderr=stderr, start_new_session=True)
        save(BASE/'MONITOR_START.json', {'utc':utc(),'pid':child.pid,'command':cmd,'caps':CFG['caps']})
        stop_reason = None
        max_cpu = max_rss = 0
        while True:
            code = child.poll()
            procs = resources(child.pid)
            max_cpu = max(max_cpu, sum(p['cpu_seconds'] for p in procs))
            max_rss = max(max_rss, sum(p['rss_bytes'] for p in procs))
            size, large, smooth = output_inventory()
            free = shutil.disk_usage(BASE).free
            elapsed = time.monotonic()-start
            if code is None:
                if elapsed > 3600*CFG['caps']['wall_hours']: stop_reason = 'WALL_CAP'
                elif max_cpu > 3600*CFG['caps']['cpu_hours']: stop_reason = 'CPU_CAP'
                elif size > CFG['caps']['new_bytes']: stop_reason = 'OUTPUT_SIZE_CAP'
                elif free < CFG['caps']['minimum_free_bytes']: stop_reason = 'FREE_SPACE_FLOOR'
            record = {'utc':utc(),'status':'RUNNING' if code is None else 'ENGINE_AND_CHECKER_FINISHED',
                      'returncode':code,'elapsed_seconds':elapsed,'max_observed_cpu_seconds':max_cpu,
                      'max_observed_rss_bytes':max_rss,'output_bytes':size,'free_bytes':free,
                      'large_units':large,'large_expected':3420,'smooth_units':smooth,'smooth_expected':13680,
                      'stop_reason':stop_reason,'processes':procs}
            if stop_reason:
                record['status'] = 'STOPPED_NO_MATHEMATICAL_VERDICT'
                os.killpg(child.pid, signal.SIGTERM)
                try: child.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(child.pid, signal.SIGKILL)
                    child.wait()
            save(BASE/'PROGRESS.json',record)
            with (BASE/'CHECKPOINTS.jsonl').open('a') as checkpoints:
                checkpoints.write(json.dumps({k:v for k,v in record.items() if k!='processes'})+'\n')
            save(BASE/'STATE.json',{'status':record['status'],'selected_prime':83,'auxiliary_prime':167,
                 'progress_file':'PROGRESS.json','production_path':str(OUT),'returncode':code,
                 'stop_reason':stop_reason,'last_checkpoint_utc':record['utc']})
            print(json.dumps({k:record[k] for k in ['utc','status','elapsed_seconds','large_units','smooth_units','returncode']}),flush=True)
            if code is not None or stop_reason: break
            time.sleep(30)
    return 2 if stop_reason else code

if __name__ == '__main__':
    raise SystemExit(main())
