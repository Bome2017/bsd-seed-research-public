# 03 — Derivations and obstructions (Lane 4)

Each section ends with a classification: NOT_PRINTED / FALSE / TYPE_MISMATCH / NEW_THEOREM_REQUIRED / PASS.

## §1. The receptacle: the only explicit "dagger/MRS object" has the wrong Tate module

**Frozen claim.** H9R8 (checkpoint l.750–753): A_r^† := I_r^† ⊗_Z J_r over Q(μ_p), I_r^† = Z[G_r] with G_Q acting through
<χ>_r^{-1/2}; "T_p(A_r^†) ≅ Z_p[G_r]^† ⊗_{Z_p} T_p(J_r)". H9R9 (l.789): "DAGGER_TRANSITION_VS_MRS = NO TYPE MISMATCH AFTER
CONTRACTION". H9R16-C inherits this object ("fixed-base dagger/MRS object").

**Source type of the étale target.** BCPV Def 4.6 (p.21): M^† := M ⊗_{Z_p[G_r]} Z_p[G_r]^†. DR22 p.19: Ω(1/2) := Ω ⊗_{Λ(G_∞)} Λ(G_∞)(1/2).
The packaged classes (4.7) take values in Hom_{Z_p[G_r]}(S, Z_p[G_r]) ≅_G Hom_{Z_p}(S, Z_p).

**Rank test.** For M = T_pJ_r (rank 2g over Z_p):
* rank_{Z_p}(Z_p[G_r]^† ⊗_{Z_p} T_pJ_r) = |G_r|·2g = p^{3(r−1)}·2g  (MRS Thm 2.2(iii) with O = Z; dim A_r^{†,Z} = |G_r|·g by MRS Thm 2.1);
* rank_{Z_p}((T_pJ_r)^†) = 2g.
For r ≥ 2 these differ. So H^1(K_0, T_p(A_r^{†,Z})) is not BCPV's H^1(K_0, (·)^†).

