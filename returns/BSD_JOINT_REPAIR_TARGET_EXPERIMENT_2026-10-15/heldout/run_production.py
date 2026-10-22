from pathlib import Path
import hashlib,json,subprocess,time,shutil
R=Path(__file__).resolve().parent
base=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14')
old=Path('/Users/bsm/BSD_CLAUDE_RECONCILIATION_AND_CONTINUATION_CODEX_2026-10-15')
gp='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
labels=['718b1','997c1','1070a1','1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh','mirror389','seed3']
receipts=[]
for label in labels:
 o=R/label;o.mkdir(exist_ok=False)
 if label=='seed3':
  b=Path('/Users/bsm/BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13/data');data=b/'stage1_data.gp';nf=Path('/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/nf_only.gp');points=Path('/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/actual_representatives.gp');matrix=b/'MATRICES.json'
  setup=f'D=read("{data}");G=D[1];nf=read("{nf}");A=read("{points}");E=ellinit(A[1]);T=A[6];'
  inputs=[data,nf,points,matrix]
 else:
  if label=='mirror389':data=old/'class_lift/mirror389/data.gp';bnf=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/bnf.bin');matrix=old/'class_lift/mirror389/matrices.json'
  else:data=base/f'arithmetic/{label}/data.gp';bnf=base/f'search/{label}/bnf.bin';matrix=base/f'arithmetic/{label}/matrices.json'
  setup=f'D=read("{data}");B=read("{bnf}");nf=B.nf;E=D[1];T=D[5];G=D[6];'
  inputs=[data,bnf,matrix]
 script=R/'produce_template.gp';(o/'produce.gp').write_text(script.read_text().replace('@SETUP@',setup));shutil.copyfile(matrix,o/'matrices.json')
 binding=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in inputs+[script,R/'PREDICTIONS.md']]
 (o/'INPUTS.json').write_text(json.dumps(binding,indent=2)+'\n')
 st=time.monotonic()
 try:q=subprocess.run([gp,'-q','-f','-s','128000000','produce.gp'],cwd=o,timeout=130,capture_output=True,text=True)
 except subprocess.TimeoutExpired as e:
  (o/'TIMEOUT.json').write_text(json.dumps({'timeout_seconds':130}));raise
 (o/'producer.out').write_text(q.stdout);(o/'producer.err').write_text(q.stderr)
 assert q.returncode==0 and 'HELDOUT_BLOCK_PRODUCER_PASS' in q.stdout,(label,q.stdout,q.stderr)
 assert not any('***' in line and 'Warning:' not in line for line in q.stderr.splitlines()),(label,q.stderr)
 blocks=[json.loads(x) for x in (o/'blocks.jsonl').read_text().splitlines()];assert len(blocks)==12
 (o/'blocks.json').write_text(json.dumps({'blocks':blocks},indent=2)+'\n')
 rec={'label':label,'seconds':time.monotonic()-st,'exit_code':q.returncode,'primes':[x['q'] for x in blocks],'source_sha256':hashlib.sha256((o/'source.json').read_bytes()).hexdigest(),'blocks_sha256':hashlib.sha256((o/'blocks.json').read_bytes()).hexdigest()};receipts.append(rec)
 (R/'PRODUCTION_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n')
 print(json.dumps(rec),flush=True)
