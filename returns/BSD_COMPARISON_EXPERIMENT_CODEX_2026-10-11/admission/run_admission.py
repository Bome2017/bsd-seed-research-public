#!/usr/bin/env python3
"""Run exact GP admission and independently check saved coefficient comparisons."""
from pathlib import Path
import hashlib, json, gzip, subprocess, time, math
ROOT=Path(__file__).resolve().parent
GP=Path('/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
MODELS=[[1,1,1,3,12],[1,1,1,-1669982047,-25795561267816],[1,1,1,1878418,-485198548]]
BOUNDS=[118272,80256,118272]
source=Path('/Users/bsm/BSD_EXACT_BD_CONSTANT_2026-10-07/checks/rank2_partner_test.gp')
raw=source.read_text().split(';')[0][4:]
rows=[r for r in json.loads(raw) if r[0]=='2541c1' and r[4] in ('287133c1','424347b1')]
assert len(rows)==2 and rows[0][1]==MODELS[0]
assert {tuple(r[5]) for r in rows}=={tuple(m) for m in MODELS[1:]}
program=ROOT.joinpath('admit.gp').read_text().replace('quit\n','')
program+='\nprint("BASE_RANK ",ellrank(E,0));\n'
program+='print("SATURATED_TO_7 ",ellsaturation(E,[[0,3],[7,17]],7));\n'
program+='Et=ellinit(elltwist(E,-19));print("TWIST ",[vector(5,i,Et[i]),ellglobalred(Et)[1],ellrank(Et,0)]);\n'
program+='print("PARTNER_RANK_113 ",ellrank(E1,0));print("PARTNER_RANK_167 ",ellrank(E2,0));\n'
program+='print("LOCAL3 ",elllocalred(E,3));\n'
for i,b in enumerate(BOUNDS):
 program+=f'write("{ROOT}/coeff_{i}.json",ellan([{",".join(["E","E1","E2"])}][{i+1}],{b}));\n'
program+='quit\n'
(ROOT/'executed.gp').write_text(program)
t0=time.monotonic()
proc=subprocess.run([str(GP),'-fq'],input=program,text=True,capture_output=True,timeout=120)
(ROOT/'executed.stdout').write_text(proc.stdout)
(ROOT/'executed.stderr').write_text(proc.stderr)
assert proc.returncode==0 and '***' not in proc.stdout
assert all('***' not in line or 'Warning: new maximum stack' in line for line in proc.stderr.splitlines())
assert 'STURM [113, 287133, 481536, 80256, 0, []]' in proc.stdout
assert 'STURM [167, 424347, 709632, 118272, 0, []]' in proc.stdout
coeff=[]; receipts=[]
for i in range(3):
 f=ROOT/f'coeff_{i}.json'; data=f.read_bytes(); a=json.loads(data)
 assert len(a)==BOUNDS[i]
 coeff.append(a)
 zipped=ROOT/f'coeff_{i}.json.gz'
 with gzip.GzipFile(filename='',mode='wb',fileobj=zipped.open('wb'),mtime=0) as z: z.write(data)
 receipts.append({'model':MODELS[i],'count':len(a),'uncompressed_sha256':hashlib.sha256(data).hexdigest(),'gzip_sha256':hashlib.sha256(zipped.read_bytes()).hexdigest()})
 f.unlink()
checks=[]
for i,ell in enumerate((113,167),start=1):
 B=BOUNDS[i]; N=2541*ell
 index=math.prod((q+1)*q**(e-1) for q,e in [(3,1),(7,1),(11,2),(ell,1)])
 assert index//6==B
 diffs=[coeff[0][n-1]-(ell*coeff[0][n//ell-1] if n%ell==0 else 0)-coeff[i][n-1] for n in range(1,B+1)]
 assert all(d%5==0 for d in diffs)
 # Deliberately wrong oldform and unraised raw form fail.
 bad_raw=next(n for n in range(1,B+1) if (coeff[0][n-1]-coeff[i][n-1])%5)
 bad_wrong=next(n for n in range(1,B+1) if (coeff[0][n-1]-(coeff[0][n//ell-1] if n%ell==0 else 0)-coeff[i][n-1])%5)
 mod25=next(n for n in range(1,B+1) if diffs[n-1]%25)
 checks.append({'ell':ell,'level':N,'index':index,'Sturm_bound':B,'mod5_mismatches':0,'wrong_raw_first_failure':bad_raw,'wrong_stabilization_first_failure':bad_wrong,'same_integer_stabilization_mod25_first_failure':mod25,'difference_at_mod25_failure':diffs[mod25-1]})
# Independent finite-field counts from the printed equation, no PARI arithmetic.
def prime(n): return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def ap_count(model,q):
 a1,a2,a3,a4,a6=model
 if q==2:
  return q+1-(1+sum((y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%q==0 for x in range(q) for y in range(q)))
 # y quadratic discriminant; Euler criterion returns0,1,-1.
 s=0
 for x in range(q):
  D=((a1*x+a3)**2+4*(x**3+a2*x*x+a4*x+a6))%q
  r=pow(D,(q-1)//2,q)
  s += 0 if r==0 else (1 if r==1 else -1)
 return -s
point_checks=[]
for i,model in enumerate(MODELS):
 for q in range(2,500):
  if prime(q) and (2541*[1,113,167][i])%q:
   v=ap_count(model,q); assert v==coeff[i][q-1]
   point_checks.append([i,q,v])
assert coeff[0][12]==-7 and coeff[1][12]==coeff[2][12]==-2
# Binary form reduced enumeration gives class number1 for -19 independently.
reduced=[]
for a in range(1,math.isqrt(19//3)+2):
 for b in range(-a,a+1):
  if (b*b+19)%(4*a): continue
  c=(b*b+19)//(4*a)
  if a>c or math.gcd(math.gcd(a,abs(b)),c)!=1:continue
  if (abs(b)==a or a==c) and b<0:continue
  reduced.append([a,b,c])
assert reduced==[[1,1,5]]
cm={str(q):(-1 if pow((-19)%q,(q-1)//2,q)==q-1 else 1) for q in [3,5,7,11,113,167]}
assert cm=={'3':-1,'5':1,'7':1,'11':1,'113':-1,'167':-1}
# All possible independent fixed lines of a conjugate transvection generateSL2.
def mul(A,B): return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%5 for i in range(2) for j in range(2))
def closure(gs):
 seen={(1,0,0,1)}; todo=list(seen)
 while todo:
  A=todo.pop()
  for g in gs:
   C=mul(A,g)
   if C not in seen: seen.add(C);todo.append(C)
 return seen
sizes=[]
for a in range(5):
 for b in range(5):
  for c in range(1,5):
   for d in range(5):
    U=(a,b,c,d)
    if (a+d)%5==2 and (a*d-b*c)%5==1:
     sizes.append(len(closure([(1,1,0,1),U])))
assert len(sizes)==20 and set(sizes)=={120}
report={'status':'EXACT_MOD5_STURM_CM_RESIDUAL_ADMISSION_PASSED','models':MODELS,'runtime_seconds':time.monotonic()-t0,'gp_binary_sha256':hashlib.sha256(GP.read_bytes()).hexdigest(),'GP_version':'2.17.3','coefficients':receipts,'sturm_comparisons':checks,'independent_point_count_controls':point_checks,'point_count_control_total':len(point_checks),'CM_discriminant':-19,'CM_splitting_characters':cm,'reduced_forms':reduced,'group_controls':{'independent_transvections':len(sizes),'generated_group_orders':sorted(set(sizes))},'inputs':[{'path':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'selected_rows':rows},{'path':'/Users/bsm/BSD_COMPARISON_DISCOVERY_PROCESS_CODEX_2026-10-11/FIRST_EXPERIMENT.md','sha256':hashlib.sha256(Path('/Users/bsm/BSD_COMPARISON_DISCOVERY_PROCESS_CODEX_2026-10-11/FIRST_EXPERIMENT.md').read_bytes()).hexdigest()}],'limits':['Computer-assisted exact check, not Lean kernel certification.','No explicit E[5] module isomorphism constructed here.','No Sha[5] assumption made or conclusion proved.','Both raised representations are demonstrably nonisomorphic mod25: good-prime q13 trace difference is -5.','No CM divisor/localization or mixed-place comparison evaluated.']}
(ROOT/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','sturm_comparisons','point_count_control_total','CM_splitting_characters','group_controls','runtime_seconds']},indent=2))
