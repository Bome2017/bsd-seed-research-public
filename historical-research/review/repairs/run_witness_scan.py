#!/usr/bin/env python3
"""Supplement the retained legacy checks. This scans about 74 GB read-only.
Requires macOS CommonCrypto, clang and the external witness corpus; never runs by default.
Output is new evidence, not a replacement for the retained point-arithmetic checks.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,subprocess,tempfile,time
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--research-root',type=Path,required=True)
ap.add_argument('--output-directory',type=Path,required=True)
ap.add_argument('--budget-seconds',type=int,default=600)
a=ap.parse_args()
if a.output_directory.exists():raise SystemExit('Choose a new output directory; existing records are not overwritten.')
a.output_directory.mkdir(parents=True)
roots=['BSD_RIGOROUS_STREAM_CORE_2026-09-19/runs/seed150M','BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run','BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run','BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p7/run','BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p11/run','BSD_SEED_P13_RUN_2026-09-21/run']
expected=[9,885,467,43,1405,948]
files=[]
for root,n in zip(roots,expected):
 found=sorted((a.research_root/root/'wit').glob('wit_*.bin'))
 if len(found)!=n:raise SystemExit(f'Corpus scope changed: {root}: expected {n}, found {len(found)}')
 files+=found
start=time.monotonic();log=a.output_directory/'scan.tsv'
with tempfile.TemporaryDirectory() as tmp:
 exe=Path(tmp)/'scanner'
 subprocess.run(['clang','-O2','-Wno-deprecated-declarations',str(Path(__file__).with_name('witness_structure_scan.c')),'-o',str(exe)],check=True,timeout=30)
 def check(f):
  remain=a.budget_seconds-(time.monotonic()-start)
  if remain<=0:raise RuntimeError('Time budget exhausted; completed rows are retained.')
  r=subprocess.run([str(exe),str(f)],capture_output=True,text=True,timeout=remain)
  if r.returncode:raise RuntimeError(r.stderr)
  row=r.stdout.rstrip().split('\t');run=f.parent.parent;sg=int(f.stem.split('_')[1])
  if 'seed150M' in str(run):
   old=next(l.split()[0] for l in (run/'logs/wit_files.sha256').read_text().splitlines() if l.split()[-1].endswith(f.name))
  else:old=(run/f'logs/witsha_{sg}.txt').read_text().split()[0]
  if row[0]!=old:raise RuntimeError('Retained hash mismatch: '+str(f))
  return row
 rows=[]
 with ThreadPoolExecutor(max_workers=2) as pool,log.open('w') as out:
  out.write('sha256\tbytes\tlo\thi\twitnesses\tmax_factor_entries\tmax_product\tpath\n')
  for row in pool.map(check,files):
   out.write('\t'.join(row)+'\n');out.flush();rows.append(row)
summary={'status':'PASS','scope':'Distinctness and safe products only; hashes matched. Not a fresh EC/primality replay.', 'files':len(rows),'witness_records_including_overlaps':sum(int(r[4]) for r in rows),'bytes_read':sum(int(r[1]) for r in rows),'elapsed_seconds':time.monotonic()-start,'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
(a.output_directory/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
