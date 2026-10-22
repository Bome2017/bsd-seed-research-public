# The fixed integral Eisenstein test for the seed

Date: 2026-09-19. This is a bounded theorem/source operation. The mathematical calculations below are written proofs, not machine formalizations. The full-image and rank-two seed inputs are retained from the [current seed record](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/SEED_PROVED_STATE.md).

**Result: ROUTE_KILLED_AT_DIRECTION.** The proposed classical GL(3) construction first fails at its characteristic-zero weight. The exact Galois target is singular; neither a common Tate twist nor a finite-order spectral-parameter jet repairs that classical obstruction. Nonclassical weight-two constructions do reach the standard Selmer group at a chosen prime, so weight alone is not a reason to dismiss every alternative allowed in the brief. The decisive failure across the checked alternatives is the direction: they give Selmer classes or lower bounds, not a fixed integral upper bound on the excess. This is a stopping condition for this operation, not an impossibility theorem for all future constructions.

## 1. The extension is correct; its eigenvalues forget the class

Let \(V=E[p]\), with its retained full \(\mathrm{GL}_2(\mathbf F_p)\)-image, and let \(c\in Z^1(\mathbf Q,V)\). Direct multiplication shows that

\[
 R_c(g)=\begin{pmatrix}\bar\rho(g)&c(g)\\0&1\end{pmatrix}
\]

is a representation if and only if \(c(gh)=c(g)+\bar\rho(g)c(h)\). Changes of the chosen lift of the quotient basis vector change \(c\) by a coboundary. Thus extensions with the two end terms identified are classified by

\[
 \operatorname{Ext}^1_{\mathbf F_p[G_{\mathbf Q}]}(\mathbf F_p,V)=H^1(\mathbf Q,V).
\]

Its determinant is \(\bar\epsilon_p\). For every \(g\),

\[
 \operatorname{tr}R_c(g)=1+\operatorname{tr}\bar\rho(g),\qquad
 \det(1-XR_c(g))=(1-X)\det(1-X\bar\rho(g)). \tag{1}
\]

These expressions are independent of \(c\). In particular the same Hecke-type characteristic polynomials occur for the split class, every Mordell–Weil class, and every possible excess Selmer class.

The infinitesimal version is equally exact. For \(A=\mathbf F_p[\eta]/(\eta^2)\), use off-diagonal block \(\eta c(g)\). Modulo strict changes of basis the fixed-block extension directions are \(H^1(\mathbf Q,V)\), but their image in the pseudorepresentation tangent space is zero. Equation (1) proves this without a conjecture. A generalized matrix algebra may retain off-diagonal extension data; its comparison with all Selmer classes is additional mathematics, not a consequence of knowing Hecke eigenvalues.

The quotient that matters remains

\[
 0\longrightarrow W\longrightarrow\operatorname{Sel}_p(E)
 \longrightarrow\Sha[p]\longrightarrow0,\qquad \dim W=2. \tag{2}
\]

No step identifies a Sha class with a preferred extension before taking this quotient.

## 2. Exact maximal-parabolic normalization

Let \(\pi_f\) be the **unitary normalization** of the automorphic representation of the weight-two newform of \(E\). Write \(\nu=|\cdot|_{\mathbf A}\), with \(|q|_q=q^{-1}\). At \(q\nmid N\), if

\[
 1-a_qX+qX^2=(1-\alpha_qX)(1-\beta_qX),
\]

then the Satake eigenvalues of \(\pi_{f,q}\) are \(\alpha_q/q^{1/2},\beta_q/q^{1/2}\).

We use the standard cohomological normalization in which the GL(3) arithmetic Galois Frobenius eigenvalues are \(q\) times its normalized Satake eigenvalues. For the maximal parabolic \(P_{2,1}\), the precise inducing datum is therefore

\[
 \boxed{I_E=\operatorname{Ind}_{P_{2,1}(\mathbf A)}^{\mathrm{GL}_3(\mathbf A),\,\mathrm{norm}}
 \left((\pi_f\otimes\nu^{1/2}\!\circ\det)\boxtimes\nu\right).} \tag{3}
\]

