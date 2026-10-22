# 66b1 — curve data, proposed family, and the pre-registered prediction

Everything below is either (a) established curve data, or (b) an explicitly labelled **hypothesis**.
Nothing here is a result.

## 1. The curve

Cremona `66b1` = LMFDB `66.b4`, optimal, semistable, non-CM, analytic rank 0, Manin constant 1.

    minimal model      y² + xy + y = x³ + x² − 2x − 1        (coefficients [1,1,1,−2,−1])
    Δ_min              528 = 2⁴·3·11              ** POSITIVE **
    (c₄, c₆)           (97, −17)
    j                  912673/528
    torsion            Z/4
    rank               0
    bad primes         2 : I₄ split, c = 4 ;  3, 11 : I₁ nonsplit, c = 1
    L(E,1)/Ω           1/4

Compare 62a1: `Δ_min = −496 = −2⁴·31`, **negative**. This sign change is the reason this packet
exists.

## 2. Proposed descent model (to be checked, not assumed)

    E₁ : Y² = X³ + 17X² + 64X          A = 17,  B = 64,  A² − 4B = 33
    Δ(E₁) = 16·64²·33 = 2¹⁶·3·11

so `B = 64` is a square, i.e. the 2-isogenous quotient is expected to have full rational 2-torsion,
as for 62a1. **The explicit change of variables between the minimal model and `E₁` is not supplied
here — derive and verify it.**

## 3. Proposed prime family (HYPOTHESIS)

    F_66 = { q prime :  q ∤ 6N,  q ≡ 5 (mod 8),  v₂(#Ẽ(F_q)) = 2,  a_q(E) ≠ 0,
                        (q/3) = −1,  (q/11) = +1 }

Note this fixes `(q/3)` and `(q/11)` **separately**, which is a stronger condition than fixing the
single symbol `(33/q) = (3/q)(11/q)`.

Recorded witness: `q = 5`, `#Ẽ(F₅) = 4`.

## 4. Pre-registered Selmer prediction (HYPOTHESIS — the thing to test)

    Sel^{φ_q}(E_q/Q)   =?  {1, 33, q, 33q}
    Sel^{φ̂_q}(E'_q/Q)  =?  {1}

Ambient support `S = {2, 3, 11, q}`, so `|Q(S,2)| = 32` squareclasses (compare 16 for 62a1).

**This is a prediction, not a theorem.** No descent has been carried out for 66b1. It is recorded
before the fact so that a later computation cannot be retrofitted to it.
