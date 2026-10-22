# GATE — read before proposing anything

## K0. Scope. This audit is ORDINARY ONLY.

Out of scope, and a run that spends effort on any of these has failed the gate:

* **supersingular primes** and BLV's signed modules — that is interface A3, a separate open problem;
* the **anomalous-prime problem** (`a_p = ±1`) — interface B;
* **proving `[c_2] != 0`** — it is the conditional input, not the target;
* **redoing the numerical `D = -7` certificate**;
* any claim of full BSD, `FIN`, or `FORMULA`;
* redesigning the wider project, or reopening A0 (unless you find a genuine incompatibility with source conventions
  you actually need — in which case say so explicitly and stop).

## K1. Forbidden assumptions

Assuming any of these makes the whole run void, because each is either the target or a known-missing theorem:

* **`Sha(E/K)[p^inf]` is finite.** This is the *target consequence* of Task 6, not a hypothesis. It is also weaker
  than `FIN`, so "I did not assume FIN" is **not** a defence — the prohibition is on the finiteness itself.
* `T_p Sha = 0`.
* **Nondegeneracy of any ordinary or derived height.** With `r^- = 0` the first anticyclotomic height is
  *identically zero* on `E(K)`, so any argument that quietly assumes a nondegenerate regulator is wrong here.
* Vanishing of a divisible subgroup by fiat.
* BSD, or `FIN`.
* Any **rank-two Heegner-index analogue** that is not an actually proved theorem. In rank one, finite support comes
  from the finite Heegner index `[E(K) : Z y_K]`; for this curve `ord L(E/K,s) = 3` over the *indefinite* field
  `Q(sqrt -23)`, so that index is **infinite** and has no rank-two analogue in the record. Do not invent one.

## K2. Failure-to-find is not a theorem

If you cannot locate a result, say so and return the missing statement. Do **not** convert "no such theorem was
found" into "no such theorem exists". Absence of a comparison is not impossibility. This rule has been broken twice
in this project's history and both times the verdict had to be withdrawn.

## K3. Do not assert standard equivalences

"These are standardly equivalent", "the usual comparison", "up to harmless factors" are not admissible steps for the
module identification (Task 2) or the eigenspace bridge (Task 4). Either cite a theorem that states the comparison,
or carry out the comparison explicitly and show the work. Local conditions, duals and imprimitive factors are exactly
where this chain can silently break.

## K4. Conditional results must stay labelled conditional

Every statement in the return must be marked as one of:

* **proved theorem** (with citation);
* **standard algebraic identification that you independently proved** (with the proof);
* **conditional consequence of `[c_2] != 0`**;
* **conjecture**;
* **unsupported inference**.

Do not promote any conditional statement to a certified project result. Everything downstream of `[c_2] != 0` is
conditional, without exception.

## K5. Parity check on the order

`ord_I L_p = 2 ord_I calL_p` is **always even**. If any line of your argument yields an odd order for `L_p`, that
line is wrong — stop and report it rather than rounding it away.

## K6. The `sigma = 4` shortcut is invalid on its own

A verdict of finiteness reached from `sigma = 4` alone, without invoking the certified twist information, is
**invalid** — `INPUTS.md` §8 lists the configurations that survive the order inequality by itself. Task 5 exists
precisely to catch this.

---

## Verdicts — return exactly ONE principal verdict

`ORDINARY_BRIDGE_PROVED`
> Only if, conditional on `[c_2] != 0`, the existing sourced results plus the certified `D = -7` input rigorously
> imply `Sha(E/K)[p^inf] = 0` for the good-ordinary primes under consideration.

`MODULE_IDENTIFICATION_FAILS`
> BLV's characteristic module is not the module the BD derived-height machinery needs, and no proved comparison
> repairs it.

`DERIVED_ORDER_INEQUALITY_FAILS`
> `sigma >= 2 max(s^+, s^-)` does not follow from the cited BD results.

`TWIST_EIGENSPACE_BRIDGE_FAILS`
> The certified rank-zero / finite-`Sha` result for `E^{-7}/Q` does not rigorously imply the required minus-eigenspace
> statement over `K`.

`LEADING_TERM_STEP_FAILS`
> Task 6 succeeds but Thm 2.23 / Rmk 2.21 do not turn the unit characteristic leading coefficient into
> `Sha(E/K)[p^inf] = 0`.

`FIRST_MISSING_THEOREM: <precise statement>`
> The chain fails elsewhere.

**A negative verdict returned early, with the first missing implication stated precisely, is a good outcome** and is
strongly preferred to a long conditional narrative. For every failure verdict state the **first** missing
implication, not downstream consequences.

## Closing ledger — required

    MODULE_IDENTIFICATION   = ?
    BD_ORDER_INEQUALITY     = ?
    TWIST_MINUS_EIGENSPACE  = ?
    A2a_DIVISIBLE_SHA       = ?
    A2b_LEADING_TERM        = ?
    ORDINARY_BRIDGE         = ?
