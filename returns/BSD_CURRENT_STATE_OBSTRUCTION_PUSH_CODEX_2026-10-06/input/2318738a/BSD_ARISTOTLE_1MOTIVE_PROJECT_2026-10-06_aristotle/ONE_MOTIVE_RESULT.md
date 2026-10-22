# The fixed 1-motive M_E = [ℤ² → E]: receiver, determinant line, globalization (2026-10-07)

**STATUS: ETNC_CIRCULAR**

Governing file: `DELTA_TASK_1MOTIVE.md`. Object: M_E = [Y = ℤ² →u E], u(e_i) = P_i, on the minimal model, with Y in degree −1. Lean: `RequestProject/OneMotive/Skeleton.lean` (no `sorry`; axioms are listed in §8).

Labels:
- **PROVED**: proved here, either on paper from the stated standard facts or in Lean.
- **IMPORTED**: an exact external source is given.
- **HEURISTIC**: not proved.

Primary source for step 3: D. Macias Castillo, T. Sano, arXiv 2603.23978v1, cited as [MCS]. The TeX source was read directly. Numbering below is taken from that source:
- Hypothesis 2.11: the technical hypothesis.
- Hypothesis 2.17: the core-vertex hypothesis.
- Theorem 2.20: Selmer complex ≃ Poitou–Tate complex.
- Proposition 3.3 and Theorem 3.4: det ≅ Stark systems.
- Corollary 3.5: Fitting ideals.

Its Proposition 3.3 uses [BSS II] (arXiv 1805.08448), Theorem 4.6(i).

---

## 1. Step 1: the fixed receiver Sel(ℚ, M_E)(n) ≅ Ш(E/ℚ)[n] for every odd n (PROVED)

**Conventions.**
- Triangle: E → M → Y[1] → E[1].
- Torsion realization: M[n] := H⁻¹(M ⊗ᴸ ℤ/n). Explicitly, M[n] = {(x,k) ∈ E(ℚ̄)×Y : nx = u(k)} / {(u(m), nm)}. It sits in 0 → E[n] → M[n] → Y/n → 0.
- Definitions, for every place v of ℚ including ∞:
  - Sel(ℚ,M)(n) := ker(H¹(ℚ,M[n]) → ∏_v H¹(ℚ_v,M)), i.e. the classes whose localizations lie in im(H⁰(ℚ_v,M)/n);
  - Ш¹(ℚ,M) := ker(H¹(ℚ,M) → ∏_v H¹(ℚ_v,M)).
- These are the standard definitions for Deligne 1-motives, as in Harari–Szamuely, *Arithmetic duality theorems for 1-motives*, J. reine angew. Math. 578 (2005). The attribution is IMPORTED at definition level; the proof below uses only the definitions.

**(a) H⁰ (PRE-CHECK (a) verified, PROVED).** The hypercohomology sequence for F = ℚ or ℚ_v is
0 → H⁻¹(F,M) → Y →u E(F) → H⁰(F,M) → H¹(F,Y) → H¹(F,E) → H¹(F,M) → H²(F,Y) → H²(F,E).
- H¹(F,ℤ) = Hom_cont(G_F, ℤ) = 0.
- ker u = 0 for F = ℚ (P₁, P₂ are independent), and also for F = ℚ_v, since E(ℚ) ↪ E(ℚ_v).
- Hence H⁰(F,M) = E(F)/⟨P₁,P₂⟩, and H¹(F,E) ↪ H¹(F,M) with cokernel ker(H²(F,Y) → H²(F,E)).
- Globally, H⁰(ℚ,M_E) = E(ℚ)/⟨P₁,P₂⟩ ≅ ℤ/2. The input is IMPORTED from the record: E(ℚ) = ℤP₁ ⊕ ℤP₂ ⊕ ℤ/2, saturated.
- So H⁰(ℚ,M_E)/n = 0 for every odd n (Lean `quotient_trivial_of_coprime`).
- The saturation is the only arithmetic input of step 1. If ⟨P₁,P₂⟩ had index m in E(ℚ)/tors, step 1 would fail exactly at the p dividing m.

