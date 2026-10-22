# Rank-zero source check for the nontrivial quintic component

Date: 2026-10-12.

**POSITIVE, SOURCE-BOUND RESULT:** Kato's Theorem 14.2(2) and Corollary 14.3 apply directly to the retained nonzero order-five twists. They prove finiteness of the full nontrivial rational-character component of the Selmer group over `F`. Consequently the trace-zero fourfold `B/Q` has finite Selmer group and finite `Sha(B/Q)`, and the relative quotient `Sha(E/F)/res Sha(E/Q)` is finite. No finiteness of `Sha(E/Q)` and no BSD formula is required.

**OPEN:** These finiteness statements do not determine the order, prime support, exponent, or generators of the relative group. In particular they do not prove a relative order of `19^4`. This check admits no theorem giving that exact value.

## 1. Bound input and primary source

The submitted proof is `submitted/BSD_QUINTIC_RELATIVE_LEADING_TERM_2026-10-12/PROOF.md`, SHA-256 `927f769eda401620ebfb815502214d49dc9d6c0f16140d42af8fbf847633e310`. Its `SOURCES.md` was also read.

Retained here are the seed elliptic curve `E/Q`, its modularity, the degree-five field `F` inside `Q(mu_25)`, and the audited four nonvanishing values

\[
L(E,\chi^j,1)\ne0\qquad(1\le j\le4).
\]

The exact normalized product `38^4/25` is not needed for the finiteness application: only nonvanishing is used. The original modular-symbol receipt was not recomputed.

The primary source checked is K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Asterisque 295 (2004), printed pp. 234-237, especially §14.1, Theorem 14.2(2), Corollary 14.3, and the first full paragraph of p. 236. [Publisher archive PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf).

The PDF was downloaded and printed pp. 234-236 were rendered and visually inspected, including the full hypotheses and conclusions. Source cache: `tmp/rankzero_sources/Kato-2004.pdf`; SHA-256 `3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`. Text extraction was checked against those images because the OCR corrupts several inequality and nonvanishing signs.

## 2. The exact theorem being used

Corollary 14.3 concerns an abelian variety `A/Q` admitting a surjective homomorphism from `J_1(M)`, a finite abelian extension `K/Q`, and a character `chi` of its Galois group. Nonvanishing of `L(A,chi,1)` implies finiteness of the `chi`-parts of its full Selmer group over `K` and its point group. Kato's character part is the subgroup annihilated by the integral ideal

\[
I_\chi=\ker(\mathbf Z[\operatorname{Gal}(K/\mathbf Q)]\longrightarrow\overline{\mathbf Q}).
\]

Theorem 14.2(2) supplies finiteness at every coefficient prime and vanishing at almost all coefficient primes. The paragraph on p. 236 also permits character quotients by `I_chi`. These are full finiteness conclusions, not merely zero corank at each prime. The corollary has no ordinary-reduction, residual-surjectivity, or prior-Sha-finiteness hypothesis.

Kato's Selmer group in §14.1 uses the usual Bloch-Kato finite local conditions; for an abelian variety its direct sum over coefficient primes is the usual full Selmer group, as stated immediately before Theorem 14.2.

## 3. All hypotheses match without invoking a false elliptic twist

Apply the corollary with `A=E` and `K=F`. Modularity gives a nonzero modular parametrization and hence a surjective homomorphism `J_1(N) -> E`. The field `F/Q` is finite abelian with group `G=C_5`. The packet supplies nonvanishing for all four nontrivial characters, so inversion of the character in a convention does not matter.

Kato's convention at Theorem 14.2 removes Euler factors at primes ramifying in `F/Q`, here only `5`. This agrees with the twisted values used in the packet. The elliptic curve has good reduction at `5`, whereas each nontrivial character has conductor `25`; the twisted local representation has no inertia invariants at `5`, so its local Euler factor there is already one.

The individual modular forms `f tensor chi^j` have nonreal order-five characters and are not elliptic curves over `Q`. No Gross-Zagier-Kolyvagin theorem for a rational elliptic curve is applied to them. There is also no need to construct an isogeny between `B` and the modular fourfold attached to `f tensor chi`, or to identify that fourfold's canonical periods. Kato's abelian-extension statement acts directly on the original elliptic curve.

## 4. The integral character orbit is exactly norm-zero

Fix a generator `sigma` of `G` and put

\[
N_G=1+\sigma+\sigma^2+\sigma^3+\sigma^4.
\]

The homomorphism `Z[G] -> Z[zeta_5]`, sending `sigma` to any nontrivial fifth root of unity, has kernel `(N_G)`: the source is `Z[X]/(X^5-1)` and the additional relation is the monic polynomial `Phi_5(X)`. All four nontrivial characters therefore give the same integral ideal. This is the entire nontrivial rational orbit, not an eigenspace for one chosen embedding into a `p`-adic coefficient field.

Writing `S_F=Sel(E/F)`, the admitted theorem proves

\[
\boxed{\ker(N_G:S_F\to S_F)\text{ is finite},\qquad
S_F/N_G S_F\text{ is finite}.}
\]

