# Corrections to TWIST_AND_IDEAL_ATTEMPT — accepted, with independent verification

Date 2026-09-21. **Additive.** Supersedes §A.3, §A.4 and §B.2 of `TWIST_AND_IDEAL_ATTEMPT.md`; that file is preserved
unedited. Authority: `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/MCS_TWIST_IDEAL_REVIEW.md`.

## C1. The cost estimate was wrong, and the error was in my favour's direction — twice over

**What I did wrong.** I calibrated against "8 444 396 certified coefficients". That figure is the count of **prime**
coefficients *verified*; the run's **summation cutoff** was `1.5 x 10^8`. Scaling the cutoff linearly in `|D|` for
`D = -23` gives

    150,000,000 x 23 = 3,450,000,000  =  3.45e9,

not the `1.94e8` I reported. **I understated the requirement by a factor of 18.**

**And the correction makes the situation better, not worse.** Verified independently from
`_work/active_full_bsd/p11/RESUME.md`: the C11 run's bounded input extent is

    T = 39,141,244,927  (= 39.14e9),  as 2333 segments of length 2^24,

and `2333 x 2^24 = 39,141,244,928 = T + 1` exactly. The prefix needed for `D = -23` is
`ceil(3.45e9 / 2^24) = 206` segments — **precisely the 206 the review reports hash-verified** — with `11.3x` headroom
remaining in the existing corpus.

**So the coefficient generation for the cheapest twist is already done.** My framing of "23x the existing run" was
wrong in both the base quantity and the conclusion: this is not a new production run at all.

What genuinely remains, and what the review states is *not* established: the twisted derivative calculation, a
certified error bound, the runtime of either, and whether `3.45e9` is an adequate cutoff. I record that last point as
open — my linear scaling of the cutoff is a heuristic, not a theorem about where the approximate functional equation
may be truncated for the twist.

## C2. The coverage statement was too broad in its summary line

My precise statement ("with a **fixed finite** set of `k` discriminants the uncovered density is `2^{-k}`") then became
the summary "**on its own it cannot reach the uniform tail that FIN requires**". That overreaches, in two ways:

1. The exponent is `2^{-r}` with `r` the number of **independent** quadratic characters, not the number of
   discriminants. Multiplicatively dependent `D_i` do not each halve the uncovered set.
2. More importantly: the argument assumes `K` is drawn from a **fixed finite** collection. **It says nothing about a
   uniform argument in which `K` varies with `p`.** Excluding that was not licensed by anything I proved.

Correct scope: *any finite fixed collection of these imaginary twists leaves infinitely many primes uncovered.* Full
stop. This is the same failure mode I was corrected for twice earlier in this thread — the precise sentence was
defensible and the summary sentence was not — and it is now the third instance. The pattern is mine, not the
mathematics'.

## C3. The Heegner index does not determine `I_3`

My §B.2 asserted that the ideals are determined by where `z^Hg_∞` sits relative to the integral lattice, "**i.e.** by
the Λ-index `[Sel(T) : Λ y_∞]`". That "i.e." is false. The review supplies an explicit algebraic counterexample:
identical index and characteristic-ideal data, with the same rank-three point-sized contribution, coexisting with
**different specialized Fitting ideals**. The full Selmer-complex information is what matters; the index is a lossy
shadow of it.

So the shortcut I proposed — read `I_3` off a Heegner index — is refuted. **This challenges my shortcut, not the MCS
theorem**, and it does not close the anticyclotomic route; it removes the cheap version of it.

## C4. `I_3`-vanishing was not new

The equivalence `I_3(ε^Hg_{1,0}) = F_p <=> Sha(E/K)[p] = 0` was already in the review. Rediscovering it adds no
obstruction and I should not have presented it as a finding. The `Fitt^i(F_p^d)` computation behind it is correct; it
was simply already known here.

## C5. Corrected status

| item | status |
|---|---|
| admissible twist set (`D = -23, -143, -863, -1031, ...`) | stands |
| `w(E^D) = -1` for every candidate, no computation | stands |
| coefficient corpus for `D = -23` | **already exists** — 206 of 2333 segments, hash-verified, 11.3x headroom |
| twisted derivative calculation + certified error bound | **open**, runtime unestablished |
| adequacy of the `3.45e9` cutoff | **open** — my linear scaling is heuristic |
| finite-twist coverage | infinitely many primes uncovered for any **fixed finite** collection; says nothing about `K` varying with `p` |
| `I_3` from the Heegner index | **refuted** by explicit counterexample |
| `I_3` evaluation | not supplied; no method |

Neither arithmetic deliverable is supplied. The twist calculation has a concrete reusable input substantially stronger
than I recognized. FIN, ORDER9, Q36 open. Nothing modified.
