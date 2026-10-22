# RETURN — ARISTOTLE_GATE_R_FINITENESS_V1

**Result: the single authorised target is proved.  Zero `sorry`, zero `admit`, no new axiom.**

    GateRFinite.h41_finite   (RequestProject/GateRFinite/Finiteness.lean)
    axioms: [propext, Classical.choice, Quot.sound]

Only `RequestProject/GateRFinite/Finiteness.lean` was edited.  All 36 other `.lean` sources are
byte-identical to the shipped packet (checked against `MANIFEST.sha256`, below).

---

## 1. Custody

Input archive, as received:

    3d1db03e1f8e7fa2c45a545b730db0ff7da1d32adf7540c43f730047cb76e573  ARISTOTLE_GATE_R_FINITENESS_V1.tar.gz

`sha256sum -c MANIFEST.sha256` inside the unpacked archive: **all 47 listed members OK** before any work
began.

Frozen-bytes check after the work (all `RequestProject/**` manifest entries except the job file):

    36 of 36 frozen Lean sources: OK
    changed: RequestProject/GateRFinite/Finiteness.lean only
      shipped : 68761a0854c19386f4bc5001a451853e2c6552186b68497df74c6986b53f8422
      returned: e3e9368290b2596ba57640cb905a591e7b641ecf4f4488b63eff4eadbc655b89