**(b) The Selmer sequence (PRE-CHECK (b) verified, PROVED).**
- The triangle M →n M → M[n][1] gives 0 → H⁰(F,M)/n → H¹(F,M[n]) → H¹(F,M)[n] → 0, globally and locally.
- The diagram chase then gives 0 → H⁰(ℚ,M)/n → Sel(ℚ,M)(n) → Ш¹(ℚ,M)[n] → 0.
- Lean: `KummerData.i_mem_sel`, `j_mem_shaN`, `exists_sel_of_mem_shaN`, `mem_range_of_sel_of_j_eq_zero`. When H⁰/n = 0 this is the isomorphism `KummerData.selEquivSha`.

**(c) Ш¹(ℚ,M_E) ≅ Ш(E/ℚ) (PRE-CHECK (c) verified, PROVED).**
- Injectivity: H¹(ℚ,E) ↪ H¹(ℚ,M) globally, and H¹(ℚ_v,E) ↪ H¹(ℚ_v,M) at every v.
- Surjectivity: let y ∈ Ш¹(M). Its image in H²(ℚ,Y) = H¹(ℚ,ℚ/ℤ)² is a pair of finite-order characters that are trivial on every decomposition group. By Chebotarev they are trivial. So y = a(x) for some x ∈ H¹(ℚ,E), and x is locally zero by local injectivity.
- Lean: `ShaData.shaEquiv`, where `sha2_zero` encodes Ш²(ℚ,ℤ²) = 0.

**Theorem 1 (PROVED, without FIN).**
- For every odd n: Sel(ℚ,M_E)(n) ≅ Ш¹(ℚ,M_E)[n] ≅ Ш(E/ℚ)[n]. In particular Sel(ℚ,M_E)(p) ≅ Ш(E/ℚ)[p] for every odd prime p.
- For n = 2 the same argument gives 0 → ℤ/2 → Sel(ℚ,M_E)(2) → Ш[2] → 0.

**Places needing care.** None, for odd n.
- At ∞: H¹(ℝ, M[n]) = 0 for odd n.
- p = 3: nothing changes; Sel(ℚ,M_E)(3) ≅ Ш[3] ≅ (ℤ/3)² (record value, IMPORTED).
- Bad primes: the local conditions are the 1-motive's own, and the argument never uses the reduction type.

**Correction to note for step 3.** The local condition at p, im(E(ℚ_p)/(pⁿE(ℚ_p) + ⟨P₁,P₂⟩)), is finite and independent of n for n large. So rationally it is the strict condition at p: dimension 0. The Bloch–Kato condition H¹_f(ℚ_p, V_pM_E) has dimension 2 (§3.3).

**Relation to the record's receiver.**
- L_p = ℚ(E[p], p⁻¹E(ℚ)) = ℚ(M_E[p]) for odd p.
- The record gives B_p ≅ Ш[p] for p ≥ 5 (IMPORTED, `1_PROVED_STATE/receiver/`). Combined with Theorem 1 this gives B_p ≅ Sel(ℚ,M_E)(p) (PROVED as a composite of isomorphisms). That the composite is the natural restriction map to G_{L_p} is HEURISTIC; it was not checked.
- What is new:
  - M_E is fixed before p is chosen;
  - Theorem 1 holds at every odd p, including 3;
  - it needs none of the retained receiver hypotheses.
- Like the record's receiver, it is an **identification, not a bound**.

## 2. Step 2: Burns–Sakamoto–Sano and Sakamoto do not apply to T_pM_E (PROVED; recorded, not pursued)

- **Residual irreducibility fails.** M_E[p] ⊃ E[p] is a proper nonzero G_ℚ-stable submodule, with trivial quotient 𝔽_p².
- **The free-rank-one coinvariant condition fails.** G_ℚ acts trivially on the quotient ℤ_p², so T_pM_E/(τ−1)T_pM_E ↠ ℤ_p² for every τ. Such a module is never free of rank one. Lean: `coinvariants_not_free_rank_one`, over any nontrivial commutative ring.
- These are [BSS II] Hypothesis 3.2(i) and (ii), labelled `hyp1`; they are standing assumptions from its §3 onwards.

