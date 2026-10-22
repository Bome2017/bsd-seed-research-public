# Two-leg tame experiment — REPORT

Claude (Opus 5.5), 2026-10-14. Bounded discovery experiment on five rank-2 control curves; about 3 CPU-minutes.
Predictions sealed before any modular symbol was computed (`PREDICTIONS_SEALED.md`, sha256 `f3f57041…59bc`).
No pushes, messages or paid compute. **Endpoint effect: none. FIN, ORDER9 and Q36 are unchanged.**

## Verdict: ONE FORM ACROSS TWO PRIMES

At level M = l1*l2 the Mazur–Tate element's leading term in I^2/I^3 has three parts. The two pure parts are forced by
the one-prime law; the mixed part c11 = sum_a ind1(a)*ind2(a)*[a/M]^+ is new information. The sealed prediction

    c11 == K_E*(a_l1-2)*(a_l2-2)*Dmix/(cexp^2*idx_M)^2   (mod q^min(e1,e2)),
    Dmix = h1(Q1)h2(Q2) + h2(Q1)h1(Q2) - 2*b1*b2   (the polarization of the determinant),

held at **714 of 714 clean rows**, including **512 of 512** rows that predict a nonzero value. Depth reached 3^3 and 5^2.

| curve | K_E | clean rows | mixed ok | pure (forced) ok |
|---|---|---|---|---|
| 389a1 | 8 | 145 | 145 | 145 |
| 433a1 | 4 | 137 | 137 | 137 |
| 664a1 | 16 | 155 | 155 | 155 |
| 655a1 | 8 | 165 | 165 | 165 |
| 1615a1 | 16 | 112 | 112 | 112 |

By q: 3 (476 rows, up to 3^3), 5 (134, up to 5^2), 7 (56), 11 (27), 13 (21). Also c00 = 0 and c10, c01 vanish in I/I^2
at every row, and both polarization identities for the tame heights agree on all 714 rows.

## The test has power (negative controls, `outputs/negative_controls.txt`)

| formula for the mixed term | matches (all 714) | matches where c11 is nonzero mod q (512) |
|---|---|---|
| sealed prediction | 714 | 512 |
| no Euler factors | 382 | 184 |
| one Euler factor only | 313 | 121 |
| +2*b1*b2 instead of -2*b1*b2 | 304 | 194 |
| no cross b-term | 304 | 194 |
| diagonal heights only | 184 | 86 |
| sign flipped | 189 | 0 |
| shuffled across rows | 179 | chance level 185 |

## What this shows

- The tame leading term at two primes is det(H1*x1 + H2*x2): the determinant of ONE pairing matrix that is linear in
  the direction. The constant is the same K_E, and each leg contributes its own factor (a_l - 2).
- No cross-prime correction term appears. Linking data between the primes (for example ind_{g1}(l2)) enter only
  through the tame heights themselves.
- So the per-prime tame laws are restrictions of one quadratic form, K_E*det(universal tame height pairing), on one
  class P1^P2. This is the shape of the Mazur–Tate refined conjecture at composite level. The record had used two-prime
  Kurihara numbers only as per-p witnesses; the mixed-term law had not been tested here before.
- Reading for reopener 1: over Q the second-order term decomposes over pairs of places ("two legs", as in Yun–Zhang),
  bilinearly, with one global constant, in every direction that has finite quotients.

## What no finite-level experiment can show (structural, follows from the result's setting)

Sym^2 of a finite abelian group is the direct sum of its q-primary parts. So every identity at any finite level,
with any number of legs, splits into separate statements about K mod q^e, one prime q at a time. No finite-level
identity couples the constant at p to the constant at p'. "One rational constant for all primes" (step C, reopener 3)
is invisible to the whole finite world; it is the statement that the family (K_q) in prod Z_q is one rational number.
This is the finite-level face of the splitting A_Q^x/Q^x = R_{>0} x Zhat^x. In rank 0 the global input is the rational
modular symbol [0]^+; in rank 1 it is the Heegner point. Rank 2 needs an object of that kind: a rational number or a
global cycle, and it must reproduce the determinant of the full pairing matrix, not just one number.

## Limits

- Control curves only (the seed's composite-level symbols would cost tens of CPU-hours per row; not run).
- l2 <= 200, q <= 13, depth <= 3^3; clean rows need q !| cexp*idx_M (Kurihara-type rows, where q | #E(F_l), are excluded).
- Same-session work, not reviewed. Consistent with a published conjecture; this is evidence, not a theorem.
