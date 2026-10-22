from sage.all import *
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'explicit/admission.json').read_text())
R=PolynomialRing(QQ,'x');x=R.gen()
K=NumberField(x**4-x**3+54671*x**2-54671*x+597816451,'a');a=K.gen()
Kexpr=lambda coeff:sum(QQ(v)*a**i for i,v in enumerate(coeff))
tau=K.hom([Kexpr(r['coordinate_coefficients']['tau'])])
F=EllipticCurve(K,[0,0,1,-14959712463303,-22270654620235278500])
T=F([Kexpr(cc) for cc in r['coordinate_coefficients']['T']])
assert 5*T==F(0) and T!=F(0)
assert F([tau(v) for v in T])==2*T
assert tau(tau(tau(tau(a))))==a and tau(tau(a))!=a
# Fresh prime decomposition and ideal permutation; no bnf/class-group run.
primes={}; prime_orders={}; perms={}
for ell in [3,5,11,61,239]:
 P=K.primes_above(ell)
 pm=[P.index(K.ideal([tau(z) for z in I.gens()])) for I in P]
 mat=matrix(GF(5),len(P),len(P))
 for j,i in enumerate(pm):mat[i,j]=1
 dim=(mat-2).right_kernel().dimension()
 primes[str(ell)]={'number':len(P),'ramification_residue':[[int(I.ramification_index()),int(I.residue_class_degree())] for I in P],'permutation':pm,'chi2_valuation_dimension':int(dim)}
 assert ell==11 or dim==0
 if ell==11:
  assert pm==r['ideal_boundary']['tau_permutation']
  assert [[int(z) for z in row] for row in mat]==r['ideal_boundary']['divisor_galois_matrix']
# Exact independent modular linear algebra on supplied class row; this
# verifies its consequences, not the expensive class-group computation.
b=r['ideal_boundary'];M=matrix(GF(5),b['divisor_galois_matrix']);v=vector(GF(5),b['chi_divisor_basis'][0]);cl=vector(GF(5),b['class_row_mod5']);val=matrix(GF(5),b['valuation_matrix'])
assert M*v==2*v and (M-2).right_kernel().dimension()==1
assert cl*v==1 and cl*val==0 and val.rank()==3
GM=matrix(GF(5),r['galois_matrix']);GM0=matrix(GF(5),r['empty_galois_matrix'])
assert (GM-2).right_kernel().dimension()==1 and (GM0-2).right_kernel().dimension()==1
for vv in r['point_vectors']:
 v0=vector(GF(5),vv);assert GM0*v0==2*v0 and v0!=0
# Audit q331 with independent rational coefficient reduction, exact curve
# membership, group order and saved f-values.
q=331;k=GF(q);root=k(67)
evalK=lambda z:sum(k(c)*root**i for i,c in enumerate(z.polynomial().list()))
Eq=EllipticCurve(k,[0,0,1,-14959712463303,-22270654620235278500])
Tq=Eq([evalK(c) for c in T]);assert Tq==Eq([85,247]) and 5*Tq==Eq(0)
vals=[evalK(Kexpr(cc)) for cc in r['coordinate_coefficients']['fQ']]
assert list(map(int,vals))==[112,89]
assert all(z**66==1 for z in vals)
Pq=Eq([1,102]);assert Pq!=Eq(0)
assert k(40)**66==k(150) and k(150)!=1 and k(150)**5==1
# Separate point count via discriminant(y²+y = rhs).
count=1
for xx in range(q):
 rhs=k(xx)**3+Eq.a4()*k(xx)+Eq.a6();disc=1+4*rhs
 count += 1 if disc==0 else (2 if disc.is_square() else 0)
assert count==325
out={'status':'PASS_WITH_SCAN_FILTER_CORRECTION','tau_has_order4':True,'tau_T_equals_2T':True,'prime_decompositions':primes,'chi2_boundary_value_mod5':int(cl*v),'point_vectors_span_empty_eigenline':True,'q331':{'point_values':list(map(int,vals)),'count':int(count),'nontrivial_fifth_character_of_40':150},'class_group_basis_recomputed':False,'class_group_grade':'retained certified producer computation; linear consequences independently checked','invalid_fifth_test_scan_primes':[row['q'] for row in r['scan'] if row['q']%5!=1]}
(ROOT/'duality/audit_quartic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
