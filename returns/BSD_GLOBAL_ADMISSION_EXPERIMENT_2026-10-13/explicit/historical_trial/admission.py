from sage.all import *
import json,time
R=PolynomialRing(QQ,'x');x=R.gen();d=ZZ(43737)
K=NumberField(x**4-x**3+54671*x**2-54671*x+597816451,'a');a=K.gen()
F=EllipticCurve(QQ,[0,0,1,-14959712463303,-22270654620235278500])
print('ISOGENIES',flush=True)
iss=F.isogenies_prime_degree(5)
for I in iss: print('kernel',I.kernel_polynomial(),flush=True)
kp=iss[0].kernel_polynomial();rr=kp.change_ring(K).roots();print('roots',rr,flush=True)
FK=F.change_ring(K);T=FK.lift_x(rr[0][0]);print('T',T, 'order',T.order(),flush=True)
autos=K.automorphisms();tau=next(s for s in autos if s(s(a)) != a);tT=FK([tau(z) for z in T]);mult=next(j for j in range(1,5) if j*T==tT);print('tau',tau(a),'mult',mult,flush=True)
S=K.primes_above(11)
print('SELmerSpace begin',len(S),flush=True)
V,gens,frm,to=K.selmer_space(S,ZZ(5),proof=True)
print('selmerdim',V.dimension(),'gens',[str(g) for g in gens],flush=True)
mat=matrix(GF(5),[list(to(tau(g))) for g in gens]).transpose()
EV=(mat-mult*identity_matrix(GF(5),V.dimension())).right_kernel()
print('matrix',mat,'eigbasis',EV.basis(),flush=True)
print('emptybegin',flush=True)
V0,gens0,frm0,to0=K.selmer_space([],ZZ(5),proof=True)
mat0=matrix(GF(5),[list(to0(tau(g))) for g in gens0]).transpose()
EV0=(mat0-mult*identity_matrix(GF(5),V0.dimension())).right_kernel()
print('emptydim',V0.dimension(),'emptymatrix',mat0,'emptyeig',EV0.basis(),flush=True)
rows=[]
for e in EV.basis():
 g=frm(e); row={'vector':list(map(int,e)),'element':str(g),'valuations11':[int(g.valuation(P)) for P in S]};rows.append(row);print('EIG',row,flush=True)
result={'field_polynomial':str(K.polynomial()),'class_group_invariants':list(map(int,K.class_group(proof=True).invariants())),'kernel_polynomial':str(kp),'T':list(map(str,T)),'tau':str(tau(a)),'kernel_multiplier':int(mult),'S11':list(map(str,S)),'selmer_generators':list(map(str,gens)),'galois_matrix':[[int(z) for z in row] for row in mat],'eigenspace':rows,'empty_generators':list(map(str,gens0)),'empty_galois_matrix':[[int(z) for z in row] for row in mat0],'empty_eigenvectors':[list(map(int,e)) for e in EV0.basis()],'empty_eigengenerators':[str(frm0(e)) for e in EV0.basis()]}
open('admission.json','w').write(json.dumps(result,indent=2)+'\n')
# Evaluate normalized Miller f_{5,T} on F; poles/zeros have their usual exceptions.
def line(P,Q,R):
    if P.is_zero() or Q.is_zero():return K(1)
    if P == -Q:return R[0]-P[0]
    m=(Q[1]-P[1])/(Q[0]-P[0]) if P!=Q else (3*P[0]**2+FK.a4())/(2*P[1]+FK.a3())
    numer=R[1]-P[1]-m*(R[0]-P[0]);PQ=P+Q
    return numer if PQ.is_zero() else numer/(R[0]-PQ[0])
def descent(R):
    f=K(1);P=T
    for bit in '01': # binary5 after leading1
        f=f*f*line(P,P,R);P=2*P
        if bit=='1':f=f*line(P,T,R);P=P+T
    assert P.is_zero()
    return f
