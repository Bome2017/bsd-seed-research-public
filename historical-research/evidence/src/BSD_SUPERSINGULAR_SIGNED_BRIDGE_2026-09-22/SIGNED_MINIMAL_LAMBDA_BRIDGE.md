# A signed minimal-lambda bridge for the fixed seed

Written derivation, 2026-09-22. **Grade: a proof supplied here using imported BLV v2 theorems and retained seed hypotheses; not independently reviewed or Lean-verified.** No signed witness has been evaluated. No assertion of literature novelty.

This strengthens the preliminary bound in DERIVATION.md. That file correctly records what follows from one character-length bound alone; the argument here additionally uses the exact specialization equality, global freeness, and complex conjugation.

## Statement and endpoint

Let E be the fixed seed, K=Q(sqrt(-7)), and p>=5 be a good supersingular prime with p not dividing 7N. Assume the retained verification of BLV Hypothesis 1.1 for this pair. Let

\[
 F^-(T)=\mathcal L_f^-(T)\in\mathbf Z_p[[T]],\qquad T=\gamma-1
\]

be BLV's primitive minus square-root series. Then the proposed theorem proved below is

\[
 \operatorname{ord}_T(\overline{F^-})=2
 \quad\Longrightarrow\quad
 \Sha(E/\mathbf Q)[p^\infty]=0.
\tag{A3}
\]

Moreover b_0=F^-(0)=0 and the reduction of b_1=[T]F^- is zero. Thus with the correctly normalized conductor-p^2 packet

\[
 v_j=\overline{\psi_f(\gamma^jP_1)},\quad
 M_i=\sum_{j=0}^{p-1}j^i v_j,
\]

one has M_0=M_1=0 and

\[
 \bar b_2=\frac12M_2,\qquad
 M_2\ne0\Longrightarrow\Sha(E/\mathbf Q)[p^\infty]=0.
\tag{A3-packet}
\]

This is a conditional implication, not a proof that M_2 is nonzero at any prime. It covers both split and inert supersingular p, using the minus sign throughout. It makes no claim about the bad primes or the real leading-term formula.

## 1. Module convention and exact inputs

Write Lambda=Z_p[[T]] and iota(gamma)=gamma^(-1). Let S be the discrete minus signed Selmer group over the anticyclotomic tower. For Pontryagin duals, use the Lambda scalar action induced by precomposition with multiplication. When applying Poitou--Tate to the compact module T_g, the local pairing is iota-sesquilinear (BLV (5.1)); consequently its cokernel is the iota-twist of this dual. In what follows X denotes the dual with the twist required by that Poitou--Tate sequence.

This convention does not hide a comparison: replacing X by X^iota leaves its augmentation quotient, mu, lambda, Z_p-torsion, and complex-conjugation eigenspace ranks unchanged. It also leaves its characteristic ideal unchanged here, since

\[
 \operatorname{char}_\Lambda X=(F^-(F^-)^\iota).
\tag{1}
\]

Equation (1) is BLV Theorem 7.3/Theorem A in the non-exceptional minus case. All uses of a character below allow this explicit inverse-character convention.

The exact inputs are:

* **Classical control.** BLV Propositions 5.3, 5.9 and Corollary 5.5, with the retained bad-place comparisons, identify S[T] with Sel_(p-infinity)(E/K) and S[p^k,T] with the classical p^k Selmer group. DERIVATION.md section 1 gives the local verification. In particular
  \[
    X/TX\simeq\operatorname{Sel}_{p^\infty}(E/K)^\vee.
    \tag{2}
  \]
