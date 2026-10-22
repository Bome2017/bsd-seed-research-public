# Two Pro 6 reviews: evidence-based reconciliation

23 September 2026. This is an additive assessment of the two supplied review bundles. Review instructions and proposed patches were treated as material to check, not as authority to rewrite the frozen release or launch computations.

## Verdict

**Both reports contain useful work. Accept three specific corrections. Retain their favorable but qualified assessment of the revised presentation and arguments. Neither report proves full BSD, finds a new arithmetic witness, or independently certifies the entire computational/theorem stack.**

The contextual second pass explicitly withdraws the blanket first-pass omission verdict for the revised manuscript. The fresh pass reaches a compatible conclusion. The four substantial repairs now open to inspection are the symbol-lattice argument, A3's algebraic deductions, the repaired coefficient-verifier predicate and preservation argument, and the restricted C13 custody reconciliation.

This agreement is review evidence, not a vote that replaces proof. Both reports use the same supplied corpus and some of the same replay tools. Their check counts must not be added as if they were disjoint independent theorems.

## Identity and local checks

Reviewed archive: `bsd-seed-research-v0.2.0-private-review.zip`, SHA-256 `c52c77c569bfdc63ad774e58056dd0fa57c831af99e75241d72072c2b9124052`.

Pinned commit: `e8af0b76db3cec7c2610355babc4da25c8396be1`; tree: `f008308751e76c052b248ff9672aa7bb976e4a94`.

The fresh reviewer assessed that ZIP. The second-pass reviewer additionally reports checking the private GitHub tag. Here I reran its inspected snapshot checker: 3,473 files, 3,472 root-manifest entries, and the reconstructed Git tree match the local pinned release. I did not repeat the remote GitHub access. The second-pass bundle's own nine manifest entries also pass.

Both input ZIPs and all their members are bound in `INPUTS.json`. Originals and the reviewed release remain unchanged. No part of a review's account of historical execution has been upgraded merely because its files have matching hashes.

## Findings worth retaining

| Finding | Local adjudication | Effect |
|---|---|---|
| ARS support result bound to the wrong paper | **Confirmed at primary sources and in the current TeX/bibliography.** | Add the 2006 Manin paper under a separate key. Keep the 2012 reference for its distinct modular-exponent theorem. |
| CNS 5.15 called a corollary | **Confirmed at primary source.** It is Theorem 5.15. | Correct the label; no mathematical change. |
| Displayed radius `0.005709` rounded inward | **Confirmed by exact rational decoding of the retained Arb dump.** | Use `0.00570901` and identify the display as outward-rounded. The existing theorem's outer interval remains valid. |
| First-pass missing-argument objections materially addressed | **Supported by the revised appendices and by both reviews' expressly limited reading.** | Stop treating an old absent-appendix objection as current. This is not independent verification of every imported geometric/Selmer input. |
| Old C checker accepts the duplicate-factor counterfeit and repaired checker rejects it | **Freshly reproduced here with the actual macOS C executables on the decisive records.** | Additional bounded execution evidence for the repair; no whole-corpus assurance. |
| Family specialization, invariants, point relation and selected Frobenius calculations | **Inspected and reran the fresh report's small exact-arithmetic program in an isolated folder; all reported outputs agree.** | Useful reproducibility support. Reusing that program is not a third independently written implementation. |
| Higher-precision regulator run | **Useful supplied execution evidence, not rerun here.** | A consistency check using the same evaluator; not a new independent algorithm or a proof of Q36. |
| C13's nine intact inputs versus three changed metadata files | **Both reviews confirm the previously scoped argument.** | Supports the existing qualification. Does not recover the original STATE or establish unchanged entire history. |
| Exact theorem references for residual-image imports could be fuller | **Reasonable secondary documentation request.** | Improve source traceability in a later revision; neither report demonstrates those results false. |

## The three corrections, precisely