## 3. Step 3: the Macias Castillo–Sano framework on T_pM_E, checked hypothesis by hypothesis

### 3.1 Standing assumptions of [MCS] §2.1, for T = T_pM_E

| Assumption | Status for T_pM_E |
|---|---|
| p odd; K = ℚ; R = ℤ_p (a local Gorenstein order) | ✓ |
| T free of finite rank, with continuous G_{ℚ,S}-action | ✓ rank 4, S = {∞, p, 2, 3, 2243, 4547, 5843}. Kummer extensions of points are unramified at good ℓ ≠ p (standard). |
| T^{I_v} free for v ∈ S_f ∖ {p} | ✓ automatic over ℤ_p, since a saturated submodule of a free module is free |
| Greenberg data at p: 0 → T⁺ → T → T⁻ → 0 with T^± free | a choice; see §3.3 |

### 3.2 Hypothesis 2.11 (i) and (iv): hold at every odd p ∉ S (PROVED)

- **2.11(i), first half: H⁰(ℚ, A) = 0 with A = M_E[p^∞].**
  - (b) gives 0 → H⁻¹(ℚ,M)/pⁿ → H⁰(ℚ,M[pⁿ]) → H⁰(ℚ,M)[pⁿ] → 0.
  - The outer terms are 0 and (ℤ/2)[pⁿ] = 0.
  - Hence H⁰(ℚ, M_E[pⁿ]) = 0 for all n. This is exactly where H⁰(ℚ,M_E)/p = 0 enters.
- **2.11(i), second half: H⁰(ℚ, T^∨(1)) = 0.**
  - T^∨(1) = G[p^∞], where G is the Cartier dual: the extension of E by 𝔾_m² attached to P₁, P₂.
  - μ_{p^∞}(ℚ) = 0 and E(ℚ)[p] = 0, so H⁰ = 0.
- **2.11(iv): H¹_ur(ℚ_v,T) = H¹_f(ℚ_v,T) for finite v ≠ p.**
  - p ∤ Tam(E) = 16, so κ_v(P_i) ∈ H¹_f(ℚ_v,T_pE) = H¹_ur(ℚ_v,T_pE).
  - So T|_{I_v} ≅ T_pE ⊕ ℤ_p², and (H¹(I_v,T)^{Fr})_tors = (H¹(I_v,T_pE)^{Fr})_tors, because ℤ_p(−1)^{Fr} = 0.
  - The p-part of the Tamagawa factor of T is therefore that of E, a p-unit.

### 3.3 Hypothesis 2.11 (ii) and (iii): depend on the Greenberg datum at p

Write L₀ := H⁰(ℚ_p, T).
- L₀ has rank one (PROVED). It is the kernel of e_i ↦ κ_p(P_i) ∈ E(ℚ_p)⊗ℚ_p, which is one-dimensional, and both images are nonzero.
- So 2.11(ii) forces L₀ ⊂ T⁺.

**(A) The receiver's own local condition: FAILS 2.11(ii) (PROVED).**
- Suppose a datum satisfies 2.11(ii). Then H¹(ℚ_p,V⁺) → H¹(ℚ_p,V) is injective, with image of dimension ≥ rank T⁺.
- So a rationally strict condition forces T⁺ = 0, and then H⁰(ℚ_p,T⁻) = L₀ ≠ 0.
- Hence no admissible [MCS] datum reproduces the local condition of Theorem 1, at any odd p.

**(B) The ordinary datum at a good ordinary prime p with p ∤ #Ẽ(𝔽_p): Hypothesis 2.11 HOLDS (PROVED).**
- Construction:
  - For non-anomalous p, the κ_p(P_i) come from the formal group. So T/T_pÊ ≅ T_pẼ ⊕ ℤ_p², with a unique splitting because Hom_G(ℤ_p², T_pẼ) = 0.
  - Set T⁻ := T_pẼ (rank 1, unramified character ψ with ψ(Fr) = α unit root) and T⁺ := ker(T → T_pẼ). T⁺ has rank 3 and is an extension of ℤ_p² by T_pÊ.
