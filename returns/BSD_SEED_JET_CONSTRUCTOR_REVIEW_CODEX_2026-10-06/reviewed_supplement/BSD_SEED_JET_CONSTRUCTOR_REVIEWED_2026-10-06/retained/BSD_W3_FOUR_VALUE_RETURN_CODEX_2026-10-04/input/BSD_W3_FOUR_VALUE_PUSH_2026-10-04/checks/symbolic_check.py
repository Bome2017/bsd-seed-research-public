#!/usr/bin/env python3
"""Exact rational polynomial identities, truncated only in T,S-degree <4.
No symbolic algebra dependency and no numerical substitutions for free symbols.
Variables: T,S,L,a,c,d,e. These checks do not prove the arithmetic functional equation.
"""
from fractions import Fraction as Q
import json

class P:
    def __init__(self, terms=None):
        self.t={m:Q(c) for m,c in (terms or {}).items() if c and m[0]+m[1]<4}
    def __add__(self, other):
        other=cast(other); d=self.t.copy()
        for m,c in other.t.items():d[m]=d.get(m,Q(0))+c
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({m:-c for m,c in self.t.items()})
    def __sub__(self, other):return self+-cast(other)
    def __rsub__(self, other):return cast(other)+-self
    def __mul__(self, other):
        other=cast(other);d={}
        for m,c in self.t.items():
            for n,b in other.t.items():
                v=tuple(x+y for x,y in zip(m,n))
                if v[0]+v[1]<4:d[v]=d.get(v,Q(0))+c*b
        return P(d)
    __rmul__=__mul__
    def __truediv__(self, other):return self*Q(1,other)
    def __pow__(self, n):
        assert isinstance(n,int) and n>=0
        out=cast(1)
        for _ in range(n):out=out*self
        return out
    def __eq__(self, other):return self.t==cast(other).t
    def substitute_s(self, value):
        out=cast(0)
        for m,c in self.t.items():
            v=list(m);v[1]=0
            out+=P({tuple(v):c})*(value**m[1])
        return out

def cast(x):return x if isinstance(x,P) else P({(0,)*7:Q(x)})
def var(i):
    m=[0]*7;m[i]=1
    return P({tuple(m):1})

T,S,L,a,c,d,e=[var(i) for i in range(7)]
Si=T-S+S*S-T*S+T*S*S-S**3
F=a*T*T-c*T*S+c*S*S+d*T**3+e*T*T*S+((1+L/2)*c-L*a/2-e)*T*S*S-(1+L/2)*c*S**3
assert F==(1+L*T/2-L*S)*F.substitute_s(Si)
zeta=(1+S)*(1-T/2+3*T*T/8-5*T**3/16)
zinv=(1+T/2-T*T/8+T**3/16)*(1-S+S*S-S**3)
assert zeta*zinv==1
Y=(zeta-zinv)/2
assert Y.substitute_s(Si)==-Y
H=(1+L*S/2-L*T/4)*F
A=a-c/4;B=c
C=d+e/4+c/8-L*a/8+L*c/16
D=-e+c/2-L*a/2-L*c/4
assert H==A*T*T+B*Y*Y+C*T**3+D*T*Y*Y
assert H.substitute_s(Si)==H
print(json.dumps({
 "status":"PASS", "coefficient_field":"exact rational numbers",
 "free_symbols":["L","a","c","d","e"],
 "checked":["functional equation to total degree three", "zeta inverse", "Y changes sign", "four coefficient formulas", "H invariance"],
 "scope":"algebra following the arithmetic functional equation, not a proof of source matching or nonvanishing"
},indent=2))
