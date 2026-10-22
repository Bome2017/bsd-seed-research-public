# Continued seed-unit experiment: exact admission and the integral norm index

2026-10-13. Status: **UNIT_COMPONENT_EXHAUSTED_AT_3; INTEGRAL_NORM_INDEX_DERIVED; NO_UNIFORM_BOUND.**

I continued beyond the explicit unit: reconstructed the complete unit component, calculated which source conditions remove candidates, constructed the actual affine-line norm into the dual field, and tested whether its integral composition identity bounds the surviving component. The calculation reaches a specific arithmetic limit. The norm identities restrict each elementary divisor, but do not control how many survive across coefficient primes.

This is an executed structural experiment on the original seed. It is not another primary-vanishing run, a novelty claim, or a full BSD result. FIN, ORDER9, Q36 and coefficient-prime coverage are unchanged.

## 1. The unit component is now completely determined

Let K be the nonzero-3-torsion point field used by the previous return, and let tau(T)=-T. Exact signatures are (2,3) for K and (2,1) for its fixed quartic field. Hence the norm-one global units have rank two and their classes modulo cubes have dimension two.

I constructed a literal global unit representing the Kummer image of P1, complementing the previous literal unit representing beta1/beta2. Their classes are independent by the retained four-class certificate. They therefore exhaust the entire norm-one unit component. Both are actual Selmer classes: the first comes from a rational point, the second is a non-point covering difference.

Consequently no additional valid source-admission or local-solubility condition can eliminate a direction from this particular unit plane. The non-point unit is already a genuine surviving class, not a spurious field unit waiting for another membership test.

The exact unit/class filtration of the four known classes is (0,1,1). This classification now follows from witnessed units, signatures and independence **without the earlier class-group completeness assumption**. This does not certify the whole class group or exclude classes outside the four-dimensional span.

## 2. Actual rejected controls and a historical code repair

Two further genuine global units were constructed. They are independent of the admitted two, giving a full four-dimensional basis of units modulo cubes. Both are rejected by anti-invariance and by the local condition at 3. Thus the admission test distinguishes real excluded candidates from the surviving excess.

The local calculation also found and repaired an omission in the September search helper. When the local Kummer image was zero, the helper skipped the local equations. At 2, 2243 and 4547, zero image instead requires the entire local evaluation to vanish. Independent matrix reconstruction reproduces the old dimension seven and gives the corrected dimension four. The four final certified classes span that corrected kernel; their certificates survive.

The old interpretation that global relations remove three *locally admissible* seed directions is withdrawn. On this cached source, the corrected local kernel and the scalar-compatible affine-norm kernel are the same four-dimensional space. The latter imposes both anti-invariance and the affine norm; the norm alone also kills rational scalar classes. A patch and corrected helper are included; frozen historical files were not changed.

## 3. The arithmetic comparison was constructed, not left as a task

The affine-line norm of Schaefer--Stoll sends the torsion-point field K to the dual torsion field B. I constructed it through the cubic algebra of the intersection of the seed with a line containing three nonzero 3-torsion points. The defining polynomial for B is

    z^8 - 10695389742 z^4 + 189820747845720 z^2
        - 9532613477773235547.

The inclusion, all torsion identities and all four resulting cube witnesses were checked exactly. A separate multiplication-matrix determinant replay agrees with the field-norm calculation. No target class group, regulator, L-value or expected Sha order was used to compute these norms.

On the matched scalar-character unit lattices, the forward and reverse incidence norms satisfy

    v u = p Id,       u v = p Id.

Thus every Smith factor is 1 or p. This is useful integral information, but it is not yet a small-kernel theorem. At the actual seed prime 3, the two independently admitted unit classes force

    Smith(u) = (3,3),       index(u) = 9,
    v is an isomorphism over Z_3.

The index statement follows from the exact maps and the complete unit plane; a target fundamental-unit basis was not computed. Detailed derivation is in PROOF.md and reviewer/INCIDENCE_NORM_REVIEW.md.

## 4. Where the attempted bound stops

For full-image odd p, the scalar-compatible unit lattice has rank (p+1)/2. The incidence identities allow any number s between zero and that rank of Smith factors equal to p: the complementary diagonal maps realize each possibility algebraically. Those examples are lattice countercontrols, not claimed seed realizations.

The seed at 3 supplies an actual arithmetic asymmetry, not just a formal control: the forward index is 9 and the reverse index is a unit. Replacing the real unit lattice by the formal archimedean permutation lattice would incorrectly predict only one admitted direction here. The exact integral lattice matters.

The attempt to obtain an upper bound from norm composition and symmetry therefore stops at the **number of p-factors in the actual unit norm map**, together with the independently calculated ideal-class lifting obstruction. We computed the latter coupling at 3 as well: explicit unit corrections repair both class directions, and its quotient obstruction is zero. Combining these admission conditions creates no further restriction on the known four classes.

The reviewer derives a sharper diagnostic: on the whole anti-invariant unit space, the norm index is expressed by a ratio of class numbers of the point and dual fields and their fixed subfields. At 3 it gives v3(h_B/h_K)=1; with the retained class-group calculation it predicts v3(h_B)=3. This is a written number-field deduction, not a computation of h_B. It locates the arithmetic lattice contribution, but supplies no bound on it as p varies. Computing a new isolated mirror class group would not resolve that cross-prime problem, so no such run was launched.

This is a scoped limit of the tested mechanism. It does not prove that another arithmetic input cannot bound these indices. It does show that further norm-one normalization, extra copies of the same admission equations, or a formal dimension substitution cannot supply the missing seed bound.

## 5. Evidence and grade

- All 15 source involution identities and all four actual class-coordinate identities have literal cube witnesses.
- A separately written residue evaluator recovers rank 15 on the source and rank four on the unit basis, using 119 valid rows.
- Fresh-nf portable verification of the three new compact unit certificates checks respectively 1,847, 1,868 and 1,865 prime-ideal valuations. The previous positive unit certificate is included and replayed separately.
- All four actual affine-line norms are literal cubes; multiplication-matrix replay agrees.
- Separate same-team matrix review reconstructs the local annihilators, the corrected dimensions, all admission intersections and the class/unit repairs.
- Exact signature and finite incidence models are checked independently. Rejected implementation trials are preserved; a printed PASS after a GP error was never accepted.

The unit exhaustion and the four-class filtration no longer use class-group completeness. Claims that the cached 15-generator source or six-dimensional valuation-zero source are globally exhaustive retain their historical GRH/source grades. Rank, saturated points, covering membership and the covering-to-cohomology map retain their prior grades. This is written mathematics plus exact arithmetic, with same-team review; no independent human certification or Lean proof is claimed.

Primary source for the norm's mathematical identity: Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, long version, Corollary 7.9 and Proposition 7.10: https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf . The new index deduction and seed calculations are separated from that imported theorem in the proof.
