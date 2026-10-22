# Complete-source norm experiment, resumed 2026-10-17

Use the already computed 389a1 degree-24 field and actual units; no new BNF.
After the exact primitive divisor computation, every scalar norm-kernel
class has zero valuations modulo 5. The ordinary virtual-unit space includes
the class-supported quotient. Its class term is zero only conditional on the
uncertified BNF class computation; keep this condition explicit.

Construct the residual scalar-character projection of actual units. Test
independence by finite-field evaluations, so unit completeness at 5 can be
proved without trusting a fundamental-unit index. Apply actual affine-line
norm products to all projected unit columns. A nonzero norm row gives an
upper bound on the complete unit kernel; combined with class control this
bounds the entire global source, rather than a supplied Selmer subspace.

Predeclared bounds: one export from cached BNF <=60 seconds, then split-prime
search below 100000 and finite-field norm evaluation <=90 seconds, 1GiB.
If necessary, one syntax/convention repair is allowed without expanding the
arithmetic search. Do not infer class absence from the unit calculation.
No seed point, Sha value, or previously known norm-kernel dimension is input.

Success: exact independent residue rank and nonzero norm rank, with the
resulting upper dimension and source grade. No endpoint change is presumed.
