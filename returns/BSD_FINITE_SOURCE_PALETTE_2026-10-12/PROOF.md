# A primitive geometric source and a finite smoothing palette

Date: 2026-10-12.
Baseline: `Bome2017/bsd-seed-lab@581f7a26a1d110bcd6131739f94569e4810a719e`.
Grade: **DERIVED_UNDER_RETAINED_INPUTS; REVIEW_REQUIRED.**

This is a written source-normalization construction, not a computation of a Kato coefficient, a proof of a relative-divisibility bound, or a novelty claim. The construction specifies a new source family. It does not authenticate the absolute scale of an arbitrarily chosen earlier source.

## 1. Statement and retained arithmetic

Retain the seed

\[
E:[0,-1,0,-66020924,-65074271436],\qquad
N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843=6503188012738584.
\]

Retain its non-CM property, rank-two saturated point lattice, and the surjectivity of its residual representation onto GL2(Fp) for every p >= 5. Retain the October 7 source-matched weak-order and integral Kato inequalities and the October 12 corrected Bockstein/height certificate. These are not independently recertified here.

Let

\[
\mathcal D=\{p\ge5:p\nmid N,\ p\notin\{19,59,487\}\}.
\]

Write H_p for the actual BKS height matrix in the common U = gamma - 1 coordinate, on the retained saturated point basis. Write L_std,p for the ordinary modular-symbol measure with the fixed Neron real period and the interpolation convention specified in the predecessor `COFINITE_NORMALIZATION.md`, and L_2,p = [U^2]L_std,p. A convention-independent name such as “the p-adic L-function” does not suffice to identify these objects.

**Derived result.** There is a fixed primitive geometric quotient and a fixed set of three smoothing pairs, specified below, such that for every ordinary p in D a selected pair defines an admissible actual integral Kato source with

\[
 v_p(K_p)=v_p(L_{2,p}),                         \tag{1}
\]

where zero on either side means zero on both sides. No unspecified image-lattice or smoothing-prime support has to be removed for this family. Consequently the retained corrected certificate gives

\[
\boxed{L_{2,p}\ne0,\quad\det H_p\ne0,\quad
v_p(L_{2,p})-v_p(\det H_p)\le1
\ \Longrightarrow\ \Sha(E/\mathbf Q)[p^\infty]=0.}       \tag{2}
\]

The domain restrictions, actual height convention, and retained Kato hypotheses are part of (2). No upper bound for the left-hand valuation difference is proved here.

The source ingredients below use the normalized rational weight-two newform f of E, the rational Manin--Drinfeld splitting in BKS (2.1.1), standard Jacobian/Tate-module identifications, and the cusp-field and Manin-constant inputs specified in SOURCES.md.

## 2. Choose a primitive quotient before p varies

Let

\[
 q_1:J_1(N)\twoheadrightarrow E_1
\]

be the optimal elliptic quotient associated with f; its kernel is connected. Choose a nonzero rational isogeny psi: E_1 -> E of least degree. Fix its sign, and form the modular parametrization

\[
 \phi=\psi\circ q_1\circ i_0:X_1(N)\longrightarrow E,
 \qquad i_0(x)=[x]-[0].                         \tag{3}
\]

Here 0 denotes the rational cusp 0. In the model of X_1(N) classifying an elliptic curve with a point of order N, the cusp infinity is generally not rational. The explicit cusp description in Mascot, Section 2.3, supplies this distinction. Translation of a parametrization would not change the induced cohomology map, but (3) fixes an actual rational map without that ambiguity.

### 2.1 The isogeny has no p-part for p >= 5

**Derived lemma.** If E[p] is irreducible, p does not divide deg(psi).

Indeed, duality identifies the degrees of psi and its dual, and a smaller-degree isogeny E -> E_1 would dualize to a smaller one E_1 -> E. Thus the dual psi-hat is also of least degree. If p divided its degree, ker(psi-hat) would have nonzero p-torsion. The Galois-stable subgroup

