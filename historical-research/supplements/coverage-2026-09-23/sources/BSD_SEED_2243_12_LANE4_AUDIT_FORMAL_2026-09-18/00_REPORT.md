# LANE 4 REPORT: independent adversarial audit of v₂(c₀) ≤ 8, plus isolated Lean formalization (seed (2243,12)), 2026-09-18

**Verdict: `V2_C0_LE_8 = LANE4_AUDIT_PASS`.**
- Five independent tracks reproduce the derived lemma v₂(c₀) ≤ 8 of MANIN_2_PRIMARY_GATE_2243_12. No track finds a fatal, bound-changing or repairable defect; every correction is cosmetic.
- The consequence chain to `SMALL_SEED_2243_12_SHA5 = PROVED_ZERO` passes.
- Four Lean files (35 theorems) machine-check the isolated algebraic and arithmetic steps. They use only the standard axioms, and fresh reviews found them faithful.

**Scope.** This lane audits and formalizes; it does not merge anything. The gate itself was merged by lane 1 at 10:32 (report sha `54aa940c…`, §8). The pre-merge pin `0a1f0329…` in `00_CHARTER.md` is explained in the charter addendum; the mathematics is unchanged.

## 1. Audit tracks

| track | model | verdict | findings |
|---|---|---|---|
| Lens A: Step A (`audit/LA_stepA.md`) | Fable, fresh context | PASS_WITH_CORRECTIONS | 4 COSMETIC |
| Lens B: Step B (`audit/LB_stepB.md`) | Fable (relaunched after the usage cap) | PASS_WITH_CORRECTIONS | 6 COSMETIC (2 already in referee), 1 UNVERIFIED (already in referee) |
| Lens N: numerics (`audit/LN_numerics.md`, `numerics/LN_*`) | Opus | PASS_WITH_CORRECTIONS | 2 COSMETIC (referee numerics), 1 UNVERIFIED (latent script hazard) |
| Lens C: consequence chain (`audit/LC_consequence.md`) | Opus | PASS | 2 COSMETIC, 2 UNVERIFIED |
| Blind rebuild (`audit/A0_blind_reconstruction.md`) + comparator (`audit/A0c_comparison.md`) | Fable, blind; Opus comparator | SAME_ROUTE_DIFFERENT_BOUND; blind **B = 4**; no defect | 2 COSMETIC |

No finding triggered adjudication: neither run started an adj:* agent, and the cap was 5 per track.

### Lens A (Step A)
- **ARS12 Thm 3.6(a) was read in the original** (math.fsu.edu/~agashe/math/moddeg3.pdf). The statement is verbatim "ñ_A ∣ r̃_A", for Γ₀(N) or Γ₁(N) with N ≥ 4.
- The lattice is S₂(Z) with integral coefficients at ∞. The complement is the Petersson complement, which equals the unique saturated Hecke-stable complement. For an elliptic curve the modular exponent equals the modular degree.
- Part (a) has no hypothesis on N, p or multiplicity one. The item "ARS12 read only through restatements" can therefore be closed.
- The step is slightly sharper than stated: v₂(c₀) ≤ v₂[P_χ(S):P_χ(H)] ≤ e′.
- ARS12 l.273–285 gives full-T equivariance of π^∨ via W_N. This is stronger than the referee's anemic-algebra repair, and both are correct.
- The class size 2 (needed for c_E ∣ 2c₀) was checked numerically with `ellisomat`, which returned degree matrix [1,2;2,1].

### Lens B (Step B)
Links B.1–B.7 were re-derived from CNS §§5–6, with Pasten §10 as corroboration:
- **B.1:** regularity holds at the cusps too (mixed-level normalization, R_v unramified), and α is étale at the four generic points.
- **B.2:** there are exactly four reduced, geometrically integral components, of degrees 1, 1, 2, 8. The bound p_a ≥ g′ needs no smoothness.
- **B.3:** s = μ/12 = ψ(N/8) by direct count, so the Deuring mass formula is bypassed. There is exactly one point over each supersingular point (ker F³), and it lies on all four components.
- **B.4:** 12μ, c_m = 4c′ and ω·F = 2μ − 4c′.
- **B.5:** integrality of the q-expansion gives regularity along the whole of C_∞.
- **B.6:** the adjunction sign passes three independent checks.
- **B.7:** the descent to X uses the S2 property of the dualizing sheaf.

