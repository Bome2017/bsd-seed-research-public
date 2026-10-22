#!/usr/bin/env python3
"""Exact finite universal-measure module. No Hida symbol or BSD bound is computed.

Coordinates m[i,j] = integral binom(X,i) z^j dmu, X=log_<1+p>(x),
for i+j<4, modulo p**(4-i-j). T=(1+p)^weight-1 is NOT T/p.
Use the tame-trivial component and right row action (x,y) -> (x,y) gamma.
"""
from __future__ import annotations
from math import comb, factorial
from typing import Sequence

ORDER=4
COORDS=tuple((i,d-i) for d in range(ORDER) for i in range(d+1))
NODES=tuple((i,d-i) for d in range(ORDER) for i in range(d+1))

def is_prime(n:int)->bool:
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def binomial_mod(x:int,i:int,m:int)->int:
    a=1
    for j in range(i): a=a*(x-j)%m
    return a*pow(factorial(i),-1,m)%m

def principal_log(v:int,p:int,digits:int)->int:
    """log(v/omega(v))/log(1+p) mod p^digits, via exact digit lifting."""
    if v%p==0: raise ValueError('The argument must be a p-adic unit')
    mod=p**(digits+1); g=1+p
    u=pow(v,p-1,mod); k=0
    for n in range(digits):
        residual=u*pow(pow(g,k,mod),-1,mod)%mod
        step=p**(n+1)
        if (residual-1)%step: raise ArithmeticError('Invalid dlog precision')
        slope=((pow(g,p**n,mod)-1)//step)%p
        digit=((residual-1)//step)*pow(slope,-1,p)%p
        k+=digit*p**n
    if pow(g,k,mod)!=u: raise ArithmeticError('Dlog verification failed')
    return k*pow(p-1,-1,p**digits)%p**digits

def invert_matrix(a:Sequence[Sequence[int]],mod:int,p:int)->list[list[int]]:
    n=len(a)
    r=[[x%mod for x in row]+[int(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        piv=next((i for i in range(j,n) if r[i][j]%p),None)
        if piv is None: raise ArithmeticError('Matrix has no unit pivot')
        r[j],r[piv]=r[piv],r[j]
        iv=pow(r[j][j],-1,mod); r[j]=[x*iv%mod for x in r[j]]
        for i in range(n):
            if i!=j:
                v=r[i][j];r[i]=[(x-v*y)%mod for x,y in zip(r[i],r[j])]
    return [row[n:] for row in r]

def moments(X:int,z:int,p:int)->list[int]:
    return [binomial_mod(X,i,p**(ORDER-i-j))*pow(z,j,p**(ORDER-i-j))%p**(ORDER-i-j) for i,j in COORDS]

def transformed_moments(X:int,z:int,gamma:Sequence[int],p:int)->list[int]:
    a,b,c,d=gamma
    if a%p==0 or c%p or a*d-b*c==0:
        raise ValueError('Expected gamma in Sigma_0(p)')
    mod=p**(ORDER+1); v=(a+c*z)%mod
    xx=(X+principal_log(v,p,ORDER))%p**ORDER
    zz=(b+d*z)*pow(v,-1,mod)%mod
    return moments(xx,zz,p)

class JetModule:
    def __init__(self,p:int):
        if p<17 or not is_prime(p): raise ValueError('This implementation is scoped to primes p >= 17')
        self.p=p; self.mod=p**ORDER
        self.precisions=[p**(ORDER-i-j) for i,j in COORDS]
        self.evaluation=[[binomial_mod(x,i,self.mod)*pow(z,j,self.mod)%self.mod for i,j in COORDS] for x,z in NODES]
        self.inv=invert_matrix(self.evaluation,self.mod,p)
    def action(self,gamma:Sequence[int])->list[list[int]]:
        values=[transformed_moments(X,z,gamma,self.p) for X,z in NODES]
        rows=[]
        for out,(i,j) in enumerate(COORDS):
            mod=self.precisions[out]
            row=[sum(self.inv[k][r]*values[r][out] for r in range(len(NODES)))%mod for k in range(len(COORDS))]
            for k,coeff in enumerate(row):
                if coeff*self.precisions[k]%mod:
                    raise ArithmeticError('Action violates weighted precision')
            rows.append(row)
        return rows
    def apply(self,A:Sequence[Sequence[int]],m:Sequence[int])->list[int]:
        if len(m)!=len(COORDS): raise ValueError('Ten moment slots are required')
        return [sum(x*y for x,y in zip(row,m))%mod for row,mod in zip(A,self.precisions)]

def multiply(g:Sequence[int],h:Sequence[int])->tuple[int,int,int,int]:
    a,b,c,d=g;e,f,k,l=h
    return (a*e+b*k,a*f+b*l,c*e+d*k,c*f+d*l)

def four_functional(p:int,w:int,s:int,source:dict[int,Sequence[int]])->int:
    """Unit-scaled source functional, NOT source authentication or a BSD certificate.
    source[a] must be the actual common-frame Xi({infinity}-{a/p}) jet.
    Only accepts the four retained (w,s) pairs. Alpha_w^{-1} is omitted (a unit).
    """
    if p<17 or not is_prime(p): raise ValueError('Expected a prime >=17')
    if (w,s) not in {(3,2),(3,3),(4,3),(4,4)}: raise ValueError('Not a retained W3 pair')
    if set(source)!=set(range(1,p)): raise ValueError('All p-1 nonzero residue cusps are required')
    mod=p**4;t=(pow(1+p,w,mod)-1)%mod;out=0
    for a in range(1,p):
        vals=source[a]
        if len(vals)!=10: raise ValueError('Each cusp requires ten moment slots')
        omega=pow(a,p**4,mod)
        inner=0
        for h in range(min(s,3)+1):
            mh=sum(pow(t,i,mod)*vals[COORDS.index((i,h))] for i in range(4-h))%mod
            inner+=comb(s,h)*pow(a,s-h,mod)*pow(-p,h,mod)*mh
        out+=pow(omega,-s,mod)*inner
    return ((-1)**s*out)%mod

if __name__=='__main__':
    import json
    print(json.dumps({'slots':list(COORDS),'p_adic_digits_per_value':sum(4-i-j for i,j in COORDS),
                      'scope':'LOCAL_COEFFICIENT_MODULE_ONLY','seed_symbol_computed':False},indent=2))
