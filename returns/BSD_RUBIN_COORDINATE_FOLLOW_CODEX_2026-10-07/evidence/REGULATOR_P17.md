# ord₁₇ Reg_γ(E(ℚ)) = 1, recomputed on the canonical model by two independent implementations (2026-09-25)

## Certificate statement (the standard a Pro 6 review requested, 2026-09-25)

    Reg_γ(E(ℚ)) = 17·r + O(17²),   r ≡ 13 (mod 17),   r ≢ 0,     so   ord₁₇ Reg_γ = 1.

**Data and conventions.**
- **Model:** the global minimal model y² = x³ − x² − 66020924x − 65074271436. It is the reduced minimal model, reached
  from the release equation by x = X + 7578 with u = 1, so ω is unchanged; see the claim index, line 90.
- **Basis:** Q₁ = (−3031, 327384) and Q₂ = (−2394, 281520), the images of P₁ = (4547, 327384) and P₂ = (5184, 281520).
  This is an index-one basis of E(ℚ)/tors (R.1/R.4, exact).
- **Height:** the cyclotomic 17-adic height of Mazur–Stein–Tate, in the Stein–Wuthrich normalization used by the
  release and by lane D. The lane checked PARI's normalization against SW's published 446d1 value at p = 5. Here PARI
  and Sage agree with the published 37a1 value at p = 5.
- **Regulator:** Reg₁₇ = det(⟨Qᵢ, Qⱼ⟩). The value is canonical because it is computed on the reduced minimal model
  (PARI) or is model-independent (Sage).
- **γ-normalization:** γ = 1 + 17 = 18, and Reg_γ = Reg₁₇ / log₁₇(18)². Here log₁₇(18) = 17 − 17²/2 + … has ord 1.

**Precision, including the loss from dividing.**
- Sage gives each height to O(17¹⁴), so Reg₁₇ is known to O(17¹⁵) and PARI's to O(17²⁶).
- Dividing by log₁₇(18)², of valuation 2, loses two digits. So Reg_γ is known to O(17¹³) from Sage and to O(17²⁴)
  from PARI.
- Only the 17¹ digit is used, r = 13, and it is ten or more digits inside every precision.

**Three facts that must stay distinct.**
1. **The computed regulator fact:** ord₁₇ Reg_γ = 1, with r ≡ 13 (mod 17). It justifies the choice of depth (n = 3),
   and it shows that the height pairing is nondegenerate on ⟨Q₁,Q₂⟩.
2. **The theorem inputs, imported and not computed:**
   - Kato's divisibility f_E | L₁₇;
   - SW Thm 6.1, whose equality clause gives primary finiteness **before** the leading-term formula is used;
   - the leading-term formula;
   - SW Prop. 3.5, the depth-3 congruence.
3. **The final valuation inequality.**
   - Given C₁₇ := [T²]L₁₇ = 17u + O(17²) with u a unit, and the ord_T argument, the leading-term formula gives
     ord #Sha[17^∞] = ord [T²]f_E − ord Reg_γ ≤ 1 − ord Reg_γ.
   - Only the lower bound ord Reg_γ ≥ 1 is needed for Sha[17^∞] = 0 at this step. The exact value 1 is what makes the
     depth-3 test meaningful: with ord ≥ 2 the residue would be forced to 0 mod 17².

**Unit-root inputs for the depth-3 package.** These are consistency inputs only; they are neither C₁₇ nor the
regulator.
- a₁₇ = −6, and #E(F₁₇) = 24.
- α ≡ 11 (mod 17), α ≡ 45 (mod 17²) and α ≡ 2068 (mod 17³), by Hensel lifting; they agree with the lane's
  `weights_output.txt` and with the review.
- α⁻¹ ≡ 167 and α⁻² ≡ 145 (mod 17²).
- 1 − 1/α ≡ 4 (mod 17), so ε₁₇ is a unit.

## Result

