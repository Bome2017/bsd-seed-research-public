# Stage 2 (NA-2): is Ξ₁∘β₁ computable from definite data? — derivation notes

Grades: SOURCE (printed, cited) / DERIVED (argued here, same-session, unreviewed) / HEURISTIC.
Notation as in the parent report D4: E/Q rank 2, K imaginary quadratic, N = N⁺N⁻ with N⁻ an odd number of
primes inert in K (definite), rank E^K(Q) = 0, P₁, P₂ a basis of E(Q)/tors, m a good modulus, (ℓᵢ, εᵢ)
admissible. V := T(J₁)/I (free of rank 2 over Z/m), J₁ = Jac X_{N⁺,N⁻ℓ₁}. S = S(N⁻,N⁺) (disc N⁻),
S_{ℓ₁} = S(N⁻,N⁺ℓ₁), S′ = S(N⁻ℓ₁ℓ₂, N⁺) (disc N⁻ℓ₁ℓ₂).

## A. The two J₁-side generators, read off BD05 (SOURCE + DERIVED)

A1 (ℓ₂ side, SOURCE BD05 §9, pp. 70–75). γ : Div(S_{ℓ₂}) → J₁(F_{ℓ₂²})/I → H¹_fin(K_{ℓ₂}, V) = V/(Frob²−1)V,
  "γ is defined by sending a point x to the image of ((Frob²_{ℓ₂} − 1)/pⁿ)x" (proof of Lemma 9.1, p. 72);
  S_{ℓ₂} ≅ S′ Hecke-compatibly (proof of Thm 9.3, p. 75, via [Wa] + strong approximation); γ "corresponds to an
  eigenform g" on S′ (Cor 9.4, p. 75); the image of the Heegner points equals L̃_g (p. 76).
  At the bottom layer (conductor 1, p ∤ N⁺) the second law is tautological: the reduction mod ℓ₂ of the CM
  divisor P_K is the Gross divisor x′_K on S′, and Kummer commutes with reduction. So
     β₁(x′_K) := loc_{ℓ₂} κ_J(ℓ₁) = γ(x′_K)            (DERIVED from SOURCE; no p-specific input).
  The identification J₁(F_{ℓ₂²})/I ≅ V/(Frob²−1)V is canonical (finite-field Kummer map; standard
  0 → T → T → J(F_q)[p^∞] → 0 via Frob_q − 1). Only the further choice "H¹_fin(K_{ℓ₂},T_{f,n}) ≅ Z/pⁿ"
  (p. 70) is non-canonical, and C(ℓ₁,ℓ₂) avoids it.

A2 (ℓ₁ side, SOURCE BD05 §5.5–5.6 + parent D1). Mumford–Tate (49) (p. 60) gives
  0 → (X^∨/I)(1) → V → X/I → 0 over K_{ℓ₁}; mod I the monodromy X/I → X^∨/I vanishes (Φ/I ≅ Z/m), so V is
  unramified at ℓ₁ (as E[m] is). H¹_sing(K_{ℓ₁},V) = Hom(I_{ℓ₁},V)^{Frob²} = X^∨/I ≅ Φ_{ℓ₁}/I (Cor 5.18,
  p. 64, geometric map), H¹_fin(K_{ℓ₁},V) = X/I. With ρ_f (parent D1): φ := image of ρ_f^{-1}(1) is a
  canonical generator of H¹_sing(K_{ℓ₁},V), up to one global sign.

A3 (the invariant, DERIVED; restates parent D4). Put
    M(ℓ₁,ℓ₂) := H¹_fin(K_{ℓ₂},V) ⊗ H¹_sing(K_{ℓ₁},V)^{−1}.
  For any G_Q-isomorphism u : V ≅ E[m] (exists: Thm 5.17 per p + CRT; unique up to (Z/m)^×), u induces
    M(ℓ₁,ℓ₂) ≅ H¹_fin(K_{ℓ₂},E[m]) ⊗ H¹_sing(K_{ℓ₁},E[m])^{−1} ≅ E(F_{ℓ₂²})/m ⊗ E(F_{ℓ₁²})/m
  (second step: Tate duality with E's Weil pairing), and this composite is independent of u (u ↦ tu
  multiplies both factors by t). Then
    C(ℓ₁,ℓ₂) = [ β₁(x′_K) ⊗ φ^{−1} ] / R(ℓ₁,ℓ₂) ∈ Z/m.
  Everything J₁-specific is in the pair (β₁, φ); the only remaining datum is the u-transport of M.

