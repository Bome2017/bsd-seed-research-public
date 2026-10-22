# Stage 4 — two corrections accepted, `H⁰` settled, and a hard constraint on the normalization question

Date 2026-09-22. **Additive.** Corrects §4–§5 of `STAGE3_BLV_CORRECTION.md`; that file preserved unedited.
No engine launched. Nothing certified.

---

## 1. Correction A — Remark 1.4 was cited for the wrong reason. Accepted.

Stage 3 §5 used BLV Remark 1.4 as evidence that the rank-two trivial-character leading term is unavailable. That is a
misreading: **Remark 1.4 is about the exceptional local zero in the supersingular / inert / `ε = +` case.** BLV say
`n = 0` is *accessible* in the non-exceptional setting. The two issues are separate, and I merged them.

The verdict is unchanged but must now rest on the second ground only:

    BLV_RANK2_LEADING_TERM = NOT PRESENT
      reason (correct)   : the paper states no higher-order augmentation / derived leading-term formula;
                           Theorem B covers the finite-Selmer, nonzero-central-value case.
      reason (WITHDRAWN) : "Remark 1.4 sets the trivial character apart."   <- exceptional case only

## 2. Correction B — `H⁰(G_{Q_q}, E[p]) = 0` for `q | N^+`. Settled, and it costs nothing.

Stage 3's `(Ram)` repair was necessary but not sufficient: BLV Hypothesis 1.1 also demands
`H⁰(G_{Q_q}, E[p]) = 0` at `q | N^+`. For `D = -7`, `N^+ = 2^3 · 4547^2`, so this is needed at `q = 2` and `q = 4547`.

`H⁰(G_{Q_q}, E[p]) = E(Q_q)[p]`. Both places are **additive** (`v_q(N) = 3` and `2`), and `j` is **integral** there
(`v_q(j) < 0` only at `3, 2243, 5843`), so the reduction is potentially good. Then:

* `E_1(Q_q)` — the formal group — is pro-`q`, so has no `p`-torsion for `p ≠ q`;
* `E_0(Q_q)/E_1(Q_q) ≅ Ẽ_ns(F_q) ≅ (F_q, +)` for additive reduction, a `q`-group, likewise no `p`-torsion;
* `E(Q_q)/E_0(Q_q) = Φ_q` has order `c_q`, and **`c_q ≤ 4` for every additive Kodaira type**
  (`II`:1, `III`:2, `IV`:3, `I_0^*`:1/2/4, `I_n^*`:2/4, `IV^*`:3, `III^*`:2, `II^*`:1).

So `#E(Q_q)_tors | q^k · c_q` with `c_q ≤ 4`, hence

    E(Q_q)[p] = 0   for every p >= 5,  q = 2 and q = 4547.

**No primes are excluded at all** — not even finitely many. The bookkeeping omission is repaired and the hypothesis is
free for us. (The exact Kodaira types were not computed; no PARI/Sage on this host. The bound `c_q ≤ 4` holds for
*every* additive type, so the conclusion does not depend on which one occurs.)

## 3. The divisibility test — logic checked, with one thing it assumes

Theorem A gives `(L_p^ε) ⊆ (Char^ε)`, i.e. `F_p | L_p` — the Euler-system direction, which bounds the algebraic side
above. Writing `L_p = F_p · G`:

    ord_T L_p = ord_T F_p + ord_T G

so if the witness gives `ord_T L_p = m` with unit normalized leading coefficient, and control forces
`ord_T F_p >= m`, then `ord_T G = 0`, `G(0) ≠ 0`, and

    (T^{-m} L_p)(0) = (T^{-m} F_p)(0) · G(0)

is a unit, which forces **both** factors to be units. The inference is sound.

**But it rests on two control inputs, not one**, and only the second was named:

    (i)  the rank-two input forces ord_T F_p >= m          <- assumed, not established
    (ii) (T^{-m} F_p)(0) in Z_p^x  ==>  Sha(E/K)[p^inf] = 0 <- the stated open question

Both are control-theorem questions. (i) should be tracked explicitly, since a shortfall there breaks the argument
before (ii) is ever reached.

## 4. The normalization question is not cosmetic — it changes `m`, but not the unit condition

BLV build the square-root object `𝓛_p` from Gross points and set `L_p = 𝓛_p · 𝓛_p^ι`. The involution `ι` sends
`γ ↦ γ^{-1}`, so on `Λ = Z_p[[T]]` with `T = γ - 1` it sends `T ↦ -T/(1+T)`. Hence `ι` preserves `I = (T)` and
`ord_T(𝓛_p^ι) = ord_T(𝓛_p)`. Therefore:

    ord_T L_p = 2 · ord_T 𝓛_p      -- ALWAYS EVEN

and if `𝓛_p = c·T^k + …` then `L_p = (-1)^k c^2 T^{2k} + …`.

Two consequences, and they pull in opposite directions:

**(a) The order is ambiguous, and the two readings give different theorems.** `BRANCH_THETA.md` manipulates the theta
elements `θ_n` — the Gross-point objects, i.e. the **square-root** side. If its degree-two witness `c_2` is the
`I²/I³` coefficient of `θ = 𝓛_p`, then `k = 2` and **`ord_T L_p = 4`**, so the test needs `ord_T F_p = 4`. If instead
the rank-two condition pins `ord_T L_p = 2`, then `ord_T 𝓛_p = 1` and the witness should sit in **`I/I²`** of `θ`, not
`I²/I³`. **The two readings are mutually exclusive and the parity is a hard check** — `ord_T L_p` cannot be odd, so any
identification implying an odd order is wrong on its face.

**(b) The unit condition is robust to the ambiguity.** Since the leading coefficient of `L_p` is `±` the *square* of
that of `𝓛_p`, one is a `p`-adic unit exactly when the other is. So the "unit normalized leading coefficient" half of
interface A survives whichever object our witness lives on; only the **order** `m` is at stake.

That splits Q1 usefully: the normalization must be resolved to know *which* `m` to prove, but not to know that the
unit property transfers.

## 5. Interfaces, restated

    A. degree-two analytic witness ==> unit normalized characteristic coefficient ==> Sha[p^inf] = 0
       A0. resolve: is the branch's c_2 the I^2/I^3 coefficient of 𝓛_p (=> m = 4) or of L_p (=> m = 2)?
       A1. control input: rank two forces ord_T F_p >= m                       [assumed, unestablished]
       A2. control input: unit leading coefficient ==> Sha(E/K)[p^inf] = 0     [the open question]
    B. the a_p = ±1 ordinary primes — conjecturally infinite, unproved both ways; moot unless A closes.

Agreed: **hold the `D = -7` run, attack A first, and A0 before A1/A2.** Agreed also that the next prompt should be the
narrow one, not another broad BLV review — with the addition that it must carry the parity constraint from §4(a), since
an audit that silently picks the wrong `m` will produce a confident and wrong answer.

**Nothing certified. No engine launched. FIN, FORMULA open.**
