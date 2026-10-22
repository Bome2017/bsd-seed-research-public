# ARISTOTLE_TAIL_COMPRESSION (2026-09-22) — read me first

**One question, with a hard kill gate.** Not "invent a FIN mechanism". You are handed one working quadratic lane, one
exactly isolated unresolved ideal, a fixed-integral-object target, and a covering obstruction already settled.

Read in order: `TASK.md`, `INPUTS.md`, `GATE.md`, then `record/FRONTIER.md`.

**Q1 is primary and independent of everything else:** can `I_3` be obtained by reduction mod `p` of a fixed
`p`-independent arithmetic object? If not, return `NO_SURVIVOR` immediately — do not proceed to coverage.

Three things are already settled and must not be re-derived or reported as findings:
1. the three-imaginary-field cover is **impossible** (every Klein-four cover contains a real quadratic subfield);
2. the Heegner Λ-index does **not** determine `I_3` (explicit counterexample, `INPUTS.md` §4);
3. any **fixed finite** set of imaginary lanes leaves primes of density `2^{-r} > 0` uncovered.

**Negative verdicts must be scoped.** A proved impossibility inside a class you delimit is a result; a construction
you could not complete is not. Never write "no such object exists" when you mean "I did not find one".

**What this package is not.** It is not a request for a new representation, group, or kernel. It is not authorization
for any computation. It contains no novelty claim, and nothing here says BSD for this curve is close — it is not.
`RANK` is closed; FIN and the real leading-term comparison are open.