* **Exact character lengths.** BLV Theorem 7.1, applied at L=1 to f modulo p^k for arbitrarily large k, gives the length of every nonzero specialization. Proposition 5.9 makes these groups the p^k-torsion of the corresponding specialization of S. Once k is larger than the asserted finite length, they stabilize. Thus the full specialized Selmer group is finite and has length twice the valuation of F^- at the inverse character. Remark 5.16 identifies the two inverse-character Selmer groups; their lengths are equal.
* **Residual free presentation.** BLV section 5.5 gives a freeing set S_aux at k=1. Its relaxed compact signed Selmer group is free of rank delta(S_aux) over F_p[[T]] (Proposition 5.13), as is the sum of singular local groups at the auxiliary primes (Lemma 3.1/local calculations). Poitou--Tate gives the presentation
  \[
   \operatorname{Sel}^-_{S_{\rm aux}}(K,T_{f,1})
    \longrightarrow\bigoplus_{\ell\mid S_{\rm aux}}H^1_{\rm sing}(K_\ell,T_{f,1})
    \longrightarrow X/pX\longrightarrow0.
   \tag{3}
  \]
  The strict discrete group at S_aux is zero, as in Step 1 of Proposition 5.13. Each rational auxiliary prime is inert in K, hence the set and all local conditions are stable under complex conjugation. The presentation is equivariant for its semilinear action.
  To obtain (3) without asserting an unproved integral Selmer-complex presentation, first apply finite-level Poitou--Tate at each K_n with E[p] coefficients. Pass to inverse limits: all finite-level groups are finite, so the relevant Mittag--Leffler conditions hold. Corollary 5.14 identifies the relaxed limit, and the local calculation identifies the singular limit. The cokernel limit is the dual of the direct limit of discrete Selmer groups, identified with S[p] by exact control. No freeness of a full integral Selmer complex is assumed.
* **Base change of (3) at T=0.** Proposition 5.10 gives the injection from the specialized relaxed compact group to its base-layer group. Both have dimension delta(S_aux) by Proposition 5.13 at n=infinity and n=0, so it is an isomorphism. The same holds for the singular local modules. The kernel of the resulting base-layer map is the classical compact p-Selmer group; its cokernel is the Pontryagin dual of the classical discrete p-Selmer group, by Poitou--Tate. The Weil pairing identifies their underlying finite Galois modules with E[p]. Local Tate duality and its invariant map are natural under complex conjugation. Thus these kernel and cokernel have **the same plus and minus dimensions**.

The proof below needs the last assertion with complex-conjugation actions, not merely equal total dimensions. It does not use an ordinary derived-height theorem.

## 2. Eliminating finite Lambda-module errors when mu=0

Suppose mu(F^-)=0 and let lambda(F^-)=d. Equation (1) gives mu(X)=0 and lambda(X)=2d. Hence X is finitely generated over Z_p. Let H be its Z_p-torsion subgroup; it is finite and Lambda-stable. Put Y=X/H, a free Z_p-module of rank 2d.

Choose a in pZ_p such that F^-(a) and F^-(iota(a)) are nonzero, where iota(a)=(1+a)^(-1)-1. Such a exists: a nonzero mu-zero power series is a distinguished polynomial times a unit, so only finitely many values are excluded. Take the continuous character gamma -> 1+a.

By the exact character-length input and the inverse-character symmetry,

\[
 \operatorname{length}_{\mathbf Z_p}X/(T-a)X
  =v_p\bigl(F^-(a)F^-(\iota(a))\bigr).
\tag{4}
\]

For Y this same equality follows directly from the determinant of its endomorphism T-a: its characteristic power series is det(T-T|Y), equal to the generator in (1) up to a Lambda-unit. In particular T-a is injective on Y. The exact sequence H -> X -> Y therefore specializes to

\[
 0\longrightarrow H/(T-a)H\longrightarrow X/(T-a)X
   \longrightarrow Y/(T-a)Y\longrightarrow0.
\]

The two right-hand lengths are equal by (4), so H/(T-a)H=0. Nakayama, since T-a is in the maximal ideal, gives H=0. Therefore

\[
 X\text{ is free over }\mathbf Z_p,\qquad
 \operatorname{rank}_{\mathbf Z_p}X=2d.
\tag{5}
\]

This argument is essential. A characteristic ideal alone would allow a finite summand, so it would not justify (5).

## 3. Complex conjugation balances the two ranks

Set u=gamma-gamma^(-1)=T(2+T)/(1+T). As p is odd this is an integral change of formal parameter, and complex conjugation tau sends u to -u. Let W=X/pX, a finite-dimensional F_p-vector space of dimension 2d, with a nilpotent u-action U and tau U=-U tau.

Under mu=0, the cokernel in (3) is finite over F_p. Its source and target are free of the same rank over the domain F_p[[u]], so its kernel is zero. Thus (3) is a free resolution of W.

Reducing at u=0, the equal eigenspace dimensions of the arithmetic kernel and cokernel from section 1 imply that the virtual tau-representation

\[
 [F_0/uF_0]-[F_1/uF_1]
\]

is zero for this resolution. Here F_1 -> F_0 denotes the first map of (3).

