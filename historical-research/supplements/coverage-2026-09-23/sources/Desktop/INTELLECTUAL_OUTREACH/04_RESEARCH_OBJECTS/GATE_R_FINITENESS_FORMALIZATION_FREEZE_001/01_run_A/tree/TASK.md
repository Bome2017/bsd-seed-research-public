# ONE TARGET.  `Finite` OF THE ACTUAL RATIONAL POINT GROUP.

Replace the single `sorry` in `RequestProject/GateRFinite/Finiteness.lean`.  That is the whole job.

```lean
theorem GateRFinite.h41_finite (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    Finite ((P01.Ecurve ε m q).toAffine.Point)
```

The signature is fixed.  Do not add a hypothesis, weaken the conclusion, rename, or restate it for
a different group.  `Finite` must be mathlib's finiteness of the actual point group — not
finiteness of a height sublevel set, not a hand-built `Fintype`, not a subgroup or quotient.

Private lemmas and local `have`s inside the module are unrestricted.  `h41_finite` is the only
authorised public output.

## Everything else is frozen, and already proved

Every other `.lean` file in this project is a certified source, **including
`RequestProject/GateR/Assembly.lean`**.  Do not edit, reformat or re-indent any of them.  **Do not
reprove anything they contain.**  The inputs this target needs are already theorems in this tree;
find them and cite them.

`CERTIFIED_STATEMENTS_ELABORATED.txt` lists all 327 source-declared theorems of this project with
their full elaborated types, produced by the elaborator in `gen_statements.lean`, which ships
alongside its output so you can rerun it.  It is an inventory, not a plan.

## No route is supplied

This packet contains the certified base, the exact target, and the boundary.  It deliberately
contains **no proof sketch, no lemma ordering, no API pointer, no constant, and no reviewer's
report.**  Find your own proof.

## What may not be used

**Constructs.**  `sorry`, `admit`, any new `axiom`, `native_decide`, `ofReduceBool`,
`implemented_by`, `unsafe`, `extern`, `trustCompiler`.  The accepted axiom footprint of the output
is a subset of `{propext, Classical.choice, Quot.sound}`.

**Premises that would make the result conditional.**  Mordell–Weil finite generation,
`Module.Finite ℤ`, `Module.Free ℤ`, `AddGroup.FG`, or any assumed finiteness, torsion, rank or
height hypothesis on the point group.  The signature carries exactly `Params`, `H41` and the prime
instance, and nothing may be added.

**Out of scope entirely.**  Canonical or logarithmic heights.  Cohomological `Sel₂`, `H¹`, Ш.  Any
L-function, analytic rank, or BSD statement.  Widening `m ≥ 3`, changing `ε`, or relaxing `Params`
or `H41`.  Redefining `R1.height`, `R1.heightQ`, `GateR.translateMax` or any frozen declaration.

**Specifically excluded, even though adjacent and tempting.**  Do not state or prove anything about
`Nat.card` of the group, its exponent, its isomorphism type, its 2-primary subgroup, or whether the
marked point `T` is a double.  Do not export or restate any `private` lemma of
`GateR/Assembly.lean`.  Those are a separate bounded target and are not authorised here.

## Execution

    lake build

builds everything, including the new module: the library globs `RequestProject.+`.  Also report

    lake build RequestProject.GateR.Assembly RequestProject.GateRFinite.Finiteness

and, for the output,

    #check @GateRFinite.h41_finite
    #print axioms GateRFinite.h41_finite

with `pp.explicit`, `pp.universes` and `pp.fullNames` enabled, plus an explicit list of which
certified declarations of this project the proof term depends on.

Do not modify `lakefile.toml`, `lake-manifest.json` or `lean-toolchain`.  Pin: Lean
`leanprover/lean4:v4.28.0`, mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.

**If your return includes a textual construct scan of your own, it must carry an injected positive
control** — a file that genuinely declares an `axiom` — and show that the scan finds it.  A scan
reporting zero hits without such a control will not be accepted as evidence.  A scanner in this
programme has already reported zero axioms for a file declaring `axiom False`.

## If you cannot close it

Report the exact residual goal and stop.  Do not substitute a weaker statement under the same name,
do not add a hypothesis, and do not report a partial result as success.

## MANDATORY STOP

When this module is complete — or blocked with a stated obstruction, or out of budget — **STOP.**
Do not prove the 2-primary corollary.  Do not begin Gate C (`Sel₂`/Ш) or Gate A (analytic BSD)
work.  Do not widen the family.  Do not make any novelty or priority claim: `PRIOR_ART_BLOCKER` is
`UNRESOLVED` and no literature comparison is authorised.
