#!/usr/bin/env python3
"""Exact F3 filtration checker. No third-party dependencies or class-number claims.

Schema: ambient_dimension=4, point_basis as a LIST OF VECTORS,
valuation_rows as matrix rows, unramified_basis as a LIST OF VECTORS,
class_rows as matrix rows on that unramified basis. Optional class invariants
and raw_class_rows check the conversion from cyclic coordinates to F3.
"""
import argparse,json,pathlib,itertools,time
P=3

def rref(rows,n):
 a=[[int(x)%P for x in r] for r in rows]
 if any(len(r)!=n for r in a):raise ValueError('wrong row width')
 j=0;piv=[]
 for col in range(n):
  k=next((k for k in range(j,len(a)) if a[k][col]),None)
  if k is None:continue
  a[j],a[k]=a[k],a[j];u=pow(a[j][col],-1,P);a[j]=[u*x%P for x in a[j]]
  for k in range(len(a)):
   if k!=j and a[k][col]:
    z=a[k][col];a[k]=[(x-z*y)%P for x,y in zip(a[k],a[j])]
  piv.append(col);j+=1
  if j==len(a):break
 return a[:j],piv

def rank(vectors,n):return len(rref(vectors,n)[1])
def nullspace(rows,n):
 a,piv=rref(rows,n);out=[]
 for j in range(n):
  if j in piv:continue
  x=[0]*n;x[j]=1
  for row,k in zip(a,piv):x[k]=-row[j]%P
  out.append(x)
 return out

def apply(rows,v):return [sum(x*y for x,y in zip(r,v))%P for r in rows]
def combination(vectors,c,n):return [sum(v[i]*x for v,x in zip(vectors,c))%P for i in range(n)]
def image_rows(rows,basis):return [[sum(r[i]*b[i] for i in range(len(b)))%P for b in basis] for r in rows]
def coordinates(basis,v,n):
 k=len(basis);a=[[b[i] for b in basis]+[v[i]%P] for i in range(n)]
 rr,piv=rref(a,k+1)
 if k in piv:raise ValueError('vector outside declared kernel basis')
 if len(piv)!=k:raise ValueError('dependent basis')
 out=[0]*k
 for row,j in zip(rr,piv):out[j]=row[-1]
 return out