- Checks:
  - (ii) H⁰(ℚ_p, T_pẼ) = 0.
  - (iii-a) H⁰(ℚ_p, Ẽ[p^∞]) = Ẽ(𝔽_p)[p^∞] = 0.
  - (iii-b) (T⁺)^∨(1) is an extension of (ℚ_p/ℤ_p)(ψ) by μ_{p^∞}². Both have H⁰ = 0, since α ≢ 1 mod p.
- χ(𝔉) = rank H⁰(ℝ, T*(1)) − rank T⁻ = 1 − 1 = **0**.
- The record states that the seed is non-anomalous at every good p ≥ 7.

**(C) The relaxed datum T⁺ = T: Hypothesis 2.11 holds when E(ℚ_p)[p] = 0 (PROVED); χ = 1.**
- This is the rank-one structure of Kato type.
- Any canonical element for it is an Euler-system class, chosen independently of M_E.

**Supersingular p: no datum with χ = 0 passes 2.11(ii) (PROVED, given the IMPORTED fact that V_pE|_{G_{ℚ_p}} is irreducible for good supersingular p > 2).**
- If V⁺ ⊇ V_pE, then V⁻ is a quotient of ℚ_p² and has invariants.
- If V⁺ ∩ V_pE = 0, then V⁺ is a trivial representation of dimension ≤ 1.
- Only χ = 1 (relaxed) and χ = −2 (T⁺ = L₀) survive. There are infinitely many supersingular p (Elkies, IMPORTED).

**The Bloch–Kato condition is not of Greenberg type for any filtration (PROVED).**
- If im H¹(V⁺) = H¹_f(ℚ_p,V), then V⁺ ↠ ℚ_p².
- With U = V⁺ ∩ V_pE, the image in H¹(ℚ_p,ℚ_p²) has dimension ≥ 4 − h²(U). But it must equal H¹_ur, of dimension 2.
- So h⁰(U*(1)) ≥ 2, forcing V_pE ≅ ℚ_p(1)². That contradicts the Hodge–Tate weights.
- So the BK complex of PRE-CHECK (f) is outside [MCS].
- In datum (B):
  - dim H¹_𝔉(ℚ_p,V) = 4 ⊋ dim H¹_f = 2 ⊋ dim(receiver condition) = 0;
  - the extra directions are the cyclotomic homomorphisms in both ℤ_p²-directions.

### 3.4 Hypothesis 2.17 (a core vertex with χ(𝔉) = χ(𝔉̃)): NOT VERIFIED (HEURISTIC: plausible)

- **The prime set.** [MCS] §3.1 takes 𝒫 = {q ∉ S : H¹_{/𝔉}(ℚ_q, Aₙ) ≅ ℤ/pⁿ}; the condition q ≡ 1 mod pⁿ is not imposed.
- **No prime q ≡ 1 (mod p) lies in 𝒫 (PROVED).**
  - H¹_{/f}(ℚ_q,Aₙ)[p] ≅ M_E[p](−1)^{Fr_q}.
  - When q ≡ 1 mod p, this has dimension ≥ dim coker(Fr_q − 1) ≥ 2, through the trivial quotient 𝔽_p².
  - A cyclic group has no subgroup (ℤ/p)² (Lean `not_cyclic_of_two_dim_torsion`).
- **𝒫 is nonempty (PROVED, from the IMPORTED GL₂ image).** It contains the q ≢ 1 mod p with ρ̄(Fr_q) ~ diag(q, 1) mod pⁿ.
- **What a core vertex needs.**
  - Dual Selmer classes coming from H¹(ℚ, μ_{pⁿ}²) are invisible at every q ∈ 𝒫, because Fr_q − 1 is invertible on μ.
  - For datum (B), H¹_{𝔉*} contains no such class. Only pᵃ is unramified outside p, and it violates the dual condition at p. This step is a sketch (HEURISTIC).
  - The remaining classes need a Chebotarev argument for the reducible module Aₙ. The available core-vertex criteria (Mazur–Rubin; [BSS II] §3, Hypothesis 3.2) assume irreducibility and τ, so they do not apply. [MCS] proves Hypothesis 2.17 only in its Heegner setting (Lemma 3.8, which uses ρ̄ surjective).
