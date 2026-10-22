# Adjacent arithmetic source screen

Date: 2026-10-11. Repository pin: `openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

Status: `RELEVANT_SOURCE_MECHANISMS_FOUND; NO_RANK_TWO_SEED_APPLICATION_ESTABLISHED`.

This is a theorem-interface screen, not independent certification of these newly posted manuscripts. “The manuscript states/proves” describes its written claim, not a promotion to an accepted theorem. The collection's abstracts were searched across the arithmetic topics; six full source directories were fetched, and the passages below were read. This is not an exhaustive proof review of 719 manuscripts. No seed arithmetic or remote research job was run.

## 1. Strongest concrete match: weighted CM-divisor/localization identity

Source: [A pointwise 2-converse for elliptic curves with rational two-torsion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/paper.pdf).
Exact source: `build/sections/coefficients.tex`, labels `co:kummer`, `co:theta-bridge`, `co:weighted-comparison`, `co:theta-sum`, `co:odd` (locally lines 187–280 and 284–563).

The manuscript constructs, at coefficient precision `2^M`, an actual finite-field Kummer detector

`lambda_M = b kappa_M : E(F_{ell^2}) -> Z/2^M`,

where `C` is complex conjugation on `T_2 E`, `b C=b`, and `Fr_ell=C mod 2^M`. Additional quadratic conditions are `(h_*/ell)=-1` and `(D_w/ell)=1`, with a fixed positive simple-zero twist witness `D_w` and a negative central-value companion `h_*`. A Kummer/Chebotarev argument claims bounded detection valuation as precision grows.

It then gives an explicit weighted ternary theta construction from the *reduced modular parametrization*:

`a_M(D) = c_0 2^{omega(N)} zeta_M(D) lambda_M(red_ell(L P_D)) mod 2^M`.

Here `P_D` is a genus-character Heegner sum; `c_0,L` are fixed integers independent of `D,M,ell`; `zeta_M(D)` is a root-of-unity phase. The source retains the quaternionic order, orientations, Schwartz weights at every bad prime, the cyclic level subgroup, automorphism denominators, Atkin–Lehner constants and torsion multiplier. In particular, the formula is substantially more specific than “there exists a geometric comparison.”

### What can be used for this project

This is the closest source match to the current CM-divisor/localization construction lane. Its *construction and accounting* can be compared directly against our divisor-to-local-point map. The source also points to published reduction geometry: Jetchev–Kane §2 and Cornut–Jetchev §3.2, §§4.6,4.9–4.10, Cor.4.1. Those references must themselves be read before importing their precise scopes.

### Exact limits

- This is a detector for a **rank-one genus-Heegner sum** and a weight-3/2 coefficient, not a formula for the seed's two-point tame regulator or its Mazur–Tate depth-two coefficient.
- The root-number and companion conditions remain essential. One cannot set `D=1` and treat the rank-two seed as the required simple-zero witness.
- The coefficient prime is **2**. The seed's missing cofinite control is chiefly at odd coefficient primes. An odd-prime analogue needs its own representation/sign/Schwartz-weight proof; `2^M` cannot simply be replaced everywhere by `p^M`.
- Fixed constants are not automatically units, and no claimed equality `c_0=288` exists here. The formula neither computes a seed coefficient nor bounds `m_p-w_p`.
- The manuscript's new theta and integral-comparison arguments have not been independently verified in this screen.

### Frobenius and target-line mismatch with seed G2

The source uses a **reflection**, complex conjugation `C`, with determinant `-1`, trace `0`, and `b C=b`. It obtains `ell=-1 mod 2^M`; the target has Frobenius sign `+1`. At odd coefficient primes, a reflection would still have a one-dimensional `+1` eigenspace.

The retained seed G2 auxiliaries instead have `Fr_ell=-I mod p`, hence `ell=1 mod p` and `a_ell=-2 mod p`. There is no `+1` invariant line in `V` in that case. Requiring the source's same scalar row to obey `b(-I)=b` gives `2b=0`, so **b=0 for odd p**. Thus the source detector cannot be carried unchanged to G2 auxiliaries. Its Frobenius-squared Kummer target can still have dimension two, but extracting a nonzero scalar then requires a compatible *different* target action/row; it is not the source's plus-eigenline construction. This is a mismatch for that direct transplant, not a prohibition on all CM pushforward maps.

What survives as reusable procedure is the explicit CM orbit pushforward, reduction naturality, local Schwartz weights, stabilizer denominators, and orientation/Atkin–Lehner accounting. What remains unproved is the odd-p detector with the desired Frobenius action and, separately, its rank-two Mazur–Tate/regulator comparison.

### Concrete admissible next test

Perform a *source map audit*, not another full detector construction: take the current CM-divisor lane's exact map and compare it with `co:weighted-comparison`, component by component (parametrization, finite-field Kummer evaluation, genus character, quaternion order, orientations, torsion multiplier, coefficient lattice). Use this exact alignment checklist:

1. **Source object:** genus-character divisor/Heegner sum versus the actual BD divisor; record fields, conductors, degree-zero adjustment and character action.
2. **Curve map:** same modular parametrization and differential lattice, including fixed cuspidal-constant and torsion multipliers.
3. **Reduction:** same good prime and cyclic-level subgroup; verify naturality of divisor pushforward and finite-field Kummer maps.
4. **Frobenius:** `C` versus `-I`, plus versus minus target action. Do not pass the source `bC=b` through G2 unchanged.
5. **Integral coefficient:** identify `c_0`, orientation multiplicity and root-of-unity phase in the actual lattice; retain their valuations.
6. **Automorphic target:** weight-3/2 Fourier coefficient versus the precise depth-two Mazur–Tate coefficient. These are distinct until a comparison is proved.
7. **Rank-two output:** identify where both `P_1,P_2` enter and where a determinant or second derivative is obtained. The rank-one detection formula supplies neither by itself.

Record which diagram is literally the same and which arrow requires a different rank-two input. A useful success is a proved shared integral local/reduction square with its exact multiplier; it is not a seed bound. Do not launch evaluation merely to confirm a generic detector that is already known to exist. Before a numerical test, identify an unresolved square whose result would change the seed comparison.

## 2. Integral interpolation is relevant technology; the low-corank gate is explicit

Same manuscript, `build/sections/cyclotomic.tex`, labels `cy:fourier`, `cy:binary`, `cy:residual`, `cy:uniform-integrality`, `cy:central`, `cy:missing-vertex`.

The arithmetic construction has `Lambda=Z_2[[t]]`, `O=completion(Lambda_(2))`, `G=(Z/2)^b`. It aims to construct one scalar `u in Lambda[1/2][G]` with a denominator `2^C` independent of the size of the family. It keeps separate:

1. rational height-one Kato divisibility after character specialization;
2. integral control from a *fixed-form* Kato class before character specialization;
3. the intersection `O intersect Lambda[1/2]=Lambda`;
4. finite local and global cohomology terms in the central determinant comparison.

The elementary intersection lemma does not lose a factor `|G|`, because both memberships are proved for the same coefficient. This is a potentially reusable way to prevent family-size denominators, not a theorem asserting that an arbitrary normalized Kato family is integral.

The binary congruence lemma states that for `r` integral group-ring functions, precision `2^M`, and `b>r(2^M-1)`, some nonzero character address has all its values congruent to the zero address. Its proof uses the divisibility `2^{|I|}` in the Boolean monomial expansion and Chevalley–Warning. This explains the actual transfer mechanism.

### Why the theorem cannot simply be applied to our seed

- `cy:missing-vertex` assumes the **full 2-infinity Selmer corank of the missing base is zero**. Its hypothesis on all nonzero addresses is not just nonvanishing: the normalized valuation `D(h)=v_2(L^alg)-2w(h)-length Sha[2^infinity]` has a uniform upper bound.
- The ring-class version (`ring-limits.tex`, `rd:missing-vertex`, lines 64–89) assumes **Selmer corank over K is one** and all nonzero addresses have a *simple* product zero with a uniform Heegner-index bound. The seed's two independent rational points already exclude this corank-one hypothesis over any K.
- The central determinant proof (`cyclotomic.tex`, lines 669 onward) uses corank zero to obtain rational global `H^2=0` and no specialization rank jump. For the rank-two seed, dropping that hypothesis erases exactly the degree-two/excess term our existing work has learned to preserve.
- `cy:residual` uses that `E[2]` is filtered by trivial modules. This is true for the rational-two-torsion seed at 2, but not for its full `GL_2(F_p)` residual representation at odd p. Its Ferrero–Washington reduction is therefore not an odd-prime uniform bound on the seed.
- A quadratic-character cube is special at 2. At odd p its sign characters do not all coalesce modulo p. A p-character replacement changes the arithmetic family and needs a new theorem.

### Prior project collision: this architecture is already assigned

The project already screened this mechanism in `work/returns/BSD_OPENAI_RELEASE_SCREEN_CLAUDE_2026-10-06/GATE4_CHECK.md` and submitted `BSD_ARISTOTLE_RANK2_ANCHOR_SUBMISSION_2026-10-06/DELTA_TASK_RANK2_ANCHOR.md`. I read both during this screen. The corrected historical verdict is `GATE4_FAILS_WITH_THE_CURRENT_KNOWN_ANCHOR`, not structural impossibility. Two gaps were already identified: a genuine rank-two global anchor, and the fact that the original missing-vertex theorem proves the converse direction (low Selmer corank -> analytic rank), whereas the seed already has analytic rank two and needs arithmetic control.

**Do not relaunch this as a newly discovered route.** The current pin is an October-7 source, while the historical file cites a September-24 version. I have not completed a version diff or shown that the revised source repairs either rank-two gap. The weighted CM detector above is a more specific source comparison to check against the current divisor map, not a claim of new project architecture.

### Technical lemma located for that already-known architecture

`ring-determinants.tex`, `rd:outer-bound`, lines 745–878, states a uniform residual determinant valuation bound from three **simultaneous** hypotheses: bounded minimal model sizes after switches; exact-kernel/all-sequence evaluation with Chebotarev realization and degree-two identities; preservation of localization, duality and classes with a common clearing exponent. Its proof uses outer rank reduction before extracting a nonzero terminal minor, rather than pretending bounded matrix size bounds torsion. The manuscript itself warns in `rd:interface-status` that ordinary duality and classical Heegner formulas do not supply this interface.

This is relevant to the project's finite-H^2-error and moving-prime problems. It is not currently applicable: its rank-one generic systems and their simultaneous arithmetic construction have not been supplied for the rank-two Kato derivative. It gives no fixed nonzero rational scalar across coefficient primes. A proposed transfer should first exhibit the *same* retained complex, class and maps at every stage; a formal analogy with the theorem's three hypotheses is not a result.

## 3. Auxiliary twists: actual existence tool, not a seed transfer theorem

Same paper, `nonvanishing.tex`, `nv:local-witness` and `nv:rough`, lines 9–28. The manuscript states auxiliary twist existence in every nonempty filter with prescribed real sign and finitely many unit squareclasses, assuming the corresponding root number. It claims nonzero central values for root +1 and nonzero derivatives for root -1, outside any prescribed finite prime set. Its bounded-factor completion additionally claims an absolute bound on the number of prime factors for central-value witnesses.

Possible use: if the present -7 or -23 companions fail a *new* finite local requirement, this provides a specific candidate source for choosing a replacement companion while preserving selected local squareclasses. The moment/sieve argument, especially the claimed absolute factor-count bound, needs review. It is not a supplied certificate for any selected numerical twist.

Our record already retains particular useful auxiliary twists. Mere existence of still more rank-zero/rank-one twists does not control the rank-two seed or prove nonzero derived classes modulo p cofinitely.

## 4. Goldfeld density / mean rank

[Goldfeld density manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026/paper.pdf), `sections/00-introduction.tex`, `thm:main-density` and `cor:finite-descent`.

It claims analytic ranks 0 and 1 each have density 1/2 among **signed squarefree twists ordered by absolute value**. Its finite-descent criterion is `dim Sel_2 - dim E(Q)[2] in {0,1}`. The mean-rank companion claims average analytic rank 1/2, with an explicit tail theorem; it expressly does not give higher analytic moments or thin-polynomial-subfamily uniformity.

Use: research control panels / auxiliary-twist selection. It is not a result on the fixed exceptional rank-two member. Density one leaves our chosen member unresolved. The actual pointwise mechanisms in sections 1–3 above are more relevant than the density headline.

## 5. Imaginary quadratic modularity

[Source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf), `sections/introduction.tex`, `thm:main` and geometric prime-switch discussion.

The claimed theorem gives automorphy for any elliptic curve over an imaginary quadratic K, matching all local parameters, with cuspidality when non-CM. The construction passes automorphy along residual congruences between rank-two character pieces of cyclic-cover Jacobians.

Our curve is already over Q and already modular. Its quadratic base change is not missing automorphy; an additional modularity theorem supplies neither a rank-two height identity nor Selmer upper control. The geometric prime switch might be a source technique only for a separately constructed auxiliary non-Q curve/representation; no such new object needed by the seed has been identified here. Do not present automorphy transfer as transfer of Sha vanishing.

## 6. Rational Hodge / Milne rationality: scope warning

[Milne rationality manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf), `sections/00_intro.tex`, `thm:main`; `05_reduction.tex`, `cor:algebraic-specialization`.

For a rational Hodge class on an abelian variety with good reduction at a **fixed place of residue characteristic p**, and complementary divisors on that reduction, it claims one rational pairing in all prime-to-p realizations and crystalline realization. The text explicitly does not require comparison between distinct reduction places. Together with the separate CM Hodge theorem it claims an algebraic representative on that special fiber.

This may help only after a proposed seed scalar is actually realized as the specified pure Hodge-class/divisor pairing. It does not construct that realization, identify the Mazur–Tate coefficient with it, compare different auxiliary reductions, prove the pairing nonzero, or control integral denominators. Rationality of a pure cohomological pairing does not by itself prove rationality of `L''/(2 Omega Reg)` or of a secondary height/biextension expression. The cycle can depend on the reduction place.

The [CM Hodge manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf) claims rational algebraicity on CM abelian varieties and consequences for abelian varieties over finite fields. That is not a theorem on number-field Sha or an integral bound on the non-CM seed. Its relevance is a possible geometric realization ingredient, conditional on the required seed object being exhibited. No such object was supplied by this screen.

## Disposition

The concrete reusable material is the CM reduction/Kummer/theta comparison and the carefully separated integral determinant/interpolation architecture. None of the inspected theorem statements closes FIN, ORDER9 or Q36 for the rank-two seed. The new concrete source-to-map examination is a tightly scoped comparison of the current arithmetic map with the explicit `co:weighted-comparison` diagram. The determinant/missing-vertex adaptation is already in the project record and its rank-two anchor assignment; do not send a duplicate task without checking the existing return and the October-7 source delta. Neither should begin by relabelling the existing excess quotient or assuming its bound.

`../sources/adjacent/SOURCE_BINDINGS.json` records the downloaded source files and hashes. Downloading a full source directory does not mean every line of it was read.
