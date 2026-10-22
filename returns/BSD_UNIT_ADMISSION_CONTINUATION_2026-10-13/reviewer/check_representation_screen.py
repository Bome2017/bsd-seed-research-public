#!/usr/bin/env python3
"""Exact small finite-group/archimedean model checks, not arithmetic units."""
import json, pathlib, time
from fractions import Fraction

def rank(rows,n,p):
    a=[[x%p for x in r] for r in rows]; k=0
    for j in range(n):
        z=next((i for i in range(k,len(a)) if a[i][j]),None)
        if z is None: continue
        a[k],a[z]=a[z],a[k];t=pow(a[k][j],-1,p)
        a[k]=[x*t%p for x in a[k]]
        for i in range(k+1,len(a)):
            t=a[i][j]
            if t:a[i]=[(x-t*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k

def check(p):
    V=[(x,y) for x in range(p) for y in range(p) if x or y]
    c=lambda v:(v[0],-v[1]%p)
    orb={min(v,c(v)) for v in V}
    # Finite places here means finite set of archimedean place labels.
    fixed={a:sum(min((a*v[0]%p,a*v[1]%p),c((a*v[0]%p,a*v[1]%p)))==v for v in orb)
           for a in range(1,p)}
    assert len(orb)==(p*p+p-2)//2
    assert fixed[p-1]==(p-1)//2
    assert all(fixed[a]==0 for a in range(2,p-1))
    # f(x,y)=x*f(1,y/x), or y*f(0,1), enforces scalar homogeneity.
    def coeff(v):
        x,y=v
        return (y*pow(x,-1,p)%p,x) if x else (p,y)
    sym=[]
    for v in V:
        row=[0]*(p+1);i,s=coeff(v);j,t=coeff(c(v))
        row[i]+=s;row[j]-=t;sym.append(row)
    lines=[]
    for a,b in V:
        row=[0]*(p+1)
        points=[(x,(1-a*x)*pow(b,-1,p)%p) for x in range(p)] if b else [(pow(a,-1,p),y) for y in range(p)]
        for v in points:i,s=coeff(v);row[i]+=s
        lines.append(row)
    # The transpose switches the scalar character to its inverse.
    def inverse_coeff(v):
        i,s=coeff(v)
        return i,pow(s,-1,p)
    reverse_sym=[];reverse_lines=[]
    for v in V:
        row=[0]*(p+1);i,s=inverse_coeff(v);j,t=inverse_coeff(c(v))
        row[i]+=s;row[j]-=t;reverse_sym.append(row)
    for a,b in V:
        row=[0]*(p+1)
        points=[(x,(1-a*x)*pow(b,-1,p)%p) for x in range(p)] if b else [(pow(a,-1,p),y) for y in range(p)]
        for v in points:i,s=inverse_coeff(v);row[i]+=s
        reverse_lines.append(row)
    reverse_dim=p+1-rank(reverse_sym+reverse_lines,p+1,p)
    ds=p+1-rank(sym,p+1,p)
    dl=p+1-rank(lines,p+1,p)
    db=p+1-rank(sym+lines,p+1,p)
    assert (ds,dl,db,reverse_dim)==((p+1)//2,2,1,(p-1)//2)
    return {'p':p,'nonzero_torsion_vectors':len(V),'real_places_K':p-1,
            'complex_pairs_K':p*(p-1)//2,'unit_rank_K':(p*p+p-4)//2,
            'real_places_Kplus':p-1,'complex_pairs_Kplus':(p-1)**2//4,
            'relative_norm_one_unit_rank':(p*p-1)//4,
            'scalar_weight_one_unit_rank':(p+1)//2,
            'formal_homogeneous_c_invariant_dimension':ds,
            'formal_affine_line_kernel_dimension':dl,
            'formal_c_invariant_affine_line_kernel_dimension':db,
            'formal_transpose_inverse_character_kernel_dimension':reverse_dim,
            'scalar_fixed_arch_places':fixed}

def trim(a):
    while a and a[-1]==0:a.pop()
    return a
def rem(a,b):
    a=a[:]
    while len(a)>=len(b):
        q=a[-1]/b[-1];k=len(a)-len(b)
        for j,x in enumerate(b):a[k+j]-=q*x
        trim(a)
    return a
def roots(a):
    a=list(map(Fraction,a));chain=[a,trim([i*a[i] for i in range(1,len(a))])]
    while chain[-1]:
        r=rem(chain[-2],chain[-1])
        if not r:break
        chain.append([-x for x in r])
    def changes(atminus):
        signs=[(1 if a[-1]>0 else -1)*(-1 if atminus and (len(a)-1)%2 else 1) for a in chain]
        return sum(a!=b for a,b in zip(signs,signs[1:]))
    return changes(True)-changes(False)

if __name__=='__main__':
    start=time.monotonic(); rows=[check(p) for p in [3,5,7,11,13,17,19,23,31]]
    quartic=[-117686586145348587,-7030398068360,-1188376638,0,1]
    octic=[quartic[i//2] if i%2==0 else 0 for i in range(9)]
    assert roots(quartic)==2 and roots(octic)==2
    out={'status':'PASS','scope':'Exact archimedean/permutation model and actual defining-polynomial signatures; no arithmetic unit-map computation.',
         'seed_actual_signature':{'K':[2,3],'Kplus':[2,1],'norm_one_unit_rank':2,
                                  'roots_of_unity':'Only +/-1, since K has real embeddings.'},
         'rows':rows}
    p=pathlib.Path(__file__).with_name('REPRESENTATION_CHECK.json');p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
