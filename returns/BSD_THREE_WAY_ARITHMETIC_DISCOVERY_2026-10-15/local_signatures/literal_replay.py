from pathlib import Path
from fractions import Fraction
import json,importlib.util,math
R=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('f3',R/'f3.py');f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)
def peval(coeff,x,q):
 s=0
 for c in reversed(coeff):
  a=Fraction(c);s=(s*x+a.numerator*pow(a.denominator,-1,q))%q
 return s
def local_eval(coeff,field,r,q):
 N=8;mod=q;rr=r
 fi=[Fraction(c) for c in field];assert all(c.denominator==1 for c in fi);fi=[int(c)for c in fi]
 def ev(a,x,m):
  z=0
  for c in reversed(a):z=(z*x+c)%m
  return z
 der=[i*fi[i]for i in range(1,len(fi))]
 while mod<q**N:
  mod*=q;rr=(rr-ev(fi,rr,mod)*pow(ev(der,rr,mod),-1,mod))%mod
 cc=[Fraction(c) for c in coeff];den=math.lcm(*(c.denominator for c in cc));ii=[int(c*den)for c in cc];num=ev(ii,rr,mod)
 if not num:raise ValueError('insufficient root precision')
 vn=vd=0
 while num%q==0:num//=q;vn+=1
 while den%q==0:den//=q;vd+=1
 return vn-vd,num*pow(den,-1,q)%q
def add(P,Q,a,q):
 if P is None:return Q
 if Q is None:return P
 a1,a2,a3,a4,a6=a;x,y=P;X,Y=Q
 if x==X and (y+Y+a1*x+a3)%q==0:return None
 if x==X:lam=(3*x*x+2*a2*x+a4-a1*y)*pow((2*y+a1*x+a3)%q,-1,q)%q
 else:lam=(Y-y)*pow((X-x)%q,-1,q)%q
 nu=(y-lam*x)%q;xx=(lam*lam+a1*lam-a2-x-X)%q;yy=(-(lam+a1)*xx-nu-a3)%q
 return [xx,yy]
res=[]
for nm in ['1913b1','28042a1','seed3','389a1','mirror389_false']:
 p=R/nm;s=json.loads((p/'SIGNATURES.json').read_text());P=json.loads((p/'actual_polynomials.json').read_text());co=json.loads((p/'coordinates.json').read_text());det={d['prime'] for d in s['summary']['greedy_independent_detectors']};small=[];counts=0
 for b in s['fresh_primes']:
  q=b['prime'];om=b['cubic_root'];assert pow(om,3,q)==1 and om!=1;assert all(peval(P['field'],r,q)==0 for r in b['roots'])
  points=[[peval(c,r,q)for c in P['T']]for r in b['roots']];assert points==b['torsion_points']
  assert all(add(add(t,t,co['ainvariants'],q),t,co['ainvariants'],q)is None for t in points)
  pairs=[[local_eval(c,P['field'],r,q)for c in P['classes']]for r in b['roots']];valuations=[[v for v,u in row]for row in pairs];assert all(v%3==0 for row in valuations for v in row);vals=[[u for v,u in row]for row in pairs];logs=[]
  for row in vals:
   assert all(row);logs.append([[1,om,om*om%q].index(pow(v,(q-1)//3,q))for v in row])
  assert logs==b['known_values'];sig=f.mul(b['annihilator_rows'],logs);assert sig==b['quotient_signatures'];counts+=1
  if q in det:
   ds=[]
   for d in s['summary']['greedy_independent_detectors']:
    if d['prime']!=q:continue
    weights=d['root_weights'];prods=[1]*len(P['classes'])
    for i,w in enumerate(weights):
     for j in range(len(prods)):prods[j]=prods[j]*pow(vals[i][j],w,q)%q
    cs=[[1,om,om*om%q].index(pow(v,(q-1)//3,q))for v in prods];assert cs==d['known_signature'];ds.append(dict(root_weights=weights,product_residues=prods,signature=cs))
   small.append(dict(prime=q,roots=b['roots'],cubic_root=om,actual_leading_units=vals,actual_valuations=valuations,detectors=ds))
 out={'status':'EXACT_FRACTION_LITERAL_REPLAY_PASS','curve':nm,'all_prime_blocks_verified':counts,'primitive_coordinate_scope':'Every residue is directly evaluated from literal actual class polynomials; no source-coordinate matrix used to generate the values.','selected_detectors':small};(p/'LITERAL_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');res.append(out)
(R/'LITERAL_REPLAY.json').write_text(json.dumps(res,indent=2)+'\n')
for r in res:print(r['curve'],r['all_prime_blocks_verified'],[(d['prime'],d['detectors'])for d in r['selected_detectors']])
