# Independent audit of the primitive quotient and BKS image lattice

Date: 2026-10-12.

**Verdict: PASS UNDER RETAINED RESIDUAL INPUT.** The claims in submitted `PROOF.md` §§2-3, equations (4)-(8), follow for the specified primitive geometric quotient from the retained surjectivity of `G_Q -> GL_2(F_p)` for each `p >= 5`. No additional exceptional prime, modular-degree divisor, cusp-count divisor, or unspecified lattice index enters this argument. The residual-image statement itself has not been freshly certified.

This audit does not certify §§4-7, the symbol value 144, a Kato coefficient, a height determinant, a Selmer group, or any new seed primary conclusion. It does not identify the lattice of an arbitrary earlier parametrization. No submitted file was changed.

## Identity and sources actually checked

The audited file is `submitted/BSD_FINITE_SOURCE_PALETTE_2026-10-12/PROOF.md`, SHA-256:

`ce4f48b9880d316eee820c4a5987cdd322ae48a6c513e507d393739f94cba13e`.

1. Burns-Kurihara-Sano, *On derivatives of Kato's Euler system for elliptic curves*, JMSJ 76 (2024), §2.1, printed pp. 863-864, equations (2.1.1)-(2.1.3). [Publisher PDF](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en). The two complete relevant pages were downloaded, rendered, and visually inspected. In particular, the arrow is the subscripted pushforward `phi_*`, not `phi^*`.
2. Mascot, *Moduli-friendly Eisenstein series over the p-adics and the computation of modular Galois representations*, §2.3, equations (2.3.2)-(2.3.3), Example 2.3.4. [Author's published article](https://link.springer.com/article/10.1007/s40993-022-00329-6). The cusp-field and rational-basepoint claims were checked in the full publisher text.
3. Milne, *Lectures on Etale Cohomology*, Theorem 16.1 and Corollary 16.2, and §24 on the Gysin map. [Author's notes](https://www.jmilne.org/math/CourseNotes/LEC.pdf). These give the localization/purity and proper-pushforward framework used below. Only the smooth characteristic-zero curve case is needed.
4. Milne, *Abelian Varieties*, Chapter IV, Lemmas 2.1-2.2. [Author's notes](https://www.jmilne.org/math/CourseNotes/AV.pdf). These record the Galois-stable-kernel quotient and isogeny/Tate-module facts; the connected-kernel argument is supplied explicitly below.
5. Fukaya-Kato, *On conjectures of Sharifi*, August 15, 2012 version, §1.9.3, printed p. 28, the exact reference cited by BKS. [Research preprint](https://www.math.ucla.edu/~sharifi/sharificonj.pdf). This identifies the Manin-Drinfeld splitting as the unique Hecke-compatible rational left inverse.
6. Scholl, *An introduction to Kato's Euler systems*, §5.2, printed pp. 451-452, also cited by BKS. [Author's reprint](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf). Its rational Hecke idempotent realizes the retraction for every coefficient prime. The source was downloaded and its relevant text inspected. Its auxiliary integer used for general parametrizations is not imported into this proof.

The downloaded publisher BKS PDF has SHA-256 `bc930bdfc4a979b80e03f953068842fcc30b12edb6edc2530290763724596386` and is held locally at `tmp/pdfs/BKS.pdf`. It is a source cache, not a new mathematical certificate or a published artifact.

## 1. Exact match to the BKS map

Write `X = X_1(N)`, `Y = Y_1(N)`, `T = T_pE`, and `V = T tensor Q_p`. The BKS map is

\[
H^1(Y_{\overline{\mathbf Q}},\mathbf Z_p(1))
 \longrightarrow H^1(Y_{\overline{\mathbf Q}},\mathbf Q_p(1))
 \xrightarrow{s}H^1(X_{\overline{\mathbf Q}},\mathbf Q_p(1))
 \xrightarrow{\phi_*}H^1(E_{\overline{\mathbf Q}},\mathbf Q_p(1))
 \simeq V.
\]

Here `s` is the rational Manin-Drinfeld retraction, and the final self-duality uses the elliptic curve's Weil pairing. Its restriction to the integral elliptic cohomology identifies that lattice with `T`, because the Weil pairing is perfect integrally. It inserts no modular degree and no nonunit scalar. Denote the full composite by `h` and its image by `T_phi`.

This agrees with the submitted definition. The retraction is Galois equivariant and is the identity on proper-curve cohomology. Its rational nature can create an over-lattice in principle; one must prove that any such over-lattice is absent here. BKS's observation that an irreducible residual representation allows a choice with `T = T_pE` is not by itself being used to authenticate this particular fixed map.

For clarity, the equivariance follows from the defining splitting, not merely from the assertion that its image happens to be stable. Fukaya-Kato §1.9.3 gives the unique Hecke-compatible rational left inverse; its uniqueness persists after extension from `Q` to `Q_p`, since the retraction and commutation conditions are finite-dimensional linear equations. The Hecke correspondences on `X_1(N)` and `Y_1(N)` are defined over `Q` and commute with the Galois action. For any `g` in `G_Q`, the conjugate `g s g^{-1}` is consequently another Hecke-compatible left inverse, so uniqueness forces `g s g^{-1}=s`. Equivalently, Scholl realizes the retraction by a rational Hecke projector. This is the same retraction in the Betti and etale realizations under comparison.

No period is introduced or changed in this identification. The source-lattice equality proved below is prior to, and independent of, any choice of Neron differential, Manin constant, real period, or distinguished symbol. In particular, BKS's later shorthand in Remark 2.3 is not a substitute for this actual-map argument.

## 2. Least-degree isogeny: the argument is valid

Let `psi:E_1 -> E` have least positive degree among rational isogenies in this direction. Duality preserves degrees and exchanges the two directions, so its dual `psi_hat:E -> E_1` is also of least degree in its direction.

If `p` divides `deg(psi_hat)`, its finite kernel in characteristic zero has a nonzero subgroup of points killed by `p`. Thus

\[
0\ne\ker(\widehat\psi)\cap E[p]\subseteq E[p]
\]

is Galois stable. Irreducibility of `E[p]` makes this subgroup all of `E[p]`. Consequently `psi_hat` factors over `Q` through the quotient by `E[p]`, namely `[p]:E -> E`. The resulting rational isogeny `E -> E_1` has degree `deg(psi_hat)/p^2`, contradicting minimality. Therefore `p` does not divide `deg(psi)`.

The submission correctly uses irreducibility on `E`, not an unproved assertion about `E_1[p]`. The factorization is over `Q`: `[p]`, its kernel, and the original morphism are defined there, and the quotient universal property descends the factor. Hence `T_p(psi)` is an isomorphism, with inverse `deg(psi)^{-1} T_p(psi_hat)`.

This argument is specific to the least-degree isogeny. For example, postcomposing any admissible map with `[p]` invalidates this conclusion for that new map.

## 3. Connected kernel really gives integral proper-image surjectivity

Put `A = ker(q_1)`. Because `q_1:J_1(N) -> E_1` has connected kernel in characteristic zero, `A` is an abelian variety and

\[
0\longrightarrow A\longrightarrow J_1(N)\xrightarrow{q_1}E_1\longrightarrow0
\]

is exact. The consequence for Tate modules does not require the modular degree to be a unit.

For each `n`, take `b` in `E_1[p^n]` and a geometric lift `x` in `J_1(N)`. Then `p^n x` lies in `A`. Multiplication by `p^n` is surjective on `A(\overline Q)`, so choose `a` in `A` with `p^n a = p^n x`. The point `x-a` lies in `J_1(N)[p^n]` and maps to `b`. Thus the sequence on `p^n`-torsion is surjective on the right. The transition maps on `A[p^n]` are surjective, so taking inverse limits gives

\[
0\longrightarrow T_pA\longrightarrow T_pJ_1(N)
 \longrightarrow T_pE_1\longrightarrow0.
\]

The Kummer identification `H^1(X,Z_p(1)) = T_p Pic^0(X)` identifies proper pushforward with the map induced by the divisor norm. For `phi = psi q_1 i_0`, this is exactly `T_p(psi q_1)`. Combining the preceding surjectivity with the isomorphism `T_p(psi)` proves

\[
h\bigl(H^1(X_{\overline{\mathbf Q}},\mathbf Z_p(1))\bigr)=T_pE.
\]

The rational cusp `0` is legitimate in the point-level model: Mascot's pair for it is `(c,d)=(1,0)`, whose Galois action fixes it. Therefore the stated Abel-Jacobi map is rational. Translation would not change the induced map on first cohomology, but no translation is needed for the stated construction.

## 4. Localization: degree-zero permutation module, without a twist

For the nonempty geometric cusp set `C = X-Y`, the relevant segment of purity/localization is

\[
0\to H^1(X,\mathbf Z_p(1))\to H^1(Y,\mathbf Z_p(1))
 \xrightarrow{\partial} H^0(C,\mathbf Z_p)
 \xrightarrow{\deg} H^2(X,\mathbf Z_p(1))\to0.
\]

All curves in this display are over `\overline Q`. The two last modules are respectively `Z_p[C(\overline Q)]` and `Z_p`; each geometric cusp has degree one, so `deg` is summation. The coefficient twist `(1)` cancels the codimension-one purity twist `(-1)`. This gives exactly

\[
0\to H^1(X,\mathbf Z_p(1))\to H^1(Y,\mathbf Z_p(1))
 \to B_C\to0,\qquad
B_C:=\ker\bigl(\mathbf Z_p[C(\overline{\mathbf Q})]\xrightarrow{\sum}\mathbf Z_p\bigr).
\]

There is no need to divide by the number of cusps, to split summation Galois equivariantly, or to assume that this number is prime to `p`. The exact sequence remains valid even when `p` divides the conductor; only characteristic zero is used here. The subsequent ordinary-prime applications can impose their separate good-reduction restriction.

## 5. The finite boundary quotient vanishes

By §3, `T` is contained in `T_phi`. Since `T_phi` is a finitely generated full `Z_p`-lattice in `V`,

\[
D_p:=T_\phi/T
\]

is a finite `p`-group. The map `h` modulo `T` vanishes on proper cohomology, so it induces a **surjective Galois-equivariant map**

\[
B_C\twoheadrightarrow D_p.
\]

This quotient step is valid even though the rational retraction `s` need not preserve the full integral proper lattice.

Mascot's formula shows that all cusps are defined over `Q(mu_N)`. Therefore the action on `B_C`, and hence on `D_p`, factors through an abelian finite quotient of `G_Q`. On the other hand the actual inclusion of lattices gives a Galois-equivariant embedding

\[
D_p\hookrightarrow V/T\simeq E[p^\infty].
\]

Suppose `D_p` were nonzero. Then `D_p[p]` would be a nonzero submodule of `E[p]` on which every Galois commutator acts trivially. The retained surjectivity `rho_p(G_Q)=GL_2(F_p)` implies

\[
\rho_p([G_{\mathbf Q},G_{\mathbf Q}])
 =[\mathrm{GL}_2(\mathbf F_p),\mathrm{GL}_2(\mathbf F_p)]
 =\mathrm{SL}_2(\mathbf F_p)\quad(p\ge5).
\]

The standard representation has no nonzero `SL_2(F_p)`-fixed vector: an upper elementary unipotent fixes only the first coordinate line, and a lower elementary unipotent fixes only the second. Thus `D_p[p]=0`, a contradiction. Consequently

\[
\boxed{T_\phi=T_pE\quad\text{for every }p\ge5
\text{ with the retained residual surjectivity}.}
\]

Only this last exclusion uses more than the irreducibility used in §2. The submitted proof has the stronger hypothesis available and uses it correctly. Merely asserting residual homothety would not establish the displayed equality of the actual lattices.

## 6. Betti comparison and exact scope

The appropriate explicit reading of submitted line 118 is

\[
\mathcal H_\phi\otimes\mathbf Z_p
 =H_1(E(\mathbf C),\mathbf Z)\otimes\mathbf Z_p
 \qquad(p\ge5),
\]

under the compatible Betti/etale comparison, where `mathcal H_phi` is the actual image in BKS (2.1.2). Equivalently the two rational Betti lattices agree after localization at `p`. This does **not** assert global equality over `Z`, and it does not remove possible factors supported at `2` and `3`. Stating this displayed localized identity would improve precision, but no correction to the submitted `p >= 5` argument is required.

The construction uses one fixed geometric map before varying `p`. Its existence is sufficient for the theorem; this audit does not produce equations for the enormous-level optimal quotient or evaluate the map. The result proves the requested absence of a `p >= 5` image-lattice normalization defect for this newly specified family. It supplies no bound on a Kato source's arithmetic divisibility, no height nondegeneracy, no Sha vanishing, and no cross-prime scalar law.

## Hostile controls and disposition

| Proposed failure | Disposition |
|---|---|
| The isogeny may have a `p`-part because only `E[p]` is known irreducible | Removed by applying irreducibility to the dual least-degree isogeny |
| Connectedness only gives rational, not integral, Tate-module surjectivity | Removed by explicit lifting on `p^n`-torsion and exact inverse limit |
| BKS uses a pullback divided by modular degree | Excluded by the actual printed pushforward and integral Weil pairing |
| The cusp boundary retains a cyclotomic twist | Excluded by coefficient/purity twist cancellation |
| A prime dividing the cusp count must be removed | Excluded; no averaging or cusp-count division occurs |
| A finite abelian-action over-lattice quotient survives inside `E[p^infinity]` | Removed by the commutator/`SL_2` fixed-space argument |
| Equality for this map authenticates arbitrary historical source maps | Excluded; `[p]phi` is an immediate negative control |
| Betti equality is global over `Z` | Excluded; the conclusion here is at each `p >= 5` |
| The seed's all-prime residual-image theorem is now independently certified | Open outside this audit; it remains a retained input |

No theorem-level repair to §§2-3 is required. The expanded arguments above make the integral exactness and finite-quotient step reviewable without promoting any retained arithmetic input.
