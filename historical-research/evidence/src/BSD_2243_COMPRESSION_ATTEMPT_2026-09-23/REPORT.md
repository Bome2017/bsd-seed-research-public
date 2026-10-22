# C_{2243,3} exact algebraic compression attempt: OBSTRUCTION, stopped (2026-09-23)

**Verdict: the attempt stops at a precise obstruction.**
* The one relation that goes beyond the earlier trace-only calculation is the W_Q Atkin–Lehner pairing on the wild coordinate. It determines every even coefficient of the certificate polynomial and **leaves c₃, the certificate itself, free**.
* Every other Manin/Hecke/Atkin–Lehner route raises the Fourier cutoff or the analytic scale, or needs a modular-symbol space of dimension 10¹⁵–10¹⁶.
* **The coefficient range is unchanged: T_run = 3.912·10¹³, 110 622.5 lch.**

**What was and was not done.**
* No coefficient production, reviewer or successor branch was launched. Nothing was spent.
* No file outside this folder was modified. The pilot-prep cost model was imported read-only, with no bytecode written.
* No novelty, FIN or BSD claim is made.

Files: `01_COLLISION_CHECK.md`, `02_DERIVATION.md`, `03_WORKLOAD.md`, and the exact checks in `checks/`.

## 1. Retained certificate, unchanged, with D5's qualification

K = 1024·Σ_{b mod ±1} bal_p(2·C(ℓ(b),3))·[b/p²]⁺. This is the SW normalization, with the plus period ω₁ (the total real period is 2ω₁, and 2 is a unit at 2243), α = a_p = +1, and ℓ(b) ≡ −q_p(b).

**K ≢ 0 (mod 2243) ⟹ Sha(E/Q)[2243^∞] = 0, given D1–D8.**
* **D5 is necessary at the retained grade.** SW Theorem 6.1's multiplicative "iff" is not supported by its cited source: Jones 1989 proves only the forward direction, under Sha finite. D5 is discharged by an independent split-height computation or by an explicit grade decision.
* **K ≡ 0 establishes nothing.**
* This attempt changes none of this.

## 2. The additional relation and the exact identities

**Coordinates.** Write b = ω(a)(1+p)^j, so j = ℓ(b). The symbols form a matrix X[a][j] = 1024[b/p²]⁺, and the certificate is **K ≡ c₃ (mod p)**, where c₃ = [T³]θ, θ(T) = Σ_j Y_j(1+T)^j, and Y_j is the j-th column sum. This is exact (02 §1).

**Earlier calculations (U_p traces only)** fix the row sums, so they determine only c₀ = 0 (Lemma T, 02 §2). This is the collision recorded in 01; it was not recomputed.

**The additional relation, W_Q:** x_{u_b} = s·x_b with u_b = (Qb)^{−1} and s = −w·a_p = −1. The sign rule was validated at a split prime in S1a (15a1, the same pattern).
* It maps column j to column −L − j, with **L = ℓ(Q) = 1989**, so Y_{−L−j} = −Y_j and Y₁₂₇ = 0.
* It was verified exactly on the certified m = 27 and m = 81 tables (s = +1 at p = 3): 18/18 and 54/54, on both signs.

**Theorem F** (02 §3). Put W = T(1+T)^{−1/2}. Then W is odd under the involution T ↦ (1+T)^{−1} − 1, and **(1+T)^{L/2}θ is an odd series in W.** Hence, exactly mod 2243:

    c₀ = 0,   c₂ = −995·c₁,   c₄ = 1247·c₃ + 511·c₁,   and c₃ is free:
    rank{c₀,c₁,c₂} = 1 < rank{c₀,c₁,c₂,c₃} = 2 on the (p−1)/2 = 1121-dimensional constraint space.

With c₁ ≡ 0 (order ≥ 3), c₃ is the leading odd coefficient, **the first free parameter of the relation.** The relation fixes the even W-coefficients only.

## 3. The precise obstruction

**The Atkin–Lehner pairing is the only relation beyond U_p that acts at denominator p², and it leaves c₃ undetermined.** All other relations tested move to larger denominators or levels, or to prohibitive spaces (`03_WORKLOAD.md`):

| route | cost |
|---|---|
| Γ₀(N) loops | scale ≥ N, i.e. ≥ 759×; actual loops 1.6·10⁸–1.8·10⁹× |
| W_p / W_N moves | ≥ 16.0× |
| T₅ | 5× cutoff, 735 762 lch, and only sums |
| level-N symbols | 2.17·10¹⁵ dimensions |
| weight-2244 Serre space | 1.08·10¹⁵ dimensions |
| overconvergent symbols | 1.30·10¹⁶ Manin symbols |
| Kolyvagin denominators | cutoff ≈ 2·10²⁵ |
| single-embedding Galois recovery | ~10⁴ digits |
| Mazur–Tate / MTT | unproved and circular |

**Aggregation to column sums** is exact and removes the length-p² DFT and the 103 GB checkpoint problem. But it needs T = 4.622·10¹³ and **134 570 lch (1.216×)**: a memory saving that costs 22% more dominant work.

**Stated precisely.** c₃ (mod p) is a function of the p − 1 central twisted values L(E, ψ, 1), where ψ runs over the characters of conductor p² and order p. Each has analytic conductor Qp⁴.
* The relations examined permute these values or trade them for values at larger conductor or level.
* The current engine evaluates them together, in one batch, at the √(Qp⁴) = 8.57·10¹² scale, and is already the cheapest point in each cusp's Atkin–Lehner/Γ₀(N) orbit.
* **This is an obstruction for the relations examined, not a proved lower bound for every algorithm.**

## 4. By-product for any future run (recorded, not acted on)

* **A built-in end-to-end check.** c₁ ≡ 0 (mod 2243) is forced by order ≥ 3 (D1, D2, D7), and the pairing does not force it. A production output with c₁ ≢ 0 would expose a pipeline or input error; it passes by chance with probability 1/p.
  * c₂ follows from c₁ via the pairing, so it is not an independent check.
  * The pairing itself holds by construction of the engine formula, so it is not an independent check either.
  * c₀ = 0 is exact from U_p, and checks the output if the [a/p]⁺ row data are also computed.
* **The aggregation layout (R6)** is the option if memory or checkpoint volume, rather than CPU, becomes binding. It costs +21.6% lch.

## 5. Unchanged, still awaiting your decision (none acted on)

1. **F4:** apply the generation-reservation fix (v2.4), rerun the tests, then a Codex re-check.
2. **D5:** an independent split-height computation, or a grade decision.
3. **Master record:** authorize reconciliation (`verify_master.py` reports RECONCILIATION_REQUIRED).

Paid computation and cloud preparation stay parked. 5843 is held.
