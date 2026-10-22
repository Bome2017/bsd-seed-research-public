# Synthesis after both Aristotle revisions

2026-09-22. Both runs returned revisions at 18:43 that **applied the review corrections**. This file records what
actually moved and what did not.

    run 1 rev 2 : returned_run1_rev2.tar.gz  sha256 ebe4701471a86c2957782a36f1f9eb985558c89fa648eb21fa539acae8ecbc77
    run 2 rev 2 : returned_run2_rev2.tar.gz  sha256 9d65388b2389533e3bbe89714b464d06f3bbd5fb640860e3f5d6987ad245f494

## 1. Run 1 rev 2 — a genuine strict reduction inside a stated sub-class

The value is **not** the earlier finite-support equivalence. It is `effective_constant_of_integral_model`, with
`minorGcd_ne_zero_of_unit_prime`. Verified in `RequestProject/Main.lean`, `sorry`-free:

    def minorGcd (A : Matrix (Fin m) (Fin n) Z) (k : N) : Z
    def SpecializesTo A k Lane I3unit : Prop :=
      forall p prime, Lane p -> ( I3unit p  <->  some k x k minor of A is != 0 in ZMod p )

    theorem effective_constant_of_integral_model (hspec : SpecializesTo A k Lane I3unit)
        (p0 prime) (Lane p0) (I3unit p0) :
      minorGcd A k != 0  AND  forall lane p, ¬ I3unit p -> (p : Z) | minorGcd A k

So for the matrix-presented sub-class `C_mat`, the downstream half is **discharged**:

    OLD bottleneck = construct integral model  +  extract an effective C_1
    NEW bottleneck = construct integral model  +  prove the specialization

**Nondegeneracy is free.** `minorGcd_ne_zero_of_unit_prime` shows one lane prime with `I_3(p_0) = F_{p_0}` forces
`minorGcd A k != 0`; the docstring names `p_0 = 13`, where `Sha[13^inf] = 0` is retained input. So "the model has a
nonzero invariant" never has to be assumed.

Also present: `lane_support_subset_divisors_of_integral_model` (the lane support lands in the explicit divisor set),
`no_integral_model_of_infinite_lane_support` (contrapositive), and
`effective_constant_of_integral_model_off_finite_set` — which already has the shape needed for a `Z[1/N]`
presentation, where cleared denominators merely enlarge a finite exceptional set.

`minorGcd` is computable and kernel-checked: `minorGcd exampleModel 2 = 12` for `!![6,10,4; 0,2,8]`, independently
confirmed here (2x2 minors `12, 48, 72`, gcd `12`; and `minorGcd _ 1 = 2`).

**`C_mat` is not artificial.** Finitely presented modules and Fitting ideals come with presentation matrices, so if the
sought `p`-free `I_3` model is an integral Fitting object, this is precisely the algebra wanted downstream.

**It does not move FIN:** `A` has not been constructed, and the specialization is a hypothesis.

## 2. Run 2 rev 2 — record repair, no arithmetic arrow

`VERDICT_CORRECTED.md` changes the verdict to `NO_SURVIVOR_FOUND_IN_THIS_BOUNDED_SEARCH`, repairs the threshold layer,
and scopes the stated obstruction. New `ShaThreshold2601.lean` (`sorry`-free) carries `coprime_30030_iff` and
`sharpness_2601`: under FIN and the retained inputs `#Sha = 9t^2` with `gcd(t, 30030) = 1`, least admissible `t > 1`
is 17, so `#Sha < 2601 => #Sha = 9`, and 2601 is numerically sharp given those inputs.

Its durable contribution is keeping the **definite-theta construction live rather than killed**. That route passes the
global-coverage gate — `Sha(E/Q)[p^inf] --> Sha(E/K)[p^inf]` injective for odd `p`, kernel killed by 2 — and stops
later at `ord_triv Theta_{E/K,p} <= 2`, uniformly in `p`.

## 3. The common frontier

    Stark lane wants:         one fixed integral object whose reductions govern I_3(p).
    definite-theta lane wants: one prime-uniform witness governing the degree-two theta term.

These are the **same question**: is the currently `p`-adic witness the specialization of a single integral,
prime-independent object? Hence

    PRIME_UNIFORM_INTEGRAL_WITNESS = OPEN

and **not** "maps have the wrong direction", **not** "rank two makes this impossible", **not** "`I_3` is `p`-dependent,
end of story".

## 4. Status, unchanged by either revision

    FIN = OPEN     FORMULA = OPEN     TAIL_FINITE_SUPPORT = OPEN
    STARK_FIXED_INTEGRAL_MODEL = OPEN     DEFINITE_THETA_UNIFORM_NONVANISHING = OPEN
    CONDITIONAL_THRESHOLD = 2601          p = 17: still not justified as the next computation

Compared with two rounds ago the research question is substantially narrower: **construct the integral ancestor of one
of the two working `p`-adic witnesses.**
