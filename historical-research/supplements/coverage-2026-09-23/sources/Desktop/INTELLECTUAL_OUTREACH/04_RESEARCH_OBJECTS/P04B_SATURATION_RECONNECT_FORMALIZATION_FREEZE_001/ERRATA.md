# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error)

Base-curve Tamagawa data transcribed into a row about the twist. `BSD_CHAIN.md` §4 is
authoritative: the twist has nonsplit `I₄` at 2, split `I₁` at 31. Product `(2,1,2)`
unaffected.

## E2 — wrapper metadata defects, both returns, twelfth and thirteenth of this mode

Both runs shipped **stale metadata**: replay 47/49 OK, failing exactly the two files each run
wrote. Each also shipped an unrequested report — `RECONNECT_RUN_RECEIPTS.md` (A),
`P04B_RECONNECT_RESULT.md` (B) — preserved unedited as the runs' own accounts, not receipts.

Neither is a proof defect. Both rebuild clean here — 8055 jobs, exit 0, zero `sorry`, standard
axioms — and all twenty-nine inherited Lean sources came back byte-identical in both.

> **Never certify an Aristotle return from its own receipts.** Regenerate build, axiom,
> source-scan, manifest and archive evidence externally; count declarations from source with
> block comments stripped.

Seventeen returns, seventeen defective metadata sets.

## E3 — declaration-counting regex could match prose (carried forward)

Recorded in full in `P03D_ISOGENY_COMPOSITES_FORMALIZATION_FREEZE_001/ERRATA.md` E3. All counts
in this object are comment-stripped.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (carried forward)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3.

## E5 — freeze archives before P03e embed host xattrs (carried forward)

Recorded in full in `P03E_…FREEZE_001/ERRATA.md` E6. Not repaired. This object uses the
corrected recipe.

## E6 — boundary scans must be scoped to the file under test (carried forward)

Recorded in full in `P04A_ISOGENY_COKERNELS_FORMALIZATION_FREEZE_001/ERRATA.md` E6. This
object's §6 is scoped to `RequestProject/P04b/Reconnect.lean` from the outset.

## E7 — shared-name counts carry no grade (carried forward, and confirmed backwards here)

Recorded in full in `P04A_…FREEZE_001/ERRATA.md` E7. P04b is the confirming case, in the
opposite direction: it scores **5** shared helper names and is an architectural cross-check,
while P04a scored **0** and was confirmation-grade. The count is now always reported alongside
a normalised route comparison and, new here, a **citation profile** — which certified results
each run actually consumed, counted in code with comments stripped. That third measurement is
what exposed the sharpest difference between these two runs and would have been invisible to
either of the other two.

## E8 — the prose orientation error, corrected before it could be frozen (recorded, not repaired)

Before this stage the project's prose described `range δ_E` as `K_exp = ⟨[D]⟩`. That is **false**:
`SDyadic.dual_exhaustion` allows only the class `1`, `SDyadic.cov_dual_one` is the only dual
witness, and `KExp` appears in the saturation object solely inside
`((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2`.

**Where it came from.** Notation shorthand — `K_exp` sat opposite `G_{φ,exp}` in the write-up,
and the dual side was assumed to mirror the φ side.

**Assessment.** Caught by reading the frozen saturation sources while scoping P04b, *before* any
Lean statement was written. It never entered a frozen object, and it is now excluded by a
certified theorem: `range δ_E = ⊥`, and `KExp` is the image of `ker φ̂` under `δ_{E'}`. Recorded
because the failure mode — trusting notation symmetry over the frozen definitions — is the one
the custody discipline exists to catch.

## Not an erratum: what P04b does and does not consume

Neither proof uses the **hard** direction of the saturation equivalence. Both need only
`Cov ⟹ LocalKummerAll`, which is base change, together with `phi_exhaustion` /
`dual_exhaustion` — which are the hard local analysis, taken at lemma level rather than through
the packaged theorem. `GlobalSet = SelmerSet` is not a dependency of either P04b proof.
Recorded so that no later description overstates the dependency.

## Not an erratum: `cls_phiB_eq_cls_DD` is Claude's, not a run's

The elementary bridge was authored and proved in the handoff. Both runs returned it
byte-identical and used it. It is plumbing supplied with the statement, in the same category as
`P04a.deltaHomE` / `deltaHomE'`, and must not be described as run-certified mathematics. See
`SOURCE_REGISTER.md`.

## Not an erratum: "independent" means proof-search independence

Two independent Aristotle proof-search runs, same Lean kernel and same mathlib pin. **Not**
independent proof-assistant verification. The qualification is mandatory wherever P04b is
described.
