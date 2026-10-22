# Stage 6 — two Stage-5 defects corrected, BD Cor 3 promoted, and what A2a actually is

Date 2026-09-22. **Additive.** Corrects `STAGE5_A0_RESOLVED.md` §2, §4, §6. No engine launched. Nothing certified.

---

## 1. BD Corollary 3 — citation hole closed, promoted

Bertolini–Darmon (Annals 2005) is in the **definite** setup: Theorem 1 assumes `N^-` squarefree with an **odd** number
of prime factors — ours. With `ρ = max(r̃^+, r̃^-)` and `δ^± = 0` in the good-ordinary case, Corollary 3 gives

    ord_{s=1} L_p(E,K,s) >= 2ρ,   i.e.   ord_I L_p >= 2·max(r^+, r^-).

Stage 5 listed this as "not read at source" and reconstructed it from the indefinite analogue plus a structural
argument. That reservation is lifted:

    BD05_DEFINITE_ORDINARY_LOWER_BOUND = PROVED   (good ordinary p, definite case)

So A0 no longer rests on a heuristic. Combined with the line-level `BRANCH_THETA` identification, `c_2` stays at
degree two on the square-root side.

## 2. Correction — Stage 5 asserted an equality it had not earned, and its check hid the gap

Stage 5 wrote `dim ker H = |r^+ − r^-|`. Correct statement:

    dim ker H = (r^+ + r^-) − 2·rank(A)  >=  |r^+ − r^-|,   equality iff A has MAXIMAL rank.

Worse, the Stage-5 verification built `A` from `rng.normal(...)` — **generically full rank** — so it confirmed only
the nondegenerate case while being presented as the general one. Redone with explicitly rank-deficient `A`:

| `(r^+,r^-)` | `rank A` | `dim ker` | `\|r^+−r^-\|` | `(r^++r^-)+ker` | `2·max` | bound holds |
|---|---:|---:|---:|---:|---:|---|
| `(2,0)` | 0 | 2 | 2 | 4 | 4 | ✓ |
| `(2,2)` | **1** | **2** | 0 | **6** | 4 | ✓ |
| `(2,2)` | 2 | 0 | 0 | 4 | 4 | ✓ |
| `(3,1)` | **0** | **4** | 2 | **8** | 6 | ✓ |
| `(2,4)` | **1** | **4** | 2 | **10** | 8 | ✓ |

**The lower bound survives a fortiori** — degeneracy only enlarges the kernel. What does not survive is any claim of
*exact* kernel dimension without a nondegeneracy hypothesis. For `(2,0)` the distinction is vacuous (`A` is `2×0`).

## 3. Correction — "`m = 4` is independent of certifying `r^- = 0`" was too broad. Withdrawn.

`w(E^{-7}) = +1` forces only `r^- ∈ {0,2,4,6,…}`, and BD Cor 3 gives `ord_I L_p >= 2·max(2, r^-)`:

| `r^-` | `ord_I L_p >=` | `ord_I 𝓛_p >=` | `rank E(K)` |
|---:|---:|---:|---:|
| 0 | **4** | 2 | 2 |
| 2 | **4** | 2 | 4 |
| 4 | **8** | 4 | 6 |
| 6 | 12 | 6 | 8 |

    WITHDRAWN : "m = 4 is independent of certifying r^- = 0"
    CORRECT   : "m = 4 is independent of distinguishing r^- = 0 from r^- = 2"

`r^- >= 4` is **not** excluded by anything currently in the project record.

**The reversal holds, and is worth keeping.** If the branch proves `[c_2] ≠ 0`, then `𝓛_p ∈ I²\I³`, so
`L_p ∈ I⁴\I⁵`, and BD Cor 3 forces `2·max(2,r^-) <= 4`, i.e. **`r^- <= 2`** — the witness excludes `r^- >= 4` for free
at ordinary `p`. It does not separate `r^- = 0` from `r^- = 2`, and the lane needs `r^- = 0`.

