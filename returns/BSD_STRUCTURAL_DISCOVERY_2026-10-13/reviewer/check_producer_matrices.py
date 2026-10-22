#!/usr/bin/env python3
"""Parse the exact printed matrices; do not trust the producer's rank fields.

This checks an accepted, arithmetic-error-free GP transcript.  Warnings about
the GP stack may be retained; any other GP diagnostic is a rejection.  It does
not prove class-group completeness or the original descent certificates.
"""
import argparse, hashlib, json, pathlib, re
from verify_filtration import check

def matrix(text):
    text=text.strip()
    if not (text.startswith('[') and text.endswith(']')):
        raise ValueError('not a bracketed matrix')
    text=text[1:-1].strip()
    if not text or text==';': return []
    rows=[]
    for row in text.split(';'):
        words=[x.strip() for x in row.split(',')]
        if not all(re.fullmatch(r'-?[0-9]+',x) for x in words):
            raise ValueError('noninteger in matrix')
        rows.append([int(x) for x in words])
    if len({len(x) for x in rows})!=1: raise ValueError('ragged matrix')
    return rows

def run(root):
    out=root/'probe.out'; err=root/'probe.err'
    s=out.read_text(); e=err.read_text()
    diagnostics=[line for line in e.splitlines() if line.strip()]
    if any('Warning: increasing stack size to ' not in line for line in diagnostics):
        raise ValueError('GP diagnostic other than retained stack-size warning')
    if s.splitlines()[-1]!='EXPERIMENT_COMPLETE':
        raise ValueError('missing final completion marker')
    def value(key):
        vals=[line.split('=',1)[1] for line in s.splitlines() if line.startswith(key+'=')]
        if len(vals)!=1: raise ValueError('missing or duplicate '+key)
        return vals[0]
    V=matrix(value('COMPLETE_VALUATIONS'))
    Vm=matrix(value('VALUATION_MOD3'))
    if Vm!=[[a%3 for a in row] for row in V]:
        raise ValueError('valuation reduction differs')
    Ub=matrix(value('UNRAMIFIED_KERNEL'))
    U=list(map(list,zip(*Ub))) if Ub else []
    C=matrix(value('CLASS3_MATRIX'))
    cyc_match=re.search(r'; CYCLIC=(\[[^\]]+\]);',s)
    if not cyc_match: raise ValueError('missing invariant factors')
    cyc=matrix(cyc_match.group(1))[0]
    raw_columns={}
    for line in s.splitlines():
        m=re.fullmatch(r'CLASS_COLUMN=([0-9]+); class=(\[[^\]]+\])~; ideal_cube_check=1',line)
        if m:
            i=int(m.group(1))
            if i in raw_columns: raise ValueError('duplicate class column')
            raw_columns[i]=matrix(m.group(2))[0]
    if sorted(raw_columns)!=list(range(1,len(U)+1)):
        raise ValueError('missing verified ideal-root class column')
    raw=list(map(list,zip(*(raw_columns[i] for i in sorted(raw_columns)))))
    d={'field':3,'ambient_dimension':4,
       'point_basis':[[1,0,0,0],[0,1,0,0]],
       'valuation_rows':V,'unramified_basis':U,'class_rows':C,
       'class_invariants':cyc,'raw_class_rows':raw}
    result=check(d)
    result['producer_binding']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in [out,err,root/'probe.gp']}
    result['producer_gp_diagnostics']=diagnostics
    result['class_group_scope']='Class-coordinate completeness remains at the retained BNF grade; this checker does not certify it.'
    return d,result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('producer_dir');p.add_argument('--out-dir',required=True);a=p.parse_args()
    d,r=run(pathlib.Path(a.producer_dir));target=pathlib.Path(a.out_dir)
    target.mkdir(parents=True,exist_ok=True)
    (target/'SEED_MATRIX_INPUT.json').write_text(json.dumps(d,indent=2)+'\n')
    (target/'SEED_MATRIX_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
