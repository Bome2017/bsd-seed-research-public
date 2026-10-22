"""Independent nodal-torus check; no elliptic addition routine is used."""
import json
from pathlib import Path
rows=[]
for p,q,n,c in [(19,2243,2242,1),(59,2243,2242,1),(487,5843,5844,2)]:
    roots=[r for r in range(q) if (r**3-r*r-66020924*r-65074271436)%q==0 and (3*r*r-2*r-66020924)%q==0]
    assert len(roots)==1
    r=roots[0]; s=(1-2*r)%q; delta=(r-s)%q
    assert delta and (-(r*r*s)+65074271436)%q==0
    def mul(z,w):
        a,b=z; x,y=w
        return ((a*x+delta*b*y)%q,(a*y+b*x)%q)
    def power(z,e):
        ans=(1,0)
        while e:
            if e&1: ans=mul(ans,z)
            z=mul(z,z); e//=2
        return ans
    legendre=pow(delta,(q-1)//2,q)
    assert n==(q-1 if legendre==1 else q+1)
    for name,x,y in [('P1',-3031,327384),('P2',-2394,281520)]:
        x%=q; y%=q
        assert (y*y-(x-r)**2*(x-s))%q==0 and x!=r
        t=y*pow(x-r,-1,q)%q
        denominator=(t*t-delta)%q
        assert denominator
        # z=(t+j)/(t-j), j^2=delta, in Fq[j]/(j^2-delta).
        z=((t*t+delta)*pow(denominator,-1,q)%q,2*t*pow(denominator,-1,q)%q)
        assert power(z,n)==(1,0)
        witness=power(z,c*(n//p))
        assert witness!=(1,0) and power(witness,p)==(1,0)
        rows.append(dict(p=p,q=q,point=name,node=r,delta=delta,split=legendre==1,torus_value=z,witness=witness,nonzero_local_class=True))
Path(__file__).with_name('ETA_INDEPENDENT_TORUS.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'controls':len(rows),'all_pass':True}))
