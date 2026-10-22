# Grading — two returned runs, ordinary anticyclotomic bridge

Date 2026-09-22. `runA.tar.gz` sha256 `922acd766e3d7016a9e16c9483f9d1717cf5bfdea11f73504b6bf6c9c3013cfc`,
`runB.tar.gz` sha256 `ba4ea713a9f69a27cc8e13ec3492adbedacb2e6a75b90fa93109208f84518479`.

---

## 1. They converge, independently, and that is the finding

Both returned **`LEADING_TERM_STEP_FAILS`**, and both got there the same way:

| ledger row | run A | run B |
|---|---|---|
| `MODULE_IDENTIFICATION` | proved (Selmer groups *literally equal*) | PROVED (place-by-place local comparison) |
| `BD_ORDER_INEQUALITY` | holds (Thm 2.23 + 2.18(2) + Lemma 3.1) | PROVED (same three, Lemma 3.1 re-derived) |
| `TWIST_MINUS_EIGENSPACE` | holds | PROVED (for Selmer/`T_pШ`, not just `E(K)`) |
| `A2a_DIVISIBLE_SHA` | holds, conditional on `[c_2] != 0` | PROVED, conditional on `[c_2] != 0` |
| `A2b_LEADING_TERM` | fails | FAILS |

Both independently flagged the **same source hazard**: BD Lemma 3.1 sits in a chapter that assumes `Ш` finite, and
both re-derived it without that assumption. Since finiteness of `Ш` was the *forbidden* hypothesis and the *target*,
a run that had missed this would have returned a circular proof. Both caught it. That is the single strongest signal
in the two returns.

**So the rank-two `Ш`-finiteness wall is crossed on the ordinary branch, conditional on `[c_2] != 0`.** Task 6
derives `Div Ш(E/K)[p^inf] = 0`, hence `Ш(E/K)[p^inf]` **finite**, with finiteness derived and never assumed. Run A
adds that no height non-degeneracy is assumed either — non-degeneracy of the *second* derived height is forced.

Independent cross-check from this side: both runs' Task-2 argument at `N^-` turns on `v_l(Delta) in {1,2}` being a
`p`-adic unit. Gate stage 3 computed `v_l(Delta) = 2, 1, 2` at `l = 3, 2243, 5843` independently, for `(Ram)`.
Same numbers, different purpose.

## 2. The user's three corrections — all three land

**(a) `A_2 = 0` is sufficient, not equivalent.** *Both* runs wrote "equivalently". Thm 2.18(5) bounds the derived-
height denominators by `p^{A_k}`; a positive saturation defect does not *force* the determinant regulator to have
negative valuation, since cancellation or extra divisibility can occur. Freeze as `NEEDED: v_p(R_der) >= 0`, with
`A_2 = 0` a **sufficient structural criterion**. Both runs overstated this identically — a shared error, not a
confirmation.

**(b) Universal vanishing is false, not merely unproved.** Correct — and worth knowing that **run B states it
itself**, not as our inference: *"if `p | #Ш(E^{-7}/Q)` the target is not merely unproved but **false**, since
`Ш(E/K)[p^inf]^- ≅ Ш(E^{-7}/Q)[p^inf]`."* So the right theorem shape is

    p does not divide #Ш(E^{-7}/Q)   ==>   Ш(E/K)[p^inf] = 0

under the standing hypotheses and `[c_2] != 0`. Chasing `A_2 = 0` universally is provably the wrong target.

**(c) Remark 2.21 is not a hidden integrality theorem.** Both runs refused the cancellation; run A notes 2.21's
sentence is about removing the *unit ambiguity*, "with no proof of integrality anywhere in §2", and run B that
Cor 2.24(2) makes only the **product** integral — precisely the quantity being split. The external check that later
literature reads the same modified regulator as well-defined only after `⊗ Q_p` supports this.

## 3. Correction to the grading: the torsion factor is vacuous here