- **Effect of Hypothesis 2.17.** Theorems 2.20 and 3.4 for T_pM_E remain conditional on it. Steps 4–6 below use only the Selmer complex itself, which is perfect by [MCS] Prop. 2.4 = Nekovář; they do not use Hypothesis 2.17.

### 3.5 The Cartier dual and G2's 𝓜

- **Cartier dual T' = T_pG.**
  - The dual datum T'⁺ = (T⁻)*(1) satisfies Hypothesis 2.11 exactly when (B) does, with χ = 0 (PROVED).
  - Nekovář duality gives RΓ̃(T') ≅ RHom(RΓ̃(T), ℤ_p)[−3] (IMPORTED: Nekovář, Selmer Complexes, Astérisque 310, §6.3 / Prop. 9.7.2 as used in [MCS] Lemma 2.14). So it has the dual line and the same Euler characteristic. **It does no better.**
  - The Panchishkin datum T'⁺ = preimage of T_pÊ (χ = 2) **fails 2.11(iii-b)** (PROVED). H⁰(ℚ_p,(T'⁺)^∨(1)) contains the kernel of (ℚ_p/ℤ_p)² → H¹(ℚ_p,(ℚ_p/ℤ_p)(ψ)), whose target has corank 1.
- **G2's 𝓜 = [ℤ² → G₁×_E G₂] (rank 6).**
  - 2.11(i) holds (PROVED, by the same H⁻¹/H⁰ computation: G(ℚ) ↠ E(ℚ) by Hilbert 90, and μ_{pⁿ}(ℚ) = 0).
  - The ordinary/Panchishkin datum **fails 2.11(ii)** (PROVED). T⁻ ≅ T_pẼ ⊕ ℤ_p², split because the κ_p(Q_i) are formal-group classes, so H⁰(ℚ_p,T⁻) ⊇ ℤ_p².
  - Other data were not classified.
  - The added torus factors contribute det RΓ̃(ℤ_p(1))², i.e. Kummer theory of ℚ with p-adic logarithms (HEURISTIC). The tame fibres of 𝓜 return s_p (G2, Theorem W), i.e. G1.

**Step-3 verdict.**
- [MCS] does not apply to the receiver's local condition (first failure: Hyp. 2.11(ii)).
- It applies to T_pM_E with the ordinary datum at good ordinary non-anomalous p, as far as Hyp. 2.11. Hyp. 2.17 remains open.
- It never applies in rank 0 at supersingular p.

So HYPOTHESES_FAIL is **not** the correct status.

## 4. Step 4: the determinant line (datum (B), good ordinary p ≥ 7, p ∉ S)

