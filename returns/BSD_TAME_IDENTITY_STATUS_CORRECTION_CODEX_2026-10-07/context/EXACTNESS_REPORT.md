# Tame-law exactness test — REPORT

Claude (Opus 5.5), 2026-10-07. Bounded discovery experiment. Total compute ≈ 4 CPU-minutes, one process at a time.
No pushes, messages, Codex/Aristotle submissions or paid compute.

## Verdict: **RIGID**

Every tested depth and every tested level matches, on all six curves:

- **Sealed rows.** All 275 sealed (curve, ℓ, q^e) rows where the regulator is defined satisfy C₂ ≡ K_E·(a_ℓ−2)·R_ℓ (mod q^e).
  - 231 of them predict a nonzero residue mod q. All 231 match.
  - θ_ℓ ∈ I² holds at all 338 sealed odd prime powers.
- **Depth.** All 104 clean depth rows match: w ≡ K_E (mod p^k) for p = 5, 7, 11, 13, 17, with k = 2 at all six curves and k = 3 at four of them.
  - 10 of these 104 rows repeat lane PK's earlier 389a1, p = 5 auxiliaries. The other 94 are new.
- **Full odd level.** The identity also holds at every q outside the record's eligibility set (Hyp 2.2) where the regulator is defined: 110 of 110 rows.
  - This covers q = 3 up to 3⁶, anomalous q, q | N, and q | #E_ns(F_r).
- **2-part (exploratory, not sealed).** The formula was fixed in RESUME.md before the computation. In G⁺ = (ℤ/ℓ)^×/±1 it matches on 13 of 13 testable rows of 389a1 and 433a1.
  - 6 of the 13 have a nonzero prediction, up to 2⁵.
- **Kill test (fixed in advance).** Not triggered: no clean row has w ≢ K_E (mod p²).

**Endpoint check (written before any computation): no FIN effect.**
- This decides the TYPE of the missing object MI-1, not its construction.
- FIN, ORDER9 and Q36 are unchanged. Nothing here concerns the seed.

## 1. Law and conventions (record normalization, unchanged)

- **The law.** w(p,ℓ) = c₂/((a_ℓ−2)·R(p,ℓ)) ≡ K_E (mod p), with K_E = 4·c∞·#Ш_an·Tam/#tors².
- **Conventions.** These are from the K288 audit §1 and lane NORM:
  - g is the least primitive root mod ℓ.
  - [a/ℓ]⁺ = Re λ(a/ℓ)/ω₁.
  - c_k = Σ_a C(ind_g a, k)·[a/ℓ]⁺. Here the FULL index in [0, ℓ−2] is used. For odd q this reduces correctly mod q^e: C(i + q^e t, 2) ≡ C(i, 2).
  - h(Q) = ind_g(−a/b mod ℓ) for Q = (a/d², b/d³) ≡ O mod ℓ with Q ∈ E⁰ at all bad primes.
  - R = det[[h₁, b₁₂], [b₁₂, h₂]] with b₁₂ = (h(Q₁+Q₂) − h₁ − h₂)/2, transported to the basis P₁, P₂ of E(ℚ)/tors.
- **What was tested.** At each odd prime power q^e ∥ ℓ−1, the multiplicative form C₂ ≡ K_E(a_ℓ−2)R_ℓ (mod q^e).
  - This makes sense even when R_ℓ is not a unit.
  - Because I²/I³ of ℤ[(ℤ/ℓ)^×] is cyclic of order ℓ−1, the conjunction over all q^e ∥ ℓ−1 IS the full-level identity in I²/I³ (test B).
  - Depth p^k (test A) is the q = p component at ℓ ≡ 1 (mod p^k).
- **One new device: the regulator via a lattice.**
  - Q₁ and Q₂ form an LLL-reduced basis of L = ker(ℤ² → E(F_ℓ)) on P′ = cexp·P. This replaces M·P.
  - So R = det H(Q)/(cexp²·[ℤ²:L])². It is defined for q ∤ cexp·[ℤ²:L].
  - Heights grow like ℓ instead of ℓ², so ℓ ≤ 4000 is cheap.
- **K_E per curve.** All six curves are rank 2 = analytic rank 2 in Cremona's curvedata.

| curve | c∞ | Tam | tors | Ш_an | K_E | eligible p used for depth |
|---|---|---|---|---|---|---|
| 389a1 | 2 | 1 | 1 | 1 | 8 | 5, 7, 11, 13, 17 |
| 433a1 | 1 | 1 | 1 | 1 | 4 | 7, 11, 13, 17 |
| 664a1 | 1 | 4 | 1 | 1 | 16 | 11, 13, 17 |
| 655a1 | 1 | 2 | 1 | 1 | 8 | 7, 11, 17 |
| 1615a1 | 2 | 8 | 2 | 1 | 16 | 7, 11, 13 |
| 194040co6 | 2 | 4 | 2 | 4 | 32 | 13, 17 |

