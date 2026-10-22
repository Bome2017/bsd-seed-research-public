# Regrade of the derived-Gross return under the tightened threshold (2026-10-07)

## STATUS: PRECISE_OBSTRUCTION (unchanged; not `IDENTITY_ONLY_UP_TO_P_UNIT`)

**What this file is.**
- The run governed by the original `DELTA_TASK_DERIVED_GROSS.md` has already been completed; its return is `DERIVED_GROSS_RESULT.md`. That return is left as it was.
- The package has now been changed so that any **future** submission is graded by the tightened threshold:
  - `DELTA_TASK_DERIVED_GROSS.md`: new sections "Admission threshold" (interfaces 1–4) and "Unit ambiguity" (`IDENTITY_ONLY_UP_TO_P_UNIT`, cases U1/U2), plus the new status in the status list and return format;
  - `SUBMISSION_PROMPT.txt` and `SUBMIT_COMMAND.txt`: the same threshold and the new status, in short form;
  - `MANIFEST.sha256`: regenerated.
- This file re-grades the existing return against interfaces 1–4 and records where each unit would sit.

**Labels.**
- **PROVED**: proved here, in Lean (`RequestProject/DerivedGross/Threshold.lean` or `Obstruction.lean`; both build, no `sorry`) or by the short argument given.
- **IMPORTED**: from the canonical packet (file named) or the literature.
- **HEURISTIC**: everything else.

## 1. The four interfaces, checked against the existing return

There are two candidates. (H^ac) is the canonical anticyclotomic Mazur–Tate pairing; (CAND) is G2's cyclotomic pairing transferred to degree two at split ℓ (`DERIVED_GROSS_RESULT.md` §2.2).

| Interface | (H^ac) | (CAND) | Label |
|---|---|---|---|
| 1. Characteristic-zero degree-two identity, every level, one constant | Degenerate: det h^ac ≡ 0 on E(ℚ) = E(K)⁺, so the top row reads Θ⁽²⁾ = 0 | **Missing.** Distribution relations and the functional equation stop at degree one; the interpolation formula has no Mordell–Weil side; no printed theorem gives Θ⁽²⁾ from E(ℚ) | PROVED (H^ac, given IMPORTED functoriality); IMPORTED/HEURISTIC literature screen (CAND) |
| 2. m_E ∈ ℚ^×, Ш/FIN/Q36/BSD-free, m_E ≠ 0 proved, denominator controlled | No constant is determined (0 = m·0) | **None defined.** Every known normalization uses #Ш(E/K) or the BSD quotient of E/K. m_E ≠ 0 is not proved; b is not defined | HEURISTIC |
| 3. Both reduction maps with one compatible normalization | – | Right map: **present.** det h^cyc ↦ R_{p,ℓ} under the convention of `CURRENT_FRONTIER.md` §1.7. Left map Θ⁽²⁾ ↦ C₂(p,ℓ): **missing** (see §2) | IMPORTED (right map, G2 and §1.7); HEURISTIC (absence of left map) |
| 4. Explicit S with Ш[p] ≠ 0 ⇒ p ∣ num(m_E) | – | The **logic** is PROVED (`finite_support_of_square`). Its hypotheses 1–3 are not supplied | PROVED (logic only) |

**First failing interface: 1** for both candidates, and for (CAND) interface 3 fails independently. So the status stays `PRECISE_OBSTRUCTION`. It is not `IDENTITY_ONLY_UP_TO_P_UNIT`: that status needs the square up to proved units, and here the left vertical map does not exist at all, so no unit question arises.

## 2. Where the left vertical map is missing (interface 3), precisely

- **The groups match** (PROVED, `Obstruction.lean` `sq_tmul_sign_invariant`). For split ℓ, (G_ℓ ⊗ ℤ_p)^{⊗2} ≅ (Gal(ℚ(μ_ℓ)/ℚ) ⊗ ℤ_p)^{⊗2} canonically. So a map of the right type exists on the level of targets.
- **The elements do not match** (HEURISTIC, no printed comparison). Θ⁽²⁾ is built from the JL eigenfunction on the definite Gross set of B (ramified at 3, 2243, 5843, ∞) and interpolates L(E/K, χ, 1) for **ring class (anticyclotomic)** χ. C₂(p,ℓ) is built from modular symbols of E/ℚ and interpolates L(E, ψ, 1) for **Dirichlet** ψ of conductor ℓ. For ψ∘N_{K/ℚ}, L(E/K, ψ∘N, s) = L(E,ψ,s)·L(E^{−7},ψ,s), but ψ∘N is cyclotomic, not anticyclotomic, so the factorization does not reach θ_ℓ. Identifying the degree-two pieces of the two groups does not identify the two elements.
- **Period normalizations** (HEURISTIC). Θ is normalized by the Gross period Ω_{E,N⁻} and the primitive JL form; C₂ by ω₁ (record convention, symbols Re λ/ω₁). Their comparison involves a fixed rational of the shape L(E^{−7},1)/Ω_{E^{−7}} times a congruence-number factor. That rational is defined without Ш (modular symbols), but the task file lists the BSD quotient of E/K among the excluded constants, and its relation to #Ш(E^{−7}) is a BSD statement. This is where a future return must decide between interface 2 succeeding and `CIRCULAR_CONSTANT`.

