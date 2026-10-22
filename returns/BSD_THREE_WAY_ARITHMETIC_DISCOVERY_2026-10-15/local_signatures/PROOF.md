# Local point-quotient detector: definition, descent and actual three-way check

Date: 2026-10-15. Coefficient prime: 3. Grade: written deduction and exact finite arithmetic, under the retained explicit-descent, rank, saturation and full-image inputs. No novelty claim or new seed-primary upper bound.

## 1. The object being measured

Let V=E[3], S=Sel_3(E/Q), and W be the Kummer image of E(Q)/3E(Q). For a finite prime q, the Selmer condition places loc_q(S) inside the local Kummer image K_q=E(Q_q)/3E(Q_q), viewed as a subspace of H^1(Q_q,V). Define

    d_q : S/W -> K_q / loc_q(W),
    [c] |-> [loc_q(c)].

This is well-defined: changing c by a global rational-point Kummer class changes its localization by precisely loc_q(W). The Kummer exact sequence identifies S/W with Sha(E/Q)[3], without assuming Sha finite. There is no assertion that localization of the torsor in H^1(Q_q,E) is nonzero; it is zero. The detector retains the local V-valued Kummer lift before forgetting the covering data, and quotients only by the image of global rational points.

The point lattice used here must supply all of E(Q)/3E(Q). Merely choosing two independent points would not suffice. That prerequisite is supplied separately by the retained rank and 3-saturation results: rank zero for 1913b1, rank one with generator P for 28042a1, and the full point planes for seed3 and 389a1. No ambient source-completeness assertion is needed to define or evaluate d_q on the named genuine classes.

## 2. Arithmetic realization at the scanned primes

The retained Schaefer--Stoll descent identifies H^1(Q,V) with the scalar-compatible and affine-norm-compatible part of the degree-eight nonzero-torsion-point algebra modulo cubes. Selmer membership additionally requires all local conditions. Corollary 7.9, Proposition 7.10 and section 10.1 are the source gate, retained with the prior explicit norm and local-image certificates; they are not replaced by a finite sample of residue relations. Primary source: https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf .

For each good q different from 3 that splits completely in this point algebra, order the eight roots and their corresponding nonzero torsion points. Since q=1 mod 3, a chosen nontrivial cube root omega in F_q defines an additive character

    chi_q(z) = j in F_3 when (q^(-v_q(z))*z mod q)^((q-1)/3)=omega^j.

For our globally unramified-at-q source classes, each branch valuation is a multiple of 3. Thus this leading-unit character records their local cube classes. The vector of eight such characters is the coordinate realization of the local Kummer class. Changing omega or the ordering of roots changes coordinates, not whether a class lies in the point image.

Let M_q be the matrix evaluating the literal source generators, and W_0 the matrix of all global point classes in those source coordinates. Compute a basis Q_q of the full left annihilator of M_q W_0. The implementation then evaluates

    Q_q M_q C_0

on the named class columns C_0. It constructs Q_q before applying those extra columns. Consequently the detector is not chosen to suppress or fit the observed excess. Its kernel on the local source image is exactly the global-point image there, by elementary finite-dimensional duality. Individual rows selected for the displayed short certificates are selected retrospectively from the sealed scan, by deterministic greedy rank increase; they are not claimed to have been predicted.

At a split good prime, the full local Kummer image has dimension two, and the eight-coordinate realization is injective on it. One way to see the latter is to identify the character evaluations with the Weil pairings of a V-valued unramified cocycle with all eight nonzero torsion points. Nondegeneracy of the pairing makes this map injective. This statement concerns genuine cohomology classes; arbitrary source elements need not satisfy these relations.

## 3. Independence from representatives

Multiplying a source element by a cube changes its branch valuation by a multiple of three and its leading residue by a cube. Both leave chi_q unchanged. If a different uniformizer uq is used, the leading residue changes by u^(-v), again a cube because v is divisible by three. Adding a global rational-point class changes the eight-coordinate vector by a column combination of M_q W_0, annihilated by Q_q. Thus d_q is independent of all these changes.

