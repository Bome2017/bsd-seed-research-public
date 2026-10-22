#!/usr/bin/env python3
"""Independent scalar arithmetic on two saved seed evaluation blocks."""
from pathlib import Path
import ast, json
R=Path(__file__).resolve().parent.parent
C=json.loads((R/'local_signatures/seed3/coordinates.json').read_text())
blocks,_=ast.literal_eval((R/'local_signatures/seed3/scan.gpdata').read_text().replace(']~',']'))
rows=[]
for block in blocks:
    q=block[0]
    if q not in (811,2767): continue
    M=block[4]; lam=[1,1,0,0,0,0,0,0]
    src=[sum(lam[i]*M[i][j] for i in range(8))%3 for j in range(15)]
    pts=[sum(src[i]*C['points'][i][j] for i in range(15))%3 for j in range(2)]
    known=[sum(src[i]*C['known'][i][j] for i in range(15))%3 for j in range(4)]
    assert pts==[0,0]
    assert known==([0,0,0,1] if q==811 else [0,0,1,2])
    rows.append({'prime':q,'root_weights':lam,'source_row':src,'point_values':pts,'known_values':known})
assert len(rows)==2
M=[z['known_values'][2:] for z in rows]
det=(M[0][0]*M[1][1]-M[0][1]*M[1][0])%3
assert det==2
out={'status':'SEED_TWO_SIGNATURE_ROWS_RECOMPUTED','rows':rows,'excess_minor_mod3':det,'scope':'Independent finite matrix arithmetic from saved residue matrices; not a regeneration of field evaluations or proof of full Selmer completeness.'}
(R/'secondary/SEED_SIGNATURE_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'determinant_mod3':det}))
