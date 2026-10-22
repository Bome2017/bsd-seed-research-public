import json,time
from pathlib import Path
from sage.all import EllipticCurve, ZZ, kronecker, prime_range, pari
root=Path(__file__).resolve().parent
raw=Path('/Users/bsm/BSD_MOCK_PLECTIC_CONSTANT_2026-10-14/tamlog/tamlog_rows.jsonl')
rows=[json.loads(x) for x in raw.read_text().splitlines()]
candidates=[r for r in rows if r['red']=='nonsplit' and r['pK'] and not r['zero']]
Ds=[]
for d in range(-1200,-4):
 m=ZZ(d if d%4==1 else d//4)
 if not ((d%4==1 and ZZ(d).is_squarefree()) or (d%4==0 and m%4 in (2,3) and m.is_squarefree())):continue
 h=int(pari.qfbclassno(d))
 if h<=8:Ds.append(d)
accepted=[]
for r in candidates:
 t0=time.monotonic(); E=EllipticCurve(r['curve']); p=ZZ(r['p']); N=E.conductor()
 if not N.is_squarefree():continue
 if E.local_data(p).tamagawa_number()%p==0 or E.discriminant().valuation(p)%p==0:continue
 bad=N.prime_factors(); psi=N
 for q in bad:psi=psi*(q+1)//q
 fields=[d for d in Ds if int(pari.qfbclassno(d))%p and kronecker(d,p)==-1 and all(kronecker(d,q)==1 for q in bad if q!=p)]
 if not fields:continue
 for l in prime_range(2,50):
  if N%l==0 or (l*l-1)%p==0 or (E.ap(l)-l-1)%p!=0:continue
  mass=(l-1)*psi//12
  if mass>4500:continue
  ds=[d for d in fields if kronecker(d,l)==-1]
  if not ds:continue
  rec=dict(curve=r['curve'],p=int(p),l=int(l),Ds=ds,mass=int(mass),N=int(N),ainvs=list(map(int,E.a_invariants())),ap=int(E.ap(p)),al=int(E.ap(l)),disc_vp=int(E.discriminant().valuation(p)),tam=int(E.tamagawa_product()),tors=int(E.torsion_order()),saved_logs=r['lam'])
  print(json.dumps(rec),flush=True);accepted.append(rec)
(root/'selection.json').write_text(json.dumps(sorted(accepted,key=lambda r:(r['mass'],r['p'],r['N'])),indent=2)+'\n')
