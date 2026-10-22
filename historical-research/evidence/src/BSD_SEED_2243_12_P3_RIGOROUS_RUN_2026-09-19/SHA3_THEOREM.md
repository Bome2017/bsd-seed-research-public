# SHA3_THEOREM: the 3-primary part of Sha for the seed (2243, 12)

**Curve.** E : y² = x³ − 22735x² + 106272484x, with N = 2³·3·2243·4547²·5843.

## Theorem

> **Sha(E/Q)[3^∞] ≅ (Z/3Z)².** In particular Sha(E/Q)[3^∞] is finite and #Sha(E/Q)[3^∞] = 9.

**Label.** PROVED (computer-assisted), relative to the published theorems in §2, cited as printed. Two published-theorem provenance notes, R1 and R2 (§4), are carried as recorded by the F1 hostile audit and are **not** closed here. This is F1's recommended label: "PROVED, citing Skinner (2016) Thm A as printed", with R1/R2 recorded.

**Corollary.** Together with Sha(E/Q)[2^∞] = 0 (Zywina, merged) and Sha(E/Q)[5^∞] = 0 (`SMALL_SEED_2243_12_SHA5 = PROVED_ZERO` in `~/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md`, via the derived v₂(c₀) ≤ 8 lemma):

> **#Sha(E/Q)[30^∞] = 9**

This equals the certified numerical Sha_an = 9 (Lane 3).

*Provenance of the p = 5 input, stated as recorded and not re-audited here.*
- The master certificate's numeric node N7 (the 20 symbols [b/25]⁺) is labelled **CERT-NUM**. It was computed by the pre-rigorous LP5 double-precision stream: its truncation errors are certified, its arithmetic follows a floating-point model.
- The p = 3 result above does **not** carry that qualifier; its enclosures are Arb balls.
- A rigorous p = 5 re-run with this core (m = 25, T_min = 7 825 119 335 at 1/1024) was not part of tonight's authorization.

**Not claimed:**
- that Sha(E/Q) is finite;
- anything at primes p ∉ {2, 3, 5};
- the full BSD formula;
- the rationality of L″(E,1)/(Ω·Reg) (SRAT).

## 1. Proof

Notation follows F1 CP-G and SW §§3, 6.

1. **Computation (this run, CERTIFIED; `P3_CERTIFICATE.md`).**
   - Every x_b = Re λ(b/81)/ω₁ (b ∈ (Z/81)^×) is enclosed rigorously and identified in (1/1024)Z.
   - With μ(b + 81Z₃) = α⁻⁴[b/81]⁺ and α = a₃ = −1, the depth-4 coefficient is a_{4,2} = 15480 = 2³·3²·5·43.
   - Hence **a_{4,2} ≡ 9 (mod 27)** and ord₃ a_{4,2} = 2.
   - The SW (Néron-period) normalisation differs by the 3-adic unit 2 (7740 ≡ 18 mod 27); the valuation is the same.
2. **Depth-4 approximation** (SW Prop. 3.5 with c = 0; F1 CP-F; e_{3,2} = 3): a₂ ≡ a_{4,2} (mod 27), where L₃(E,T) = Σ aᵢTⁱ. So a₂ ≡ 9u (mod 27) with u ≢ 0 (mod 3). Hence **a₂ ≠ 0 and ord₃ a₂ = 2**.
   - c = 0 needs every symbol [a/3^m]⁺ to be 3-integral for every m ≥ 4. This holds because each b/3^m is Γ₀(N)-equivalent to the single rational cusp 1/3 and 3 ∤ c₀ (Mazur; GV Thm 3.2); see F1 CP-F.
3. **Main conjecture at p = 3** (Skinner 2016 Thm A with the F1-checked identifications):
   - Ch_Λ(Sel₃(E/Q_∞)^∨) = (L₃(E,T)) in Z₃[[T]], with both divisibilities.
   - The Selmer groups are equal (F1 CP-B), and the periods agree up to a 3-adic unit (GV Prop. 3.1, 3.3, Rem. 3.4; F1 CP-C).
   - So ord_T f_E = ord_T L₃(E,T), and f_E and L₃ have leading coefficients of the same 3-adic valuation.
4. **SW Thm 6.1** (Schneider, Perrin-Riou; Jones for multiplicative p): ord_T f_E ≥ r = 2.
   - Since a₂ ≠ 0, **ord_T f_E = 2 = rank E(Q)**.
   - The equality clause of Thm 6.1 then gives: **Sha(E/Q)[3^∞] is finite** and the 3-adic height is non-degenerate.
   - The rank is 2 by Zywina Thm 1.2 (merged), and E(Q)/tors = ⟨P₁,P₂⟩ with index prime to 3.
5. **Leading term** (SW Thm 6.1 / Algorithm 11.1 step 4, non-split line):

       ord₃ a₂ = ord₃ ε₃ + Σ_v ord₃ c_v + ord₃ #Sha(E/Q)[3^∞] + ord₃ Reg_γ − 2·ord₃ #E(Q)[3^∞]

   Here ε₃ = 2, ∏c_v = 16, Reg_γ is a 3-unit (ord₃ Reg₃ = 2 and ord₃ log₃ 4 = 1), and #E(Q)_tors = 2. Hence **#Sha(E/Q)[3^∞] = 3² = 9**.
   - This is an equality: both divisibilities come from Skinner Thm A.
