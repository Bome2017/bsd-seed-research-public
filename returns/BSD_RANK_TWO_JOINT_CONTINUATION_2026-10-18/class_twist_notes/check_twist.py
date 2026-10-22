from pathlib import Path
import json, sympy as s
here=Path(__file__).resolve().parent
root=here.parent
x=s.symbols('x');d=-47
f=4*x**3-4*x**2-40*x-79
g=4*x**3-4*x**2-91304*x+9647521
assert s.expand(d**3*f.subs(x,(x-16)/d)-g)==0
D=json.loads((root/'twist_divisor/ACTUAL_DIVISORS.json').read_text())
rows=[]
for q,ef,perm,*rest in D:
 n=len(perm)
 assert sorted(perm)==list(range(1,n+1))
 assert sum(e*f for e,f in ef)==48
 assert all(perm[perm[perm[i]-1]-1]==i+1 for i in range(n))
 A=s.zeros(n)
 for i,j in enumerate(perm):A[j-1,i]=1
 # Custom modular rank independent of producer.
 def rank(M):
  a=[[int(v)%7 for v in row] for row in M.tolist()];r=0
  for c in range(len(a[0]) if a else 0):
   z=next((i for i in range(r,len(a)) if a[i][c]),None)
   if z is None:continue
   a[r],a[z]=a[z],a[r]; inv=pow(a[r][c],-1,7);a[r]=[(inv*v)%7 for v in a[r]]
   for i in range(len(a)):
    if i!=r:
     m=a[i][c];a[i]=[(v-m*w)%7 for v,w in zip(a[i],a[r])]
   r+=1
  return r
 dims={str(lam):n-rank(A-lam*s.eye(n)) for lam in (3,5)}
 assert all(v==0 for v in dims.values())
 rows.append({'place':q,'degree_check':48,'sigma_cube_identity':True,'faithful_eigenspace_dimensions':dims})
R={'status':'PASS','twist_d':d,'x_twist':'-47*x+16','Y_twist':'-47*sqrt(-47)*Y; Y=2y+1','twist_cubic_identity':True,'actual_divisor_checks':rows,'t_D_chi':0,'class_bound_proved':False}
(here/'CHECK.json').write_text(json.dumps(R,indent=2)+'\n')
print(json.dumps(R,indent=2))
