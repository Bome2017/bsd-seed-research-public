import os,pathlib,subprocess,sys,time,json,hashlib,re
r=pathlib.Path(__file__).resolve().parent
exe='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
start=time.monotonic()
with (r/'certify.out').open('w') as out,(r/'certify.err').open('w') as err:
 p=subprocess.Popen([exe,'-q','-f','-s','64000000'],stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,cwd=r)
 try:p.communicate('default(parisizemax,1000000000);\nread("certify.gp");\nquit;\n',timeout=100);timedout=False
 except subprocess.TimeoutExpired:p.kill();p.communicate();timedout=True
stdout=(r/'certify.out').read_text();stderr=(r/'certify.err').read_text()
errors=[l for l in stderr.splitlines() if l.strip() and 'Warning: new maximum stack size' not in l and not re.fullmatch(r'\s*\*\*\* (bnfcertify|read): Warning: increasing stack size to [0-9]+\.',l)]
ok=not timedout and p.returncode==0 and not errors and 'SOURCE_QUOTIENT_CERT_COMPLETE' in stdout and 'CLASS_QUOTIENT_CERTIFICATE=1' in stdout
receipt={'stage':'source_quotient_certification','status':'PASS' if ok else 'TIMEOUT' if timedout or 'alarm interrupt' in stderr else 'FAILED','elapsed_seconds':time.monotonic()-start,'returncode':p.returncode,'internal_seconds':90,'outer_seconds':100,'stdout_sha256':hashlib.sha256(stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(stderr.encode()).hexdigest(),'errors':errors}
(r/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));print(stdout)
if not ok:sys.exit(1)
