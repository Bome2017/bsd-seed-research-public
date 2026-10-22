# S1: sign, split-height and dependency checks at p = 2243 (split multiplicative)

Date 2026-09-22. Read-only on every sealed artifact. The stream core binaries were used read-only; all outputs are in
this folder.

## S1a. Sign rule s = −w·a_M at multiplicative M ≥ 5: PASS

Method (`S1a_sign/`):
* Eight Δ > 0 curves covering all eight (M ∈ {5, 7}, a_M = ±1, w = ±1) combinations, with M ∥ N and other bad
  primes present.
* Engine `arbcore msl` run at m = M, M², M³ with the predicted s, and with −s as a negative control.
* Every exact eclib symbol [b/m]^± checked for containment in the engine's Arb balls, in exact rational arithmetic.

**Results.**
* **24/24 checks pass. 3 728 exact symbols are contained** with the predicted sign. The count identity holds, and
  the a_q segment roots equal the verifier's.
* **Wrong-sign controls: 24/24 reject**, excluding between 10/12 and 588/588 symbols each. The test has teeth.
* **The seed's patterns are covered:**
  * 15a1 (M = 5, split, w = +1), the same as 2243 (a_M = +1, w = +1, s = −1);
  * 85a1 (M = 5, non-split, w = +1), the same as 5843.

Result file: `S1a_sign/S1A_RESULT.txt`.

## S1b. Split-case height at 2243

**Values** (PARI 2.17.3, seed minimal model):
* Reg_p = 2181·p² + 676·p³ + … ⇒ v_p(Reg_p) = 2, det ≢ 0 (mod p³);
* q_E ≡ 4 521 378 839 (mod p³), v(q_E) = 1;
* ℓ_γ(E) = (ℒ/log κ(γ)) mod p ≡ **1799**. This was reproduced independently by the reviewer (exact modular
  arithmetic from the j-expansion) and here (PARI Tate path).

**Which height PARI uses** (source, `ellpadic.c` `ellpadicregulator`). In the split case PARI sets
s₂ = s₂^{Tate} − 1/(log_p(q)·u²), described as the "extended MW group contribution". `ellpadicbsd` divides by
`ellQp_L` (log q / v(q)).

**Normalization calibration**, as evidence rather than proof, since p-adic BSD is conjectural. `split_bsd_check.sage`
tests PARI's p-adic L-function (modular-symbol path) divided by (L-invariant, Tamagawa, torsion), against PARI's
extended regulator (Tate path). In **9/9** split cases the ratio is 1 + O(p^{4–6}), equal to Sha_an = 1. This
includes **three rank-2 curves with the seed's exact shape**: 446d1 at p = 223, 655a1 at p = 131, 707a1 at p = 101,
each with r_L = 3 = r + 1.

**What is and is not load-bearing.** This is derived from Jones's Thm 3.1 read at source (below).
* **The regulator's valuation is not load-bearing for the sufficient direction.** If a₃ is a unit, the leading term
  f* is a unit. Jones's formula then writes 0 as a sum of non-negative valuations, so v(#Sha) = 0 whatever v(Reg_γ)
  is. Every term is integral by structure:
  * the multiplier into the formal group divides p − 1, and c₂₂₄₃ = 1;
  * log terms lie in pZ_p;
  * ℒ/log κ(γ) ∈ Z_p.

  A wrong regulator value could only make the test fail. It cannot certify falsely.
* **The regulator's nonvanishing is load-bearing.** Jones's leading-term formula is proved **only under**
  nondegeneracy of the height. Jones does not prove the converse "order = r + 1 ⇒ nondegenerate". This is exactly
  how the p = 3 chain was organized: an independent nonzero height certificate (F1 CP-E) was supplied as an input.
  **D5 is therefore open:** an independent certificate that the split-case extended height regulator at 2243 is
  nonzero. PARI's path gives det ≡ 2181·p² ≠ 0 (mod p³). An independent code path is needed before the full run,
  for example the Tate-curve product formula for σ with Werner's correction, or an adaptation of F1's integrality
  method. It is not needed for the pilot.