**1. Separate the two Agashe–Ribet–Stein sources.** Appendix D.1 currently points `Cor. 3.7` to bibliography key `ars`, which names the modular-degree paper. Its item 3.7 is a remark. The desired odd-prime support statement is Corollary 3.7 of the 2006 Manin paper: for the optimal newform quotient, an odd prime dividing the Manin constant has square dividing the level. The current optimal-quotient setup is the one named by that statement. This source check fixes the binding; it does not reprove the entire lattice appendix. Sources: [Manin support corollary](https://wstein.org/papers/ars-manin/html/node6.html), [modular-degree paper, Theorem 3.6 and Remark 3.7](https://www.math.fsu.edu/~agashe/math/moddeg3.pdf).

**2. Use “Theorem 5.15.”** The primary CNS source labels the integrality statement a theorem. This matches the intended use of the differential associated with a normalized newform. Source: [CNS, Theorem 5.15](https://arxiv.org/html/1911.09446v3).

**3. Round the displayed analytic enclosure outward.** The exact stored radius is

`0.005709008823032490909099578857421875`,

which exceeds `0.005709`. With the printed midpoint `35.93531375275170089`, the replacement radius `0.00570901` covers both the stored radius and the midpoint's rounding error. The extra margin is positive, approximately `1.17697e-9`. The exact certificate remains inside

`[35.929604, 35.941023]`.

This is a real rigorous-numerics display error, not a counterexample to that outer interval or to the analytic-rank implication. The check decodes the retained ball; it does not recompute the original large sum or prove that the stored ball was produced correctly. Exact output and source hash: `checks/exact_rounding_check.json`.

`VERIFIED_THREE_CORRECTIONS.patch` contains the corrections. The supplied patch was applied and checked **only on three isolated source copies** in `candidate_patch/`. The original ARS theorem citation is retained, the new bibliography key is unique, and the theorem's outer interval is unchanged. No PDF rebuild, manifest regeneration, commit, tag replacement, or push was performed. The patch is ready for the builder's next revision, where normal bibliography/PDF and release verification still have to run.

## What the agreement does and does not establish

For A3, both reviewers report no error in the displayed algebra **from the stated arithmetic inputs**. They specifically distinguish exact specialization lengths and individual conjugation-eigenspace dimensions from weaker characteristic-ideal or total-dimension statements. They did not freshly build Lean or independently reconstruct all of the arithmetic comparison. It would be an overstatement to turn “no gap found in this scoped review” into unconditional independent certification of A3's arithmetic realization.

For the lattice, the displayed inequality gives the integer eight from the listed geometric premises. The shared remaining review target is whether the regularity, component, genus/incidence and differential-descent inputs apply to the precise model. These are visible imported premises. Neither report supplies a counterexample or justifies dropping the retained lattice theorem solely because its entire source stack was not reproved.

The native C run here used the release's inspected `coefficient_verifier_regression.py --compile` and the unmodified old/repaired C source. It reproduced four expected outcomes: counterfeit accepted by the old checker, rejected by the repaired one; genuine record accepted by both. The Pro bundles additionally report Linux/shim/sanitizer and malformed-input cases. Those supplied executions are not relabeled as executions performed here. The billion-record corpus remains outside this bounded check.

Both reviews therefore sharpen the external-review request to two specific mathematical applications: the integral modular-curve model and the equivariant Selmer comparison. They do not discover a route to FIN, ORDER9 or Q36. Their suggestion of a full repaired-engine/corpus replay would strengthen computational assurance; it is not necessary to implement these three corrections and is not launched or authorized by this assessment.

## Handoff

Carry the three verified corrections into the next patch release while preserving v0.2.0. Keep the earlier coverage supplement alongside it: these Pro bundles reviewed the fixed snapshot, not that newly assembled historical supplement. Avoid presenting their agreement as review of files they did not receive.

The practical gain is a cleaner, better-supported dossier and a narrower expert-review question. The mathematical endpoints and computational trust boundaries are unchanged.