The two bounds are *not* the same statement:

    run A :  A_2 <= v_p( #Ш(E^{-7}/Q) * #E^{-7}(Q)_tors )
    run B :  A_2 <= c,   p^c = EXPONENT of Ш(E^{-7}/Q)[p^inf]

Run A carries a torsion factor the summary dropped; run B uses the exponent rather than the order. Neither dominates.
**But the torsion factor is empty for this curve:** the twist is `y^2 = x^3 + 159145 x^2 + 5207351716 x`, its quadratic
factor has discriminant `4497724161 = 49 * 91790289`, not a square (the seed's `91790289` is not), so there is only
the one rational 2-torsion point; point counts give `#E^{-7}(Q)_tors | 2`, hence **exactly `Z/2`**. By Mazur the only
primes that could ever appear are `2, 3, 5`, and BLV needs `p >= 5`, so the factor could only ever touch `p = 5` —
and here it does not.

    => run A's and run B's bounds have the SAME SUPPORT:  { p : p | #Ш(E^{-7}/Q) }.

## 4. Correction to the framing: "cofinite" is narrower than it reads

The proposed freeze `ORDINARY_COFINITE_P_VANISHING = PROVED_CONDITIONAL_ON_C2` is right only with **admissible**
doing heavy lifting. The admissible set excludes, beyond the finite twist-`Ш` primes:

| excluded set | size | status |
|---|---|---|
| supersingular `p` | **proved infinite** (Elkies), density 0 | interface A3, untouched |
| anomalous `a_p = ±1` | **conjecturally infinite** (Lang–Trotter), density 0; unproved either way; none below 30000 here | interface B, untouched |
| BLV/BD finite hypotheses | finite | discharged |
| `p \| #Ш(E^{-7}/Q)` | finite (certificate) | **the new item** |

So this is **not** finite support, and not even finite support restricted to ordinary primes, because the anomalous
set is not known to be finite. Honest statement:

    conditional on [c_2] != 0 :  Ш(E/Q)[p^inf] = 0  for every good-ordinary, non-anomalous p
                                 satisfying the BLV/BD hypotheses and not dividing #Ш(E^{-7}/Q);
                                 and Ш(E/K)[p^inf] is FINITE at the remaining ordinary primes.

That is a large advance and it is still two infinite sets short of `FIN`.

## 5. The next question, and where it lands

Agreed: do not attack `A_2 = 0` universally. The high-value question is now

> **What are the prime divisors of `#Ш(E^{-7}/Q)`?**

This is a **finite, fixed-curve** problem: `E^{-7}` is a certified analytic-rank-zero curve with `L(E^{-7},1)`
enclosed to six digits and `#E^{-7}(Q)_tors = 2`. Two routes:

[Private-correspondence paragraph omitted from public export; no mathematical certification is inferred from correspondence.]

**The outreach track and the mathematical frontier have converged on the same question.** That was not true this
morning.

## 6. Ledger after grading

    ORDINARY_MODULE_IDENTIFICATION      = PROVED (both runs, independently)
    ORDINARY_BD_ORDER_INEQUALITY        = PROVED (both; Lemma 3.1 re-derived off the finiteness assumption)
    ORDINARY_TWIST_MINUS_EIGENSPACE     = PROVED (both, for Selmer/T_pSha)
    ORDINARY_A2a_SHA_FINITENESS         = PROVED_CONDITIONAL_ON_C2       <- the rank-2 finiteness wall, crossed
    ORDINARY_VANISHING_OFF_TWIST_SHA    = PROVED_CONDITIONAL_ON_C2
    ORDINARY_EVERY_P_VANISHING          = FALSE where p | #Sha(E^-7/Q)   <- not a gap, a fact
    NEEDED                              = v_p(R_der) >= 0;  A_2 = 0 SUFFICIENT, not equivalent
    TWIST_SHA_PRIME_SUPPORT             = OPEN, finite, fixed-curve       <- the new target
    C2_NONVANISHING                     = OPEN, unchanged
    A3 supersingular / B anomalous      = untouched, both still infinite sets
    FIN, FORMULA                        = OPEN
