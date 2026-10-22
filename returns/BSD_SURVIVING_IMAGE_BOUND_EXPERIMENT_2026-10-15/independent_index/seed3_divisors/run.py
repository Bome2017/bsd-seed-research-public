import pathlib,subprocess,json,hashlib,os
r=pathlib.Path(__file__).resolve().parent
exe=os.environ.get('PARI_GP','/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
script='default(parisizemax,1000000000);\n'+'read("produce.gp");\nquit;\n'
x=subprocess.run([exe,'-q','-f','-s','64000000'],input=script,text=True,capture_output=True,cwd=r,timeout=100)
(r/'produce.out').write_text(x.stdout);(r/'produce.err').write_text(x.stderr)
assert x.returncode==0 and 'INDEPENDENT_INDEX_PRODUCER_COMPLETE' in x.stdout,(x.returncode,x.stderr,x.stdout)
assert '***' not in x.stderr or all('new maximum stack size' in ln or not ln.strip() for ln in x.stderr.splitlines()),x.stderr
print(x.stdout)
