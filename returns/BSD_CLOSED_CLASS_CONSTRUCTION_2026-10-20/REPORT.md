# Complete class bound on the actual seed: obtained, but too coarse for FIN

Date: 2026-10-20. Status: **COARSE_COMPLETE_RELATIVE_CLASS_BOUND_DERIVED**.

This attempt changes the method from collecting relations to bounding the entire relative ideal class group analytically. It includes classes missing from every collected factor base. It produces a written bound under the retained exact field inputs, with exact outward numerical checks. The bound is too large to give the required small surviving source. FIN, ORDER9, Q36 and seed-prime coverage are unchanged.

For the actual coefficient-five point field A of degree 24, and its scalar-minus-one fixed field K of degree 12, the result is

\[
\left|\ker\bigl(N:\operatorname{Cl}(A)\to\operatorname{Cl}(K)\bigr)\right|
=h_A/h_K\le262\cdot10^{66}<5^{98}.
\]

Hence the whole relative five-primary class group has length at most 97. In particular,

\[
\dim_{\mathbf F_5}\operatorname{Cl}(A)[5]^{\chi_2}
+\dim_{\mathbf F_5}\operatorname{Cl}(A)[5]^{\chi_3}\le97,
\qquad \chi_2(2)=2,\ \chi_3(2)=3.
\]

This bounds all class-supported directions in these two characters. It does not assert that 97 directions exist, that the two dimensions agree, or that this is the dimension of Sha. With the retained faithful unit dimension three and zero valuation allowance at five, the corresponding conservative complete-source ceiling is **100**, before further authenticated norm/local cuts. That is not close enough to the required rank-two control.

## How the bound avoids the old omitted-class problem

The [proof](theory/COMPLETE_CLASS_BOUND.md) retains the full relative unit lattice and its unknown index. A nontrivial norm-one unit generates the quadratic extension A/K. The relative discriminant therefore gives a lower bound for its logarithmic length. Minkowski's theorem turns that into a lower bound for the covolume of the entire rank-six relative unit lattice. The conversion to the usual regulator keeps the unit index, with an explicit power-of-two upper bound.

The analytic class number formula then gives

\[
h_A/h_K=
\frac{\sqrt{D_A/D_K}\,L_K(1,\psi)}{(2\pi)^6(R_A/R_K)}.
\]

Louboutin's Theorem 4(1), equation (10), bounds this quadratic Hecke L-value from above. Its statement applies to an arbitrary base field, including ramification at infinity. The CM-only class-number consequence is not used. A is not CM. [Primary source](https://doi.org/10.4153/CJM-2001-045-5).

Finally, finite ramification makes A disjoint from the Hilbert class field of K. Chebotarev proves the class norm is onto, so the ratio bounds the actual norm kernel, not a selected quotient. No GRH, seed Sha order, BSD formula, or assertion that collected prime ideals generate the class group enters this class bound.

The [exact certificate](theory/EXACT_BOUND.json) uses rational series with outward remainder bounds. A separate implementation obtains the weaker but sufficient bound 2.8·10^68<5^98. The retained maximal-order discriminants and signatures were read back from the saved field objects and agree; their original construction is retained, not freshly recertified here.

## The genuinely new relation family was also tested to completion

The arithmetic lane used elliptic line and tangent functions on the actual seed, rather than combinations of the previous 196 relative-reduction rows. The predeclared 42 functions reduce to 31 distinct functions. All exact number-field norms agree with their division-polynomial resultants.

Including all scalar conjugates gives 124 elements and 134 pairwise-coprime ideal atoms. Rational denominators and every outside-support divisor remain in the calculation. For each faithful character:

| Quantity | Value |
| --- | ---: |
| Faithful support columns | 28 |
| Columns with outside support | 22 |
| Full relation rank | 20 |
| Outside-support rank | 20 |
| Net relation rank on the bounded support | **0** |

All 84 rational-kernel products of the anti-divisors evaluate exactly to 1. Saturating this kernel can only introduce roots of unity, which are trivial modulo fifth powers here. Thus the tested geometric family gives neither a class-rank gain nor a nontorsion unit. It is stopped. This is a finite-family result, not an impossibility theorem for geometric constructions. [Arithmetic report](arithmetic/REPORT.md).

The older conditional 8,918-column generating budget is unchanged by these relations. The new analytic ceiling of 97 is a different kind of bound: it does not depend on that generator budget at all.

## Across-prime consequence and limit

[SCALING.md](theory/SCALING.md) derives the analogous formula for the actual point-field construction at an odd prime p. The full relative unit lattice has rank (p²−1)/4, while one faithful unit sector has dimension (p+1)/2. The class ceiling keeps the conductor, relative discriminant, regulator lower bound, and degree of the Hecke L-function explicit.

No larger-prime field or small bound was computed in this return. The formula does not show that the class contribution stays small across primes. Sharpening decimal constants in the present bound cannot resolve the difference between a ceiling of 100 and the needed rank-two control. A useful continuation must obtain substantially more information about the relevant p-primary classes or impose verified arithmetic constraints on them; the present whole-order estimate alone is insufficient.

## Ledger and grade

- **REMOVED:** dependence on a complete collected factor base for this coarse coefficient-five class bound.
- **EXCLUDED:** this fixed 31-function family as a source of new closed class rank or nontorsion units; universal norm reductions through strictly smaller permutation fields in the screened setting.
- **OPEN:** a sufficiently small complete unit/class bound; its behavior across coefficient primes; FIN, ORDER9 and Q36.

The bound is a written application of published mathematics plus explicit lattice and norm deductions, supported by exact arithmetic and a separate agent's desk review. It is not a novelty claim or a proof-assistant certificate. The independent review states precisely which ideal, rank, unit and numerical computations were replayed. [Review](review/FINAL_REVIEW.md) · [Replay instructions](REPLAY.md) · [Source boundaries](SOURCES.md).
