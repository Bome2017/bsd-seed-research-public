# Basis-pair pilot: scoped code/output review

Date: 2026-10-22. This note reviews the producer and saved result; it does not independently regenerate all norms.

Read `source_recovery/basis_unit_scan.gp`, `BASIS_UNIT_RESULT.gp`, the receipt, and stderr. The finite candidate count is exactly

`24 + binomial(24,2) * 2 * 4 = 2232`.

The candidates are the 24 maximal-order basis elements and, for each i<j, `c*b_i+d*b_j` with c in {1,2} and d in {-2,-1,1,2}. Linear independence of the integral basis makes these records distinct. This is a finite additive maximal-order source family; it differs from the prior torsion-coordinate multiplicative and relative ideal-cycle families.

For an admitted candidate the code requires exact field norm +/-1, verifies integrality of the element and inverse, and verifies both integrality and exact norm-one identity for `u/tau(u)`. Thus a numerical lattice calculation or provisional class number is not used for admission. The scalar involution and field polynomial bindings are checked.

The saved result contains precisely the constant 1 and no non-torsion relative unit. Exit code, completion marker and empty stderr agree. The finite scan therefore supplies no new unit input. It does not exclude larger coefficients, three-term combinations, products whose nonzero divisors cancel, or other arithmetic producers. In particular, this result is not a theorem that the whole unit group has rank zero.

No class bound, residue-saturation certificate, or endpoint result follows. No computational replay is claimed by this review.
