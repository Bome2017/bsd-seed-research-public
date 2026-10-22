# Review of Aristotle run 2 (return on the 2026-09-20 invention packet)

2026-09-22. `returned_run2.tar.gz`, sha256 `ca59c470195cd4f88569ee9cb8b744ff31d67d4ea7f99604452abbe11fdc42a1`,
112 668 bytes. Four Lean files, **all `sorry`-free** (0 occurrences across `Main`, `ShaThreshold`,
`CoverCalculus`, `SeedData`). Note: this is a return on the **earlier invention packet**, which shipped with the
arrow-orientation error — see §3 and §5.

## Recorded verdict

    NO_SURVIVOR_FOUND_IN_THIS_BOUNDED_SEARCH.        ENDPOINT EFFECT: NONE.

Not `NO_SURVIVOR` as returned. Its own text concedes no proof of the theta nonvanishing for even one `p`, no
K1-K5 kill condition, and no impossibility theorem. The route reached a new arithmetic problem it could not
solve; that is an operational stop, not a no-go.

## Retained — three items

1. **Restriction coverage.** `Sha(E/Q)[p^inf] --> Sha(E/K)[p^inf]` is injective for odd `p`, the kernel being
   killed by `[K:Q] = 2`. Formalized abstractly in `CoverCalculus.lean` ("every element of the kernel is killed
   by 2"). **This receives the whole unknown primary quotient** — not the known Mordell-Weil plane, not selected
   classes. The admission geometry is genuinely different from the earlier failures.
2. **The first unproved arrow, precise.** `ord_triv Theta_{E/K,p} <= 2`, equivalently the degree-two component of
   the anticyclotomic theta element `Theta_{E/K,p}` in `Z_p[[Gamma]]` is nonzero mod `p`, uniformly over the
   relevant ordinary tail. The intended chain is `corank Sel_{p^inf}(E/K) <= ord_triv Theta`. A real arithmetic
   bottleneck, not "find some comparison".
3. **The 2-descent reading of the coordinate coincidence.** With `a = -5*4547` and `b = 4*4547*5843`, the cofactor
   at `x = 4547` is `4547*(4547 - 5*4547 + 4*5843) = 4547*5184 = 4547*72^2`, so the point over `x = 4547` is
   forced and `4547` is exactly the 2-descent class `delta_2(P_1)`; the companion is `x(P_2) = 5184 = 72^2` with
   `delta_2(P_2) = 1`. Arithmetic checked here. A clean interpretation of the previously uninterpreted datum —
   and, as the run itself says, **2-descent only, with no odd-primary consequence and no FIN effect.**

## Correction 1 — equivalence is not grounds for rejection

`ARISTOTLE_SUMMARY.md` §8: *"on the good-ordinary tail the arrow above is equivalent to the vanishing it was
meant to produce — an equivalence, hence `NO_SURVIVOR` rather than `NEW_LEMMA_ONLY`."* That inference is wrong
under the rule this project already fixed: **an independently proved equivalent theorem would solve the problem.**
Equivalence means the route is not yet a demonstrated difficulty reduction; it does not make the route invalid.
The theta route **passed** the whole-Sha coverage gate and then failed later, at uniform nonvanishing.

## Correction 2 — the formal threshold layer is stale by two primary theorems

The largest concrete error. `ShaThreshold.lean` builds `coprime_210_iff` (2,3,5,7), `eq_nine_of_lt_1089`, and
`sharpness_1089`, with line 29 asserting *"With `Sha[7^inf] = 0` the correct sharp threshold is `9*11^2 = 1089`"*.
That is the **post-`p=7`** state. Since then:

    Sha[11^inf] = 0   and   Sha[13^inf] = 0,

so under FIN the current arithmetic is `#G = 9t^2` with `gcd(t, 30030) = 1`, the least admissible `t > 1` is 17,
and the exact endgame is

    #G < 2601  =>  #G = 9.

The Lean theorems may be perfectly valid under their stated hypothesis (`t` coprime to 210), but
**`sharpness_1089` must not enter the live canonical record as current sharpness**, and the summary's claim that
this *"corrects the project's formal layer"* is itself outdated.

**Cause, stated plainly.** `ARISTOTLE_SUMMARY.md` says it is correcting the A1/A2 layer's 441 (`gcd(t,30)=1`)
upward. It took 1089 from the 2026-09-20 invention packet — which I built, and which **hard-coded** the number.
P11 landed that same evening and P13 the next day. So one stale constant was "corrected" to another stale
constant, and the drift propagated into a machine-checked theorem. This is the concrete realization of the risk
flagged when the 1089 -> 1521 drift was first noticed: **a package must cite the master's threshold line, never
copy the value.** Any reissue must do so.

## Correction 3 — the `p`-independence claim needs scope

`VERDICT.md` line 87 and `ARISTOTLE_SUMMARY.md` §8: *"Every currently available way to bound `Sha` in analytic
rank two ends in a degree-two component of a `p`-adic object at a `p`-dependent auxiliary level."* At best a
search conclusion over the mechanisms examined. It is not formalized by any of the four Lean files and does not
imply that no integral theta / Fitting / determinant construction exists. Preserve:

> this attempted definite-anticyclotomic construction still leaves a `p`-dependent nonvanishing problem

and not the universal claim.

## The relocated frontier diagnosis — what the two runs jointly establish

Run 1: the `-23` rank-three/Stark lane cleans up so that, outside the finite support of the rank-one twist's Sha,
failure of `I_3(p)` is genuinely about the seed — but no `p`-independent model of `I_3` was constructed.
Run 2: a definite anticyclotomic theta construction **satisfies the whole-Sha coverage requirement** and then
terminates at uniform nonvanishing of a `p`-dependent degree-two theta coefficient.

Together they support a narrower and more useful statement than the earlier framing:

> **The obstruction is no longer "wrong arrow direction."** Both architectures can be arranged to see the whole
> unknown quotient. What neither supplies is a **prime-uniform arithmetic witness whose nonvanishing or defect is
> controlled by one fixed integral object.**

That supersedes the "everything dies because the maps go the wrong way" framing, which was wrong on its own terms
and has already been withdrawn.

## Status set

    TAIL_FINITE_SUPPORT                 = OPEN
    STARK_FIXED_INTEGRAL_MODEL          = OPEN
    DEFINITE_THETA_UNIFORM_NONVANISHING = OPEN
    FIN                                 = OPEN
    CURRENT_CONDITIONAL_THRESHOLD       = 2601

**Do not run `p = 17` on the basis of either return.** Neither converted the infinite tail to a finite
exceptional set containing 17.
