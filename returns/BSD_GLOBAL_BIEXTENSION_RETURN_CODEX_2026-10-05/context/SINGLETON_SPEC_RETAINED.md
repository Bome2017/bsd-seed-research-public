# Single-prime witness certificate: frozen specification (v1, 2026-09-26)

This is the evaluation contract for testing Sha[p^∞] = 0 at one good prime p through one auxiliary prime l. It is
**frozen for the independent audit**; changes after the audit need a new version. **No seed run is authorized.**

## 1. Statement used (to be audited)

**Ota, arXiv:1509.00682**, Theorem 1.5, a special case of Theorem 6.4, with the order of vanishing from Theorem 5.17.
The WC deduction's reading is in `EXACT_WC_ANTECEDENT.md`, which copies the sealed WITNESS_CONTENT_THEOREM.md, sha256
556ecfa5…. For E/ℚ of rank 2 and a prime p meeting Ota's hypotheses (5.17), and S a squarefree product of admissible
auxiliary primes:

> if the rank-2 leading term θ̃_S ∈ I_S²/I_S³ is nonzero mod p, then Sha(E/ℚ)[p] = 0.

Then Sha[p] = 0 implies Sha[p^∞] = 0: a nonzero p-primary torsion group contains an element of order p.

## 2. Admissible auxiliary prime (the singleton S = {l}, k = 1)

l is prime, l ∤ pN, and l ≡ 1 (mod p) with **v_p(l − 1) = 1**, so P_S = (ℤ/l)ˣ ⊗ ℤ_p ≅ ℤ/p. In addition
**E(F_l)[p] is cyclic**, either 0 or ℤ/p; check it from the group structure of E(F_l).

Seed values (PARI, `seed_aux_primes.txt`):

| p | l | #E(F_l) | E(F_l) | E(F_l)[p] |
|---|---|---|---|---|
| 17 | **103** | 106 | ℤ/106 | 0 |
| 17 | 137 | 140 | ℤ/70 × ℤ/2 | 0 |
| 17 | 239 | 214 | ℤ/214 | 0 |
| 19 | 191, 229 | 202, 240 | cyclic | 0 |
| 23 | 47 | 44 | ℤ/44 | 0 |
| 29 | 59 | 64 | ℤ/32 × ℤ/2 | 0 |

The prime p itself: #E(F₁₇) = 24, #E(F₂₃) = 24 and #E(F₂₉) = 30, so none is anomalous. a₂₃ = a₂₉ = 0 (supersingular),
and a₁₇ = −6.

## 3. The coefficient

- **Generator:** g = the **smallest primitive root** mod l.
- **Index:** x(a) = ind_g(a) mod p, taken in {0, …, p−1}.
- **Symbols:** [a/l]⁺ are the plus modular symbols in the **ω₁ normalization** (least positive real period) of the
  certified pipeline.
  - They are identified exactly in (1/1024)ℤ.
  - They equal Sage/eclib's `modular_symbol(sign=+1)` on the regression curve (§6).

Then

    c_k = Σ_{a=1}^{l−1} C(x(a), k) · [a/l]⁺   for k = 0, 1, 2,        and the witness is  c₂ mod p.

**Why this is θ̃_S in I²/I³.**
- The Mazur–Tate element is θ_l = Σ_a [a/l]⁺ σ_a ∈ ℚ[G_l]. Project it to ℤ_p[P_S], sending σ_a to σ^(x(a)) with σ the
  image of g.
- In 𝔽_p[P_S]/I³ = 𝔽_p[T]/(T³), with T = σ − 1, (1+T)^x = Σ_k C(x,k)T^k, so θ ≡ c₀ + c₁T + c₂T².
- When c₀ = c₁ = 0 (Ota 5.17 at rank 2), c₂T² is the image of θ in I²/I³ ≅ 𝔽_p.

**Invariance: nonvanishing is intrinsic.**
- **Generator change:** g ↦ g^u sends c₂ to c₂·u⁻² (mod p). This was checked on all 12 primitive roots at
  389a1, l = 29.
- **σ_a ↦ σ_a⁻¹:** u = −1, so c₂ is unchanged.
- **Period and Manin-constant conventions** differ by powers of 2 (c_E | 512 on the seed; Ω = 2ω₁ when Δ > 0). These
  are units at odd p.
- **Audit item 7** checks that Ota's normalization of θ̃ differs from this one by a p-adic unit only.

## 4. Pipeline parameters (seed)

- `arbcore msl` with target `m = l`, M = 1, Q = N = 6503188012738584, sign s = w = +1, LATDEN = 1024.
- T is the aligned `arbcore tmin` value (SEGQ = 2²⁴):

  | l | T_min | segments |
  |---|---|---|
  | 103 | 33,207,031,228 | 1,980 |
  | 137 | 44,427,625,787 | 2,649 |
  | 239 | 78,386,390,940 | 4,673; Stage W must be extended |

- **Coefficients:** the existing verified a_q segments (`BSD_SEED_P13_RUN_2026-09-21/run/ap`, 3,281 segments), read-only.
  msl writes only to its own output folder.
- **Stage C (as in `p3_check.py`):**
  - AP_SEGROOT equals the SHA-256 over the verifier's per-segment receipts for exactly the segments used;
  - the count identity holds;
  - all φ(l) plus and minus symbols are identified (a unique point of (1/1024)ℤ in each ball).

## 5. Built-in checks (all must pass, or the result is void)

1. **c₀ = 0 exactly.** This is Hecke at l: Σ_{a=1}^{l−1}[a/l]⁺ = (a_l − 2)[0]⁺, and [0]⁺ = L(E,1)/Ω⁺ = 0.
2. **c₁ ≡ 0 (mod p).** Ota 5.17 forces it; a failure means an error.
3. **Symmetry:** [(l−a)/l]⁺ = [a/l]⁺ for every a.

## 6. Regression fixture: 389a1, p = 7 (PASS, 2026-09-26)

The files are in `regression_389a1/`: `compare.sage`, `compare.txt`, the `msl_m{29,379}.txt` outputs, the logs and the
tmin values. The full certified chain ran (apwit, then wverify, then arbcore msl; T = 65535).

| l | symbols vs exact eclib | c₀, c₁, c₂ (pipeline = exact) | c₂ mod 7 |
|---|---|---|---|
| 29 | 28/28 equal (ratio exactly 1) | 0, 0, 8 | **1**: positive case |
| 379 | 378/378 equal | 0, 0, 0 | **0**: negative case |

This is a regression of the pipeline and the formula. It is not evidence for the theorem.

## 7. Outcome rule

- **c₂ ≢ 0 (mod p):** Sha(E/ℚ)[p^∞] = 0, at the grade "written deduction plus published theorem applied (Ota)",
  subject to the audit.
- **c₂ ≡ 0 (mod p):** **inconclusive** at this l; nothing follows.
  - Next: l = 137, then l = 239.
  - **No automatic depth escalation,** and no automatic move to two-prime S.
- **Any built-in check fails:** the result is void; investigate.

## 8. Not this

This singleton coefficient in I_l²/I_l³ is **not** the two-prime Kurihara/core-pair coefficient (c₁₁ for S = l·m).
The rank-2 "two primes" intuition belongs to that different projection. Ota's theorem allows any squarefree S, including
a single prime.
