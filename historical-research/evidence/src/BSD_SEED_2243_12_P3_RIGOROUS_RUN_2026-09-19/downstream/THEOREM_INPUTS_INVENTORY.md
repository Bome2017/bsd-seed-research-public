# Inventory of inputs to the p = 3 conclusion (independent of the run's outcome)

**Sources:**
- F1 hostile audit: `~/BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F1_P3_HOSTILE_AUDIT.md`, verdict `P3_CHAIN_PASS_WITH_CORRECTIONS`;
- Lane 3 `D_primes/04_P3.md`;
- the rigorous core `~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/`.

Nothing here is re-derived. It is the list the final report must carry.

## A. PROVED mathematical inputs (exact algebra/arithmetic; no numerics)

| id | statement | source |
|---|---|---|
| M1 | Curve data: N = 2³·3·2243·4547²·5843; minimal model (u = 1); w = +1; a₃ = −1 (non-split multiplicative, I₂, c₃ = 2); ∏c_v = 16; E(Q)_tors = Z/2 | PARI (exact algorithms); re-computed by F1 (CP-E) and by the core (`certificate/hypotheses_output.txt`) |
| M2 | ε₃ = 1 − 1/α = 2 (α = a₃ = −1); #Ẽ_ns(F₃) = 4 | SW l. 499–503; F1 CP-D |
| M3 | ρ̄_{E,3} = GL₂(F₃), so irreducible and absolutely irreducible | upstream (Lane 3 `01_GATES.md` §4; AUDIT_D [3]); F1 Finding 10 / R7: not re-audited by F1 |
| M4 | rank E(Q) = 2 and E(Q)/tors = ⟨P₁,P₂⟩ (index prime to 3) | Zywina Thm 1.2 (merged); saturation at 3 certified (ℓ = 17, 53; AUDIT_D ℓ = 2027, 2087); F1 `ellsaturation` ≤ 100 |
| M5 | 2243 ∥ N with v₂₂₄₃(Δ) = 1, so ρ̄₃ is ramified at 2243 | F1 CP-E (re-computed) |
| M6 | c_E \| 2⁹: v₂(c₀) ≤ 8 (MANIN_2_PRIMARY_GATE, merged) and 4547 ∤ c₀ (Edixhoven check, merged) | merged ledger; F1 R7 (not re-audited) |
| M7 | Lattice: x_b = Re λ(b/81)/ω₁ ∈ (1/(2c_E))Z ⊆ (1/1024)Z (corrected Wuthrich 2018 Prop. 1). Sharper: (1/c_E)Z ⊆ (1/512)Z, since [1/3]⁺ = 0 | F1 CP-F. **A theorem input; the run does not prove it** |
| M8 | Depth-4 approximation: a_{4,2} ≡ a₂ (mod 27). SW Prop. 3.5 with c = 0 (all symbols [a/3^m]⁺ are 3-integral for every m, since 3 ∤ c₀); e_{3,2} = 3 | F1 CP-F (re-derived); Lane 3 §4 |
| M9 | L(E,1) = 0: rank ≥ 1 plus Gross–Zagier–Kolyvagin plus modularity. Used only by the consistency checks a_{n,0} = 0 and [1/3]⁺ = 0 | core `ANALYTIC_RANK_CERTIFICATE.md` §3 |

## B. PROVED computer-assisted inputs

| id | statement | certificate |
|---|---|---|
| C1 | ord₃ Reg_γ = 0: ord₃ Reg₃ = 2 (det ≡ 9 mod 27) for the Mazur–Tate canonical height; ord₃ log₃ 4 = 1 | F1 CP-E / Finding 2: independent exact computation (integrality characterisation, unique c ≡ 22 mod 81), agreeing with PARI's Tate-curve route to 3⁶–3⁸ |
| C2 | ord_{s=1} L(E,s) = 2, with L″(E,1)/2 ∈ [35.929604, 35.941023] | core `ANALYTIC_RANK_CERTIFICATE.md`. Not needed by the p = 3 chain itself (F1 CP-G step 2), recorded for completeness |
| C3 | **This run:** a_q for every prime q ≤ 14 847 836 159, each re-proved by the independent verifier; all 54 + 54 symbols [b/81]^± and 18 + 18 symbols [b/27]^± enclosed in Arb balls and identified in (1/1024)Z; a_{4,j} computed exactly | this directory (`P3_CERTIFICATE.md`) |

