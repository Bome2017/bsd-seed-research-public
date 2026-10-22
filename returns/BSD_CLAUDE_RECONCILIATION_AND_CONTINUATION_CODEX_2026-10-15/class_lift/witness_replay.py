from pathlib import Path
import subprocess,json,re,time
R=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14');O=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
template=(O/'check_witness_template.gp').read_text();out=[]
for label in ['1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh']:
 s=template.replace('LABEL',label);(O/label/'witness_check.gp').write_text(s)
 t=time.monotonic();r=subprocess.run([GP,'-s','100000000','-q','-f'],input=s.encode(),cwd=R,capture_output=True,timeout=40)
 (O/label/'witness_check.out').write_bytes(r.stdout);(O/label/'witness_check.err').write_bytes(r.stderr)
 bad=[l for l in r.stderr.decode().splitlines() if l.strip() and not re.match(r'\s*\*\*\*\s+Warning: (new maximum stack size =|increasing stack size to)',l)]
 out.append({'curve':label,'rc':r.returncode,'pass':r.returncode==0 and not bad and 'WITNESS_REPLAY_PASS' in r.stdout.decode(),'unexpected_stderr':bad,'seconds':round(time.monotonic()-t,3)})
(O/'witness_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
