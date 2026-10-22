#!/usr/bin/env python3
"""Exact elementary features; never label an unresolved prime as nonzero Sha."""
import json
from pathlib import Path
ps=[5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
solved={5,7,11,13,17,19,23,29,31,37,41,43,47,83}
rows=[]
for p in ps:
    n=1
    for x in range(p):
        t=(x*x*x-22735*x*x+106272484*x)%p
        n+=1 if t==0 else 2 if pow(t,(p-1)//2,p)==1 else 0
    direct=1+sum((y*y-x*x*x+22735*x*x-106272484*x)%p==0 for x in range(p) for y in range(p))
    assert n==direct
    rows.append({'p':p,'ap':p+1-n,'order':n,'ordinary':(p+1-n)%p!=0,
                 'mod4':p%4,'mod3':p%3,
                 'status':'retained_vanishing' if p in solved else 'unresolved_in_located_record',
                 'nonanomalous':n%p!=0})
out={'scope':'Exact elementary features, not a classifier; unresolved is not nonzero Sha. Status to be checked against coverage ledger.','rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PRIME_FEATURES_PASS',len(rows))
