#!/usr/bin/env python3
"""Independent exact downstream arithmetic, not a replay of interval production.
Uses copied certified symbol tables and freshly evaluated GP point regulators.
Run from any directory; no network, no mutation of retained evidence.
"""
from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib,math,ast
root=Path(__file__).resolve().parents[1]
for b in json.loads((root/'INPUT_BINDINGS.json').read_text()):
 assert hashlib.sha256((root/b['copy']).read_bytes()).hexdigest()==b['sha256']
cfg=json.loads((root/'INPUTS.json').read_text())
def primitive(l):
 return [g for g in range(2,l) if len({pow(g,e,l) for e in range(l-1)})==l-1]
def symbols(path,l):
 ans={}
 for line in path.read_text().splitlines():
  if not line.startswith('XB '):continue
  ts=line.split();a=int(ts[1]);plus=ts[ts.index('plus'):ts.index('minus')];k=plus.index('cand')
  assert plus[k+2:k+6]==['contains','1','unique','1']
  assert a not in ans;ans[a]=F(plus[k+1])
 assert set(ans)==set(range(1,l));assert all(ans[a]==ans[l-a] for a in ans)
 return ans
def reduce(x,p):
 x=F(x);return x.numerator*pow(x.denominator,-1,p)%p
def moment(sym,g,l,p):
 inds={pow(g,e,l):e%p for e in range(l-1)}
 return [sum((math.comb(inds[a],k)*v for a,v in sym.items()),F(0)) for k in range(3)]
