# Integral Kato bound: bounded source screen

2026-10-12. Scope: the submitted direct-base probe, coefficient prime equal to the cyclic extension degree. No seed computation, external job, publication, or new residual-image certification was performed.

**Disposition.** Kato supplies a genuine one-sided integral bound for a specified twisted representation with specified integral lattice and period. This is stronger than character-part finiteness. The companion algebra audit supplies a clean tame domain where the standard twisted Selmer group is exactly the packet's group `K`. Thus a conditional bound for `K` in terms of a precisely normalized central value is available on that domain. The integral period comparison with the seed's scalar and an evaluated bound of at most 2 remain OPEN. The packet correctly avoids claiming a Fitting-ideal membership or equivalence with Ota.

## 1. Primary source and exact hypotheses

Source: K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), [primary PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf). The already authenticated local PDF is

`/Users/bsm/BSD_QUINTIC_RELATIVE_REVIEW_CODEX_2026-10-12/tmp/rankzero_sources/Kato-2004.pdf`

with SHA256 `3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`. Printed pages 236, 244, 248–249 were visually checked for the formulas below. The text of §§14.6 and 14.8 was checked for integral comparison and local conditions.

Use a normalized twisted newform `g` of weight 2 and a stable lattice `T` in Kato's representation `V(g)(1)`, over `O = Z_p[zeta_p]`. Fix the character/inverse-character convention by an actual Galois-representation isomorphism; Kato's induced group-ring action in (14.6.1) uses the inverse of the image of Galois in `G`. Assume the requisite central value is nonzero.

Theorem 14.5(3), printed p.236, additionally requires odd `p`, potential good reduction at `p` in weight 2, a basis satisfying the image hypothesis of Theorem 12.5(4), and a basis of the required sign part of `T(-1)`. The image condition says that, in an integral basis, the image over `Q(mu_{p^infinity})` contains `SL_2(Z_p)`.

There is an internal cross-reference defect in the printed text: 14.5(3) calls the hypothesis in 12.5(4) “(12.5.1)”; the actual image hypothesis in 12.5(4) is numbered **(12.5.2)**, printed p.222. Condition (12.5.1) is instead the exceptional potentially multiplicative case. The content of 12.5(4), not the mistaken number, governs this application.

For a good-reduction seed at `p`, a finite-order twist is potentially good at `p`, including when its character is ramified at `p`. The stronger image input must still be supplied for the chosen lattice; the packet's sole hypothesis `E(Q)[p]=0` is not that input. This audit does not promote retained image information into a fresh certification.

## 2. The actual bound available from Kato

Let `z` be the specialized Kato class attached to the prescribed sign basis. Set