\[
 \ker(\widehat\psi)\cap E[p]
\]

would then be a nonzero submodule of E[p]. Irreducibility forces it to be all of E[p]. The map psi-hat would factor through [p]: E -> E, yielding an isogeny E -> E_1 of degree deg(psi)/p^2, a contradiction. This proof uses irreducibility on E itself, not an unproved assertion about the residual image of E_1.

Since a connected-kernel quotient of abelian varieties is surjective on Tate modules, (3) therefore gives

\[
 \operatorname{im}\bigl(H^1(X_1(N)_{\overline{\mathbf Q}},\mathbf Z_p(1))
                \xrightarrow{\phi_*}T_pE\bigr)=T_pE.   \tag{4}
\]

The map is the pushforward under Poincare duality, equivalently the map on Tate modules of the Jacobians. It is not a pullback divided by the modular degree.

## 3. The open modular curve adds no p-denominator

Let X = X_1(N), Y = Y_1(N), and C = X - Y. Put T_phi equal to the image lattice of BKS (2.1.1), using the fixed phi of (3). The rational Manin--Drinfeld projection restricts to the identity on proper-curve cohomology. Thus (4) implies

\[
 T_pE\subseteq T_\phi\subseteq V_pE.                    \tag{5}
\]

Both terms in (5) are full lattices, so T_phi/T_pE is finite. Localization for the smooth proper curve with its cusps removed gives

\[
0\to H^1(X_{\overline{\mathbf Q}},\mathbf Z_p(1))
\to H^1(Y_{\overline{\mathbf Q}},\mathbf Z_p(1))
\to \mathbf Z_p[C(\overline{\mathbf Q})]^0\to0.           \tag{6}
\]

The last term denotes the kernel of summation in the cusp permutation module. There is no remaining cyclotomic twist on this boundary term: the coefficient twist (1) cancels the purity twist for a divisor.

Every cusp is defined over Q(mu_N). Therefore the action on the last term of (6) factors through an abelian quotient of G_Q. As the quotient T_phi/T_pE is an image of that boundary module, it too has abelian Galois action.

On the other hand, (5) embeds it in

\[
 V_pE/T_pE\simeq E[p^\infty].                           \tag{7}
\]

The image of the commutator subgroup of G_Q on E[p] contains SL2(Fp), because the residual image is GL2(Fp). The standard two-dimensional SL2(Fp)-module has no nonzero fixed vector. For example, the upper and lower elementary unipotents already have zero common fixed space. Consequently E[p] has no nonzero submodule with abelian Galois action. Any nonzero finite p-subgroup in (7) with abelian action would have nonzero p-torsion and give such a submodule. This is impossible.

We have proved the actual lattice equality

\[
 \boxed{T_\phi=T_pE\quad\text{for every }p\ge5.}        \tag{8}
\]

The same conclusion holds after compatible Betti/etale comparison for the Betti image lattice of this fixed rational map. Only the good-prime portion of (8) is used below.

This is the step that replaces the predecessor's unspecified integer J. It depends on selecting (3). For an arbitrary multiple [a]phi with p | a, the proper image in (4) is no longer T_pE; this argument does not assert equality for that different map. General residual homothety alone is not being mistaken for equality.

## 4. Bind the one-fifth symbol to the primitive plus line

Write omega_f = 2*pi*i*f(z) dz. Let mu_1 and mu_0 be the Manin constants of the optimal newform elliptic quotients of J_1(N) and J_0(N), respectively, measured with minimal Neron differentials. The imported Manin-constant input is that mu_0 is a p-unit at good p >= 5. The seed already retains a stronger good-prime conclusion; no additive-prime Manin assertion is needed in this proof.

CNS Lemma 6.5 gives mu_0 = mu_1 times an integral Lie-cokernel index for these connected-kernel quotients. Hence mu_1 is a p-unit at every good p >= 5. The least-degree isogeny psi has degree prime to p by Section 2. Its differential multiplier between Neron differentials is a p-unit: the multiplier of its dual is integral and the product is deg(psi). Thus

