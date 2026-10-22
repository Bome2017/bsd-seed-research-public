# Testing small source bounds across coefficient primes

October 18 UTC / October 17, 2026 local. Parent lab commit: 6eb993b4e778eed5d74ace1fbea2cf4901835045.

**Outcome: no cofinite small bound obtained. The seed companion groups at3 are determined conditionally; the actual p7 extension has not supplied an improved norm-kernel bound.**

The task was to try to keep the whole arithmetic source small as the coefficient prime grows, including unit and class-supported directions. We used actual number-field computations and changed failed source constructions rather than just refining a detector. These bounded experiments do not demonstrate that the method will finish the seed, or that it cannot.

## 1. Exact companion contribution at the seed's positive-excess prime

Under the retained GRH-dependent source class completeness and incidence-index inputs, the new deduction gives

    Cl(B){3}^- = (Z/3)^3,
    Cl(B,S){3}^- = (Z/3)^2,
    dim K_A = 4,

for the same seed source/companion fields and S={2,3,2243,4547,5843}. The earlier companion bound2 and complete-source bound4 are attained.

We reconstructed the actual ordinary class-image matrix of the four known source elements:

    [0 2 2 2; 0 0 2 2].

Its rank is2. Exact substitution replays all four affine norms as cubes. Consequently the actual incidence map kills the entire source minus3-class group, provided the source presentation is complete. The reverse-composition identity kills the companion group by3, while the actual unit-index identity gives its length3. Its S-quotient has length2.

This computes the companion's relevant abstract group without a companion BNF. It uses explicit source elements, their actual ideal classes, cube identities and the retained index theorem, not a previously known Sha size. It remains conditional; no unconditional class certification was obtained. See class_control/PROOF.md and CLASS_PROOF_REVIEW.md.

Together with the retained all-place membership and rank-two inputs for the four independent classes, this prevents a false target: coefficient 3 really has excess. The complete global source itself has dimension 4 under the stated assumptions. It is a positive-excess control for a rule aimed at the other coefficient primes.

## 2. What a bound across larger primes actually requires

The retained full-image framework gives ordinary faithful-character unit dimension d=(p+1)/2. If authenticated units exhibit r independent incidence-norm images, while t_D bounds the primitive divisor kernel and k_C bounds the ordinary class-map kernel Cl(A)[p]^chi -> Cl(B)[p]^(chi^-1), then

    dim K_chi <= (p+1)/2 - r + t_D + k_C.

This concerns the whole source, including unlisted directions. Source upper2 suffices directly for the rank-two seed; upper3 suffices under the separately retained parity theorem on its domain. With t_D=k_C=0, the norm ranks needed for upper3 are0,1,3,24 atp5,7,11,53. A single nonzero norm at5 does not establish this growing rank requirement.

The class-control certificate need not enumerate the companion BNF: a complete source p-torsion presentation and genuine sufficiently precise Artin characters of the target can upper-bound the whole class kernel. Neither an incomplete source list nor arbitrary residue functions suffice. No such new larger-prime class matrix was computed here. The earlier finite-index and higher-exponent safeguards are explicit in class_control/CROSS_PRIME_CERTIFICATE.md.

## 3. Actual p7 arithmetic and source repairs

For rank-two control389a1 we constructed the irreducible degree48 seven-torsion point field, the actual universal point, scalar3 automorphism of order6, and maximal-order data. Signature=(6,21), discriminant=-7^47*389^36. A separate exact field replay passes. The ordinary chi-unit ambient dimension is4.

One bounded BNF attempt hit its117s alarm before saving units or class data. We did not treat GP's zero process exit code after that error as success, and did not repeat the same BNF attempt.

We then changed the source method. An exact scan of2000 integral basis/small-combination candidates found no norm±1 units, but did find an S-unit of norm-7^15. The actual scalar permutation on primes over7 is[1,3,2], so sigma^2-1 cancels its divisor integrally. Its resulting quotient, however, is exactly1. A broader principal-ideal equality test of scalar translates of the same2000 candidates also found no nontrivial unit. Norm identities and the ideal/scalar action have separate exact replays.

These are finite source-search outcomes, not nonexistence theorems. No actual p7 norm rank or class bound follows. See p7_arithmetic/REPORT.md and p7_direct_units/REPORT.md. A different reduced-principal-ideal search then completed 253 of 432 planned reductions before its time cap, retaining no nontrivial units. Its partial scope is recorded in p7_reduced_ideals/REPORT.md.

## 4. Explicit seed functions were tested, with admission checked

To avoid relying solely on BNF units, we tested h(T)=2y(T)+a1*x(T)+a3-m*x(T)-b on the seed and controls atp5,7,11. Its exact rational norm is

    Res(psi_p,(m*x+b)^2-(4*x^3+b2*x^2+2*b4*x+b6))/p^3.

All5637 raw candidates were checked. The only raw S-unit survivors on the seed and389a1 were the homogeneous odd coordinate itself, whose class has zero faithful odd projection. There were two shifted survivors for37a1,p5. Their affine norms really are nontrivial, but a subsequent exact prime-divisor calculation shows nonzero projected valuations above2: (1,3,4,2) mod5. They lie outside the required ordinary-unit source. Their two projected classes are inverse, so their span cannot repair that support.

All5637 resultant integers were independently replayed. A second reviewer also regenerated division polynomials independently and checked36 sampled resultants with SymPy. The new constant-degree norm algorithm completed the full search after the original high-degree loop timed out; no incomplete table was accepted.

Failure of raw h to be an S-unit does NOT exclude a quotient, character projection or combination with cancelled divisors. We do not claim all such combinations were exhausted. The parity proof excludes homogeneous parity-eigen functions only; it does not kill every possible explicit source. See explicit_seed_functions/PROOF.md, rank_mechanism/SOURCE_SEARCH_REVIEW.md and shifted_control37/REPORT.md.

## 5. What is established at the end

- **Derived conditionally:** exact seed companion minus3-primary groups and sharpness of the preceding upper bounds, with the retained class-completeness qualification.
- **Executed:** actual p7 field construction; bounded BNF attempt (timed out); direct source/ideal repairs; actual seed function searches and independent exact replays.
- **Not obtained:** a sufficiently small p7 source bound, a uniform norm-rank estimate, or a cross-prime class-kernel bound.

The previous p5 unit upper2 remains intact. This return does not extend it to7 or claim a new seed coefficient-prime conclusion. FIN, ORDER9 and Q36 remain unchanged. Written proofs received same-team model review, not formal verification or independent human certification. Hashes and publication verify custody only.
