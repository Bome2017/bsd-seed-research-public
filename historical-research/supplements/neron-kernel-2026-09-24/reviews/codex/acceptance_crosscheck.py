"""Independent direct-integer oracle for the supplied interval acceptance routine."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json
import time

ROOT = Path(__file__).resolve().parent
source = ROOT/'input/BSD_NERON_DENOMINATOR_INDEPENDENT_CHECK_2026-09-24/independent_checks.py'
spec = importlib.util.spec_from_file_location('review_checks', source)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
start = time.process_time()
count = 0
for prime in [5, 11, 13, 17, 23]:
    for x in range(-64, 65):
        for y in range(x, 65):
            lo, hi = F(x, 4), F(y, 4)
            integers = [k for k in range(-17, 18) if lo <= k <= hi]
            if not integers:
                expected = 'EMPTY_LATTICE_INCONSISTENCY'
            elif all(k % prime for k in integers):
                expected = 'UNIT_WITNESS_IF_MEMBERSHIP'
            elif len(integers) == 1:
                expected = 'DIVISIBLE_WITNESS_INCONCLUSIVE_FOR_SHA'
            else:
                expected = 'INCONCLUSIVE'
            got = m.interval_decision(lo/m.B_THETA, hi/m.B_THETA, prime)['status']
            if got != expected:
                raise RuntimeError((prime, lo, hi, got, expected))
            count += 1
rejected = 0
for prime in [2, 3, 7, 9, 15, 2243, 4547, 5843]:
    try:
        m.interval_decision(F(0), F(1), prime)
    except ValueError:
        rejected += 1
    else:
        raise RuntimeError(('inadmissible prime accepted', prime))
print(json.dumps({'status': 'PASS', 'direct_integer_oracle_cases': count,
    'inadmissible_primes_rejected': rejected, 'cpu_seconds': time.process_time()-start,
    'scope': 'Acceptance arithmetic only; no seed evaluation or source-proof verification'}, indent=2))
