# STATUS — GATE_R_FINITENESS_FORMALIZATION_FREEZE_001

## Disposition

    RESULT        LEAN_CERTIFIED
    CERTIFICATION two independent Aristotle proof searches, both externally rebuilt
    AXIOMS        [propext, Classical.choice, Quot.sound], both runs
    REPLICATION   confirmation-grade with substantive route divergence;
                  ZERO shared private helper names — the cleanest separation yet measured

```lean
theorem GateRFinite.h41_finite
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    Finite ((P01.Ecurve ε m q).toAffine.Point)
```

    E_q(Q) is FINITE, for the H41 family.

mathlib's `Finite` on `WeierstrassCurve.Affine.Point` of `P01.Ecurve ε m q` over `ℚ` — read off the
elaborated term, not the source. Not a sublevel set, not a hand-built `Fintype`, not another group.
Hypotheses are exactly `Params`, `H41` and the prime instance; nothing was added.

This is strictly stronger than the previously certified `rank ℤ E_q(ℚ) = 0`, and both runs bypass the
rank theorem entirely — it is `NOT USED` in either dependency footprint, which is correct, since
finiteness does not factor through it.

## Verified externally, never from the runs' receipts

| Check | Run A | Run B |
|---|---|---|
| Input received | packet `3d1db03e…`, exact | exact |
| Nested-skeleton trap | none — no extracted input copy | none |
| Inherited bytes, enumerated from the shipped manifest | 47 checked, **1 altered** | 47 checked, **1 altered** |
| The one altered file | `README.md`, platform banner, byte-identical in both | same |
| Frozen `.lean` sources altered | **0 of 36** | **0 of 36** |
| Fresh `lake build`, independent package base | 8063 jobs, exit 0 | 8063 jobs, exit 0 |
| Proposition identical to shipped, by typechecking | **yes** | **yes** |
| Axioms, regenerated | standard | standard |
| Construct scan, corrected and self-tested | all 0 | all 0 |
| Dependency footprint | 366 | 366 |

## `AddGroup.FG` — adjudicated, no violation

Both returns contain `AddGroup.FG`, which `TASK.md` listed among things not to use. **It is derived,
not assumed**: one `haveI … := AddGroup.fg_iff.mpr …` per return, built from a finite generating set
the run constructed itself. A binder-position test found zero occurrences in hypothesis position, and
the type-identity check confirms the signature is unchanged. Both conclude via
`AddCommGroup.finite_of_fg_torsion` with torsion from the frozen `GateR.every_point_torsion`.

Two defects of mine surfaced here and are recorded in `receipts/AddGroup_FG_ADJUDICATION.txt`: my
prohibition was ambiguously worded, and my corrected scanner had dropped the premise-prohibition
names, so it could not have caught a genuine violation. Third appearance of the same defect family —
first time found by me rather than by an external reviewer.

## Replication, measured

8 declarations each; **1 shared name, and it is the one I mandated.** Zero shared private helpers —
seven unique helpers each. Similarity 0.231; of 27 identical lines, 7 are my shipped text and 4 are
boilerplate, leaving **16 of 193 = 8.3% substantive**, almost all of it interface-forced (there is
one way to consume R1, one way to consume `halving_representatives`, one way to discharge `T+T=0`).

Genuine divergence in structure: run A uses `strict_halving` + `mem_closure_of_strict_halving` with
generating set `{R | tmax R ≤ C} ∪ {T}`; run B uses `hgt_pow_four_le` + `strict_descent` +
`closure_eq_top` with an existential generating set, and isolates a fourth-power lemma run A does not.

**Neither took Claude's route.** My withheld check bounded the *raw* height via a finite doubling
orbit; both runs built a finite generating set for the *translated maximum* height and went through
finite generation plus torsion. Third consecutive stage where withholding the route produced
divergence from it — and here the runs' route is arguably better than mine.

## Boundary — unchanged

    FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
    ACTUAL_H1_SELMER_OBJECT  = NO
    touches_L_function       = NO
    PRIOR_ART_BLOCKER        = UNRESOLVED

Now certified for the H41 family: `E_q(ℚ)/2E_q(ℚ) ≅ ℤ/2ℤ`; every rational point is torsion;
`rank ℤ E_q(ℚ) = 0`; **`E_q(ℚ)` is finite**.

Still NOT certified: the order, exponent or isomorphism type of `E_q(ℚ)`; `E_q(ℚ)[2^∞] ≅ C₂` or
`v₂(|E_q(ℚ)|) = 1` — which needs `T ∉ 2E`, still `private` in the Gate-R modules; genuine
cohomological `Sel₂`; Ш or any of its torsion subgroups; central nonvanishing; analytic rank; BSD(2)
or full BSD; uniform all-H41 analytic control; novelty of 66b1.

Finiteness does not pin the 2-adic valuation: `C₄` is finite with quotient of order two and
`v₂ = 2`.