## 3. Where units would sit in a future return (the U1/U2 distinction)

- **Proved unit factors that are harmless (PROVED arithmetic).**
  - a_ℓ − 2 ≡ −4 (mod p) at G2's ℓ (ρ̄_p(Frob_ℓ) = −I, IMPORTED G2). So the Euler-type factor (a_ℓ − 2) is a proved p-unit for odd p.
  - Changing the generator g of F_ℓ^× to g^k with p ∤ k scales the degree-two piece by k², a proved p-unit. The record fixes g = least primitive root (§1.7).
  - Swapping λ and λ̄ acts trivially on degree two (`sq_tmul_sign_invariant`).

  These are U2-type factors, each proved to be a unit, so they preserve zero detection (`proved_units_preserve_zero`). They affect only the exact residue (the 288 calibration).
- **A correction to the U1/U2 dichotomy as posed (PROVED).** For pure zero/nonzero detection mod p, what matters is not whether there is one unit or two, but whether the **total discrepancy** (v_{p,ℓ}/u_{p,ℓ}) is proved to be a p-adic unit. Two separately **proved** units are as good as one (`proved_units_preserve_zero`). What fails is any factor that is not proved to be a unit: an element of ℤ_p of unknown valuation, an element of ℚ_p, or two maps normalized independently so that the top row is not transported by one map. Then the bottom row gives no detection (`uncontrolled_factor_no_detection`). The package now states the dichotomy in this form.
- **Unit versus constant (IMPORTED, `3_LIVE_QUESTION/STATUS.md` §1).** The existence form of the Law (free p-units) is FIN restated **because its m can be chosen as the product of the Ш-alarm primes**. With m_E Ш-free and proved nonzero, a U1 result, or a U2 result with proved units, still gives finite support. It does not give the exact Law or consistency with the eleven 288 residues.

## 4. What the full square would deliver (PROVED logic, Lean)

- **Finite support** (`finite_support_of_square`). Hypotheses:
  - Interface 1: b•Θ = a•D.
  - Interface 2: a, b ≠ 0.
  - Interface 3: one additive map φ_{p,ℓ} with φΘ = C₂ and φD = w·(a_ℓ − 2)R, w proved nonzero (w = 1 exact).
  - G2: an admissible ℓ with (a_ℓ − 2)R ≢ 0.
  - Detector: C₂ ≢ 0 ⇒ Ш[p] = 0.

  Conclusion: for p ∉ S with p ∤ b, Ш[p] ≠ 0 ⇒ p ∣ a; so {p : Ш[p] ≠ 0} ⊆ S ∪ {p ∣ b} ∪ {p ∣ a}, which is finite.
- **The bottom row is the exact Law** (`bottom_row_is_exact_law`). b·C₂ = a·X with X ≠ 0 and p ∤ b gives s_p = C₂/X = a/b in F_p. So `DERIVED_GROSS_IDENTITY` in the tightened sense implies G1 with m = m_E. That is consistent with `CURRENT_FRONTIER.md` §3 (G1 is sufficient, and strictly stronger than FIN-tail).
- **Coverage** (IMPORTED, `CURRENT_FRONTIER.md` §1.3). If the bottom row is read with the record's C₂(p,ℓ) and the Ota detector, no ordinarity is needed. The previous return's bookkeeping used the definite detector M₂ (good ordinary p only); a full square would remove that restriction.
- **The exceptional set a future return must write out** (IMPORTED/HEURISTIC). At least S₀ ∪ B* = {2, 3, 5, 19, 59, 487, 2243, 4547, 5843}, plus 7 (ramified in K), plus the primes of b, plus whatever the left map excludes. G2's ℓ must also split in K = ℚ(√−7) for (CAND) to apply. Compatibility of that Chebotarev condition with G2's conditions is HEURISTIC: it needs K ∩ L_p = ℚ, which is not checked here.
- **Calibration** (HEURISTIC). With exact normalization (w = 1, §1.7 convention), the eleven audited residues force m_E ≡ 288 at p = 5, 17, …, 47. By the record's CRT bound, any such m_E of height ≤ 3·10⁶ equals 288 = 2⁵·3². Delivering it would require a Ш-free definition of 288 (conjecturally 32·#Ш = 8q). Its numerator primes {2, 3} lie in S, so the support conclusion would be Supp Ш ⊆ S.

## 5. Lean

File: `RequestProject/DerivedGross/Threshold.lean`. It builds, has no `sorry`, and adds no axioms.

```
'DerivedGross.Threshold.single_unit_preserves_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.Threshold.proved_units_preserve_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.Threshold.uncontrolled_factor_no_detection' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.Threshold.bottom_row_is_exact_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.Threshold.finite_support_of_square' depends on axioms: [propext, Classical.choice, Quot.sound]
```

FIN, ORDER9 and Q36: unchanged.
