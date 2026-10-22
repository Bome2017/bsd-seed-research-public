# Independent desk audit of the cyclotomic 5-tower deduction

Date: 2026-10-12.

Reviewed input: `submitted/BSD_CYCLOTOMIC5_AND_MOMENT_2026-10-12/PROOF.md`, Section 3, from the source return at `c728f2d2`. This audit does not re-certify the retained seed rank, residual image, periods, or historical modular-symbol computation. The exact small-table replay is reviewed separately.

**Verdict: TOWER_DEDUCTION_SUPPORTED_UNDER_RETAINED_INPUTS.** No blocking error was found in the ordinary Selmer-module argument or its passage to every finite layer. This is a written mathematical review, not formal verification, an independent reconstruction of Kato's theorem, or a novelty determination.

## 1. Exact module and imported theorem checks

The module is the Pontryagin dual of the direct limit of the usual `Sel_{5^infinity}(E/Q_n)` under restriction. It is not the full-S Iwasawa H^2 module from the preceding Bockstein work. This distinction is maintained correctly.

Freshly read source: [Stein–Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, published author offprint](https://www.wstein.org/papers/mcom2649-iwasawa-alg.pdf), Section 6, printed pp.1775–1776, and Proposition 7.2 / Theorem 7.3, printed p.1778. Section 6 uses exactly this direct-limit Selmer group and its finitely generated dual. Section 6.1 supplies torsion for the good ordinary case. Proposition 7.2 allows full residual image at p>=5 to supply full p-adic image. Theorem 7.3 states the integral factorization `L_p=f_E d` with `d` in Lambda under full p-adic image and semistable reduction at p. Good ordinary reduction satisfies the relevant reduction hypothesis; no assertion about a supersingular Selmer module is imported. The standard period/measure convention remains the retained source-normalization input. The weaker statement with an extra unknown power of p is not being substituted for this full-image theorem.

Freshly read source: [Greenberg, *Iwasawa Theory for Elliptic Curves*, arXiv:math/9809206v1](https://arxiv.org/pdf/math/9809206), Proposition 4.14 and proof, printed pp.52–53. Its assumptions are cyclotomic Selmer cotorsion and `E(F)[p^infinity]=0`; its conclusion is absence of proper finite-index Lambda-submodules of the discrete Selmer group. Dualizing gives exactly absence of nonzero finite Lambda-submodules of X. Although Section 4 initially discusses finite base Selmer groups, the appendix beginning on p.43 explicitly generalizes the earlier proposition; Proposition 4.14's proof uses twists and cotorsion, not finiteness of the original base Selmer group or Sha. The global cyclotomic convention is stated in the introduction. No hidden rank-zero hypothesis is retained here.

The primary sources were read in their full-source parsed text, including these proofs and surrounding definitions. Screenshot calls were made, but this audit does not claim independent visual inspection of rendered pages. The original Kato theorem itself was not newly rederived here; the published ordinary formulation above is the imported theorem.

## 2. Restriction and the point subgroup

Let `A/Q` satisfy the proposition's hypotheses, and let Q_infinity/Q be the cyclotomic Z_p-extension. The vanishing

    A[p^infinity](Q_infinity)=0

follows from `A(Q)[p]=0`. If A[p](Q_n) were nonzero, it would be a nonzero F_p-representation of the finite p-group Gal(Q_n/Q); such a representation has nonzero invariants. These invariants would lie in A(Q)[p]. Every torsion point in the infinite extension is defined at a finite layer, and a nonzero p-power torsion point produces p-torsion. This part needs neither a control theorem nor full residual surjectivity.

Inflation–restriction consequently makes

    H^1(Q_n,A[p^infinity]) -> H^1(Q_infinity,A[p^infinity])

injective. The same holds between finite layers. Restriction respects Kummer local conditions. Thus the direct-limit Selmer group can be treated as a union inside infinite-field cohomology, and the base Kummer subgroup

    W=A(Q) tensor (Q_p/Z_p)

embeds in it. The Gamma action on the image of this base-field cohomology is trivial. The induced dual map

    X -> W^vee = (Lambda/(U))^r

is therefore a genuine surjection of compact Lambda-modules. This is stronger than an assertion of equal ranks or a control map with bounded kernel.

## 3. Removing the finite error exactly

Write K for the kernel of the displayed surjection. Since X is a finitely generated torsion module, characteristic-ideal multiplicativity gives

    char(X) = char(K) (U^r).

The integral divisibility `f_X | L` and the unit coefficient `[U^r]L` then force

    L=U^r u(U),  u(U) in Lambda^times,
    char(X)=(U^r),  char(K)=(1).

The lower coefficients of L vanish here because the point quotient forces U^r to divide f_X and therefore L. A finite approximant with nonzero lower coefficients is not being interpreted as the infinite series.

There is a particularly direct way to finish the argument. Over the two-dimensional regular local ring `Lambda=Z_p[[U]]`, a finitely generated torsion module with trivial characteristic ideal is supported only at the maximal ideal. It has finite length, hence finite cardinality. Thus K is a finite Lambda-submodule of X. Greenberg excludes K, giving

    X = (Lambda/(U))^r

via the actual point quotient map.

This also validates the submitted structure-theorem proof: mu=0 and lambda=r make X finitely generated over Z_p of rank r; its Z_p-torsion is finite and is excluded by Greenberg; the point quotient is then an isomorphism between free Z_p-modules of rank r. The direct kernel argument above merely shortens that passage. Neither version discards a pseudo-null term without an arithmetic theorem.

The submitted counterexamples correctly identify the two independent ingredients: a finite summand would evade the characteristic ideal, while `Lambda/(U^2)` lacks the required rank-two trivial-action quotient. Both the point map and finite-submodule exclusion are used.

## 4. Every finite layer

For every n, the restriction map on Selmer groups is injective and its image contains the image of W. The preceding result says W is the entire infinite-layer Selmer group. Hence restriction is an isomorphism at every finite layer.

The Kummer map is compatible with restriction and extension of points. Therefore the finite-layer Kummer subgroup contains the preimage of W and is itself the entire finite-layer Selmer group. The Kummer exact sequence gives

    Sha(A/Q_n)[p^infinity]=0.

Its corank gives `rank A(Q_n)=r`. No prior finiteness of a finite-layer Sha is used. In particular, the argument proves vanishing, not merely bounded growth or finiteness. No surjective integral Mazur control theorem with omitted local terms is required.

## 5. Seed application

For p=5, the retained seed inputs supply good ordinary reduction, rank two, no rational 5-torsion and full residual image. The separately authenticated historical symbol tables supply

    [U^2]L_std,5 = 1 mod 5.

Subject to those retained arithmetic inputs, Sections 1–4 justify

    X_cyc,5 = (Z_5[[U]]/(U))^2,
    rank E(Q_n)=2,
    Sha(E/Q_n)[5^infinity]=0   for every n>=0.

This is an actual field-tower consequence for the fixed seed. It is not a new coefficient-prime theorem over Q, and it says nothing here about the nontrivial tame-character components of the full cyclotomic fields.

## 6. Optional stronger point-group consequence

This corollary uses an additional retained input from the prior finite-source-palette record: **E[ell] is irreducible over Q for every prime ell>=5**, not merely the residual image at 5. The present review does not re-certify that all-prime input.

Under it, the rank conclusion strengthens to

    E(Q_n)=E(Q) for every n>=0,
    E(Q_infinity)=E(Q).

Here is the proof, which is independent of any new symbol calculation.

For ell>=5, E[ell](Q_n) is G_Q-stable because Q_n/Q is Galois. Irreducibility makes it either zero or all of E[ell]. The latter would put Q(mu_ell) inside Q_n by the Weil pairing. This is impossible: its degree ell-1 is even, while `[Q_n:Q]=5^n` is odd. Hence no new ell-primary torsion for ell>=5 occurs.

For ell=2 or 3 and any k, the degree of the full ell^k-division field divides `|GL_2(Z/ell^k)|`. Those orders have only the prime factors 2 and 3. Their intersection with Q_n is therefore Q, since the degree of Q_n is a power of 5. All ell-power torsion over Q_n is already rational. Thus the retained rational torsion calculation gives

    E(Q_n)_tors=E(Q)_tors=Z/2.

The rank equality makes E(Q_n)/E(Q) a finite group. For P in E(Q_n), choose m>0 with mP in E(Q). For sigma in Gal(Q_n/Q), the point sigma(P)-P is torsion, hence belongs to the rational Z/2. Since that torsion is rational,

    sigma -> sigma(P)-P

is a group homomorphism from the finite 5-group Gal(Q_n/Q) to Z/2. It is zero. Thus P is Q-rational. Taking the union proves the infinite-layer assertion.

This strengthening is explicitly conditional on the stronger retained residual-image input. It is a consequence in the field direction and does not improve the base-field coefficient-prime coverage.

## 7. Endpoint effect and review limits

The all-layer rank and 5-primary vanishing are supported at written-proof grade under the named retained inputs. The optional point-group equality is supported with its stronger residual hypothesis. These are stronger statements than a base-field 5-primary result, but FIN, ORDER9 and Q36 for the seed over Q remain unchanged.

No new modular-symbol table, Kato derivative value, height determinant, Selmer computation or number-field point search was performed in this theorem audit. No main-conjecture equality, height nondegeneracy, or Sha finiteness was assumed. The one-sided integral divisibility plus the actual unit quadratic coefficient and Greenberg's finite-error theorem suffice.
