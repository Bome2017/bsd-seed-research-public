# P3_THEOREM_GATE: which published theorem turns the p = 3 computation into a theorem about Sha(E/Q)[3^∞]? (2026-09-19)

## Verdict: `P3_THEOREM_CHAIN_VALID`

The published chain checks out.
- Every printed hypothesis holds on the seed. I checked each one against the source text myself, independently of lanes C and D.
- Lane 3's open identifications (1)–(3) are discharged: (2) and (3) at the source, (1) by a standard comparison.
- Lane 3's open item O-4, the regulator normalization at the non-split prime 3, is closed at the level used, the 3-adic valuation (§4).

What remains is provenance only (§5). No hypothesis is unverified, and nothing mathematical is assumed.

The seed: E: y² = x³ − 22735x² + 106272484x, N = 2³·3·2243·4547²·5843. Its reduction at 3 is **non-split multiplicative** (I₂; a₃ = −1).

## 1. The chain, with source lines

The text extractions are in `p3src/` here (sha256 of the PDFs below).

| # | statement | exact source | read here? |
|---|---|---|---|
| T1 | **Skinner Theorem A.** p ≥ 3; f ∈ S_k(Γ₀(N)) a newform, ordinary at p; (i) k ≡ 2 (mod p−1); (ii) ρ̄_f irreducible; (iii) some q ≠ p with q ∥ N and ρ̄_f ramified at q. Then Ch_L(f) = (L_f) **in Λ_O**, which is the full Iwasawa–Greenberg main conjecture. It explicitly covers p ∣ N; Kato 17.4 does not. | Skinner, arXiv:1407.1093v1, p. 1–2, `Skinner_1407.1093.txt` l. 43–57 (PDF sha256 `02d176d8…`) | **yes** |
| T2 | **Skinner's Selmer group.** Sel_{Q∞,L}(f) is defined à la Greenberg: at p, the image in H¹(I_p, M⁻)^{G_{Q_p}} must vanish; at ℓ ∈ S∖Σ the class must be unramified. By his Lemma 2.1.1 it is independent of the lattice T_f when ρ̄_f is irreducible. | same, §2.3, l. 386–410 | **yes** |
| T3 | **Periods.** If ord_p N ≤ 1 and E[p] is irreducible, then Ω_E = ∫_{c⁺} ω_E is a Z₍p₎^×-multiple of −2πiΩ_f^+. The argument: the X₁(N)-optimal curve has φ*ω = c·2πi f dz with p ∤ c (Greenberg–Vatsal Prop. (3.3)), plus an isogeny to E of degree prime to p. | same, §3.3 (proof of Thm C), l. 1339–1370 and footnote 8 | **yes** (G–V itself not read) |
| T4 | **SW Theorem 6.1** (Schneider, Perrin-Riou, Jones), for good ordinary or multiplicative p. ord_T f_E ≥ r, with equality iff the p-adic height is nondegenerate **and** Sha(E/Q)(p) is finite. In that case the leading term of f_E has the valuation of ε_p·∏c_v·#Sha(p)·Reg_γ/(#E(Q)(p))². | Stein–Wuthrich 2013, `~/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt` l. 1066–1088 | **yes** (Jones 1989 not read) |
| T5 | **The non-split case.** In all the theorems involved, the non-split case never differs from the good ordinary case. ε_p = 2 for non-split multiplicative p. | same, l. 1300–1302; ε_p definition l. 499–503 | **yes** |
| T6 | **Greenberg vs classical Selmer over Q∞.** For good ordinary E, the usual Selmer group over Q∞ equals Sel_{Q∞}(T_pE, T_p⁺E) = Sel_{Q∞,Q_p}(f). | Skinner–Urban, `SkinnerUrban_MC.txt` §3.6.7, l. 2496–2508 (PDF sha256 `f9faa40a…`) | **yes**, good ordinary case only; see §3(1) |

## 2. Hypotheses on the seed at p = 3

