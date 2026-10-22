#!/usr/bin/env python3
"""Scoped replay of saved data. No PARI/Sage arithmetic is regenerated."""
import argparse, hashlib, itertools, json, math, re
from pathlib import Path
from fractions import Fraction
parser=argparse.ArgumentParser()
parser.add_argument('--source',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
a=parser.parse_args(); src=a.source.resolve(); hashes={}
def read(rel):
 p=src/rel; b=p.read_bytes(); hashes[rel]=hashlib.sha256(b).hexdigest(); return b.decode()
def mod(v,p):
 v=Fraction(v); return v.numerator*pow(v.denominator,-1,p)%p
# Verify manifest and prediction bindings, preserving all failures as data.
manifest=read('MANIFEST.sha256'); checks=[]
for line in manifest.splitlines():
 h,rel=line.split(maxsplit=1); rel=rel.removeprefix('./'); p=src/rel
 checks.append({'path':rel,'exists':p.is_file(),'match':p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==h})
seals=[]
for d,n in [('proxy','PREDICTIONS_SEALED.md'),('padic_bsd','PREDICTION.md')]:
 actual=hashlib.sha256(read(f'{d}/{n}').encode()).hexdigest(); expected=read(f'{d}/{n}.sha256').split()[0]
 seals.append({'path':f'{d}/{n}','sha256':actual,'match':actual==expected})
# Parse the printed p-adic results, not a regenerated numerical computation.
pat=re.compile(r'PBSD (\S+) p=(\d+) n=(\d+) r=(\d+) ratio=1 \+ O\((\d+)\^(\d+)\) vReg=(\d+)')
pr=[]
for name in ['padic_bsd/padic_bsd.out','padic_bsd/padic_bsd_rest.out']:
 for ln,line in enumerate(read(name).splitlines(),1):
  if line.startswith('PBSD '):
   m=pat.fullmatch(line.split(' ms=')[0]); assert m,line
   cv,p,n,r,base,k,reg=m.groups(); assert p==base
   pr.append({'curve':cv,'p':int(p),'input_precision':int(n),'reported_rank':int(r),'ratio_residue':1,'ratio_precision':int(k),'regulator_valuation':int(reg),'source':name,'line':ln})
assert len({(r['curve'],r['p'])for r in pr})==len(pr)
# Read exact local determinant entries and recompute determinants.
dets={}; local=[]
for ln,line in enumerate(read('proxy/global_side.out').splitlines(),1):
 if not line.startswith('{'):continue
 r=json.loads(line); p=r['p']; x=(r['dP']*r['rhoQ']-r['dQ']*r['rhoP'])%p
 assert x==r['det']; dets[(r['curve'],p,r['l'])]=x; local.append(r)
for line in read('proxy/p13_rows.txt').splitlines():
 r=json.loads(line); u,v=r['dP,dQ']; x,y=r['rho']; det=(u*y-v*x)%13
 assert det==r['det']; dets[('1001c1',13,r['l'])]=det
# Only final RESULT records admitted; interrupted attempts are not extra observations.
rows={}; attempts=[]
for pth in sorted((src/'proxy').glob('*.out')):
 text=read(str(pth.relative_to(src)))
 for ln,line in enumerate(text.splitlines(),1):
  if not line.startswith('RESULT '):continue
  r=json.loads(line[7:]); key=(r['curve'],r['p'],r['l']); assert key not in rows,key
  r['source']=str(pth.relative_to(src)); r['line']=ln;r['determinant']=dets[key]
  r['zero_pattern_matches']=all((f['D_l']%r['p']==0)==(r['determinant']==0)for f in r['fields'])
  assert all(f['S0']==0 for f in r['fields']); rows[key]=r
# Exact modular ratios of saved, numerically recognized twist rational candidates.
vals={}
for line in read('proxy/twist_values.txt').splitlines():
 m=re.match(r'TWV (\S+) D=(-?\d+) L=\S+ r=(\S+) s=(\S+) ',line)
 if m: vals[m[1],int(m[2])]=(Fraction(m[3]),Fraction(m[4]))
pairs=[]
for key,r in sorted(rows.items()):
 cv,p,ell=key
 for f,g in itertools.combinations(sorted(r['fields'],key=lambda f:f['D']),2):
  if f['D_l']%p==0 or g['D_l']%p==0:continue
  obs=mod(Fraction(f['D_l'],g['D_l'])**2*Fraction(f['D'],g['D']),p)
  r1,s1=vals[cv,f['D']];r2,s2=vals[cv,g['D']]
  cand={'constant':1,'twist_real_period':mod(r1/r2,p),'gross_period':mod(s1/s2,p)}
  pairs.append({'curve':cv,'p':p,'ell':ell,'fields':[f['D'],g['D']],'observed_square_ratio':obs,'candidates':cand,'matches':{k:v==obs for k,v in cand.items()}})
# A mathematical gauge countercontrol: with arbitrary nonzero u at each source,
# every proposed nonzero scalar can fit an individual nonzero D/det.
gauge=[]
for r in rows.values():
 p=r['p']; det=r['determinant']
 if not det:continue
 for f in r['fields']:
  solutions={str(c):f['D_l']*pow(c*det,-1,p)%p for c in range(1,p)}
  assert all(u and (u*int(c)*det-f['D_l'])%p==0 for c,u in solutions.items())
  gauge.append({'curve':r['curve'],'p':p,'ell':r['l'],'field':f['D'],'all_nonzero_scalar_candidates_fit_by_source_unit':True})
# Concrete CM-edge arithmetic; this does not evaluate the modular parametrization.
A,B,C=3275,455,19; N=655; disc=B*B-4*A*C
content=math.gcd(math.gcd(A//N,B),C*N)
quot=[A//N//content,B//content,C*N//content]
assert disc==-67*25**2 and content==5 and quot==[1,91,2489]
assert quot[1]**2-4*quot[0]*quot[2]==-67*5**2
out={'scope':'saved-output exact arithmetic replay; no class-set, modular-symbol, p-adic, or L-value regeneration','manifest':{'entries':len(checks),'all_match':all(x['match']for x in checks),'failures':[x for x in checks if not x['match']]},'prediction_seals':seals,'padic':{'rows':len(pr),'curves':len({r['curve']for r in pr}),'precision_range':[min(r['ratio_precision']for r in pr),max(r['ratio_precision']for r in pr)],'data':pr},'proxy':{'rows':len(rows),'field_computations':sum(len(r['fields'])for r in rows.values()),'all_patterns_match':all(r['zero_pattern_matches']for r in rows.values()),'data':list(rows.values())},'crossfield':{'pairs':len(pairs),'tally':{k:sum(r['matches'][k]for r in pairs)for k in ['constant','twist_real_period','gross_period']},'data':pairs,'twist_input_grade':'rational candidates obtained by bestappr of floating L-values; not certified exact here'},'gauge_countercontrol':gauge,'cm_edge':{'source_quadratic_form':[A,B,C],'source_discriminant':disc,'quotient_primitive_form':quot,'quotient_discriminant':-67*5**2,'interpretation':'conductor25 to conductor5 under tau -> 655*tau; 131 horizontal, 5 ascending; not yet matched to saved Gross orbit'},'source_hashes':hashes}
a.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['scope','manifest','prediction_seals']}))
print(json.dumps({'padic_rows':len(pr),'proxy_rows':len(rows),'field_computations':out['proxy']['field_computations'],'crossfield_tally':out['crossfield']['tally'],'cm_edge':out['cm_edge']}))
