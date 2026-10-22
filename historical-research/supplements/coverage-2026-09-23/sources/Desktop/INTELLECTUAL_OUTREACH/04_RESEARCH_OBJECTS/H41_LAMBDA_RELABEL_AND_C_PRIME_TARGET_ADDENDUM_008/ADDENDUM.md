# Eighth addendum — the λ table re-labelled, `(L)` not closed by known theorems, and the target narrowed to `(C′)`

**Tier: RECORD AND CORRECTION.** No new mathematics. No new level computed. No research run commissioned.
`H41_KILL_TEST_EXECUTED_ADDENDUM_007` (`c1a6f8ea…`) is preserved **byte-identical** and is not
superseded; this object records the correct reading of its §5 and two forward points. Prior objects
unmodified: `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`, `3eb98a60…`,
`da70ec51…`, `c1a6f8ea…`.

## 1. The evidentiary re-labelling — accepted, with its scope corrected to ONE value

The operator's point: `ADDENDUM_007` §5's line `4L/Ω = 1, 3, 9, 117` must be labelled database /
numerical confirmation rather than exact values, *unless* a separate certified rational-reconstruction
argument exists — proposed for "the latter two".

**Accepted for `117/4`. It does not apply to `9/4`:** a certificate for that value already exists in the
frozen record and predates `ADDENDUM_007`. The correct picture has **three** categories, not two:

    N        λ       status              basis
    62      1/4    EXACT, twice over   rigorous interval with unique contained candidate
                                       + modular-symbol certificate_62.gp
    254     3/4    EXACT, twice over   rigorous interval + certificate_254.gp
    16382   9/4    EXACT, once         rigorous denominator reconstruction with uniqueness
                                       width test.  NO modular-symbol certificate exists at
                                       this level, and none is needed for the certificate.
    262142 117/4   NOT CERTIFIED       ecdata printed decimal columns only, ~30-digit
                                       agreement, no rigorous error bound, no denominator
                                       bound, no uniqueness test.

The certificate lives in `CODEX_ANALYTIC_H41_RESEARCH_FREEZE_001` (`d5888b62…`),
`01_stage_I/computations/exact_base/rigorous_denominator_reconstruction.json`. Its mechanism: a rigorous
192-bit integer interval encloses `λ`, together with a **proved** denominator bound `q ≤ 24·d_max = 96`
(`d_max = 4`, the largest isogeny degree from the base); if exactly one rational of denominator `≤ 96`
lies in the interval, `λ` is pinned exactly.

**Re-audited here** (`computation/audit_lambda_certificates.py`), by exact integer arithmetic with no
float in the decision, at all eight levels the certificate covers:

    N       q≤    claimed   rationals with q≤96 inside the interval   unique   v₂
    62      96    1/4       {1/4}                                     yes      −2
    66      96    1/4       {1/4}                                     yes      −2
    114     96    5/4       {5/4}                                     yes      −2
    254     96    3/4       {3/4}                                     yes      −2
    258     96    3/4       {3/4}                                     yes      −2
    4098    96    7/4       {7/4}                                     yes      −2
    16382   96    9/4       {9/4}                                     yes      −2
    16386   96    81/4      {81/4}                                    yes      −2

Interval widths run from `9.0e−56` at `N = 62` to `7.0e−41` at `N = 16382`, against a minimum separation
of `1/(96·95) ≈ 1.1e−4` between distinct rationals of denominator `≤ 96`. Every certificate input digest
the file recorded still matches the bytes on disk — 24 of 24, zero mismatches
(`computation/verify_certificate_inputs.py`).

The certificate's load-bearing theorem dependencies, recorded because they are assumptions and are **not**
re-proved anywhere in this project: semistable modularity; semistable optimal Manin constant 1;
Manin–Drinfeld rational cuspidal torsion; Mazur rational torsion exponent `≤ 12`; full real period
`c_∞ ≤ 2`; complete rational isogeny class with minimal-isogeny differential transport; modular Mellin
formula with coefficient bound; AGM real-period formula.

