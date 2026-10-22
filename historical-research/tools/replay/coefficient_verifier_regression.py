#!/usr/bin/env python3
"""Exact regression for the legacy point-order verifier defect.
Default: portable finite arithmetic; --compile: also exercise both C verifiers on macOS.
All generated files stay in a temporary directory. No corpus is needed.
"""
from pathlib import Path
import math,struct,subprocess,sys,tempfile
R=Path(__file__).resolve().parents[2]
p=4099; a2=-22735; a4=106272484
c4=(4*a2)**2-48*a4;c6=-(4*a2)**3+72*(4*a2)*a4
A=-27*c4%p;B=-54*c6%p
chi=lambda z: 0 if z%p==0 else (1 if pow(z,(p-1)//2,p)==1 else -1)
true_a=-sum(chi(x*x*x+a2*x*x+a4*x) for x in range(p))
assert true_a==86 and all(p%q for q in range(2,math.isqrt(p)+1))
def add(P,Q,C):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v)%p==0:return None
 m=((3*x*x+C)*pow(2*y,-1,p) if x==u else (v-y)*pow(u-x,-1,p))%p
 z=(m*m-x-u)%p;return z,(m*(x-z)-y)%p
def mul(P,n,C):
 Q=None
 while n:
  if n&1:Q=add(Q,P,C)
  P=add(P,P,C);n//=2
 return Q
def fac(n):
 out=[];q=2
 while q*q<=n:
  e=0
  while n%q==0:e+=1;n//=q
  if e:out.append((q,e))
  q+=1
 if n>1:out.append((n,1))
 return out
def setup(x,a):
 d=(x**3+A*x+B)%p;assert d
 return (d*x%p,d*d%p),A*d*d%p,p+1-chi(d)*a
bad=[(2,1)]*6+[(3,1)]*2
P,C,h=setup(59,68);assert h==4032
assert mul(P,6,C) is None and all(mul(P,k,C) is not None for k in (1,2,3))
D=math.prod(q**e for q,e in bad);s=math.isqrt(4*p);lo=p+1-s;hi=p+1+s
assert D==576 and D>2*s and hi//D-(lo-1)//D==1 and h%D==0 and mul(P,h,C) is None
for q,e in bad:
 v=next(v for z,v in fac(h) if z==q)
 assert mul(P,h//q**(v-e+1),C) is not None
print('PASS: true a_4099=86; false a_4099=68 satisfies every old witness test with duplicate factors.')
# Find a genuine distinct-factor witness directly from the exact point count.
for x in range(256):
 if (x**3+A*x+B)%p==0:continue
 P,C,h=setup(x,true_a);order=h
 for q,e in fac(h):
  for _ in range(e):
   if order%q==0 and mul(P,order//q,C) is None:order//=q
   else:break
 if order>2*s and hi//order-(lo-1)//order==1:
  good=(x,fac(order));break
else:raise AssertionError('no small genuine witness')
assert len({q for q,e in good[1]})==len(good[1])
print('PASS: independent genuine control witness found.')
if '--compile' in sys.argv:
 if sys.platform!='darwin':raise SystemExit('--compile requires macOS CommonCrypto; portable math checks passed.')
 with tempfile.TemporaryDirectory() as td:
  t=Path(td);wd=t/'wit';wd.mkdir();od=t/'out';od.mkdir()
  sources=[R/'evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/verifier/wverify.c',R/'review/repairs/wverify_distinct.c']
  for i,src in enumerate(sources):
   exe=t/f'v{i}'
   subprocess.run(['clang','-O2','-Wno-deprecated-declarations',str(src),'-o',str(exe)],check=True,capture_output=True,timeout=30)
   for name,a,x,fs in [('malicious',68,59,bad),('genuine',true_a,*good)]:
    data=struct.pack('<QQQ',0,4100,1)+struct.pack('<QiBB',p,a,x,len(fs))+b''.join(struct.pack('<QB',q,e) for q,e in fs)
    (wd/'wit_000000.bin').write_bytes(data)
    r=subprocess.run([str(exe),'wit','0',str(a2),'0',str(a4),'0','4099','4096','4100',str(wd),str(od),'0','1'],capture_output=True,text=True,timeout=30)
    if name=='malicious' and i==1:
     assert r.returncode==3 and 'duplicate prime factor' in r.stderr
    else:
     assert r.returncode==0,(i,name,r.stderr)
     assert struct.unpack('<i',(od/'ap_000000.bin').read_bytes()[-4:])[0]==a
    print(f'PASS: {src.name} {name}: exit {r.returncode}')
print('ALL PASS')
