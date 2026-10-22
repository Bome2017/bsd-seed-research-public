#!/usr/bin/env python3
"""Exhaust all subgroups containing the chosen transvection in GL2(F3)."""
import itertools,json
from pathlib import Path
q=3
els=tuple(a for a in itertools.product(range(q),repeat=4) if (a[0]*a[3]-a[1]*a[2])%q)
pos={a:i for i,a in enumerate(els)}
def mul(a,b):
 return tuple(v%q for v in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
tab=[[pos[mul(a,b)] for b in els] for a in els]
identity=pos[(1,0,0,1)];u=pos[(1,1,0,1)]
def closure(gens):
 out={identity};todo=[identity]
 while todo:
  x=todo.pop()
  for g in gens:
   y=tab[x][g]
   if y not in out:out.add(y);todo.append(y)
 return frozenset(out)
first=closure([u]);known={first};todo=[first]
while todo:
 h=todo.pop()
 for g in range(48):
  if g in h:continue
  hh=closure(tuple(h)+(g,))
  if hh not in known:known.add(hh);todo.append(hh)
def det(h):return sorted({(els[x][0]*els[x][3]-els[x][1]*els[x][2])%3 for x in h})
def orbit(h):return {(els[x][0],els[x][2]) for x in h}
rows=[{'order':len(h),'determinants':det(h),'orbit_size_e1':len(orbit(h))} for h in known]
rows.sort(key=lambda r:(r['order'],r['determinants'],r['orbit_size_e1']))
qual=[h for h in known if len(orbit(h))==8 and det(h)==[1,2]]
assert len(qual)==1 and len(qual[0])==48
result={'group_order':48,'transvection_order':3,'subgroups_containing_transvection':len(known),'qualifying_subgroups':len(qual),'unique_qualifying_order':48,'subgroup_profiles':rows,'arithmetic_application':'Irreducible degree-eight nonzero torsion-point field gives transitivity; multiplicative discriminant valuation one gives transvection; Weil determinant is surjective.'}
print(json.dumps(result,indent=2))
