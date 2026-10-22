from pathlib import Path
import json
R=Path(__file__).resolve().parent
rows=[]
for p in [5,7,11,13,17,19,23,29,31,53,83,101]:
 d=(p*p-1)//4;m=(p*p-1)//2
 # Exact integer form of q^[d(1−1/(4p))]/m>p^4.
 ok=pow(4547,d*(4*p-1))>pow(m*pow(p,4),4*p)
 assert ok
 rows.append({'p':p,'relative_unit_rank':d,'base_degree':m,'bare_expression_exceeds_p_to_4':ok,'class_group_computed':False})
(R/'SCALING_CHECK.json').write_text(json.dumps({'status':'PASS','proof':'see SCALING_TEST.md for all p>=5, finite rows only cross-check exact exponent arithmetic','rows':rows},indent=2)+'\n')
print('SCALING_EXPRESSION_CHECK_PASS')
