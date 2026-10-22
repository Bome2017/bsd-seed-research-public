# 03 — Derivation (Lane 1: BCPV W_{Np^r} versus Hida w_r)

Types and notation: 01. Sources: 02. Machine check: `_verify/wl_dictionary_check.py` (exact rational
lattice model of complex points, generic τ; output `_verify/wl_dictionary_check.out`, all positive tests
pass, negative controls fail as expected) and `_verify/up_commutation_check.py`.

## 0. Result in one paragraph

BCPV's curve X_1(Np^r) classifies (A, P) with P a point of order Np^r; Hida's X_r classifies
(E, φ: μ_{Np^r} ↪ E). These are **different Q-forms** of Γ_1(Np^r)\H* (KLZ2 §7.2 prints the resulting
diamond-valued Galois twist). BCPV's W and Hida's w live on different curves, so "W = δ·w" only has
meaning after a model identification. There is a **ζ-free, Q-rational** identification
α_r: X^pt_r ≅ X^μ_r, (A,P) ↦ (A/⟨P⟩, Weil-pairing μ-structure). Through it:

    W^BCPV_{Np^r} = ⟨c_r⟩^{-1} ∘ α_r^{-1} ∘ w_r ∘ α_r,
    α_r^{-1} ∘ π^{r+1}_r ∘ α_{r+1} = ⟨u_r⟩^{-1} ∘ ϖ_{1,*},