## C. Published theorems used (as printed)

1. **Skinner, Pacific J. Math. 283 (2016), Thm A.** Ch_Λ(Sel) = (L₃(E,T)) in Λ, giving both divisibilities at p = 3, 3 ∥ N, non-split. It runs through Chida–Hsieh Thm C via Skinner's erratum to SU Prop. 12.3.6 (F1 CP-A2).
2. **Greenberg–Vatsal, Invent. Math. 142 (2000), Prop. (3.1), Thm (3.2)/Prop. (3.3), Rem. (3.4).** Canonical period = Néron period up to a 3-adic unit (F1 CP-C).
3. **Stein–Wuthrich, Math. Comp. 82 (2013):**
   - Prop. 3.5 (approximation);
   - Thm 6.1 (Schneider, Perrin-Riou; Jones [Jon89] for multiplicative p): ord_T f_E ≥ r, with equality iff the height is non-degenerate and Sha(p) is finite;
   - Algorithm 11.1 step 4 (the leading-term valuation).
4. **Mazur–Tate:** the canonical σ (integral normalisation) at the multiplicative prime 3.
5. **Cassels:** on a finite Sha[3^∞] the Cassels–Tate pairing is non-degenerate and alternating. Hence Sha[3^∞] ≅ A × A.
6. **Mazur, Cor. 4.1 (via GV Thm 3.2):** c₁ is prime to p when p ∥ N.
7. **Selmer identification:** proved in F1 CP-B, citing only Shapiro's lemma (Greenberg 1989, Prop. 3.2).
8. **Modularity:** Wiles; Taylor–Wiles; BCDT.

**Not used:** Kato's divisibility (it excludes 3 ∣ N), the Manin conjecture, p-adic BSD, and any statement at p ≠ 3.

## D. Published-theorem provenance notes (carried from F1 §4; NOT closed tonight)

- **R1.** Jones 1989 (Duke 59), the multiplicative case of SW Thm 6.1: **unread** (paywalled). SW Thm 6.1 as printed covers "multiplicative type" and singles out only the split case. Supporting evidence: F1's universal-norm argument (CP-D) and exact numerical p-adic BSD on 57a1 and 681c1 (CP-D′).
- **R2.** The freeness / Gross-versus-canonical period bridge behind SU Prop. 12.3.6 at p = 3 with 3 ∥ N and N non-squarefree is literature-internal. Chida–Hsieh Prop. 6.1 assumes p > k + 1 and p ∤ N, and both fail here. Pollack–Weston 2011 (squarefree N) is unread. This is load-bearing for integrality in Λ, and there is no second source, since Kato excludes 3 ∣ N. F1's label: "PROVED, citing Skinner (2016) Thm A as printed", with this dependency recorded.
- **R3–R7** (F1 §4):
  - R3: Greenberg 1989 Prop. 3.2 is cited, not read.
  - R4: EPW Prop. 3.4.3 is internal to Skinner.
  - R5: Mazur–Tate σ at multiplicative 3 was confirmed numerically only.
  - R6: GV was read in the authors' copy.
  - R7: the upstream nodes M3, M4 and M6 were not re-audited by F1.
- **R8** (the run's floating-point certification) is **discharged by this run**. The coefficients and symbols come from the rigorous core, with Arb enclosures and independently verified a_q.

## E. Purely consistency checks (they detect errors; they prove nothing)

- a_{4,0} = a_{3,0} = a_{2,0} = 0.
- a_{4,1} ≡ 0 (mod 27).
- The SW Prop. 3.5 congruences between depths 2, 3 and 4.
- The U₃ relations 81 → 27 (an independent m = 27 run), 27 → 9 and 9 → 3.
- [1/3]⁺ = [2/3]⁺ = 0.
- The symmetries [m−b]⁺ = [b]⁺ and [m−b]⁻ = −[b]⁻.
- Even numerators over 1024 (the (1/512)Z lattice).
- The msl count identity.
- ms/msl agreement and validation on 9 curves (core).
- Byte-identical replays.
- ord₃ a_{4,2} ≠ 1 (square order).