def check(d):
 if d.get('field',3)!=3:raise ValueError('checker only supports F3')
 n=d['ambient_dimension'];W=d.get('point_basis',[[1,0,0,0],[0,1,0,0]])
 V=d['valuation_rows'];B=d.get('unramified_basis')
 if B is None:B=nullspace(V,n)
 C=d['class_rows'];k=len(B)
 if n!=4 or len(W)!=2 or rank(W,n)!=2:raise ValueError('expected independent point plane in F3^4')
 if rank(B,n)!=k or k!=n-rank(V,n) or any(any(apply(V,b)) for b in B):raise ValueError('declared basis is not full valuation kernel')
 if any(len(r)!=k for r in C):raise ValueError('class-map domain width mismatch')
 if 'raw_class_rows' in d:
  cyc=d['class_invariants'];raw=d['raw_class_rows']
  if len(cyc)!=len(raw) or any(len(r)!=k for r in raw):raise ValueError('bad cyclic coordinate dimensions')
  converted=[]
  for z,row in zip(cyc,raw):
   if z<=0:raise ValueError('bad invariant factor')
   vals=[int(x)%z for x in row]
   if any(3*x%z for x in vals):raise ValueError('claimed class coordinate not 3-torsion')
   if z%3==0:
    q=z//3
    if any(x%q for x in vals):raise ValueError('nonintegral 3-torsion normalization')
    converted.append([(x//q)%3 for x in vals])
   elif any(vals):raise ValueError('nonzero prime-to-3 component')
  if converted!=[[x%3 for x in row] for row in C]:raise ValueError('raw class coordinate conversion mismatch')
 VW=image_rows(V,W);W0=[combination(W,c,n) for c in nullspace(VW,len(W))]
 CW=image_rows(C,[coordinates(B,w,n) for w in W0])
 U=[combination(B,c,n) for c in nullspace(C,k)]
 du=len(U);duw=du+len(W)-rank(U+W,n)
 dims={'valuation':rank(V,n)-rank(VW,len(W)), 'unit':du-duw, 'class':rank(C,k)-rank(CW,len(W0))}
 assert all(x>=0 for x in dims.values())
 assert sum(dims.values())==n-len(W)==2
 assert k-len(W0)==dims['unit']+dims['class']
 return {'status':'EXACT_LINEAR_ALGEBRA_PASS','dimensions':dims,'dimension_sum':sum(dims.values()),'dim_A0':k,'dim_W0':len(W0),'dim_U':du,'dim_UW':duw,'rank_valuation':rank(V,n),'rank_point_valuation':rank(VW,len(W)),'rank_class':rank(C,k),'rank_point_class':rank(CW,len(W0)),'unramified_basis':B,'unit_basis':U,'point_unramified_basis':W0,'scope':'Checks supplied matrices and exact sequences, not their number-field arithmetic or class-group completeness.'}

def subspaces(n):
 for k in range(n+1):
  for piv in itertools.combinations(range(n),k):
   slots=[(i,j) for i,a in enumerate(piv) for j in range(a+1,n) if j not in piv]
   for vals in itertools.product(range(P),repeat=len(slots)):
    b=[[int(j==a) for j in range(n)] for a in piv]
    for (i,j),x in zip(slots,vals):b[i][j]=x
    yield b

def intervention(d,shift):
 # New cubic representatives e3+a e1+b e2, e4+c e1+d e2.
 # A physical vector's coordinates transform by the inverse matrix.
 n=4;Pcols=[[1,0,0,0],[0,1,0,0],[shift[0],shift[1],1,0],[shift[2],shift[3],0,1]]
 def inverse(v):return [(v[0]-shift[0]*v[2]-shift[2]*v[3])%3,(v[1]-shift[1]*v[2]-shift[3]*v[3])%3,v[2],v[3]]
 return {'ambient_dimension':4,'point_basis':[[1,0,0,0],[0,1,0,0]],'valuation_rows':image_rows(d['valuation_rows'],Pcols),'unramified_basis':[inverse(v) for v in d['unramified_basis']],'class_rows':d['class_rows']}

def controls():
 t=time.monotonic();total=0;invariant=0;patterns={};spaces=list(subspaces(4));assert len(spaces)==212
 for B in spaces:
  k=len(B);V=nullspace(B,4)
  for Ucoord in subspaces(k):
   C=nullspace(Ucoord,k)
   d={'ambient_dimension':4,'valuation_rows':V,'unramified_basis':B,'class_rows':C}
   r=check(d);total+=1;key=tuple(r['dimensions'].values());patterns[str(key)]=patterns.get(str(key),0)+1
   # Each of the 81 changes of the two excess representatives by the point plane.
   for shift in itertools.product(range(3),repeat=4):
    rr=check(intervention(d,shift))
    assert rr['dimensions']==r['dimensions']
    invariant+=1
 # Guard against confusing cyclic mod-3 reduction with normalization of 3-torsion.
 good={'ambient_dimension':4,'valuation_rows':[[1,0,0,0],[0,1,0,0]],'unramified_basis':[[0,0,1,0],[0,0,0,1]],'class_invariants':[12,6,2],'raw_class_rows':[[4,0],[0,2],[0,0]],'class_rows':[[1,0],[0,1]]}
 check(good);bad={**good,'class_rows':[[1,0],[0,2]]}
 try:check(bad)
 except ValueError:pass
 else:raise AssertionError('naive cyclic reduction was accepted')
 return {'status':'PASS','subspaces_F3_4':len(spaces),'nested_flags':total,'representative_changes_checked':invariant,'dimension_patterns':patterns,'cyclic_coordinate_negative_control':'rejected','elapsed_seconds':time.monotonic()-t,'scope':'Abstract exact controls, not seed class-group arithmetic.'}

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('input',nargs='?');a.add_argument('--self-test',action='store_true');a.add_argument('--out');a=a.parse_args()
 result=controls() if a.self_test else check(json.loads(pathlib.Path(a.input).read_text()))
 text=json.dumps(result,indent=2)+'\n'
 if a.out:pathlib.Path(a.out).write_text(text)
 print(text,end='')
