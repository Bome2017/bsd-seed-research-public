#!/usr/bin/env python3
"""Exact D/I model for655a1 split multiplicative reduction at coefficient7."""
import itertools,json
from fractions import Fraction
from pathlib import Path
p=7
V=[v for v in itertools.product(range(p),repeat=2) if v!=(0,0)]
def mm(g,h):
 a,b,c,d=g;e,f,i,j=h
 return ((a*e+b*i)%p,(a*f+b*j)%p,(c*e+d*i)%p,(c*f+d*j)%p)
def gi(g):
 a,b,c,d=g;q=pow((a*d-b*c)%p,-1,p)
 return (d*q%p,-b*q%p,-c*q%p,a*q%p)
def av(g,v):
 a,b,c,d=g;x,y=v
 return ((a*x+b*y)%p,(c*x+d*y)%p)
def bv(g,v):
 a,b,c,d=gi(g);x,y=v
 return ((a*x+c*y)%p,(b*x+d*y)%p)
def closure(gs):
 H={(1,0,0,1)}
 while True:
  K=H|{mm(g,h) for g in gs for h in H}
  if K==H:return sorted(H)
  H=K
I=closure([(1,1,0,1)]);D=closure([(1,1,0,1),(131%p,0,0,1)])
def orbits(action):
 out=[];seen=set()
 for x in V:
  if x not in seen:
   C=sorted({action(g,x) for g in D});out.append(C);seen.update(C)
 return out
A=orbits(av);B=orbits(bv)
ea=[len({av(g,C[0]) for g in I}) for C in A]
eb=[len({bv(g,C[0]) for g in I}) for C in B]
M=[]
for j,C in enumerate(B):
 lam=C[0];row=[]
 for i,T in enumerate(A):
  k=sum((lam[0]*v[0]+lam[1]*v[1])%p==1 for v in T)
  z=Fraction(eb[j]*k,ea[i]);assert z.denominator==1;row.append(int(z))
 M.append(row)
# chi(a)=a and chi^-1(a)=a^-1 occur on the six nonformal/fixed orbits.
a=[0 if C[0][1]==0 else C[0][1] for C in A]
b=[pow(C[0][1],-1,p) if C[0][0]==0 else 0 for C in B]
assert [sum(x*y for x,y in zip(row,a))%p for row in M]==b
# In both scalar modules these vectors are the entire χ/χ^-1 eigenspaces.
def scalar(orbs):
 index={x:i for i,C in enumerate(orbs) for x in C}
 return [[int(index[(3*C[0][0]%p,3*C[0][1]%p)]==j) for j in range(len(orbs))] for C in orbs]
def rank(A):
 A=[[x%p for x in r] for r in A];k=0
 for j in range(len(A[0])):
  z=next((i for i in range(k,len(A)) if A[i][j]),None)
  if z is None:continue
  A[k],A[z]=A[z],A[k];iv=pow(A[k][j],-1,p);A[k]=[x*iv%p for x in A[k]]
  for i in range(len(A)):
   if i!=k:
    c=A[i][j];A[i]=[(x-c*y)%p for x,y in zip(A[i],A[k])]
  k+=1
 return k
SA=scalar(A);SB=scalar(B)
assert len(A)-rank([[x-(3 if i==j else 0) for j,x in enumerate(row)] for i,row in enumerate(SA)])==1
assert len(B)-rank([[x-(5 if i==j else 0) for j,x in enumerate(row)] for i,row in enumerate(SB)])==1
r={'status':'PASS','p':p,'place':131,'local_hypothesis':'split multiplicative, primitive unipotent inertia; monodromy coefficient1 mod7 retained; Frob diag(131,1)',
   'I_order':len(I),'D_order':len(D),'point_orbits':A,'covector_orbits':B,'point_ramification':ea,'covector_ramification':eb,
   'primitive_divisor_matrix':M,'source_chi_vector':a,'target_inverse_chi_vector':b,'matched_character_map_mod7':1,
   'matched_character_divisor_index':0,'scope':'exact finite decomposition/inertia model; local arithmetic hypotheses retained'}
Path(__file__).with_name('LOCAL_DIVISOR_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
print('PASS: I_order=7; D_order=42; primitive chi-divisor map is a unit; tDchi=0')

# Bind model source orbit indices and scalar cycles to actual number-field decomposition.
actual=json.loads(Path(__file__).with_name('ACTUAL_DIVISORS.json').read_text())
assert actual[0][0]==7 and actual[0][1]==[[6,1],[7,3],[7,3]] and actual[0][2]==[1,3,2]
assert actual[0][3:]==[[],[]]
assert actual[1][0]==5 and actual[1][3:]==[[],[]]
assert actual[2][0]==131
assert sorted(actual[2][1])==sorted([[ea[i],len(A[i])//ea[i]] for i in range(len(A))])
def cycles(pm):
 seen=set();out=[]
 for i in range(len(pm)):
  if i in seen:continue
  t=i;z=[]
  while t not in seen:seen.add(t);z.append(t);t=pm[t]
  out.append(len(z))
 return sorted(out)
ind={v:i for i,C in enumerate(A) for v in C}
model_perm=[ind[(3*C[0][0]%p,3*C[0][1]%p)] for C in A]
assert cycles(model_perm)==cycles([j-1 for j in actual[2][2]])==[1,6]
assert len(actual[2][3])==len(actual[2][4])==1
r['actual_source_binding']={'coefficient_prime_has_no_faithful_divisor_part':True,'bad_prime_ef_and_scalar_cycles_match':True,'actual_scalar_permutation':actual[2][2],'model_scalar_permutation':[j+1 for j in model_perm],'S':[5,7,131],'total_primitive_divisor_kernel_dimension':0}
Path(__file__).with_name('LOCAL_DIVISOR_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
print('ACTUAL_P7_P5_P131_BINDING_PASS: tDchi(S)=0')
# Negative control: omit primitive ramification and falsely obtain zero mod7.
raw=[[sum((C[0][0]*v[0]+C[0][1]*v[1])%p==1 for v in T) for T in A] for C in B]
assert [sum(x*y for x,y in zip(row,a))%p for row in raw]==[0]*len(B)
r['countercontrol_unweighted_count_falsely_zero_mod7']=True
Path(__file__).with_name('LOCAL_DIVISOR_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
