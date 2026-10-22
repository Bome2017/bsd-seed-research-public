#!/usr/bin/env python3
"""Recombine retained exact symbols, without recertifying their analytic origin."""
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path

root=Path(__file__).resolve().parent.parent
data=(root/'context/P17_MSL.txt').read_bytes()
receipt=json.loads((root/'context/P17_RETAINED_RECEIPT.json').read_text())
assert hashlib.sha256(data).hexdigest()==receipt['msl_sha256']
p,ell,g=17,103,5
symbols={}
for line in data.decode().splitlines():
    if not line.startswith('XB '):
        continue
    m=re.fullmatch(r'XB (\d+) plus \[.*?\] cand (-?\d+)/(\d+) contains 1 unique 1 minus \[.*?\] cand (-?\d+)/(\d+) contains 1 unique 1',line)
    assert m,line
    a,num,den,_,_=map(int,m.groups())
    assert a not in symbols
    symbols[a]=Fraction(num,den)
assert set(symbols)==set(range(1,ell))
assert all(symbols[a]==symbols[ell-a] for a in symbols)
logs={pow(g,j,ell):j%p for j in range(ell-1)}
assert len(logs)==ell-1
moments=[sum(symbols[a]*(1 if k==0 else logs[a] if k==1 else logs[a]*(logs[a]-1)//2) for a in symbols) for k in range(3)]
residues=[x.numerator*pow(x.denominator,-1,p)%p for x in moments]
assert list(map(str,moments))==[receipt['c0'],receipt['c1'],receipt['c2']]
assert residues==[0,0,7]
R=6
aell=ell+1-receipt['E_Fl_order']
w=residues[2]*pow((aell-2)*R%p,-1,p)%p
assert (aell,w)==(-2,16)
out={'status':'PASS','scope':'Exact recombination of retained identified symbols; corpus, intervals and Ota application not recertified',
     'symbols':len(symbols),'p':p,'ell':ell,'generator':g,'moments':list(map(str,moments)),
     'mod_p':residues,'regulator':R,'a_ell':aell,'w_17':w,
     'comparison_to_288':w==288%p,'global_rational_scalar_constructed':False}
(root/'checks/SYMBOL_RECOMBINATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
