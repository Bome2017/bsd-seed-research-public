"""Independent exact integer/fraction checks of saved arithmetic tables."""
from pathlib import Path
from fractions import Fraction
import json, re, hashlib
ROOT=Path(__file__).resolve().parent.parent
def res(x,mod):
    x=Fraction(x)
    return x.numerator*pow(x.denominator,-1,mod)%mod
out=[]
for p,n,ap in [(7,4,-3),(31,3,-2)]:
    q=p**n;mod=p**(n-1)
    path=ROOT/f'outputs/655a1_p{p}_table{q}.gp'
    rows=json.loads(re.sub(r'(-?\d+/\d+)',r'"\1"',path.read_text()))
    assert len(rows)==(p-1)*p**(n-1)
    assert {a for a,j,s in rows}=={a for a in range(1,q) if a%p}
    assert all(pow(a,p-1,q)==pow(1+p,j*(p-1),q) for a,j,s in rows)
    sums=[sum(Fraction(s)*c for a,j,s in rows for c in [[1,j,j*(j-1)//2][k]]) for k in range(3)]
    alpha=ap%p
    for k in range(2,n+2):
        modulus=p**k
        alpha=(alpha-(alpha*alpha-ap*alpha+p)*pow(2*alpha-ap,-1,modulus))%modulus
    factor=(1-p*pow(alpha,-2,mod))*pow(alpha,-n,mod)%mod
    coeff=factor*res(sums[2],mod)%mod
    assert coeff%p==0 and coeff//p%p!=0
    expected={7:4*7+2*7**2,31:13*31}[p]
    assert coeff==expected
    # Reparametrizing the top principal-unit group by gamma^2 scales the
    # leading quadratic term by 1/4, because lower moments vanish mod mod.
    order=p**(n-1);inv2=pow(2,-1,order)
    alt=sum(Fraction(s)*((j*inv2%order)*(j*inv2%order-1)//2) for a,j,s in rows)
    altcoeff=factor*res(alt,mod)%mod
    assert res(sums[0],mod)==0 and res(sums[1],mod)==0
    assert altcoeff==coeff*pow(4,-1,mod)%mod
    assert altcoeff!=coeff
    out.append(dict(curve='655a1',p=p,n=n,rows=len(rows),sums=list(map(str,sums)),
       coefficient_residue=coeff,modulus=mod,normalized_coefficient_valuation=1,
       mismatched_generator_residue=altcoeff,input_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
result={'status':'PASS','grade':'exact checks on software-generated modular symbols; not an independent modular-symbol implementation','rows':out}
(ROOT/'outputs/FINITE_TABLE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