On the reduced minimal model y² = x³ − x² − 66020924x − 65074271436, obtained by x = X + 7578 with u = 1, and with the
index-one basis Q₁ = (−3031, 327384) and Q₂ = (−2394, 281520):

    Reg₁₇ = 13·17³ + 16·17⁴ + 14·17⁵ + 0·17⁶ + 14·17⁷ + 11·17⁸ + 2·17⁹ + 9·17¹⁰ + 6·17¹¹ + 17¹² + 17¹³ + 14·17¹⁴ + O(17¹⁵)
    Reg_γ = Reg₁₇ / log₁₇(18)² = 13·17 + 12·17² + 8·17³ + … ,   so   ord₁₇ Reg₁₇ = 3  and  ord₁₇ Reg_γ = 1.

**Agreement between implementations, digit for digit from 17³ through 17¹⁴:**

| implementation | model | Reg₁₇ |
|---|---|---|
| PARI 2.17.3 `ellpadicregulator` | reduced minimal model | 13·17³ + 16·17⁴ + 14·17⁵ + 14·17⁷ + … |
| Sage 10.9 `padic_height` (Mazur–Stein–Tate/Harvey; a different code base) | raw and reduced models (identical, as expected) | the same digits |

The individual height-pairing entries also agree: h(Q₁) = 13·17 + 16·17² + …, ⟨Q₁,Q₂⟩ = 5·17 + 7·17² + …, and
h(Q₂) = 15·17 + 12·17² + ….

**Normalization calibration.** For 37a1 at p = 5, PARI and Sage both give 5 + 5² + 5³ + 3·5⁶ + 4·5⁷ + 5⁹ + O(5¹⁰), the
published value.

## What changes relative to the lane-D record (C3, CERTIFIED_NUMERIC)

- **The lane ran PARI on the raw model** y² = x³ − 22735x² + 106272484x. Its value was 9·17³ + 10·17⁴ + ….
- **PARI 2.17.x maps heights back to non-reduced models incorrectly.** See the memory
  `pari-padic-heights-model-dependent`, refereed on 2026-09-18. For this u = 1 change, the offset is the rank-one term
  c·Lᵀadj(H)L.
- **At 17 that offset has valuation ≥ 3.** #E(F₁₇) = 24 is prime to 17, so log Pᵢ ∈ 17ℤ₁₇, and adj(H) has entries in
  17ℤ₁₇. So the offset reaches exactly the 17³ digit on which the valuation depends: it moved that digit from 13 to 9.
  The raw-model valuation happened still to be 3, but nothing protected it.
- **AUDIT_D [9] and [13] recorded a unit-part difference** between PARI and Sage, "ratio ≡ 9 (mod 17)", and
  attributed it to a convention difference. **It is the PARI model bug.** PARI on the reduced minimal model reproduces
  Sage exactly.
- **Proposed grade for ord₁₇ Reg_γ = 1:** computer-assisted.
  - Exact 17-adic arithmetic, with two independent implementations on the canonical model agreeing to O(17¹⁵).
  - The normalization is calibrated on a published value.
- **The other inputs to the depth rule:**
  - The saturation E(ℚ)/17E(ℚ) = ⟨P₁,P₂⟩ is from lane D C2 (PROVED), and the basis has index one (R.4, exact).
  - ε₁₇ is a unit: a₁₇ = −6, the unit root α ≡ −6 (mod 17), and 1 − 1/α ≡ 4 (mod 17).
  - ord₁₇ log₁₇(18) = 1.
  - Hence k = ord ε₁₇ + ord Reg_γ = 1, and depth n₁₇ = k + 2 = 3, as the release states (claim index line 592).

## Files

- `reg17.gp` and `reg17_pari_2173.txt`: PARI on the raw and minimal models, plus the 37a1 calibration. The gp is the
  sage-env 2.17.3.
- `reg17_sage.sage` and `reg17_sage.txt`: the Sage computation.

About 10 CPU-s in total. No lane or handoff file was modified.
