"""Exact controls for the reduction of the seed minimal model at the bad odd primes
(producer script; pure integers). For each q it reports the singular point, the shape of the
tangent cone (node split/non-split or cusp) and #E_ns(F_q) obtained by counting the
non-singular points of the reduced curve (Euler's criterion, all x in F_q)."""
import json
a2,a4,a6=-1,-66020924,-65074271436
F=lambda x:x**3+a2*x*x+a4*x+a6
def leg(a,q):
    a%=q
    if a==0: return 0
    return 1 if pow(a,(q-1)//2,q)==1 else -1
res={}
for q in [3,2243,4547,5843]:
    sing=[x for x in range(q) if F(x)%q==0 and (3*x*x+2*a2*x+a4)%q==0]
    x0=sing[0]
    # expand F(x0+u) = u^3 + A u^2 + B u + C ; at singular point B=C=0 mod q
    A=(3*x0+a2)%q; B=(3*x0*x0+2*a2*x0+a4)%q; C=F(x0)%q
    if A==0: kind="cusp (additive)"
    else: kind="node, split" if leg(A,q)==1 else "node, non-split"
    affine=sum(1+leg(F(x),q) for x in range(q))
    ns=affine-1+1   # remove the singular point, add the point at infinity
    res[q]={"singular_x":x0,"B,C (must be 0)":[B,C],"quadratic_coeff_A":A,"type":kind,"#E_ns(F_q)":ns}
print(json.dumps(res,indent=1))
