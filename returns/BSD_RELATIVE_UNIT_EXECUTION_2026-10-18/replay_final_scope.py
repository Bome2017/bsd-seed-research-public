"""Read-only replay of final saved-table selection and matrix elimination."""
from pathlib import Path
import ast, json
r=Path(__file__).resolve().parent
s=r/'source'
rows=[ast.literal_eval(line) for line in (s/'norm_trials.gp').read_text().splitlines() if line.strip()]
ideals=json.loads((s/'IDEAL_NORMS.json').read_text())
scored=[]
for row in rows:
    num=abs(row[5]); den=ideals[row[3]-1][1]
    assert num % den == 0
    scored.append([num//den]+row)
assert sorted(scored)[:20]==json.loads((s/'DIAGNOSTIC_TOP20.json').read_text())
a=json.loads((r/'FINAL_ANTI_MATRIX.json').read_text())
assert len(a)==127 and all(len(row)==20 for row in a)
a=[[z%7 for z in row] for row in a]
rank=0
for j in range(20):
    pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
    if pivot is None: continue
    a[rank],a[pivot]=a[pivot],a[rank]
    inv=pow(a[rank][j],-1,7)
    a[rank]=[inv*z%7 for z in a[rank]]
    for i in range(len(a)):
        if i!=rank:
            scalar=a[i][j]
            a[i]=[(x-scalar*y)%7 for x,y in zip(a[i],a[rank])]
    rank+=1
assert rank==20
print(json.dumps({'selection':'TOP20_PASS','matrix':[127,20],'rank_mod7':rank,'integer_kernel_dimension':0,'scope':'Saved table and matrix replay only; no factor or candidate generation.'}))
