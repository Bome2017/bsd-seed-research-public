from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
D,E=json.loads((R/'UNIT_DIVISOR_MATRIX.json').read_text())
assert len(D)==116 and len(D[0])==144 and len(E)==144 and len(E[0])==26
z=all(sum(a*b for a,b in zip(row,col))==0 for row in D for col in zip(*E))
assert z
result={'status':'PASS','divisor_rows':116,'distinct_factors':144,'unit_candidates':26,'integer_equations_checked':116*26,'all_exact_divisors_zero':True,'scope':'integer exponent arithmetic; actual factors and complete principal ideals authenticated separately by GP','matrix_sha256':hashlib.sha256((R/'UNIT_DIVISOR_MATRIX.json').read_bytes()).hexdigest()}
(R/'UNIT_MATRIX_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