## 2. Design and custody

- **Row rule.** The rule is fixed in the header of `scripts/s1_select_reg.gp`, before any symbol was computed.
  - (A) Rows use p ∈ {5, 7, 11, 13, 17} where p is eligible: all five lane-NORM pcheck flags hold.
    - ℓ ≤ 4000 is prime, v_p(ℓ−1) ≥ 2, ℓ ∤ N and p ∤ #E(F_ℓ).
  - (B) Rows use every ℓ of (A), plus the primes ℓ ≤ 1500 with v₃(ℓ−1) ≥ 3, plus lane 7's 17 saved co6 auxiliaries.
  - A clean depth row also needs R a p-unit and the quadratic checks to pass.
- **Seal 1, 11:27.** File `predictions/predictions.json`, sha256 `53643a10…8c50dc`. It has 332 rows: R_ℓ, the predicted C₂ mod q^e and the predicted w.
  - It was written after the regulators and before any modular symbol.
- **Seal 2, 11:31.** File `supp_co6.json`, sha256 `354414ab…d7d39f`. It covers co6 at ℓ = 2029, 3719 (p = 13) and 3469 (p = 17).
  - The co6 extension was pre-registered in RESUME at 11:28: ℓ = 2029 runs if ℓ = 677 takes less than 4 min. It took 14 s.
  - The rest of the small-curve rule was then applied to co6 on cost grounds alone, before any evaluation.
  - The first write of seal 2 carried a wrong time stamp (11:36). It was regenerated at 11:31, before any symbol.
- **Custody.**
  - The ordering is custodian-attested only. The same session sealed and computed, as in the K288 audit.
  - `evaluate.py` refuses to run if either seal hash changed.
  - c₀, c₁ and c₂ were recomputed in Python from the saved symbol vectors. They agree with the gp sums on all 171 vectors that have both.

## 3. Normalization checks (all pass)

- **Symbol normalization (kap).** kap = 1 on all five msfromell curves. The Birch ratio τ(χ)L(E,χ̄,1)/(ω₁Σχ(a)[a/ℓ₀]) equals 1 to within 10⁻⁵⁷ at 6 characters per curve (`s2_sym.out`).
- **Regulator, 389a1 (`x0_regcheck.out`).** The lattice regulator equals the record's M·P regulator on every common odd modulus: 8 values of ℓ, two bases.
  - It reproduces lane PK's R^(2) = 22, 21, 1, 17 (mod 25) at ℓ = 101, 151, 401, 601.
- **Regulator, cexp > 1 or torsion (`x0b_regcheck.out`).** The same equality holds on 664a1, 1615a1 and 194040co6: 13 of 13.
  - It reproduces lane 7's co6 level-1 rows (R, C₂, w) exactly at ℓ = 53, 79, 131, 157, 313.
- **Quadratic form.** h is quadratic mod the odd part of ℓ−1 (parallelogram, h(2Q) = 4h(Q)) on every row.
  - Mod 2 it is quadratic only modulo (ℓ−1)/2, because h(−Q) = h(Q) + ind(−1). This is why q = 2 is handled in G⁺ (§4C).
