# Seventh addendum — the N = 16382 kill test, executed by database lookup: `a = 0`

**Tier: EXECUTED FINITE DIAGNOSTIC — SURVIVOR, NOT SUPPORT.** No mathematical claim of the programme is
proved or withdrawn here. Prior objects unmodified and byte-identical: `ac82f3ad…`, `82b6730f…`,
`81ac107b…`, `35f21882…`, `0bfb6b5e…`, `3eb98a60…`, `da70ec51…`.

`H41_ETA_CONGRUENCE_ADDENDUM_005` §7 fixed the kill condition in advance:

    a = 1  ⟹  (C) fails.      a = 0  ⟹  merely another survivor.

`H41_KILL_TEST_NOT_EXECUTED_ADDENDUM_006` recorded that the test had **not** been executed, because four
attempts to reach `a` through the modular degree died on the modular-symbol construction. That object
stands unmodified and remains a true record of the modular-symbol route. This object records that the
test has now been executed by a **different and much cheaper route**, and the outcome under the
pre-fixed condition.

## 1. Result

    a  at  N = 16382   =   0.
    The kill condition  a = 1  is NOT met.  (C) is NOT refuted.
    (C) is NOT supported either: a = 0 is, by the rule fixed in advance, merely another survivor.

And at no extra cost, a level never previously tested:

    a  at  N = 262142  (n = 17)  =  0.   Same route, same outcome.

The negative-branch levels for which `a` is now determined are `n = 5, 7, 13, 17`. The remaining two
known members, `n = 19` (`N = 1048574`) and `n = 31` (`N = 4294967294`), lie outside Cremona's database
and are untouched.

## 2. The route, and why `ADDENDUM_006`'s closing sentence was wrong

`a = −v₂(h)` with `h = Ω_{0,R}/Ω_{E,R}`, so `a` is determined the moment the Γ₀(N)-optimal member of the
isogeny class is identified. `ADDENDUM_006` reached for the modular degree, which the optimal curve
minimises, and hit the `msinit` wall at genus 2047. It then concluded:

> *Sage or Magma, or a machine with substantially more memory, is what would execute it.*

**That was wrong, and the error was mine.** The determination needed no computation at all on this host.
Cremona's `ecdata` records optimality directly, and the H41 base's minimal model is simply looked up:

    minimal model of the N = 16382 base  =  [1,-1,1,-87211,10000251]  =  Cremona 16382b1
    ecdata opt_man entry:  16382 b 1 [1,-1,1,-87211,10000251] 1 1
                                                             ^ ^
                                                             | Manin constant = 1
                                                             optimality flag = 1, i.e. PROVED OPTIMAL

so `E₀ = E`, hence `h = 1`, `v₂(h) = 0`, and `a = 0`. Identically at `N = 262142`, where the base's
minimal model is `262142c1`, also flagged `1 1`.

The same table also **already contains the modular degree the failed job was computing**:

    degphi(16382b1) = 91008        degphi(262142c1) = 15060864

The wall was never a compute wall. It was a failure to look for work already done. The general lesson is
one already on the record in this project and it was not applied: price the lookup before the run.

## 3. Why the flag means what is claimed

`ecdata`'s own parser (`scripts_files.py`, `parse_opt_man_line`) fixes the column semantics:

    N iso num ainvs opt mc
    opt = 0 not optimal | 1 optimal | n>1 one of n possibly-optimal curves in the class
    mc  = Manin constant, CONDITIONAL on curve #1 being the optimal one

So `opt = 1` is a **decided** optimality, distinguished in the data itself from the undecided case
`opt = n > 1`. Because curve #1 is the flagged curve here, `mc = 1` holds unconditionally for this class.

The cited documentation — optimal curve = curve number 1 for every conductor up to 370000, single
exception `990h3` — was **tested against the data rather than trusted** (`computation/threshold.sh`):

    curve records in the pulled range (N < 500000)   3064705
    records flagged opt>1 (undecided)                 140309
    smallest conductor carrying opt>1                  400002
    undecided classes strictly below 370000                 0
    below 370000, curves flagged optimal with number ≠ 1:  exactly one — 990h3

Both decisive levels, 16382 and 262142, are far below the first undecided conductor. The documented
exception is reproduced exactly. This is the external authority behaving as documented, not a
computation performed here.

## 4. Four independent legs under the identification

1. **The curve is the H41 base.** The model quoted in the commissioning message, `[1,-1024,0,262144,0]`,
   and the base `[0,-4095,0,4194304,0]` have equal conductor 16382 and equal
   `j = -73355527176398544897/562881233944576`; `ellisisom` returns the transformation `[2,0,1,0]`; both
   reduce to the same minimal model `[1,-1,1,-87211,10000251]`.
2. **The class is complete and correctly matched.** PARI's `ellisomat`, computed with no reference to the
   database, returns exactly four members whose minimal models are exactly the four of `ecdata` class
   `16382b`, with isogeny degree matrix `[1,2,4,4; 2,1,2,2; 4,2,1,4; 4,2,4,1]` — identical to the matrix
   frozen in `ADDENDUM_005` for `N = 62, 254`.