\[
\mu=\frac{[H^1(\mathbf Z[1/p],T):z]}{\#H^2(\mathbf Z[1/p],T)},\qquad
\nu=\frac{[H^1(\mathbf Q_p,T)/H_f^1(\mathbf Q_p,T):z]}{\#H^2(\mathbf Q_p,T)}.
\]

These are Kato's generalized indices: the definition allows a rational class and records its denominator, rather than discarding it. Theorem 14.5(3) gives `mu >= 1`. Proposition 14.16(2), printed p.244, gives

\[
\#S(T)=\mu^{-1}\nu\,
 \#H^0(\mathbf Q,T\otimes\mathbf Q/\mathbf Z)\,
 \#H^0(\mathbf Q,T^*(1)\otimes\mathbf Q/\mathbf Z).
\]

Consequently, under the hypotheses just listed,

\[
\#\operatorname{Sel}(T)\leq\#S(T)
\leq \nu h_0(T)h_0(T^*(1)).                                      \tag{A}
\]

This is a published, usable upper-bound mechanism for the standard twisted Selmer group. It does not assume finiteness of the base seed's Sha or base BSD. It also does not require treating a nonselfdual order-`p` twist as an elliptic curve over `Q`.

Here `S(T)` is exactly Kato's relaxed group in §14.8, with the finite condition imposed at `p`. His usual `Sel(T)` is a subgroup. The quotient is finite and embeds in the sum, over places away from `p`, of

\[
 H^1(\mathbf F_v,H^0(\mathbf Q_v^{\rm ur},T\otimes\mathbf Q/\mathbf Z))
 /({\rm divisible\ part}).
\]

These are local defects. They cannot be silently replaced by zero at ramified or bad primes. Using `S(T)` on the upper-bound side of (A) is valid without making that replacement; it may lose sharpness. The local `H^2` factor in `nu` and the two global `H^0` factors must likewise be retained until their vanishing is justified. For an exact lattice `T_pE tensor O(chi)` and its dual twist, reduction modulo `pi` has the seed's residual representation since `chi = 1 mod pi`; under the retained absence of rational `p`-torsion their global `H^0` factors vanish. This observation concerns that exact lattice and dual, not an arbitrary unidentified period normalization.

## 3. What “in terms of the twist value” actually means

For a twist whose level is prime to `p`, Proposition 14.21(1), printed p.248, applies when `p > 2`. Choose a strongly divisible lattice `D` with `T=T(D)(1)`, an integral generator `omega` of its filtered line, and an integral sign generator `gamma^+` for `T(-1)`. Define the period by

\[
\operatorname{per}_{g}(\omega)^+=\Omega_{g,T}\gamma^+.
\]

Kato then evaluates the same local factor:

\[
\nu=[\mathcal O:L(g^*,1)/\Omega_{g,T}].                         \tag{B}
\]

The star is Kato's conjugate-coefficient newform; it must not be lost when a faithful character is replaced by its inverse. Since the residue field of `O` is `F_p`, (A)–(B) give

\[
\operatorname{length}_{\mathcal O}\operatorname{Sel}(T)
\leq v_\pi\!\left(L(g^*,1)/\Omega_{g,T}\right)
 +\log_p h_0(T)+\log_p h_0(T^*(1)).                              \tag{C}
\]

The period in (B) is tied simultaneously to the actual Galois lattice and the strongly divisible differential lattice. It has not been identified in this packet with the seed's real Néron period times an asserted Gauss factor. Such an identification is an integral comparison problem; an unspecified algebraic proportionality is insufficient for a length-2 test.

This crystalline formula covers a tame auxiliary conductor prime to a good coefficient prime `p`, once the lattice is matched. It does **not** apply as stated to a character of conductor `p^2`: `p` then divides the twisted level. The more general index bound (A) remains the relevant source statement when its hypotheses hold, but a ramified local period/exponential calculation is still needed. No crystalline formula was transplanted into that case here.

## 4. The integral norm-zero lattice and the nonunit map

Write

\[
 R=\mathbf Z_p[G],\quad I=\ker(\epsilon:R\to\mathbf Z_p),\quad
 \mathcal O=R/(N_G),\quad \pi=\sigma-1.
\]

There is an **integral isomorphism**

\[
 \alpha:\mathcal O\xrightarrow{\sim}I,\qquad
 \bar x\longmapsto(\sigma-1)x.
\]

Its composite with inclusion and the quotient projection is

\[
 \mathcal O\xrightarrow{\alpha}I\hookrightarrow R\longrightarrow\mathcal O,
 \qquad \bar x\longmapsto\pi\bar x.                             \tag{D}
\]

Thus the natural map from the norm-zero integral lattice to the character quotient is multiplication by the nonunit `pi`. On tensoring with the rank-two Tate module, its lattice cokernel is `(O/pi)^2`. This concrete defect explains why rational character splitting or a normalization comparison cannot be used as an integral equality at the coefficient prime. It does **not** show that the abstract lattice `I` cannot be matched to a twisted lattice: `alpha` already is such an isomorphism. Nor does it justify automatically adding or subtracting 2 from the length of a Selmer group; cohomology and local conditions must be followed through the map.

Kato's own reduction in §14.6, printed pp.237–238, preserves this limitation. The group-ring normalization comparison has kernel and cokernel killed by an integer annihilating the normalization quotient. In the present degree-`p` situation that comparison is not an integral averaging isomorphism at `p`.

There is a useful precise global construction. Let `A_I=(T_pE tensor I) tensor Q_p/Z_p` and define `A_R` similarly. The split exact sequence of underlying `Z_p`-modules `0 -> I -> R -> Z_p -> 0` induces

\[
0\to A_I\to A_R\to E[p^\infty]\to0.
\]

Since `E(Q)[p^infinity]=0`, global cohomology and Shapiro give an injection

\[
 H^1(\mathbf Q,A_I)\hookrightarrow H^1(L,E[p^\infty])
\]

whose image is the corestriction kernel. Restriction back to `L` is injective under the packet's `E[p^infinity](L)=0`, so this is also the norm kernel in global cohomology. The actual `K` therefore identifies with the Selmer group on `A_I` whose local conditions are **pulled back from the elliptic Selmer conditions over `L`**.

To apply (A) or (C) to `K`, one must compare these pulled-back local conditions with the standard finite conditions for the exact twisted lattice identified through `alpha`. A rational representation isomorphism, or finiteness of both groups, does not prove equality of those local conditions. In general, one must compute the relevant local quotients and the image of global localization in them. A comparison bound of the form

\[
\operatorname{length}_{\mathcal O}K
\leq \operatorname{length}_{\mathcal O}\operatorname{Sel}(T)+\delta
\]

would combine with (A), or with (C) in the crystalline case. This screen does not evaluate a general correction `delta` or set it to zero outside an established local domain.

The companion `MAP_AUDIT.md` supplies a useful clean case. Let `B` be the connected kernel of the trace map `Res_{L/Q} E -> E`. Then `T_pB=T_pE tensor I`. The unique global lift of a class of `K` has, at each place `v`, a possible failure of the local Kummer condition measured by the kernel of

\[
 H^1(\mathbf Q_v,B)\longrightarrow
 H^1(\mathbf Q_v,\operatorname{Res}_{L/\mathbf Q}E),
\]

which the abelian-variety exact sequence identifies with

\[
 E(\mathbf Q_v)/\operatorname{Tr}_{L\otimes\mathbf Q_v/\mathbf Q_v}
 E(L\otimes\mathbf Q_v).
\]

If these local norm cokernels have no `p`-primary part, the lift is Selmer at every place and

\[
 K\simeq\operatorname{Sel}_{p^\infty}(B/\mathbf Q)
   =\operatorname{Sel}(T_pE\otimes I).                           \tag{E}
\]

A sufficient tame domain is: `p` is a good prime for `E`; `L` is the degree-`p` subfield of `Q(mu_ell)` for a good prime `ell != p` with `ell = 1 mod p`; `p` does not divide `#E(F_ell)`; and the Tamagawa component groups at bad primes have order prime to `p`. At the ramified prime `ell` the reduction obstruction is `E(F_ell)/pE(F_ell)` and vanishes under the named hypothesis; the formal-group norm has no `p` obstruction. Unramified good-reduction norm maps are onto, including at the coefficient prime; at the unramified bad primes the possible `p` obstruction is removed by the component-group hypothesis. The odd-degree extension also has no archimedean obstruction. No ordinarity assumption is introduced in this comparison.

On this domain, identify the exact lattice in (E) through `alpha` and choose the strongly divisible lattice and period in §3 to match it. Under the image hypotheses of §1, (C) now yields the concrete conditional inequality

\[
 \boxed{\operatorname{length}_{\mathcal O}K
 \leq v_\pi\!\left(L(g^*,1)/\Omega_{g,T}\right).}                \tag{F}
\]

The global torsion factors disappear for this exact lattice as explained in §2. Kato's relaxed away-from-`p` group still gives a valid upper bound; no equality with that relaxed group is asserted. Equation (F) is not a claim that the displayed seed/Gauss scalar in the submission has already been identified with its right-hand side.

## 5. Threshold, Ota comparison, and first missing arithmetic

The packet's formal injection and resulting sufficient threshold are unchanged: an independently obtained `length_O K <= 2` proves `Sha(E/Q)[p^infinity]=0`. A bound at most 3 gives only `dim_Fp Sha[p] <= 1` from that argument. Using 3 as a vanishing threshold requires an independently justified evenness statement for this dimension; Cassels–Tate alternation on the finite quotient alone must not be substituted for primary finiteness or control of the divisible part. No new parity theorem is imported by this screen.

On the clean tame domain, the first unfinished arithmetic interface is now concrete: identify the period `Omega_{g,T}` for the actual lattice with a computable scalar normalized by the seed differential and character data. The next requirement is an authenticated valuation of that scalar at most 2 (or a justified parity variant). Outside that domain the additional local defects must also be computed. Nonvanishing alone does not bound the valuation. Even a successful single-prime calculation would not prove the required cofinite family assertion.

The submitted packet already retains Ota's rank-two leading-symbol criterion with its ambient hypotheses. Nothing in the checked Kato statements proves equivalence of that premise with this uncomputed length bound, or makes the length bound strictly stronger. In particular (D) is a reason to require an integral comparison, not a proof of either equivalence or impossibility.

**Endpoint:** standard-twist integral upper bound FOUND; exact norm-zero transfer AVAILABLE on the clean tame local domain through the companion algebra audit; integral seed-period identification and numerical short-length bound NOT CONSTRUCTED. No new coefficient prime, base FIN, ORDER9, or Q36 is settled.
