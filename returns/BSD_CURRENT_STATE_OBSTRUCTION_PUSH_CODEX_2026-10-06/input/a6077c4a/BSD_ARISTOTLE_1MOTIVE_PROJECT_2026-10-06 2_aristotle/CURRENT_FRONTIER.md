# BSD seed: current frontier (canonical state, 2026-10-06)

Read this file first. It replaces every earlier frontier, state or summary file in your project. Each item points to its full source inside this packet. Grades are as recorded; nothing here is human-refereed.

## 0. The curve and the endpoint

- **The curve.**
  - Model: E: y² = x³ − 22735x² + 106272484x.
  - Global minimal model: [0,−1,0,−66020924,−65074271436], via x = X + 7578 with u = 1.
  - Conductor: N = 2³·3·2243·4547²·5843.
  - Δ > 0, so Ω_E = 2ω₁. No CM.
- **Mordell–Weil group, Tamagawa numbers and Galois image.**
  - E(ℚ) = ℤP₁ ⊕ ℤP₂ ⊕ ℤ/2, with P₁ = (−3031, 327384) and P₂ = (−2394, 281520) on the minimal model. The basis is saturated.
  - The Tamagawa product is 16.
  - The mod-p image is GL₂(F_p) for every odd p.
  - Rank and analytic rank are 2.
- **The endpoint is FIN ∧ ORDER9 ∧ Q36.**
  - FIN: Ш(E/ℚ) is finite.
  - ORDER9: #Ш = 9.
  - Q36: q := L″(E,1)/(2Ω_E·Reg) = 36. Proved rigorously so far: 35.99427 < q < 36.00573.
- **The uniform step U.** Find a finite set S with Ш[p] = 0 for every p ∉ S. FIN is U plus finiteness at the primes of S.

## 1. Proved and accepted state (sources in `1_PROVED_STATE/`)

1. **Settled primes** (`SETTLED_PRIMES.md`).
   - Ш[p^∞] = 0 for p = 2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
   - Ш[3^∞] ≅ (ℤ/3)².
   - Conditionally on FIN, #Ш = 9 or #Ш ≥ 25,281.
2. **Receiver exactness** (`receiver/`; Codex-reviewed written deduction under retained inputs).
   - B_p := Hom_{Γ_p}(Cl(O_{L_p}[1/p])/p, E[p]) ≅ Ш(E/ℚ)[p] for every p ≥ 5.
   - With retained parity: dim B_p ≤ 1 ⟺ B_p = 0 ⟺ Ш[p^∞] = 0.
3. **Ota detector** (`ota/`). Source: Ota, Amer. J. Math. 140 (2018), Thm 1.5/6.4 with 5.17; the application was audited by Pro as SOUND_WITH_CORRECTIONS.
   - Admissible auxiliary ℓ: ℓ ∤ pN, p ∥ ℓ − 1, E(F_ℓ)[p] cyclic.
   - Put c₂(p,ℓ) = Σ_{a∈(ℤ/ℓ)^×} C(ind_g(a) mod p, 2)·[a/ℓ]⁺.
   - Then c₂(p,ℓ) ≢ 0 (mod p) ⇒ Ш[p^∞] = 0.
4. **G2** (`G2/`; written deduction 09-26, Codex independent source-and-proof PASS).
   - Statement: for every p ∉ S₀ = {2,3,5,2243,4547,5843} there are infinitely many ℓ ∤ pN with ℓ ≡ 1+p (mod p²), ρ̄_p(Frob_ℓ) = −I and R_{p,ℓ} ≢ 0 (mod p). So a_ℓ − 2 ≡ −4 and #E(F_ℓ) ≡ 4.
   - Mechanism: a fixed 1-motive M = [ℤ² → G₁ ×_E G₂], built from normalized Poincaré lifts over Q_j = 16P_j, with L_p = ℚ(M[p], E[p²]).
   - R_{p,ℓ} ≢ 0 ⟺ det β(Frob_ℓ) ≢ 0, where β = c − b(A−I)⁻¹a.
   - The Kummer block is full, from saturation. The central block contains Sym₂(F_p), via commutators.
   - **No Selmer or Ш input.**
5. **Theorem W** (`theorem_W/`; written deduction 09-29, Codex CONFIRMED_WITH_CORRECTIONS).
   - Statement: for p ∉ B* = {2,3,19,59,487,2243,4547,5843} and admissible ℓ, ℓ′ with R ≠ 0, s_{p,ℓ} := C₂(p,ℓ)/((a_ℓ−2)·R_{p,ℓ}) equals s_{p,ℓ′} (sign +).
   - So each such p has a scalar s_p ∈ F_p that does not depend on ℓ. The p-adic version gives s_p^∞ ∈ ℤ_p.