The literal replay evaluates the actual rational-coefficient polynomials at Hensel lifts of the roots, strips numerator and denominator valuations, and checks that the remaining valuation is divisible by three. This is necessary: for seed3 at q=2767, root index 7, the literal P2 representative has valuation 3, with leading unit 916. Its naive residue is zero although its cube class is well-defined. That row is retained, not skipped. The exact leading-unit result agrees with the factorized source character.

`REPRESENTATIVE_CONTROLS.json` records 6,912 unit-cube changes, 4,608 nonunit cube changes using actual q^(+/-3)-scaled polynomial evaluation, 2,304 uniformizer changes and 1,584 point-shift checks. All pass. These are finite implementation controls; the preceding argument proves the general invariance.

## 4. The actual certificates

The symbols beta1,beta2 below name the prior literal seed representatives; their genuine global and all-local membership and independence are retained inputs. The new calculation does not infer their existence from a Sha order.

| Case | Rational point dimension | Genuine known excess dimension | Fresh detecting rows on excess | Rank |
|---|---:|---:|---|---:|
| 1913b1 | 0 | 2 | q=997: (0,2), (1,1) | 2 |
| 28042a1 | 1 | 2 | q=487: (2,1); q=691: (1,1) | 2 |
| Seed at 3 | 2 | 2 | q=811: (0,1); q=2767: (1,2) | 2 |
| 389a1 | 2 | 0 | every point-quotient row is zero | 0 |

For the seed, the full class order is (P1,P2,beta1,beta2). The selected root weights at both q=811 and q=2767 are (1,1,0,0,0,0,0,0), and the full signatures are respectively (0,0,0,1) and (0,0,1,2). The excess determinant is 2 mod 3. At q=811 the literal root-products on the four classes are (622,561,8,208); at q=2767 they are (1127,1495,1735,2526). The cube characters give the displayed signatures directly.

For 28042a1, class order is (P,unit1,unit2); the selected weights are (2,1,0,0,0,0,0,0). The full signatures (0,2,1) and (0,1,1) have excess determinant 1. For 1913b1 the first two individual root characters at q=997 already have determinant 1.

Each positive statement is a lower/detection statement on a named span. In particular, the 28042a1 source-completeness certification timed out in the preceding run; exact class membership survives that limitation, but a complete upper bound does not follow. The seed's ambient source retains its prior completeness grade. No upper claim is obtained from the absence of further displayed columns.

## 5. Why global admission must come first

The mirror389 false calibration is the previously scalar-compatible, locally repaired ordinary class lift with source exponents

    (0,0,0,0,0,0,2,2,2,2,1).

It has a nonzero local point-quotient signature already at q=127. This does not make it a Selmer class. At q=151, root indices (0,2,7), roots (5,25,147), correspond to the actual affine line with torsion points (24,138),(60,47),(53,136). Their sum is zero, and the line does not contain the origin. The literal source residues (93,68,125) have product 15 mod 151, and

    15^50 = 32 mod 151,

where 32 is a nontrivial cube root of unity. Hence the actual affine-line norm has noncube residue. A global cube cannot have this residue at a split unramified branch. This is a conclusive failure of the global norm condition, not merely a missing positive certificate. `mirror389_false/GLOBAL_NORM_REJECTION.json` contains the literal data.

The resulting two-stage classifier is therefore:

1. Authenticate the global cohomology image and all Selmer local conditions. A noncube norm residue rejects a candidate; finitely many zero residues do not prove admission.
2. For admitted classes, pass to K_q/loc_q(W). A nonzero signature proves a non-point class; zero at a particular q does not prove it is a point.

This separates an actual false source element, actual point classes, and actual excess classes. It is not an algorithm proving the absence of all undiscovered classes.

## 6. What the experiment establishes toward the research question

The same arithmetic extraction works across full-image rank-zero, rank-one and rank-two examples, including the actual seed's known 3-primary excess. It no longer relies on the rational five-isogeny detector from the older control. The scalar/unit/class origin of a source does not determine whether its admitted class is a point; actual global admission plus quotient-local evaluation does distinguish the named examples.

`JOINT_EVALUATION_DENSITY.md` explains, under the retained full-image and independence inputs, why individual good primes can be blind even when the known quotient is nonzero. That theorem permits arbitrary finite excess and supplies no global bound. FIN, ORDER9, Q36 and seed coefficient-prime coverage are unchanged.