## 4. A2 split accepted — and A2a is not a side condition

BD *Derived p-adic heights* Thm 2.23 gives the leading coefficient of the algebraic characteristic ideal as

    [ Sha(E/K)[p^inf] / Div Sha(E/K)[p^inf] ]  ×  R_der

so a unit leading coefficient yields `Sha[p^inf] = Div Sha[p^inf]` — i.e. `Sha[p^inf] ≅ (Q_p/Z_p)^d` — **not**
`Sha[p^inf] = 0`. The split is right:

    A2a : control/eliminate the divisible part
    A2b : control v_p(R_der) strongly enough that a unit product forces Sha[p^inf] = 0

**A2a is not supplied by the formula, and that is demonstrable.** Write `X_∞ ~ ⊕_i Λ/(f_i)`. Control gives
`corank Sel(K) = #{i : T | f_i} = rank E(K) + d = 2 + d`, while `ord_I F_p = Σ_i ord_T(f_i)`. Take four factors each
with `ord_T f_i = 1` and unit leading coefficient: then `ord_I F_p = 4`, the normalized leading coefficient is a unit,
and `d = 2`. **A unit `I⁴/I⁵` coefficient is consistent with `Sha(E/K)[p^∞]` of corank 2.** So A2a must come from
outside.

**And A2a is exactly the project's recurring wall.** `A2a ≡ Sha(E/K)[p^∞] is finite`. At analytic rank 2 there is no
known source for it — which is precisely what Keller named: in rank one, finiteness of `Sha` comes from the finite
Heegner index, and that has no rank-two analogue. The project has recorded `wall = Sha finiteness` before (H9R19).

> **Consequence for the audit prompt:** A2a must be named as load-bearing and explicitly forbidden as an assumption.
> A run that treats "eliminate the divisible part" as a technical step will either stall there or smuggle in
> `Sha` finiteness and return a confident circular proof. The standing instruction "without assuming FIN" is not
> enough on its own, because A2a is weaker than FIN and can be assumed without appearing to assume FIN.

One route that may make A2a non-circular, offered as a lead rather than a claim: `ord_I L_p = 4 < ∞` gives `L_p ≠ 0`,
and BLV Theorem A's `F_p | L_p` then forces `F_p ≠ 0`, i.e. `X_∞` is **Λ-torsion**. Whether Λ-torsion plus the control
theorem converts into `d = 0` is the thing to check — the module computation above shows it does **not** follow from
the order and unit coefficient alone, so if it works it must use more.

## 5. Updated freeze

    A0_OBJECT_NORMALIZATION           = RESOLVED  (theta order 2, full order 4)
    BD05_DEFINITE_ORDINARY_ORDER      = PROVED    ord_I L_p >= 2·max(r^+,r^-), good ordinary, definite
    C2_LOCATION                       = RESOLVED  I^2/I^3 of the square-root theta  [BRANCH_THETA, line level]
    KERNEL_DIMENSION                  = INEQUALITY ONLY  (>= |r^+-r^-|; equality needs nondegeneracy)
    M4_FROM_RANK_DATA                 = VALID IFF r^- <= 2; NOT from parity alone. r^- >= 4 unexcluded.
    EXACT_M4                          <== [c_2] != 0                                   OPEN
                                          (and would itself force r^- <= 2 at ordinary p)
    A1   = exact algebraic/BLV characteristic comparison at degree 4 under (r^+,r^-) = (2,0)
    A2a  = divisible-Sha control            <- LOAD-BEARING; = Sha(E/K)[p^inf] finite; the recurring wall
    A2b  = derived-regulator valuation control
    A3   = supersingular signed analogue    <- still separate; BD Cor 3 is good-ordinary only
    B    = the a_p = ±1 ordinary primes     <- moot unless A closes

    still uncertified : rank E^{-7}(Q) = 0

**Nothing certified. No engine launched. FIN, FORMULA open.**
