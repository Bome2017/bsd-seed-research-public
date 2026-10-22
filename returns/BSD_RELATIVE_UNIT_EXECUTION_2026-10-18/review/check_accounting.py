from pathlib import Path
import ast, json, re, hashlib
root=Path(__file__).resolve().parent.parent
s=root/'source'
rows=[ast.literal_eval(line) for line in (s/'norm_trials.gp').read_text().splitlines() if line.strip()]
ideals=json.loads((s/'IDEAL_NORMS.json').read_text())
out=(s/'search.gp.out').read_text()
pattern=r'CHECKPOINT stage=(\d+) amplitude=(\d+) direction=(\d+) ideal=(\d+) exact_norms=(\d+) pure_skips=(\d+) duplicates=(\d+) admitted=(\d+) wall_ms=(\d+)'
ms=list(re.finditer(pattern,out));last=tuple(map(int,ms[-1].groups()))
reject=[row for row in rows if abs(row[5])==ideals[row[3]-1][1]]
res={'status':'SCOPED_OUTPUT_ACCOUNTING_PASS' if len(rows)==last[4] and not reject and last[7]==0 else 'MISMATCH','exact_norm_log_rows':len(rows),'last_complete_checkpoint':dict(zip(['stage','amplitude','direction','ideal','exact_norms','pure_skips','duplicates','admitted','wall_ms'],last)),'logged_exact_norm_matches':len(reject),'no_completion_marker':'SEARCH_SCHEDULE_COMPLETE' not in out,'gp_alarm_recorded':'alarm interrupt' in (s/'search.gp.err').read_text(),'admissions_file_present':(s/'admissions.gp').exists(),'source_norms_recomputed':False,'scope':'Independent arithmetic/accounting comparison of saved exact norm outputs to exact ideal norms; no regeneration of candidate norms or search.','hashes':{n:hashlib.sha256((s/n).read_bytes()).hexdigest() for n in ['search.gp','SEARCH_CONTRACT.md','norm_trials.gp','search.gp.out','search.gp.err','search.gp.receipt.json','IDEAL_NORMS.json']}}
print(json.dumps(res,indent=2))
assert res['status']=='SCOPED_OUTPUT_ACCOUNTING_PASS'