Further results:
- Every hypothesis of the Lean lemma `StepB.k_le_eight` is supplied by the geometry in the same normalization.
- No step needs smooth components; smoothness enters only the unused K ≤ 4 remark.
- Nothing depends on the odd primes of N beyond their being 2-adic units.
- Seed constants: μ = 13017263840621568, c′ = 145536, and the bound 9 − 12c′/μ = 8.99999999987.

Cosmetic citations:
- LB-1: add the tame cusp factors to "CNS 5.10 at the cusps".
- LB-2: explain why the type of the cyclic subgroup is constant on the ordinary locus (via w₈).
- LB-3: over ∞ there are four cusps of X_m, with widths 1, 1, 5, 5; any of them works.

### Lens N (numerics)
- **e′(N)** is 0, 2, 1, 3, 3, 3, 3, 4, 4, 3, 3, 4, 3, 4, 3, 3, 3 at N = 24, 56, 72, 88, 120, 152, 168, 184, 248, 264, 280, 312, 344, 376, 392, 408, 456.
  - These were computed exactly by a new rational method: integrality through W_N, f(z+½)|W_N and f(z+¼)|W_{2N}.
  - Levels 24–184 were also computed numerically at precisions 160 and 320, with identical H.
  - The a=0 pole is ≤ 4 on 40 levels N = 8M (M odd, 3 ≤ M ≤ 81).
- **There is no e′ ≥ 5 and no e′ ≥ 9.**
- **Mechanism of the growth.** The growth comes from level-raised oldforms: (V₈g)|W_N = (1/8)·g|W_M gives pole 3. At most +1 more comes from the mod-2 Frobenius relations h₁ + h₂² + h₄⁴ + h₈⁸ = 0. These occur at M = 23, 31, 39, 47, 55, all ≡ 7 (mod 8).
  - Open: the source of the pole 4 at N = 472 (M = 59).
- **Step A inequalities.** All 45 Cremona optimal curves at these levels satisfy κ ≤ v₂(deg φ) − v₂(c₀) and v₂(deg φ) ≤ v₂(r_E) ≤ e′ + κ.
- **Corrections to the referee's numerics:**
  - LN-1: κ(152b1) = 2, not 1.
  - LN-2: the referee's scripts run at realprecision 38, so the [S:H] indices they report are unreliable. Their e′ values are nevertheless correct.

### Lens C (consequence chain, new links only)
- c₀ = 2^a, and c_E ∣ 2c₀ ∣ 2⁹, so c_E ≤ 512 < 3999 (T₁) < 399575 (T₂).
- **LC-2 (UNVERIFIED, not a defect).** The streaming run's floating-point error is a modelled bound (300 ulp per term), not interval arithmetic. Its size is 2.65·10⁻⁹ against a slack of ≈ 1.95·10⁻³ at c_E ≤ 512, so the model would have to be wrong by a factor of **≈ 7·10⁵** to matter.
- **LC-3 (COSMETIC).** "Kato + SW only" should read "p-adic inputs: Kato + SW Thm 6.1 only; no Manin hypothesis". The chain also uses Kolyvagin (L(E,1) = 0), Mazur/Česnavičius for odd p ≠ 4547, Edixhoven for 4547, Steps A/B, and the merged rank and saturation facts.
- **LC-4 (UNVERIFIED).** The absence of odd-degree isogenies is cited from the merged all-odd residual-image review. Lens A confirmed the class size numerically.