6. **BKS factorization** (retained imports; Codex audit 09-27, `3_LIVE_QUESTION/K288_UNIFORMITY_AUDIT_CODEX.md`).
   - When the Selmer corank is 2: s_p ≐ x_{ℚ,Σ}·#Ш[p^∞], up to a p-adic unit. Here x_{ℚ,Σ} is the coordinate of Kato's determinantal zeta element.
   - When the corank exceeds 2: s_p = 0.
   - (K), "x_{ℚ,Σ} is a p-unit", is retained at good ordinary p (Kato + Skinner–Urban). It is open at supersingular p.
7. **K288 data** (`k288_audit/`; two independent pipelines).
   - s_p ≡ 288 (mod p) at p = 17, 19, 23, 29, 31, 37, 41, 43, 47. Two sealed residues at p = 5 also match.
   - Under the stated convention the unit is u = 1. The convention: symbols Re λ/ω₁; g the least primitive root; b₁₂ = (h(Q₁+Q₂) − h₁ − h₂)/2; R = det/M⁴.
   - CRT gives exactly 288. Any other rational fitting the nine has height > 3·10⁶.
   - Conjectural reading: 288 = 32·#Ш = 8q.
8. **Twist and Heegner facts** (`twist/`).
   - E^{−23}(ℚ) has rank 1, with L′ ∈ [39.512236, 40.182321]. rank E(ℚ(√−23)) = 3.
   - ν_p ≤ 2 ⟺ Ш[p] = 0 ∧ dim Sel_p(E^{−23}) ≤ 3.
   - Where the twist side is minimal, {ν_p > 2} = Supp Ш.
9. **Lattice lemma** (Lean `TameScalar.eq_288_of_mem_lattice`). If W = 8q and W ∈ (1/D)ℤ with D ≤ 21, then W = 288 and q = 36. D = 22 fails.

## 2. Closed lanes: do not reopen (reasons and sources in `2_CLOSED_LANES/CLOSED_LANES.md`)

- **Receiver refinements.** Exactness is done; upper control gives no bound.
- **Coinvariant / norm descent.** It reconstructs the strict-at-p Selmer group, i.e. Ш[p]. No bound.
- **Heegner ν_p ≤ 2.** This restates Ш[p] = 0 on the tail.
- **Auxiliary primes, biextension fullness, `Deg`.** Solved by G2.
- **W3.** The same constant times a p-local regulator form. No fixed cross-prime object.
- **First-order cohomological operations** (cup products, Massey products, receptacles). Exhausted at first order.
- **Candidates K1–K11 for a global scalar** (Kato/BK, Fitting ideals, plectic, diagonal cycles, Eisenstein, 1-motive alone, 8q). Missing constructions, not refutations.
- **Per-prime work.** Settled primes and new per-prime runs.

## 3. The single live tame question: G1, the Ш-free Tame Law (`3_LIVE_QUESTION/`)

**Exact Law (G1).** There are a finite set S ⊇ S₀ ∪ B* and an m ∈ ℚ^×, defined without Ш, such that s_p ≡ m (mod p) for all p ∉ S.

- **G1 is sufficient.** With G2, Theorem W and Ota, G1 gives Supp Ш ⊆ S ∪ {p : p ∣ num m}, i.e. finite support.
- **The existence form is FIN restated.** In the existence form, m is fixed but each p may have its own p-unit u_p.
  - It is equivalent to FIN-tail ∧ (K) (Lean `TameLink.link_iff_fin_and_kato`).
  - The backward direction sets W = the product of the alarm primes (`DetectorRule.exists_fixed_carrier_iff_finite_alarms`).
  - (K) is already retained at ordinary p, so this form is FIN restated.
- **Zero-pattern weakenings.** No statement that depends only on which s_p vanish is both sufficient for finite support and weaker than FIN-tail (`STATUS.md` §4).
- **Residue laws** (the exact Law, bounded-unit laws, finitely many candidate constants). These are strictly stronger than FIN-tail. Each needs a characteristic-zero identity that produces the residues.
- **Sources screened for such an identity; none is sufficient:**
  - m = 8q (TAC): needs q ∈ ℚ, which is open for every rank-two curve.
  - G2's 1-motive: gives the regulator side only.
  - Rank-two Gross–Zagier: known over function fields only.
  - Tan, Ann. Inst. Fourier 45 (1995), Thms 3.12/3.14/3.16: assumes BSD over every intermediate field, and gives the constant only up to F_p^×.
  - The characteristic-zero comparison Θ_E ↔ Z ↔ M_G2: the degree-two class has no ℚ-valued realization (`ADMISSION.md`, NOT_ADMITTED).
  - OpenAI math Result 002 (exact BSD from low Selmer corank): its rank-one anchor is a tame Gross–Zagier identity for Heegner points, which reads 0 = 0 in rank two (`2_CLOSED_LANES/EXTERNAL_OPENAI_RESULT002_TRANSPLANT.md`). It is independent evidence that the missing object is a rank-two global identity.

**The question for this run.** Find a residue-level identity with a mechanism that does not use FIN, BSD or #Ш. Any rational m will do, not necessarily 288 or 8q. Alternatively, prove precisely that a specific proposed version is equivalent to FIN-tail. See `TASK.md`.

FIN, ORDER9 and Q36 are open.
