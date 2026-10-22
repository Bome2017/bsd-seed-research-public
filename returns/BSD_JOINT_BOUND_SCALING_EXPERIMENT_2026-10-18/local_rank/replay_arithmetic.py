"""Replay exact products, ranks, local branch binding and the saved small minor.

This does not re-run idealstar or the sibling unit authentication.
"""
import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R))
from evaluate_split import rank

def det_mod(A,p):
    a=[row[:] for row in A];d=1
    for j in range(len(a)):
        k=next(i for i in range(j,len(a)) if a[i][j]%p)
        if k!=j:a[j],a[k]=a[k],a[j];d=-d
        pivot=a[j][j]%p;d=d*pivot%p
        for i in range(j+1,len(a)):
            z=a[i][j]*pow(pivot,-1,p)%p
            a[i]=[(x-z*y)%p for x,y in zip(a[i],a[j])]
    return d%p

def replay_local(source,filename):
    C=json.loads((R/source).read_text());K=C[5];weights=[6,2,3,1,5,4]
    n=len(K);m=len(K[0]);a=json.loads((R/filename).read_text())
    vals=a[3];logs=a[4]
    assert a[1]==[6,1] and a[8][a[0]-1]==[-2,-3]
    assert all(sum(vals[j]*K[j][c] for j in range(n))==0 for c in range(m))
    raw=[[sum(row[j]*K[j][c] for j in range(n))%7 for c in range(m)] for row in logs]
    assert raw==a[5]
    proj=[[sum(row[6*k+(j+t)%6]*weights[t]*K[6*k+j][c] for k in range(n//6) for j in range(6) for t in range(6))%7 for c in range(m)] for row in logs]
    assert proj==a[6] and any(a[9])
    return {'file':filename,'raw_rank':rank(raw),'chi_rank':rank(proj),'point_branch_checked':True,'valuation_cancellation_checked':True,'nonpower_calibration_nonzero':True}

def main():
    count=1+sum((y*y+y-x*x*x+x*x+10*x+20)%7==0 for x in range(7) for y in range(7))
    assert count==10
    checks=[]
    for n in (8,9):
        checks.append(replay_local('compact_units_batch1.json',f'formal_branch_{n}.json'))
        checks.append(replay_local('compact_units_11a1.json',f'11a1_formal_{n}.json'))
    S=json.loads((R/'11a1_split_rows.json').read_text())
    assert S['curve']==[0,-1,1,-10,-20]
    for n in (8,9):
        F=json.loads((R/f'11a1_formal_{n}.json').read_text())[6]
        for q in S['rows']:
            rows=[q['additivity_defects'][j]+[F[i][j] for i in range(len(F))] for j in range(26)]
            assert rank(rows)==4 and rank(q['additivity_defects'])==3 and rank(q['chi_unit_logs'])==4
    minor=json.loads((R/'11a1_MINOR_CERTIFICATE.json').read_text())
    assert det_mod(minor['matrix_mod7'],7)==minor['det_mod7']==6
    q=S['rows'][0];F=json.loads((R/'11a1_formal_8.json').read_text())[6]
    columns=[j-1 for j in minor['unit_columns_1based']]
    rows=[]
    for meta in minor['row_definitions']:
        if meta['type']=='split_additivity':
            i=q['points'].index(meta['point']);assert q['labels'][i]==meta['point_label']
            rows.append([q['additivity_defects'][j][i] for j in columns])
        else:rows.append([F[meta['coordinate_1based']-1][j] for j in columns])
    assert rows==minor['matrix_mod7']
    result={'point_count_11a1_mod7':count,'local_product_replays':checks,'actual_joint_rank_11a1_p7':4,'minor_det_mod7':6,'independent_unit_dimension_bound':4,'class_completeness_claim':False}
    (R/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
