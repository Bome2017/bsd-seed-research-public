# READ ME FIRST  —  BLIND VARIANT

## What this is
A two-stage hostile audit of one **fixed curve**: the quadratic twist `E^{-7}` of the project's seed. Stage I is
blind. Stage II compares against prior work you must not read first.

## Read in this order
1. `READ_FIRST/FREEZE.md`        the canonical state. Sections 1-2 are established, 3 is the open frontier,
                                 5 is the fixed-curve data you will need.
2. `READ_FIRST/D7_CERTIFICATE.md` the certified L-value, its validation record and its explicit scope limits.
3. `PRIMARY_SOURCES.md`          what to read at source.
4. `GATE.md`                     binding. Especially K0 (stage order) and K1 (no BSD-to-Sha).
5. `TASK.md`                     the questions.
6. `STAGE_II_ONLY/`              ONLY after Stage I is frozen.

## The one-line question
Can the prime divisors of `#Sha(E^{-7}/Q)` be restricted or eliminated by existing unconditional arithmetic?

## Why it matters, stated without prejudging it
An adjacent argument reduces a wider question to controlling that support. Whether that reduction is the right one
is itself part of Stage II. Stage I does not depend on it: the question "what is the p-support of Sha for this
specific certified rank-zero curve" stands on its own.

## Calibration
This project has twice had to withdraw a verdict for treating "not found" as "does not exist", and once had two
independent agreeing runs share the same error. Agreement is evidence, not proof. Check the sources yourself.
