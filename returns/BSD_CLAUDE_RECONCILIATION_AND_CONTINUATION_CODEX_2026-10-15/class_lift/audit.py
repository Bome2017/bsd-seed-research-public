from pathlib import Path
import hashlib,json,subprocess,re,sys,time
R=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14')
OLD=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13')
OUT=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
labels=['1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(p,base):
 rows=[]
 for line in p.read_text().splitlines():
  h,n=line.split(None,1);n=n.lstrip('* ');f=base/n
  rows.append({'path':n,'match':f.is_file() and sha(f)==h,'expected':h,'actual':sha(f) if f.is_file() else None})
 return {'total':len(rows),'matches':sum(r['match'] for r in rows),'failures':[r for r in rows if not r['match']]}
report={'manifests':{'continuation':manifest(R/'continuation/MANIFEST_CONTINUATION.sha256',R),'atcopy_vs_original':manifest(R/'continuation/ORIGINAL_MANIFEST_AT_COPY.sha256',OLD),'atcopy_vs_copy':manifest(R/'continuation/ORIGINAL_MANIFEST_AT_COPY.sha256',R)}}
# Exact next-24 selection independent of the extension script.
first=json.loads((R/'search/SCAN_CANDIDATES.json').read_text());oldlabels={c['label'] for c in first};pool=[]
for line in (R/'search/rank2_candidates.txt').read_text().splitlines():
 w=line.split();label=''.join(w[:3])
 if w[2]=='1' and int(w[0])%3 and label not in oldlabels|{'389a1','433a1','655a1'}:pool.append(label)
extrows=json.loads((R/'search/SCAN_CANDIDATES_EXT.json').read_text());assert [x['label'] for x in extrows]==pool[:24]
s=json.loads((R/'search/SCAN_STATE_EXT.json').read_text())['results'];assert [x['candidate'] for x in s]==pool[:24]
report['scan']={'count':24,'next24_confirmed':True,'statuses':{k:sum(x['status']==k for x in s) for k in sorted({x['status'] for x in s})},'selected_new_count':len(labels),'table_total':len(json.loads((R/'continuation/ALL_RELEVANT_CURVES.json').read_text()))}
# Read-only replays; no BNF certification, source search, or original writes.
inputs={x['label']:x for x in extrows}
replays=[]
for label in labels:
 base=label.split('_')[0];model=inputs[base]['model'];dest=OUT/label;dest.mkdir(exist_ok=True)
 jobs=[('identities',[GP,'-q','-f'],(R/f'review/check_{label}_identities.gp').read_bytes()),('matrix',[sys.executable,'-I',str(R/'review/check_718b1_matrices.py'),label],None),('hensel',[sys.executable,'-I',str(R/'continuation/check_local_hensel_ext.py'),label,model],None),('transvection',[sys.executable,'-I',str(R/'continuation/transvection.py'),label,model],None)]
 for kind,cmd,data in jobs:
  t=time.monotonic();a=subprocess.run(cmd,input=data,cwd=R,capture_output=True,timeout=40)
  (dest/f'{kind}.out').write_bytes(a.stdout);(dest/f'{kind}.err').write_bytes(a.stderr)
  err=a.stderr.decode(errors='replace');bad=[line for line in err.splitlines() if line.strip() and not re.match(r'\s*\*\*\*\s+(?:[A-Za-z_]+:\s+)?Warning: (new maximum stack size =|increasing stack size to)',line)]
  expected=R/f'review/{label}_{dict(identities="identity_review",matrix="matrix_review",hensel="hensel_review",transvection="transvection")[kind]}.{dict(identities="out",matrix="json",hensel="json",transvection="json")[kind]}'
  replays.append({'curve':label,'kind':kind,'rc':a.returncode,'stderr_clean_except_stack_warnings':not bad,'unexpected_stderr':bad,'byte_identical_saved_stdout':expected.is_file() and expected.read_bytes()==a.stdout,'seconds':round(time.monotonic()-t,3)})
report['replays']=replays
(OUT/'audit_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