\[
 \phi^*\omega_E=\mu_\phi\omega_f,\qquad
 \mu_\phi\in\mathbf Z_p^\times\quad(p\ge5,\ p\nmid N). \tag{9}
\]

This does not claim that a general nonoptimal parametrization has unit Manin constant. Multiplication of the target by p is an immediate counterexample to that overstatement. No degree of X_1 -> X_0 is inverted in (9).

Fix

\[
 \xi=\begin{pmatrix}1&0\\5&1\end{pmatrix},
 \qquad\{\xi(0),\xi(\infty)\}=\{0,1/5\}.               \tag{10}
\]

The retained symbol receipt used in `COFINITE_NORMALIZATION.md` has [1/5]^+ = 144 in the omega_1 real-period convention, and central value zero. Its only use here is the valuation statement: the normalized plus integral of this relative symbol is a p-unit for every p >= 5, because 144 = 2^4*3^2. Passing between the real-component and primitive real-cycle conventions can introduce a factor 2; it cannot introduce a prime >= 5. If the receipt is expressed with the old minimal X_0 parametrization rather than omega_f, (9) and the retained good-prime Manin unit give the same valuation statement. The numerical receipt itself is not freshly replayed.

Combining that retained integral with (9), and then using the lattice equality (8), proves that the plus projection of the image of (10) is primitive in the actual p-adic plus lattice. Thus this one fixed xi satisfies BKS (2.1.3) at every good p >= 5, and its real period obeys

\[
 \Omega_\xi/\Omega_E\in\mathbf Z_p^\times.             \tag{11}
\]

We do not identify the exact rational multiplier in (11), because only its valuation is required. The specified conventions are enough for that valuation. A future exact coordinate calculation must also fix its sign and real-period factor.

## 5. Three fixed smoothing pairs cover all good p >= 5

Set

\[
 M=6N=39019128076431504,\qquad c_i=1+iM\quad(1\le i\le3).
\]

Explicitly,

\[
(c_1,c_2,c_3)=
(39019128076431505,\ 78038256152863009,\ 117057384229294513).
\]

Fix the three pairs (c_1,c_2), (c_1,c_3), (c_2,c_3). Each entry is greater than one, congruent to one modulo N, and coprime to 6N. The entries are pairwise coprime: for adjacent pairs use the obvious integer combinations; for (c_1,c_3), the gcd divides 2 and both entries are odd.

At a good p >= 5, p does not divide M, and p does not divide i for 1 <= i <= 3. Thus none of the c_i - 1 is zero modulo p. At most one c_i can be zero modulo p, since the difference of two of them is (i-j)M and 0 < |i-j| <= 2. Consequently some pair has

\[
 p\nmid c_ic_j(c_i-1)(c_j-1).                          \tag{12}
\]

Choose the lexicographically first such pair. For this pair cd is coprime to 6 and every finite prime in S = {infinity, p, primes dividing N}. These are the BKS Section 2.1 admissibility requirements. The actual smoothing series has augmentation

\[
 t_{c,d}(0)=cd(c-1)(d-1)\in\mathbf Z_p^\times.          \tag{13}
\]

This selects an admissible integral source, not a quotient of a source with a nonunit smoothing factor. The choice is fixed as p varies except for selecting one of the same three pre-specified pairs. Each selected source has its own ordinary Euler-system construction at that coefficient prime; no mixed-prime Euler-system compatibility is being asserted.

A useful exact control is

\[
 \gcd_{i<j}\{c_ic_j(c_i-1)(c_j-1)\}=M^2.              \tag{14}
\]

After removing M^2 the three entries are 2c_1c_2, 3c_1c_3, and 6c_2c_3. Their gcd is one: primes >= 5 are excluded by pairwise coprimality, and the appropriate entries exclude 2 and 3 because c_i = 1 mod 6. This proves (14), not just its finite numerical tests.

