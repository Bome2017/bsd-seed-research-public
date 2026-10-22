from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))
def count(q):
    return 1+sum(1 if (r:=(x*x*x-22735*x*x+106272484*x)%q)==0 else 1+ (1 if pow(r,(q-1)//2,q)==1 else -1) for x in range(q))
R=[]
for q in range(7,243):
    if not prime(q):continue
    n=count(q)
    if n%5==0:R.append({'q':q,'order':n,'a_q':q+1-n,'valuation_5':next(i for i in range(1,10) if n%5**(i+1))})
expected=[7,29,31,53,67,73,113,137,149,151,181,223,229]
assert [r['q'] for r in R]==expected
# Each good q in the range with rational five-torsion contributes two
# negation pairs, except full rational E[5] would contribute twelve.
# Here v5(order)=1 for each except13? assert directly.
assert all(r['valuation_5']==1 for r in R)
out={'status':'PASS','method':'independent integer quadratic-residue point counts','degree_one_split_pair_count':2*len(R),'rows':R,'scope':'degree-one primes independently checked; absence of higher-degree pairs from exact maximal-order ideal computation'}
(ROOT/'POINT_COUNT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','degree_one_split_pairs':2*len(R),'rational_primes':len(R)}))