| hypothesis | value | basis |
|---|---|---|
| p ≥ 3 | p = 3 | — |
| ordinary at p, k = 2 | a₃ = −1, a unit; non-split multiplicative; k = 2 ≡ 2 (mod 2) | PARI `ellap`; Kodaira code 6 = I₂ (`runs/p3_reg_robust_output.txt`) |
| ρ̄₃ irreducible | ρ̄₃ = GL₂(F₃); in fact ρ₃ = GL₂(Z₃) | merged ALL_ODD_RESIDUAL_IMAGE_VERIFIED; Lane 3 S3 (derived, re-derived by two audits) |
| some q ≠ 3, q ∥ N, with ρ̄₃ ramified at q | q = 2243: v₂₂₄₃(N) = 1 and v₂₂₄₃(Δ) = 1, 3 ∤ 1, so ramified (Tate curve) | N0 of the master certificate |
| ord₃ N ≤ 1 (needed for T3) | ord₃ N = 1 | N0 |
| an isogeny to E of degree prime to 3 (T3) | the class has exactly 2 curves, joined by a 2-isogeny | `ellisomat` [1,2;2,1] (Lane 4, lens A); local4547 |
| ε₃, ∏c_v, #E(Q)(3) are 3-units | ε₃ = 2, ∏c = 16, #E(Q)_tors = 2 | SW l. 499–503; Lane 3 B |
| symbols 3-integral, so c = 0 in SW Prop. 3.5 | [b/81]⁺ ∈ (1/(2c_E))Z ⊆ (1/1024)Z, with c_E ∣ 2c₀ ∣ 2⁹ | corrected Wuthrich Prop. 1 at unitary cusps; the merged v₂(c₀) ≤ 8 lemma; 4547 ∤ c₀ |

## 3. Status of Lane 3's identifications (1)–(3)

1. **Greenberg Selmer = classical Selmer over Q∞ at the multiplicative prime 3.** Only characteristic ideals are needed, and a finite discrepancy does not change them.
   - **At ℓ ≠ 3 the conditions agree exactly.** Q_{∞,η} contains the unramified Z₃-extension of Q_ℓ. So "unramified" coincides with "zero", since the pro-prime-to-3 quotient has no 3-primary cohomology.
   - **At 3 they agree too.** The unramified defect of Greenberg's condition is H¹_ur(Q_{∞,3}, Q₃/Z₃(ψ)) = (Q₃/Z₃)/(ψ(Frob) − 1), where ψ is the non-split unramified quadratic character. This quotient is 0, because ψ(Frob) − 1 = −2 is a 3-adic unit.
   - SU §3.6.7 states the good-ordinary analogue. Greenberg's general comparison (LNM 1716 §2) was not read.
   - **Status: discharged; provenance note only.**