6. **Cassels–Tate.** On the finite group Sha(E/Q)[3^∞] the Cassels–Tate pairing is non-degenerate and alternating. So Sha[3^∞] ≅ A × A with #A = 3, i.e. **(Z/3Z)²**. Z/9 is impossible, since an alternating form on a cyclic group is zero. ∎

## 2. Inputs, by kind

### PROVED mathematical inputs (exact computation or proof; details in `downstream/THEOREM_INPUTS_INVENTORY.md` §A)

- **M1.** N; the minimal model (u = 1); w = +1; a₃ = −1, type I₂, c₃ = 2; ∏c_v = 16; E(Q)_tors = Z/2.
- **M2.** ε₃ = 2.
- **M3.** ρ̄₃ = GL₂(F₃) (upstream; F1 R7).
- **M4.** rank 2 with generators P₁, P₂, saturated at 3 (Zywina, merged; the saturation certificates).
- **M5.** v₂₂₄₃(Δ) = 1, so ρ̄₃ is ramified at 2243.
- **M6.** c_E ∣ 2⁹ (v₂(c₀) ≤ 8 and 4547 ∤ c₀; merged). This gives **M7**, the identification lattice (1/1024)Z (corrected Wuthrich Prop. 1; F1 CP-F).
  - The lattice is a theorem input; the computation cannot detect a stray 4547 in the denominator (F1 Finding 8).
- **M8.** a_{4,2} ≡ a₂ (mod 27) (SW Prop. 3.5, c = 0; F1 CP-F).

### PROVED computer-assisted inputs

- **C1.** ord₃ Reg_γ = 0: an exact integrality-characterised Mazur–Tate height, independent of PARI's Tate-curve path, agreeing with it to 3⁶–3⁸ (F1 CP-E, Finding 2).
- **C2** (not needed by the chain; recorded). ord_{s=1} L(E,s) = 2, with L″(E,1)/2 ∈ [35.929604, 35.941023] (core certificate).
- **C3.** **This run** (`P3_CERTIFICATE.md`):
  - 663 685 727 a_q, each verified independently (root `5f9994d9…`);
  - 72 + 72 symbols in Arb balls, all identified;
  - a_{4,2} = 15480.

### Published theorems (as printed)

- Skinner, Pacific J. Math. 283 (2016), Thm A (via Chida–Hsieh Thm C, Skinner's erratum to SU Prop. 12.3.6).
- Greenberg–Vatsal, Invent. Math. 142 (2000), Prop. 3.1, Thm 3.2 / Prop. 3.3, Rem. 3.4.
- Stein–Wuthrich, Math. Comp. 82 (2013), Prop. 3.5, Thm 6.1, Algorithm 11.1.
- Mazur–Tate (canonical σ).
- Mazur (c₁ at p ∥ N).
- Cassels (Cassels–Tate pairing).
- Shapiro's lemma (Greenberg 1989, Prop. 3.2).
- Modularity (Wiles; Taylor–Wiles; BCDT).

**Not used:** Kato's divisibility (it does not cover 3 ∣ N), the Manin conjecture, p-adic BSD.

### Purely consistency checks (they detect errors; they prove nothing)

- a_{n,0} = 0 (n = 2, 3, 4).
- a_{4,1} ≡ 0 (mod 27).
- SW Prop. 3.5 congruences between depths.
- U₃: 81 → 27 (36 exact identities against the independent m = 27 run), 27 → 9 → 3.
- [1/3]⁺ = [2/3]⁺ = 0.
- Symmetries.
- (1/512)Z (all 144 values are integers).
- Count identities.
- PARI `primepi` = the verifier's prime count.
- Byte-identical replays (`P3_REPLAY.md`).
- Three independent evaluations of a_{4,2}.

## 3. What the run itself certifies, and what it does not

**The run certifies:** the exact values of the 144 symbols **given** the lattice input M7, and the arithmetic leading to a_{4,2} = 15480.

**The run does not certify:**
- the lattice (M6/M7);
- the theorem chain (§1, steps 2–6);
- the upstream nodes M3, M4, M6.

## 4. Provenance notes carried from F1 (§4 of the audit; not closed)

- **R1.** Jones 1989 (Duke 59), the multiplicative case of SW Thm 6.1, is **unread** (paywalled).
  - SW Thm 6.1 as printed covers "multiplicative type" and singles out only the split case.
  - Supporting evidence (not a replacement): F1's universal-norm argument (CP-D) and exact numerical p-adic BSD on 57a1 and 681c1 (CP-D′).
- **R2.** The freeness / Gross-versus-canonical period bridge behind SU Prop. 12.3.6 at p = 3 with 3 ∥ N and N non-squarefree is literature-internal.
  - Chida–Hsieh Prop. 6.1 needs p > k + 1 and p ∤ N, and both fail here.
  - Pollack–Weston 2011 (squarefree N) is unread.
  - It is load-bearing for integrality in Λ, and there is no second source, since Kato excludes 3 ∣ N.
- **Other notes:**
  - R3: Greenberg 1989 Prop. 3.2 is cited, not read.
  - R4: EPW Prop. 3.4.3 is internal to Skinner.
  - R5: the Mazur–Tate σ at multiplicative 3 was confirmed numerically only.
  - R6: GV was read in the authors' copy.
  - R7: upstream nodes were not re-audited by F1.
  - **R8** (the run's floating-point certification) is **discharged**: the load-bearing computation is the rigorous Arb pipeline with independently verified coefficients.

Nothing is merged. This file does not edit the master ledger.
