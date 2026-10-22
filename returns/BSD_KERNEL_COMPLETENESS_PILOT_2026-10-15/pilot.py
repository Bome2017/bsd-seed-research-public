#!/usr/bin/env python3
"""Exact F3 whole-source and common-point experiments on bound saved matrices."""
from pathlib import Path
import hashlib
import itertools
import json

ROOT = Path(__file__).resolve().parent

def read(name):
    return json.loads((ROOT / 'inputs' / name).read_text())

def rr(a, n=None):
    n = len(a[0]) if a else (n or 0)
    b = [[int(x) % 3 for x in row] for row in a]
    assert all(len(row) == n for row in b)
    piv = []
    for j in range(n):
        k = next((i for i in range(len(piv), len(b)) if b[i][j]), None)
        if k is None:
            continue
        i = len(piv)
        b[i], b[k] = b[k], b[i]
        u = pow(b[i][j], -1, 3)
        b[i] = [x*u % 3 for x in b[i]]
        for k in range(len(b)):
            if k != i and b[k][j]:
                u = b[k][j]
                b[k] = [(x-u*y) % 3 for x,y in zip(b[k],b[i])]
        piv.append(j)
    return b[:len(piv)], piv

def rank(a):
    return len(rr(a)[1])

def transpose(a):
    return [list(x) for x in zip(*a)] if a else []

def mul(a,b):
    if not b:
        return [[] for _ in a]
    assert all(len(row)==len(b) for row in a)
    assert all(len(row)==len(b[0]) for row in b)
    bt = transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) % 3 for col in bt] for row in a]

def nullrows(a,n):
    b,piv = rr(a,n)
    out=[]
    for j in range(n):
        if j in piv:
            continue
        x=[0]*n
        x[j]=1
        for i,k in enumerate(piv):
            x[k]=-b[i][j] % 3
        out.append(x)
    return out

def annihilator(image, m):
    return nullrows(transpose(image),m)

def evaluate(rows, v):
    assert all(len(row)==len(v) for row in rows)
    return [sum(x*y for x,y in zip(row,v)) % 3 for row in rows]

def solve(a,b,n):
    ar=[row+[v] for row,v in zip(a,b)]
    r,piv=rr(ar,n+1)
    if n in piv:
        return None
    x=[0]*n
    for row,j in zip(r,piv):
        x[j]=row[-1]
    assert evaluate(a,x)==b
    return x

def detector(blocks, W, C):
    E=[row for b in blocks for row in b['source_residue_rows']]
    EW=mul(E,W)
    EC=mul(E,C)
    Q=annihilator(EW,len(E))
    new=mul(Q,EC)
    old=[]
    for b in blocks:
        e=b['source_residue_rows']
        old.extend(mul(annihilator(mul(e,W),len(e)),mul(e,C)))
    return {'primes':[b['prime'] for b in blocks],
            'old_rank':rank(old), 'common_point_rank':rank(new),
            'local_value_rank':rank(EC),'diagonal_point_rank':rank(EW),
            'old_kernel_basis':nullrows(old,len(C[0])),
            'common_kernel_basis':nullrows(new,len(C[0])),
            'common_signature_rows':rr(new)[0],
            'common_root_weight_rows':Q}