Q=[FK(6288329,-11502941299),FK(8502485,21568458354)]
fQ=[descent(P) for P in Q]
qvec=[to0(z) for z in fQ]
print('POINT_VECTORS',qvec,flush=True)
assert all(mat0*v==mult*v for v in qvec)
assert matrix(GF(5),qvec).rank()==1
assert EV0.dimension()==1
result['point_descent_values']=list(map(str,fQ));result['point_vectors']=[list(map(int,v)) for v in qvec]
print('SCAN BEGIN',flush=True)
scan=[];hit=None
for q in prime_range(2,5001):
    if q in [3,5,11,61,239]:continue
    k=GF(q);pr=K.polynomial().change_ring(k).roots()
    if len(pr)!=4:continue
    er=sorted(z for z,m in pr)[0]
    def ev(z):return z.polynomial().change_ring(k)(er)
    fq=[ev(z) for z in fQ]
    if not all(fq):continue
    image=[int(v**((q-1)//5)) for v in fq]
    scan.append({'q':int(q),'root':int(er),'point_values':list(map(int,fq)),'fifth_test':image})
    if image!=[1,1]:continue
    Ered=F.change_ring(k);Tr=Ered([ev(z) for z in T]);bad=set([int((j*Tr)[0]) for j in range(1,5)])
    def rl(P,Q,R):
      if P.is_zero() or Q.is_zero():return k(1)
      if P == -Q:return R[0]-P[0]
      mm=(Q[1]-P[1])/(Q[0]-P[0]) if P!=Q else (3*P[0]**2+Ered.a4())/(2*P[1]+Ered.a3())
      num=R[1]-P[1]-mm*(R[0]-P[0]);PQ=P+Q
      return num if PQ.is_zero() else num/(R[0]-PQ[0])
    for xx in range(q):
      if xx in bad:continue
      for Rloc in sorted(Ered.lift_x(k(xx),all=True),key=lambda P:int(P[1])):
        val=rl(Tr,Tr,Rloc)**2*rl(2*Tr,2*Tr,Rloc)*rl(4*Tr,Tr,Rloc)
        if val and val**((q-1)//5)!=1:
          hit={'q':int(q),'root':int(er),'T':list(map(int,Tr)),'point_values':list(map(int,fq)),'local_point':list(map(int,Rloc)),'local_value':int(val),'fifth_test':int(val**((q-1)//5)),'group_cardinality':int(Ered.cardinality())};break
      if hit:break
    if hit:break
result['scan']=scan;result['hit']=hit
print('HIT',hit,flush=True)
open('admission.json','w').write(json.dumps(result,indent=2)+'\n')
# Exact ideal-class obstruction for allowing new support at11.
CG=K.class_group(proof=True)
classes=[list(map(int,CG(P).exponents())) for P in S]
perm=[S.index(K.ideal([tau(z) for z in P.gens()])) for P in S]
PV=matrix(GF(5),4,4)
for j,i in enumerate(perm):PV[i,j]=1
chiDiv=(PV-mult*identity_matrix(GF(5),4)).right_kernel()
clrow=vector(GF(5),[cs[0] for cs in classes])
valuation_matrix=matrix(GF(5),[[g.valuation(P) for g in gens] for P in S])
obstructions=[int(clrow*v) for v in chiDiv.basis()]
assert chiDiv.dimension()==1 and obstructions[0]!=0
assert clrow*valuation_matrix==0
assert valuation_matrix.rank()==3
result['ideal_boundary']={'class_group_invariants':list(map(int,CG.invariants())),'prime_classes':classes,'tau_permutation':perm,'divisor_galois_matrix':[[int(z) for z in row] for row in PV],'chi_divisor_basis':[list(map(int,v)) for v in chiDiv.basis()],'class_row_mod5':list(map(int,clrow)),'nonzero_boundary':obstructions,'valuation_matrix':[[int(z) for z in row] for row in valuation_matrix]}
print('IDEAL_BOUNDARY',result['ideal_boundary'],flush=True)
open('admission.json','w').write(json.dumps(result,indent=2)+'\n')
result['certification']={'bnfcertify':int(K.pari_bnf(proof=True).bnfcertify()),'isogeny_target_isomorphic_A':bool(iss[0].codomain().is_isomorphic(EllipticCurve(QQ,[0,0,1,-19766893413,-1937478573143510])))}
result['coordinate_coefficients']={'T':[list(map(str,z.polynomial().list())) for z in T],'tau':list(map(str,tau(a).polynomial().list())),'fQ':[list(map(str,z.polynomial().list())) for z in fQ]}
assert result['certification']['bnfcertify']==1 and result['certification']['isogeny_target_isomorphic_A']
open('admission.json','w').write(json.dumps(result,indent=2)+'\n')
