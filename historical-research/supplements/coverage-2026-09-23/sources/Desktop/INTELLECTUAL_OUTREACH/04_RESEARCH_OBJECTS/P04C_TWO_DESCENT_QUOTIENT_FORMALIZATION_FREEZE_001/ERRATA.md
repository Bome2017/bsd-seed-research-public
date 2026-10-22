# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error)

Base-curve Tamagawa data transcribed into a row about the twist. `BSD_CHAIN.md` §4 is
authoritative: the twist has nonsplit `I₄` at 2, split `I₁` at 31. Product `(2,1,2)` unaffected.

## E2 — wrapper metadata defects, both returns, fourteenth and fifteenth of this mode

Both runs shipped **stale metadata**: replay 51/53 OK, failing exactly the two files each wrote.
Each also shipped an unrequested report — `P04C_COMPLETION_NOTES.md` (A),
`receipts_p04c_completion/verification.txt` (B) — preserved unedited as the runs' own accounts.

Neither is a proof defect. Both rebuild clean here — 8056 jobs, exit 0, zero `sorry`, standard
axioms — and all thirty inherited Lean sources came back byte-identical in both.

> **Never certify an Aristotle return from its own receipts.**

For the programme-wide tally, and for the one return that was clean, see E10 — the running
"Nth occurrence" counts used in these notices are **not** a consistent series.

## E3 — declaration-counting regex could match prose (carried forward)

`P03D_…FREEZE_001/ERRATA.md` E3. All counts here are comment-stripped.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (carried forward)

`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3.

## E5 — freeze archives before P03e embed host xattrs (carried forward)

`P03E_…FREEZE_001/ERRATA.md` E6. Not repaired; this object uses the corrected recipe.

## E6 — boundary scans must be scoped to the file under test (carried forward)

`P04A_…FREEZE_001/ERRATA.md` E6. This object's §6 is scoped from the outset.

## E7 — shared-name counts carry no grade (carried forward, third confirmation)

`P04A_…FREEZE_001/ERRATA.md` E7, confirmed in the opposite direction by P04b. P04c is the third
confirmation and the sharpest: **2 shared names, the second lowest of any stage, and
confirmation-grade.** The grade rests on the normalised route comparison, the citation profile,
and — new here — the transitive dependency footprint.

## E8 — the prose orientation error (carried forward)

`P04B_…FREEZE_001/ERRATA.md` E8. `range δ_E` is trivial; `KExp` is the image of `ker φ̂` under
`δ_{E'}`. Corrected before any Lean statement was written; never entered a frozen object.

## E9 — a supplied lemma that nothing used (new, recorded not repaired)

`P04c.KExp_le_GphiExp` was authored and proved in the handoff by Claude, on the reasoning that
the run would need it and that it makes the statement's `(KExp).subgroupOf (GphiExp)` the
intended subgroup rather than an intersection. The transitive dependency footprint shows
**neither run used it**.

**Assessment.** Not a defect in the frozen result: it is proved, clean, and the second half of
the reasoning stands — it does document the statement's intent. But the first half was wrong,
and supplying it was a small unnecessary widening of Claude-authored content in a handoff whose
whole point was that the mathematics comes from the runs. Recorded because the pattern —
supplying "plumbing the run will surely need" — is how authored content creeps into a
certification chain. The same check should be run on `cls_phiB_eq_cls_DD` (P04b): the P04c
footprint shows it **is** a genuine dependency, so that one earned its place.

## E10 — the running metadata-defect ordinals are not a consistent count (new)

Each `STALE_METADATA_NOTICE.md` in this programme carries a running ordinal — "ninth
occurrence", "twelfth occurrence". A census of the notices actually on disk shows those ordinals
are **not a single consistent series**: the P03c pair is numbered "ninth consecutive occurrence"
while the later P03d Run B notice is numbered "eighth occurrence", so two different counting
bases were used and crossed. Every individual notice correctly describes its own return; only
the running numbering is unreliable.

**The disk census supersedes the ordinals.** As of this freeze:

    22 Aristotle returns across 11 stages, two accounts
    21 notice files across the freezes, covering 20 distinct returns
       (Delta Run A is carried in both Delta freezes, so its notice appears twice)
    modes: 18 stale-manifest notices (17 distinct returns) + 3 partial-wrapper notices
    saturation Run A: shipped NO root manifest; it returned the handoff's manifest unchanged
    saturation Run B: shipped a CORRECT successor manifest, replaying 30/30 against its own
       tree, recorded at the time as "E2 — none found in Run B"

So the accurate statement is: **21 of 22 returns shipped defective or absent metadata; exactly
one — saturation Run B, the very first stage — shipped a correct successor manifest, and no
return since has.**

**Assessment.** Claude's error, and a claim in this object's own first draft: it asserted
"nineteen returns, nineteen defective metadata sets" and that no return had ever shipped correct
metadata. Both were wrong — the count was off and the saturation Run B exception was on record in
`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E2 the whole time. Caught by counting
from disk before this object was sealed; corrected here and in
`THEOREM_STATUS_H1_FREE_BRIDGE_COMPLETE_001`. **Earlier freezes are not rewritten** — their
ordinals stand as written, with this erratum as the pointer. The lesson is the programme's own:
a running tally carried forward by hand is exactly the kind of claim that must be recomputed
from the artifacts, not incremented from memory.

## Not an erratum: the route nobody predicted

Before sending, each conjunct was proved privately to confirm reachability, by transporting
along `P04a.isogeny_cokernels`. **Neither run took that route**; both built two surjections out
of `E'_q(ℚ)` with a common kernel, and `E'_q(ℚ) ⧸ φ(E_q(ℚ))` never appears as an intermediate
object in either proof. The reachability check did its job — establish that a proof exists — and
was not predictive of the proof found. Recorded because it is the clearest evidence in the
programme that withholding the route is worth doing.

## Not an erratum: what the result does not say

`Nat.card (E_q(ℚ) ⧸ 2E_q(ℚ)) = 2` does **not** give `rank E_q(ℚ) = 0`, and does not say
`E_q(ℚ)` is finite. `Finite` and `Fintype` are 0 in code in both returns; no finiteness
hypothesis exists anywhere in the development. `STATUS.md` and
`THEOREM_STATUS_H1_FREE_BRIDGE_COMPLETE_001` state the boundary in full.

## Not an erratum: "independent" means proof-search independence

Two independent Aristotle proof-search runs, same Lean kernel and same mathlib pin. **Not**
independent proof-assistant verification. Mandatory wherever P04c is described.