2. **L_f = L₃(E,T) up to a unit of Λ.** T3 gives Ω_E ∈ Z₍₃₎^×·(−2πiΩ_f^+), with Ω_E = ∫_{c⁺}ω_E = ω₁. That is exactly the period used to normalize our x_b = Re λ(r)/ω₁. The X₀ Manin constant plays no part in this identification; it only enters the numerical lattice. **Status: discharged at the source.**
3. **T_f = T₃E.** When ρ̄₃ is irreducible, every stable lattice is homothetic to T₃E, and T2 (Skinner's Lemma 2.1.1) makes Sel and Ch lattice-independent. **Status: discharged at the source.**

## 4. The one computed input: ord₃ Reg_γ = 0. It is robust (new here; `runs/p3_reg_robust.gp` and its output, a few CPU-s)

- **Model.** The computation uses the minimal model, reached by a u = 1 change of variables from the seed model, so PARI's model-translation defect vanishes.
- **Scalar pairing entries**, from 1×1 regulators: ord₃ [h₁₁, h₁₂, h₂₂] = [1, 1, 1]. ord₃ Reg₃ = 2, and it agrees with det(h) to O(3¹⁸).
- **3-adic logs** of 8Pᵢ ∈ E₁(Q₃), divided by 8: ord₃ [log P₁, log P₂] = [1, 2].
- **Rank-one update lemma** (the argument of ADDENDUM_001, now at p = 3).
  - Change the σ/E₂ normalization by any c ∈ Z₃. Then det H moves by c·(l₁²h₂₂ − 2l₁l₂h₁₂ + l₂²h₁₁).
  - The three terms have ord ≥ 3, 4 and 5 respectively, all greater than 2.
  - So **ord₃ Reg₃ = 2 in every 3-integral normalization**. Since ord₃ log₃ 4 = 1, **ord₃ Reg_γ = 0**.
- **What is still assumed.** PARI's Tate-curve height (`ellpadics2_tate`) differs from Schneider's canonical height by at most such a c, times a 3-unit. The coordinator's 13-curve calibration (Lane 3 §10 C7) excludes a 3-power offset at the valuation level. A second implementation at a multiplicative prime does not exist locally.

## 5. Residual items (provenance, not hypotheses)

| # | item | risk | cheapest discharge |
|---|---|---|---|
| P1 | Only Skinner arXiv v1 was read; the published version (Pacific J. Math. 283 (2016)) was not | low. v1 is the refereed argument's preprint; the theorem's hypotheses match SW/SU usage | read the published Thm A text (library or journal) |
| P2 | Greenberg LNM 1716 §2 (the multiplicative Selmer comparison) was not read | low. §3(1) gives a self-contained reason at 3 | read §2 |
| P3 | Greenberg–Vatsal Prop. (3.1)/(3.3) (used inside T3) was not read | low. Skinner cites it for exactly this case | read G–V §3 |
| P4 | Jones 1989 (the multiplicative case of T4) was not read. SW's T5 sentence carries no citation for the non-split bookkeeping | low. Only valuations enter; ε₃, c₃ and Ẽ_ns(F₃) (order 4) are 3-units | read Jones 1989 |
| P5 | PARI's Tate-path height is correct up to 3-integral normalization | low. Robust by §4; calibrated on 13 curves | an independent Tate-parametrization height, or Magma |

## 6. EXACTLY what a successful p = 3 run proves

**The run.** Stein–Wuthrich + Wuthrich streaming of the unitary symbols [b/81]⁺ (width N/3; W_{N/3}; sign −w·a₃ = +1), certified as the p = 5 run was (node N7):
- certified truncation with T ≈ 1.73·10¹⁰, error ≤ 2.5·10⁻⁶;
- lattice (1/1024)Z;
- all theorem-forced checks pass: a_{4,0} = 0 exactly, a_{4,1} ≡ 0 (mod 27), the Hecke relations at depths 2–5, lattice membership, and T₁ and T₂ giving identical vectors;
- the result is a_{4,2} ≡ a₂ (mod 27) with **ord₃ a_{4,2} = 2**.

**THEOREM** (modulo §5 provenance and the run's certification): for the seed E,
1. **Sha(E/Q)[3^∞] is finite, of order exactly 9, and ≅ (Z/3)².**
   - #Sha[3^∞] = 3^{ord₃ a₂ − ord₃ Reg_γ} = 3², using T1, T2, T4 and T5, with ε₃, ∏c and torsion all 3-units.
   - Z/9 is excluded because the Cassels–Tate pairing on a finite Sha[3^∞] is alternating and nondegenerate.
2. ord_T L₃(E,T) = 2 = rank E(Q). This is the 3-adic analytic rank.
3. The 3-adic height pairing on E(Q) is nondegenerate. It is already computed nonzero; T4 now also forces it.
4. f_E = L₃(E,T)·(unit of Λ), which is the main conjecture at 3 (T1). The 3-part of the 3-adic BSD formula holds up to 3-adic units.
5. Together with the proved Sha[2^∞] = Sha[5^∞] = 0: **#Sha(E/Q)[30^∞] = 9**, matching Sha_an = 9 (NUMERIC).

**Other outcomes** (Lane 3's rules, unchanged; each is decisive under the chain):

| result | meaning under the chain | action |
|---|---|---|
| ord₃ a_{4,2} = 0 | Sha[3^∞] = 0 | contradicts Sha_an = 9: stop and audit |
| ord₃ a_{4,2} = 1 | impossible (square order) | stop and audit |
| a_{4,2} ≡ 0 (mod 27) | #Sha[3^∞] ≥ 81, or Sha[3^∞] infinite | go to depth 5 (a₂ mod 81); stop and audit |

**What the run does not prove:**
- anything at p ≠ 3;
- the complex BSD formula L″(E,1)/2 = C·#Sha;
- finiteness of all of Sha.

It needs neither the Manin conjecture (only c_E ∣ 512) nor p-adic BSD.

## 7. Recommendation

**Authorize Phase A + depth-4 p = 3** (the Lane 3 "Tier 1′" pass {3, 7}, ≈ 14 CPU-h, NUMERIC cost model).
- The chain is valid.
- The expected outcome closes the only prime at which BSD predicts nontrivial Sha.
- Every alternative outcome is decisive.

**Optional independent audit** of the lower half, at a cost to be measured: an unconditional **#Sha[3] ≥ 9** by 3-visibility. Find a 3-congruent curve F with F[3] ≅ E[3] and rank F(Q) ≥ 2 extra, then apply Cremona–Mazur/Agashe–Stein visibility. Alternatively, exhibit explicit 3-coverings. Either route avoids Skinner entirely and cross-checks the run.

**Precondition added after the infrastructure survey** (ARCHIVE_RECOVERED_BRIDGES.md; NEXT_3_TARGETS archive update 1): run T1 only on the *rigorous streaming core*.
- The current `swstream.c` multiplies by the double-rounded `M_PI` (macOS defines it without an `L` suffix), and its 300-ulp error bound is a model.
- The p = 5 result is unaffected: the effect is ≈ 10⁻¹¹ against a slack of 1.95·10⁻³.
- The p = 3 certificate should nevertheless carry a proved floating-point bound.
