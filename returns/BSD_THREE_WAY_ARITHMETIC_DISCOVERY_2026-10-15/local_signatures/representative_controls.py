from pathlib import Path
import json,importlib.util,contextlib,io,itertools
from fractions import Fraction
R=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'literal_replay.py');lit=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(lit)
f=lit.f;results=[]
for nm in ['1913b1','28042a1','seed3','389a1','mirror389_false']:
 p=R/nm;poly=json.loads((p/'actual_polynomials.json').read_text());S=json.loads((p/'SIGNATURES.json').read_text());np=S['summary']['point_dimension'];nc=len(poly['classes']);ct={'cube_unit':0,'cube_valuation':0,'uniformizer':0,'point_shifts':0}
 for b in S['fresh_primes']:
  q=b['prime'];om=b['cubic_root'];roots=b['roots'];Q=b['annihilator_rows'];ev=[[lit.local_eval(c,poly['field'],r,q)for c in poly['classes']]for r in roots];U=[[u for v,u in row]for row in ev]
  chi=lambda u:[1,om,om*om%q].index(pow(u,(q-1)//3,q))
  for ri,row in enumerate(ev):
   for ci,(v,u) in enumerate(row):
    for c in [2,3,q-1]:assert chi(u*pow(c,3,q)%q)==chi(u);ct['cube_unit']+=1
    for k in [-1,1]:
     scaled=[str(Fraction(c)*Fraction(q)**(3*k))for c in poly['classes'][ci]]
     vv,uu=lit.local_eval(scaled,poly['field'],roots[ri],q)
     assert vv==v+3*k and chi(uu)==chi(u);ct['cube_valuation']+=1
    assert chi(u*pow(2,-v,q)%q)==chi(u);ct['uniformizer']+=1
  for j in range(nc):
   old=[[chi(row[j])]for row in U];old=f.mul(Q,old)
   for ee in itertools.product(range(3),repeat=np):
    changed=[]
    for row in U:
     u=row[j]
     for k,e in enumerate(ee):u=u*pow(row[k],e,q)%q
     changed.append([chi(u)])
    assert f.mul(Q,changed)==old;ct['point_shifts']+=1
 results.append({'curve':nm,'passed':True,'counts':ct,'scope':'Cubic-residue representative, canonical q-uniformizer, and all mod3 combinations of saturated point directions; no Selmer membership inferred from signatures.'})
(R/'REPRESENTATIVE_CONTROLS.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
