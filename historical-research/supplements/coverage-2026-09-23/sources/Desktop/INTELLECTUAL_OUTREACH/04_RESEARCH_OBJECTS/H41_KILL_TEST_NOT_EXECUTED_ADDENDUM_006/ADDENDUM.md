# Sixth addendum — the N = 16382 kill test was not executed

**Tier: NEGATIVE OPERATIONAL RESULT.** No mathematical claim is made or withdrawn here. Prior objects
unmodified: `ac82f3ad…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`, `3eb98a60…`.

`H41_ETA_CONGRUENCE_ADDENDUM_005` §7 fixed the kill condition in advance:

    a = 1  ⟹  (C) fails.      a = 0  ⟹  merely another survivor.

This object records the outcome of attempting it, judged under that condition rather than folded back
into the fifth object.

## Result

    a at N = 16382 is UNDETERMINED.
    The kill condition is NEITHER MET NOR FAILED — it is untested.
    (C) is NOT supported and NOT refuted by this attempt.  No inference either way.

The only executed finite diagnostic of the mechanism remains `N = 254`.

## Why

Determining `a = −v₂(Ω_optimal/Ω_base)` requires identifying the Γ₀-optimal member of the isogeny
class. The criterion that worked at `N = 62` and `N = 254` is the modular degree, which the optimal
curve minimises. Four attempts, none returning a value:

    1  ellmoddegree, default stack           PARI stack overflow
    2  parisizemax 12 GB, stack 4 GB         exited 0 with nothing computed
    3  parisizemax 24 GB, stack 8 GB         died silently, no output written
    4  msinit(16382,2,1) alone, 2 GB stack   no completion within 420 s

**The wall is the modular-symbol space construction, not `ellmoddegree`.** `X₀(16382)` has genus 2047,
so the plus-part space has dimension in the low thousands, and `msinit` alone does not finish. Any route
to `a` at this level that passes through modular symbols is blocked with the tooling present. Sage or
Magma, or a machine with substantially more memory, is what would execute it.

## An operational error of mine, recorded

Attempt 3 requested a **24 GB PARI stack on a 16 GB machine** — unsatisfiable by construction, and it
turned a diagnosable failure into a silent one. During attempts 3 and 4 free pages fell to roughly 3900
(about 15 MB): the host was thrashing. I terminated both PARI jobs to protect it and free pages
recovered to about 36000; swap use was unchanged at 1114 MB of 2048 MB before and after. Stack requests
must be bounded by physical RAM, and a long-running job on this host must be checked against free memory
rather than launched and left.

## What did land at N = 16382

Already frozen in `ADDENDUM_005`, and unaffected — these need only `ellinit`, `ellisomat`, `ellap`,
`ellan`, all cheap:

* `(B) Θ_p ≡ f mod 2`, zero mismatches over `m = 1..4000`;
* isogeny degree matrix `[1,2,4,4; 2,1,2,2; 4,2,1,4; 4,2,4,1]`, identical to `N = 62, 254`;
* real-period ratios `1 : ½ : ½ : ¼`, identical to `N = 62, 254`;
* Eisenstein conditions: `a₂ = 1`, `a_p = −1` both odd, `a_ℓ` even for good odd `ℓ < 200`.

What is missing is only the optimality determination, hence only `a`.

## What this does not license

The structural identity of the isogeny graph, the period ratios and the Eisenstein data across all three
levels makes `a = 0` at `N = 16382` plausible. **That is not a determination and is not recorded as
one.** The kill test remains open, and the architecture's evidentiary position is unchanged from
`ADDENDUM_005`: one forced case at `N = 62`, one genuine test at `N = 254`, and the uniform congruence
(B).

**The H41 seed remains unproved.**