**Can the Z-type object be salvaged?** Inside Z_p[G_r] ⊗ M (G_r acting by g ⊗ g^{-1} on the anti-diagonal), the invariants
are the norm image {Σ_g g ⊗ g^{-1}m} ≅ M, and this recovers the group-ring tensor. Hence the correct object is the
G_r-invariant abelian subvariety of A_r^{†,Z} (T_p commutes with invariants), not A_r^{†,Z} itself. But the frozen
transition τ^geom_r := s_r ⊗ ϖ_{1,*} (H9R8 l.762), restricted to invariants, is in M-coordinates
    Σ_{g'∈G_{r+1}} pr(g') ⊗ ϖ_*(g'^{-1}m) = Σ_{g∈G_r} g ⊗ g^{-1}·ϖ_*(Σ_{k∈ker} k^{-1}m) = (norm of) p^3·ϖ_*(m),
because ker(G_{r+1}→G_r) ≅ (Z/p)^3 acts trivially after ϖ_* (ϖ_1∘<k> = ϖ_1 for k ≡ 1 mod p^r, DR22 (1.13)–(1.14)).
DR22 L2.8 has **no** constant. So even on the salvaged subvariety the frozen τ^geom is off by p^3 per level relative to the
source transition: over Z_p this destroys the inverse-limit lattice (a compatible system would need P_r ∈ p^{3r}Ĵ); over
Q_p it changes the normalization of every point by p^{−3r}.

**Group after contraction.** G_r ⊂ ((Z/p^r)^×)^3 acts on the triple product. After Π_{Z,*} the output is a single Jacobian
(factor 1); coordinates 2 and 3 act only on the auxiliary carrier B^bal_r. §2 shows that on the p-part the auxiliary
half-twists cancel exactly, leaving <m>^{1/2} on factor 1. So the post-contraction dagger group is the factor-1 cyclic
quotient (order p^{r−1}), not G_r.

**Classification.** TYPE_MISMATCH (receptacle of H9R8/H9R9 as inherited by H9R16-C). Not FALSE for the route: the
BCPV-type receptacle exists as an MRS twist of type (G) (01 §5) over the factor-1 diamond ring, or as the invariant
subvariety with the transition divided by the kernel order. The change-of-rings functoriality for type (G) is NOT_PRINTED
in MRS §1–2 (formal; see 04 L1).

## §2. Galois descent of the A_r-modified coefficient-retaining point: a tame-nebentype twist is missing

**Input laws.**
(a) Atkin–Lehner conjugation [Hida p.15, citing MW86 p.237, MW84 2.5.6]: for σ with ζ^σ = ζ^{z}, z ∈ (Z/Np^r)^×,
    W^σ = <z>∘W = W∘<z>^{-1}.  The same law holds for the (A,P)-model normalization W(A,P) = (A/<P>, Q), e(P,Q) = ζ:
    σWσ^{-1}(A,P) = (A/<P>, Q') with e(P,Q') = ζ^z, so Q' = zQ; and W<a> = <a>^{-1}W because e(aP,Q'') = ζ forces Q'' = a^{-1}Q.
    BCPV's own evidence that its W_{Np^r} obeys a law of this kind: Lemma 4.2(ii) (index inversion) and the target
    Z_p[Δ_{N_hp^r}] of (1.6).
(b) All Hecke correspondences T'_ℓ, U'_p, <d>, the idempotent e'_ord, Π_Z and the tame push-downs are defined over Q.
(c) BCPV (4.1)–(4.3), Lemma 4.2(ii): σ_mΔ^ord_r[d] = Δ^ord_r[m^{-1}d] = <m,m,m>^{1/2}Δ^ord_r[d] for m ∈ 1+pZ_p (a square).
(d) H9R16-A/B balance: Φ^mod_r(t_2u', t_3) = Φ^mod_r(t_2, u't_3); diamonds move between factors 2 and 3 unchanged.

**Tame part.** Let σ ∈ Gal(Q̄/Q(μ_{p^r})) with χ_cyc(σ) ≡ n (mod N), n ∈ (Z/N)^×.
1. σ fixes Δ_r[d] (defined over Q(μ_{p^r})). σ(W_{Np^r}^{⊗3}) = W^{⊗3}<n,n,n>^{-1}. The diagonal tame diamond preserves
   Δ_r[d] (it preserves X_123 ⊂ X_1(N)^3 and does not touch the p^r-Weil-pairing conditions). Hence σΔ^ord_r[d] = Δ^ord_r[d],
   and <n,n,n>Δ^ord_r[d] = Δ^ord_r[d].
2. σ(A_r) = σ(W_{N_gp^r})^{-1}(U'_p)^r = <n>W^{-1}(U'_p)^r = W^{-1}<n>^{-1}(U'_p)^r = A_r∘<n>^{-1}  (factor 3 only).
3. Therefore σΦ^mod_r(t_2,t_3) = Π_{Z,*}((1⊗t_2⊗A_r t_3<n>^{-1})Δ^ord_r) and, by step 1 (<n>^{-1}_{(3)}Δ^ord = <n>_{(1)}<n>_{(2)}Δ^ord),
       σΦ^mod_r(t_2,t_3) = <n>_{(1)} · Φ^mod_r(t_2<n>, t_3).
   Using (d) the auxiliary diamond cannot be cancelled: the only relations available are balance (2 ≡ 3) and the diagonal
   relation <n>_{(1)}<n>_{(2)}<n>_{(3)} ≡ 1, under which the class of the twist is <n>^{-1} on the carrier, equivalently
   <n>_{(1)}<n> on the carrier. It is trivial on a quotient iff <n> acts trivially there.
4. On the f-isotypic output (ε_f = 1, BCPV §1.1.5) and the g-branch quotient of B^bal_r (where <n> acts by ε_g(n); by
   balance the same value on factors 2 and 3):  σ acts on the projected point through **ε_g^{(t)}(n)^{±1}**.

**p-part.** For σ_m with m ∈ 1+pZ_p (and n = 1): factors 1,2,3 receive <m>^{1/2} from (c); step 2 gives A_r∘<m>^{-1} on factor 3.
Moving diamonds between factors 2 and 3 by (d): the auxiliary total is <m>^{1/2}·<m>^{1/2}·<m>^{-1} = 1. Hence
    σ_mΦ^mod_r(t_2,t_3) = <m>^{1/2}_{(1)} Φ^mod_r(t_2,t_3):
exactly the dagger twist on the output factor. (The A_r modification is what makes the auxiliary p-part Galois-neutral —
a consistency check on H9R16-A/B.)

**Consequence.** Over K_0 = Q(μ_p) the coefficient-retaining finite modified point satisfies
    σ ∘ Φ̄^mod_r = <χ(σ)>^{1/2}_{p,(1)} · <n_σ>_{(1)} ∘ Φ̄^mod_r ∘ R(<n_σ>),   n_σ := χ_cyc(σ) mod N,
where R(u) is the action of u on B^bal_r. The dagger receptacle of H9R16-C encodes only the first factor. The tame factor is
a character of Gal(Q(μ_N)/Q), and Q(μ_N) ∩ Q(μ_{p^∞}) = Q, so no choice of p-cyclotomic base absorbs it.
In the étale picture BCPV absorb the same twist by replacing the third factor with h^c = h ⊗ ε_h^{-1} as a Galois module
((1.7), p.5); the point side has no Galois action on the Hecke-coefficient carrier, so the twist must be put into the MRS
lattice explicitly (for η_{K/Q}: a quadratic twist of the coefficient module, MRS Ex. 1.5(ii)).

**Relevance.** In the Castella–Hsieh case the g-family has nebentype ω^{-1}η_{K/Q} (§4.4), so ε_g^{(t)} ⊇ η_{K/Q} ≠ 1 and the
twist is nontrivial exactly in the case the route targets.

**Classification.** TYPE_MISMATCH: P_r^{tr,†} as "dagger/MRS object over K_0" does not contain the finite A_r-modified
point unless the lattice also carries the tame-nebentype character. Not FALSE: the retyped receptacle (04 §1) contains it
by the computation above, which is a proof from printed laws (a)–(d). Also flagged: A_r uses W at native level N_gp^r
while Δ^ord uses W at common level Np^r; the push-down N → N_g does not intertwine W_{Np^r} with W_{N_gp^r} without
degeneracy/Atkin–Lehner-at-N/N_g factors (Lane 1 bookkeeping; it changes only the tame character bookkeeping in step 1).

## §3. BCPV (4.9): the printed constant does not make (4.8) commute

Let ψ = Σ_{g∈G_{r+1}} ψ_g·g ∈ Hom_{Z_p[G_{r+1}]}(S_{r+1}, Z_p[G_{r+1}]), so ψ_g = φ(g^{-1}•) with φ = G(ψ) = ψ_e (BCPV p.20).
Equivariance gives ψ_g(hx) = ψ_{h^{-1}g}(x). For y = ϖ_1^{*⊗3}(x') and k ∈ ker(G_{r+1}→G_r): ϖ_1∘<k> = ϖ_1 (k ≡ 1 mod p^r,
DR22 (1.13)–(1.14)), so ky = y and ψ_{g̃k}(y) = ψ_{g̃}(y) for all k. The fibre of pr over g' has |ker| = p^3 elements
(G_r ≅ (Z/p^{r−1})^3). Hence (4.9) sends ψ to Σ_{g'} (p^3/p)·ψ_{g̃'}∘ϖ_1^{*⊗3}·g', and G_r of this is p^2·φ∘ϖ_1^{*⊗3} = p^2·(ϖ_1^{*⊗3})'(φ).
(4.8) asserts the square with (ϖ_1^{*⊗3})' commutes, which requires the factor 1/p^3 (the average over the kernel), not 1/p.
DR22 L2.8, the source cited, has no constant and is consistent (its proof uses the distribution relation of DR22 L2.4).

**Classification.** FALSE_AS_PRINTED (a constant p^2 per level in BCPV (4.9)). Not a route obstruction if τ^et is taken from
DR22 L2.8. It does correct the H9R6/H9R9 reading of (4.9): integrality survives (the p^3 averaged terms coincide), but any
τ^et written from (4.9) literally is off by p^2 per level. Independent re-check recommended (arithmetic only).

## §4. Modular level change versus field corestriction

* Hida's Kummer diagrams (p.16–18) have the SAME field κ on both rows; π^r_s is defined over Q.
* DR22 L2.8 is over the FIXED base Q(ζ_1): group-ring projection p_{r+1,r} and push-forward of test vectors; no corestriction.
* BCPV L4.7: passage Q(μ_{p^r}) → Q(μ_p) is unique descent (restriction is injective), not corestriction.
* In a type (G) receptacle (post-contraction, non-induced), take x ∈ H^1(K_0, M^†_{r+1}). Then
  Cor_{F_{r+1}/F_r}(res_{F_{r+1}}x) = Cor∘res_{F_{r+1}/F_r}(res_{F_r}x) = p·res_{F_r}(x). So a vertical map that uses Cor on the
  field side while the other side uses descent + p_{r+1,r} differs by [F_{r+1}:F_r] = p per level.
* In a type (Z) / induced receptacle with the triple G_r, p_{r+1,r} is Cor along the diagonal cyclic part composed with a
  sum over the p^2 transverse cosets of ker(G_{r+1}→G_r); on invariants this is the p^3 of §1.

**Classification.** The H9R16-C wording "cyclotomic descent/corestriction or Shapiro" is under-determined. Literal Cor
paired with descent is FALSE (off by p per level). Consistent choice: descent (restriction-type) + group-ring projection on
the dagger lattice, no corestriction. TYPE caution, no obstruction once fixed.

## §5. "Hida's w-twisted transition" versus BCPV's untwisted transition

* BCPV's étale tower is untwisted ϖ_{1,*} on e'_ord-parts (Cor 4.11, Def 4.12). DR22's untwisted ϖ_{1*} tower is compatible with
  U_p^* := π_{1*}π_2^* (DR22 p.8).
* Hida: the UNtwisted Albanese system {Ĵ_s, π_{s,r,*}} is T*(n)-equivariant and carries e* (co-ordinary); Lemma 5.1 gives
  π_*: Ĵ^r_s(k)^{co-ord} ≅ Ĵ_r(k)^{co-ord} at point level. The w-twisted system {Ĵ_s, π^r_s} is its conjugate for the U(p)-ordinary part.
* Hida's X_r is the μ_{Np^r} ↪ E model (p.1); BCPV/DR22 use the (A,P) model. No source prints the model isomorphism together with
  its effect on ϖ_1 and on U versus U*.
* Therefore the point-level counterpart of BCPV's untwisted e'_ord tower is, a priori, Hida's UNTWISTED co-ordinary system,
  conditional on U'_p ↔ U*(p) and on the model identification. Building τ^MW from π^r_s = w_r π_* w_{r+1} while τ^et is untwisted
  forces the comparison through w_r(·)w_{r+1}, so the discrepancy enters as δ_r(·)δ_{r+1}^{-1}, not as a single δ_r.

**Classification.** TYPE caution plus NOT_PRINTED dictionary (Lane 1). Not FALSE: either formulation can be made consistent,
but they are not interchangeable, and the frozen instruction prejudges the twisted one.

## §6. Kummer injectivity, p-completion, inverting p

PASS, with conditions:
1. Over a fixed number field F: A(F)⊗Z_p ↪ H^1(F, T_pA) (Hida L2.1; no reduction hypothesis); ⊗Q_p stays injective (flatness).
2. Descent: res: H^1(K_0, T^{tw}) → H^1(F'_r, T) is injective because T_pA^{G_{F'_r}} = 0 (A(F'_r)[p^∞] finite). Point descent
   may therefore be inferred from class descent plus injectivity — once the point exists over F'_r in the right twist (§2).
3. Coefficients must enter as Hom_{Z_p}(B^bal_r, Ĵ) (left exact). B^bal_r ⊗ Ĵ is right exact only and can acquire a kernel from
   Tor_1(B^bal_r, coker Kum); B^bal_r is a quotient module and may have torsion.
4. e'_ord gives a direct summand of the p-completed group, and (U'_p)^{-r} exists on the ordinary part of a finitely generated
   Z_p-module. No inverse Chow correspondence is needed.

## §7. Coefficient retention across the transition

The carrier map B^bal_{r+1} → B^bal_r is induced by Hecke-algebra restriction (Hida p.3: h_s → h_r), and ring maps preserve the
balance relation. But A_{r+1} and A_r contain W at different levels, and W interchanges ϖ_{1,*} and ϖ_{2,*} (BCPV L4.10 proof).
So on factor 3 the degeneracy compatible with A-transport is ϖ_2-type (A-conjugated), and one U'_p per level is left over, matching
the a_p(g)^{-r} in BCPV (4.14) against a_p(g)^{-2r} in L4.15. Applying ϖ_{1,*} uniformly to all three factors after A_r-transport
(as Cor 4.11 does for the untransported TRIPLE class) is a TYPE error. Operator-level version: NOT_PRINTED, formal given Lane 1's
constants. No obstruction found.

## §8. g^c duality and transition direction

The third factor is the Rosati-dual model. The adjoint of ϖ_{1,*} under the pairing is ϖ_1^*. DR22 L2.8 pushes forward the test
vectors and uses (ϖ_1^3)^* in its proof, and BCPV (4.9) uses ϖ_1^{*⊗3} in Hom-coordinates. The output factor 1 stays covariant
(Albanese), so τ^MW is not reversed. The dual factor's coefficients must move by the adjoint (op) convention, already encoded in
H9R16-A/B's ρ_r: (T'_r)^op → T_r. PASS with that convention. Treating the dual factor as covariant is a TYPE error.

## §9. A central diamond discrepancy δ_r (Lane 1's possible output)

Suppose W_{Np^r} = δ_r·w_r after the model identification.
* Harmless if δ_r ∈ (Z_p[diamonds])^× is defined over Q. It commutes with σ, so the twisted-equivariance law of §2 is unchanged.
  A p-part diamond on factor 3 reindexes Δ_r[d] via (4.1). In packaged sums this is multiplication by a group-like unit commuting
  with Galois. A level-dependent δ_r = <c>^r is absorbed by P'_r := <c>^{-r}P_r (c := ζ-compatibility defect; e.g. Hida's
  ζ_{Np^r} := ζ_Nζ_{p^r} gives ζ_{Np^{r+1}}^p = ζ_N^pζ_{p^r} ≠ ζ_{Np^r}, a tame <p>-type defect).
