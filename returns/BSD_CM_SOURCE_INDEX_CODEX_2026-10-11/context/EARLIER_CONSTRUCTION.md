# Construction of C(ℓ₁,ℓ₂) in one integral convention — steps C0–C8

Phase 2 of BSD_EXACT_BD_CONSTANT_2026-10-07 (change of plan in RESUME.md, ~18:00). Target (Codex review,
`~/BSD_BD_INTEGRAL_REVIEW_CODEX_2026-10-07/HANDOFF.md`): instantiate α and β at the conductor-one,
coefficient-prime-free bottom layer in one orientation convention; prove that β is the localization of the global
CM class, with orientation factors; use the fixed-idempotent quotient; then, only if this succeeds, evaluate.
Grades: SOURCE (cited) / DERIVED (argued here; same-session, unreviewed) / COMPUTED (script + output in this
folder) / HEURISTIC. Page numbers for BD05 are the 2007 preprint's (Codex: Cor 5.18 is printed p. 52).

## C0. Setting and conventions (fixed once)

- E/Q of conductor N = N⁺N⁻. K imaginary quadratic with d_K prime to N·m (BD's coprime-discriminant
  hypothesis; this excludes p = 7 for K = Q(√−7)). N⁻ is squarefree with an odd number of primes, all inert
  in K. All primes of N⁺ split in K; N⁺ may be non-squarefree.
- m = ∏ p^{n_p}, every p ≥ 5 and eligible (C2 gives the base-module condition). (ℓ₁,ε₁), (ℓ₂,ε₂) are
  admissible: ℓᵢ inert in K, ℓᵢ ∤ Nm, p ∤ ℓᵢ²−1, m | ℓᵢ+1−εᵢa_{ℓᵢ}. For detectors from E(Q), ε₁ = ε₂ = +1
  (stage-2 B5; Codex §3).
- Frobenius is arithmetic. K_ℓ = Q_{ℓ²} and Frob_{K_ℓ} = Frob_ℓ². Fix embeddings ι_{ℓᵢ} : Q̄ ↪ Q̄_{ℓᵢ}; each
  localization is restriction along ι.
- Finite-field Kummer map. For A with good reduction at ℓ, x ∈ A(F_{ℓ²}), choose y with my = x and send x to
  (Frob_ℓ² − 1)(y) mod (Frob_ℓ²−1)A[m]. This gives A(K_ℓ)/m ≅ A(F_{ℓ²})/m ≅ H¹_fin(K_ℓ, A[m]) (BD05 Lemma 9.1
  proof, p. 72).
- Singular part: H¹_sing(K_ℓ, V) := Hom(I_ℓ, V)^{Frob²}, evaluated at a fixed generator of tame inertia matched
  with a fixed compatible system (ζ_m).
- Local duality: H¹_fin × H¹_sing → H²(K_ℓ, μ_m) = Z/m, via inv_ℓ and E's Weil pairing e_m (one fixed
  convention).
- Global signs fixed once: the sign of the primitive JL form f on S, the orientation P₁∧P₂ of E(Q)/tors, and the
  orientation 𝔑⁺ ⊂ O_K of the Heegner data (O_K/𝔑⁺ ≅ Z/N⁺).
- **Parity convention at ℓ₁ (new, DERIVED).** The vertex class of the Čerednik–Drinfeld dual graph that contains
  the CM vertices r_{ℓ₁}(D_K) is called even (justification in C7).

## C1. Bottom-layer objects (no p-level)

X₁ := X_{N⁺, N⁻ℓ₁} is the Shimura curve of an Eichler order of level N⁺ in the indefinite algebra of
discriminant N⁻ℓ₁, as in BD05 §5.1, but without BD's Γ₀(p) at p. J₁ := Pic⁰(X₁), with Hecke algebra T₁ acting by
Picard functoriality.
- The level-raised character f_{ℓ₁} : T₁ → Z/m (U_{ℓ₁} ↦ ε₁) comes from the action on Φ_{ℓ₁}(J₁)/I ≅ Z/m (C2,
  C3). BD05 Thm 5.15, pp. 58–59, uses Prop 5.9, Prop 5.13, residual irreducibility, admissibility and
  hypothesis 2. None of these uses the p-level; hypothesis 2 is replaced by C2.
- V_J := T(J₁)/I with T(J₁) = ∏_{p|m} T_p(J₁).