- **Euler factor.** a_ℓ − 2 ≡ −#E(F_ℓ) (mod q^e) is exact on every row.
- **194040co6 symbols.** These come from Birch inversion (lane 7's route, re-typed here).
  - The same code reproduces 389a1's exact msfromell symbols at ℓ = 101, to 2·10⁻⁵⁶ at 50 digits and 10⁻³⁶ at 30 digits. The t-independence check gives 10⁻⁵⁶.
  - The co6 values were identified in 8ℤ, using lane 7's denominator bound, with error at most 9.6·10⁻³⁵ (margin ≥ 4·10³⁴).
  - 17 of the co6 ℓ use lane 7's saved exact symbols.

## 4. Results (full tables: `outputs/EVAL_TABLES.md`; machine-readable: `outputs/evaluation.json`)

### (A) Depth: clean rows, w = C₂/((a_ℓ−2)R) mod p^e

| curve | p^e tested (rows) | clean rows | match |
|---|---|---|---|
| 389a1 | 5² (18), 5³ (3), 7² (11), 7³ (1), 11² (4), 11³ (1), 13² (2), 17² (1) | 41 | 41 |
| 433a1 | 7² (9), 7³ (1), 11² (5), 13² (3), 17² (1) | 19 | 19 |
| 664a1 | 11² (5), 11³ (1), 13² (3), 17² (1) | 10 | 10 |
| 655a1 | 7² (9), 11² (4), 11³ (1), 17² (1) | 15 | 15 |
| 1615a1 | 7² (9), 11² (2), 11³ (1), 13² (3) | 15 | 15 |
| 194040co6 | 13² (3), 17² (1) | 4 | 4 |

- **Depth-3 rows.** All have w = K_E mod p³:
  - 389a1 at 5³ (ℓ = 2251, 3001, 3251), 7³ (ℓ = 1373) and 11³ (ℓ = 2663);
  - 433a1 at 7³ (ℓ = 1373);
  - 664a1, 655a1 and 1615a1 at 11³ (ℓ = 2663).
- **194040co6 (Ш = 4).** w = 32 mod 169 at ℓ = 677, 2029, 3719, and w = 32 mod 289 at ℓ = 3469.
- **Controls on all 104 clean rows.**
  - (G) Mismatched generator g′ = g^s gives w′ = s⁻²K_E ≠ K_E on 104 of 104.
  - (L) Reading the level-1 jets naively mod p^e hits K_E on 13 of 104. Chance would give Σ1/p ≈ 13.5. So the depth agreement is not automatic.

### (B) Full odd level: every sealed (curve, ℓ, q^e), by class of q

| curve | eligible q: match / defined | q outside Hyp 2.2: match / defined (q values, max e) | undefined (q ∣ cexp·index) |
|---|---|---|---|
| 389a1 | 70/70 | 19/19 (3⁶) | 17 |
| 433a1 | 26/26 | 15/15 (3⁶; 5 anomalous) | 12 |
| 664a1 | 12/12 | 16/16 (3⁶; 5 anomalous; 7 ∣ #E_ns) | 9 |
| 655a1 | 23/23 | 23/23 (3⁶; 5 ∣ N; 13 ∣ #E_ns) | 7 |
| 1615a1 | 23/23 | 15/15 (3⁴; 5, 17 ∣ N) | 13 |
| 194040co6 | 21/21 | 12/12 (3², 5, 7, 11 ∣ N) | 5 |

- **Strongest rows.** The deepest nonzero-prediction matches are at q = 3 (never eligible) with ℓ = 1459, where ℓ − 1 = 2·3⁶:
  - 433a1: C₂ = 266 = prediction (mod 729), w = 4.
  - 664a1: 417 = 417.
  - 389a1: 312 = 312, with v₃(R) = 1.
  - 655a1: 402 = 402.
- **Undefined rows.** On these 63 rows only θ ∈ I² was tested; it holds on all of them.

### (C) 2-part, exploratory (in G⁺ = (ℤ/ℓ)^×/±1, n⁺ = (ℓ−1)/2; not sealed)

- **Coordinates.** A_k = Σ_{j<n⁺} 2x_j C(j, k), with x_j = [g^j/ℓ]⁺. Then C₂⁺ = A₂ − (A₁/n⁺)·C(n⁺, 2) mod n⁺.
- **Prediction.** At 2^f ∥ n⁺: C₂⁺ ≡ (K_E/4)(a_ℓ−2)·(4h₁h₂ − (h₁₂−h₁−h₂)²)/(cexp²·idx)².
- **Scope.** It is testable only where cexp·idx is odd, which here means 389a1 and 433a1 only.
- **Result.** 13 of 13 match. The 6 rows with a nonzero prediction:
  - 389a1 at ℓ = 1601 (2⁵: 10 = 10) and ℓ = 3137 (2⁵: 2 = 2);
  - 433a1 at ℓ = 197, 541, 1373 (2¹) and ℓ = 1297 (2³).
- **Sanity check.** The same C₂⁺ reproduces the sealed odd-part residues on 86 of 86 rows.
- **Grade.** This is evidence only. It is unsealed, covers two curves, and the 2-adic normalization of the Mazur–Tate element is convention-laden. Llerena-Córdova (2024) found that the stated conjectures fail at ℓ ∣ #E(ℚ)_tors.

## 5. Kill test and verdict

- **Kill test (fixed in advance).** MOD_P_ONLY if w ≢ K_E (mod p²) at clean (p, ℓ) on two or more curves.
  - Observed: zero mismatches in 104 clean rows on six curves, at p² and at p³.
- **Verdict rule.** "If every tested depth and level matches, record RIGID."
  - Every depth (A) matches, every odd level (B) matches, and the exploratory 2-part (C) matches.
  - **Verdict: RIGID.**

## 6. What this says about the missing object (MI-1)

1. **The mod-p law is the shadow of an integral identity at each tame level.**
   - On these curves the depth-2 part of θ_ℓ equals K_E·(a_ℓ−2)·R_ℓ as an element of I²/I³ ≅ ℤ/(ℓ−1).
   - This holds on its odd part wherever R_ℓ is defined, and, exploratorily, on the 2-part in G⁺.
   - Lane PK's p-adic scalar w_p^∞ ∈ ℤ_p (Theorem W^(k)) equals the rational K_E to every tested depth, up to p³.
   - The cross-p uniformity, one α for all p, is therefore what a level-by-level identity would give automatically. One identity at level ℓ fixes the residue at every q | ℓ−1 at once, small and bad q included.
2. **The type of object to build is characteristic-0 or integral.**
   - Concretely: a rank-2 identity θ̃_ℓ = (#Ш·Tam/#tors²)·(normalization)·(a_ℓ−2)·R_ℓ in I²/I³. This is the Mazur–Tate refined conjecture at tame level.
   - A mod-p-only mechanism is the wrong target. It would leave the p², p³, 3⁶ and full-level agreement unexplained.
3. **The identity does not use the record's per-p hypotheses.**
   - It holds at q = 3, anomalous q, q | N and q | #E_ns(F_r).
   - So the object is one global statement per ℓ, not a family of p-adic statements gated by Hyp 2.2.
   - In rank 1, the analogous object is Darmon's refined conjecture for Heegner points (Invent. Math. 1992), fed by Gross–Zagier. In rank 2, no such source is known.
4. **For the seed** (K_E = 288 = 32·9), RIGID predicts w ≡ 288 (mod p^k) at every tame level, not just mod p.
   - Testing that needs seed singleton runs at ℓ ≡ 1 (mod p²). That is seed-size compute and out of scope here.

## 7. What this does not show

- **No proof.** There is no proof and nothing about the seed. FIN, ORDER9 and Q36 are unchanged.
- **Odd #Ш is untested.** The seed has Ш = 9. Lane 7's scan found that every rank-2 curve with Ш_an ≠ 1 at N < 500k has Ш_an = 4.
  - The Ш factor was tested only as the unit 4 at p = 13, 17, to depth 2.
- **Manin constant c ≠ 1 is untested.** All six curves have c = 1.
- **q | cexp·[ℤ²:L].** Here the lattice regulator is undefined (63 rows); only θ ∈ I² was tested.
- **q = 2.** Not sealed. It was tested only on cexp = 1 curves.
- **194040co6 symbols are numerical identifications,** with margin ≥ 4·10³⁴, resting on lane 7's 8ℤ bound. They are not exact modular symbols.
- **Same-session, unreviewed.** Independent replay is the natural Codex check (§9 commands).

## 8. Literature: prior numerical tests (no novelty claim)

- **Mazur & Tate 1987.** B. Mazur, J. Tate, "Refined conjectures of the 'Birch and Swinnerton-Dyer type'", Duke Math. J. 54 (1987), no. 2, 711–750.
  - Per Portillo-Bobadilla, their own numerical evidence was for 37A and 43A (rank 1), with S = {q} a single prime of non-split multiplicative reduction.
  - I did not read the 1987 paper itself.
- **Portillo-Bobadilla 2019.** F. X. Portillo-Bobadilla, "Experimental evidence on a refined conjecture of the BSD type", Bol. Soc. Mat. Mex. (3), 2019, doi:10.1007/s40590-018-0216-8, arXiv:1709.01204.
  - Tests MT Conjecture 4 (leading term, canonical-height regulator) in RANK 1 only: the first 3000 Cremona rank-1 curves with Ш = 1, 20 curves with Ш = 4 and 7 with Ш = 9.
  - S consists of primes < 300, tested multiplicatively in G_M = (∏F_p^×)/±1. That is a full-level test in rank 1.
- **Llerena-Córdova 2024.** J.-P. Llerena-Córdova, "Numerical study of refined conjectures of the BSD type", arXiv:2412.17703 (2024).
  - Tests MT Conjectures 4–6 at M = p split multiplicative: 425,713 pairs (E, p).
  - Found failures exactly at ℓ | #E(ℚ)_tors, and repaired them by inverting #tors.
  - No tame-level rank-2 leading-term test was found in what I read (summary of the HTML).
- **Theory, no numerics on this point:**
  - K. Ota, Amer. J. Math. 140 (2018) 495–542, and Ann. Inst. Fourier 73 (2023) 1319–1364: the rank part (order of vanishing).
  - Burns–Kurihara–Sano, J. Math. Soc. Japan 76 (2024) (arXiv:1910.07404) and arXiv:2103.11535 (2021).
  - D. Bullach, M. Honnor, arXiv:2511.07203 (2025): order of vanishing and a weak main conjecture for p-parts. Their leading-term result is trivial in positive rank (their Rem. 1.8(b)).
  - Darmon, Invent. Math. 110 (1992): the Heegner-point analogue.
- **Bottom line.** In these sources I found no published numerical test of the rank-2 leading-coefficient identity at tame level ℓ, at depth p^k or at full level.
  - The search was bounded: 6 web searches and 8 page fetches, reading abstracts, introductions and machine summaries. It is not a survey, and this is not a claim of novelty.

## 9. Files, hashes, replay

- **Scripts.**
  - `lib_tl.gp`: conventions and the lattice regulator.
  - `x0_regcheck.gp` and `x0b_regcheck.gp`: normalization checks.
  - `s1_select_reg.gp` and `s1b_co6_reg.gp`: row rule and regulators.
  - `seal.py` and `seal_supp.py`: the seals.
  - `s2_sym.gp`: exact symbols for five curves.
  - `s3_co6.gp`, `s3b_co6_common.gp` and `s3b_l*.gp`: co6 symbols.
  - `evaluate.py`, `twopart.py` and `tables.py`.
- **Outputs.** `outputs/*.out`, `symbols/` (171 vectors), `evaluation.json`, `twopart.json`, `EVAL_TABLES.md`, and `qclass.out` (pcheck flags of every q).
- **Hashes.** Every sha256 is in `MANIFEST.sha256`.
- **Replay.** Run from `scripts/`, with GP = run040 sage-env gp 2.17.3 and `-q -D nbthreads=1 -D parisizemax=8000000000 … < /dev/null`.
  - Steps: `x0_regcheck`, `x0b_regcheck`, `s1_select_reg`, then `python3 seal.py`. The seal is fixed, so compare the hashes rather than overwrite them.
  - Then `s2_sym`, `s3_co6`, `s1b_co6_reg`, `seal_supp.py`, `s3b_l2029/3719/3469`, `evaluate.py`, `twopart.py` and `tables.py`.
  - Wall time is about 4 min in total.
- **Resources.** About 250 CPU-seconds in total. The largest job was co6 at ℓ = 3719: 73 s and about 1 GB.

## Appendix — Table A in full (every clean depth row; generated by scripts/tables.py)

Columns: R, C₂, w and the controls are residues mod p^e. "naive level-1 lift" = C₂ from ind mod p read mod p^e (control L); "mismatched gen." = w with g′ = g^s in the symbols only (control G, expected s⁻²K_E).

| curve | K_E | p^e | l | a_l | #E(F_l) | R | C2 | w | K_E mod p^e | naive level-1 lift | mismatched gen. (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 389a1 | 8 | 5^2 | 101 | -4 | 106 | 22 | 19 | **8** | 8 | 23 | 12 (3) |
| 389a1 | 8 | 5^2 | 151 | -10 | 162 | 21 | 9 | **8** | 8 | 23 | 17 (7) |
| 389a1 | 8 | 5^2 | 401 | -22 | 424 | 1 | 8 | **8** | 8 | 23 | 12 (3) |
| 389a1 | 8 | 5^2 | 601 | -40 | 642 | 17 | 13 | **8** | 8 | 13 | 17 (7) |
| 389a1 | 8 | 5^2 | 701 | 34 | 668 | 3 | 18 | **8** | 8 | 13 | 12 (3) |
| 389a1 | 8 | 5^2 | 1051 | 64 | 988 | 24 | 4 | **8** | 8 | 18 | 7 (13) |
| 389a1 | 8 | 5^2 | 1151 | -36 | 1188 | 13 | 23 | **8** | 8 | 23 | 12 (3) |
| 389a1 | 8 | 5^2 | 1201 | 50 | 1152 | 22 | 23 | **8** | 8 | 3 | 17 (7) |
| 389a1 | 8 | 5^2 | 1301 | -44 | 1346 | 21 | 22 | **8** | 8 | 23 | 12 (3) |
| 389a1 | 8 | 5^2 | 1451 | -10 | 1462 | 9 | 11 | **8** | 8 | 3 | 12 (3) |
| 389a1 | 8 | 5^2 | 1601 | -75 | 1677 | 13 | 17 | **8** | 8 | 8 | 12 (3) |
| 389a1 | 8 | 5^2 | 1801 | -27 | 1829 | 14 | 2 | **8** | 8 | 23 | 17 (7) |
| 389a1 | 8 | 5^2 | 1901 | 14 | 1888 | 23 | 8 | **8** | 8 | 23 | 12 (3) |
| 389a1 | 8 | 5^3 | 2251 | -52 | 2304 | 123 | 114 | **8** | 8 | 123 | 92 (7) |
| 389a1 | 8 | 5^2 | 2551 | 4 | 2548 | 9 | 19 | **8** | 8 | 23 | 17 (7) |
| 389a1 | 8 | 5^2 | 2801 | 66 | 2736 | 12 | 19 | **8** | 8 | 8 | 12 (3) |
| 389a1 | 8 | 5^3 | 3001 | -22 | 3024 | 54 | 7 | **8** | 8 | 98 | 92 (7) |
| 389a1 | 8 | 5^3 | 3251 | -82 | 3334 | 61 | 8 | **8** | 8 | 123 | 112 (3) |
| 389a1 | 8 | 5^2 | 3301 | -62 | 3364 | 22 | 11 | **8** | 8 | 13 | 17 (7) |
| 389a1 | 8 | 5^2 | 3701 | -92 | 3794 | 21 | 8 | **8** | 8 | 8 | 12 (3) |
| 389a1 | 8 | 5^2 | 3851 | 74 | 3778 | 14 | 14 | **8** | 8 | 8 | 12 (3) |
| 389a1 | 8 | 7^2 | 197 | 8 | 190 | 5 | 44 | **8** | 8 | 43 | 39 (3) |
| 389a1 | 8 | 7^2 | 491 | -27 | 519 | 6 | 29 | **8** | 8 | 1 | 39 (3) |
| 389a1 | 8 | 7^2 | 883 | -50 | 934 | 36 | 18 | **8** | 8 | 36 | 16 (5) |
| 389a1 | 8 | 7^3 | 1373 | -1 | 1375 | 289 | 267 | **8** | 8 | 288 | 39 (3) |
| 389a1 | 8 | 7^2 | 1471 | -31 | 1503 | 44 | 46 | **8** | 8 | 8 | 11 (11) |
| 389a1 | 8 | 7^2 | 1667 | 19 | 1649 | 40 | 1 | **8** | 8 | 43 | 39 (3) |
| 389a1 | 8 | 7^2 | 2549 | -90 | 2640 | 45 | 4 | **8** | 8 | 43 | 39 (3) |
| 389a1 | 8 | 7^2 | 2647 | 35 | 2613 | 27 | 23 | **8** | 8 | 1 | 16 (5) |
| 389a1 | 8 | 7^2 | 2843 | 48 | 2796 | 19 | 34 | **8** | 8 | 43 | 39 (3) |
| 389a1 | 8 | 7^2 | 3137 | 97 | 3041 | 15 | 32 | **8** | 8 | 36 | 39 (3) |
| 389a1 | 8 | 7^2 | 3529 | -34 | 3564 | 19 | 16 | **8** | 8 | 29 | 16 (5) |
| 389a1 | 8 | 7^2 | 3823 | -48 | 3872 | 8 | 34 | **8** | 8 | 1 | 16 (5) |
| 389a1 | 8 | 11^2 | 727 | -26 | 754 | 71 | 68 | **8** | 8 | 52 | 10 (5) |
| 389a1 | 8 | 11^2 | 1453 | 44 | 1410 | 54 | 115 | **8** | 8 | 74 | 10 (5) |
| 389a1 | 8 | 11^2 | 2179 | 50 | 2130 | 40 | 114 | **8** | 8 | 52 | 10 (5) |
| 389a1 | 8 | 11^3 | 2663 | -82 | 2746 | 27 | 490 | **8** | 8 | 1196 | 1184 (3) |
| 389a1 | 8 | 11^2 | 3631 | 22 | 3610 | 107 | 59 | **8** | 8 | 52 | 94 (7) |
| 389a1 | 8 | 13^2 | 677 | 22 | 656 | 56 | 3 | **8** | 8 | 73 | 76 (3) |
| 389a1 | 8 | 13^2 | 3719 | 3 | 3717 | 106 | 3 | **8** | 8 | 47 | 76 (3) |
| 389a1 | 8 | 17^2 | 3469 | 66 | 3404 | 82 | 79 | **8** | 8 | 25 | 35 (5) |
| 433a1 | 4 | 7^2 | 197 | -9 | 207 | 33 | 18 | **4** | 4 | 25 | 44 (3) |
| 433a1 | 4 | 7^2 | 491 | 20 | 472 | 23 | 39 | **4** | 4 | 18 | 44 (3) |
| 433a1 | 4 | 7^2 | 883 | 26 | 858 | 11 | 27 | **4** | 4 | 39 | 8 (5) |
| 433a1 | 4 | 7^3 | 1373 | 63 | 1311 | 59 | 333 | **4** | 4 | 333 | 191 (3) |
| 433a1 | 4 | 7^2 | 1471 | 57 | 1415 | 45 | 2 | **4** | 4 | 32 | 30 (11) |
| 433a1 | 4 | 7^2 | 1667 | 57 | 1611 | 43 | 3 | **4** | 4 | 25 | 44 (3) |
| 433a1 | 4 | 7^2 | 2549 | -30 | 2580 | 2 | 38 | **4** | 4 | 25 | 44 (3) |
| 433a1 | 4 | 7^2 | 2647 | 22 | 2626 | 12 | 29 | **4** | 4 | 4 | 8 (5) |
| 433a1 | 4 | 7^2 | 3137 | -42 | 3180 | 27 | 1 | **4** | 4 | 18 | 44 (3) |
| 433a1 | 4 | 7^2 | 3529 | -46 | 3576 | 20 | 31 | **4** | 4 | 25 | 8 (5) |
| 433a1 | 4 | 11^2 | 727 | -8 | 736 | 109 | 117 | **4** | 4 | 37 | 5 (5) |
| 433a1 | 4 | 11^2 | 1453 | -6 | 1460 | 102 | 3 | **4** | 4 | 92 | 5 (5) |
| 433a1 | 4 | 11^2 | 2179 | -52 | 2232 | 7 | 61 | **4** | 4 | 70 | 5 (5) |
| 433a1 | 4 | 11^2 | 3389 | 25 | 3365 | 78 | 37 | **4** | 4 | 70 | 108 (3) |
| 433a1 | 4 | 11^2 | 3631 | 62 | 3570 | 18 | 85 | **4** | 4 | 26 | 47 (7) |
| 433a1 | 4 | 13^2 | 677 | 12 | 666 | 41 | 119 | **4** | 4 | 95 | 38 (3) |
| 433a1 | 4 | 13^2 | 2029 | 1 | 2029 | 140 | 116 | **4** | 4 | 108 | 61 (5) |
| 433a1 | 4 | 13^2 | 3719 | 49 | 3671 | 69 | 128 | **4** | 4 | 95 | 38 (3) |
| 433a1 | 4 | 17^2 | 3469 | -16 | 3486 | 174 | 188 | **4** | 4 | 89 | 162 (5) |
| 664a1 | 16 | 11^2 | 727 | -23 | 751 | 85 | 1 | **16** | 16 | 16 | 20 (5) |
| 664a1 | 16 | 11^2 | 1453 | -62 | 1516 | 72 | 82 | **16** | 16 | 27 | 20 (5) |
| 664a1 | 16 | 11^2 | 2179 | -45 | 2225 | 81 | 72 | **16** | 16 | 60 | 20 (5) |
| 664a1 | 16 | 11^3 | 2663 | 89 | 2575 | 690 | 829 | **16** | 16 | 1160 | 1037 (3) |
| 664a1 | 16 | 11^2 | 3389 | 27 | 3363 | 28 | 68 | **16** | 16 | 60 | 69 (3) |
| 664a1 | 16 | 11^2 | 3631 | -96 | 3728 | 32 | 39 | **16** | 16 | 27 | 67 (7) |
| 664a1 | 16 | 13^2 | 677 | -22 | 700 | 33 | 3 | **16** | 16 | 133 | 152 (3) |
| 664a1 | 16 | 13^2 | 2029 | -13 | 2043 | 155 | 149 | **16** | 16 | 68 | 75 (5) |
| 664a1 | 16 | 13^2 | 3719 | 66 | 3654 | 4 | 40 | **16** | 16 | 133 | 152 (3) |
| 664a1 | 16 | 17^2 | 3469 | -40 | 3510 | 159 | 82 | **16** | 16 | 50 | 70 (5) |
| 655a1 | 8 | 7^2 | 197 | -2 | 200 | 6 | 4 | **8** | 8 | 1 | 39 (3) |
| 655a1 | 8 | 7^2 | 491 | -42 | 534 | 23 | 38 | **8** | 8 | 43 | 39 (3) |
| 655a1 | 8 | 7^2 | 883 | -30 | 914 | 40 | 1 | **8** | 8 | 29 | 16 (5) |
| 655a1 | 8 | 7^2 | 1471 | 24 | 1448 | 4 | 18 | **8** | 8 | 43 | 11 (11) |
| 655a1 | 8 | 7^2 | 1667 | -52 | 1720 | 22 | 2 | **8** | 8 | 29 | 39 (3) |
| 655a1 | 8 | 7^2 | 2549 | 6 | 2544 | 32 | 44 | **8** | 8 | 8 | 39 (3) |
| 655a1 | 8 | 7^2 | 3137 | -48 | 3186 | 31 | 46 | **8** | 8 | 36 | 39 (3) |
| 655a1 | 8 | 7^2 | 3529 | -22 | 3552 | 12 | 48 | **8** | 8 | 29 | 16 (5) |
| 655a1 | 8 | 7^2 | 3823 | -106 | 3930 | 27 | 45 | **8** | 8 | 8 | 16 (5) |
| 655a1 | 8 | 11^2 | 1453 | 31 | 1423 | 3 | 91 | **8** | 8 | 107 | 10 (5) |
| 655a1 | 8 | 11^2 | 2179 | -40 | 2220 | 18 | 2 | **8** | 8 | 118 | 10 (5) |
| 655a1 | 8 | 11^3 | 2663 | 80 | 2584 | 701 | 856 | **8** | 8 | 833 | 1184 (3) |
| 655a1 | 8 | 11^2 | 3389 | -38 | 3428 | 48 | 7 | **8** | 8 | 74 | 95 (3) |
| 655a1 | 8 | 11^2 | 3631 | -24 | 3656 | 36 | 14 | **8** | 8 | 52 | 94 (7) |
| 655a1 | 8 | 17^2 | 3469 | 77 | 3393 | 58 | 120 | **8** | 8 | 229 | 35 (5) |
| 1615a1 | 16 | 7^2 | 197 | -18 | 216 | 47 | 3 | **16** | 16 | 16 | 29 (3) |
| 1615a1 | 16 | 7^2 | 491 | 12 | 480 | 31 | 11 | **16** | 16 | 44 | 29 (3) |
| 1615a1 | 16 | 7^2 | 883 | -4 | 888 | 8 | 16 | **16** | 16 | 30 | 32 (5) |
| 1615a1 | 16 | 7^2 | 1471 | -56 | 1528 | 27 | 32 | **16** | 16 | 44 | 22 (11) |
| 1615a1 | 16 | 7^2 | 2549 | -14 | 2564 | 2 | 27 | **16** | 16 | 37 | 29 (3) |
| 1615a1 | 16 | 7^2 | 2647 | -8 | 2656 | 26 | 5 | **16** | 16 | 30 | 32 (5) |
| 1615a1 | 16 | 7^2 | 3137 | 6 | 3132 | 46 | 4 | **16** | 16 | 16 | 29 (3) |
| 1615a1 | 16 | 7^2 | 3529 | 104 | 3426 | 48 | 34 | **16** | 16 | 16 | 32 (5) |
| 1615a1 | 16 | 7^2 | 3823 | 8 | 3816 | 40 | 18 | **16** | 16 | 30 | 32 (5) |
| 1615a1 | 16 | 11^2 | 727 | 8 | 720 | 65 | 69 | **16** | 16 | 60 | 20 (5) |
| 1615a1 | 16 | 11^3 | 2663 | 54 | 2610 | 556 | 735 | **16** | 16 | 214 | 1037 (3) |
| 1615a1 | 16 | 11^2 | 3631 | -50 | 3682 | 3 | 45 | **16** | 16 | 16 | 67 (7) |
| 1615a1 | 16 | 13^2 | 677 | 24 | 654 | 25 | 12 | **16** | 16 | 81 | 152 (3) |
| 1615a1 | 16 | 13^2 | 2029 | -80 | 2110 | 113 | 126 | **16** | 16 | 107 | 75 (5) |
| 1615a1 | 16 | 13^2 | 3719 | -48 | 3768 | 81 | 96 | **16** | 16 | 120 | 152 (3) |
| 194040co6 | 32 | 13^2 | 677 | 6 | 672 | 43 | 96 | **32** | 32 | 45 | 135 (3) |
| 194040co6 | 32 | 13^2 | 2029 | -86 | 2116 | 38 | 138 | **32** | 32 | 45 | 150 (5) |
| 194040co6 | 32 | 13^2 | 3719 | 0 | 3720 | 133 | 107 | **32** | 32 | 149 | 135 (3) |
| 194040co6 | 32 | 17^2 | 3469 | 14 | 3456 | 128 | 22 | **32** | 32 | 185 | 140 (5) |

