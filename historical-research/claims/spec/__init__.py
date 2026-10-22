"""The claim specification: the single editable source for claims/claims.json and claims/CLAIM_INDEX.md."""
from .part1_core import CLAIMS as _p1
from .part2_bridges import CLAIMS as _p2
from .part3_stops import CLAIMS as _p3
from .part4_open import CLAIMS as _p4
from .common import GRADES, KINDS, STOP_KINDS, REVIEWS

CLAIMS = _p1 + _p2 + _p3 + _p4