To compute the same virtual representation explicitly, use the canonical resolution

\[
 0\to\mathbf F_p[[u]]\otimes(W\otimes\mathrm{sgn})
  \xrightarrow{\ u-U\ }
  \mathbf F_p[[u]]\otimes W\to W\to0.
\tag{6}
\]

The sign on the source is necessary: tau(u)=-u and tau U=-U tau make u-U equivariant precisely with that sign. Nilpotence of U proves exactness. Reduction modulo u computes the same Tor groups, with their natural tau-actions, in either resolution. Consequently

\[
 [W]-[W\otimes\mathrm{sgn}]=0.
\]

Since 2 is invertible, tau is diagonalizable with eigenvalues +/-1. Thus dim W^+=dim W^-=d. Lifting the idempotents (1+tau)/2 and (1-tau)/2 on the free Z_p-module X yields

\[
 \operatorname{rank}_{\mathbf Z_p}X^+
 =\operatorname{rank}_{\mathbf Z_p}X^-=d.
\tag{7}
\]

Only the parity action on this presentation is used. No claim that the raw Gross-point packet is purely even or purely odd is needed.

## 4. Minimal rank forces the seed's Sha to vanish

Because uX=TX, equation (2) and tau u=-u tau give

\[
 (X/TX)^+=X^+/uX^-.
\]

Quadratic restriction/corestriction identifies this plus quotient with the dual of Sel_(p-infinity)(E/Q). Its Kummer exact sequence is

\[
 0\to\Sha(E/\mathbf Q)[p^\infty]^\vee
   \to X^+/uX^-\to\mathbf Z_p^2\to0.
\tag{8}
\]

If d=2, then X^+ is free of rank two by (7). The composite surjection X^+ -> Z_p^2 in (8) is therefore an isomorphism: a surjective map of free Z_p-modules of equal rank has unit determinant. Its kernel contains uX^-, so uX^-=0, and the remaining kernel in (8) is zero as well. This proves (A3).

More generally, the same argument shows d>=2 whenever mu(F^-)=0. If the linear coefficient of F^- were a p-adic unit, its already-proved zero constant term would give d=1, a contradiction. Hence the linear coefficient vanishes modulo p. With the first-layer formula (3) of DERIVATION.md, this proves M_1=0 and (A3-packet).

The proof uses the seed's rank two and the quadratic plus projection. It does NOT conclude that Sha(E/K) vanishes. It does NOT require the twist's Sha support. Its retained rank-zero twist input remains part of the project's construction of this definite setup, but finiteness or a support bound for that twist is not used in (8).

## 5. Internal counterchecks

1. **Finite errors cannot be ignored.** Adding F_p to a torsion Lambda-module leaves its characteristic ideal unchanged but increases the specialization length. Section 2 uses the exact specialization equality to rule this out.
2. **Balanced ranks cannot be omitted.** X=(Lambda/(T))^4 with tau acting trivially has characteristic T^4 and a rank-four plus augmentation quotient. It is excluded by the equivariant arithmetic presentation in section 3, not by its characteristic ideal.
3. **No accidental vanishing of the twist.** Let X have plus basis e_1,e_2 and minus basis f_1,f_2, and define u e_i=p^c f_i and u f_i=0. Then X is Z_p-free of rank four, its characteristic ideal is (u^4), and its augmentation quotient is Z_p^2 in the plus part and (Z/p^c)^2 in the minus part. Thus the seed conclusion is compatible with a nontrivial finite twist Sha, as required by the ordinary Cassels--Tate analysis.

## 6. What this establishes in the BSD dependency chain

At the grade of this written derivation, A3 has a supersingular forward bridge using the same kind of conductor-p^2 quadratic Gross-point moment as the ordinary case. The ordinary and supersingular normalizations have opposite signs, which do not affect unit status.

This does **not** supply the witness at one prime, at positive density, or uniformly. It does not make the ordinary witness problem easier. A uniform arithmetic nonvanishing theorem (or a different input controlling every remaining primary component), the bad-prime work, and the real leading-term comparison remain unsupplied. These statements must not be upgraded from the existence of the bridge.

No new package has been sent and no sealed file has been edited. The proof obligations singled out for independent review are the equivariant Poitou--Tate presentation and the passage from finite-coefficient exact specialization lengths to (4); the details used for both have been stated above so a reviewer can test them directly.
