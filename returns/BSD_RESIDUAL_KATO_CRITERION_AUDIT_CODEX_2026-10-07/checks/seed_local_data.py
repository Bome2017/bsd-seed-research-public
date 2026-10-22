import json
from pathlib import Path
b2,b4,b6=-4,-132041848,-260297085744
b8=4*(-1)*(-65074271436)-(-66020924)**2
c4=b2*b2-24*b4
c6=-b2**3+36*b2*b4-216*b6
disc=-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
assert c4**3-c6**2==1728*disc
assert disc==2**8*3**2*2243*4547**3*5843**2
def val(n,q):
 k=0
 while n and n%q==0:k+=1;n//=q
 return k
rows=[]
for q in [2,3,2243,4547,5843]:
 d={"q":q,"v_delta":val(disc,q),"v_c4":val(c4,q),"v_j":3*val(c4,q)-val(disc,q)}
 if q in [3,2243,5843]:
  assert c4%q
  eps=pow(-c6%q,(q-1)//2,q)
  eps=1 if eps==1 else -1
  d.update(split_sign=eps,euler_numerator=q-eps,inertia_monodromy_index=val(disc,q))
 else:
  assert d["v_j"]>=0
  d.update(local_input="retained additive potentially good reduction; prime-to-p inertia for p>=5")
 rows.append(d)
assert [r["split_sign"] for r in rows if "split_sign" in r]==[-1,1,-1]
assert 2242==2*19*59
assert 5844==2**2*3*487
count=1+sum((y*y-(x*x*x-x*x-66020924*x-65074271436))%5==0 for x in range(5) for y in range(5))
assert count==8
out={"status":"PASS","c4":c4,"c6":c6,"discriminant":disc,"rows":rows,"E_F5":count,"additional_p_ge_5_local_exclusions":[19,59,487],"scope":"Exact seed invariants, split signs, factorization and p=5 count; no derivative or Sha computation"}
print(json.dumps(out,indent=2))
