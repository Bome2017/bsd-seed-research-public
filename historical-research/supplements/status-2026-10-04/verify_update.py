"""Verify the documentation supplement; optionally replay the frozen release checks.

This never changes the frozen claim ledger or runs new production arithmetic.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,message):
    if not ok:raise SystemExit('FAIL: '+message)

ap=argparse.ArgumentParser()
ap.add_argument('--with-release-checks',action='store_true')
args=ap.parse_args()
meta=json.loads((HERE/'UPDATE.json').read_text())
base=json.loads((HERE/'BASE_FILES.json').read_text())
rows=[]
for line in (HERE/'MANIFEST.sha256').read_text().splitlines():
    h,n=line.split('  ',1)
    require(not Path(n).is_absolute() and '..' not in Path(n).parts,'safe manifest path')
    rows.append((h,n))
require(len(rows)==len({n for _,n in rows}),'unique supplement manifest paths')
for h,n in rows:require(sha(HERE/n)==h,'supplement hash '+n)
actual={str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file() and p!=HERE/'MANIFEST.sha256' and '__pycache__' not in p.parts}
require(actual=={n for _,n in rows},'exact supplement file set')
require(sha(ROOT/'README.md')==meta['current_readme_sha256'],'current navigation README')
for r in base:
    p=HERE/'base/README.md' if r['path']=='README.md' else ROOT/r['path']
    require(sha(p)==r['sha256'],'frozen base '+r['path'])
for r in json.loads((HERE/'SOURCE_BINDINGS.json').read_text()):
    require(sha(HERE/r['path'])==r['sha256'],'captured source '+r['path'])
allowed={r['path'] for r in base}|{str(HERE.relative_to(ROOT))+'/'+n for _,n in rows}|{str(HERE.relative_to(ROOT))+'/MANIFEST.sha256'}
actualroot={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts and '__pycache__' not in p.parts}
require(actualroot==allowed,'only frozen base and declared documentation supplement')
release_checks=[]
if args.with_release_checks:
    with tempfile.TemporaryDirectory(prefix='bsd_v026_snapshot_') as t:
        dst=Path(t)
        for r in base:
            src=HERE/'base/README.md' if r['path']=='README.md' else ROOT/r['path']
            p=dst/r['path'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,p)
        for command in ['tools/verify_patch_release.py','tools/verify_release.py']:
            r=subprocess.run([sys.executable,'-B',str(dst/command)],cwd=dst,text=True,capture_output=True)
            if r.returncode:
                print(r.stdout[-7000:]+r.stderr[-7000:]);raise SystemExit('FAIL: '+command)
            release_checks.append({'command':command,'exit_code':r.returncode,'tail':r.stdout.splitlines()[-3:]})
print(json.dumps({'status':'PASS','frozen_base_commit':meta['base_commit'],'base_files':len(base),'supplement_manifest_entries':len(rows),'release_checks':release_checks,'scope':'integrity and retained release checks; no new mathematical promotion'},indent=2))