def cardinal(curve,p):
 if curve=='seed':f=lambda x:(x**3-22735*x*x+106272484*x)%p;return 1+sum(1 if f(x)==0 else 2 if pow(f(x),(p-1)//2,p)==1 else 0 for x in range(p))
 # (2y+1)^2=1+4(x^3+x^2-2x)
 f=lambda x:(1+4*(x**3+x*x-2*x))%p
 return 1+sum(1 if f(x)==0 else 2 if pow(f(x),(p-1)//2,p)==1 else 0 for x in range(p))
def gprows(file,curve):
 t=(root/file).read_text();assert t.rstrip().endswith('DONE')
 err=(root/str(file).replace('.out','.err')).read_text()
 assert all('Warning: increasing stack size' in line for line in err.splitlines() if line.strip()),err
 ans={}
 for line in t.splitlines():
  m=re.fullmatch(r'ROW p=(\d+) l=(\d+) #E\(F_l\)=(\d+) a_l=(-?\d+) M=(\d+) data=(.*)',line)
  if m:
   p,l,n,a,M=map(int,m.groups()[:5]);d=ast.literal_eval(m[6]);ans[curve,p,l]={'Nell':n,'aell':a,'M':M,'data':d}
 return ans
regs={}
for file,curve in [('checks/tame_replay.out','seed'),('checks/tame_negative.out','seed'),('checks/tame_389.out','389a1')]:regs.update(gprows(file,curve))
out=[]
for row in cfg['tame']:
 curve,p,l=row['curve'],row['p'],row['ell'];path=root/row['paths']['msl.txt'];sym=symbols(path,l);report=json.loads((root/row['paths']['SINGLETON_REPORT.json']).read_text());manifest=json.loads((root/row['paths']['RUN_MANIFEST.json']).read_text())
 h=hashlib.sha256(path.read_bytes()).hexdigest();assert h==report['msl_sha256'];assert h==manifest.get('msl_output_sha256',h)
 reg=regs[curve,p,l];assert cardinal(curve,l)==reg['Nell'];assert l+1-reg['Nell']==reg['aell']
 gs=primitive(l);m=moment(sym,gs[0],l,p);rr=[reduce(v,p) for v in m];assert rr[0]==rr[1]==0
 if report['p']==p:assert m[2]==F(report['c2'])
 expected=288 if curve=='seed' else 8;euler=(reg['aell']-2)%p;R=reg['data'][0][-1]
 assert euler!=0
 gens=[]
 for values in reg['data']:
  g,h1,h2,b,det,Rg=values;c=moment(sym,g,l,p);cr=reduce(c[2],p)
  assert (h1*h2-b*b)%p==det and det*pow(pow(reg['M'],4,p),-1,p)%p==Rg
  assert cr==expected*euler*Rg%p
  gens.append({'g':g,'c2_mod_p':cr,'regulator':Rg,'scalar':cr*pow(euler*Rg,-1,p)%p if Rg else None})
 # Entire primitive-root orbit is checked against the c2 transformation.
 for g in gs:
  u=next(e for e in range(1,l-1) if pow(gs[0],e,l)==g)
  assert reduce(moment(sym,g,l,p)[2],p)==rr[2]*pow(u,-2,p)%p
 denom=euler*R%p;scalar=rr[2]*pow(denom,-1,p)%p if denom else None
 normalized=scalar*pow(32 if curve=='seed' else 8,-1,p)%p if scalar is not None else None
 out.append({'curve':curve,'p':p,'ell':l,'role':row['role'],'raw_sha256':h,'symbols':len(sym),'g':gs[0],'moments_exact':[str(v) for v in m],'moments_mod_p':rr,'aell':reg['aell'],'Euler_mod_p':euler,'regulator_mod_p':R,'scalar':scalar,'arithmetic_normalized_scalar':normalized,'expected_scalar':expected%p,'point_count_at_p':cardinal(curve,p),'ap':p+1-cardinal(curve,p),'primitive_root_checks':len(gs),'two_generators':gens,'selection':'retrospective; not randomly sampled; later seed auxiliary selection used nonzero-regulator prescreen'})
# Independently reconstruct the ordinary p^2 coefficient at its one guaranteed digit.
heighttext=(root/'checks/ordinary_heights.out').read_text();assert heighttext.rstrip().endswith('DONE');assert not (root/'checks/ordinary_heights.err').read_text().strip()
heights={int(p):(int(a),int(v),int(r)) for p,a,v,r in re.findall(r'ROW p=(\d+) ap=(-?\d+) valuation=(-?\d+) residue=(\d+)',heighttext)}
def plain(path):
 return {int(t[0]):F(t[1]) for line in path.read_text().splitlines() if line.strip() and not line.startswith('#') and len(t:=line.split())==3}
ordrows=[]
for row in cfg['ordinary']:
 p=row['p'];sym=plain(root/row['top']);lower=plain(root/row['lower']);assert len(sym)==p*(p-1);assert len(lower)==p-1
 ap,v,r=heights[p];assert ap==p+1-cardinal('seed',p);assert v==0
 moments=[F(0)]*3
 for a,symbol in sym.items():
  assert symbol==sym[p*p-a]
  j=(-(pow(a,p-1,p*p)-1)//p)%p # numerator divisible p (negative integer quotient)
  assert pow(a,p-1,p*p)==(1-p*j)%(p*p)
  for k in range(3):moments[k]+=math.comb(j,k)*symbol
 raw=[reduce(x,p) for x in moments];L=raw[2]*pow(ap,-2,p)*pow(2,-1,p)%p
 # Complete lower correction per Teich orbit: its total coefficient is C(p,3).
 correction=math.comb(p,3)*sum(lower.values(),F(0));assert reduce(correction,p)==0
 assert raw[:2]==[0,0]
 eps=(1-pow(ap,-1,p))**2%p
 Q=L*pow(eps*r,-1,p)*4*pow(16,-1,p)%p
 assert Q==9%p
 ordrows.append({'p':p,'top_denominator':p*p,'raw_quadratic_moment':str(moments[2]),'moments_mod_p':raw,'unit_root_mod_p':ap%p,'L2_full_period_mod_p':L,'height_regulator_U_mod_p':r,'epsilon_mod_p':eps,'torsion_square':4,'tamagawa_product':16,'corrected_quotient_mod_p':Q,'expected_9_mod_p':9%p,'precision':'mod p only for L2; higher regulator digits do not increase numerator precision','height':'fresh GP ellpadicregulator on retained point pair and U=gamma-1, gamma=1+p; not derived from Sha'})
result={'grade':'EXACT_DOWNSTREAM_RECOMPUTATION_WITH_RETAINED_SYMBOL_CERTIFICATION_AND_HEIGHT_CONVENTIONS','tame':out,'ordinary':ordrows,'summary':{'tame_rows':len(out),'ordinary_rows':len(ordrows),'tame_all_defined_ratios_match':True,'tame_zero_detector_rows':[(r['curve'],r['p'],r['ell']) for r in out if r['regulator_mod_p']==0],'positive_excess_row':[r for r in out if r['p']==3],'crossmethod_shared_prime':5,'uniform_theorem_proved':False,'new_primary_vanishing':False}}
(root/'DISTILLATION_DATA.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result['summary'],indent=2))
print('DISTILLATION_REPLAY_PASS')
