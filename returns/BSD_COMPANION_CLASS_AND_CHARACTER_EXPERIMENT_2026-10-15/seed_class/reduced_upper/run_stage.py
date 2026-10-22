import os,pathlib,subprocess,sys,time,json,hashlib,re
r=pathlib.Path(__file__).resolve().parent
stage=sys.argv[1]
assert stage in ['reduce','construct','certify']
seconds={'reduce':40,'construct':130,'certify':190}[stage]
exe=os.environ.get('PARI_GP','/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
start=time.monotonic()
with (r/(stage+'.out')).open('w') as out,(r/(stage+'.err')).open('w') as err:
 p=subprocess.Popen([exe,'-q','-f','-s','64000000'],stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,cwd=r)
 try:p.communicate('default(parisizemax,1000000000);\nread("'+stage+'.gp");\nquit;\n',timeout=seconds);timedout=False
 except subprocess.TimeoutExpired:p.kill();p.communicate();timedout=True
stdout=(r/(stage+'.out')).read_text();stderr=(r/(stage+'.err')).read_text()
markers={'reduce':'REDUCTION_COMPLETE','construct':'BNF_UPPER_CONSTRUCTION_COMPLETE_PROVISIONAL','certify':'CLASS_UPPER_CERTIFICATION_COMPLETE'}
errors=[line for line in stderr.splitlines() if line.strip() and 'Warning: new maximum stack size' not in line and not re.fullmatch(r'\s*\*\*\* (polredbest|nfinit|bnfinit|bnfcertify): Warning: increasing stack size to [0-9]+\.',line)]
ok=not timedout and p.returncode==0 and not errors and markers[stage] in stdout
receipt={'stage':stage,'status':'PASS' if ok else 'TIMEOUT' if timedout else 'FAILED','elapsed_seconds':time.monotonic()-start,'returncode':p.returncode,'outer_seconds':seconds,'stdout_sha256':hashlib.sha256(stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(stderr.encode()).hexdigest(),'errors':errors}
(r/(stage+'_receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));print(stdout)
if not ok:sys.exit(1)
