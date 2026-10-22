#!/usr/bin/env python3
"""Actual seed unramified prime-ideal orbit demand; not class completeness."""
import ast, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rows=[ast.literal_eval(x) for x in (ROOT/'seed_counts.out').read_text().splitlines() if x.strip()]

def primitive(p):
    return next(g for g in range(2,p) if len({pow(g,i,p) for i in range(p-1)})==p-1)

def demand(p,q,a,group,B=2000):
    # The only repeated-root ambiguity relevant to a faithful scalar character
    # is identity vs nontrivial unipotent. Full rational E[p] resolves it.
    identity=(a%p==2 and q%p==1 and len(group)==2 and all(n%p==0 for n in group))
    if a*a%p==4*q%p and a%p!=2:
        # A nonidentity scalar lies in the Frobenius subgroup, for both Jordan types.
        return {'q':q,'trace':a,'columns':0,'identity':False,'skipped_scalar_stabilizer':True}
    g=primitive(p)
    V={(x,y) for x in range(p) for y in range(p) if x or y}
    action=(lambda v:v) if identity else (lambda v:((-q*v[1])%p,(v[0]+a*v[1])%p))
    orbits=[]; lookup={}
    while V:
        v=min(V); orb=[]; w=v
        while w not in orb:
            orb.append(w); w=action(w)
        assert w==v
        idx=len(orbits)
        for w in orb: lookup[w]=idx; V.remove(w)
        orbits.append(orb)
    eligible={i for i,o in enumerate(orbits) if q**len(o)<=B}
    scalar={i:lookup[(g*orbits[i][0][0]%p,g*orbits[i][0][1]%p)] for i in range(len(orbits))}
    free=[]; all_lengths=[]
    while eligible:
        i=min(eligible); cyc=[];j=i
        while j not in cyc:
            cyc.append(j); j=scalar[j]
        assert j==i and set(cyc)<=eligible
        eligible-=set(cyc); all_lengths.append(len(cyc))
        if len(cyc)==p-1:free.append(len(orbits[i]))
    return {'q':q,'trace':a,'columns':len(free),'identity':identity,'prime_degrees':free,'scalar_orbit_lengths':all_lengths}

# Independent direct finite-field count for every saved trace (not ellcard).
for q,a,group in rows:
    card=1+sum(1 if (v:=(x*x*x-22735*x*x+106272484*x)%q)==0 else 1+(1 if pow(v,(q-1)//2,q)==1 else -1) for x in range(q))
    assert card==q+1-a==math.prod(group)
output={'status':'FINITE_GENERATOR_DEMAND_ONLY','norm_cutoff':2000,'excluded_rational_bad_primes':[2,3,2243,4547,5843],'count_rows_verified':len(rows),'panels':[]}
for p in [5,7,11,13]:
    data=[demand(p,q,a,G) for q,a,G in rows if q!=p]
    panel={'p':p,'faithful_unit_rank':(p+1)//2,'relative_antiunit_rank':(p*p-1)//4,'unramified_columns':sum(r['columns'] for r in data),'identity_frobenius_primes':[r['q'] for r in data if r['identity']],'rows':data}
    output['panels'].append(panel)
(ROOT/'RESULT.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='panels'}))
for x in output['panels']:print(json.dumps({k:v for k,v in x.items() if k!='rows'}))