`lakefile.toml`, `lake-manifest.json`, `lean-toolchain` are unmodified (Lean
`leanprover/lean4:v4.28.0`, mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`).

Which tree is which: there is exactly one working tree, the project root.  The input archive is
also preserved at the root as `ARISTOTLE_GATE_R_FINITENESS_V1.tar.gz`; **that archive still
contains the original `sorry` in its copy of the job file** — it is the preserved input, not the
return.  The return is the unpacked tree.

Files added by this return and therefore *not* in the manifest (expected, per `CUSTODY.md`):

    RETURN_REPORT.md
    verify/Verify.lean            type + axiom + dependency harness (not in the library glob)
    verify/verify_output.txt      its captured output
    verify/scan_constructs.py     construct scanner with injected positive control
    verify/scan_output.txt        its captured output
    README.md TASK.md CUSTODY.md DIGESTS.md FORMALIZATION_BOUNDARY.md
    MANIFEST.sha256 CERTIFIED_STATEMENTS_ELABORATED.txt gen_statements.lean
                                  (the packet's own documents, unpacked alongside the sources,
                                   byte-identical to the archive)

The manifest was **not** rewritten.

The stale frozen comment in `GateR/Assembly.lean` mentioning `sorry` was left untouched, as
instructed.  The job file's own opening comment (`"Replace the single sorry below."`) is likewise
preserved verbatim; it is now stale in the same way, and its `sorry` is comment text, not a term.

## 2. Build

    lake build
      Build completed successfully (8063 jobs).

    lake build RequestProject.GateR.Assembly RequestProject.GateRFinite.Finiteness
      Build completed successfully (8062 jobs).

The only warning in the whole build is a pre-existing `unused variable hH` linter note from the
frozen `RequestProject/R1/Height.lean:112`.  Elaborating the new module produces no `sorry`
warning and no `declaration uses sorry` message.

## 3. The elaborated target type

With `pp.explicit`, `pp.universes`, `pp.fullNames`:

```
GateRFinite.h41_finite : ∀ (ε : Int) (m q : Nat) [inst : Fact (Nat.Prime q)],
  @SDyadic.Params ε m q inst →
    SDyadic.H41 ε m →
      Finite.{1}
        (@WeierstrassCurve.Affine.Point.{0} Rat Rat.commRing
          (@WeierstrassCurve.toAffine.{0} Rat (P01.Ecurve ε m q)))
```

This is the shipped signature, unchanged: same name, same binders, same hypotheses, and the
conclusion is mathlib's `Finite` applied to the affine point group of the actual curve
`P01.Ecurve ε m q` over `ℚ`.

## 4. Axiom footprint

```
'GateRFinite.h41_finite' depends on axioms: [propext, Classical.choice, Quot.sound]
```

A subset of the accepted set.  No `sorryAx`, no `Lean.ofReduceBool`, no `Lean.trustCompiler`, no
declared axiom of this project.

## 5. Proof route

Everything arithmetic comes from theorems already in the tree; nothing frozen is reproved and no
new arithmetic input is introduced.

Write `T = P01.Tpt hP`, `H = R1.height`, and `M P = GateR.translateMax T H P = max (H P) (H (P+T))`
(the frozen `GateR.translateMax`, applied to the frozen `R1.height`).

1. **Strict descent step** (private `strict_halving`).  From the certified
   `R1.h41_multiplicative_duplication_height` — `∃ C ≥ 1, ∀ P, H P ^ 4 ≤ C * H (P + P)` — and the
   certified `GateR.halving_representatives` — every `P` is `Q + Q + e • T` with `e ≤ 1` — one gets
   `M Q ^ 4 ≤ C * M P`.  The two doubles `Q+Q` and `(Q+T)+(Q+T)` coincide because `T + T = 0`
   (`P01.Ecurve_two_torsion`), and that common double is `P` or `P + T`, so its height is `≤ M P`.
2. **Infinite descent** (private `mem_closure_of_strict_halving`).  Strong induction on `M P`: if
   `M P ≤ C` then `P` is in the generating set; otherwise take the halving `P = Q + Q + e•T`.
   Either `M Q ≤ C`, or `C < M Q`, in which case `M Q ^ 4 ≤ C * M P` with `1 ≤ M Q`
   (`R1.one_le_height`) forces `M Q < M P` and the induction hypothesis applies.  Hence every
   rational point lies in `AddSubgroup.closure ({R | M R ≤ C} ∪ {T})`.
3. **The generating set is finite** (private `finite_tmax_le`).  `{R | M R ≤ C} ⊆ {R | H R ≤ C}`,
   which is finite by the certified `GateR.height_sublevels`; adding the single point `T` keeps it
   finite.  So that closure is all of the group and `AddGroup.FG` holds — *derived here, never
   assumed*.
4. **Torsion.**  The certified `GateR.every_point_torsion` gives `AddMonoid.IsTorsion` of the point
   group.
5. **Conclusion.**  `AddCommGroup.finite_of_fg_torsion` yields `Finite` of the point group.

No Mordell–Weil theorem, no canonical or logarithmic height, no new height theorem, no uniform
exponent, no `Nat.card`, no 2-primary statement, no `Sel₂`/Ш/BSD input, and no assumed finiteness,
torsion, rank or finite-generation hypothesis: the signature carries exactly `Params`, `H41` and
the prime instance.  `Tpt_not_mem_twoE` and the other `private` lemmas of `GateR/Assembly.lean`
were not exported, restated or used; only the five public Gate-R outputs are cited.

## 6. Certified declarations the proof term depends on

Directly cited in the new source:

    R1.h41_multiplicative_duplication_height      duplication height inequality
    GateR.halving_representatives                 P = 2Q + eT, e ≤ 1
    GateR.height_sublevels                        height sublevel sets are finite
    GateR.every_point_torsion                     every rational point is torsion
    GateR.translateMax, R1.height, R1.one_le_height
    P01.Ecurve, P01.Tpt, P01.Ecurve_two_torsion
    SDyadic.Params, SDyadic.H41

Mathlib results used for the final step: `AddGroup.fg_iff`,
`AddCommGroup.finite_of_fg_torsion`, `isOfFinAddOrder_iff_nsmul_eq_zero`, plus `AddSubgroup`
closure lemmas and `Nat.strong_induction_on`.

The full transitive closure of this project's declarations inside the proof term — 331 names,
including `R0.properHeightTwoDescentTorsion`, `GateR.bounded_halving`, the `P03*`/`P04*` descent
chain and the `SDyadic` base reached through the cited theorems — is listed verbatim in
`verify/verify_output.txt`, together with the immediate constants of the proof term.

Reproduce with:

    lake env lean verify/Verify.lean

## 7. Construct scan, with injected positive control

`verify/scan_constructs.py` scans every `.lean` file of the tree for `sorry`, `admit`, `axiom`,
`native_decide`, `ofReduceBool`, `trustCompiler`, `implemented_by`, `unsafe`, `extern`, both raw
and after stripping Lean comments.  It **injects a positive control** — a file that genuinely
declares `axiom controlFalse : False` and genuinely contains all the other constructs — and
aborts with FAIL unless the scan finds every one of them.  The control is written to a temporary
directory outside the tree and deleted afterwards, so that no prohibited construct is delivered;
rerunning the script regenerates it.

Captured output (`verify/scan_output.txt`):

    RequestProject/GateR/Assembly.lean
        raw (comments included): {'sorry': 1}
        code (comments stripped): {}
    RequestProject/GateRFinite/Finiteness.lean
        raw (comments included): {'sorry': 1}
        code (comments stripped): {}
    RequestProject/P01/Instances.lean
        raw (comments included): {'native_decide': 1}
        code (comments stripped): {}
    POSITIVE_CONTROL.lean
        raw:  {'sorry': 1, 'admit': 1, 'axiom': 1, 'native_decide': 1, 'ofReduceBool': 1,
               'trustCompiler': 1, 'implemented_by': 1, 'unsafe': 1, 'extern': 1}
        code: {'sorry': 1, 'admit': 1, 'axiom': 1, 'native_decide': 1, 'ofReduceBool': 1,
               'trustCompiler': 1, 'implemented_by': 1, 'unsafe': 1, 'extern': 1}

    PASS: the scanner detects a genuine axiom/sorry/admit/native_decide/unsafe/
          implemented_by/extern file.
    no forbidden construct in code position in any project .lean file

The three raw hits are documentation prose: the two stale `sorry` mentions in frozen and job-file
doc comments (one each, since `grep` counts per file), and the sentence in `P01/Instances.lean`
explaining that `decide` there is *not* `native_decide`.  All three vanish with comments stripped.
The `#print axioms` footprint in §4 is the independent, non-textual confirmation.

## 8. Boundary of what was established

Exactly the displayed statement, for the `H41` family under the existing `Params`: the group of
rational points is finite.  Nothing is claimed about its order, exponent, isomorphism type,
2-primary subgroup, or whether the marked point `T` is a double.  No novelty or priority claim is
made; `PRIOR_ART_BLOCKER` remains `UNRESOLVED` and no literature comparison was performed.

## 9. STOP

The mandated stop point has been reached.  The 2-primary corollary was not attempted, Gate C and
Gate A were not begun, the family was not widened, and no frozen theorem was modified or reproved.
