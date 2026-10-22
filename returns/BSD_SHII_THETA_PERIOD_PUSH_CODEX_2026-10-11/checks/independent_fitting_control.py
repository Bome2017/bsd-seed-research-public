"""Exact abstract Fitting controls, not seed computations."""
from itertools import combinations, permutations
import json

def parity(q):
    return (-1)**sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))

def fitting_exponents(a):
    # Entries are (coefficient, p exponent, T exponent).
    zero=None
    matrix=[[zero for _ in range(6)] for _ in range(4)]
    for row,col,entry in [(0,0,(1,0,1)),(1,1,(1,0,1)),(2,2,(1,a,0)),(2,3,(1,0,1)),(3,4,(1,a,0)),(3,5,(1,0,1))]:matrix[row][col]=entry
    out=[]
    for cols in combinations(range(6),4):
        poly={}
        for perm in permutations(range(4)):
            entries=[matrix[i][cols[perm[i]]] for i in range(4)]
            if any(x is None for x in entries):continue
            coefficient=parity(perm)
            for entry in entries:coefficient*=entry[0]
            powers=(sum(x[1] for x in entries),sum(x[2] for x in entries))
            poly[powers]=poly.get(powers,0)+coefficient
        poly={str(k):v for k,v in poly.items() if v}
        if poly:out.append({'columns':cols,'minor':poly})
    powers={key for item in out for key in item['minor']}
    assert powers=={str((2*a,2)),str((a,3)),str((0,4))}
    return out

if __name__=='__main__':
    examples={str(a):fitting_exponents(a) for a in [1,2,3,17]}
    print(json.dumps({'status':'PASS','scope':'abstract presentation maximal minors only; not seed Selmer computation','examples':examples},indent=2))
