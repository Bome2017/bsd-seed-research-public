# Review: the seed's cyclotomic 5-tower and single-table extraction

Date: 2026-10-12.

**Verdict: CYCLOTOMIC_5_TOWER_DEDUCTION_SUPPORTED_UNDER_RETAINED_INPUTS; ONE_TABLE_EXTRACTION_SUPPORTED.**

The submitted deduction supplies a seed-specific arithmetic consequence, rather than another conditional nonvanishing criterion: the old certified unit coefficient, together with the stated ordinary Kato and Greenberg inputs, gives rank two and zero 5-primary Sha in every finite layer of the cyclotomic Z_5-extension. This review supports that conclusion at written-proof grade under the retained arithmetic inputs.

There is also a further consequence, using the project's stronger retained residual-image input at every prime ell>=5: **the entire Mordell–Weil group is unchanged throughout this tower**, not just its rank. The proof is in [TOWER_AUDIT.md, Section 6](TOWER_AUDIT.md#6-optional-stronger-point-group-consequence).

Neither conclusion settles a new coefficient prime over Q. FIN, ORDER9 and Q36 remain unchanged. This is separate same-team model review, not independent human certification, formal verification, or a novelty claim.

## 1. Exact review scope

Reviewed author return: [c728f2d2c993f480d99de297906e8482838419f9](https://github.com/Bome2017/bsd-seed-lab/tree/c728f2d2c993f480d99de297906e8482838419f9/work/returns/BSD_CYCLOTOMIC5_AND_MOMENT_2026-10-12), branch `research/cyclotomic5-moment-2026-10-12`.

All ten published files were exported directly from that commit. Their nine manifest entries verify. The supplied replay reproduces its saved output byte-for-byte, and all five listed historical document/table Git bindings match the pinned baseline. No producer-side local ZIP was supplied in this turn; the source archive accompanying this review is explicitly our export of the pinned Git tree, not an independently authenticated copy of an unseen producer ZIP.

Separate review covered:

- [TOWER_AUDIT.md](TOWER_AUDIT.md): published Iwasawa inputs, actual Selmer module, finite-kernel elimination, finite-layer restriction, and the stronger point-group corollary.
- [MOMENT_AUDIT.md](MOMENT_AUDIT.md): primary measure convention, layer indexing, integrality, transfer contribution, sharp precision, and an independent replay of the actual saved symbols.

The old large Fourier/Arb computation, its denominator theorem, the rank and residual-image certificates, and the prior source-normalization chain retain their existing grades. Their full original computations were not rerun.

## 2. Why the tower statement follows

Let Q_n be the unique degree-5^n subfield of Q(mu_(5^(n+1))), Q_infinity their union, Lambda=Z_5[[U]], and X the dual of the usual 5-infinity Selmer group over Q_infinity. It is not the full-S Iwasawa H^2 of the earlier Bockstein argument.

The two point directions inject into the infinite-layer Selmer group. Indeed, absence of rational 5-torsion implies absence of 5-power torsion in this pro-5 extension, and inflation–restriction is then injective. Dualizing the point injection gives the actual map

\[
X\twoheadrightarrow(\Lambda/(U))^2.
\]

The retained good ordinary/full-image hypotheses give integral ordinary Kato divisibility, as stated in Stein–Wuthrich Section 6.1, Proposition 7.2 and Theorem 7.3. The point quotient forces U^2 to divide the characteristic series, and therefore the standard L-series. The saved coefficient is a unit, so

\[
L_{\mathrm{std},5}=U^2u(U),\qquad u\in\Lambda^\times,
\qquad\operatorname{char}_\Lambda X=(U^2).
\]

Let C be the kernel of the point quotient. Multiplicativity gives char(C)=(1). Since Lambda is a two-dimensional regular local ring, this finitely generated torsion module is supported only at its maximal ideal, hence is finite. **Greenberg Proposition 4.14 excludes this finite submodule**, so C=0. This directly proves

\[
\boxed{X\simeq(\Lambda/(U))^2}
\]

through the actual point quotient map, rather than merely up to pseudo-isomorphism. Greenberg's hypotheses here are cyclotomic Selmer cotorsion and absence of base-field p-primary torsion. Its proof does not assume finiteness of the original base Selmer group or of Sha. The relevant appendix generalizes the earlier finite-base-Selmer discussion.

For each n, restriction on Selmer groups is injective. Its image contains the already exhaustive base-field point subgroup, so it is also surjective. Compatibility of Kummer maps then gives

\[
\boxed{\operatorname{rank}E(\mathbf Q_n)=2,\qquad
\Sha(E/\mathbf Q_n)[5^\infty]=0\quad(n\ge0).}
\]

No finite-layer Sha finiteness, height nondegeneracy, or main-conjecture equality was assumed. The finite-module issue is removed by a theorem about this Selmer module, not by discarding it in characteristic-ideal notation. See the detailed audit for the exact source hypotheses and negative controls.

## 3. Further consequence: no new points in the tower

Add the already retained input that E[ell] is irreducible over Q for every prime ell>=5. This is stronger than the mod-5 input needed for the tower theorem above, and it is not freshly certified here.

For such an ell, the subgroup \(E[\ell](\mathbf Q_n)\) is G_Q-stable. Irreducibility makes it zero or all of E[ell]. The latter would put Q(mu_ell) in Q_n by the Weil pairing, impossible since ell-1 is even and [Q_n:Q] is odd. Hence there is no ell-primary torsion for ell>=5.

For ell=2 and 3, the degrees of the full ell^k-division fields divide

\[
|\mathrm{GL}_2(\mathbf Z/\ell^k)|
=\ell^{4(k-1)}(\ell^2-1)(\ell^2-\ell).
\]

These orders are prime to 5. Their intersection with Q_n is Q, so no new 2- or 3-primary torsion appears either. Thus E(Q_n)_tors=E(Q)_tors=Z/2.

The rank equality makes E(Q_n)/E(Q) finite. For any point P, some mP is rational, so sigma(P)-P is torsion and therefore belongs to the rational Z/2. The map sigma -> sigma(P)-P is then a homomorphism from Gal(Q_n/Q), a 5-group, to Z/2, so it is zero. Every P is rational. Consequently

\[
\boxed{E(\mathbf Q_n)=E(\mathbf Q)\text{ for all }n,
\qquad E(\mathbf Q_\infty)=E(\mathbf Q).}
\]

This is an additional written deduction from the accepted tower argument and stronger retained image input, with a separate same-team check. It concerns actual point groups, not just equality after tensoring. No number-field point search was required. It remains a result in the field direction at the cyclotomic prime 5.

## 4. The old coefficient was genuinely replayed

Both supplied tables agree with their original pinned Git blobs. Independent grouping and direct discrete-log evaluation recover

\[
(-76,0,-76,76,76),\qquad
\Theta_2(U)=380U+608U^2+380U^3+76U^4.
\]

The original tables use omega_1 and the standard measure uses Omega_E=2 omega_1. Hence the quadratic moment is 304. With alpha=3 mod 5, the standard infinite coefficient is

\[
L_{2,5}\equiv\alpha^{-2}\cdot304\equiv1\pmod5.
\]

The four exact plus-symbol Hecke relations also pass. In this particular replay, the lower table's augmentation is exactly zero, so its transferred polynomial is zero. That does not upgrade the precision of the infinite coefficient beyond modulo 5. The lower-degree terms of the finite approximant are not lower-degree terms of the infinite series.

This is a fresh replay of an old residue. No new symbol or coefficient digit was computed, and the tower statement remains conditional on the historical certification of these symbol values.

## 5. The one-table formula and its limits

The submitted congruence checks:

\[
L_{2,p}\equiv
(1-p/\alpha^2)\alpha^{-n}A_n\pmod{p^{n-1}}
\qquad(n\ge2).
\]

Here A_n is the correctly normalized raw quadratic moment at denominator p^n, with gamma=1+p and integral symbol/measure inputs. Both the lower-table transfer and its precision cost are retained. A nonzero residue gives the exact numerator valuation; a zero residue gives only a lower bound. Extra unit-root digits cannot recover a digit absent from the finite measure projection.

The extractor passes separate mathematical review and saved-data replay. Its general proof does not require constant and linear terms of the infinite series to vanish. Its precision-sharpness examples remain abstract integral measures, not additional seed examples.

One citation locator needs correction: the Stein–Wuthrich distribution and finite-polynomial definitions are in Section 3, printed pp.1762–1763, not subsection 3.1. The formula itself is unchanged. The original submission is preserved; this review carries the locator correction.

For the retained matched height valuation at 17, denominators 4913 and, if necessary, 83521 have the stated precisions for testing valuations one and two. Neither table was computed here. Reducing the verifier's input to one table does not reduce or certify the cost of generating that table, and does not predict that the test succeeds.

## 6. Seed significance and remaining scope

The tower result is a substantive consequence for the actual seed under retained inputs: all finite cyclotomic 5-power layers have zero 5-primary Sha, and the stronger image input gives no new points. It should not be described merely as another proposed criterion.

It also does not supply the missing control over coefficient primes over Q. The ordinary coefficient-to-height ratio still requires new arithmetic values or a uniform bound. Supersingular and exceptional-primary coverage, ORDER9 and Q36 are unaffected. No statement about the other tame components of the full cyclotomic fields follows from this argument.

The two audits, source bindings, nine-entry input manifest, supplied replay and separate saved-data checker are included. The supplied controls contain 84 compatible synthetic extraction cases, five sharpness cases, eight invalid-input cases and four precision boundaries. The separate check adds 20 transfer-coefficient cases and its own saved-table calculation. These tests are not formal verification of the tower theorem.

Primary references actually checked: [Stein–Wuthrich, published offprint](https://www.wstein.org/papers/mcom2649-iwasawa-alg.pdf), Sections 3 and 6.1, Proposition 7.2 and Theorem 7.3; [Greenberg, arXiv:math/9809206v1](https://arxiv.org/pdf/math/9809206), Proposition 4.14 and surrounding proof. The original full Kato proof and the project's full residual/rank/symbol certification chain were retained rather than rebuilt.