Equation (14) is a statement about source normalization, not about Sha support. In particular it is not a fixed Sha annihilator. One must not combine all three sources at a prime where one pair is inadmissible by appealing to a Bezout identity.

The former single pair fails at p = 5 because 5 | c_1. The palette selects (c_2,c_3) there. This repairs a source-admissibility exception; it is not a new result about Sha[5].

## 6. Compare to the standard ordinary measure

Retain the full interpolation comparison in the October 7 fixed-source note. It uses the same minimal differential, primitive source period, cyclotomic generator, character direction and p-Euler convention. For the selected actual smoothed source the quadratic leading-coefficient comparison is

\[
 K_p=t_{c,d}(0)\,(\Omega_E/\Omega_\xi)\,c_N\,L_{2,p},   \tag{15}
\]

up to an integral unit if a unit basis identification is left unspecified. This qualification changes no valuation or nonzero assertion. One must not substitute a bare numerical series bearing a similar name for the specified standard measure.

Here

\[
 c_N=(1+1/3)(1-1/2243)(1+1/5843)
 =\frac{17469664}{13105849}
 =\frac{2^5\cdot19\cdot59\cdot487}{2243\cdot5843}.     \tag{16}
\]

The bad-prime Euler series has augmentation c_N. The separate p-Euler factor cancels exactly as in the retained interpolation comparison; it is not discarded a second time. The weak-order input makes the constant and linear coefficients vanish, so multiplication by these series affects the quadratic leading term only by their augmentations.

By (8), there is no additional p-homothety in the target lattice. By (11) and (13), both the period and smoothing factors in (15) are p-units at every good p >= 5. By (16), the remaining augmentation is a p-unit exactly after imposing the named exceptions in D. This proves (1), including its zero equivalence.

## 7. Compose with the reviewed height-ratio certificate

The retained review supplies, for a source-authenticated nonzero K and nonsingular matched H,

\[
 v_p(K)-v_p(\det H)
 =\operatorname{length}_{\mathbf Z_p}\Sha[p^\infty]+e_p,
 \qquad e_p\ge0                                     \tag{17}
\]

at ordinary p in D. Nonzero K supplies nonzero derivative via its retained zero-case implication before primary finiteness is used. Substitution of (1) into (17) gives

\[
 v_p(L_{2,p})-v_p(\det H_p)
 =\operatorname{length}_{\mathbf Z_p}\Sha[p^\infty]+e_p. \tag{18}
\]

Primary finiteness has already been obtained in this branch. The alternating Cassels--Tate pairing then makes its length even. An upper bound of one in (18) proves (2). The lower bound zero follows from (18); it is an input-consistency check, not another estimate to conjecture.

The source defect e_p survives. No claim is made that changing among the unit-smoothing pairs can reduce this intrinsic defect. Ordinary-prime restriction is essential for the standard numerical measure used here. The integral lattice and smoothing arguments themselves do not assert an ordinary height convention at supersingular primes.

## 8. What has, and has not, changed

The earlier finite-support proof allowed an uncomputed image-lattice index and excluded the support of a single smoothing pair. The present construction removes those two unspecified normalization issues for the family (3), (10), and Section 5. In that precise sense it connects the reviewed criterion to the standard ordinary leading coefficient on an explicit domain.

This is not an evaluation of that coefficient. It supplies no estimate for v(L_2) - v(det H), no proof that H is nonsingular cofinitely, and no new seed primary result. It does not retroactively rescale or identify all historical Kato-source packets. FIN, ORDER9, Q36, supersingular coverage and the remaining exceptional-primary obligations are unchanged.

The sources and retained inputs are listed in SOURCES.md. Checks exercise the palette algebra, simple residual-module controls and small finite-field arithmetic, not the global theorems used in (4), (6), (9), or (17). Independent review should target the exact direction of the cohomological pushforward, the boundary quotient in (6), and the provenance/convention of the retained 144 symbol.
