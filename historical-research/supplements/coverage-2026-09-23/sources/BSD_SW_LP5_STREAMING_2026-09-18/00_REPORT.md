# STEIN_WUTHRICH_P5_LP_RUN_001 — certified streaming computation of a₂ mod 5 for the seed (2243, 12)

**Operator authorization (2026-09-18):** up to 20 threads, 12 GB, about 6 aggregate CPU-hours, 30 minutes wall time.

**Operator conditions:**
1. A certified truncation.
2. Validation on 234446a1, 446d1 and 389a1.
3. Two independent final evaluations.
4. A repeat at a stricter error target.

**Seed.** E: y² = x³ − 22735x² + 106272484x (Zywina (m, n) = (2243, 12)), N = 6 503 188 012 738 584, root number +1.

**Target.** a₂ mod 5, where

    a₂ ≡ 3([2/25]⁺ + [3/25]⁺ + [4/25]⁺ + [11/25]⁺) + 4([9/25]⁺ + [12/25]⁺)   (mod 5)

(merged SW gate, six-symbol addendum). a₂ ≢ 0 (mod 5) gives ord_T L₅ = 2, v₅(L*₅) = 0, b₅ = 0, and **Sha(E/Q)[5^∞] = 0**. This uses Kato Thm 7.3 and SW Thm 6.1 only. The identification of the computed symbols needs the Manin-constant condition c₀ ≤ 199 787 (§3).

## 1. Method (Wuthrich, Math. Comp. 87 (2018), §4 and Thm 12; unitary cusps, gcd(25, N) = 1)

**The formula.**
- λ(b/25) = λ(τ) + w·λ(W_r τ), with τ = b/25 + iy, y = 1/(25√N), W_r τ = −u_b/25 + iy, u_b = (Nb)⁻¹ mod 25 and w = +1. This is Wuthrich's (8) with ε_N = −w.
- Both evaluations use the 25 class sums S_k = Σ_{n≡k (25)} (aₙ/n)·e^{−2πny}.
- x_b := Re λ(b/25)/ω₁, where ω₁ = PARI `E.omega[1]` = 0.0280449….

**Streaming (`src/swstream.c`).** The decomposition of n ≤ T₂ is exact:
- **Part L:** n = s·q with q prime in (R, T₂] and s ≤ T₂/q, so a_n = a_s·a_q.
- **Part S:** the R-smooth n, by a segmented sieve with exact integer a_{p^e}.

Here R = ⌊√T₂⌋. Memory is O(√T), and the sums are compensated (Neumaier) sums in x86 80-bit `long double`.

**a_q.**
- Small primes and bad primes: PARI `ellap`.
- q > R: a new certified counter (`src/fastap.c`). It is a baby-step giant-step count with the 2-torsion congruence (the known rational 2-torsion root is asserted for every q) and the twist trick (d·x₀, d²) on E_d, which avoids square roots. It scans the entire Hasse interval and accepts only a unique, directly verified solution; otherwise it falls back to PARI `Fl_elltrace`.
- In-run spot check: every 1000th fast value is recomputed with PARI, and the run aborts on any mismatch.

**Certified truncation (condition 1).**
- Deligne gives |aₙ| ≤ d(n)√n. The explicit Dirichlet divisor bound |Δ(x)| ≤ 0.961√x is Berkane–Bordellès–Ramaré 2012.
- Together these give tail(T) ≤ e^{−2πyT}·(1.922 + (log T + 1.2)/(2πy√T)). This is sharper than Wuthrich's Lemma 4, which uses |aₙ| ≤ n.
- λ(b/25) has error ≤ 2·tail + fp, with fp ≤ 300·2⁻⁶⁴·Σ_{n≤T} d(n)/√n.

| level | T | tail | certifies denominators < |
|---|---|---|---|
| T₁ | 7 682 510 690 | 3.506·10⁻⁶ | 10³ |
| T₂ (stricter repeat, condition 4) | 9 134 686 292 | 3.506·10⁻⁸ | 10⁵ |

**Two final evaluations (condition 3):**
- (a) the six symbols reconstructed from the S_k;
- (b) a separate direct accumulator of Σ (aₙ/n)e^{−2πny}·W(n mod 25), with W(k) = Σ_b coef_b·(cos 2πkb/25 + cos 2πk u_b/25).

