"""Independent literal arithmetic for all freshly generated433 source columns."""
from pathlib import Path
from fractions import Fraction
from math import lcm
import json,hashlib
R=Path(__file__).resolve().parent
D=json.loads((R/'433_scan/source_elements.json').read_text())
S=json.loads((R/'inputs/433a1_signatures.json').read_text())['fresh_primes']
field=[int(x) for x in D['field']]
def evaluate(coeffs,x,mod):
 v=0
 for a in reversed(coeffs):v=(v*x+a)%mod
 return v
def valuation(a,q):
 if a==0:raise ValueError('insufficient precision')
 v=0
 while a%q==0:a//=q;v+=1
 return v

def leading_unit(coeffs,root,q,precision=8):
 c=[Fraction(s)for s in coeffs];den=lcm(*(a.denominator for a in c));ints=[int(a*den)for a in c]
 x=root
 for j in range(1,precision):
  modulus=q**(j+1);fx=evaluate(field,x,modulus);derivative=evaluate([i*field[i]for i in range(1,len(field))],x,q)
  assert fx%(q**j)==0 and derivative
  x+=( (-fx//(q**j))*pow(derivative,-1,q)%q)*(q**j)
 assert evaluate(field,x,q**precision)==0
 value=evaluate(ints,x,q**precision);vn=valuation(value,q);vd=valuation(den,q);v=vn-vd
 assert vn<precision and v%3==0
 unit=(value//q**vn)*pow(den//q**vd,-1,q)%q
 return v,unit

def mod_fraction_poly(coeffs,x,q):
 vals=[]
 for s in coeffs:
  a=Fraction(s);vals.append(a.numerator*pow(a.denominator,-1,q)%q)
 return evaluate(vals,x,q)

def add(P,Q,a,q):
 if P is None:return Q
 if Q is None:return P
 a1,a2,a3,a4,a6=a;x1,y1=P;x2,y2=Q
 if x1==x2 and (y1+y2+a1*x1+a3)%q==0:return None
 if x1!=x2:
  inv=pow((x2-x1)%q,-1,q);lam=(y2-y1)*inv%q;nu=(y1*x2-y2*x1)*inv%q
 else:
  inv=pow((2*y1+a1*x1+a3)%q,-1,q);lam=(3*x1*x1+2*a2*x1+a4-a1*y1)*inv%q;nu=(-x1**3+a4*x1+2*a6-a3*y1)*inv%q
 x3=(lam*lam+a1*lam-a2-x1-x2)%q;y3=(-(lam+a1)*x3-nu-a3)%q
 return x3,y3
out=[];count=0
for b in S:
 q=b['prime'];omega=b['cubic_root'];assert pow(omega,3,q)==1 and omega!=1;chars={1:0,omega:1,omega*omega%q:2};computed=[];exceptional=[]
 for i,root in enumerate(b['roots']):
  assert evaluate(field,root,q)==0
  P=tuple(mod_fraction_poly(c,root,q)for c in D['T']);assert P==tuple(b['torsion_points'][i]);a=D['ainvariants'];x,y=P
  assert (y*y+a[0]*x*y+a[2]*y-x**3-a[1]*x*x-a[3]*x-a[4])%q==0
  assert add(add(P,P,a,q),P,a,q)is None
  row=[]
  for j,c in enumerate(D['source']):
   v,u=leading_unit(c,root,q);row.append(chars[pow(u,(q-1)//3,q)]);count+=1
   if v:exceptional.append({'root_index':i,'source_column':j,'valuation':v,'leading_unit':u})
  computed.append(row)
 assert computed==b['source_residue_rows']
 out.append({'prime':q,'all_source_rows_equal':True,'literal_evaluations':8*len(D['source']),'nonunit_literal_representatives':exceptional})
result={'status':'ALL_FRESH_433_SOURCE_ROWS_REPLAYED','source_columns':len(D['source']),'literal_evaluations':count,'blocks':out,'input_bindings':[{ 'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in [R/'433_scan/source_elements.json',R/'inputs/433a1_signatures.json']],'scope':'Exact polynomial and Hensel-leading-unit replay of every full-source character, field root and torsion point; no producer libraries or known-class columns. Source completeness and source coordinate binding retained separately.'}
(R/'FRESH_433_LITERAL_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