This statement includes the coefficient prime `5`; no integral idempotent `N_G/5` was used. It also includes primes `2` and `3`. Their exact orders are not obtained from the theorem.

For a coefficient prime `ell != 5`, the idempotent `1-N_G/5` is integral, and the displayed kernel is exactly the ordinary nontrivial direct summand at `ell`. At `5`, the kernel can include invariant five-torsion. In particular, under the retained equality `E(F)=E(Q)` of rank two, the point contribution `(E(F) tensor Q/Z)[N_G]` is `(Z/5Z)^2`. Finiteness of the norm-zero Selmer group does not assert it is zero.

## 5. Consequences for actual Sha groups

Let `X_F=Sha(E/F)`. The natural surjection `S_F -> X_F` is `G`-equivariant, so it gives a surjection

\[
S_F/N_GS_F\twoheadrightarrow X_F/N_GX_F.
\]

The latter group is finite. On Sha, the group-ring norm satisfies `N_G=res cor`, where restriction and corestriction connect `Q` and `F`. Consequently `N_GX_F` is contained in `res Sha(E/Q)`, and

\[
\boxed{\operatorname{coker}\bigl(\Sha(E/\mathbf Q)
 \xrightarrow{\operatorname{res}}\Sha(E/F)\bigr)\text{ is finite}.}
\]

This is a finite relative quotient even if both full Sha groups are infinite. No equality of their orders has been divided or cancelled.

The norm-zero subgroup `X_F[N_G]` is finite as well. Its natural map into `X_F/N_GX_F` has kernel contained in `X_F[5]`: if `x=N_Gy` and `N_Gx=0`, then `5x=N_G^2y=0`. The group `X_F[5]` is finite by finite descent. Thus both the image and kernel of this map are finite. This argument does not need the retained stronger vanishing of the full five-primary group.

Alternatively, under retained `E(F)=E(Q)`, multiplication by `N_G` on `E(F) tensor Q/Z` is the surjective multiplication-by-five map. The Selmer exact sequence then gives a surjection `S_F[N_G] -> X_F[N_G]` with kernel `(Z/5Z)^2`.

The norm-zero group here means kernel of the endomorphism `N_G` on `Sha(E/F)`. Kernel of corestriction to `Sha(E/Q)` is contained in it, and is consequently finite too. Integral identification of these different relative objects, especially at `5`, should retain their actual maps.

## 6. Finiteness for the trace-zero fourfold without a modular-fourfold shortcut

Let `R=Res_{F/Q}E` and `B=ker(Tr:R -> E)`. Geometrically, `Tr` is summation `E^5 -> E`, so its kernel is connected and isomorphic to `E^4`. In particular `B` is an abelian fourfold, and

\[
0\longrightarrow B\longrightarrow R\xrightarrow{\operatorname{Tr}}E\longrightarrow0
\]

is exact. On geometric torsion points it remains exact, including surjectivity on the right: lift a torsion point of `E`, then subtract a suitable point of `B`, using divisibility of `B(\overline Q)`.

The kernel of the induced map on first Galois cohomology of torsion is therefore an image of `E(Q)_tors`, hence finite. The inclusion `B -> R` carries the usual local Kummer conditions into those for `R`, so the map

\[
\operatorname{Sel}(B/\mathbf Q)\longrightarrow
\operatorname{Sel}(R/\mathbf Q)\simeq\operatorname{Sel}(E/F)
\]

has finite kernel. The final isomorphism is Shapiro's isomorphism, with the corresponding local decompositions. Since `N_G` on `R` is diagonal inclusion composed with trace, it is zero on `B`. The image of this Selmer map is contained in the finite subgroup `S_F[N_G]`. It follows that

\[
\boxed{\operatorname{Sel}(B/\mathbf Q)\text{ is finite},\qquad
\Sha(B/\mathbf Q)\text{ is finite},\qquad
\operatorname{rank}B(\mathbf Q)=0.}
\]

This proof includes the prime `5` without assuming a prime-to-five splitting and without assuming finiteness of the base curve's Sha. The independent algebraic-splitting audit can give the finer identifications of the relative groups away from `5`.

## 7. Why the exact 19-primary order remains unproved here

The computed product gives an analytic factor, and the source theorem gives finiteness. Neither conclusion identifies an integral Selmer Fitting ideal with the ideal of the algebraic twisted value. Kato's adjacent Theorem 14.5(3) is a one-sided cohomological bound subject to additional lattice and image hypotheses, not an equality of the relative Sha order with the packet's product. It cannot be converted into such an equality by quoting its finiteness corollary.

An exact relative `19^4` claim would require a two-sided arithmetic comparison for the nontrivial orbit with its actual integral periods, local conditions, and Euler factors, or an independent descent of sufficient strength. No such comparison has been checked or imported in this focused source screen. This is a source-bound remaining obligation, not a claim that no applicable theorem exists anywhere.

In particular this file proves neither that relative 19-torsion is nonzero nor that all other relative prime parts vanish. It also leaves the invariant base component, FIN, ORDER9, and Q36 unchanged. The useful new result is that the arithmetic added by this finite quintic extension is a finite group, independently of the unresolved base finiteness problem.
