# Stage 5 — A0 checked before agreeing. It holds. `THETA_ORDER_2_FULL_ORDER_4`.

Date 2026-09-22. **Additive.** Resolves A0 from `STAGE4_INTERFACE_A_SETUP.md` §4. No engine launched.
Nothing certified.

---

## 1. The apparent counterexample, and why it is not one

A source search returned `ord_J θ = max{r^+, r^-} − 1` — a **`−1`** that would give theta order 1, full order 2, i.e.
exactly the reading stage 4 called "reading 2" and that this resolution retires. Chased to source
(`arXiv:1910.08680`, *On anticyclotomic variants of the p-adic BSD conjecture*): that statement is explicitly the
**indefinite** case, "`N^-` squarefree with an **even** number of prime factors."

**Ours is definite — `|N^-| = 3`, odd.** The `−1` does not apply. A0 survives the challenge.

## 2. Independent confirmation of `2·max`, from the pairing structure

Not taken from BD's statement; re-derived here. The anticyclotomic character is **odd** under complex conjugation, so
`⟨P^τ, Q^τ⟩ = −⟨P,Q⟩`. Hence the pairing vanishes identically on `E(K)^+ × E(K)^+` and on `E(K)^- × E(K)^-`, and the
height matrix is **block-antidiagonal**:

        [  0    A  ]        A of size r^+ x r^-
        [ -A^T  0  ]

`rank = 2·rank(A) <= 2·min(r^+,r^-)`, so the kernel has dimension `(r^+ + r^-) − 2·min = |r^+ − r^-|`, and

    ord >= (total rank) + (kernel dim) = (r^+ + r^-) + |r^+ − r^-| = 2·max(r^+, r^-).

Checked numerically across `(r^+,r^-) = (0,0), (1,1), (2,0), (2,2), (3,1), (2,1)`; matrix ranks match `2·min` in every
case. Sanity anchors: `(1,1) → ord 2` (no extra vanishing, matches the complex order), `(0,0) → ord 0`. **So the
definite formula is `2·max`, with no `−1`** — and the extra vanishing over the complex order is exactly
`2·max − (r^+ + r^-) = |r^+ − r^-|`, zero precisely when `r^+ = r^-`, which is BD's emphasis.

For our intended lane `(r^+, r^-) = (2, 0)`:

    ord_I L_p >= 4,     ord_I 𝓛_p >= 2.          A0 = THETA_ORDER_2_FULL_ORDER_4.

## 3. The line-level citation that was missing

`BRANCH_THETA.md` is on this host and was read this session. It settles which object carries `c_2`, at line level:

* §1 defines the stabilized element `θ_n^α = θ_{n+1} − α^{-1}ν(θ_n)` — **Kim's α-stabilization of the finite
  Gross-point theta element**, i.e. the square-root side, not the full `L_p`.
* §2 computes the cyclic norm element `N = Σ_{i=0}^{p-1}(1+t)^i ≡ p + C(p,2)t + C(p,3)t²  (mod I³)`, concludes
  `N ∈ pΛ + I³`, and states the consequence: the `α^{-1}ν(θ_n)` correction is *"invisible in exactly the quotient that
  detects the mod-`p` **degree-two** witness."*
* §3 states the target as `Σ_σ c_2(σ) φ_E(x_{p^n}(σ)) ≢ 0 (mod p)`.

So the branch's witness is the **`I²/I³` coefficient, mod `p`, of the stabilized Gross-point theta element** — the
square-root object. That is `𝓛_p`, and `k = 2`. **Confirmed at line level: `c_2` must not be reindexed to degree one.**

## 4. An addition — the order target is more robust than the conditional premise

`rank E^{-7}(Q) = 0` is uncertified, and `w(E^{-7}) = +1` only forces `r^- ∈ {0, 2, 4, …}`. But note:

| `(r^+, r^-)` | `2·max` | `rank E(K)` | height pairing | leading term |
|---|---:|---:|---|---|
| `(2, 0)` | **4** | 2 | **identically zero** | **derived** regulator |
| `(2, 2)` | **4** | 4 | can be nondegenerate | standard regulator |

**`m = 4` is the same either way.** So the augmentation-order target does *not* depend on certifying `r^- = 0`; only
the *nature of the leading term* does. That partially de-risks A0 — the order is robust — while sharpening A2.

## 5. The caveat this creates for A2, confirmed at source

With `(r^+, r^-) = (2,0)` the anticyclotomic height pairing is **identically zero** — there is no `E(K)^-` to pair
`E(Q)` against — and `|r^+ − r^-| = 2 > 1`. The source is explicit that in this regime the **standard regulator
vanishes** and the leading coefficient is captured by a **derived** regulator via derived height pairings `hp^(k)`.

So A2 must be stated with the derived object:

    A2 (corrected): if the normalized I^4/I^5 coefficient of F_p is a unit, does that force Sha(E/K)[p^inf] = 0
                    -- where the leading term carries a DERIVED regulator, not the classical one?

This is consistent with the branch already reaching for derived `p`-adic heights (Bertolini–Darmon / Nekovář,
MCS Thm 1.8), but it is a materially harder ask than the classical statement and should be in A2's wording rather than
discovered mid-audit.

## 6. What I did NOT verify

**BD Corollary 3 itself was not read at source.** What is verified here is (i) the *indefinite* analogue —
`arXiv:1910.08680` Thm 3.2, `ord_J F_p >= 2(max{r^+,r^-} − 1)` under mild hypotheses — and (ii) the pairing mechanism
giving `2·max` in the definite case. The **definite inequality `ord >= 2·max` still needs its own citation**; it should
not be recorded as a proved theorem on the strength of the indefinite one plus a structural argument.

Also agreed and widened: do not transplant `m = 4` to BLV's signed supersingular objects. BD's Corollary 3 is stated
for **good ordinary** `p`, and the tail needs *all* `p` — so interface A as now posed is **ordinary-only**, and the
supersingular branch has no established augmentation order at all. That is a third gap, distinct from A and B.

## 7. Frozen

    A0_NORMALIZATION = THETA_ORDER_2_FULL_ORDER_4                          [RESOLVED]
      theta_n  = finite stabilized Gross-point / square-root theta element
      calL_p   = norm-compatible inverse limit of those
      L_p      = calL_p * calL_p^iota
      ord_I calL_p >= 2,  ord_I L_p >= 4     [definite; conditional on the (2,0) or (2,2) input]
      exact order requires [c_2] != 0, which is the branch's standing open target

    A1 (rewritten) : does the BLV/BD algebraic characteristic object satisfy ord_I F_p >= 4 under (r+,r-) = (2,0)?
    A2 (rewritten) : if its normalized I^4/I^5 coefficient is a unit, does Sha(E/K)[p^inf] = 0 follow --
                     with a DERIVED regulator in the leading term?
    A3 (new)       : the supersingular analogue of A1/A2. No established augmentation order. Untouched.
    B              : the a_p = ±1 ordinary primes. Moot unless A closes.

    still uncertified: rank E^{-7}(Q) = 0  (affects A2's regulator, not A0's order)
    still unread    : BD Corollary 3 at source

**Nothing certified. No engine launched. FIN, FORMULA open.**
