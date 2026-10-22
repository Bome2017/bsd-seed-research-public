from pathlib import Path
import ast,json
R=Path(__file__).resolve().parent
for name in ['1913b1','28042a1']:
 p=R/name;bs=ast.literal_eval((p/'blocks.gpdata').read_text().replace(']~',']'));out=[];off=0
 for q,rt,pt,om,chi,tr,rows in bs:
  out.append(dict(prime=q,row_start_zero_based=off,row_end_exclusive=off+len(rows),roots=rt,torsion_points=pt,cubic_root=om,cubic_residue_rows=chi,triples_zero_based=tr,rows=rows));off+=len(rows)
 x=json.loads((p/'matrices.json').read_text());assert [r for b in out for r in b['rows']]==x['additivity']
 for b in out:
  for (i,j,k),r in zip(b['triples_zero_based'],b['rows']):assert r==[(a+d-c)%3 for a,d,c in zip(b['cubic_residue_rows'][i],b['cubic_residue_rows'][j],b['cubic_residue_rows'][k])]
 x['additivity_blocks']=out;(p/'matrices.json').write_text(json.dumps(x,indent=2)+'\n');(p/'additivity_blocks.json').write_text(json.dumps(out,indent=2)+'\n')
print('BOTH_BLOCK_EXPORTS_PASS')