**End-to-end check.** λ(0) = 2·Σ(aₙ/n)e^{−2πn/√N} = L(E,1) must vanish (rank 2).

## 2. Validation (condition 2) — all passed

| check | result |
|---|---|
| streamed [b/25]⁺, [b/5]⁺ vs Sage exact eclib: 37a1 (w = −1), 389a1, 446d1 | ratio exactly 1, all zeros agree, every value within 10⁻¹⁶ of a half-integer |
| 234446a1 (Wuthrich's rank-4 example), all 20 [b/25]⁺ | identical to BOTH eclib and Wuthrich's own Sage implementation: (−5, 8, 8, −7, −5, 6, 6, −8, −7, 4, 4, −7, −8, 6, 6, −5, −7, 8, 8, −5) |
| P₂ from streamed symbols vs Sage `padic_lseries(5).series(2)` | ours = 2 × Sage (a constant unit) on every coefficient for 37a1 and 389a1; both ≡ 0 for 446d1 (SW: T² coefficient 5 + 5² + …) |
| 234446a1, T⁴ coefficient of P₂ | ≡ 2 = 2·1 (mod 5), matching Wuthrich's "≡ 1 (mod 5)" up to the same factor 2 |
| L(E,1)-check on the rank ≥ 2 validation curves | about 10⁻¹⁷ |
| Wuthrich's printed "[1/27]⁺ = 1" for 234446a1 | a **slip in the paper**: eclib (exact) and his own implementation both give 0, as do we; his [1/7]⁻ = 1 and [1/7]⁺ = 0 agree with ours |
| fast counter vs PARI `Fl_elltrace`, seed curve | 0 mismatches and 0 fallbacks on 210 000 primes in 7 windows from 2·10⁶ to 1.3·10¹⁰; 3.0–3.4× faster |
| full pipeline, seed curve, T = 2·10⁸ | fast and PARI class sums **bit-identical**; 11 077 in-run spot checks passed; 4 workers vs 1 agree to 3·10⁻²⁰ |

## 3. Manin constant (tracked, not assumed; revised after operator review, 2026-09-18)

### 3.1 What the computed numbers are

Wuthrich's [r]⁺ = Re λ(r)/Ω⁺ uses λ(r) = 2πi∫_{i∞}^r f(z)dz, normalized by the newform, and Ω⁺, the least positive real period of E. Our x_b is exactly this for the seed model. It equals eclib's value on every validation curve.

Let φ: X₀(N) → E be the minimal-degree parametrization, with φ*ω_E = c_E · 2πi f(z)dz. Then c_E = c₀·u:
- c₀ is the Manin constant of the strong Weil curve E₀ in the 2-curve isogeny class.
- u = 1 if E = E₀.
- Otherwise the 2-isogeny ψ: E₀ → E satisfies ψ*ω_E = u·ω_{E₀}, and u·v = 2 with the dual, so u ∈ {1, 2}.

Also 5 ∤ c_E, because p | c₀ ⇒ p² | 4N (Mazur).

### 3.2 The lattice that is actually available

- gcd(25, N) = 1, so b/25 = γ(0) for some γ ∈ Γ₀(N). Also λ(0) = L(E,1) = 0, since the rank is 2.
- Hence λ(b/25) is the period of 2πi f dz over a closed loop on X₀(N).
- Pushing the loop forward: c_E·λ(b/25) = ∫_{φ∗loop} ω_E ∈ Λ_E.
- Λ_E is rectangular (Δ > 0; `E.omega[2]` is purely imaginary; checked in `runs/manin_threshold_output.txt`).

Therefore **c_E·x_b ∈ Z**. This is the unitary case of Wuthrich's Prop. 1 argument, with the Manin constant multiplying the symbol. The torsion factor drops out because φ(0) = O here.

### 3.3 Identification condition (sharpened)

- All 20 recovered values h_b are integers, with |x̃_b − h_b| ≤ 2.63·10⁻¹².
- The certified error at T₂ is |x_b − x̃_b| ≤ 2.5027·10⁻⁶.
- Since x_b − h_b ∈ (1/c_E)Z, we get x_b = h_b for all 20 b whenever **c_E ≤ 399 575**.
- Because c_E ≤ 2c₀, this holds whenever **c₀ ≤ 199 787**, with no assumption about which curve is optimal.
- At T₁ the corresponding bounds are c_E ≤ 3 999 and c₀ ≤ 1 999.

This replaces the earlier draft's "c_E < 5·10⁴". That figure came from the generic rounding criterion applied to the (1/(2c_E))Z lattice.

### 3.4 What is known about c₀

- c₀ ∈ Z (Edixhoven).
- p | c₀ ⇒ p² | 4N (Mazur). Also p | c₀ ⇒ p | N (Abbes–Ullmo).
- Since 4N = 2⁵·3·2243·4547²·5843, this gives **c₀ = 2^a·4547^b**.
- We know of no published bound on a or b. Česnavičius–Neururer–Saha give c₀ | deg φ, but deg φ cannot be computed at this conductor.

The hypothesis c₀ ≤ 199 787 therefore **fails exactly when 4547² | c₀, 2⁶·4547 | c₀, or 2¹⁸ | c₀**. Manin's conjecture (c₀ = 1) implies it.

Raising T only raises the threshold: each extra ~3.2·10⁸ terms buys about one factor of e. It can never remove the dependence, because b is unbounded in the published results.

### 3.5 The proposal to drop the condition via Wuthrich 2018, Prop. 1: checked and rejected

The proposal read the last sentence of the proof literally (line 230 of our text extraction of arXiv 1608.06423). That sentence puts c₀ in the denominator of the integrality expression, which would give [r]⁺ ∈ (c₀/2)Z ⊆ ½Z for the seed. The paper itself does not support this reading:

1. **The proof's own chain.** It shows that t₀c₀λ(r) lies in Λ_{E₀}, and that c₀t₀q^±[r]^± ∈ (c_∞/2)Z. So c₀ multiplies the symbol.
2. **The [r]⁻ bound in the same paragraph.** It gives [r]⁻ ∈ (1/(2c₀))Z, with c₀ in the denominator of the lattice.
3. **The remark after Prop. 1.** For semistable curves "without assuming c₀ = 1", it bounds the denominator of [r]⁺ by 4·#E(Q)_tors/c_∞(E). That is 2c₀·#tors/c_∞ with the then-known c₀ ≤ 2, which is impossible under the literal reading.
4. **Direct test on class 11a** (`validation/manin_direction_11a.gp`, with output). For E = 11a3:
   - c_E = 5. The lattice 5Λ(11a1) sits inside Λ(11a3) with index 5, while u = 1 fails.
   - #tors = 5, c_∞ = 1, and [0]⁺ = L(E,1)/Ω⁺ = 1/25.
   - The literal expression gives 2/5 (with c₀ = 1) or 2/25 (with c_E = 5); neither is an integer.
   - The corrected expression 2·#tors·c_E·[r]⁺/c_∞ gives 2 ∈ Z.
5. **Structure.** As r runs over the cusps Γ₀(N)-equivalent to 0, λ(r) − λ(0) runs over all of Λ_f = c₀⁻¹Λ_{E₀}, since Γ₀(N) → H₁(X₀(N), Z) is onto. If c₀ > 1, some unitary plus symbols really do have c₀ in their denominators.

Correct statement: **2·#E(Q)_tors·c_E·[r]⁺/c_∞(E) ∈ Z**, where c_E is the constant of the curve whose torsion and components appear.

Item 4 also shows that the *printed* unitary statement of Prop. 1 (under "c₀ = 1") fails for curves other than the strong Weil curve: [0]⁺(11a3) = 1/25 ∉ (1/10)Z. This is the second slip we have found in this paper, after [1/27]⁺ for 234446a1 (§2). A minor third: the introduction pairs the rectangular lattice with negative discriminant, which is reversed; the proof uses the correct pairing.

## 4. Results (seed run, 12 workers, T₂ = 9 134 686 292)

**[b/25]⁺ for b = 1…24 with 5 ∤ b.** Identical at T₁ and T₂. Integers, subject to §3.3.

| b | 1 | 2 | 3 | 4 | 6 | 7 | 8 | 9 | 11 | 12 | 13 | 14 | 16 | 17 | 18 | 19 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [b/25]⁺ | −54 | 16 | 90 | −52 | −76 | 16 | 76 | −52 | −54 | 90 | 90 | −54 | −52 | 76 | 16 | −76 | −52 | 90 | 16 | −54 |

**Evaluations of a₂:**

| check | result |
|---|---|
| (a) six reconstructed symbols (condition 3) | 3(16 + 90 − 52 − 54) + 4(−52 + 90) = 3·0 + 4·38 = **152 ≡ 2 (mod 5)** |
| (b) direct weighted accumulator (condition 3) | X_direct = 152.000000000006 at T₂; differs from the unrounded six-symbol combination by 6.6·10⁻¹⁸ |
| stricter repeat (condition 4) | T₁ (certified error 2.5·10⁻⁴) and T₂ (2.5·10⁻⁶) give identical integer vectors and the identical value 152 |
| (c) full P₂ from all 20 symbols (`runs/p2check.gp`) | uses α, the unit root (a₅ = −2, α ≡ 13 mod 25), Teichmüller representatives and γ = 6. T² coefficient ≡ **2** (mod 5); T⁰ = 0 and T¹ ≡ 0 (mod 5). This algebraically checks the six-symbol reduction on the same rounded values; it is not a further numerical evaluation. |
| L(E,1)-check | λ(0) = 2.9·10⁻¹⁴ at T₂ (should vanish) |

a₂ ≡ 2 (mod 5) in our normalization. Every other normalization in play differs from ours by a 5-adic unit: c_∞, c_E, u, and Sage's factor 2. So **a₂ ≢ 0 (mod 5)** in all of them.

**Streaming custody:**
- 417 388 618 primes q > R, all counted by the certified fast counter.
- 0 fallbacks; 417 382 in-run PARI spot checks, 0 mismatches; no FATAL.
- termsL + smooth = T₂ − 3 250 559. The loop skips the zero terms of primes q > R with a_q = 0 without counting them.

## 5. Resources (authorization: ≤ 20 threads, 12 GB, about 6 CPU-hours, 30 min wall)

| item | used | within? |
|---|---|---|
| threads | 12 | yes |
| memory | peak RSS 141.3 MB per worker, about 1.7 GB total | yes |
| CPU | 5.645 CPU-h (seed run) + 0.240 CPU-h (metered pipeline and validation runs), plus unmetered Sage/eclib reference runs and the 210k-prime counter test (minutes) | yes, about 5.9 |
| wall | 14:34:20Z → 15:07:44Z = **33.4 min** | **NO: exceeded the 30-min cap by 3.4 min (11%)**; the run was not stopped at 30 min |

The review-time checks (`p2check.gp`, `manin_threshold.gp`, `manin_direction_11a.gp`) took seconds each.

## 6. Conclusion

The chain uses only the merged gates plus this run:
1. rank E(Q) = 2 and E(Q)/5E(Q) = ⟨P₁, P₂⟩.
2. v₅(Reg_γ) = 0.
3. ord_T L₅ ≥ 2 (Kato).
4. a₂ ≢ 0 (mod 5), **if c₀ ≤ 199 787**.
5. Hence ord_T L₅(E,T) = 2, v₅(L₅*) = 0, b₅ = 0, and **Sha(E/Q)[5^∞] = 0**.

Step 5 uses SW Thm 6.1 and Kato's upper-bound direction only. It does not assume p-adic BSD and does not need Skinner–Urban.

**Status: CONDITIONAL on c₀ ≤ 199 787.** The condition fails only if 4547² | c₀, 2⁶·4547 | c₀ or 2¹⁸ | c₀. It holds under Manin's conjecture. The unconditional upgrade proposed via Wuthrich's Prop. 1 is not justified (§3.5).

## 7. Proposed ledger block (NOT merged; awaiting operator acceptance)

```
== STEIN_WUTHRICH_P5_LP_RUN_001 (2026-09-18) — seed (2243,12): certified streaming a_2 mod 5 ==
RESULT      a_2(L_5) ≡ 2 (mod 5) [≢ 0 in every 5-unit normalisation], CONDITIONAL ON c_0 ≤ 199787.
            20 symbols [b/25]^+ recovered as integers; six-symbol combination = 152.
            Checks: direct weighted accumulator 152.000000000006; T1/T2 repeat identical;
            full 20-symbol P_2 gives T^2 coefficient ≡ 2; L(E,1)-check 2.9e-14.
            Validation: 37a1, 389a1, 446d1, 234446a1 (all 20 [b/25]^+ = eclib = Wuthrich's implementation).
CONSEQUENCE Kato + Stein–Wuthrich Thm 6.1 upper-bound direction only; no p-adic BSD; no Skinner–Urban:
            IF c_0 ≤ 199787 THEN ord_T L_5(E,T) = 2, v_5(L_5^*) = 0, b_5 = 0, Sha(E/Q)[5^∞] = 0.
STATUS      SMALL_SEED_2243_12_SHA5 = ZERO_CONDITIONAL_ON_MANIN_BOUND
            c_0 = Manin constant of the strong Weil curve (2-curve class) = 2^a·4547^b by published theorems.
            The condition fails only if 4547^2 | c_0, 2^6·4547 | c_0 or 2^18 | c_0; Manin's conjecture implies it.
NOT CLAIMED Unconditional Sha[5^∞] = 0. The removal via Wuthrich 2018 Prop. 1 was checked and REJECTED:
            the proof's last line misplaces c_0. For 11a3, c_E = 5 and [0]^+ = 1/25 refute the literal reading.
            Correct form: 2·#E(Q)_tors·c_E·[r]^+/c_∞(E) ∈ Z.
RESOURCES   12 threads, 1.7 GB, ≈5.9 CPU-h. Wall 33.4 min: EXCEEDED the 30-min authorization by 3.4 min.
FILES       ~/BSD_SW_LP5_STREAMING_2026-09-18 (MANIFEST.sha256)
```

## 8. Files

- `src/`
  - `swstream.c`: streaming core.
  - `fastap.c`: certified counter. `fastap_stub.c` is the PARI-only build.
  - `symbols.gp`: symbols from the class sums.
  - `pari/`: symlinks to the PARI 2.17.4 headers of the H41 build. They are external and not hashed; the binaries `swstream` and `swstream_pari` are hashed.
- `validation/`
  - `certT.gp`: certified truncation.
  - Reference comparisons: `run_valid.sh`, `sage_ref.sage`, `sage_234446.sage`, `compare.gp`, `w234.gp`, `ours_234446.gp`, and `out_*`.
  - `manin_direction_11a.gp`, with its output.
- `runs/`
  - Setup and run: `seed_params.gp`, `seed_weights.txt`, `seed_run.sh`, `seed_run.log`.
  - Worker outputs: `seed_w*.txt` and `seed_w*.err`.
  - Evaluation: `seed_eval.gp` and `seed_eval_output.txt`; `p2check.gp` and `p2check_output.txt`; `manin_threshold.gp` and `manin_threshold_output.txt`; `isog.gp`.
  - Tests: `pipe_*` and `fastap_test_210k.txt`.

## Addendum (operator review, 2026-09-18): 4547 ∤ c₀. This addendum governs §3.4, §6 and §7.

- **Operator correction, verified** in `~/BSD_MANIN_4547_EDIXHOVEN_CHECK_2026-09-18/00_REPORT.md`.
  - Edixhoven [Edi91, Thm 3], as stated in CNS (arXiv:1911.09446v3, §1) and Česnavičius (arXiv:1703.02951, §1.2): for the optimal quotient and p ≥ 11, if E over Q_p does not have *potentially ordinary* reduction of type II, III or IV, then ord_p(c) = 0.
  - Both curves of the class have type III at 4547, v(j) = 0 and j ≡ 1728 (mod 4547). Since 4547 ≡ 3 (mod 4), the potentially good reduction is supersingular. Hence ord₄₅₄₇(c₀) = 0.
  - The primary source was not read; it is paywalled.
- **Consequence.** c₀ = 2^a, and the condition c₀ ≤ 199 787 of §3.3 is equivalent to **a ≤ 17**. If the seed is the strong Weil curve, a ≤ 18 suffices. The failure alternatives 4547² | c₀ and 2⁶·4547 | c₀ are gone; only **2¹⁸ | c₀** remains.
- **Revised status:** `SMALL_SEED_2243_12_SHA5 = ZERO_CONDITIONAL_ON_V2_C0_LE_17`. If v₂(c₀) ≤ 17, then:
  - ord_T L₅ = 2
  - v₅(L₅*) = 0
  - b₅ = 0
  - Sha(E/Q)[5^∞] = 0

  This uses Kato and SW Thm 6.1 only.
- **2-adic literature.** Nothing closes the 2-part:
  - CNS Thm 1.2 gives only v₂(c₀) ≤ v₂(deg φ₀), because N has primes ≡ 3 (mod 4). deg φ₀ is not computable here.
  - Raynaud's 4 | c ⇒ 4 | N is vacuous.
  - Edixhoven's 2-adic bounds are unpublished.
  - Manin's conjecture is not assumed.
