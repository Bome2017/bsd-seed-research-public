#!/usr/bin/env python3
"""Optional numerical area cross-check; requires mpmath.

The independent path integrates the two periods. The comparison interval comes
from the prior handoff's unchanged rational-AGM implementation in reference/.
Quadrature agreement is numerical evidence, not a new certified quadrature.
"""
from pathlib import Path
import importlib.util
import json
import sys
import mpmath as mp

mp.mp.dps = 110
sd = mp.sqrt(91790289)
e1, e2 = (22735 + sd)/2, (22735 - sd)/2
A, B, C = e1-e2, e1, e2
O1 = mp.quad(lambda t: 2/mp.sqrt(A*mp.sin(t)**2+B*mp.cos(t)**2),
             [0,mp.pi/4,mp.pi/2])
O2 = mp.quad(lambda t: 2/mp.sqrt(C*mp.cos(t)**2+B*mp.sin(t)**2),
             [0,mp.pi/4,mp.pi/2])
value = 4*mp.pi**2/(O1*O2)
path = Path(__file__).parent/'reference'/'normalize_from_balls.py'
spec = importlib.util.spec_from_file_location('prior_normalizer',path)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
ball,_ = m.period_area_multiplier(-22735,106272484)
lo = mp.mpf(ball.lo.numerator)/ball.lo.denominator
hi = mp.mpf(ball.hi.numerator)/ball.hi.denominator
out = {'scope':'Independent numerical quadrature compared with replayed rational-AGM interval',
       'decimal_precision':110,'mpmath_version':mp.__version__,
       'Omega1_quadrature':str(O1),'Omega2_quadrature':str(O2),
       'multiplier_quadrature':str(value),
       'replayed_AGM_interval_display':m.decimal_enclosure(ball,25),
       'quadrature_inside_replayed_interval':bool(lo<=value<=hi),
       'actual_seed_kernel_value_computed':False}
assert out['quadrature_inside_replayed_interval']
print(json.dumps(out,indent=2))