def main():
    for b in json.loads((ROOT/'INPUT_BINDINGS.json').read_text()):
        assert hashlib.sha256((ROOT/b['path']).read_bytes()).hexdigest()==b['sha256']
    full=[]
    for case in ['1913','389','433']:
        d=read(case+'_matrices.json'); n=d['source_dimension']; W=d['points']
        A=d['scalar']+d['additivity']+d['local']
        U=nullrows(A,n)
        scalar_local=nullrows(d['scalar']+d['local'],n)
        assert not any(any(r) for r in mul(A,W))
        row={'case':case,'source_dimension':n,'containing_kernel_dimension':len(U),
             'containing_kernel_basis':U,'point_dimension':rank(W),
             'candidate_quotient_dimension':len(U)-rank(W),
             'scalar_and_local_only_dimension':len(scalar_local),
             'without_local_conditions_dimension':len(nullrows(d['scalar']+d['additivity'],n))}
        if case=='1913':
            sig=read('1913b1_SIGNATURES.json')['fresh_primes']
            row['detector_kernels']=[]
            for primes in [[1867],[997],[1867,997]]:
                E=[r for b in sig if b['prime'] in primes for r in b['source_residue_rows']]
                Z=nullrows(A+E,n)
                row['detector_kernels'].append({'primes':primes,'dimension':len(Z),'basis':Z})
            # Exhaustive independent test directly against original arithmetic rows.
            found=[list(v) for v in itertools.product(range(3),repeat=n)
                   if not any(evaluate(A,v))]
            generated=sorted([[(a*U[0][j]+b*U[1][j])%3 for j in range(n)]
                              for a,b in itertools.product(range(3),repeat=2)])
            assert sorted(found)==generated
            row['exhaustive_vectors_tested']=3**n
            row['exhaustive_survivors']=len(found)
            # Known class list consulted only after reconstruction.
            known=read('1913b1_coordinates.json')['known']
            assert rank(U+transpose(known))==len(U)==rank(known)
            row['withheld_class_list_recovered']=True
        full.append(row)
    results={}
    for case in ['seed3','389a1','1913b1','28042a1']:
        co=read(case+'_coordinates.json'); sig=read(case+'_SIGNATURES.json')['fresh_primes']
        W,C=co['points'],co['known']
        # All pairs are a retrospective matrix comparison, not held-out arithmetic.
        pairs=[]
        for a,b in itertools.combinations(sig,2):
            x=detector([a,b],W,C)
            assert x['common_point_rank']>=x['old_rank']
            assert x['common_point_rank']<=rank(C)-rank(W)
            pairs.append({k:x[k] for k in ['primes','old_rank','common_point_rank']})
        blind=[b for b in sig if detector([b],W,C)['old_rank']==0]
        hist={}
        for x in pairs:
            key=str(x['old_rank'])+'->'+str(x['common_point_rank'])
            hist[key]=hist.get(key,0)+1
        results[case]={'point_dimension':rank(W),'supplied_class_dimension':rank(C),
                       'individually_blind_primes':[b['prime'] for b in blind],
                       'pair_rank_histogram':hist,'pair_count':len(pairs),'all_pairs':pairs,
                       'first_blind_prefixes':[detector(blind[:k],W,C) for k in [2,3,4] if len(blind)>=k]}
        if case=='seed3':
            chosen=[next(b for b in sig if b['prime']==q) for q in [1213,1543]]
            x=detector(chosen,W,C)
            x['point_repairs']=[]
            for b in chosen:
                EW=mul(b['source_residue_rows'],W)
                EC=mul(b['source_residue_rows'],C)
                solutions=[solve(EW,col,rank(W)) for col in transpose(EC)]
                x['point_repairs'].append({'prime':b['prime'],'columns_in_known_class_order':solutions})
            left,right=x['point_repairs']
            L=transpose(left['columns_in_known_class_order'])
            R=transpose(right['columns_in_known_class_order'])
            diff=[[(a-b)%3 for a,b in zip(l,r)] for l,r in zip(L,R)]
            x['repair_difference_matrix']=diff
            assert rank(diff)==x['common_point_rank']
            results[case]['sealed_pair']=x
    out={'grade':'EXACT_SAVED_MATRIX_EXPERIMENT_UNDER_RETAINED_ARITHMETIC',
         'full_source':full,'common_point':results,
         'scope':'Full source completeness retained only for certified controls; common-point results elsewhere apply to supplied true-class span. No new seed endpoint.'}
    (ROOT/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'full_source':full,'common_point':{k:{a:b for a,b in v.items() if a in ['pair_rank_histogram','pair_count','individually_blind_primes']} for k,v in results.items()},'seed_sealed_pair':results['seed3']['sealed_pair']},indent=2))

if __name__=='__main__':
    main()
