# D = -23 certificate: independent checks, and which primes it serves

Date 2026-09-21. Records checks on `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21/RESULT.md`
and one consequence not stated there. Nothing launched.

## 1. Certificate arithmetic reproduces

    2S_T = 39.847278312318874 +- 4.28e-16   at T = 3,456,106,495
    B_{-23}(T) <= 0.335041797049

    2S_T - B = 39.512237  -> RESULT lower bound 39.512236  (outward-rounded down)  OK
    2S_T + B = 40.182320  -> RESULT upper bound 40.182321  (outward-rounded up)    OK
    margin |2S_T| / B = 118.9x

The tail figure is consistent with my own evaluation of (2): I computed `B(3.45e9) = 0.342643`, and the run's slightly
larger `T = 3,456,106,495` gives `0.335042`. Same function, same value.

## 2. My cutoff verdict was wrong in the event, not merely unproved

RESULT: *"The original cutoff is therefore adequate; the seven-billion extension was unnecessary and was not executed."*

`|L'| ~ 39.85` against a tail of `0.335` is a **119x** margin. I had called `3.45e9` "not adequate" on the basis that it
would need `|L'| > 0.343` — a condition that was in fact satisfied by two orders of magnitude. The review's verdict
("undetermined until the interval exists") was the correct epistemic position, and the outcome shows the cost of
substituting a guess for it: had the recommendation been followed, the run would have done 2x the necessary work.

Two other corrections also land as measured: peak RSS **1.00 GB** (against a dense path I never checked, which would
have needed 26.1 GiB), and runtime **708.40 s** with twelve workers — my ~6-minute streaming anchor was within a factor
of two, but of a quantity I had mislabelled as the whole cost.

## 3. New: which primes the certified premise actually serves

The comparison needs regime (P) **and** `p` split in `K = Q(sqrt -23)`, i.e. `(-23 | p) = +1`. Using `a_p` read from the
retained corpus:

| `p` | `a_p` | `#E(F_p)` | ordinary | `p ∤ #E` | `(-23\|p)` | served |
|---|---|---|---|---|---|---|
| 5, 7, 11 | -2, -2, -2 | 8, 10, 14 | yes | yes | -1 | no |
| **13** | **-4** | **18** | **yes** | **yes** | **+1** | **YES** |
| 23 | 0 | 24 | no (ss) | yes | 0 (ramified) | no |
| 29, 131 | 0 | - | no (ss) | yes | +1 | no |
| 31, 41, 47, 71, 73, 101, 127, 139, 151 | - | - | yes | yes | +1 | YES |
| 59 | -4 | 64 | yes | yes | +1 | no — in the excluded set {19, 59, 487} |

Served up to 160: **13, 31, 41, 47, 71, 73, 101, 127, 139, 151**.

**`p = 13` is served, and 13 is the threshold-determining prime**: the current bound `1521 = 9 * 13^2` is exactly what
`gcd(t, 2310) = 1` leaves once `2,3,5,7,11` are excluded. So the newly certified premise lands on the next prime that
could move the threshold — and independently, the 2026-09-21 Aristotle archive supplied Lean-checked reduction data at
13 (`#E(F_13) = 18`, `a_13 = -4`), which I verified by direct point count.

`p = 11` is **not** served (`(-23|11) = -1`), which costs nothing since C11 already settled it.

This is a statement of coverage, not a proposal. Evaluating `I_3` at any served prime remains the unevaluated
obligation, with no method; the certificate supplies a premise, not a Sha bound.
