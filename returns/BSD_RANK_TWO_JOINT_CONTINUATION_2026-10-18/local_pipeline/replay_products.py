"""Independent integer-product replay of the actual saved local rows.

This checks assembly and ranks, not the idealstar generator construction.
The split evaluator itself computes residues directly from exact field packs.
"""
import json,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
args=sys.argv[:];sys.argv=['evaluate_split.py']
from evaluate_split import rank
sys.argv=args

def main():
    root=Path(sys.argv[1]).resolve()
    C=json.loads((root/'compact_source.json').read_text());K=C[5]
    weights=[6,2,3,1,5,4];n=len(K);m=len(K[0]);out=[]
    S=json.loads((root/'split_rows.json').read_text())
    for precision in (8,9):
        a=json.loads((root/f'formal_{precision}.json').read_text())
        assert a[1]==[6,1] and a[8][a[0]-1]==[-2,-3]
        assert all(sum(a[3][j]*K[j][c] for j in range(n))==0 for c in range(m))
        raw=[[sum(row[j]*K[j][c] for j in range(n))%7 for c in range(m)] for row in a[4]]
        projected=[[sum(row[6*k+(j+t)%6]*weights[t]*K[6*k+j][c]
                       for k in range(n//6) for j in range(6) for t in range(6))%7
                    for c in range(m)] for row in a[4]]
        assert raw==a[5] and projected==a[6] and any(a[9])
        joint=[[x for q in S['rows'] for x in q['additivity_defects'][j]]+
               [row[j] for row in projected] for j in range(m)]
        out.append({'precision':precision,'raw_local_rank':rank(raw),
                    'chi_local_rank':rank(projected),'joint_rank':rank(joint),
                    'valuation_cancellation':True,'formal_point_binding':True,
                    'nonpower_calibration':True})
    result={'source_columns':m,'checks':out,'split_ranks':[
        {'q':q['q'],'raw':rank(q['raw_unit_logs']),
         'chi':rank(q['chi_unit_logs']),'defect':rank(q['additivity_defects'])}
        for q in S['rows']],
        'no_completeness_or_global_power_assertion':True}
    (root/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
