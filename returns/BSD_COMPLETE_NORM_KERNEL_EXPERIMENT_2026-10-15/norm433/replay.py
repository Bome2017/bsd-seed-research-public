from pathlib import Path
import tempfile,subprocess,shutil,json,hashlib,re,os
R=Path(__file__).resolve().parent
GP=os.environ.get('PARI_GP','/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
scripts=['construct.gp','certify_rank.gp','local_certify.gp','verify_exact.gp']
products=['norm_data.gp','dual_nf.gp','candidate_cube_roots.gp','norm_map.json','norm_polynomials.json','norm_residue_rows.jsonl','complete_certificate.json','local_precision.json']
results=[]
with tempfile.TemporaryDirectory(prefix='433_norm_replay_') as td:
 T=Path(td);shutil.copytree(R/'inputs',T/'inputs');shutil.copy2(R/'SOURCE_BINDINGS.json',T/'SOURCE_BINDINGS.json')
 for name in scripts:
  shutil.copy2(R/name,T/name)
  with (T/name).open() as f:
   p=subprocess.run([GP,'-D','parisizemax=1000000000','-q','-f'],stdin=f,cwd=T,capture_output=True,text=True,timeout=100)
  assert p.returncode==0 and not re.search(r'\*\*\*|error|Error|alarm',p.stderr),(name,p.stdout,p.stderr)
  results.append({'script':name,'returncode':p.returncode,'stderr':p.stderr,'final_line':p.stdout.strip().splitlines()[-1]})
 for name in products:assert (R/name).read_bytes()==(T/name).read_bytes(),name
 for name in ['independent_check.py','local_witness_check.py']:
  shutil.copy2(R/name,T/name);p=subprocess.run(['python3',name],cwd=T,capture_output=True,text=True,timeout=20);assert p.returncode==0,(name,p.stderr)
 out={'status':'CLEAN_REPLAY_PASS','products_byte_identical':products,'steps':results,'independent_check':json.loads((T/'INDEPENDENT_CHECK.json').read_text()),'local_hensel':json.loads((T/'local_witness_check.json').read_text())}
(R/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