- **Multiplicativity (PRE-CHECK (f), first bullet: verified, with a correction; PROVED given Nekovář's exactness of Selmer complexes in compatible exact sequences, IMPORTED).**
  - T_pE ∩ T⁺ = T_pÊ is the ordinary datum of E, and the quotient ℤ_p² inherits (ℤ_p²)⁺ = ℤ_p², i.e. the **relaxed** condition at p.
  - Hence det RΓ̃(T_pM_E) ≅ det RΓ̃(T_pE) ⊗ det RΓ̃(ℤ_p)^{⊗2}.
- **The trivial pieces (PROVED).** For ℤ_p, relaxed at p and unramified elsewhere:
  - H̃⁰ = ℤ_p;
  - H̃¹ = Hom(Γ_cyc, ℤ_p) = ℤ_p φ₀;
  - H̃² = 0, by duality: elements of p^ℤ⊗ℚ_p/ℤ_p that are strict at p;
  - H̃³ = 0.
  - Its line is trivialized by (1, φ₀), canonically up to ℤ_p^×.
- **Cohomology of T_pM_E.**
  - By [MCS] Lemma 2.15 (needs only 2.11(i)): H̃⁰ = H̃³ = 0 and H̃¹ is free. Euler characteristic 0.
  - Exact sequence:
    0 → ℤ_p² →δ₀ H̃¹(T_pE) → H̃¹(T_pM_E) → ℤ_p² →δ₁ H̃²(T_pE) → H̃²(T_pM_E) → 0.
- **The connecting maps.**
  - δ₀(e_i) = κ(P_i). H̃¹(T_pE) = Sel(T_pE) is an extension of T_pШ by E(ℚ)⊗ℤ_p ([MCS] Lemma 2.14). By saturation, δ₀ is an isomorphism onto E(ℚ)⊗ℤ_p. This is where H⁰(M_E)/p = 0 is used a second time.
  - δ₁(φ₀⊗e_i) = h_p(P_i, ·) ∈ H̃²(T_pE) ≅ Sel_{p^∞}(E/ℚ)^∨. This is the Bockstein/cyclotomic height (IMPORTED: Nekovář, Ch. 11). Its identification with this connecting map is standard but was not re-derived (HEURISTIC at that level).
- **Result (PROVED modulo the δ₁ identification).**
  - H̃¹(V_pM_E) ≅ V_pШ ⊕ ker H_p, where H_p = (h_p(P_i,P_j)) is the normalized cyclotomic p-adic height matrix.
  - RΓ̃(V_pM_E) is acyclic ⟺ Ш[p^∞] is finite **and** det H_p ≠ 0 (Schneider's nondegeneracy, open).
  - In that case:
    \[ \#\widetilde H^2(T_pM_E)=\#Ш(E/ℚ)[p^\infty]\cdot p^{v_p(\det H_p)}. \]
- **The Bloch–Kato version (PROVED).** H¹_f(ℚ, V_pM_E) ≅ V_pШ (PRE-CHECK (f), second bullet). It uses exactness of the crystalline f-sequences and H¹_f(ℚ, ℚ_p) = 0. This complex is not of [MCS] type (§3.3).
- **Correction to PRE-CHECK (f), third bullet.**
  - The special value attached to the [MCS] line is the p-adic one: the leading term of the cyclotomic L_p(E,s) at s = 1, expected ≐ (1−1/α)²·#Ш·Tam·det H_p / #tors² (Mazur–Tate–Teitelbaum / Schneider; conjectural).
  - It is not L*(E,1)/(Ω·Reg). The quotient q enters only after the p-adic regulator is divided out and p-adic BSD and BSD are both invoked.

## 5. Step 5: is there a canonical element from M_E itself?

- **What the 1-motive supplies (PROVED).** It supplies:
  - the isomorphism of lines in §4, which is not an element;
  - when RΓ̃(V_pM_E) is acyclic, the acyclicity trivialization ϑ_p. The element ζ_p^M := ϑ_p⁻¹(1) has index #Ш[p^∞]·p^{v_p(det H_p)} in det⁻¹RΓ̃(T_pM_E).
- **Nothing else.** P₁ and P₂ are used up as the extension data. Under Hyp. 2.17 and [MCS] Theorem 3.4 / Corollary 3.5, the Stark-system ideals of a basis are the Fitting ideals of H¹_{𝔉*}(Aₙ*(1))^∨, which contain Ш[p^∞]. This is the tautological case of PRE-CHECK (g).
- **Comparison with s_p.**
  - s_p ≐ x_{ℚ,Σ}·#Ш[p^∞] (record, BKS; IMPORTED).
  - v_p(index ζ_p^M) = v_p(#Ш[p^∞]) + v_p(det H_p).
  - The common factor is #Ш[p^∞]. The cofactors differ: the cyclotomic (wild) p-adic regulator against the Kato coordinate. In s_p the tame regulator is divided out.
  - Any identity between the cofactors would be a p-adic BSD / Perrin-Riou type statement (HEURISTIC; not available).
- **Existence.** ζ_p^M exists only at good ordinary p, and only under p-local finiteness of Ш and Schneider nondegeneracy. So canonical elements are not available "for each p" unconditionally, and **P_ADIC_ONLY is not claimed.**

## 6. Step 6: globalization; stop condition met

- **What a global index requires (PROVED, Lean `global_index_forces_finite`).** Suppose some A_M ≠ 0 satisfies p | index(ζ_p^M) ⟺ p | A_M for p outside a finite set. Then:
  - Ш[p] = 0 for almost all p: FIN-tail;
  - p ∤ det H_p for almost all p.
- The second condition is open. Heuristically it fails for infinitely many p, since Σ 1/p diverges (HEURISTIC).
- So the Euler-characteristic elements do not globalize as they stand.
- **The only way to define A_M without #Ш** is an independent normalization of a basis of each line: the p-adic L-function / Kato–Perrin-Riou zeta element.
- Matching those across p with one rational number is p-adic BSD with a p-independent value, together with BSD. This is the leading-term (ETNC) normalization of h¹(E)(1), equivalently of M_E, and q enters through it.
- Removing the p-adic regulator instead and passing to the tame scalar gives s_p, i.e. G1 / TAC.
- The stop condition of the delta task is met. **STATUS: ETNC_CIRCULAR.**

## 7. Claim ledger

| # | Claim | Label |
|---|---|---|
| 1 | Sel(ℚ,M_E)(n) ≅ Ш(E/ℚ)[n] for every odd n; for n = 2, an extension by ℤ/2 | PROVED (inputs: saturation, IMPORTED from the record; Chebotarev) |
| 2 | PRE-CHECK (a)–(c) correct as stated. The local condition at p is rationally strict, not BK | PROVED |
| 3 | BSS / Sakamoto fail on T_pM_E (irreducibility; τ-coinvariants) | PROVED (Lean) |
| 4 | [MCS] Hyp. 2.11(i), (iv) hold for T_pM_E at every odd p ∉ S | PROVED |
| 5 | The receiver's local condition fails [MCS] Hyp. 2.11(ii) | PROVED |
| 6 | The ordinary datum satisfies Hyp. 2.11 at good ordinary non-anomalous p, with χ = 0 | PROVED |
| 7 | Supersingular p: no χ = 0 datum satisfies 2.11(ii) | PROVED (local irreducibility IMPORTED) |
| 8 | The BK condition for V_pM_E is not of Greenberg type | PROVED |
| 9 | Stark-system primes for M_E[pⁿ] satisfy q ≢ 1 mod p; 𝒫 ≠ ∅ | PROVED (Lean for the group lemma) |
| 10 | Hyp. 2.17 (core vertex) for T_pM_E | HEURISTIC (open) |
| 11 | Cartier dual: same line up to duality; Panchishkin datum fails 2.11(iii) | PROVED / duality IMPORTED |
| 12 | 𝓜: ordinary datum fails 2.11(ii) | PROVED |
| 13 | det-line multiplicativity; H̃* of T_pM_E; acyclicity ⟺ Ш[p^∞] finite ∧ det H_p ≠ 0; #H̃² formula | PROVED modulo δ₁ = height (IMPORTED / HEURISTIC) |
| 14 | H¹_f(ℚ,V_pM_E) ≅ V_pШ (BK) | PROVED |
| 15 | The canonical element is the acyclicity trivialization: tautological plus the p-adic regulator; ≠ s_p in general | PROVED (structure) / HEURISTIC (comparison) |
| 16 | A global index forces FIN-tail and p-unit p-adic regulators almost everywhere | PROVED (Lean) |
| 17 | The only non-tautological globalization is the zeta / leading-term normalization | HEURISTIC (structural), giving STATUS ETNC_CIRCULAR |

## 8. Lean (`RequestProject/OneMotive/Skeleton.lean`, builds with no `sorry`)

`#print axioms`, for every new theorem and definition: each depends on exactly `[propext, Classical.choice, Quot.sound]`.

- `OneMotive.KummerData.selEquivSha`, `selEquivSha_apply`, `i_mem_sel`, `j_mem_shaN`, `exists_sel_of_mem_shaN`, `mem_range_of_sel_of_j_eq_zero`
- `OneMotive.quotient_trivial_of_coprime`
- `OneMotive.ShaData.shaEquiv`, `shaEquiv_apply`, `exists_shaE_of_mem_shaM`
- `OneMotive.coinvariants_not_free_rank_one`
- `OneMotive.not_cyclic_of_two_dim_torsion`
- `OneMotive.global_index_forces_finite`

The arithmetic inputs (the hypercohomology sequences, local injectivity, Ш²(ℤ²) = 0, H⁰ ≅ ℤ/2) appear as named hypotheses or structure fields.

FIN, ORDER9 and Q36: unchanged.
