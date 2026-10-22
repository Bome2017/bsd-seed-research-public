# Actual coefficient-seven continuation: exact field reached, arithmetic-unit stage timed out

Status: **ACTUAL_FIELD_COMPLETED; NO_P7_UNIT_OR_CLASS_BOUND_COMPUTED**.

This continuation follows the previous actual p=5 norm calculation, on the same rank-two control 389a1. It is not a seed calculation and is not a geometric mock norm test.

## Exact arithmetic completed

For E=[0,1,1,-2,0], the resultant of the seven-division polynomial with the equation in w=2y+1 has degree 48 and is irreducible over Q. In its quotient field the code reconstructs x, y, verifies the curve equation and [7]T=0, and constructs the scalar-3 automorphism from [3]T. Its order is exactly6. The resultant/point stage took 0.996 s.

The reduced defining polynomial, its binding to w, the universal point, the scalar-3 map and an nfinit maximal-order representation were saved in 23.885 s. The signature is (6,21), and the discriminant is

    -7^47 * 389^36.

The exact curve checks give Delta=389, a_389=1 and a_7=-5. Thus the multiplicative prime389 has discriminant valuation 1 and supplies a nontrivial transvection on E[7]. The irreducible torsion-point polynomial implies irreducibility of E[7], and with the standard transvection subgroup argument and cyclotomic determinant this is the full-image setting of the retained character-unit formula. The relevant ordinary character-unit dimension is 4. No full-image conclusion is needed to claim the literal field identities themselves.

`check_exact.gp` independently rechecks the irreducible polynomial, recovered point, both scalar maps, exact order 6, reduction binding and saved number-field/local identities. It passes in 1.535 s. It does not rerun the maximal-order computation; that remains the exact nfinit producer input.

## The bounded source computation did not finish

One `bnfinit(F,1)` attempt was allowed, with a 117 s internal alarm and 120 s wall cap. It reached the internal alarm before any `bnf.bin`, class presentation or compact-unit output was saved. Peak observed RSS was 432,558,080 bytes. The raw stderr records the alarm. GP exits with code0 after this interactive error, so the process exit code is NOT a success certificate; absence of the required stage markers/output is authoritative.

No BNF retry, class certification, actual unit authentication, incidence norm evaluation, or residue-rank claim followed. The prewritten `export.gp` and `split_primes.gp` were NOT executed. Total wall time of the four arithmetic processes was 143.478 s, below the 360 s contract cap.

## Effect on the bounding experiment

The p=5 result is not yet extended to p=7. Four is an ambient ordinary-unit dimension, not a new improved norm-kernel bound. No p=7 unit norm rank, ordinary class bound, or class-supported norm bound has been computed. In particular, the previous p=5 nonzero norm witness cannot be reduced modulo 7 to create a witness here.

The outcome is a reproducible computational checkpoint, not a mathematical obstruction to extending the method. An independently constructed unit family could still be evaluated in this exact field without another BNF attempt; that would be a different arithmetic source and would require its own unitness proof. The present record makes no claim that such a family spans the complete character-unit lattice.

FIN, ORDER9, Q36 and seed-prime coverage are unchanged.
