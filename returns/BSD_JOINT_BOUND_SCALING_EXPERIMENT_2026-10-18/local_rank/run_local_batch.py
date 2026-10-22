"""Freeze and evaluate a supplied actual compact-unit source; does no unit search."""
import hashlib,json,subprocess,sys,time
from pathlib import Path

R=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
src=Path(sys.argv[1]).resolve()
label=sys.argv[2]
assert label.replace('_','').isalnum()
snapshot=R/f'compact_units_{label}.json'
snapshot.write_bytes(src.read_bytes())
data=json.loads(snapshot.read_text());n=len(data[5]);m=len(data[5][0])
binding={'source':str(src),'snapshot':snapshot.name,'sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),'base_elements':len(data[4]),'factor_columns':n,'unit_columns':m}
(R/f'{label}_BINDING.json').write_text(json.dumps(binding,indent=2)+'\n')
receipts=[]
for precision in [8,9]:
    name=f'{label}_formal_{precision}'
    script=(R/'formal_branch.gp').read_text().replace(str(R/'compact_units_batch1.json'),str(snapshot)).replace('idealpow(NF,P,8)',f'idealpow(NF,P,{precision})').replace('"formal_branch.json"',f'"{name}.json"')
    (R/f'{name}.gp').write_text(script)
    start=time.monotonic()
    proc=subprocess.run([GP,'-q','-f','-s','128000000','-D','parisizemax=1000000000',name+'.gp'],cwd=R,capture_output=True,text=True,timeout=65)
    (R/f'{name}.out').write_text(proc.stdout);(R/f'{name}.err').write_text(proc.stderr)
    receipt={'name':name,'seconds':time.monotonic()-start,'exit':proc.returncode,'complete_marker':'FORMAL_LOCAL_COMPLETE' in proc.stdout}
    receipts.append(receipt)
    if not receipt['complete_marker'] or proc.stderr:
        raise RuntimeError(receipt,proc.stderr)
    print(proc.stdout.strip())
proc=subprocess.run([sys.executable,str(R/'evaluate_split.py'),str(snapshot),str(R/f'{label}_split_rows.json')],capture_output=True,text=True,timeout=60)
(R/f'{label}_split.out').write_text(proc.stdout);(R/f'{label}_split.err').write_text(proc.stderr)
if proc.returncode:raise RuntimeError(proc.stderr)
print(proc.stdout.strip())
(R/f'{label}_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n')
