"""Recompute valuations and quotient from raw saved p-adic digits, not Q field."""
import re,json
from pathlib import Path
p=5
s=Path('outputs/candidate43737_replay.out').read_text()
fields=next(x[len('VALUES ['):-1] for x in s.splitlines() if x.startswith('VALUES [')).split(', ')
def parse(x):
 m=re.fullmatch(r'(.+) \+ O\(5\^(\d+)\)',x);assert m,x
 n=int(m[2]);v=0
 for t in m[1].split(' + '):
  z=re.fullmatch(r'(?:(\d+)\*)?5(?:\^(\d+))?',t)
  if z:v+=int(z[1] or 1)*5**int(z[2] or 1)
  else:assert t.isdigit();v+=int(t)
 return {'residue':v%5**n,'precision_exponent':n}
def val(n):
 if n==0:return None
 k=0
 while n%5==0:k+=1;n//=5
 return k
keys=['J','R_scalar','L2_derivative_conversion','H_U','ordinary_Euler','printed_Q']
d=dict(zip(keys,map(parse,fields)))
for a in d.values():a['valuation']=val(a['residue'])
J=d['J'];R=d['R_scalar'];ep=d['ordinary_Euler'];n=min(J['precision_exponent']-R['valuation'],R['precision_exponent']-R['valuation'],ep['precision_exponent']);mod=5**n
q=(J['residue']//5**R['valuation'])*pow((R['residue']//5**R['valuation'])*ep['residue']*4,-1,mod)%mod
assert n==3 and q==25
assert d['printed_Q']['residue']%mod==q
assert d['J']['valuation']==4 and d['R_scalar']['valuation']==2
assert d['L2_derivative_conversion']['valuation']==2 and d['H_U']['valuation']==0
assert '(4*5^2 + O(5^3))*x^2' in s
assert not Path('outputs/candidate43737_replay.err').read_text()
result={'p':5,'digits':d,'recomputed_Q':{'residue':q,'precision_exponent':n},'difference':2,'Q_over_25_mod5':q//25,'direct_series_agrees_to_mod125':True,'interpretation':'finite computation for explicit 5-saturated point pair; not an exact Sha order'}
Path('outputs/NUMERICAL_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