### Blind rebuild and comparison
- **The route.** The blind agent never saw the gate. It reconstructed the same route: rational singularities ⇒ H is the Néron lattice; ω_f primitive; π∘π^∨; ARS12; κ cancels; intersection theory on the regular model of Γ₀(N) ∩ Γ₁(ℓ).
- **Its bound is v₂(c₀) ≤ 4.** The sharper constant comes from all three component rows plus the Katz–Mazur 13.4.7 contact orders (2 for {(3,0),(2,1)} and {(0,3),(1,2)}, 1 otherwise).
  - It read these through Edixhoven 1990 §1.4 and Conrad BDP17 Thm B.3.1.3 on the web; they are **not verified locally**.
  - **v₂(c₀) ≤ 4 is therefore CONDITIONAL** on those contact orders. It is not needed, since 8 suffices.
- **Consistency with the numerics.** The numerics attain K = 4 (at N = 184, 248, 312, 376), so 4 is the best this route can give.
- **Comparator.** It found 9 divergences, and none exposes a defect. The gate's weaker inequalities all point in the direction the argument needs, and every overlapping number agrees.

## 2. Lean formalization (`lean/`; rebuilt independently at the end, logs in `state/final_rebuild/`)
Toolchain: Lean v4.30.0-rc2, Mathlib 5450b53e. Every file has 0 errors and 0 warnings. The axioms are only {propext, Classical.choice, Quot.sound}. No file contains sorry, admit, an axiom declaration, native_decide, implemented_by or unsafe.

| file | main theorems | covers | fresh review (Fable) |
|---|---|---|---|
| `StepB_Intersection.lean` | `intersection_bound` (general n), `k_sub_le_eight`, `k_le_eight`, `k_sub_le_rat`, `k_sub_le_four_conditional`, `nonvacuous_k_le_eight` | the intersection-matrix inequality and K ≤ 8 (k_i − k_∞ ≤ 9 − c′/s) | faithful, 3 minor |
| `StepA_Lattice.lean` | `congruenceModuleEquiv` (S/(S_χ+S_⊥) ≃ P(S)/S_χ), `exponent_transfer`, `rank_one_index`, `valuation_chain`, `stepA_master`, `stepA_master_dvr` | Step A algebra; κ cancels | faithful, 5 minor |
| `Regulator_Saturation.lean` | `gram_change_of_basis`, `det_gram_change`, valuation invariance (ℚ and p-adic), `not_dvd_det_of_images`, `seed_index_prime_to_five`, `seed_regulator_valuation`, torsion-killing lemmas | regulator index invariance and mod-5 saturation (R = [[1,1],[1,0]]) | faithful, 4 minor |
| `GL2F5.lean` | `sl_le_of_transvection`, `eq_top_of_sl_le_of_det_surj`, `image_eq_top`, `X_sq_add_two_irreducible`, `R_det`, **`neg_one_mem_of_index_lt`** | the GL₂(F₅) image argument; **"every subgroup of index < 24 contains −I", previously GAP-only** | faithful, 3 minor |

**Not formalized (by design).** The modular-curve geometry is the hypotheses of `k_le_eight`. The step "K ≤ 8 ⇒ 2⁸S ⊆ H" (descent) is geometry; review F2 notes that it lies between the two Lean files. The lattice inputs are hypotheses of `stepA_master`: rational singularities, ω_f primitive, the Néron maps, and ARS12. The Galois inputs are hypotheses of `image_eq_top`: ψ₅ irreducible, the Tate transvection, and det = cyclotomic. Nothing was sent to Aristotle or Harmonic.

