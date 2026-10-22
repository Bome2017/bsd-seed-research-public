#!/Library/Developer/CommandLineTools/usr/bin/python3
import os,sys,time,json
from pathlib import Path
with Path('/Users/bsm/BSD_2243_ACC_CODEX_CHECK_2026-09-23/restart_probe/events.jsonl').open("a") as f:
 f.write(json.dumps({"pid":os.getpid(),"segment":sys.argv[1],"directory":sys.argv[2]})+"\n"); f.flush(); os.fsync(f.fileno())
time.sleep(60)
raise SystemExit(17)
