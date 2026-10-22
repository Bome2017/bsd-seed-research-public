# Seed arithmetic in the cyclotomic 5-tower, and a one-table numerator extractor

2026-10-12. Baseline: `0e8bb6859d1391e6d449b1ef02aff2cfd85310f1`.

**Status: CYCLOTOMIC_5_TOWER_VANISHING_DERIVED_UNDER_RETAINED_INPUTS; ONE_TABLE_QUADRATIC_EXTRACTION_DERIVED; OLD_SEED_NUMERATOR_REPLAYED.**

This continuation uses an actual retained seed coefficient rather than another source normalization. It derives an infinite-tower consequence at p=5 and implements a finite-precision extraction rule for further ordinary coefficients. It does not obtain a new coefficient prime or a cofinite ratio bound.

## 1. The mathematical consequence

Let Q_n be the unique degree-5^n subfield of Q(mu_(5^(n+1))). Thus these are the layers of the cyclotomic Z_5-extension, not the whole cyclotomic fields or their whole maximal real subfields. Under the named retained seed inputs and published Iwasawa inputs,

\[
\boxed{\operatorname{rank}E(Q_n)=2,\qquad
\Sha(E/Q_n)[5^\infty]=0\quad\text{for every }n\ge0.}
\]

More precisely, restriction from the rational point group identifies

\[
\operatorname{Sel}_{5^\infty}(E/Q_\infty)
=E(Q)\otimes\mathbf Q_5/\mathbf Z_5,
\]

and the Pontryagin dual is literally

\[
(\mathbf Z_5[[U]]/(U))^2,
\]

not merely pseudo-isomorphic to it. The equality denotes the restriction/Kummer identification, not an identification of all rational coordinates or all prime-to-5 torsion over the tower.

The proof uses the old certified unit quadratic coefficient, ordinary Kato divisibility, the rational-point subgroup, and Greenberg's no-finite-submodule theorem. It neither assumes a main-conjecture equality nor needs a height determinant for this unit-leading case. [Full proof, Section 3](PROOF.md#3-from-the-unit-numerator-to-the-entire-cyclotomic-5-tower).

This is a written deduction requiring independent review. It is not a novelty claim: the source theorems are established and the base-field coefficient was already certified. The extension written here is in the field direction at the fixed prime 5. It does not solve the missing coefficient-prime tail over Q.

## 2. The actual arithmetic replay

The original denominator-25 and denominator-5 symbol tables were recovered at the pinned lab commit, copied byte-for-byte, and checked against their Git blob hashes. The denominator-25 Teichmuller sums are

\[
(-76,0,-76,76,76).
\]

Their raw quadratic moment is 608. Dividing by two for Omega_E=2 omega_1 gives 304. With the ordinary unit root alpha=3 mod5, the standard coefficient is

\[
L_{2,5}\equiv alpha^{-2}\cdot304\equiv1\pmod5.
\]

An independent discrete-log enumeration agrees, the four plus Hecke relations pass, and the direct two-table stabilized measure gives the same residue. This recovers the old unit exactly from saved data. The original large Fourier corpus, ball arithmetic, denominator theorem and global residual-image proof were not rerun.

## 3. Why finite errors do not invalidate the tower deduction

The unit residue and Kato divisibility force the ordinary Selmer characteristic ideal to be (U^2), because two rational-point directions already force the factor U^2. This alone would leave finite Lambda-modules invisible.

Greenberg Proposition 4.14 applies because the Selmer group is cotorsion and E(Q)[5]=0. It excludes the finite submodule in the dual. The dual is consequently free of Z_5-rank two. Its surjection onto the dual of the base-field point group is an isomorphism. Global restriction is injective because E[5^infinity](Q_infinity)=0; the base points already fill the target, forcing each finite-layer Selmer group to be precisely its Kummer subgroup.

The packet includes explicit abstract countercontrols showing why neither the characteristic ideal alone nor free base coinvariants suffice without the finite-submodule theorem. No finite error is simply dropped.

## 4. A finite arithmetic test for the next coefficient

For a good ordinary p>=5, let A_n be the quadratic moment of the raw, source-matched, p-integral plus-symbol table of denominator p^n in the gamma=1+p coordinate. For n>=2,

\[
\boxed{L_{2,p}\equiv(1-p/alpha^2)alpha^{-n}A_n
\pmod {p^{n-1}}.}
\]

Thus a nonzero A_n modulo p^(n-1) determines the exact valuation of L_2,p. A valuation-only test needs one denominator table and no computed unit root. The actual coefficient residue still requires the specified unit multiplier and period normalization.

The lower table has not been discarded without proof: its transfer contribution is eliminated using compatibility of the ordinary measure, with the precision loss retained. [Proof, Section 4](PROOF.md#4-a-single-denominator-quadratic-numerator-extraction).

For the retained matched r_17=1, denominator 4913 gives the first potentially decisive mod-17^2 test; if it vanishes, denominator 83521 permits the valuation-two case using mod17^3. The existing denominator-289 layer alone cannot certify the needed higher valuation. These are preparation/acceptance levels, not newly computed seed tables or authorization of a campaign.

No bound is obtained for the intrinsic ratio at a new prime. The extractor does not eliminate the high-conductor Fourier work needed to create its top table and carries no claimed wall-time improvement for the existing engine.

## 5. Evidence, review grade and endpoints

The standard-library [checker](checks/verify.py) and [deterministic results](checks/RESULTS.json) contain the actual seed replay, 84 synthetic compatible one-table cases, five precision-sharpness controls, eight malformed-input controls and four precision boundaries. These tests do not formally prove the tower theorem or certify new seed values.

[SOURCES.md](SOURCES.md) separates primary theorems, retained arithmetic and new deductions. [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) pins the historical records. [REVIEW.md](REVIEW.md) identifies the critical mathematical checks.

**No new base-field coefficient prime is settled. FIN, ORDER9 and Q36 remain unchanged.** There is no new coefficient, cofinite nonvanishing theorem, supersingular result or exceptional-primary result. The new global conclusion to review is the field-tower statement at 5. The new computational output is a one-table extraction rule, tested on actual old seed data and exact synthetic controls.

Publication is additive on an isolated lab branch based on the pinned review. No main merge, expert-repository promotion, paid job, remote computation campaign or independent reviewer is claimed.