Its normalized Satake eigenvalues are

\[
 \alpha_q/q,\quad\beta_q/q,\quad1/q.
\]

Multiplication by \(q\) gives exactly \(\alpha_q,\beta_q,1\), and consequently the desired Euler polynomial

\[
 (1-X)(1-a_qX+qX^2).
\]

The central character of (3) is \(\nu^2\); the arithmetic determinant is \(\epsilon_p\), since \(q^3\cdot q^{-2}=q\). Thus there is no hidden extra cyclotomic character on the GL(1) block.

Equivalently, in the normalization where Satake eigenvalues themselves are the arithmetic eigenvalues, twist (3) by \(\nu^{-1}\circ\det\). Its datum becomes

\[
 \operatorname{Ind}^{\mathrm{norm}}_{P_{2,1}}
 \left((\pi_f\otimes\nu^{-1/2}\!\circ\det)\boxtimes1\right). \tag{4}
\]

Equations (3) and (4) are two declared normalizations of the same desired arithmetic parameter. They must not be combined with the other convention's Galois shift. The opposite parabolic permutes the constituents and does not change the semisimple target. Existence of a meromorphic analytic Eisenstein family from this datum is not existence of an integral cohomological Hecke point at it.

## 3. The classical weight obstruction

Use the question's Hodge–Tate convention: \(\epsilon_p\) has weight 1, and \(\rho_E\) has weights \(\{0,1\}\). The target has

\[
 \mathrm{HT}(1\oplus\rho_E)=\{0,0,1\}. \tag{5}
\]

The archimedean calculation makes the obstruction independent of terminology. The unitary discrete-series representation of a weight-two modular form has infinitesimal character \((1/2,-1/2)\). The GL(2) twist in (3) changes this to \((1,0)\), and the GL(1) constituent contributes 1. Thus

\[
 \boxed{\mathrm{IC}(I_{E,\infty})=\{1,1,0\}.} \tag{6}
\]

It is singular. If \(M_\lambda\) is a finite-dimensional algebraic representation of GL(3), with dominant integral highest weight \(\lambda_1\ge\lambda_2\ge\lambda_3\), nonzero relative Lie-algebra cohomology with coefficients \(M_\lambda^\vee\) requires infinitesimal character in the Weyl orbit of

\[
 \lambda+\rho_3=(\lambda_1+1,\lambda_2,\lambda_3-1).
\]

These three numbers are strictly decreasing. They cannot be the multiset (6). Equivalently, subtracting \(\rho_3=(1,0,-1)\) from the decreasing ordering \((1,1,0)\) gives \((0,1,1)\), which is not dominant.

