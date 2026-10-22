#!/usr/bin/env python3
"""Portable downstream checks only; does not re-certify source theorems/BNF/Arb."""
from pathlib import Path
import hashlib,importlib.util,json,subprocess,sys,tempfile,shutil
R=Path(__file__).resolve().parent
manifest=R/'MANIFEST.sha256'
if manifest.exists():
 for line in manifest.read_text().splitlines():
  h,n=line.split('  ',1);p=R/n
  assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==h,n
spec=importlib.util.spec_from_file_location('compatibility_review',R/'class_lift_review/check_compatibility.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.ROOT=R
mirror=m.inspect(R/'class_lift/mirror389/matrices.json');hensel=m.hensel()
assert mirror['class_fibers'][1]['common_repair_count']==0
assert mirror['short_joint_certificate']['restricted_row_on_units_then_class']==[0,0,0,0,1]
q=subprocess.run([sys.executable,str(R/'plectic_kolyvagin/new_twist/recheck.py')],check=True,capture_output=True,text=True)
twists=json.loads(q.stdout);assert [x['valuation_at_5'] for x in twists['twists']]==[1,1]
with tempfile.TemporaryDirectory() as d:
 p=Path(d);(p/'experiment').mkdir();shutil.copyfile(R/'experiment/independent_points.py',p/'experiment/independent_points.py')
 z=subprocess.run([sys.executable,'experiment/independent_points.py'],cwd=p,check=True,capture_output=True,text=True)
 points=json.loads(z.stdout);assert points['determinant_mod5']==3
print(json.dumps({'status':'PORTABLE_DOWNSTREAM_CHECK_PASS','manifest_checked':manifest.exists(),'mirror_unit_corrections':mirror['unit_corrections_enumerated'],'mirror_valuation_zero_elements':mirror['valuation_zero_classes_enumerated'],'short_class_exclusion_row':[0,0,0,0,1],'hensel_samples':hensel['samples'],'hensel_minimum_margin':hensel['minimum_margin'],'exact_twist_sums':[x['pure_imaginary_eigencycle_factor'] for x in twists['twists']],'rational_point_determinant_mod5':points['determinant_mod5'],'scope':'Checks saved arithmetic, rational point group law and source bindings; not BNF certification, modular-symbol construction, source theorem verification or BSD proof'},indent=2))
