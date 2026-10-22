"""Independent streamed row-basis check of complete-source dimensions over F3.

No saved kernel, rank, repair vector, or class-count output is used as input.
Number-field source completeness and validity of the constraint rows are retained.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
def rank(rows):
    basis = {}
    for original in rows:
        row = [int(x) % 3 for x in original]
        for j, x in enumerate(row):
            if not x:
                continue
            if j in basis:
                b = basis[j]
                for k in range(j, len(row)):
                    row[k] = (row[k] - x*b[k]) % 3
            else:
                inv = 1 if x == 1 else 2
                basis[j] = [(v*inv) % 3 for v in row]
                break
    return len(basis)

def multiply(a, b):
    columns = list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col)) % 3 for col in columns] for row in a]

rows = []
for path in sorted((ROOT/'class_contribution/inputs').glob('*.json')):
    d = json.loads(path.read_text())
    n = d['source_dimension']
    if 'field' in d:
        S = [[(v+(i==j)) % 3 for j,v in enumerate(row)] for i,row in enumerate(d['tau_matrix'])]
        V, U, A, L = d['valuation_rows'], d['unit_basis_rows'], d['additivity_rows'], d['local_rows']
        W = [row[:2] for row in d['actual_coordinates']]
    else:
        S, V, U, A, L, W = [d[k] for k in ['scalar','valuation','units','additivity','local','points']]
    assert rank(U) == len(U[0])
    result = {'label': path.stem}
    for label,R in [('global_necessary',S+A),('joint',S+A+L)]:
        full = n-rank(R)
        unramified = n-rank(R+V)
        unit = len(U[0])-rank(multiply(R,U))
        result[label] = {'unit':unit,'class':unramified-unit,
                         'valuation':full-unramified,'whole':full}
        assert all(v>=0 for v in result[label].values())
        if W:
            assert not any(x for row in multiply(R,W) for x in row)
    result['point_rank'] = rank(W)
    result['excess_upper'] = result['joint']['whole']-result['point_rank']
    rows.append(result)

other = {r['label']:r for r in json.loads((ROOT/'class_contribution/FILTERED_BOUNDS.json').read_text())['cases']}
for r in rows:
    o=other[r['label']]['joint']; j=r['joint']
    assert (j['unit'],j['class'],j['valuation'],j['whole']) == (o['admitted_units'],o['admitted_classes'],o['admitted_valuation_layer'],o['whole_source_upper'])
assert len(rows)==10
print(json.dumps({'status':'INDEPENDENT_SAVED_MATRIX_CHECK_PASS','cases':rows,
                  'scope':'Independent elimination of saved matrices; no fresh field, unit or class certification'},indent=2))
