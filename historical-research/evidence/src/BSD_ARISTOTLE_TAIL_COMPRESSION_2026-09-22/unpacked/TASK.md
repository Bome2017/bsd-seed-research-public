# TAIL-COMPRESSION THEOREM TASK — do not run a prime ladder

Fixed seed `E : y^2 = x^3 - 22735 x^2 + 106272484 x`, `N = 2^3 * 3 * 2243 * 4547^2 * 5843`. All retained results in
`INPUTS.md` are inputs, not things to re-derive. Read `GATE.md` before proposing anything.

**Goal.** Decide whether the retained rank-three Selmer-to-Sha comparison can be upgraded to a finite-exception theorem

    Sha(E/Q)[p] != 0  =>  p in S,      S one explicit finite set.

There are two load-bearing questions. **They are independent, and Q1 is primary** — if Q1 fails, coverage is irrelevant.

---

## Q1 (PRIMARY). Is the Stark ideal reducible to a fixed integral object?

For a lane `i` with certified data, the retained comparison leaves exactly one unresolved arithmetic term: the ideal
`I_{3,i}` of the Heegner-point Stark system. At `p = 13` the whole implication reduced to

    I_3(eps^Hg_{1,0}) = F_13   =>   Sha(E/Q)[13^inf] = 0.

**Question.** Determine whether `I_{3,i}(p) = F_p` can be obtained by reduction mod `p` of a **fixed** arithmetic object
independent of `p` — an integral ideal, determinant, Fitting ideal, presentation matrix, integral Selmer complex, or
anything else finite and `p`-free. The desired shape is

    I_{3,i}(p) != F_p   =>   p | C_i,     C_i a fixed nonzero integer.

**What you are up against, stated honestly.** *As presently defined* the object is `p`-dependent: it is built from
`T = T_p(E)` and a Selmer complex with local conditions at `p`. **That describes the current definition, not the
object — whether it descends from something `p`-free is exactly Q1 and must not be prejudged.** The one obvious
`p`-independent candidate is already **refuted**: the Heegner Λ-index does **not** determine `I_3`. Explicit counterexample in `INPUTS.md` §4 — identical
index and characteristic-ideal data, same rank-three point contribution, different specialized Fitting ideals. So a
positive answer requires a genuinely new integral model, not the index.

A negative answer is a real result and should be returned promptly. See kill condition K1.

## Q2 (SECONDARY). Coverage — and the obstruction you are handed

The character-cover idea is correct as far as it goes. With `chi_3 = chi_1 chi_2`, no prime unramified in all three can
have `chi_1(p) = chi_2(p) = chi_3(p) = -1`, since the third value would be `+1`. So every such prime splits in at least
one of the three fields.

**But every such cover contains a real quadratic field, and the retained comparison cannot use it.**

`chi_D` is odd exactly when `D < 0`. A product of two odd characters is even, so `chi_1, chi_2` imaginary forces
`K_3 = Q(sqrt D_1 D_2)` **real**. Equivalently: a product of three odd characters is odd, never trivial, so
`chi_1 chi_2 chi_3 = 1` with all three imaginary is impossible. Checking the three biquadratic signatures:

    a imag, b imag  ->  subfields imag, imag, REAL
    a imag, b real  ->  subfields imag, REAL, imag
    a real, b real  ->  all three real

**Every Klein-four cover has at least one real quadratic subfield.** The Heegner/anticyclotomic machinery the retained
comparison rests on requires `K` imaginary. So the naive three-imaginary-twist cover **cannot be constructed**, and this
is settled before your run begins — do not spend time rediscovering it.

### The three repair directions, none endorsed

1. **Serve the real lane by a different mechanism.** Requires a real-quadratic analogue. Stark-Heegner points are
   conjectural and therefore inadmissible under `GATE.md` K4; anything else must be a proved theorem.
2. **Let `K` vary with `p`.** Nothing in the record excludes this, and it dissolves the covering problem: for each `p`
   there are discriminants with `p` split. The price is that you no longer have finitely many lanes, so `C_i` must
   become uniform in `D` — and the rank-one condition must hold for the chosen `D`, which points at nonvanishing
   results for `L'(E^D,1)` in families rather than one certificate at a time. This **adds a uniformity-in-`D`
   requirement beyond Q1**; no claim is made that it is logically stronger.
3. **Accept a finite set of imaginary lanes.** This does **not** give a theorem: with `r` independent quadratic
   characters the uncovered primes have density `2^{-r} > 0` for every finite `r`. Recorded so it is not re-proposed.

## `p = 17` calibration

Verified directly from the seed: `#E(F_17) = 24`, `a_17 = -6`, so 17 is good, ordinary (`17 ∤ -6`) and nonanomalous
(`17 ∤ 24`). But `chi_{-23}(17) = -1`, so the **already-certified** `D_1 = -23` lane does not serve it.

That makes 17 the first clean generic prime that tests whether a *second* lane genuinely extends coverage rather than
repackaging lane 1. Use it as a coverage test only. **This is not permission to compute `C_17`** — no prime ladder, no
modular-symbol run.

## Deliverable

State the exact first unproved arrow, and return one of the four verdicts in `GATE.md`. If Q1 returns negative, return
immediately; do not proceed to Q2.
