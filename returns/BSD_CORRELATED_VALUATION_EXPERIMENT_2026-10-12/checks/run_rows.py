import json, subprocess, time, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
GP=Path('/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
models={'655a1':([0,0,1,-13,18],[[1,2],[3,2]]),'433a1':([1,0,0,0,1],[[0,1],[-1,1]])}
selection=json.loads((ROOT/'outputs/SELECTED.json').read_text())
ledger=[]
for row in selection['exceptional']+selection['controls']:
    c,p=row['curve'],row['p']; a,pts=models[c]
    nn=5
    data=f'label="{c}";p={p};nn={nn};ainvs={a};pts={pts};\n'
    (ROOT/'checks/row_input.gp').write_text(data)
    stem=f'{c}_p{p}_n{nn}'
    (ROOT/'outputs'/f'{stem}.input.gp').write_text(data)
    t=time.monotonic()
    try:
        run=subprocess.run([str(GP),'-q','-f','-D','parisizemax=1500000000','checks/one_row.gp'],cwd=ROOT,capture_output=True,text=True,timeout=45)
        out,err=run.stdout,run.stderr
        status='completed' if run.returncode==0 and 'DONE' in out and all('***' not in line or 'Warning: increasing stack size' in line for line in err.splitlines()) else 'error'
    except subprocess.TimeoutExpired as e:
        out=e.stdout or b'';err=e.stderr or b''
        out=out.decode() if isinstance(out,bytes) else out;err=err.decode() if isinstance(err,bytes) else err
        status='timeout'
    (ROOT/'outputs'/f'{stem}.out').write_text(out)
    (ROOT/'outputs'/f'{stem}.err').write_text(err)
    receipt={'curve':c,'p':p,'moment_precision':nn,'status':status,'elapsed_seconds':time.monotonic()-t,'output_sha256':hashlib.sha256(out.encode()).hexdigest()}
    ledger.append(receipt)
    (ROOT/'outputs/RUN_LEDGER.json').write_text(json.dumps(ledger,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
