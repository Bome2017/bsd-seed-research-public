#!/usr/bin/env python3
"""Independent division-polynomial recurrence and selected exact resultants."""
from pathlib import Path
import json,hashlib
import sympy as s
x=s.Symbol('x');ROOT=Path(__file__).resolve().parent;DATA=ROOT.parent/'explicit_seed_functions'
models={'seed':(0,-22735,0,106272484,0),'389a1':(0,1,1,-2,0),'37a1':(0,0,1,-1,0)}
checks=[];files={}
for name,(a1,a2,a3,a4,a6) in models.items():
 b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6;b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
 C=s.Poly(4*x**3+b2*x**2+2*b4*x+b6,x)
 z=s.Poly(0,x);one=s.Poly(1,x)
 def add(a,b):return(a[0]+b[0],a[1]+b[1])
 def neg(a):return(-a[0],-a[1])
 def mul(a,b):return(a[0]*b[0]+a[1]*b[1]*C,a[0]*b[1]+a[1]*b[0])
 def cube(a):return mul(a,mul(a,a))
 memo={0:(z,z),1:(one,z),2:(z,one),3:(s.Poly(3*x**4+b2*x**3+3*b4*x*x+3*b6*x+b8,x),z),4:(z,s.Poly(2*x**6+b2*x**5+5*b4*x**4+10*b6*x**3+10*b8*x*x+(b2*b8-b4*b6)*x+b4*b8-b6*b6,x))}
 def psi(n):
  if n in memo:return memo[n]
  m=n//2
  if n%2:r=add(mul(psi(m+2),cube(psi(m))),neg(mul(psi(m-1),cube(psi(m+1)))))
  else:
   tmp=mul(psi(m),add(mul(psi(m+2),mul(psi(m-1),psi(m-1))),neg(mul(psi(m-2),mul(psi(m+1),psi(m+1))))))
   q,rem=s.div(tmp[0],C);assert rem.is_zero;r=(tmp[1],q)
  memo[n]=r;return r
 for p in [5,7,11]:
  path=DATA/f'direct_{name}_{p}.json';d=json.loads(path.read_text());files[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
  D,W=psi(p);assert W.is_zero and D.degree()==(p*p-1)//2 and D.LC()==p
  wanted={(0,0),(1,1),(-2,1),(2,-1)}
  for m,b,N,vv,free in d['candidates']:
   if (m,b) not in wanted:continue
   Q=s.Poly((m*x+b)**2,x)-C
   nr=int(s.resultant(D,Q));assert nr==N,(name,p,m,b,nr,N)
   r=abs(N)
   for q,v in zip(d['S'],vv):
    assert r%q**v==0;r//=q**v;assert r%q!=0
   assert r==free
   checks.append({'curve':name,'p':p,'m':m,'b':b,'exact_resultant_agrees':True,'Sfree':str(free)})
out={'status':'PASS','method':'independent division-polynomial recurrence plus SymPy exact resultant','rows_checked':len(checks),'checks':checks,'bindings':files,'interpretation':'support screen only; not affine norm rank or source completeness'}
(ROOT/'ROOT_RESULTANT_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','rows_checked':len(checks)}))
