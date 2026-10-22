"""Exact arithmetic consequence of retained R.6/R.7; no seed L-value computation."""
from fractions import Fraction
import json

q_lo = Fraction("35.99427")
q_hi = Fraction("36.00573")
torsion_order = 2
tamagawa_product = 16
bsd_multiplier = Fraction(tamagawa_product, torsion_order**2)
sha_lo, sha_hi = q_lo / bsd_multiplier, q_hi / bsd_multiplier
integers = [n for n in range(sha_lo.numerator // sha_lo.denominator,
                           sha_hi.numerator // sha_hi.denominator + 2)
            if sha_lo < n < sha_hi]
assert bsd_multiplier == 4
assert sha_lo == Fraction("8.9985675")
assert sha_hi == Fraction("9.0014325")
assert integers == [9]
assert Fraction("35.929604") > 0
print(json.dumps({
    "grade": "EXACT_ARITHMETIC_FROM_RETAINED_INPUTS",
    "q_open_interval": [str(q_lo), str(q_hi)],
    "bsd_q_per_sha_order": str(bsd_multiplier),
    "conditional_sha_order_open_interval": [str(sha_lo), str(sha_hi)],
    "integers_in_interval": integers,
    "retained_second_derivative_interval_excludes_zero": True,
    "new_seed_certificate": False,
    "large_certificate_replay_performed": False,
}, indent=2) + "\n", end="")