## C2. Base rank-one quotient by a rational idempotent (Codex §2 repair) — COMPUTED for two curves

M = Z[S(N⁻,N⁺)] carries the Brandt action. v is the primitive integral f-eigenvector (row, v·T_q = a_q v) and φ
the primitive integral eigenfunctional (column). Then e_f = v φᵀ/(v·φ). For p ∤ J_f := |v·φ| (contents of v and
φ are 1), M_(p) = Z_(p)v ⊕ ker φ_(p) and M_(p)/I_f M_(p) ≅ Z_(p) via φ.

`construction/idempotent_J.sage` → `idempotent_J_output.txt` (Sage BrandtModule, prime discriminant):

| curve | definite set | h | J_f = v·φ | Cremona modular degree |
|---|---|---|---|---|
| 389a1 | S(389, 1) | 33 | 40 = 2³·5 | 40 |
| 2541c1 (N⁻ = 3) | S(3, 847) | 176 | 144 = 2⁴·3² | 288 |
| 2541c1 (N⁻ = 7) | S(7, 363) | 264 | 144 = 2⁴·3² | 288 |

Consequences:
- **For 389a1, p = 5 is not eligible** (5 ∣ J_f). Every p = 5 row on 389a1 in the stage-2 parity check is
  therefore a local group-arithmetic control only, not a BD-admitted example (Codex's "do not assume the
  uncomputed exceptional support avoids any chosen coefficient prime" — here it does not).
- **For 2541c1, p = 5 is eligible** (5 ∤ 144). This is the case of the named next attack NA-3.
- **For the seed, J_f is not computable.** S has mass ≈ 5.4·10¹⁴ (parent check). So no seed coefficient prime
  is certified eligible at this step.
- The idempotent repair exists only because f is a characteristic-0 eigenform with rational coefficients. The
  level-raised eigensystems (on X_{ℓ₁}(J₁) and on Z[S′]) exist only mod m. **No rational idempotent exists at the
  level-raised ideals**, so the repair does not reach C3.

## C3. α : Φ_{ℓ₁}/I → H¹_sing(K_{ℓ₁}, V_J) — the map is constructed; its isomorphism property is per p only

**Construction (DERIVED from SOURCE; integral, no p).**
- Čerednik–Drinfeld (BD05 Thm 5.1, p. 46) makes J₁ over Q_{ℓ₁²} a split torus quotient. Mumford–Tate gives
  0 → X → X^∨ ⊗ Q̄^× → J₁ → 0 (BD05 (49), p. 60), with ord∘[ , ] = ⟨ , ⟩ ((50)).
- Specialization J₁(K_{ℓ₁}) → Φ_{ℓ₁} = coker(j) (Prop 5.11, p. 54) is surjective, because the torus is split
  over K_{ℓ₁} = Q_{ℓ₁²}.
- Points of the identity component come from X^∨ ⊗ O^×. Their Kummer classes are unramified (m is prime to ℓ₁).
- Hence c ↦ (Kummer class of any lift of c) mod H¹_unr is a well-defined Hecke-equivariant map
  α : Φ_{ℓ₁}/I → H¹_sing(K_{ℓ₁}, V_J). This is BD05 Remark 2 after Thm 5.17 (p. 63) and Cor 5.18 (p. 64) at the
  bottom layer.

**Normalization of the source (DERIVED; parent D1 with C2).** Under C2 and m non-Eisenstein, Prop 5.13 (p. 55)
gives ρ_f : Φ_{ℓ₁}/I ≅ Z/m, ω̄(x,y) ↦ f(x) − ε₁f(y), with x in the even class (C0). The generator is
φ := α(ρ_f^{−1}(1)).

**Isomorphism (needs a per-p input — FIRST BLOCK of the integral construction).**
- α is an isomorphism iff H¹_sing(K_{ℓ₁}, V_J) is cyclic of order m and α is onto. From (49) mod I this needs
  X/I and X^∨/I to be rank one at the level-raised maximal ideal m₁, so that the monodromy vanishes mod I and
  H¹_sing ≅ X^∨/I ≅ Φ/I. Equivalently: multiplicity one for the level-raised eigensystem on J₁.
- The sources prove this only one p at a time: BD05 Thm 5.17, Step 1, pp. 61–62 ([BoLeRi] semisimplicity
  mod m_{f_ℓ}, then dim Φ/m = 1 forces k = 1), followed by Nakayama over Z/pⁿ.
- C2's rational-idempotent repair cannot replace this, because the level-raised eigensystem is defined only
  mod m.
- At a single p the proof transfers to the bottom layer: it uses (49), Thm 5.15, [BoLeRi] and the GL₂(F_p)
  image, and never BD's Γ₀(p). For n = 1 it can also be certified by exact linear algebra mod p on the
  ℓ₁-new part of Z[S(N⁻,N⁺ℓ₁)] (Prop 5.9 identifies X_{ℓ₁}(J₁) with it). V_J ≅ E[p] then follows from
  Brauer–Nesbitt together with the irreducibility of E[p].

**→ CONSTRUCTION_BLOCKED_AT_C3 (integral convention).** Citation: BD05 Thm 5.17 Step 1, pp. 61–62; Cor 5.18,
p. 64 (published p. 52): "canonical up to the choice of an identification of T_p(J^{(ℓ)})/I_{f_ℓ} with T_{f,n}".
The step needs an input available only after choosing p. It does not need Ш = 0.

## C4. β and the CM/localization compatibility — constructed; compatibility PROVED (standard)

**The CM divisor (DERIVED from SOURCE).**
- D_K := Σ_{σ∈Pic O_K} P_σ, where P_σ ∈ X₁(H) are the CM points by O_K with orientation 𝔑⁺ at N⁺. These
  exist because N⁺ is split, and N⁻ℓ₁ (ramified in the algebra) is inert in K.
- Modulo I, Div = Div⁰, since the degree is Eisenstein and I is not (BD05 p. 71). So
  κ_J := Kum(D_K) ∈ H¹(K, V_J) needs no cusp or Hodge-class correction.

**Compatibility (PROVED; standard).**
- ℓ₂ ∤ N⁻ℓ₁N⁺, so X₁ has good reduction at ℓ₂. Since ℓ₂ is inert in K, the prime ℓ₂O_K is principal and
  ℓ₂ splits completely in H. Each P_σ reduces at λ₂ := ι_{ℓ₂}|_H to a supersingular point P̄_σ ∈ S_{ℓ₂}
  (BD05 p. 75).
- For coefficients prime to ℓ₂, the Kummer map commutes with reduction (Néron model of J₁ over Z_{ℓ₂}). Hence
      loc_{ℓ₂} κ_J = γ(Σ_σ P̄_σ) =: β ∈ H¹_fin(K_{ℓ₂}, V_J),
  with γ the finite-field Kummer map of C0 composed with supersingular divisors → J₁(F_{ℓ₂²})/I (BD05 (62)–(65),
  pp. 70–71).
- No surjectivity (BD05 Prop 9.2, which uses the p-level) and no identification with S′ is needed to define β.

**Definite reading (only to compute β).**
- S_{ℓ₂} ≅ S′ = S(N⁻ℓ₁ℓ₂, N⁺) (BD05 Thm 9.3 proof, p. 75, via [Wa] + strong approximation). The bijection is
  fixed up to the normalizer of the Brandt module.
- On the g-eigenline that normalizer acts by Atkin–Lehner signs: at q | N⁺, w_q(g); at ℓ₂, U*_{ℓ₂} = Frob on
  S_{ℓ₂} (BD05 p. 75, [Ri2] Prop 3.8), consistent with γ(Frob x) = ε₂γ(x) (Lemma 9.1).
- The Gross points are x′_σ = class of Ψ : O_K → End(P̄_σ) (BD05 p. 76).
- **Orientation factor: ±1**, a product of Atkin–Lehner eigenvalues, fixed once per (K, 𝔑⁺) together with the
  bijection.

**Line normalization of β.**
- Λ is a unit iff γ is surjective and Z[S′]/I′ has rank one.
- Surjectivity is BD05 Prop 9.2. Its proof needs a torsion-free Γ̃(ℓ₂) (via Γ₁(p)) and the [DT] Ihara lemma.
  At the bottom layer the Γ₁(p) must be replaced by an auxiliary Γ₁(M) with p ∤ M−1 (the cokernel step on
  p. 73 then has order dividing M−1). This is DERIVED as a sketch only, not checked.
- Rank one of Z[S′]/I′ is again per p (multiplicity one at the level-raised ideal; same block as C3).

## C5. Localizations of P₁, P₂ — integral, canonical (DERIVED; trivial)

F_i := H¹_fin(K_{ℓᵢ}, E[m]) ≅ E(F_{ℓᵢ²})/m via C0's Kummer map. For ε = +1 these groups are cyclic of order m:
Frobenius has eigenvalues 1 and ℓ, distinct mod p (Codex §3). Then
- loc_i(P_j) := red_{ℓᵢ}(P_j) ∈ F_i;
- R_P := loc₁P₁⊗loc₂P₂ − loc₁P₂⊗loc₂P₁ ∈ F₁⊗F₂.

Detecting pairs (R_P a unit) found so far:
- seed: (73,223) at p = 5 (det 4) and (47,271) at p = 11 (det 6) (Codex §3);
- 389a1: (23,31) at p = 7, R ≡ 2, K = Q(√−8), the smallest eligible pair (`construction/smallest_detector_output.txt`);
- 2541c1: ℓ₁ ∈ {113,167} at p = 5 (stage-2 scan; R not yet computed).

## C6. The tensor recipe (Codex §1) — C is well defined, given C3 at every p | m

If H := Hom_G(E[m], V_J) is invertible with H ⊗ E[m] ≅ V_J (this is C3 at each p | m), then:
- α gives Φ ≅ H ⊗ F₁^∨, hence H ≅ Φ ⊗ F₁;
- Ξ : H¹_fin(K_{ℓ₂},V_J) = H ⊗ F₂ ≅ Φ ⊗ F₁ ⊗ F₂;
- **C(ℓ₁,ℓ₂) is the unique element of Φ/I with Ξ(β) = C ⊗ R_P.**

C is independent of h, of the bases e₁, e₂ (Codex's explicit check) and of the embeddings ι (any conjugation acts
compatibly on both sides). Ш = 0 is not used anywhere in C0–C6.

## C7. Orientation bookkeeping — one global sign (DERIVED)

| Choice | Effect on C | Fixed by |
|---|---|---|
| sign of f | ±1, global | C0 |
| P₁∧P₂ | ±1, global | C0 |
| Weil pairing / inv convention | ±1, global | C0 |
| 𝔑⁺ orientation | ±1 per K (Atkin–Lehner) | C0, once per K |
| parity labelling at ℓ₁ | ρ_f ↦ −ε₁ρ_f = −ρ_f (ε₁ = +1), **per ℓ₁** | C0: the CM vertices are even |
| S_{ℓ₂} ≅ S′ bijection | none on the definition; ±1 in a computation | match γ (C4) |

Why the CM-even convention is well defined: all CM vertices r_{ℓ₁}(P_σ) lie in one class.
- The vertex attached to P_σ is b_σ·v₀ with b_σ ∈ B^× (B definite, disc N⁻).
- Represent σ by an ideal prime to ℓ₁. Then b_σ can be taken with nrd(b_σ) equal to that ideal's norm times
  an ℓ₁-unit, so ord_{ℓ₁} nrd(b_σ) = 0.
- Hence all v_σ are at even distance from one another in the bipartite tree quotient (BD05 §5.3, Γ_{ℓ,1}).
- The parent's D2 left this as a HEURISTIC detail; it is DERIVED here.

So, with C0, C(ℓ₁,ℓ₂) is canonical up to ONE sign common to all pairs for fixed (E, K). This answers Codex's
"Nor does it prove that all orientation choices at different raised levels amount to one common sign": the only
per-level choice is the parity labelling, and the CM vertices fix it.

## C8. Evaluating the residue of C — SECOND BLOCK (even at a single p)

Codex §1 computes C = b/(ar) from α(φ) = a·h⊗e₁^∨ and β = b·h⊗e₂ for one auxiliary h ∈ H. The ratio does not
depend on h, but computing a and b needs some explicit h (equivalently, the position of the ℓ₁-toric line and the
ℓ₂-coinvariant line of V_J measured inside one realization of E[m]).
- No geometric h exists. J₁ has purely toric reduction at ℓ₁ (BD05 Cor 5.10 and Thm 5.1), while E has good
  reduction there, so Hom(J₁, E) = 0 and no morphism induces h.
- The elements of H exist only through BD05 Thm 5.17 (per p, existence only).
- Every instantiation found in stage 2 (notes/stage2_derivation.md B4) needs an input available only after
  choosing p:
  - Galois cohomology of E[p]⊗χ over K(E[p]), degree ≥ 960 for p = 5;
  - a rational level-raised partner E₁ with an explicit E₁[p] ≅ E[p]. This exists only in rare cases, e.g.
    2541c1 at p = 5.

**→ EVALUATION_BLOCKED_AT_C8 for the residue of C (RIGID_LR's content).**

## C9. What does not need C8: the index detector (DERIVED, per p)

The index of C is insensitive to units:
- when the C4 line normalization holds, ind(C) = v_p(G_K) − v_p(R_P), with G_K := Σ_σ g₀(x′_σ) for any
  primitive mod-pⁿ eigenform g₀ on S′;
- for a detecting pair, ind(C) = v_p(G_K) — definite and normalization-free.

Codex §5 gives ind(C) = min(k, δ_sys + ½·length Ш(E/K)[p^k]) under Howard's hypotheses for the realized system.

The direction a certificate needs does not use C4's surjectivity: if G_K ≢ 0 mod p at a detecting pair, then
Ш(E/K)[p] = 0. Proof sketch, all per p and unit-insensitive:
1. Let s ∈ Sel_{F(ℓ₁ℓ₂)} be nonzero. Chebotarev gives an admissible ℓ₃ with loc_{ℓ₃}(s) ≠ 0 (BD05 Thm 3.2).
2. BD's first law at depth 3, for the Shimura curve of discriminant N⁻ℓ₁ℓ₂ℓ₃ at ℓ₃ (Čerednik–Drinfeld
   components ↔ S′), gives ∂_{ℓ₃}κ(ℓ₁ℓ₂ℓ₃) = (unit)·G_K.
3. Global reciprocity then gives ⟨∂_{ℓ₃}κ, loc_{ℓ₃}s⟩ = 0, a contradiction. So Sel_{F(ℓ₁ℓ₂)} = 0.
4. Codex §4 (invertible two-point matrix) gives Sel_{F(ℓ₁ℓ₂)} ≅ Ш(E/K)[p].

This is BD/Howard's "λ_n unit ⇒ Sel_{F(n)} = 0" step read at the bottom layer. It needs:
- per-p multiplicity one at depths 1–3 (the C3-type input);
- the bottom-layer first law at depth 3 (BD05 Thm 4.1 proof via §8, which uses no p);
- Codex's comparison.

It does not need Λ, h, or Ш = 0.

**Cost of evaluating the detector.** G_K mod p needs the Brandt module at a three-prime discriminant. Sage
supports prime discriminant only (`checks/sage_brandt_capability.txt`); the record's `brandt.py` is hard-wired
to discriminant 3. So new code is needed.
- Smallest eligible case for 389a1: p = 7, (ℓ₁,ℓ₂) = (23,31), R ≡ 2, K = Q(√−8), h ≈ 1.07·10⁴ classes.
- For the seed, S′ at discriminant 3·2243·5843·73·223 is far beyond reach. The detector cannot be evaluated for
  the seed by definite computation.

## Verdict for the construction phase

- **CONSTRUCTION_BLOCKED_AT_C3** (one integral convention over Z/m). Multiplicity one at the level-raised ideal
  is available only one p at a time (BD05 Thm 5.17 Step 1, pp. 61–62; Cor 5.18, p. 64). The rational-idempotent
  repair (C2) reaches only the base module.
- **Per p, the construction completes.** At a fixed eligible p (p ∤ J_f, GL₂ image, C3 certified at that p):
  - α (C3) and β (C4) are constructed;
  - the CM/localization compatibility is proved (C4: β = loc_{ℓ₂} κ_J);
  - orientation factors are listed, and the CM-even labelling makes C canonical up to one global sign (C7);
  - C is well defined (C6), and Ш = 0 is used nowhere.
- **EVALUATION_BLOCKED_AT_C8** for the residue of C, even at one p.
- **The index detector (C9) needs no C8 input.** Its evaluation needs new composite-discriminant Brandt code.
  Predictions for the smallest eligible case are sealed in `SEALED_PREDICTIONS_389a1_p7.md`. Evaluation not run.
- J_f computed: 389a1 → 40 (p = 5 ineligible); 2541c1 → 144 (p = 5 eligible). Seed: not computable.