**So the correct statement of where the seed's 2-adic valuation stands:**

    v₂(λ) = −2 is CERTIFIED at N = 62, 254, 16382   (negative branch)
                          and at N = 66, 114, 258, 4098, 16386   (positive branch)
    v₂(λ) = −2 at N = 262142 is SUPPORTED, NOT CERTIFIED.

**The defect in `ADDENDUM_007` §5, recorded not repaired.** Its table printed all four values as bare
rationals with no category marking, and — the substantive fault — drew no line between the three
certified levels and the uncertified fourth. The prose said "numerical confirmation"; a reader takes the
table. The heading "tested numerically at four levels" also understates three of the four rows and
overstates the fourth.

## 2. No circularity: the λ certificate is independent of `a`, so `ADDENDUM_007` is a genuine cross-check

It would be natural to suspect the `16382` λ certificate of presupposing the very optimality that
`ADDENDUM_007` later determined — one of its dependencies is "semistable optimal Manin constant 1". It
does not. The reconstruction script states at line 6:

> No database, floating point, or guessed optimal representative is an input.

and builds its denominator bound to be **agnostic** about which class member is optimal —
`d_max = max(degrees[0]); den_bound = 24*d_max` — while taking the period of the **minimal model**, not
of a selected optimal representative. That is exactly why the bound is `96` rather than something
smaller.

Three consequences:

1. The certificate does not presuppose `a = 0`. Had the kill test fired, the λ values would have stood.
2. `ADDENDUM_007`'s optimality determination is **logically independent** of the certificate, not
   circular with it. `λ` is base-normalised; `a = −v₂(Ω₀/Ω_E)` compares optimal to base. Different
   quantities, disjoint inputs — the certificate uses no database, `ADDENDUM_007` uses nothing but.
3. Their agreement on `λ = 9/4` at `N = 16382` is therefore a real independent cross-check, and it
   incidentally validates `ecdata`'s `real_period` and `special_value` columns at that level against a
   rigorous interval.

Taking §1 and `ADDENDUM_007` together, at the three negative levels where **both** are known —
`N = 62, 254, 16382` — we have `v₂(λ) = −2` certified and `a = 0` established, hence
`v₂(w_ℓ) = a = 0`: `w_ℓ` odd. At `N = 262142`, `a = 0` is established but `λ` is only supported.

## 3. A certified route to `N = 262142` exists and is cheap — recorded as available, deliberately NOT run

The denominator-reconstruction route needs 2000 Dirichlet coefficients, an AGM real period, a
192-bit interval and an isogeny-degree bound. It needs **no modular symbols**. It certified `16382` and
`16386` without touching `msinit`, so it is not blocked by the genus-2047 wall that stopped
`ADDENDUM_006`, and it would very likely certify `262142` — and possibly `n = 19` — at similar cost.

It is **not run here**, by the operator's directive to stop numerical level checks and move to proof
construction. Recorded so the option is visible and need not be rediscovered. Upgrading `117/4` from
supported to certified would change no conclusion in this programme: no finite level decides the uniform
statement.

This does not soften `ADDENDUM_007` §2. That section concerned `a` — which curve is optimal — for which
the modular degree was the wrong tool and `ecdata` the right one. `λ` is a different quantity by a
different route. No conflation, and no retroactive excuse for the four failed jobs.

## 4. No known rational-torsion theorem closes `(L)` — recorded from the operator's literature check

Recorded as handed in by the operator, **not independently verified in this object**; no literature
search or browsing was performed here, and this is not a novelty or priority claim.

* Ohta's squarefree-level theorem covers primary torsion **away from 6**.
* Yoo's later theorem handles primes **`≥ 5`**, plus certain 3-primary cases.
* Yoo–Yu (2025) determine the rational **cuspidal** subgroup — which is *not* a theorem that every
  rational 2-torsion point of `J₀(2p)` is cuspidal.
* Recent overviews still describe the full generalized Ogg conjecture as **unresolved at precisely these
  exceptional primary parts**.

