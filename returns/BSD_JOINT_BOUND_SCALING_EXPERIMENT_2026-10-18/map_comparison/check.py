from pathlib import Path
import json
R=Path(__file__).resolve().parent

def rank(rows,p,n):
    basis={}
    for row in rows:
        row=[x%p for x in row]
        for k,b in sorted(basis.items()):
            a=row[k]
            if a:row=[(x-a*y)%p for x,y in zip(row,b)]
        k=next((i for i,x in enumerate(row) if x),None)
        if k is not None:
            a=pow(row[k],-1,p);basis[k]=[a*x%p for x in row]
    return len(basis)

def experiment(p):
    points=[(x,y) for x in range(p) for y in range(p) if x or y]
    reps=[(1,t) for t in range(p)]+[(0,1)]
    def evalrow(P):
        x,y=P;v=[0]*(p+1)
        if x:v[y*pow(x,-1,p)%p]=x
        elif y:v[p]=y
        return v
    ev={P:evalrow(P) for P in points};ev[(0,0)]=[0]*(p+1)
    norm=[]
    for a,b in reps:
        line=[P for P in points if (a*P[0]+b*P[1])%p==1]
        norm.append([sum(ev[P][j] for P in line)%p for j in range(p+1)])
    # Additivity against the two coordinate increments already forces full linearity.
    add=[]
    for P in [(0,0)]+points:
        for Q in [(1,0),(0,1)]:
            C=((P[0]+Q[0])%p,(P[1]+Q[1])%p)
            add.append([(x-y-z)%p for x,y,z in zip(ev[C],ev[P],ev[Q])])
    rn=rank(norm,p,p+1);ra=rank(add,p,p+1);rj=rank(norm+add,p,p+1)
    assert ra==p-1 and rn==ra==rj
    for coord in range(2):
        pointcolumn=[P[coord] for P in reps]
        assert all(sum(a*b for a,b in zip(row,pointcolumn))%p==0 for row in norm+add)
    return {'p':p,'scalar_function_dimension':p+1,'norm_rank':rn,'additivity_rank':ra,'stacked_rank':rj,'kernels_equal':True,'kernel_dimension':p+1-rj,'point_linear_forms_survive':True}
rows=[experiment(p) for p in [3,5,7,11,13,17]]
r={'status':'EQUAL_RESIDUE_KERNELS','cases':rows,'scope':'finite geometric residue maps; no arithmetic unit or class bound'}
(R/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
