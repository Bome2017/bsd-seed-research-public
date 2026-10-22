"""Bounded exact replay; producers need Sage, verifiers use standard Python."""
import argparse,subprocess,pathlib,time,json,hashlib,sys,resource
ap=argparse.ArgumentParser();ap.add_argument('--sage-python',required=True);args=ap.parse_args()
base=pathlib.Path(__file__).parent.resolve()
outputs=['principal_probe.json','leak_repair.json','line_source_probe.json','verify_principal.json','verify_line_source.json']
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={x:digest(base/x) for x in outputs if (base/x).exists()}
jobs=[('principal_probe.py',args.sage_python),('leak_repair.py',args.sage_python),('line_source_probe.py',args.sage_python),('verify_line_source.py',sys.executable)]
results=[]
for script,python in jobs:
 start=time.monotonic();old=resource.getrusage(resource.RUSAGE_CHILDREN);run=subprocess.run([python,str(base/script)],cwd=base,capture_output=True,text=True,timeout=60);new=resource.getrusage(resource.RUSAGE_CHILDREN)
 (base/(script+'.replay.stdout')).write_text(run.stdout);(base/(script+'.replay.stderr')).write_text(run.stderr)
 record={'script':script,'exit':run.returncode,'elapsed_seconds':time.monotonic()-start,'child_cpu_seconds':new.ru_utime+new.ru_stime-old.ru_utime-old.ru_stime,'stderr_empty':not run.stderr}
 results.append(record)
 if run.returncode or run.stderr:raise RuntimeError(record)
after={x:digest(base/x) for x in outputs}
assert all(after[x]==v for x,v in before.items())
receipt={'status':'PASS','runs':results,'saved_json_reproduced_byte_for_byte':before==after,'outputs':after,'sage_python':args.sage_python,'verifier_python':sys.executable}
(base/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