## 3. Chain-level item from Lane 2: the PARI p-adic height bug is CONFIRMED (`numerics/L4_reg5_NOTE.md`)
- On a non-reduced model, PARI 2.17.4 `ellpadicheight` differs from the canonical value by exactly −r·log P·log Q (in ellpadiclog units), with r = 7578, the x-shift to the minimal model. The source is `ellpadic.c` l.740–744. Lane 2's referee writes the same term as −2r·lᵢlⱼ in PARI's internal normalization.
- Sage's own `padic_height` (not PARI) is model-independent here: it reproduces SW's 446d1 value to O(5⁹), and on the seed it matches PARI on `ellminimalmodel` to O(5¹³).
- **The canonical value is Reg_γ ≡ 21 (mod 25).** The SW gate's raw-model value was 6 (mod 25), and its printed digits are correct only mod 5³.
- **ord₅ Reg_γ = 0 holds in every model and every implementation, so the Sha[5^∞] = 0 chain is unaffected.**
- Lane 2's consistency flag (a₂ vs 4·#Sha mod 5) is RESOLVED on their word, via Lane 3's certified Sha_an = 9; Lane 3's audit is pending. It is not verified here and is not load-bearing.

## 4. Suggested cosmetic edits to the gate report (for the owner; not applied here)
- Close the ARS12 provenance item (LA-F2).
- Add a sentence saying the class has exactly two curves, so c_E ∣ 2c₀ (LA-F3).
- Fix the three Step-B citations: LB-1 (tame cusp factors), LB-2 (type constant on the ordinary locus via w₈) and LB-3 ("a cusp over ∞", four of them).
- Correct the referee's κ(152b1) to 2, and add a precision caveat on the referee's scripts (LN-1, LN-2).
- Reword "Kato + SW only" (LC-3).
- Optionally record the ≈ 7·10⁵ floating-point margin (LC-2).
- Optionally add the canonical Reg_γ ≡ 21 (mod 25), with the model caveat, to the SW gate record.

## 5. Process record
- **Forked duplicates.** At 11:04 I sent the checkpoint rule to 4 running workflow agents with SendMessage, and each send forked a duplicate. I stopped the forks by id at 11:07, and the originals continued.
- **Usage cap.** It cut off lens B, lens N and the blind rebuild at about 11:40. They were relaunched from disk at 15:55 (`state/resume_workflow.js` v2, `state/relaunch_args_1555.json`) and finished without errors.
- **Restartability.** `RESUME.md` and `STATE.json` were maintained throughout by `tools/checkpoint.py`, which merges both runs and ran every 10 minutes. Every agent result is in `state/results/`.
- **Duplicate-writer exposure.** `GL2F5.lean` was reviewed and rebuilt after the overlap. The final rebuild of all four files is clean.

## 6. Proposed ledger block (NOT merged)
```
LANE4_AUDIT_V2_C0_LE_8 (2026-09-18) — MANIN_2_PRIMARY_GATE_2243_12 independently AUDITED: PASS (cosmetic corrections only)
  Tracks: lens A (Step A; ARS12 Thm 3.6(a) read in the original), lens B (Step B, B.1-B.7 re-derived from CNS 5-6),
    lens C (consequence links), lens N (e'(N) <= 4 at 17 levels 24..456, exact; a=0 pole <= 4 on 40 levels),
    blind rebuild (same route, never saw the gate; B = 4 CONDITIONAL on KM 13.4.7 contact orders read via Edixhoven 1990 /
    Conrad BDP17, not verified locally). No fatal, bound-changing or repairable finding. v2(c0) <= 8 stands.
  Lean (v4.30.0-rc2, Mathlib 5450b53e; standard axioms only; fresh-reviewed faithful): StepB_Intersection (K <= 8 from the
    intersection data), StepA_Lattice (congruence-module iso; kappa cancels), Regulator_Saturation (det A^2 index law; mod-5
    saturation for R = [[1,1],[1,0]]), GL2F5 (transvection + no stable line => SL2; index < 24 => contains -I).
  Chain notes: LC-2 fp error of the SW streaming run is modelled (margin ~7e5 at c_E <= 512), not interval arithmetic.
    PARI 2.17.4 p-adic heights are wrong on non-reduced models (-r log P log Q); canonical Reg_gamma = 21 mod 25 (Sage-confirmed);
    ord_5 Reg_gamma = 0 unaffected.
```

## 7. Files
`MANIFEST.sha256` lists every file in this directory except the `state/` snapshots and `tools/.leanslot*`. The restart state is in `RESUME.md` and `STATE.json`.
