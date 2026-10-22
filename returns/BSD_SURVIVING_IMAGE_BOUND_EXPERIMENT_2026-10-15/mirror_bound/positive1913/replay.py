from pathlib import Path
import tempfile,subprocess,shutil,os,json,re
R=Path(__file__).resolve().parent;GP=os.environ.get('PARI_GP','/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp');steps=[]
with tempfile.TemporaryDirectory(prefix='positive_reverse_') as td:
 T=Path(td);shutil.copytree(R/'inputs',T/'inputs')
 for f in ['INPUT_BINDINGS.json','verify_reverse.gp','check_reverse.gp','check_matrices.py']:shutil.copy2(R/f,T/f)
 for f in ['verify_reverse.gp','check_reverse.gp']:
  with (T/f).open() as h:p=subprocess.run([GP,'-s','64000000','-D','parisizemax=1000000000','-q','-f'],stdin=h,cwd=T,capture_output=True,text=True,timeout=70)
  assert p.returncode==0 and not re.search(r'\*\*\*|error|Error|alarm',p.stderr),(f,p.stdout,p.stderr)
  steps.append({'script':f,'exit':p.returncode,'stderr':p.stderr,'stdout':p.stdout})
 for f in ['reverse_certificate.gp','reverse.json']:assert (T/f).read_bytes()==(R/f).read_bytes(),f
 p=subprocess.run(['python3','check_matrices.py'],cwd=T,capture_output=True,text=True);assert p.returncode==0,p.stderr
 out={'status':'LITERAL_POSITIVE_REVERSE_NORM_REPLAY_PASS','byte_identical_products':['reverse_certificate.gp','reverse.json'],'steps':steps,'independent_matrix_check':json.loads((T/'MATRIX_CHECK.json').read_text())}
(R/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
