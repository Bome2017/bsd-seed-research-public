#!/usr/bin/env python3
"""Clean-directory replay; GP write appends, so never replay onto old products."""
from pathlib import Path
import tempfile,subprocess,time,json,hashlib,shutil,os
R=Path(__file__).resolve().parent
GP=os.environ.get('PARI_GP','/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
summary=[]
for label in ['mirror389','1664n1']:
 src=R/'authentication'/label; hashes=[]
 for run in range(2):
  with tempfile.TemporaryDirectory(prefix='bsd_class_map_') as td:
   d=Path(td)
   for n in ['bnf.bin','data.gp']:shutil.copy2(src/n,d/n)
   st=time.monotonic();p=subprocess.run([GP,'-q','-f','-s','256000000'],input=(R/'authenticate.gp').read_text(),text=True,cwd=d,capture_output=True,timeout=65)
   (src/f'clean_replay_{run}.out').write_text(p.stdout);(src/f'clean_replay_{run}.err').write_text(p.stderr)
   assert p.returncode==0 and not p.stderr.strip() and 'AUTHENTICATION_COMPLETE' in p.stdout,(label,p.stderr)
   cert=d/'ideal_map_certificate.gp';assert cert.exists();h=hashlib.sha256(cert.read_bytes()).hexdigest();hashes.append(h)
   q=subprocess.run([GP,'-q','-f','-s','128000000'],input=(R/'summarize.gp').read_text(),text=True,cwd=d,capture_output=True,timeout=5);assert q.returncode==0 and not q.stderr.strip();obj=json.loads(q.stdout)
   if run==1:
    shutil.copy2(cert,src/cert.name);shutil.copy2(d/'certified_target_bnf.bin',src/'certified_target_bnf.bin');(src/'RESULT.json').write_text(json.dumps(obj,indent=2)+'\n')
   summary.append({'label':label,'run':run,'seconds':round(time.monotonic()-st,3),'certificate_sha256':h,'arithmetic_accepted':True})
 assert hashes[0]==hashes[1],(label,hashes)
 print(label,'CLEAN_TWO_REPLAYS_IDENTICAL',hashes[0],flush=True)
(R/'REPLAY.json').write_text(json.dumps({'status':'PASS','method':'two independent clean temporary directories per control','results':summary},indent=2)+'\n')
