# ORDINARY ANTICYCLOTOMIC BRIDGE — hostile source audit. Ordinary primes only.

You are an independent hostile mathematical referee.

Audit **only** the good-ordinary definite anticyclotomic bridge described here. Do not redesign the wider BSD
project, do not treat supersingular primes, and do not reopen certified numerical work unless a logical dependency
forces it. Read `INPUTS.md` before starting and `GATE.md` before proposing anything.

**Objective.** Determine whether the remaining ordinary-prime implication is actually *proved* by existing theorems,
or isolate the exact first missing theorem.

---

## The central conditional

Test the consequences of

    [c_2] != 0.

**Do not claim `[c_2] != 0` has been proved.** It is the branch's separate analytic nonvanishing target and is out of
scope here. The question is:

> If `[c_2] != 0` is eventually proved, do the existing BLV and Bertolini–Darmon results already convert it —
> together with the certified `D = -7` input — into `Sha(E/K)[p^inf] = 0` for every good-ordinary `p` satisfying the
> required hypotheses?

## TASK 1 — source-check the BLV side

Read Bertolini–Longo–Venerucci (arXiv:2306.17784, Math. Ann. 395 (2026)) **at source**. Identify exactly:

1. the Selmer module whose Pontryagin dual has characteristic ideal `Char_p(f)`;
2. **all** local conditions defining it;
3. the exact ordinary case of Theorem A;
4. whether the ordinary case is always non-exceptional;
5. whether Theorem A gives **equality of principal ideals** `(L_p) = (Char_p)` under our hypotheses.

**Do not replace equality by a divisibility.** Then determine whether, if `[c_2] != 0`, BLV gives
`ord_I Char_p = 4` with a unit normalized `I^4/I^5` characteristic coefficient. Track every normalization.

## TASK 2 — module identification  (the main unresolved A1 residue)

Read Bertolini–Darmon, *Derived p-adic heights*, at source, especially the definitions surrounding the pro-`p` Selmer
module `S = S_p(E/K)` and the Iwasawa module `X_inf` whose characteristic ideal enters the derived-height formulas.

Determine whether BLV's characteristic module **is** that module, or differs only by a completely controlled
modification preserving `ord_I`, the normalized leading coefficient, and the relevant control/specialization
statement. Compare explicitly:

* global Selmer condition;
* conditions at primes dividing `p`;
* conditions at primes dividing `N`;
* ordinary/Greenberg vs strict/relaxed choices;
* Pontryagin dual conventions;
* finite or pseudo-null correction terms;
* imprimitive Euler factors;
* twist and involution conventions.

**Do not write "these are standardly equivalent"** without an actual theorem or an explicit comparison you carry out.
Return `MODULE_IDENTIFICATION_PROVED`, or the first precise mismatch.

## TASK 3 — verify the derived-height order inequality

Read at source the relevant parts of Bertolini–Darmon, especially **Theorem 2.7, Theorem 2.18, Theorem 2.23,
Remark 2.21**, and whatever definitions and lemmas those actually require. **Do not rely on this packet's summaries
of them** — `INPUTS.md` §7 records that they have *not* been source-read here.

With `S = S_p(E/K)` and `s^± = rank_{Z_p} S^±`, verify or refute, from the actual derived-height filtration,

    sigma >= rank_{Z_p} S + rank_{Z_p} S^(2) >= 2 max(s^+, s^-).

In particular verify:

1. the first anticyclotomic height pairs only **opposite** `tau`-eigenspaces;
2. hence `rank S^(2) >= |s^+ - s^-|`;
3. the characteristic-order formula really counts the filtration ranks in the required way;
4. no omitted higher filtration term can invalidate the inequality;
5. any truncation at level `p` causes no problem when `p >= 5` and `sigma = 4 < p`.

If the chain is not exactly what the source proves, state the strongest correct replacement.

## TASK 4 — use the `tau`-eigenspaces correctly

For odd `p`, `e^± = (1 ± tau)/2` are integral idempotents. Verify at source, or by a complete algebraic argument, the
quadratic-twist identifications needed to pass between the `K`-Selmer eigenspaces and the two rational curves
`E/Q` and `E^{-7}/Q`. Establish or refute the corresponding identification **for the inverse-limit / pro-`p` Selmer
group and for `T_p Sha`**.

The certificate supplies `rank E^{-7}(Q) = 0` and `Sha(E^{-7}/Q)[p^inf]` finite. Determine rigorously whether this
implies `s^- = 0`.

**Do not merely cite the familiar decomposition of `E(K)`.** The required statement is about the Selmer / `T_p Sha`
objects, not the Mordell–Weil group.

## TASK 5 — replay the live-configuration enumeration

Write `d^± = corank_{Z_p} Div Sha(E/K)[p^inf]^±`. Before using the `D = -7` certificate,
`s^+ = 2 + d^+` and `s^- = r^- + d^-`. If `sigma = 4` and `sigma >= 2 max(s^+, s^-)`, these configurations all survive:

| `d^+` | `r^-` | `d^-` | `s^+` | `s^-` | `2 max` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 2 | 0 | 4 |
| 0 | 0 | 1 | 2 | 1 | 4 |
| 0 | 0 | 2 | 2 | 2 | 4 |
| 0 | 1 | 0 | 2 | 1 | 4 |
| 0 | 1 | 1 | 2 | 2 | 4 |
| 0 | 2 | 0 | 2 | 2 | 4 |

The distinction that matters:

* `d^+ = 0` **should** follow from the order inequality, because the known rank-two `E(Q)` already fills `s^+ = 2`;
* `d^-` does **not** follow from that inequality alone.

The `D = -7` certificate is what is supposed to supply the minus-side input. **Replay this logic independently.**
A verdict of `ORD4_FORCES_SHA_FINITE` reached from `sigma = 4` alone, without invoking the certified twist
information, is **invalid**.

## TASK 6 — A2a: does certificate + order 4 kill the divisible part?

Assuming (1) `[c_2] != 0`; (2) module identification succeeds; (3) hence `sigma = 4`; (4) the Task-3 inequality holds;
(5) the certificate implies `s^- = 0` — **prove or refute `d^+ = d^- = 0`**, equivalently
`Div Sha(E/K)[p^inf] = 0`.

This is the key point. See `GATE.md` for the forbidden assumptions; `Sha(E/K)[p^inf]` finite is a **target
consequence here, not an allowable hypothesis**. If the conclusion holds, identify exactly which theorem(s) make it
hold.

## TASK 7 — A2b: leading coefficient to `Sha[p^inf] = 0`

**Only if Task 6 succeeds.** Read BD Theorem 2.23 and Remark 2.21 at source and determine the **exact** leading-
coefficient statement. This project currently expects something schematically like

    leading coeff  =  u * #( Sha(E/K)[p^inf] / Div Sha(E/K)[p^inf] ) * R_der,     u in Z_p^x

**Do not assume that schematic is accurate.** Replace it with the exact source statement. Then check:

1. what lattice or determinant contains `R_der`;
2. when `R_der` is integral;
3. whether vanishing of the divisible part makes `Sha[p^inf]` finite;
4. whether both factors then have non-negative `p`-adic valuation;
5. whether a unit normalized characteristic leading coefficient forces `v_p(#Sha(E/K)[p^inf]) = 0`;
6. hence whether `Sha(E/K)[p^inf] = 0`.

**Do not silently cancel a regulator whose integrality or valuation has not been justified.**

---

## Deliverable

A theorem-by-theorem source audit, then **exactly one** principal verdict from `GATE.md`, then the compact ledger.
For every failure verdict, state the **first** missing implication, not downstream consequences.
