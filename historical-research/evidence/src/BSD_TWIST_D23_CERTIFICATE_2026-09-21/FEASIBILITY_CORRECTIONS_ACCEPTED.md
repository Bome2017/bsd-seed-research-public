# Corrections to FEASIBILITY_REPORT — accepted, verified at the engine source

Date 2026-09-21. **Additive.** Supersedes the Summary table, §1's verdict, §4 and §5 of `FEASIBILITY_REPORT.md`; that
file is preserved unedited. Authority:
`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/D23_FEASIBILITY_REVIEW.md`.
I checked each correction against `~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/arbcore.c` rather than accepting it.

## E1. "Both feasibility questions answered" is withdrawn, and so is "not adequate"

What I proved: `B_D(3.45e9) = 0.343` (recomputed, and `B_D(1e9) = 5548.43`, matching the review's figure exactly).
What I then asserted: that `3.45e9` is **not adequate** and that `7e9` is the **recommendation**.

Neither follows. The certificate is `|truncated interval| > B(T)`, and **I never computed the interval**. If the
truncated sum lands far enough from zero, `0.343` is sufficient; if it lands close, even `7e9` may not be. Adequacy is
**undetermined in both directions** until the interval exists. `7e9` is a *candidate* cutoff, not a recommendation, and
the honest statement is that the cutoff must be chosen **from the actual interval and tail**, not in advance.

This is the fourth time in this thread that my underlying numbers were right and my verdict sentence outran them. The
pattern is mine.

## E2. The numerical machinery is substantially further along than I said — verified

My §4 claimed the `E_1`-in-balls kernel "does not exist yet". **False.** From `arbcore.c`:

* **Arb balls are already the accumulation type**, not a planned upgrade: 147 `arb_`/`acb_` call sites; line 18 states
  *"No M_PI, no double in any enclosure: pi, gamma, sqrt, exp, log, **E1**, cos/sin(pi*rational), AGM all from Arb."*
* **`E_1` and its Taylor coefficients already exist**, inside the second-derivative (G2) evaluator: line 85
  `arb_hypgeom_expint(e1+0, one, x, prec); /* E1(x) */`, then line 86 builds the derivative coefficients from
  `E1' = -e^{-t}/t`. Line 77: *"Taylor coefficients G2^(i)(x)/i!, i = 0..JDEG+1, at exact node x, by exact series
  algebra."*
* **Rigorous remainder control is in place**: line 112 rejects a Taylor step outside `[-H, 2H]` because *"remainder
  bound needs this"*.
* **A validation harness already exists in the pattern the review asks for**: mode `g2t` (line 305) is a unit test of
  *"node Taylor models vs direct series"*.

Note the direction of the surprise: our twist needs the **first**-derivative weight `E_1(cn)` of formula (1), and `E_1`
is already computed as `e1+0` *inside* the construction of the heavier G2 weight. The missing piece is a twist **mode**
wired to existing parts, not the apparatus itself.

Existing modes (line 327): `l2`, `ms`, `msl`, plus `tmin` and `g2t`. A twist mode joins that dispatch.

## E3. The six-minute figure is not a twist benchmark, and I ignored memory entirely

It extrapolates stage A's *modular* workload to a *ball* workload with a different weight. It is an anchor, not a
measurement, and I labelled it as if it settled the cost.

Worse, I never considered allocation. `arbcore.c` line 159 has the dense path `A = calloc(top + 1, 4)`:

| `T` | dense `A` at 4 B/entry |
|---|---|
| 3.45e9 | 12.9 GiB |
| **7e9** | **26.1 GiB** |

on a **16 GiB** host — matching the review's ~28 GB. **Directly adapting the dense derivative mode is impossible at
either candidate cutoff.** The C11 path avoids this: line 240 allocates per-block (`rem`, `an` at `BLK*8`), not per-`T`.
Any twist mode must be built on that table-free traversal.

## E4. The 1e9 floating scout cannot certify scale

`B_D(1e9) = 5548.43` (confirmed). So that pass is **heuristic only** — it can indicate the magnitude of `L'` to guide a
cutoff choice, and it can prove nothing about it. My §5 suggested it as the first step without stating that its
rigorous tail is four orders larger than any plausible value of the derivative. It remains useful as a scout **if
labelled as one**; it is not a step toward the certificate.

## E5. Corrected status

| item | status |
|---|---|
| `B_D(T)` values | stand (`3.45e9 -> 0.343`, `7e9 -> 1.08e-6`, `1e9 -> 5548.43`) |
| adequacy of any cutoff | **undetermined** — requires the computed interval |
| `7e9` | a **candidate**, not a recommendation |
| corpus format (int32/prime, cross-checked `a_5..a_37`, `a_2243`) | stands |
| stage W already paid | stands |
| `E_1` / Arb / Taylor / remainder / unit-test machinery | **already exists**; my "does not exist" withdrawn |
| ~6 minutes | an anchor from a different workload, **not** a twist benchmark |
| memory | dense path needs 26.1 GiB at `7e9` on a 16 GiB host — **must use the table-free traversal** |
| 1e9 scout | heuristic only, tail 5548 |

**Next step, as the review sets it:** implement and benchmark an isolated twist mode on the existing table-free
traversal and `E_1` machinery; validate representative blocks against direct Arb evaluation in the `g2t` pattern; then
choose the cutoff from the actual interval and tail. Engineering, here, no new package. **Not launched.**

Nothing certified. `L'(E^{-23},1)` remains of unknown size and sign. FIN, ORDER9, Q36 open.
