"""Exact comparison from producer digits, not their printed quotient fields."""
from pathlib import Path
import re,json

def parse(s,p=5):
    s=s.replace('O(5)', 'O(5^1)')
    if s.startswith('O('): return (0,int(re.search(r'5\^(\d+)',s)[1]))
    m=re.fullmatch(r'(.+) \+ O\(5\^(\d+)\)',s);assert m,s
    n=int(m[2]);a=0
    for term in m[1].split(' + '):
        t=re.fullmatch(r'(?:(\d+)\*)?5(?:\^(\d+))?',term)
        if t:a+=int(t[1] or 1)*5**int(t[2] or 1)
        else:assert term.isdigit();a+=int(term)
    return (a%5**n,n)
def val(a):
    if not a:return None
    v=0
    while a%5==0:a//=5;v+=1
    return v

def record(path,C):
    s=Path(path).read_text();assert s.rstrip().endswith('DONE')
    assert not Path(str(path).replace('.out','.err')).read_text()
    fields=next(x[8:-1] for x in s.splitlines() if x.startswith('VALUES ['))
    ds=list(map(parse,fields.split(', ')))
    J,R,L,H,E,Q=ds; vj=val(J[0]);vr=val(R[0]);vc=val(C); ve=val(E[0]);assert ve==0
    # Enough relative precision to divide through R, Euler and C safely.
    if vj is None:
        assert L[0]==0 and Q[0]==0
        return {'status':'LOWER_BOUND_ONLY','J':J,'L2':L,'HU':H,
                'L2_valuation_at_least':L[1],'HU_valuation':val(H[0]),
                'Q_valuation_at_least':J[1]-vr-vc,
                'interpretation':'zero residue is not an exact zero or an exact valuation'}
    qv=vj-vr-vc;n=min(J[1]-vj,R[1]-vr,E[1])+qv
    assert qv>=0 and n>qv
    mod=5**n
    numerator=(J[0]//5**vj)*5**qv
    denominator=(R[0]//5**vr)*E[0]*(C//5**vc)
    recomputed=numerator*pow(denominator,-1,mod)%mod
    assert recomputed==Q[0]%mod
    series=next(x for x in s.splitlines() if x.startswith('SERIES '))
    direct=re.search(r'\(([^()]+ \+ O\(5\^\d+\))\)\*x\^2',series)
    assert direct,series
    d=parse(direct[1]);assert (d[0]-L[0])%5**min(d[1],L[1])==0
    return {'digits':dict(zip(['J','Rscalar','L2conversion','HU','Euler','printedQ'],ds)),
      'direct_L2':d,'valuations':{'L2':val(d[0]),'HU':val(H[0]),'C':vc,'Q':qv},
      'recomputed_Q':{'residue':recomputed,'precision_exponent':n}}

A=record('outputs/partner_A.out',20)
F=record('inputs/candidate43737_replay.out',4)
assert (F['direct_L2'][0]-5*A['direct_L2'][0])%125==0
assert (F['digits']['HU'][0]-A['digits']['HU'][0])%5**8==0
assert F['recomputed_Q']['residue']==25 and A['recomputed_Q']['residue']==1
result={'d43737':{'A':A,'F':F,'numerator_factor5_to_available_precision':True,'determinants_equal_mod5power8':True,'quotient_factor25_to_available_precision':True}}
new=Path('outputs/combined329233_chunked.out')
if new.exists() and new.read_text().rstrip().endswith('DONE'):
    result['d329233']=record(new,4)
new8=Path('outputs/combined329233_n8.out')
if new8.exists() and new8.read_text().rstrip().endswith('DONE'):
    result['d329233_n8']=record(new8,4)
Path('outputs/DIGIT_COMPARISON.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