The gap is exactly our case: the **2-primary part at even level** `2 | N`. So

    (L)  J₀(2p)(ℚ)[𝔪] = 𝔽₂·T_p

is **not** made automatic by known results, and no theorem has been overlooked that would close it. The
sufficient criterion remains a criterion, and remains unproved.

## 5. The target narrows from `(L)` to `(C′)`

`(L) ⟹ (C′)`, and `(L)` may be **strictly stronger than necessary**. Characteristic-2 multiplicity one
can fail globally while the one cuspidal line we care about still maps exactly where required.
Accordingly `(L)` is **retired as the object of proof** and `(C′)` replaces it:

    (C′)      T_p = π̂(S₀)     in  J₀(2p)[2].

**The statement to attack, in the operator's formulation:** *the unique order-two point in the cyclic
subgroup generated by `[0] − [∞]` lies in the embedded optimal H41 elliptic factor of `J₀(2p)`.*

A precision note on the closed form. With `div(F_p) = k([0] − [∞])`, `k = (p²−1)/8`, the written formula

    T_p = ((p²−1)/16)·([0] − [∞])

equals that unique order-two point precisely when `v₂(ord([0]−[∞])) = v₂(k) = n−2`; the order of
`[0]−[∞]` divides `k` but is not asserted equal to it anywhere in this record. The **order-theoretic
description is the robust one** and should be treated as the definition; the closed form carries that
prerequisite. Recorded as a prerequisite to be discharged, not as a defect in the formulation.

What a proof must engage: the Hecke action, the old/new decomposition at level `2p`, and the optimal
quotient map. **No L-values appear.** That is the point of the narrowing — it moves the remaining work
out of central-value computation entirely and into the integral/Jacobian identification.

## 6. A second and SEPARATE question — uniform Γ₀-optimality of the negative base

    Is the explicit negative-H41 base curve Γ₀(N)-optimal for every admissible p?

Four accessible cases say yes: `n = 5, 7, 13, 17`, from `ADDENDUM_007`. Proving it would establish
`a = 0` **uniformly** and remove an entire branch of the eta-character ambiguity.

Three disciplines on it:

* It **does not prove `(C′)`** and must not be conflated with it. It removes an ambiguity; it does not
  supply the identification.
* Its evidence is four levels, from an external database, of an index set **not known to be infinite**.
  It is recorded as a question worth investigating, **not promoted to a conjecture** here.
* It is a distinct theorem from `(C′)` with a distinct proof obligation, and should be worked, if at all,
  as its own item.

## 7. Directives recorded

* `ADDENDUM_007` preserved exactly as sealed. Not modified, not superseded.
* **No further numerical level checks.** In particular no `n = 19` computation, and the §3 route above is
  recorded rather than executed.
* Next useful work is **proof construction around `(C′)`**, not more levels.
* Standing: no Gate C, no novelty or priority analysis, no Lean commissioned, no Aristotle or Codex run.

## 8. Status of the negative branch

    Θ_p ≡ f_H41 (mod 2)            PROVED, symbolic, uniform in p.
    a = 0                          n = 5, 7, 13, 17, from proved Γ₀-optimality.
    v₂(λ) = −2                     CERTIFIED at N = 62, 254, 16382; supported at 262142.
    w_ℓ odd                        follows at N = 62, 254, 16382.
    χ_p = α_p (mod 2)              forced at N = 62; genuinely verified on full homology at
                                   N = 254; compatible with a = 0 at 16382 and 262142.
    (L)                            sufficient, stronger than needed, and NOT closed by any
                                   known rational-torsion theorem — the gap is the 2-primary
                                   part at even level.
    (C′)                           THE remaining target. Integral/Jacobian identification.
                                   No L-values. Unproved.
    positive branch                entirely outside this eta-2p architecture, untouched.

The route has survived two further kill tests and one narrowing. Nothing in this object advances the
mathematics; it fixes what the record claims and states what is left to prove.

**The H41 seed remains unproved.**
