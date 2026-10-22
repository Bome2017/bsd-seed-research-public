#!/usr/bin/env python3
"""Replay the reviewed historical checker, redirecting its sole output write.

This verifies existing inputs and logs. It does not recompute coefficient
witnesses or the finite L-series sum. The historical output field named
fresh_recombination_identical compares two OLD logs; see separate combine
receipt for any recombination performed in this review.
"""
from pathlib import Path
import hashlib,json,sys
cert=Path(sys.argv[1]).resolve(); out=Path(sys.argv[2]).resolve()
source=cert/'review_completion.py'; original=source.read_text()
old='(R/"COMPLETION_REVIEW.json").write_text'
new='(OUT/"HOST_METADATA_REPLAY.json").write_text'
assert original.count(old)==1
modified=original.replace(old,new)
# Keep __file__ at the historical source so all read paths retain their meaning.
exec(compile(modified,str(source),'exec'),{'__file__':str(source),'__name__':'__main__','OUT':out})
(out/'HOST_METADATA_REPLAY_ADAPTATION.json').write_text(json.dumps({
 'original_script':str(source),'original_script_sha256':hashlib.sha256(original.encode()).hexdigest(),
 'sole_change':{'from':old,'to':new},'historical_certificate_files_modified':False,
 'scope':'Hash, identity, count and historical-log replay; not a fresh full numerical sum'},indent=2)+'\n')
