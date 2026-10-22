# Check and correction notes

- This was an adaptive discovery experiment following the prior panel. TWIST_PROTOCOL.md records the initial 60-case screen, capped 1000-case extension and subsequent S-class filter. It is same-session registration, not an external timestamp.
- The third S-class candidate, d=43737, supplied the control. Earlier point-index screens used floating height ratios only to nominate cases. The final index is verified by exact point equations and independent finite-field saturation certificates.
- The S-class script's final DONE row prints its loop variable d symbolically because that variable is local to the GP loop. Its completed counts are numeric and its FIELD_CANDIDATE/CLASS_CERTIFY rows contain d=43737 explicitly. The last symbolic field is not evidence of an arithmetic value.
- Intermediate script syntax/name errors were repaired before any numerical claims were admitted. The final exact GP proof output ends with DONE and has empty stderr. A missing polrootsrat call was replaced by exact extraction from the factored quadratic kernel polynomial.
- The n8/256MB and n6/1400MB numerator runs overflowed. Their logs contain no numerator and are excluded. The accepted fixed-4GB n5 run and its replay have empty stderr, numeric finite-precision output and matching saved values. PARI's zero exit code alone is not an acceptance criterion.
- The Python digit checker reads the actual saved J, regulator and Euler digits and computes Q afresh. The printed Q is only compared afterwards.
- The explicit Python group law uses short coordinates y'=y+1/2, including for reduction certificates. Its finite-field generator coordinates therefore refer to those short coordinates.
- The lower bound on Sha is not read from Q. The rank upper bound still relies on PARI's unconditional two-descent implementation. The finite-field checks independently establish 5-saturation, not a new implementation of two-descent.
- The point pairs are 5-saturated, not asserted to be a full global basis. A prime-to-5 index would change leading units by a unit square, but cannot change the measured excess valuation two.
- No ordinary seed theorem requiring full residual image is applied to this reducible-residual control. Its independent isogeny argument is specific to the control.