## B. Where the global datum enters (DERIVED)

B1 (the ℓ₁-side and ℓ₂-side generators live in different local cohomology groups of one global module).
  φ is defined from the ℓ₁-adic (Čerednik–Drinfeld) fibre of J₁; β₁ from the ℓ₂-reduction of J₁. Each is a
  generator of a free rank-1 module over T₁/I ≅ Z/m. A comparison of two free rank-1 modules needs extra
  structure; here that structure is the G_Q-module V (equivalently, its isomorphism with E[m]). The
  u-independent content is the relative position, inside V, of the ℓ₁-toric generator and the
  ℓ₂-coinvariant line, measured against the same two local structures of E[m].

B2 (definite data link only Eichler orders inside ONE quaternion algebra). Every canonical definite map
  used by BD05 and the parent report — Ihara degeneracy maps δ_*, Prop 5.5/5.7/5.13, ω_ℓ, ρ_f, the Ribet
  sequence Prop 5.9 — relates class sets of Eichler orders in the same definite algebra (disc N⁻, levels N⁺,
  N⁺ℓ₁, N⁺m…). Ribet's sequences relate character groups of two Jacobians whose definite sets COINCIDE
  (Prop 5.9: both sides are built on disc-N⁻ sets; Ribet's X_q(J^{pq}) and X_p(J_0(pq)) are both Z[S(p,q)]).
  S′ belongs to the algebra B′ of disc N⁻ℓ₁ℓ₂ ≠ N⁻. The only links between Z[S] and Z[S′] in the sources are
  (i) the two reductions (at ℓ₁ and at ℓ₂) of the same Shimura curve X^{(ℓ₁)} — whose comparison is the
  generic fibre, i.e. the global Galois module; and (ii) CM points, which are global objects whose
  two-place comparison again runs through a global class (B4 below). At depth 1 (one level raising) both
  ends live in the disc-N⁻ algebra, which is why ρ_f (parent D1) is definite and canonical; at depth 2 the
  algebra changes, and that is exactly where the definite description stops.

B3 (factorization lemma L1). Fix any Z/m-valued eigenform g₀ on S′ with the eigenvalues of Thm 9.3 (unique
  up to (Z/m)^× by multiplicity one, Prop 9.2 + Cor 9.4). The map Ξ₁∘γ : Z[S′] → M(ℓ₁,ℓ₂) ⊗ (E-side) factors
  through the g-eigenquotient, so Ξ₁∘γ = Λ(ℓ₁,ℓ₂)·g₀ for a unique Λ(ℓ₁,ℓ₂) (a generator of the target).
  Neither γ (defined on all of S′) nor Ξ₁ (local fields K_{ℓᵢ} = Q_{ℓᵢ²}, the same for every K in which
  ℓ₁, ℓ₂ are inert) nor R (built from E(Q) when rank E^K(Q) = 0) depends on K. Hence
      C_K(ℓ₁,ℓ₂) = Λ(ℓ₁,ℓ₂) · G_K(ℓ₁,ℓ₂) / R(ℓ₁,ℓ₂),   G_K := Σ_{σ∈Pic O_K} g₀(x′_{K,σ}),
  with G_K definite and Λ(ℓ₁,ℓ₂) independent of K. (DERIVED.) The whole unknown of RIGID_LR is Λ.

B4 (equivalent forms of Λ; each needs a non-definite input) (DERIVED).
  (a) Twisted rank-0 laws. For a ring class character χ with Σχ(σ)f(x_σ) a unit and Sel^χ_strict = 0, the
      χ-twisted first and second laws give ∂_{ℓ₁}κ^χ = (Σχf)·φ and loc_{ℓ₂}κ^χ = Σχ g(x′_σ) (J₁-normalized).
      The class with prescribed singular part at ℓ₁ is unique, so loc_{ℓ₂} = Λ^χ_E ∘ ∂_{ℓ₁} with Λ^χ_E an
      intrinsic (u-free) Galois invariant of E[m]⊗χ at (ℓ₁,ℓ₂). Hence
         C_K(ℓ₁,ℓ₂) = Λ^χ_E(ℓ₁,ℓ₂) · (Σχ f(x_σ)) · G_K / ( (Σχ g₀(x′_{χ,σ})) · R(ℓ₁,ℓ₂) ).
      All factors but Λ^χ_E are definite. Λ^χ_E needs class field theory of K(E[p], χ) (degree ≥ 960 for
      p = 5): not feasible in the brief's budget. RIGID_LR is thereby equivalent (given the laws) to a
      statement tying the rank-0 transfer Λ^χ_E to the rank-2 regulator R: equivalent ≠ circular, but no
      easier.
  (b) Congruent curve. If the ℓ₁-level-raised form lifts to an elliptic curve E₁ of conductor Nℓ₁
      (a_{ℓ₁}(E₁) = ε₁), the Shimura parametrization J₁ → E₁ gives a canonical u₁ : V ≅ E₁[m] (when it is an
      isomorphism mod I), the ℓ₂-side becomes BD99/Vigni's canonical η for E₁ (constant u·deg π_{E₁}), and
      the ℓ₁-side becomes E₁'s Tate-curve generator of Φ_{ℓ₁}(E₁)/m. What remains is one explicit
      G_Q-isomorphism E₁[p] ≅ E[p] (computable from one p-torsion point field, degree 24 for p = 5) plus
      the component-group factor of J₁ → E₁ (depth-1 definite data at (N⁻, N⁺ℓ₁)). Gate checked below (C2):
      for 389a1 no such E₁ exists in Cremona's range.

B5 (parity constraint; DERIVED + CHECKED). Frob_ℓ acts on E(F_{ℓ²})/p ≅ T/(Frob²−1)T by ε (BD05 Lemma 9.1,
  p. 72). Points of E(Q) reduce into the Frob-fixed part, so red_ℓ(E(Q)) = 0 in E(F_{ℓ²})/p when ε = −1
  (equivalently: ℓ+1+a_ℓ ≡ 0 and p ∤ ℓ+1 force p ∤ #E(F_ℓ)). Hence, when rank E^K(Q) = 0,
     R(ℓ₁,ℓ₂) ≠ 0 mod p  ⟹  ε₁ = ε₂ = +1.
  Consistency: w(g̃) = w(E)·ε₁ε₂ for a characteristic-0 lift g̃ of g (Steinberg root numbers), and
  w(g̃⊗χ_K) = w(g̃)·χ_K(−Nℓ₁ℓ₂) = w(g̃) (χ_K(−1) = −1, χ_K(N⁻) = −1 for an odd number of inert primes, χ_K(N⁺) = χ_K(ℓ₁ℓ₂) = +1), so ε₁ ≠ ε₂ forces Σg̃(x′_K) = 0 in characteristic 0,
  matching R = 0. Check (checks/parity_389_output.txt, 389a1, K = Q(√−71), ℓ < 3000): every ε = −1
  admissible ℓ has p ∤ #E(F_ℓ) (21/21 for p = 5, 30/30 for p = 7); among ε = +1 pairs, R ≠ 0 mod p in
  348/406 (p = 5) and 336/406 (p = 7).
  Consequence for the seed: the parent report's "ℓ = 283, ε = −1, covers p = 5 and p = 7" is fine for the
  first law (depth 1) but ℓ = 283 is unusable for C(ℓ₁,ℓ₂) and RIGID_LR: #E(F_283) = 288 = 2⁵·3², so R(283,·) = 0
  mod 5 and mod 7. The seed's usable primes are its ε = +1 admissible ones (p = 5: 73, 223, …; p = 7: 173, 367,
  409, …; parent checks/seed_facts2_output.txt).

B6 (cross-field corollary L2; DERIVED, not computed). Let K, K′ both satisfy the setting (ℓ₁, ℓ₂ inert in both,
  rank E^K(Q) = rank E^{K′}(Q) = 0). By B3, Q(ℓ₁,ℓ₂) := G_K/G_{K′} = C_K/C_{K′} (Λ and R cancel; sign
  conventions give ±). If Ш(E/K)[p] = Ш(E/K′)[p] = 0, parent D4 gives C_K(ℓ₁,ℓ₂) = −c_{J₁,K}(ℓ₁), independent
  of ℓ₂; the same argument with J₂ = Jac X_{N⁺,N⁻ℓ₂} (S′ is symmetric in ℓ₁, ℓ₂) shows Q is independent of ℓ₁.
  So Q is constant over all ε = +1 pairs for the modulus. Characteristic-0 reading: Q² ≡ ratio of the
  rank-0 twist values L^alg(E^K,1)/L^alg(E^{K′},1) up to u_K-type factors (Gross's formula for a lift g̃ plus
  congruence of imprimitive twisted values; the period unit cancels between K and K′). So the K-dependence of
  C is classical rank-0 information, and constancy of Q is a CONTROL for the framework (D4 + bottom-layer laws +
  Ш[p] = 0), not evidence for RIGID_LR. A computation needs Brandt modules at disc N⁻ℓ₁ℓ₂ (three primes); the
  local Sage BrandtModule handles prime discriminant only (checks/sage_brandt_capability.txt: NotImplementedError
  for N = 105; BrandtModule(389) has dimension 33), so it would need new code.

B7 (place count — why depth 1 is local and depth 2 is not; DERIVED for the maps in the sources, HEURISTIC as
  a general statement). Two quaternion algebras over Q compared by a single Shimura curve differ at the places
  where that curve's reductions switch type. Depth 1: B_{N⁻} (definite) vs B_{N⁻ℓ₁} (J₁) differ at {ℓ₁, ∞}, one
  finite place — the comparison is local at ℓ₁ (Čerednik–Drinfeld), hence canonical (ρ_f, parent D1). BD99
  Thm 6.1 is the same situation (M₂(Q) vs B_q: one finite place q, and the indefinite curve parametrizes E).
  Depth 2: B_{N⁻} vs B_{N⁻ℓ₁ℓ₂} differ at {ℓ₁, ℓ₂}, two finite places. And E's own algebra M₂(Q) vs B_{N⁻ℓ₁}
  (J₁) differs at N⁻ ∪ {ℓ₁}, again at least two finite places. Any comparison across two finite places runs
  through a generic fibre, i.e. a global Galois module — this is where Λ lives.

## C. Checks run (all ≤ 1 CPU-minute, one process)
C1 checks/parity_389.gp → parity_389_output.txt (B5).
C2 checks/find_level_raised.py, congruence_test*.gp → congruence_test_output.txt, congruence_test2_output.txt:
   for 389a1, all ε = +1 admissible (p, ℓ) with p ∈ {5,7,11,13}, ℓ < 1285 (71 pairs, 65 conductors 389ℓ, 27
   isogeny classes in Cremona's curvedata): 0 classes congruent to 389a1 mod p (a_q compared for q < 400).
   So route B4(b) has no elliptic-curve partner for 389a1 in Cremona's range; the level-raised forms there
   have Hecke field ≠ Q, and B4(b) would need abelian varieties with real multiplication.

## D. Kill test K2
K2 (fixed in advance): "if Ξ₁∘β₁ cannot be expressed through definite data without an input that exists only on
X^(ℓ₁) (Heegner points / indefinite Jacobian) or only after choosing p → NO_DEFINITE_FORMULA (scoped), stop
before probe design." — FIRES.
- β₁ is definite up to the normalization of g (B3: Λ·g₀).
- Λ(ℓ₁,ℓ₂) is not given by any definite map in the sources (B1, B2, B7). Each equivalent form needs a global
  input: Galois cohomology of E[p]⊗χ (B4a), or a congruent curve E₁ on X^(ℓ₁) plus an explicit G_Q-isomorphism
  E₁[p] ≅ E[p], which exists only after choosing p (B4b).
- Scope: the derivation routes listed (BD05 §§5, 8, 9 maps; Ribet sequences; Ihara degeneracy maps; Gross
  points incl. twisted; BD99/Vigni η). Not a proof that no definite formula can exist.
