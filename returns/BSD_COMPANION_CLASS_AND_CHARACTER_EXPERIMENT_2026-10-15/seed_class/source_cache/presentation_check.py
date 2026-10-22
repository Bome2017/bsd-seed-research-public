#!/usr/bin/env python3
"""Exact integer/finite-field audit of saved class presentation; not class certification."""
from pathlib import Path
import itertools,hashlib,json,math,re
from sympy import Matrix
r=Path(__file__).resolve().parent
s=(r/'inspect.out').read_text()
def matrix(key):
    v=re.search(re.escape(key)+r'=\[([^\]]*)\]',s).group(1)
    return Matrix([[int(x.strip()) for x in row.split(',')] for row in v.split(';')])
D=Matrix.diag(12,6,2);T=matrix('TAU');P=matrix('S_PRIME_CLASSES');H=D.row_join(P)
g=0
for cols in itertools.combinations(range(H.cols),3):
    g=math.gcd(g,abs(int(H[:,cols].det())))
assert g==1
assert all(int((T*T-Matrix.eye(3))[i,j])%int(D[i,i])==0 for i in range(3) for j in range(3))
odd=D.row_join(T+Matrix.eye(3));od=0
for cols in itertools.combinations(range(odd.cols),3): od=math.gcd(od,abs(int(odd[:,cols].det())))
v3=lambda n: 0 if n%3 else 1+v3(n//3)
assert v3(od)==2
# The two primes in columns4,9 alone generate the 3-primary part.
M=P[:2,(3,8)];det=int(M.det());assert det%3!=0
geom=(r/'geometry.out').read_text();assert 'GEOMETRY_COMPLETE' in geom
assert 'A_SIGN=[2, 3];PLUS_SIGN=[2, 1];ORD_MINUS_UNIT_RANK=2' in geom
perm=[1,2,3,5,4,6,7,8,10,9,11]
assert 'S_INVOLUTION=['+', '.join(map(str,perm))+']' in geom
rankD=sum(i+1!=j for i,j in enumerate(perm))//2
assert rankD==2
out={'status':'EXACT_SAVED_PRESENTATION_CHECK_PASS','source_class_certification':'NOT_CERTIFIED; conditional on cached class completeness (retained GRH grade)','S_quotient_order_in_computed_presentation':g,'ordinary_minus_3_length_in_computed_presentation':2,'chosen_S_prime_columns_one_based':[4,9],'chosen_3_primary_determinant':det,'ordinary_minus_unit_rank':2,'minus_S_divisor_rank':rankD,'minus_S_unit_rank':2+rankD,'conditional_companion_minus_S_class_length_upper':2,'conditional_entire_global_norm_kernel_dimension_upper':4,'known_Selmer_or_Sha_used':False,'input_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [r/'inspect.out',r/'geometry.out']}}
print(json.dumps(out,indent=2))
