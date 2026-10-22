# TWIST_D7_CENTRAL_VALUE_NONZERO_CERTIFIED

Date 2026-09-22. Local computer-assisted certificate with written error bounds.

## Result

    L(E^{-7}, 1)  in  [ 9.054319 , 9.054421 ]        (outward-rounded, / 10^6)

so `L(E^{-7},1) != 0`, and it is positive. The twist has root number `+1` (established at gate stage 1:
`chi_D(N) = (-1)^{|N^-|} = -1`, so `w(E^D) = -chi_D(N) = +1`), so this is the central value and the analytic rank of
`E^{-7}` is **0**.

By the retained Gross–Zagier–Kolyvagin theorem at analytic rank zero:

    rank E^{-7}(Q) = 0        and        Sha(E^{-7}/Q) is finite.

**Nothing further is claimed.** No BSD statement, no leading-term or order formula, no order of any `Sha`, no new
primary component of the seed, and no statement about FIN, ORDER9 or Q36.

## Numerical certificate

    T          = 2,013,265,919   (120 complete retained segments of 2^24)
    c          = 2 pi / (7 sqrt N) = [1.11306024996424415572731700584e-8 +/- 2.51e-38]
    2 S_T      = [9.05436995266740316598495882372 +/- 6.28e-30]
    tail bound = [5.068075129247713082248669e-5  +/- 4.28e-30]
    L-value    = [9.0544 +/- 8.08e-5]
    interval   = [9054319, 9054421] / 10^6
    ZERO_EXCLUDED 1     POSITIVE 1
    margin |2 S_T| / B  =  1.79e5

Count identity: `660,934,050 + 1,352,331,869 = 2,013,265,919 = T`.
`AP_SEGROOT_SHA256 99b4799501a07acf0e52d1bec98e0cb27dc579ac8c1c29b99e1293c16c848103` over 120 segments.
`SMOOTH_MERKLE_SHA256 a39ef9d4569c9c9d05f1df1b12c54e02fcb8a4c8380a1b4d5836cc163fae49d3` over 480 blocks.

Run: 600 units, 12 workers, ~4.5 min wall, peak RSS **0.83 GB** on a 16 GiB host. Table-free traversal throughout;
no dense `O(T)` allocation.

## Mathematical contract

    L(E^D,1) = 2 * sum_{n>=1} chi_D(n) a_n / n * exp(-c n),    c = 2 pi / (|D| sqrt N)

with `D = -7` fundamental, `D = 1 mod 4` so `chi_D(n) = (n/7)`, and `gcd(7, N) = 1` so the twist has conductor
`49 N` and `sqrt(49N) = 7 sqrt N`. The tail satisfies

    | 2 sum_{n>T} |  <=  2 * tail_MS(c, T),
    tail_MS(k,T) = [ 2 sqrt T + ( (log T + 2)/k + 1/(k^2 T) ) / sqrt T ] * exp(-k T)

`tail_MS` is the retained engine's own elementary tail. The central value is the **base case** of the family the
sealed adapters already used: the first-derivative adapter's tail is `2 tail_MS/(cT)` and the `L''` mode's is
`2[..]/(cT)^2`, both coming from `E_1(x) <= e^{-x}/x`. **Cross-checked:** recomputing `2 tail_MS(c_23, 3456106495)/(c_23 T)`
gives `0.335041797048` against the sealed `D = -23` run's recorded `0.335041797049`.

## Cutoff discipline

No cutoff was chosen in advance. The tail function was tabulated first as a **stopping criterion**
(`T = 1e9 -> 3.75`, `2e9 -> 5.9e-5`, `3e9 -> 9.4e-10`), and the run stopped at the first admissible `T` whose computed
interval rigorously excludes zero. It did, with a 1.8e5 margin, so no larger cutoff was executed.

## Validation performed

| check | result |
|---|---|
| `EXP_TEST` — working-precision weight vs higher precision, 10 bases x 128 offsets | 1280 checked, **0** non-overlaps, max radius 3.56e-39 |
| `BLOCK_TEST` — traversal vs independent trial-factorisation coefficients and direct Arb, 7 blocks | 448 terms, **0** failures, all overlap |
| `chi` table vs Euler's criterion mod 7 | agrees on every tested `n` |
| fresh deterministic recombination | **byte-identical** ball dumps (`PARTIAL/TAIL/LVALUE`) |
| **independent end-to-end replay** at `T = 16,777,215`, separate implementation (numpy spf sieve + multiplicativity + `math.fsum`), sharing only the raw `a_p` bytes | engine `9.28074326789452806960721098863`, independent `9.28074326789452896946`, **diff 1.8e-15** (float64 roundoff) |
| independent tail recomputation (mpmath, 40 dps) at the certificate `T` | matches engine to 22 significant digits |
| `a_p` spot checks | `a_5,a_7,a_11,a_13 = -2,-2,-2,-4`; `a_2243 = 1`, `a_4547 = 0`, `a_5843 = -1` |
| **corpus integrity** | **0** `ap_*.bin` segments modified during the run; the 2026-09-21 write-through-symlink failure mode did **not** recur |

## Trust base and limits

This is a computer-assisted certificate resting on: the retained `a_p` corpus and its segment hashes, the retained
FLINT/Arb runtime, the retained engine source (`retained_arbcore.c`, sha256
`56a43aac38161d48848df4ed5c2f931f1dc7d5db745600bd140e4be3cac67fd7`, byte-identical to the sealed C11 engine), and
this new isolated adapter. It is **not** a Lean proof, not a fresh witness re-verification of the whole coefficient
corpus, and not independent human review. The GZK step is a retained theorem, applied, not reproved.

## Why this was computed

Gate stage 7: the anticyclotomic derived-height inequality forces `d^+ = 0` but leaves `d^- in {0,1,2}`. Only a
rank-zero twist certificate removes those rows, because GZK at analytic rank 0 supplies **both** `r^- = 0` and
finiteness of `Sha(E^{-7}/Q)`, hence `d^- = 0`. See `~/BSD_DEFINITE_FIELD_GATE_2026-09-22/STAGE7_A2A_ROUTE_LIVE.md`.
What that yields downstream remains conditional on `[c_2] != 0` and on the module identification, both open.