Therefore this characteristic-zero Eisenstein parameter has **no classical GL(3) cohomological weight with finite-dimensional algebraic coefficients**, at any finite level. This includes classical Eisenstein cohomology and the algebraic local systems used in the Harder–Raghuram construction. The source supplies the infinitesimal-character criterion and discrete-series convention; the substitution above is the seed-specific type check. See [Harder–Raghuram, §§2.2.5–2.2.6 and 3.1.4](https://arxiv.org/pdf/1405.6513).

“Singular” here refers to the infinitesimal character, not merely to a highest weight lying on a dominance wall. For example, the trivial algebraic coefficient is allowed, but its \(\rho_3\)-shift is regular. That familiar example does not admit (6).

### Common twists and nearby regular weights do not preserve the target

A common Tate twist gives \(\{t,t,t+1\}\), still with a repetition. More generally, replacing the constituents by \(\rho_E(t)\) and \(\epsilon^j\) gives extension coefficient

\[
 \operatorname{Hom}(\epsilon^j,\rho_E(t))=\rho_E(t-j). \tag{7}
\]

Preserving the characteristic-zero standard representation requires \(t=j\), and again forces a repeated weight. Swapping the extension direction and dualizing gives the same obstruction.

For residual coefficients and a **fixed** pair of integers \(t,j\), preserving the standard representation for arbitrarily large \(p\) also forces \(t=j\). Indeed the full GL(2) image has no nontrivial determinant-power self-twist of its natural module. To check this, apply a hypothetical isomorphism \(V\otimes\det^d\simeq V\) to \(\operatorname{diag}(a,1)\). For every \(a\ne-1\), its nonzero trace implies \(a^d=1\). Choosing a generator of \(\mathbf F_p^\times\), which is not \(-1\) for \(p\ge7\), gives \(p-1\mid d\). An unbounded sequence of \(p-1\) cannot divide a fixed nonzero integer \(d=t-j\).

One can instead choose a twist depending on \(p\), such as \(j=t+p-1\), to preserve a residual character while separating characteristic-zero weights. This changes the algebraic coefficient essentially with \(p\) and does not supply the fixed integral object required in Stage B. Moreover equality of residual characters alone does not identify the crystalline extension condition at the new weight with the original finite-flat Kummer condition.

### Finite spectral-parameter jets do not repair classical cohomology

Let \(J^r I_E\) be any finite-order jet of the same inducing family at this singular parameter. It has a finite filtration whose subquotients have the infinitesimal character (6). Each subquotient has zero cohomology with every finite-dimensional algebraic coefficient by the preceding argument. The long exact cohomology sequences therefore give

\[
 H^\bullet(\mathfrak{gl}_3,K_\infty;J^r I_E\otimes M_\lambda^\vee)=0
 \quad\text{for every finite }r. \tag{8}
\]

Equivalently, its generalized central character remains singular; a central element separating it from the regular character of the coefficient acts invertibly on the entire finite jet. Thus merely differentiating this Eisenstein family twice cannot insert it into the missing classical cohomology group. Equation (8) does not rule out new nonclassical categories or a different arithmetic comparison theorem.

## 4. Exact local conditions on the extension directions

The weight obstruction is not a defect in the Selmer-to-extension construction. Its exact local deformation condition is

\[
 c|_{G_{\mathbf Q_q}}\in
 \mathcal L_q:=\delta_q(E(\mathbf Q_q)/p)\subset H^1(\mathbf Q_q,E[p]). \tag{9}
\]

Together with fixed diagonal constituents and fixed determinant, these specify the relevant extension functor. They do not identify it with an automorphic deformation functor.

At a good coefficient prime \(p\ge7\), rational 2-torsion and Hasse's bound imply \(p\nmid\#\widetilde E(\mathbf F_p)\). Hence \(\dim\mathcal L_p=1\). The Kummer condition is the finite-flat condition

\[
 \mathcal L_p=\operatorname{im}\left(
 H^1_{\mathrm{fppf}}(\mathbf Z_p,\mathcal E[p])\longrightarrow H^1(\mathbf Q_p,E[p])\right).
\]

In characteristic zero, the corresponding fixed-diagonal extension condition is crystalline, with weights \(\{0,0,1\}\); integrally it is the Kummer finite-flat extension condition with this weight range. Repeated Hodge–Tate weights are allowed in crystalline Galois representation theory. The obstruction is to the proposed *classical automorphic cohomology realization*, not to the existence of these local Galois extensions. Replacing this by unrestricted ordinary, trianguline, or de Rham deformation conditions would require a new equality-of-local-conditions proof. An ordinary condition also does not cover the supersingular primes.

For \(q\ne p\), every Kummer class is unramified in the cohomological sense, because multiplication by \(p\) is surjective over \(\mathbf Q_q^{\mathrm{ur}}\): the seed's geometric component orders are all prime to \(p\). The exact bad-prime data are:

| \(q\) | Retained local representation / reduction | Exact condition from (9) |
|---|---|---|
| 2 | Additive \(I_1^*\), geometric component order 4 | \(\mathcal L_2=0\) for \(p\ge7\) |
| 3 | Nonsplit multiplicative \(I_2\), nonzero transvection | \(\mathcal L_3=0\) for \(p\ge7\) |
| 2243 | Split multiplicative \(I_1\), nonzero transvection | \(\mathcal L_{2243}=0\) unless \(p\in\{19,59,2243\}\); otherwise retain the exact Kummer image |
| 4547 | Additive III; for \(p\ne4547\), inertia of order 4 with square \(-I\) | \(\mathcal L_{4547}=0\) for \(p\ge7\), \(p\ne4547\) |
| 5843 | Nonsplit multiplicative \(I_2\), nonzero transvection | \(\mathcal L_{5843}=0\) unless \(p\in\{487,5843\}\); otherwise retain the exact Kummer image |

In particular, for every \(p>5843\), the extension must be **split as an extension on every bad-prime decomposition group**, although its diagonal two-dimensional constituent is itself ramified. Merely keeping the same tame inertial type is not a substitute for that exact condition. At good \(q\ne p\), the condition is the usual unramified Kummer subgroup. At the archimedean place odd-primary cohomology is zero. For the three bad coefficient primes use (9), not the good-reduction crystalline condition.

These local assertions are carried from the [previous exact local reduction](/Users/bsm/BSD_CODEX6_DIVISION_FIELD_HORIZONTAL_2026-09-19/DIVISION_FIELD_REDUCTION_THEOREM.md). No class-group estimates or exceptional-prime computations are used here.

## 5. Why the checked deformation and congruence theorems do not reverse the arrow

The standard generalized matrix algebra construction has the direction

\[
 \operatorname{Hom}(B_{\mathrm{aut}},\mathbf F_p)
 \hookrightarrow H^1(\mathbf Q,E[p]), \tag{10}
\]

with its image in Selmer only after checking the local conditions. Here \(B_{\mathrm{aut}}\) denotes the appropriate off-diagonal module of an automorphic Cayley–Hamilton algebra. The precise general result is [Bellaïche–Chenevier, Theorems 1.5.5–1.5.6](https://arxiv.org/pdf/math/0602340): its image consists of extensions that already factor through that Cayley–Hamilton quotient. That description does not assert that every Galois/Selmer extension factors through it.

Thus (10) bounds automorphic extension data **by** Selmer data. It does not bound \(\operatorname{Sel}_p(E)/W\) by a congruence module. Taking the universal Galois extension algebra makes the factorization tautological, but supplies neither an automorphic identification nor an independently finite characteristic-zero invariant. Equation (1) explains why the missing factorization cannot be inferred solely from characteristic polynomials.

The general residually reducible theorem of [Berger–Klosin](https://arxiv.org/pdf/1103.5100) does not fill this gap for the seed. With constituents \(\rho_1=E[p]\), \(\rho_2=1\), their Assumption 5.1(1) requires the relevant extension Selmer space to have dimension one. The seed's Kummer subspace already has dimension two. Their relaxed conditions away from \(p\) do not remove those two classes. In addition, Theorem 8.5 takes a Selmer-order **upper bound as an input**, rather than obtaining it from a lower congruence bound alone. One cannot substitute \(\Sha[p]\) for the extension space in that theorem: quotienting by the global Mordell–Weil subspace changes the deformation problem and is not part of its statement.

Nor is the unmodified three-dimensional target polarized in the usual essentially self-dual sense. If

\[
 (1\oplus\rho_E)^\vee\simeq(1\oplus\rho_E)\otimes\mu,
\]

the unique one-dimensional constituent forces \(\mu=1\). The two-dimensional constituents would then be self-dual, contradicting \(\det\rho_E=\epsilon\) of infinite order. The residual analogue contradicts \(\bar\epsilon_p^2\ne1\) for \(p\ge7\). For unchanged restriction to an imaginary quadratic field, conjugation preserves the isomorphism class of \(\rho_E\), so the same obstruction applies. This prevents simply importing a polarized three-dimensional lifting theorem. A larger unitary/symplectic representation is a different realization whose exact comparison still has to be proved; dimension alone does not rule it out.

An adjoint theorem also cannot be substituted by a name change. The center \(-I\) acts trivially on \(\operatorname{ad}^0(E[p])\) and by \(-1\) on \(E[p]\), so there is no nonzero equivariant linear map between those modules in the required direction. The larger adjoint does contain the desired summand:

\[
 \operatorname{ad}^0(1\oplus\rho_E)
 \simeq\operatorname{ad}^0(\rho_E)\oplus1\oplus\rho_E\oplus\rho_E^\vee.
\]

But applying an adjoint automorphic theorem to this identity requires that theorem at the **reducible singular** three-dimensional representation. A theorem at an irreducible regular cuspidal point does not specialize there automatically.

## 6. Fixedness and the rank-two baseline

A classical finite-level integral cohomology group with a fixed algebraic coefficient would have been a plausible fixed finitely generated object. Section 3 shows that it has no characteristic-zero Eisenstein point of the required type. This is the first failed arrow for the classical construction. No prime-independent integral deformation/Hecke object with the required upper-bound comparison was identified in the nonclassical alternatives either.

Completed, ordinary, overconvergent, and eigenvariety constructions are defined after choosing \(p\), its weight space, its slope/ordinary operator, and often a tower of levels at \(p\). The reviewed results do not identify their relevant integral fibers with localizations of one fixed finitely generated \(\mathbf Z[1/S]\)-object. A finite module over a fixed \(p\)-adic weight algebra is not such an identification. This observation is a scope check; it is not a theorem that every conceivable \(p\)-adic fiber must lack integral descent.

There is also an elementary correction to the schematic rank-two length formula. If \(M\) is a fixed finite abelian congruence module, then

\[
 \operatorname{length}_{\mathbf Z_p}(M\otimes\mathbf Z_p)=0
\]

for all but finitely many \(p\). It therefore cannot equal \(2+\dim\Sha[p]\) for all sufficiently large \(p\). If the baseline is a free rank-two summand, its \(\mathbf Z_p\)-length is infinite, not two. For a fixed finitely generated integral module of rank two the meaningful identity is instead

\[
 \dim_{\mathbf F_p}M/pM=2+\dim_{\mathbf F_p}M[p]. \tag{11}
\]

To use (11), one would still need a proved map identifying or bounding excess Selmer classes by \(M[p]\), together with a justified integral removal of the Mordell–Weil baseline. No such \(M\) and comparison was constructed or found. The double zero of \(L(E,s)\) does not by itself establish any of those integral statements; an order in an analytic parameter is not a \(p\)-primary module length.

In particular, the outcome is not “the ordinary construction works and only a second derivative theorem is missing.” The ordinary characteristic-zero cohomological point is absent already. Finite-order jets in that same classical category are ruled out by (8). No assertion about a rank-two derived Eisenstein equality is promoted from Bloch–Kato or BSD.

## 7. The bounded source gate and stopping point

The [source audit](PRIMARY_SOURCE_AUDIT.md) checks Harder–Raghuram, Urban's weight-two construction with its erratum, generalized matrix algebras, reducible deformation criteria, recent Klingen modularity, the July 2026 small-parabolic eigenvariety revision, and higher-codimension congruence modules. The relevant nearby results either concern other representations, require incompatible hypotheses, or construct/lower-bound Selmer classes at a chosen \(p\). None of the checked sources proves a specialization that supplies the requested fixed integral upper bound for this seed.

The first classical stopped arrow is

\[
 1\oplus\rho_E\text{ with exact Kummer local conditions}
 \ \not\longrightarrow\ 
 \text{a classical algebraic-coefficient GL(3) Eisenstein point}.
\]

The nonexistence on the right in the stated classical category is proved by (6). The broader allowed test also includes nonclassical standard-representation methods, so its decisive missing arrow is

\[
 \boxed{\Sha(E/\mathbf Q)[p]\hookrightarrow M[p]
 \quad\text{for one independently constructed fixed finitely generated integral }M.}
\]

No such injection, equivalent upper inequality, or suitable fixed \(M\) is supplied by the checked sources. They supply the direction (10) instead. This is a bounded applicability finding; it is not a proof that every future converse theorem is impossible.

No \(C_E\), exceptional Sha-prime set, FIN result, or strict horizontal reduction is obtained. The operation stops at the direction gate, with the classical weight obstruction retained as a proved design constraint. No successor architecture is begun.