* Not harmless if δ_r involves a single W/w, a level-mixing W_{N/N_g}, or a pseudo-eigenvalue/Gauss-sum scalar. Those are not
  endomorphisms over K_0, so the twisted-invariant receptacle is not preserved.
* Sufficient identity for the square: τ^et∘δ_{r+1} = u_r·δ_r∘τ^et with u_r a diamond unit over Q, then renormalize by Π u_j.

## §10. Was point existence inferred from an étale realization?

No, in the frozen C text. Φ^mod_r is a Chow-level construction (Π_{Z,*}, algebraic correspondences, p-adically completed
e'_ord per BCPV (4.4)), so it exists in Ĵ_r(F'_r)^ord. What is NOT_PRINTED is its global Kummer identity
Kum∘Φ̄^mod_r = (modified étale contraction)∘cl_1(Δ^ord_r). BCPV §6 prints only res_p/log comparisons. The identity is formal from
étale Abel–Jacobi functoriality under correspondences plus continuity for e'_ord. The fixed-base point is legitimate only through
§6.2, after §2's retyping.

## §11. Summary

| Attack point | Result | Class |
|---|---|---|
| balanced finite point ∈ fixed-base MRS module? | NO for the frozen dagger-only receptacle when ε_g^{(t)} ≠ 1 (§2); YES after adding the tame-nebentype twist | TYPE_MISMATCH |
| Kummer target = correct Tate representation? | NO for type (Z) (rank \|G_r\|·2g vs 2g) (§1) | TYPE_MISMATCH |
| level change vs corestriction conflated? | wording ambiguous; literal Cor vs descent is off by p (§4) | FALSE if literal; caution |
| group-ring projection vs MRS lattice | frozen τ^geom = s_r⊗ϖ_* is off by p^3 on invariants; BCPV (4.9) off by p^2 (§1, §3) | TYPE_MISMATCH; FALSE_AS_PRINTED (4.9) |
| Hida w-transition on the twisted object | exists formally over Q (π^r_s is diamond-linear), but pairs with untwisted BCPV only through extra W-conjugation (§5) | NOT_PRINTED dictionary |
| central diamond changes dagger descent? | no, if δ_r is a Q-rational diamond unit (§9) | PASS (conditional) |
| p-completion / inverting p vs injectivity | no loss; coefficients via Hom (§6) | PASS |
| coefficient retention across transition | survives with A-conjugated factor-3 degeneracy (§7) | NOT_PRINTED |
| g^c duality changes direction | adjoint convention on the dual factor only (§8) | PASS |
| point existence inferred from étale? | no; global Kummer identity not printed (§10) | NOT_PRINTED |

Net: H9R16-C is NOT killed. The square as frozen is not well-typed: its only explicit receptacle has the wrong Tate module, and no
dagger-only receptacle contains the A_r-modified coefficient-retaining point in the Castella–Hsieh case. The retyped square is in 04.

## Convention note (applies to §2 and to 04 §1)

The exponent signs of the diamonds in §2 depend on (i) the sign in the Atkin–Lehner conjugation law (W^σ = <z>W, Hida p.15), and
(ii) the transpose convention by which a diamond on factor 1 passes through Π_Z = X_14 × Z to the output factor. Changing either
convention inverts some exponents. It does not change the two conclusions: the p-part auxiliary twists cancel, and a tame
diamond twist <n_σ> on the carrier survives. That twist is nontrivial on the g-branch iff ε_g^{(t)} ≠ 1.
