from pathlib import Path
import json,functools
r=Path(__file__).resolve().parent
out=[]
for q,ps in json.loads((r/'SPLIT_POINTS.json').read_text()):
    pts=[tuple(P) for P in ps];ix={P:i for i,P in enumerate(pts)}
    def add(P,Q):
        if P is None:return Q
        if Q is None:return P
        x,y=P;u,v=Q
        if x==u and (y+v+1)%q==0:return None
        m=((3*x*x-1)*pow(2*y+1,-1,q) if P==Q else (v-y)*pow(u-x,-1,q))%q
        z=(m*m-x-u)%q
        return z,(-y+m*(x-z)-1)%q
    def mul(P,n):
        Z=None
        for _ in range(n):Z=add(Z,P)
        return Z
    assert len(ix)==24
    assert all((y*y+y-x*x*x+x)%q==0 and mul((x,y),5) is None for x,y in pts)
    perms={a:[ix[mul(P,a)] for P in pts] for a in range(1,5)}
    vals=[2*(x+y)%q for x,y in pts]
    a=[functools.reduce(lambda z,k:z*pow(vals[perms[k][i]],4*pow(k,-1,5)%5,q)%q,range(1,5),1) for i in range(24)]
    lines=set()
    for T in pts:
        base={mul(T,k) for k in range(5)}
        for P in pts:
            if P in base:continue
            lines.add(tuple(sorted(ix[add(P,mul(T,k))] for k in range(5))))
    assert len(lines)==24
    rows=[]
    for line in sorted(lines):
        values=[a[i] for i in line]
        norm=functools.reduce(lambda z,t:z*t%q,values,1)
        rows.append({'line_indices':line,'projected_values':values,'norm':norm,'power_residue':pow(norm,(q-1)//5,q)})
    assert any(x['power_residue']!=1 for x in rows)
    out.append({'q':q,'points':pts,'norms':rows,'nontrivial_norm_residue_count':sum(x['power_residue']!=1 for x in rows)})
(r/'NORM_RESIDUES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{'q':x['q'],'nontrivial_norm_residue_count':x['nontrivial_norm_residue_count']} for x in out],indent=2))
