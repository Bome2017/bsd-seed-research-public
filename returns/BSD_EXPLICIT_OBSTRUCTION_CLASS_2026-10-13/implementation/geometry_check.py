from sage.all import QQ, PolynomialRing, matrix
from itertools import combinations
import json
from pathlib import Path
p=Path(__file__).parent
m=json.loads((p/'FISHER_MODEL.json').read_text())
P=PolynomialRing(QQ,names=['x0','x1','x2','x3','x4']); xs=P.gens()
qs=[P(q) for q in m['signed_pfaffians']]
J=matrix(P,[[q.derivative(x) for x in xs] for q in qs])
minors=[J.matrix_from_rows_and_columns(a,b).det() for a in combinations(range(5),3) for b in combinations(range(5),3)]
charts=[]
for j,x in enumerate(xs):
    I=P.ideal(qs+minors+[x-1]); gb=I.groebner_basis(); ok=(len(gb)==1 and gb[0]==1)
    print('SMOOTH_CHART',j,ok,flush=True);assert ok;charts.append({'chart':j,'singular_ideal_groebner_basis':['1']})
(p/'GEOMETRY_CHECK.json').write_text(json.dumps({'char0_nonsingular':True,'charts':charts,'hilbert_polynomial':m['hilbert_polynomial']},indent=2)+'\n')
