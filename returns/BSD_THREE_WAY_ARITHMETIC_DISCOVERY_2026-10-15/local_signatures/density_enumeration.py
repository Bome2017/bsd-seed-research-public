from pathlib import Path
import itertools,json,importlib.util,hashlib
R=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('f3',R/'f3.py');f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
seal=R.parent/'incidence_review/JOINT_DENSITY_PREDICTIONS.md';binding=hashlib.sha256(seal.read_bytes()).hexdigest()
expected={(0,2):[1,32,48],(1,2):[73,608,48],(2,2):[4177,2336,48],(2,0):[81,0,0]};out=[]
for (r,s),pred in expected.items():
 counts=[0,0,0];d=r+s
 for a in itertools.product(range(3),repeat=2*d):
  M=[list(a[:d]),list(a[d:])];A=[row[:r]for row in M];k=f.rank(M)-f.rank(A);counts[k]+=1
 assert counts==pred and sum(counts)==3**(2*d)
 out.append({'r':r,'s':s,'rank_difference_counts':counts,'total':sum(counts),'conditional_densities':[f'{c}/{sum(counts)}'for c in counts]})
result={'status':'EXHAUSTIVE_F3_MATRIX_ENUMERATION_PASS','sealed_prediction_path':str(seal),'sealed_prediction_sha256':binding,'cases':out,'scope':'Exact finite algebra supporting the stated fixed-coefficient-prime Chebotarev deduction; not a statistical inference from the first24 scanned primes.'}
(R/'DENSITY_ENUMERATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