3. **The database reproduces the frozen modular degrees.** `ADDENDUM_005` §6 recorded `2, 4, 8, 8` at
   `N = 62` and `24, 48, 96, 96` at `N = 254`, obtained here months earlier by direct computation.
   `ecdata`'s `degree` column gives `2, 4, 8, 8` and `24, 48, 96, 96`. The two routes agree exactly, and
   curve #1 attains the minimum at all four levels — the criterion §6 used, now confirmed against
   Cremona's independent optimality flag.
4. **The kill condition was live, not vacuous.** Each class contains two curves of least-real-period
   ratio `½` to the base. Had either been the optimal member, `h` would have been `½` and `a` would have
   been `1`, firing the kill. The test was capable of failing; it did not.

## 5. The seed, tested numerically at four levels

The same tables carry `real_period` and `special_value`, so the seed itself can be checked. The H41 base
has `signD = −1` at every level — one real component — so `real_period` **is** the least real period for
exactly the curve in question and no component-count convention enters.

    N         λ = L(E,1)/Ω_{E,R}      4λ        odd?
    62              1/4                 1       yes
    254             3/4                 3       yes
    16382           9/4                 9       yes
    262142        117/4               117       yes

Agreement to ~30 digits. So `v₂(λ) = −2` at all four levels: the seed **holds numerically** wherever it
can be checked. As an independent consistency check on the very columns used, `L·|T|²/(Ω·∏c_p)`
reproduces the separately stored `sha_an` at all four levels — `1, 1, 1, 9`.

This is a numerical confirmation at four levels. It is **not** a proof of the seed, and the uniform
statement over all H41 is exactly what remains open.

## 6. A precision note on the recorded period ratios — values correct, ordering enumeration-dependent

`ADDENDUM_005` §6 and `ADDENDUM_006` record real-period ratios `1 : ½ : ½ : ¼`. Recomputed here on
minimal models by an independent method, the ratios of least real periods form the multiset
`{1, ½, ½, ¼}` at all four levels, with the base always the largest — so the recorded **values** are
correct and the inference resting on them is untouched. The per-index **tuple** is however
enumeration-dependent: in Cremona numbering it reads `(1, ½, ¼, ½)` at `N = 62, 254, 16382` and
`(1, ½, ½, ¼)` at `N = 262142`. The frozen tuples were in PARI `ellisomat` order. They should be read as
multisets; no index-wise identification of curves should be made from them. Recorded as a reading
correction, not an erratum in the values.

## 7. What this does not license

* `a = 0` at two further levels is **not** evidence for uniformity of `a = 0`, and the rule fixed in
  advance says so. Four levels, of a set not known to be infinite.
* Whether the `a` determination is **forced** at `n = 13, 17` — in the way `(C)` at `N = 62` was forced
  by `J₀(62)(ℚ)[2] ≅ ℤ/2` — is **not determined here**. Deciding that needs `J₀(2p)(ℚ)[2]` at these
  levels, which is the same modular-symbol computation that is out of reach. So the informativeness of
  these two survivals is itself undetermined, and no weight beyond "did not fire" should be placed on
  them.
* `ADDENDUM_005` §7 predicted `a = 0` as the likelier and less informative outcome on structural grounds.
  That prediction was correct, which further limits what the outcome adds.
* The uniform comparison `(C) χ_p = α_p mod 2` is untouched. Nothing here bears on proving it in `p`.
* **The positive branch remains entirely outside this eta-2p architecture.** There `N = 2·3·ℓ`, the
  eta quotient `F_p` is not even defined, and none of the above is meaningful. No positive-branch
  conductor was looked up, and none should be read as covered.
* The determination rests on Cremona's published `ecdata` as an **external authority**. It was not
  re-derived here, and the object records its digests so that the dependency is explicit and auditable.

## 8. Tooling errata recorded

Five defects, all mine, all found while doing this and none silently repaired:

1. **`awk '$1==16382'` on `curvedata` matches nothing.** In `curvedata` field 1 is the *label*
   (`16382b1`); the conductor is field 10. In `opt_man` field 1 *is* the conductor. The first lookup
   returned empty and could have been misread as "curve absent from the database".
2. **This `gp` build reads script files line-by-line.** A `for(...)` body split across newlines never
   closes: `syntax error, unexpected end of file`, after which every statement in the body executes at
   top level against undefined variables and emits a cascade of type errors that hides the real cause.
   Every loop in `computation/` is written on one line for this reason.
3. **`ellisomat(E,,1)` returns short `[a4,a6]` models** — recurrence of a trap already on this project's
   record. Each carries its own scaling, so periods taken from them are not comparable across a class.
   Minimal models must be formed first.
4. **`real(ellperiods(E)[1])` is not the least real period.** PARI's basis is real, purely imaginary, or
   neither depending on the curve; for `62a3` that expression returns `0`. The least real period is
   computed here as the smallest positive real element of the period lattice.
5. **zsh does not word-split unquoted variables** — recurrence of a defect already recorded in this
   project. A `for spec in …; set -- $spec` loop collapsed four arguments into one and printed an empty
   table. `computation/lookup.sh` uses one explicit call per level instead.

## 9. Status

    a = 0 at N = 16382 and N = 262142.  Kill condition NOT met.  (C) survives, unsupported.
    The seed holds numerically at n = 5, 7, 13, 17.
    n = 19 and n = 31 are outside the database and undetermined.
    The uniform all-H41 analytic theorem is unchanged and unproved.

**The H41 seed remains unproved.**
