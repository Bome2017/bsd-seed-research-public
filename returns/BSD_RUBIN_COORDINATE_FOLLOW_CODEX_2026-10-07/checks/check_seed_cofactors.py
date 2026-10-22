"""Exact new local-log calculation; consumes, but does not recompute, saved heights."""
from fractions import Fraction as F
from pathlib import Path
import json, re, hashlib

ROOT = Path(__file__).resolve().parents[1]
A2, A4, A6 = -1, -66020924, -65074271436
POINTS = [(F(-3031), F(327384)), (F(-2394), F(281520))]

def on_curve(P):
    return P is None or P[1]**2 == P[0]**3 + A2*P[0]**2 + A4*P[0] + A6

def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x,y=P; X,Y=Q
    if x == X and y == -Y: return None
    slope = (Y-y)/(X-x) if x != X else (3*x*x+2*A2*x+A4)/(2*y)
    z = slope*slope-A2-x-X
    R = (z, -y+slope*(x-z))
    assert on_curve(R)
    return R

def multiply(n, P):
    Q=None
    while n:
        if n&1: Q=add(Q,P)
        P=add(P,P); n//=2
    return Q

def residue(x, modulus):
    return x.numerator * pow(x.denominator,-1,modulus) % modulus

def vp(n,p):
    if n==0: return None
    r=0
    while n%p==0: n//=p; r+=1
    return r

def series_integer(s,p):
    s=s.split('O(')[0].strip().rstrip('+').strip()
    total=0
    for term in s.split('+'):
        term=term.strip()
        # Full match: no eval and no silent omissions.
        m=re.fullmatch(r'(?:(\d+)\*)?'+str(p)+r'(?:\^(\d+))?',term)
        if m: total+=int(m[1] or 1)*p**int(m[2] or 1)
        elif term.isdigit(): total+=int(term)
        else: raise ValueError(term)
    return total

def height_values(p):
    if p==5:
        text=(ROOT/'evidence/c9_sage_output.txt').read_text()
        line=next(l for l in text.splitlines() if l.startswith('S1 seed h11 ='))
        return [series_integer(re.search(r'h'+ij+r' = (.*?)(?: ;|$)',line)[1],p)
                for ij in ['11','12','22']]
    text=(ROOT/'evidence/reg17_pari_2173.txt').read_text()
    return [series_integer(next(l.split(' = ',1)[1] for l in text.splitlines()
                    if l.startswith(key)),p)
            for key in ['MIN h(Q1) =','MIN <Q1,Q2> =','MIN h(Q2) =']]

def point_count(p):
    return 1+sum((y*y-x*x*x-A2*x*x-A4*x-A6)%p==0
                 for x in range(p) for y in range(p))

rows=[]
for p in [5,17]:
    n=point_count(p)
    assert n%p != 0
    logs=[]; point_controls=[]
    for P in POINTS:
        assert on_curve(P)
        Q=multiply(n,P)
        repeated=None
        for _ in range(n): repeated=add(repeated,P)
        assert repeated==Q
        t=-Q[0]/Q[1]
        assert vp(t.numerator,p)-vp(t.denominator,p)>=1
        # log(t)=t modulo p^2 in the integral formal group, p>=5.
        value=residue(t/F(p*n),p)
        Q2=multiply(2*n,P)
        assert residue((-Q2[0]/Q2[1])/F(2*p*n),p)==value
        logs.append(value)
        point_controls.append({'t_nP_numerator':str(t.numerator),
                               't_nP_denominator':str(t.denominator)})
    a,b,c=height_values(p)
    assert a%p==b%p==c%p==0
    # log(1+p)/p = 1 modulo p, so these are gamma-height entries mod p.
    h=[(a//p)%p,(b//p)%p,(c//p)%p]
    cofactor=[(h[2]*logs[0]-h[1]*logs[1])%p,
              (h[0]*logs[1]-h[1]*logs[0])%p]
    det=(a*c-b*b)%(p**5)
    det_valuation=vp(det,p)-2
    assert cofactor != [0,0]
    rows.append({'p':p,'point_count':n,'log_over_p_mod_p':logs,
                 'height_gamma_mod_p':[[h[0],h[1]],[h[1],h[2]]],
                 'adj_height_times_log_over_p_mod_p':cofactor,
                 'det_height_gamma_valuation':det_valuation,
                 'det_height_gamma_unit_mod_p':(det//p**(det_valuation+2))%p,
                 'cofactor_content_valuation':1,
                 'point_controls':point_controls})
assert rows[0]['log_over_p_mod_p']==[0,2]
assert rows[0]['adj_height_times_log_over_p_mod_p']==[1,4]
assert rows[0]['det_height_gamma_valuation']==0
assert rows[1]['log_over_p_mod_p']==[2,13]
assert rows[1]['adj_height_times_log_over_p_mod_p']==[16,6]
assert rows[1]['det_height_gamma_valuation']==1
out={'grade':'exact rational point arithmetic plus downstream reuse of retained height outputs',
     'height_engine_reexecuted':False,'kato_coefficient_evaluated':False,
     'new_primary_result':False,'results':rows}
print(json.dumps(out,indent=2))
