#!/usr/bin/env python3
"""Point-relative joint-repair diagnostics; exact F_3 arithmetic, no Sha inputs.

New purpose: export dual mixed arithmetic row certificates and block profiles.
This is not the earlier exhaustive finite-field repair enumerator.
"""
import argparse, hashlib, json
from pathlib import Path
P = 3

def rref(A, ncols=None):
    A = [[x % P for x in r] for r in A]
    n = len(A[0]) if A else (ncols or 0)
    piv=[]; i=0
    for j in range(n):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None: continue
        A[i],A[k]=A[k],A[i]
        u=pow(A[i][j],-1,P); A[i]=[(u*x)%P for x in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]:
                u=A[k][j]; A[k]=[(x-u*y)%P for x,y in zip(A[k],A[i])]
        piv.append(j); i+=1
        if i==len(A): break
    return A,piv

def rank(A): return len(rref(A)[1])
def tr(A,ncols=None):
    n=len(A[0]) if A else (ncols or 0)
    return [[A[i][j] for i in range(len(A))] for j in range(n)]
def mm(A,B):
    if not A:return []
    if not B:return [[] for _ in A]
    assert len(A[0])==len(B)
    return [[sum(x*y for x,y in zip(row,col))%P for col in tr(B)] for row in A]
def cat(A,B):
    assert len(A)==len(B)
    return [a+b for a,b in zip(A,B)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def ker(A,n):
    R,piv=rref(A,n); free=[j for j in range(n) if j not in piv]
    out=[]
    for j in free:
        v=[0]*n;v[j]=1
        for i,k in enumerate(piv):v[k]=-R[i][j]%P
        out.append(v)
    return tr(out,ncols=n)
def rowbasis(A):
    if not A:return [],[]
    ix=rref(tr(A))[1];return [A[i] for i in ix],ix
def colbasis(A):
    ix=rref(A)[1];return [[r[j] for j in ix] for r in A]
def cols(A):return len(A[0]) if A else 0
def coordinates(B,V):
    """Unique coordinates of columns V in independent columns B."""
    n=cols(B); out=[]
    for v in tr(V):
        R,piv=rref([r+[x] for r,x in zip(B,v)])
        assert n not in piv and len(piv)==n
        z=[0]*n
        for i,j in enumerate(piv):z[j]=R[i][-1]
        out.append(z)
    ans=tr(out,ncols=n);assert mm(B,ans)==V
    return ans
def complement(B,H):
    out=[[] for _ in H];basis=[r[:] for r in B];d=rank(B)
    for v in tr(H):
        X=[r+[x] for r,x in zip(basis,v)]
        if rank(X)>d:
            basis=X;out=[r+[x] for r,x in zip(out,v)];d+=1
    assert rank(basis)==rank(H)
    return out
def zero(A):return not any(x%P for r in A for x in r)

def adapt(d):
    n=d['source_dimension']
    if 'valuation_rows' in d:
        assert d['actual_columns'][:2]==['P1','P2']
        scalar=[[(x+int(i==j))%3 for j,x in enumerate(row)] for i,row in enumerate(d['tau_matrix'])]
        return dict(n=n,V=d['valuation_rows'],H0=d['unramified_basis_rows'],U=d['unit_basis_rows'],
          G0=scalar,A=d['additivity_rows'],L=d['local_rows'],W=[r[:2] for r in d['actual_coordinates']],
          protected=d['actual_coordinates'],locals=[{'prime':x[0],'rows':x[1]} for x in d['local_block_rows']],
          grade=d['source_completeness_grade'])
    V=d['valuation'];U=d['units'];W=d['points'] or [[] for _ in range(n)]
    return dict(n=n,V=V,H0=d.get('valuation_zero_basis',ker(V,n)),U=U,G0=d['scalar'],
      A=d['additivity'],L=d['local'],W=W,protected=W,locals=d['local_blocks'],
      grade='Retain source certificate separately; numerical matrices do not authenticate completeness.')

def profile(d,G,L,label):
    n=d['n'];U=d['U'];H=d['H0'];W=colbasis(d['W']);nu=cols(U)
    assert rank(U)==nu and zero(mm(d['V'],U))
    assert zero(mm(G,d['protected'])) and zero(mm(L,d['protected'])), 'Protected actual class rejected'
    C=complement(U,H);B=cat(U,C);nc=cols(C)
    Gbase,gix=rowbasis(G);Lbase,lix=rowbasis(L)
    GU=mm(Gbase,U);LU=mm(Lbase,U);GC=mm(Gbase,C);LC=mm(Lbase,C)
    annG=tr(ker(tr(GU,ncols=nu),len(Gbase)))
    annL=tr(ker(tr(LU,ncols=nu),len(Lbase)))
    C0=ker(mm(annG,GC)+mm(annL,LC),nc)
    gr,gri=rowbasis(GU);lr,lri=rowbasis(LU)
    # Relations a*GU=b*LU are the dual common-unit-row intersection.
    T=cat(tr(gr,ncols=nu),[[-x%P for x in row] for row in tr(lr,ncols=nu)])
    rel=ker(T,len(gr)+len(lr));witnesses=[];O=[]
    for r in tr(rel):
        aa=r[:len(gr)];bb=r[len(gr):]
        ag=[sum(aa[k]*Gbase[gri[k]][j] for k in range(len(aa)))%P for j in range(n)]
        bl=[sum(bb[k]*Lbase[lri[k]][j] for k in range(len(bb)))%P for j in range(n)]
        mixed=[(x-y)%P for x,y in zip(ag,bl)]
        assert zero(mm([mixed],U))
        values=mm([mixed],C)[0];O.append(values)
        witnesses.append(dict(global_row_coefficients=[{'row':gix[gri[k]],'coefficient':a} for k,a in enumerate(aa) if a],
          local_row_coefficients=[{'row':lix[lri[k]],'coefficient':b} for k,b in enumerate(bb) if b],
          convention='global minus local; this evaluates -dual(omega)',source_row=mixed,class_values=values))
    assert rank(mm([w['source_row'] for w in witnesses],U))==0
    overlap=len(witnesses)
    assert overlap==rank(GU)+rank(LU)-rank(GU+LU)
    Cadm=mm(C0,ker(mm(O,C0),cols(C0)))
    J0=mm(H,ker(mm(Gbase+Lbase,H),cols(H)))
    K=mm(U,ker(mm(Gbase+Lbase,U),nu))
    Jfull=ker(Gbase+Lbase,n)
    W0=mm(W,ker(mm(d['V'],W),cols(W)))
    assert zero(mm(Gbase+Lbase,W))
    wc=coordinates(B,W0)[nu:]
    class_point_dim=rank(wc)
    unit_point_dim=cols(W0)-class_point_dim
    assert cols(J0)==cols(K)+cols(Cadm)
    assert rank(cat(Cadm,wc))==cols(Cadm)
    du=cols(K)-unit_point_dim;dc=cols(Cadm)-class_point_dim
    dv=cols(Jfull)-cols(J0)-cols(W)+cols(W0)
    assert min(du,dc,dv)>=0 and du+dc+dv==cols(Jfull)-cols(W)
    return dict(label=label,source_dimension=n,unit_dimension=nu,class_span_dimension=nc,
      source_class_lift_basis=C,global_unit_rank=rank(GU),local_unit_rank=rank(LU),joint_unit_rank=rank(GU+LU),
      dual_overlap_dimension=overlap,separately_repairable_class_dimension=cols(C0),
      compatibility_defect_rank=rank(mm(O,C0)),joint_admitted_class_dimension=cols(Cadm),
      joint_admitted_unit_dimension=cols(K),point_unit_intersection_dimension=unit_point_dim,
      point_class_image_dimension=class_point_dim,point_relative_dimensions=dict(unit=du,ordinary_class=dc,valuation=dv),
      full_joint_dimension=cols(Jfull),protected_columns=cols(d['protected']),
      mixed_class_rows=O,dual_mixed_certificates=witnesses)

def run(path,extra_path=None):
    original=json.loads(path.read_text());d=adapt(original);ans=[]
    source_hash=hashlib.sha256(path.read_bytes()).hexdigest();extra_binding=None
    gs=[('scalar',d['G0']),('scalar+all_saved_additivity',d['G0']+d['A'])]
    assert len(d['A'])%32==0
    gs += [(f'scalar+saved_split_block_{i}',d['G0']+d['A'][32*i:32*i+32]) for i in range(len(d['A'])//32)]
    if extra_path:
        extra=json.loads(extra_path.read_text())
        assert extra['source_sha256']==source_hash, 'Fresh rows are not bound to this source matrix'
        extra_binding={'path':str(extra_path),'sha256':hashlib.sha256(extra_path.read_bytes()).hexdigest()}
        for b in extra['blocks']:
            assert all(len(row)==d['n'] for row in b['rows']), 'Fresh source row has wrong width'
        gs += [(f"scalar+fresh_{b['label']}",d['G0']+b['rows']) for b in extra['blocks']]
    ls=[('all_local',d['L'])]+[(f"local_{x['prime']}",x['rows']) for x in d['locals']]
    for gn,g in gs:
        for ln,l in ls:ans.append(profile(d,g,l,gn+'__'+ln))
    return dict(source=str(path),sha256=source_hash,extra_binding=extra_binding,
      grade=d['grade'],scope='Exact containing-screen and source-span diagnostics, not an independent arithmetic bound.',profiles=ans)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('matrix',type=Path);ap.add_argument('--extra',type=Path);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();out=run(args.matrix,args.extra);args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'source':str(args.matrix),'profiles':len(out['profiles']),'protected_columns':out['profiles'][0]['protected_columns'],'status':'DUAL_OVERLAP_PROFILES_VERIFIED'}))
