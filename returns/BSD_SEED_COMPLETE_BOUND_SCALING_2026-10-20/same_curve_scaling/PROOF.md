# Same-curve p=3 to p=5 scaling: proved components and missing class term

Fix E=1664n1: y²=x³-4x+16, and p=5. This is the same rank-two curve whose complete three-descent source was bounded by two in the preceding return. It is not the original seed.

## Arithmetic source

`construct.gp` forms the primitive resultant of the five-division polynomial and w²/4−x³+4x−16, proves that it is irreducible of degree 24, reduces it with an explicit binding, and recovers an actual nonzero point T of order 5. The scalar automorphism sigma is checked to send T to2T and to have order 4. The maximal-order field has signature(4,10), discriminant 2^68 5^23 13^16. The retained general descent construction uses the sigma=2 character. Its inverse also has the same valuation and unit dimensions below; the evaluated incidence norm uses the former convention consistently.

The irreducible degree 24 point polynomial in particular gives irreducible E[5]. The multiplicative place13 has minimal discriminant valuation1, furnishing a transvection. These are compatible with the full-image setting, but the arithmetic unit rank argument below needs only the actual torsion orbit, scalar action and complex-conjugation action. `source_checks.gp` also verifies that Phi5 stays irreducible over A, hence the source has no fifth roots of unity.

## Entire character-unit space

Dirichlet's unit representation is the augmentation-zero permutation representation on archimedean places. On E[5]−{0}, complex conjugation has eigenvalues +1 and−1. Its archimedean orbits consist of four singleton real embeddings and ten conjugate pairs. Scalar2 acts on the resulting fourteen places; its eigenvalue 2 and3 spaces modulo5 both have dimension 3. The trivial augmentation line affects neither faithful character. This gives the full character-unit dimension 3 without assuming that any computed unit list is fundamental.

The BNF computation supplies thirteen compact candidate units. Their provisional fundamentalness is NOT used. For all332 distinct compact factors, exact principal-ideal factorizations and HNF reconstructions were obtained. Their exponent matrix E and divisor matrix D satisfy D E=0 over the integers across291 prime ideals. Every candidate is therefore an actual unit, independently of GRH and independently of class certification. `replay_units.gp` refactors and reconstructs every factor ideal and all exponents separately.

The projector e_chi has coefficients (4,2,1,3) on 1,sigma,sigma²,sigma³ modulo5. Integral exponent representatives define actual projected units. At eight completely split rational primes, the evaluator recovers all 24 torsion points, verifies their elliptic group law and sigma permutation, and computes the fifth-power residue of every projected unit. The resulting aggregate source residue matrix has rank 3. Thus the candidates actually span the full three-dimensional character-unit space modulo fifth powers; no missing-unit index can add a fourth dimension.

For each affine coset P+<T> not containing zero, the multiplicative incidence norm is the product over its five points. Adding their residue logarithms gives exact norm-residue rows. At q=6101 already the rank is1; the total eight-prime stack also has rank 1. A nonzero residue cannot be a fifth power in the target, so the actual norm map has rank at least1. Consequently its kernel on the ENTIRE character-unit space has dimension at most3−1=2. The measured residue rank does not prove the exact algebraic norm rank is only1; the asserted conclusion is an upper bound, not equality.

## Entire allowed valuation sector

S={2,5,13}. The exact source prime decompositions and scalar actions are:

*2: one prime, (e,f)=(24,1), fixed;
*5: two primes, (4,1),(5,4), both fixed;
*13: three primes, (5,2),(5,2),(1,4), scalar action exchanges the first two and fixes the third.

These permutation matrices have no eigenvalue 2 or3 over F5. Thus the entire faithful divisor module above S vanishes. A faithful S-virtual unit is an ordinary virtual unit. This is an exact action on primitive prime ideals, not geometric orbit counting. No uncomputed valuation sector is omitted.

## Class contribution remains explicit

The exact ordinary sequence gives

    0 -> (O_A^*/O_A^{*5})^chi -> A(empty,5)^chi -> Cl(A)[5]^chi -> 0.

Combining the unit bound and zero valuation sector gives the rigorous full-source bound

    dim ker(u on A(S,5)^chi) <= 2 + dim Cl(A)[5]^chi.

The class term is NOT set to zero. BNF returns a provisional cyclic class group C3; `bnfcertify(B,1)` did not complete before its 110-second alarm. Its exit code0 is not success: stderr contains the alarm, the completion marker and certificate are absent, and the wrapper rejects the run.

Under GRH, or if an unconditional class quotient certificate later verifies the provisional C3 presentation, the class term is zero and the complete bound is at most2. No such unconditional certification is claimed here. Since this term could be positive without that input, this run does not establish the complete bound or a new Sha-vanishing theorem at 5.

## What the scaling experiment learned

The same curve at coefficient 3 had complete ordinary unit-kernel dimension 1 plus class contribution 1. At coefficient 5, the full faithful unit-kernel upper bound is2 and the valuation sector is zero; the provisional class data suggest zero contribution, but its proof is the remaining step. It is therefore false to report that unit growth alone already destroyed the small bound. It is also false to report that the small bound has been established at 5. The same-curve test isolates a concrete class-certification bottleneck after the full unit and valuation sectors have been controlled.

This establishes no scaling theorem, no original-seed bound and no FIN conclusion.
