# Direct unit-source repairs at coefficient seven

Status: **FINITE_SOURCE_SEARCH_COMPLETED; NO_NONTRIVIAL_CHARACTER_UNIT_OBTAINED**.

This is a changed-source continuation of the actual degree-48 389a1 torsion field. It does not retry BNF or use a class group, Selmer dimension, or known Sha value.

## 1. Direct integral norm scan

The pre-registered 2000 candidates consist of 47 nonconstant maximal-order basis vectors, 21 small shifts of the reduced defining generator, and 1932 ordered small sums/differences of basis vectors. `norm_rows.gp` records every candidate and exact field norm. None has norm +1 or -1. A separate script recomputes all 2000 norms and agrees. The smallest absolute norm is

    2051073672649 = 751^2 * 1907^2,

attained by basis vector 4 minus basis vector 5. The producer took 3.675 s and independent norm replay 3.421 s.

This finite failure says nothing about the existence of other units.

## 2. Repair using a genuine S-unit

One candidate has norm supported only at 7 and 389: basis vector 2, whose norm is -7^15. Since it is integral, it is a genuine S-unit supported only above 7.

The actual prime decompositions and scalar-3 action are computed, not inferred from geometric incidence matrices. Above 7 the pairs (e,f) are

    (6,1), (7,3), (7,3),

and the scalar permutation is [1,3,2]. Consequently sigma^2-1 annihilates the entire prime-divisor module above 7 INTEGRALLY. A mere zero divisor modulo7 would not be enough to prove ordinary unitness.

Thus sigma^2(a)/a is an actual ordinary unit. The principal ideals are checked equal. However the exact field calculation gives sigma^2(a)=a, so this quotient is 1. In particular this candidate has zero projection to the faithful character sigma ->3 mod 7: its scalar orbit has order dividing 2, while that character has order 6.

Above 389 the actual scalar permutation is [3,6,2,5,1,4,8,7]; its faithful character divisor dimension is 1. That computation does not eliminate the prime389 contribution in general.

## 3. Repair without a support restriction

For the same 2000 integral candidates, test whether sigma^j(a) and a generate the same principal ideal, for j=1,2,3. Literal sigma^j(a)=+/-a cases are excluded first. If equality of principal ideals held in a nontrivial case, the quotient would be an authenticated ordinary unit regardless of its norm's prime support. This is an actual arithmetic source repair, not an assumption that every norm-one quotient is a unit.

All2000 candidates were tested; no nontrivial ordinary unit quotient was obtained. The entire scalar matrix is computed in the integral basis. `ideal_scan_rows.gp` records every candidate outcome. The scan took 41.422 s. No norm residue rank was then assigned to an empty candidate family.

A coding inefficiency in the first matrix construction recomputed each column once per entry. It was stopped at 28.896 s and preserved in `rejected_repeated_matrix_entry/`; caching the 48 columns changed only implementation, not the mathematical search. A separate initial parse error from using GP's reserved name I is also preserved. Both consumed times are included in the budget accounting.

`REPAIR_REPLAY.gp` independently verifies the 48 scalar columns, the actual permutation above 7, and the exact triviality of the repaired S-unit quotient. It does not repeat the entire2000-candidate principal-ideal search.

## 4. Effect

No p=7 ordinary-unit norm rank, complete-unit kernel improvement, class-supported bound, or seed conclusion follows from these finite searches. The known relevant ambient unit dimension is 4, but this return has not lowered it by an arithmetic norm witness.

The useful distinction is exact: the only small S-supported candidate was obtained, but its faithful character component is zero; abandoning small support and cancelling actual ideals also found no candidate within the specified finite set. This does not prove a general unit construction impossible.

The prior `p7_arithmetic` checkpoint remains sealed. No BNF retry, class computation, publication or external job was performed. FIN, ORDER9 and Q36 remain unchanged.