with c_r, u_r explicit units (01 §2) and ⟨·⟩ the Q-rational diamond (A,P) ↦ (A,dP). The discrepancies
are Q-rational, central in the Hecke algebra and of finite order; they are harmless in the fixed-base
dagger/MRS transition when inserted as in §4. The Hecke-preserving identification ι_ζ, which H9R12 implicitly used
(U'_p ↔ U^*(p)), is Galois-twisting and gives a type mismatch for Kummer squares over Q or K_0 (§5).

## 1. Lemmas (moduli; every identity machine-checked where noted)

Fix M = Np^r ≥ 4. Moduli points are taken up to isomorphism, so (A,P) = (A,−P): ⟨−1⟩ is the identity
on X^pt_r and g_{−1} is the identity on X^μ_r. All identities below are identities of morphisms of curves
(over Q(μ_M) where a root of unity is involved) and hence, by Albanese functoriality, of homomorphisms of
Jacobians and of maps on H^1_et(·, Z_p(1)) = T_p J. For coefficient sheaves TSym^k with k > 0 each
suppressed ⟨−1⟩ acts by (−1)^k; H9R16-C points live at k = 0.

**L1 (α_r is a Q-isomorphism).** For (A,P) over a Q-scheme S, put G = ⟨P⟩ ≅ Z/M, B = A/G, and
e_P: A[M]/G → μ_M, Q ↦ e_M(P,Q). e_P is well defined (e_M(P,P) = 1) and an isomorphism: on geometric
fibres the e_M-annihilator of a point of exact order M is the cyclic group it generates. Put
φ := e_P^{-1}: μ_M ≅ A[M]/G ⊂ B. The construction uses no auxiliary choice and commutes with base change,
so it is a morphism of moduli functors over Q; by L3 it has inverse α' := (E,φ) ↦ (E/Im φ, i(1)) with Hida's
i = (φ^*)^{-1}. Hence α_r: Y^pt_r ≅ Y^μ_r over Q, extending uniquely to X^pt_r ≅ X^μ_r and J^pt_r ≅ J^μ_r.
(A statement of this kind appears only in a commented-out line of DR22's TeX: NOT_PRINTED.)

**L2 (root-of-unity dependence = Galois behaviour).** For a moduli morphism f_ζ defined over Q with
parameter ζ, σ∘f_ζ∘σ^{-1} = f_{σ(ζ)}. Directly from the definitions, for z ∈ (Z/M)^×:

    W_{ζ^z} = ⟨z⟩ ∘ W_ζ          (the new P'' satisfies e(P,P'') = ζ^z, so P'' = zP')         [check T4a]
    w_{ζ^z} = g_{z^{-1}} ∘ w_ζ    (ϕ_{ζ^z}(ξ) = ϕ_ζ(ξ^{z^{-1}}))                               [check T4b]
    ι_{ζ^z} = ι_ζ ∘ ⟨z^{-1}⟩      (φ(ζ^{za}) = aP means φ(ζ^b) = z^{-1}bP)                      [check T4c]

So for σ with σ(ζ) = ζ^z: σ(W) = ⟨z⟩W, σ(w) = g_{z^{-1}}w, σ(ι) = ι⟨z⟩^{-1}.

**L3 (w_ζ ∘ α = ι_ζ).** Let B = A/⟨P⟩, π: A → B, φ(ξ) = π(Q_ξ) with e^A_M(P,Q_ξ) = ξ. Pick y_0 with
M y_0 = P. Then π(y_0) ∈ B[M] and, using e^B_M(z, πQ) = e^A_M(π̂z, Q) and π̂π = [M],
e^B_M(π y_0, φ(ξ)) = e^A_M(M y_0, Q_ξ) = e^A_M(P, Q_ξ) = ξ. So Hida's i(1) is the class of π(y_0) (for the
Cartier-dual orientation e(x, φ(ξ)); the other orientation replaces it by its negative), and
w_ζ(B, φ) = (B/Im φ, ζ^m ↦ m π(y_0)). Since Im φ = A[M]/⟨P⟩, B/Im φ = A/A[M] ≅ A via [M], carrying
π(y_0) to M y_0 = P. Hence w_ζ(α(A,P)) = (A, ζ^m ↦ mP) = ι_ζ(A,P).                        [checks T1, T1']
Since Hida's definition factors as w_ζ = ι_ζ ∘ α', this also gives α'∘α = id (L1).

**L4 (diamonds under α).** e(dP,Q) = e(P,Q)^d, so α(A,dP) = (A/⟨P⟩, φ∘d^{-1}):  α∘⟨d⟩ = g_{d^{-1}}∘α.  [check T5]

**L5 (W on the point model).** W_ζ(A,dP) has P'' = d^{-1}P', so W_ζ⟨d⟩ = ⟨d⟩^{-1}W_ζ (KLZ2 §2.5 relation).
ι_ζ∘W_ζ = α (both send (A,P) to (A/⟨P⟩, ζ^a ↦ aP')). Computing W_ζ twice with the dual-isogeny pairing
as in L3 gives W_ζ^2(A,P) = (A,−P), so W_ζ^2 = ⟨−1⟩ = id on X^pt_r and W_ζ^{-1} = W_ζ there
(consistent with KLZ2's W_N^2 = diag(N,N)⟨−1⟩_N).                                             [check T3]

**L6 (μ-restriction versus ϖ_1).** Let ζ' be a primitive Np^{r+1}-th root, ζ a primitive Np^r-th root,
(ζ')^p = ζ^u. Restricting φ^{ζ'}_P to μ_{Np^r}: ζ^{ub} = (ζ')^{pb} ↦ pbP. Hence
π ∘ ι_{ζ'} = ι_ζ ∘ ⟨u^{-1}⟩ ∘ ϖ_1. For Hida's ζ^H_{Np^r} = ζ_N ζ_{p^r}, u = u_r ≡ p (mod N), ≡ 1 (mod p^r);
u_r = 1 only for p-power-coherent roots (e.g. KLZ2 §7.1's e^{2πi/m}).                        [checks T8, u_r]

## 2. Theorems C1-a, C1-b, C1-c

**Theorem C1-a (literal W/w relation).** Let ζ^B be the root defining BCPV's W_{Np^r} (KLZ2 §2.5 moduli
operator with Q = Np^r; the root is NOT_PRINTED in BCPV) and ζ^H := ζ_N ζ_{p^r} Hida's. Define c_r by
ζ^H = (ζ^B)^{c_r}. Then, as automorphisms of X^pt_r ⊗ Q(μ_{Np^r}), of J^pt_r ⊗ Q(μ_{Np^r}), and of
H^1_et(X^pt_{r,Qbar}, Z_p(1)):

    W^BCPV_{Np^r}  =  δ_r ∘ (α_r^{-1} ∘ w_r ∘ α_r)  =  (α_r^{-1} ∘ w_r ∘ α_r) ∘ δ_r^{-1},     δ_r := ⟨c_r⟩^{-1},

and the same formula holds with α_r replaced by ι_{ζ^H}.

*Proof.* From L5, α = ι_ζ W_ζ; from L3 and L5, ι_ζ^{-1} w_ζ ι_ζ = α'ι_ζ = W_ζ^{-1} = W_ζ. Hence
α^{-1} w_ζ α = W_ζ^{-1}(ι^{-1}wι)W_ζ = W_ζ for every ζ. With ζ = ζ^H and L2, W_{ζ^H} = ⟨c_r⟩W_{ζ^B}.
The second form uses W⟨c⟩ = ⟨c⟩^{-1}W (L5). ∎                                                [check T7; NEG7 fails]

For KLZ2 §7.1 roots ζ^B = e^{2πi/Np^r} and Hida roots ζ_N = e^{2πia/N}, ζ_{p^r} = e^{2πib/p^r}:
c_r = a p^r + b N (mod Np^r), i.e. c_r ≡ a p^r (mod N) and c_r ≡ bN (mod p^r). The tame part is
**level dependent** (multiplied by p at each step) and cannot be removed by re-choosing Hida's fixed ζ_N.

**Theorem C1-b (type of the discrepancy).** δ_r lies in the image of (Z/Np^r)^× in Aut_Q(X^pt_r). It is
(i) defined over Q; (ii) central in the Hecke algebra generated by T'_ℓ, U'_q, T_ℓ, U_q, ⟨d⟩;
(iii) of finite order, hence invertible over Z; (iv) not commuting with W (Wδ_rW^{-1} = δ_r^{-1}), so
the order in C1-a matters; (v) on a weight-two eigencomponent with tame character ε and wild character ψ
it acts by the root of unity ε(c_r)^{∓1}ψ(c_r)^{∓1} (sign fixed by the diamond convention).

*Consistency checks against printed formulas.* By L2 and L4, σ(α^{-1}wα) = α^{-1}g_{z^{-1}}wα = ⟨z⟩(α^{-1}wα)
and σ(W^BCPV) = ⟨z⟩W^BCPV, so σ(δ_r) = δ_r, as (i) requires.
BCPV Lemma `DR_Lemma_2_5`(ii) prints σ_mΔ^ord_r[d] = Δ^ord_r[m^{-1}d]. With σ_m(W) = ⟨m⟩W (L2) and DR22's
⟨a_1,a_2,a_3⟩Δ_r[d] = Δ_r[a_2a_3d_1, a_1a_3d_2, a_1a_2d_3]:
σ_m(W^{⊗3}Δ_r[d]) = (⟨m⟩W)^{⊗3}Δ_r[md] = W^{⊗3}⟨m^{-1}⟩^{⊗3}Δ_r[md] = W^{⊗3}Δ_r[m^{-1}d]. ✓
A Q-rational W would give Δ^ord[md]; the opposite Galois orientation would give Δ^ord[m^3d]. So BCPV's
printed lemma pins the L2 type of their W. Hida's printed w^σ = ⟨z⟩∘w = w∘⟨z^{-1}⟩ agrees with L2
(σ(w) = g_{z^{-1}}∘w as Albanese maps) exactly when Hida's ⟨z⟩ on J_r is the Picard pullback g_z^* = (g_{z^{-1}})_*,
the same functoriality Hida uses for Hecke operators (LMW §3). Status: INFERRED; C1-a itself uses only
the moduli maps and does not depend on this reading.

**Theorem C1-c (Hida's w-twisted transition on BCPV's curve).** As homomorphisms J^pt_{r+1} → J^pt_r over Q:

    α_r^{-1} ∘ π^{r+1}_r ∘ α_{r+1} = ⟨u_r⟩^{-1} ∘ ϖ_{1,*},     u_r ≡ p (mod N), u_r ≡ 1 (mod p^r),

where π^{r+1}_r = w_r ∘ π_* ∘ w_{r+1} is Hida's transition built with his roots ζ^H.

*Proof.* w_{r+1}α_{r+1} = ι_{r+1} (L3); π_*ι_{r+1} = ι_r⟨u_r^{-1}⟩ϖ_{1,*} (L6); w_rι_r = w_r w_r α_r = α_r
(L3 and Hida's w_r^2 = 1). Compose. ∎                                                        [check T6; NEG6 fails unless p ≡ 1 mod N]

**Corollary C1-c'.** With v_s ≡ p^s (mod N), v_s ≡ 1 (mod p^s), the maps β_s := α_s∘⟨v_s⟩ satisfy
β_r∘ϖ_{1,*} = π^{r+1}_r∘β_{r+1}. So BCPV's point-model tower {J^pt_s, ϖ_{1,*}} and Hida's w-twisted tower
{J^μ_s, π^s_r} are isomorphic Q-rational projective systems. Proof: ⟨v_{r+1}⟩ ≡ ⟨v_r⟩⟨u_r⟩ at level Np^r,
and diamonds commute with π^s_r (w⟨d⟩w = ⟨d⟩^{-1}) and with ϖ_{1,*}.

## 3. Hecke dictionary (Theorems C1-d, C1-e, C1-f)

**Theorem C1-d (U_p versus U'_p versus U^*(p)).** Under the Q-rational α_r:

    α_r^{-1} U(p) α_r = U'_p,   α_r^{-1} e α_r = e'_ord,   α_r^{-1} U^*(p) α_r = U_p,   α_r^{-1} e^* α_r = e_ord,
    α_r^{-1} U(q) α_r = U'_q (q | N),   α_r^{-1} T(ℓ) α_r = T'_ℓ (ℓ ∤ Np).

*Proof.* (1) α = ι_ζ W_ζ (L5). With ζ = e^{2πi/M}, ι_ζ is the identity of Γ_1(M)\H for the standard
uniformisations, so it carries each double-coset operator to the same double-coset operator with the same
functoriality. Conjugation by the **full-level** Atkin–Lehner operator exchanges each unprimed operator
with its primed transpose and introduces no diamond (BSV (68): w_{Np}U_p = U'_p w_{Np}; BSV (91): U_q ↦ U'_q,
T_ℓ ↦ T'_ℓ; BCPV §1.1.8). So α^{-1}Xα is the primed/unprimed partner of ι^{-1}Xι.
(2) Which partner is fixed by printed equivariances, not by unwinding conventions. Hida prints
U(p)∘π^s_r = π^s_r∘U(p). By C1-c, α^{-1}U(p)α commutes with ⟨u_r⟩^{-1}ϖ_{1,*}, hence with ϖ_{1,*}. Of the two
p-correspondences, C1:(A,P) ↦ Σ_{D∩⟨P⟩=0}(A/D, P mod D) commutes with ϖ_1: X_1(Np^{r+1}) → X_1(Np^r) and its
transpose C2 does not (`_verify/up_commutation_check.out`: 24/24 versus 0/24, r ≥ 1 on the target).
Unwinding KLZ2's U'_p = pr_*∘Φ_p^*∘p̂r^* on divisors gives exactly C1. Hence α^{-1}U(p)α = U'_p, and taking
limits of powers, α^{-1}eα = e'_ord. α is an isomorphism of curves, so it respects canonical polarisations
and Rosati involutions, which gives the U^*(p) and e^* statements.
(3) Hida defines U(p), U(q) and T(ℓ) by the same functoriality for diag(1,n) double cosets (LMW §3); KLZ2
defines U'_p, U'_q and T'_ℓ by one formula (§2.4). By (1), α^{-1}(·)α lands in the same (primed) family for
all of them, as it does for U(p) by (2). ∎

Status of (3): proved given the uniform-convention reading, which is printed in both sources. It is not
load-bearing for H9R16-C: only U'_p, e'_ord, diamonds and ϖ_{1,*} enter the f-side tower.
Consequence for g versus g^c: α carries BCPV's primed Hecke algebra T_{N p^∞} = ⟨T'_ℓ, U'_q, ⟨d⟩⟩ onto
Hida's h = ⟨T(n), U(q), ⟨d⟩_H⟩ with the same labels. The g^c-side of BCPV (h^c = h ⊗ ε_h^{-1}) matches Hida's
w-image f^*_P = w_r(f_P) (LMW §5), which is consistent with C1-f below.

**Theorem C1-e (diamonds).** α_r^{-1} g_d α_r = ⟨d⟩^{-1} as Albanese maps (L4). With Hida's Picard reading
⟨d⟩_H = g_d^* = (g_{d^{-1}})_* (C1-b), α_r^{-1}⟨d⟩_H α_r = ⟨d⟩_pt. BSV's ⟨d⟩ on H^i is the pullback and ⟨d⟩'
the pushforward (02 S4). KLZ2 lets Λ_D act through the inverse diamonds at p. In any formula with group-ring
coefficients, write down which of these four conventions is meant.

**Theorem C1-f (BCPV's A_r in Hida's language).** At level N_g p^r, k = 0:

    A_r = W_{N_g p^r}^{-1}(U'_p)^r = α_r^{-1} ∘ w_r ∘ g_{c_r^{-1}} ∘ U(p)^r ∘ α_r ,

a map e'_ord J^pt_r → e_ord J^pt_r over Q(μ_{N_g p^r}), which in Hida's model is e J^μ_r → e^* J^μ_r.
*Proof.* W^{-1} = W at k = 0 (L5). By the second form of C1-a, W = α^{-1}wα⟨c_r⟩. Then
α⟨c_r⟩α^{-1} = g_{c_r^{-1}} (L4) and α U'_p α^{-1} = U(p) (C1-d). ∎

## 4. Is δ_r harmless in the fixed-base dagger/MRS transition, and where does it go?

Receptacle (H9R8/H9R9): A_r^† = I_r^† ⊗ J^pt_r over K_0 = Q(μ_p), T_p(A_r^†) = Z_p[G_r]^† ⊗ T_p J_r.

**D1 (harmless).** Let f be a Q-rational endomorphism of J^pt_r that commutes with whatever Z[G_r]-structure
enters the tensor product. For ⊗_Z this is automatic. For ⊗_{Z[G_r]} with G_r acting through diamonds it holds
for diamonds, U'_p, T'_ℓ and ϖ_{1,*}, and fails for W, w and α. Then id⊗f is a K_0-homomorphism of the MRS
twist, T_p(id⊗f) = id⊗T_p f, and Kum∘(id⊗f) = H^1(K_0, id⊗T_p f)∘Kum by functoriality of the Kummer
sequence. δ_r = ⟨c_r⟩^{-1}, ⟨u_r⟩ and ⟨v_s⟩ are Q-rational, central and of finite order, hence
automorphisms. So they commute with Galois, with the lattice and with Kummer maps, and they preserve
injectivity, p-completion and ⊗Q_p.

**D2 (exact insertion points).** δ-type factors appear only when a BCPV operator is rewritten through Hida's
w_r or π^s_r:
* finite point: replace A_r by α_r^{-1}∘w_r∘g_{c_r^{-1}}∘U(p)^r∘α_r (C1-f), i.e. insert ⟨c_r⟩ on the g^c factor;
* modular part of τ_r^MW: replace ϖ_{1,*} by α_r^{-1}∘⟨u_r⟩_H∘π^{r+1}_r∘α_{r+1} (C1-c), i.e. insert ⟨u_r⟩ on the f factor;
* pro-system: use β_s = α_s∘⟨v_s⟩ (C1-c').
If the tower is written on BCPV's own curve, **nothing is inserted**: the modular part of τ_r^MW is ϖ_{1,*},
which is Q-rational and U'_p-equivariant, and Hida's theorems are imported through β_s.

**D3 (dagger descent unchanged by δ_r).** The wild part of δ_r is a group-like element of (Z/p^r)^×. It
commutes with the character ⟨χ⟩_r^{-1/2} (the group ring is commutative) and is Galois-invariant. So the
twisted class descends to K_0 (BCPV Lemma `lemma_Gal_action_on_bold_Delta`) iff its δ_r-translate does.

**D4 (what does change dagger descent).** Transporting a G_r-structure that acts through diamonds along α
without correction. L4 turns ⟨d⟩_pt into g_{d^{-1}}. If one uses the Albanese μ-model diamonds g_d as the
G_r-action, M^† = M ⊗_{Z_p[G_r]} Z_p[G_r]^† is converted into the ⟨χ⟩_r^{+1/2}-twist. That is a
TYPE_MISMATCH (a sign flip of the half-twist), not a scalar. Correct insertion: compose the group-ring
structure with g ↦ g^{-1}, or use ⟨d⟩_H = g_d^*.

**D5 (intrinsic, not caused by W/w).** W is not K_0-rational (L2), so A_r is not a K_0-endomorphism of A_r^†.
The finite point becomes K_0-rational only after group-ring packaging (BCPV Lemma (ii) plus the dagger).
Hence τ_r^MW must be assembled from K_0-rational maps (s_r, ϖ_{1,*}, U'_p); A_r may appear only inside the
packaged point. Since δ_r is Q-rational, the W/w dictionary neither creates nor removes this constraint.

## 5. Hostile checks — classification

| # | Finding | Class |
|---|---|---|
| K1 | H9R12's tentative "U'_p ↔ U^*(p)" is the ι-dictionary. It preserves Hecke shape but twists Galois (σ(ι) = ι⟨z⟩^{-1}; KLZ2 §7.2 prints the character 1+k+ε_N). Used for Mordell–Weil groups over Q or K_0, it compares J^pt with a diamond-twist of J^μ. The Galois-rational dictionary is α: U'_p ↔ U(p), e'_ord ↔ e, ϖ_{1,*} ↔ ⟨u_r⟩π^{r+1}_r (**w-twisted ordinary** system, not the untwisted co-ordinary one) | TYPE_MISMATCH (corrected) |
| K2 | BCPV never define W (root, orientation, pull/push) | NOT_PRINTED; absorbed into c_r, Galois type pinned by BCPV Lemma (ii) |
| K3 | BCPV's footnote target in BSV (between Prop 3.2 and Rem 3.3) contains no Atkin–Lehner operator in the author PDF | NOT_PRINTED (possible version/pagination drift) |
| K4 | Ohta 1999 Eq. 1.5.4 not read (paywalled); KLZ2 reports "τ_r = W^{-1} up to signs" | INACCESSIBLE; not load-bearing |
| K5 | The p-part w_p intertwines U_p and U'_p only up to ⟨p⟩_N (BSV (68)); full-level w_{Np} has no factor. Substituting W_{p^r} for W_{Np^r} would add ⟨p⟩_N-powers (KLZ2 W_{QQ'} = ⟨Q'⟩_QW_QW_{Q'}) | TYPE_MISMATCH if made; not made by BCPV or Hida |
| K6 | Hida's ζ_Nζ_{p^r} is not tame-coherent ⇒ u_r ≡ p mod N in C1-c; omitting ⟨u_r⟩ breaks the square by ε_f(p)^{±1} per level whenever ε_f(p) ≠ 1 (NEG6) | explicit central unit; must be inserted |
| K7 | For k > 0, W^{-1} ≠ W and ⟨−1⟩ acts by (−1)^k | irrelevant at weight-two points; keep for any Λ-adic statement |
| K8 | Hida's printed w^σ = ⟨z⟩w holds only with the Picard reading of ⟨z⟩ | INFERRED convention; not load-bearing |
| K9 | BCPV print λ_{Np^r}(g_λ) and λ_{N_g p^r}(g) for the same normalisation | printed inconsistency, out of lane (R2) |
| K10 | No finite-level point was inferred from étale data; no inverse limit, density, H9R15 localization or other downstream item was used | clean |

No FALSE statement in BCPV, KLZ2, BSV or Hida blocks C1. C1 needs no new theorem.

## 6. Non-claims

* R1 (the C2 square), R2 (tame-level W_{Np^r} versus W_{N_g p^r}) and R3 (which dagger receptacle) are not
  proved here (04).
* BCPV's actual root of unity for W is not asserted; C1-a is stated for an arbitrary one.
* The T(ℓ) ↔ T'_ℓ label in C1-d(3) rests on the printed uniform conventions; the f-side tower does not use it.
* The lattice checker validates identities on complex points for generic τ. Rationality statements (fields
  of definition) are proved from the moduli definitions and L2, not by the checker.
