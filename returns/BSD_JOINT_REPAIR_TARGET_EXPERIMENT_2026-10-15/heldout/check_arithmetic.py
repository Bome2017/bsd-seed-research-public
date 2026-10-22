#!/usr/bin/env python3
"""Independent standard-library replay of the newly generated arithmetic blocks.

This checks field/root/elliptic/cubic-symbol arithmetic, not global source
completeness, local Kummer images, or the primary descent theorem.
"""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))
def rat(x, q):
    if isinstance(x, int): return x % q
    a,b=x
    return a*pow(b,-1,q)%q
def ev(poly,x,q):
    v=0
    for a in reversed(poly): v=(v*x+rat(a,q))%q
    return v
def on(E,P,q):
    a1,a2,a3,a4,a6=E;x,y=P
    return (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6)%q==0
def add(E,P,Q,q):
    if P is None:return Q
    if Q is None:return P
    a1,a2,a3,a4,a6=E;x,y=P;z,t=Q
    if x==z and (y+t+a1*x+a3)%q==0:return None
    if x==z:
        assert P==Q
        den=(2*y+a1*x+a3)%q
        lam=(3*x*x+2*a2*x+a4-a1*y)*pow(den,-1,q)%q
    else:lam=(t-y)*pow((z-x)%q,-1,q)%q
    nu=(y-lam*x)%q
    xx=(lam*lam+a1*lam-a2-x-z)%q
    return (xx, (-(lam+a1)*xx-nu-a3)%q)

def check_source(folder):
    S=json.loads((folder/'source.json').read_text())
    B=json.loads((folder/'blocks.json').read_text())['blocks']
    E=S['model']; F=S['field']; sources=S['source_factors']
    assert len(E)==5 and len(F)==9 and F[-1]!=0 and len(B)==(60 if folder.name=='mirror_extension' else 12)
    counts={'blocks':0,'torsion_points':0,'source_symbols':0,'additivity_rows':0}
    for block in B:
        q=block['q']; roots=block['roots']; om=block['omega']
        assert prime(q) and q>10000 and q%3==1
        assert len(roots)==len(set(roots))==8
        assert all(ev(F,x,q)==0 for x in roots)
        assert pow(om,3,q)==1 and om!=1
        pts=[tuple(ev(c,x,q) for c in S['torsion_point']) for x in roots]
        assert pts==[tuple(P) for P in block['points']]
        assert len(set(pts))==8
        for P in pts:
            assert on(E,P,q) and add(E,add(E,P,P,q),P,q) is None
        chars=[]
        for x in roots:
            row=[]
            for factors in sources:
                value=1
                for poly,exponent in factors:
                    u=ev(poly,x,q);assert u!=0
                    value=value*pow(u,exponent,q)%q
                char=pow(value,(q-1)//3,q)
                row.append([1,om,om*om%q].index(char))
            chars.append(row)
        assert chars==block['characters']
        triples=[]; rows=[]
        for i,P in enumerate(pts):
            for j in range(i,8):
                Q=add(E,P,pts[j],q)
                if Q is None:continue
                k=pts.index(Q);triples.append([i,j,k])
                rows.append([(a+b-c)%3 for a,b,c in zip(chars[i],chars[j],chars[k])])
        assert len(triples)==32 and triples==block['triples'] and rows==block['rows']
        counts['blocks']+=1;counts['torsion_points']+=8
        counts['source_symbols']+=8*len(sources);counts['additivity_rows']+=32
    old=ROOT/'rejected_polynomial_json'/folder.name/'blocks.jsonl'
    if folder.name=='mirror_extension':
        assert (ROOT/'mirror389/source.json').read_bytes()==(folder/'source.json').read_bytes()
    else:assert old.read_bytes()==(folder/'blocks.jsonl').read_bytes(), 'Serialization repair changed arithmetic'
    return dict(label=folder.name,status='EXACT_ARITHMETIC_REPLAY_PASS',**counts,
      source_sha256=sha(folder/'source.json'),blocks_sha256=sha(folder/'blocks.json'),
      matrix_sha256=sha(folder/'matrices.json'),first_primes=[b['q'] for b in B])

def main():
    receipt=json.loads((ROOT/'PRODUCTION_RECEIPT.json').read_text())
    out=[check_source(ROOT/r['label']) for r in receipt]
    if (ROOT/'mirror_extension').exists():out.append(check_source(ROOT/'mirror_extension'))
    totals={k:sum(r[k] for r in out) for k in ['blocks','torsion_points','source_symbols','additivity_rows']}
    result=dict(status='INDEPENDENT_ARITHMETIC_REPLAY_PASS',scope=__doc__,totals=totals,sources=out)
    (ROOT/'ARITHMETIC_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],**totals}))

if __name__=='__main__': main()
