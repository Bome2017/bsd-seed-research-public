# STATUS — GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001

## Disposition

    GATE R RESULT      LEAN_CERTIFIED
    CERTIFICATION      two independent Aristotle proof searches, both externally rebuilt
    AXIOMS             [propext, Classical.choice, Quot.sound] on all five outputs, both runs
    REPLICATION        confirmation-grade with substantive route divergence

The certified statement, for the H41 family, on mathlib's actual rational point group:

```lean
theorem GateR.h41_rank_zero
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    Module.rank ℤ (P01.Ecurve ε m q).toAffine.Point = (0 : Cardinal)
```

`Module.rank` valued in `Cardinal.{0}`, over `ℤ`, on `WeierstrassCurve.Affine.Point` of
`P01.Ecurve ε m q` over `ℚ`, under the canonical `AddCommGroup.toIntModule` structure — read
off the elaborated term, not the source. No `finrank`, no `Group.rank`, no surrogate group, no
added hypothesis. **`rank E_q(ℚ) = 0` is Lean-certified for the H41 family.**

Together with the four supporting outputs: `height_sublevels`, `halving_representatives`,
`bounded_halving`, `every_point_torsion`.

## What was verified externally, never from the runs' receipts

| Check | Run A | Run B |
|---|---|---|
| Input the run received | packet digest `9f15927e…`, exact | exact |
| `sorry` / `admit` in deliverable | 0 | 0 |
| Frozen Lean sources altered | **0 of 35** | **0 of 35** |
| Lean files added outside the deliverable | 0 | 0 |
| Fresh `lake build`, independent package base | 8062 jobs, exit 0 | 8062 jobs, exit 0 |
| Five propositions identical to shipped, by typechecking | **yes** | **yes** |
| `translateMax` still the shipped definition, by `rfl` | yes | yes |
| Axiom footprint, regenerated | standard ×5 | standard ×5 |
| Forbidden-construct scan, scoped to deliverable | all 0 | all 0 |
| Elaborates over the *other* certified base (run_B) | exit 0 | exit 0 |
| Dependency footprint (endpoint) | 366 | 366 |

Type identity was tested by discharging the verbatim target types with the returned theorems,
not by comparing source text. A run that kept the names and changed a proposition would have
failed that test.

## Replication, measured

332 vs 289 lines. 13 declarations each. Of 9 shared names, 6 are names I mandated, so the
genuinely shared private helpers are **three**. Normalised route comparison after
α-renaming the role-matched encoder pair: similarity 0.302, of which 27 lines are text I
shipped and 18 are generic tactic boilerplate — leaving **31 substantively convergent lines out
of 393, or 7.9%**. Citation profiles: 23 each, 17 shared, Jaccard **0.586**.

Genuine divergence: Run A encodes points into `Option (ℚ × ℚ)` with a `y² = c` fibre argument,
Run B into an x-coordinate plus a **Boolean** sign of y; the descent plumbing to `T ∉ 2E`
differs (`P04a`/`P03c` cokernel identities versus `P04c` kernel transport); Run A inlines the
two doubling cases, Run B isolates a generic fourth-power lemma.

**The most interesting finding.** About 22 of the 31 convergent lines are one lemma,
`cls_q_not_mem_KExp`. Both runs proved `[q] ∉ KExp` by **prime/square arithmetic**. The Codex
review predicted a closure/index contradiction and said explicitly "No new prime/square
arithmetic"; both Pro designs and Claude's private reachability check used that index route too.
Both runs independently declined it. Withholding the route produced a genuine divergence from
every prior design.

## Read this alongside the result

Reachability was established **before** these runs were commissioned:
`GATE_R_FINAL_ASSEMBLY_PRESHIP_RECORD_001`, receipt `WITHHELD_ROUTE.txt`, dated earlier. A PASS
confirms that two independent searches found their own routes and that the propositions hold in
the pinned environment. **It does not establish that the assembly was hard — it was known to be
closeable.** What the runs added, which the private check could not, is two independent
constructions and the prime/square divergence above. See `receipts/REACHABILITY_DISCLOSURE.txt`.

## Errata

Five, in `ERRATA.md`. Two are mine: an inherited-bytes check that omitted every shipped `.md`
and `.txt` and so missed the README banner, and **a construct scanner that was silently broken
and printed a row of zeros** — caught only by running positive controls, the third appearance of
that defect family. Also: the platform attribution banner in both returns, the inherited
`SelmerSet`/`LocalKummer` hits scoped correctly on the second pass, both runs' custody
self-reports overstating by omitting the README change, and one Run B build figure I did not
verify.

## Programme state

    H1-free actual-point bridge      DONE     (P01, P03a-e, P04a-c)
    Gate R / algebraic rank zero     DONE     this object
    genuine Sel2 / Sha  (Gate C)     REMAINING
    analytic BSD        (Gate A)     REMAINING — highest mathematical uncertainty

## Boundary — unchanged

    FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
    ACTUAL_H1_SELMER_OBJECT  = NO
    touches_L_function       = NO
    PRIOR_ART_BLOCKER        = UNRESOLVED

This certifies **algebraic** rank zero for the H41 family. It is not an analytic-rank
statement, not a BSD result, not a classification of the rational points, and not a claim about
any curve outside `Params` with `H41` and `m ≥ 3`. No novelty or priority claim is authorised:
`PRIOR_ART_BLOCKER` remains `UNRESOLVED` and no literature comparison has been performed.

"Independent" continues to mean two independent Aristotle proof-search runs at one Lean kernel
and one mathlib pin. It has never meant independent proof-assistant verification.