## S1c. The frozen certificate statement and its dependencies

**Certificate (sufficient direction only).** Let a_{2,3} be the T³ coefficient of the depth-two approximation, in
the Stein–Wuthrich normalization (Néron period Ω⁺ = ω₁, α = a₂₂₄₃ = +1), of the 2243-adic L-function of the seed.
Equivalently, take K = 1024·Z with Z = Σ_{b mod ±1} bal_p(2·C(ℓ(b), 3))·[b/p²]⁺. Then:

    K ≢ 0 (mod 2243)   ( <=> a_{2,3} is a 2243-adic unit )   ==>   Sha(E/Q)[2243^inf] = 0,

provided D1–D8 below hold. **Nothing is claimed if K ≡ 0 (mod 2243).** The converse is withdrawn.

| # | dependency | status |
|---|---|---|
| D1 | Skinner 2016 Thm A at p = 2243 (split; p ∥ N; ρ̄ irreducible; q = 3 or 5843 with q ∥ N and ρ̄ ramified) | hypotheses **verified**; theorem **imported as published** (same stance as the retained 3-primary theorem) |
| D2 | **Split Selmer comparison:** char_Λ(X_Greenberg) = T·char_Λ(X_classical), integrally, given ℒ ≠ 0. At p = 3 the comparison used 1 − a_p = 2 (a unit). Here 1 − a_p = 0, the extra zero. | **OPEN, source item.** Greenberg's trivial-zero argument, used by Skinner for Thm B under ℒ ≠ 0 (hypothesis (iii); ℒ ≠ 0 is known for elliptic curves). Jones's f_H = T^e·f_S is the same structure. Must be read and bound before the full run |
| D3 | Period comparison, canonical versus Néron/Gross periods, at 2243 ∣ N (the R2-type seam; Kim–Ota needs p ∤ N) | **as at p = 3**: retained "Skinner as published", with internal provenance open at the Euler-removal interface |
| D4 | Finiteness first: the R1 argument (2.1)–(2.4) | transfers: E[p^∞](Q_∞) = 0 by irreducibility; restriction injection; rank ≤ order. Via D2, ord_T char(X_cl) = ord L_p − 1 = 2 ⇒ Sha[p^∞] finite |
| D5 | Nondegeneracy: certified nonzero split-case extended height regulator at 2243 | **OPEN before the full run** (independent code path). PARI: det ≡ 2181·p² ≠ 0 (mod p³); calibration 9/9 |
| D6 | Jones Thm 3.1, split elliptic clause (**read at source this session**, author copy l.676–718): under Hyp 1–4 (Hyp 1 = Sha finite, supplied by D4; Hyp 4 needs log_p q ≠ 0, where v(log q) = 1), ρ ≥ r + 1; if nondegenerate, ρ = r + 1 and L^{(ρ)} ∼ (log q/ord_p q)·det⟨,⟩·#Sha·∏m_ℓ/(tors·tors~). Also Jones 1990 Thm 4.3 (algebraic = −Schneider height) and SW §4.2 (Werner-corrected split height) | **read**; used only in the direction "nondegenerate + finite ⇒ formula" |
| D7 | SW Prop 3.5, depth-two approximation mod p (c = 0; every cusp b/p^k is equivalent to 1/p; lattice (1/1024)Z with v₂(c₀) ≤ 8 and 4547 ∤ c₀; p ∤ c₀ at p ∥ N) | read (SW §3); lattice and Manin inputs retained from the p = 3 theorem |
| D8 | Engine: unitary-cusp formula, sign s = −w·a_M, truncation bound, verifier | **validated** (S1a at M ≥ 5; stream-core validation at M = 1, 3) |

**Consequence for spending.** D2 and D5 must be discharged before a full run is purchased. Neither blocks the
engineering pilot, because the pilot measures cost and correctness of the pipeline, not the certificate.
