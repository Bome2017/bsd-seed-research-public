# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error)

Base-curve Tamagawa data transcribed into a row about the twist. `BSD_CHAIN.md` §4 is
authoritative: the twist has nonsplit `I₄` at 2, split `I₁` at 31. Product `(2,1,2)`
unaffected.

## E2 — wrapper metadata defects, both returns, tenth and eleventh of this mode

Both runs shipped **stale metadata**: replay 33/35 OK, failing exactly the two files each run
wrote (`README.md`, `RequestProject/P04a/Cokernels.lean`). Each also shipped an unrequested
report — `P04A_COMPLETION_RECEIPT.md` (A), `P04A_COMPLETION_NOTES.md` (B). Both are the runs'
own accounts, not receipts, and are preserved unedited.

Neither is a proof defect. Both rebuild clean here — 8041 jobs, exit 0, zero `sorry`, standard
axioms — and all fourteen inherited Lean sources came back byte-identical in both.

> **Never certify an Aristotle return from its own receipts.** Regenerate build, axiom,
> source-scan, manifest and archive evidence externally; count declarations from source with
> block comments stripped.

Fifteen returns, fifteen defective metadata sets. This is the observed base rate, not a
precaution.

## E3 — Claude's declaration-counting regex could match prose (carried forward)

Recorded in full in `P03D_ISOGENY_COMPOSITES_FORMALIZATION_FREEZE_001/ERRATA.md` E3. All
counts in this object are comment-stripped.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (carried forward)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3. This object's
root manifest excludes only itself.

## E5 — earlier freeze archives embed host xattrs (carried forward)

Recorded in full in `P03E_DESCENT_KERNEL_IS_ISOGENY_IMAGE_FORMALIZATION_FREEZE_001/ERRATA.md`
E6. Every freeze archive before P03e carries `com.apple.provenance` / `com.apple.macl` pax
records and cannot be rebuilt byte-identically off this host. Contents intact, digests still
correct. Not repaired. This object uses the corrected recipe (`SOURCE_REGISTER.md`).

## E6 — Claude's first boundary scan measured the wrong scope (found and corrected pre-freeze)

The first draft of §6 of both per-run receipts scanned prohibited tokens over the **whole**
`RequestProject/` tree and then asserted "code-only = 0 for every one". That assertion was
**false as printed**: the same table showed `SelmerSet` = 5, `LocalKummerAll` = 7 and
`card` = 1 in code.

**Cause.** All eight occurrences are in inherited, byte-identical files — `Run013/Selmer.lean`
is where `SelmerSet` and `LocalKummerAll` are *defined*, and `SDyadic/Family.lean`'s single
`card` is the `Finset.card` inside `sCount`. None is reachable from `P04a.isogeny_cokernels`.
The boundary claim belongs to the one file each run wrote, not to the tree.

**Assessment.** Caught before the manifest was built; no frozen object carries the false line.
§6 now has two parts: 6a scopes the claim to `P04a/Cokernels.lean` (where every token really
is 0 in code), and 6b accounts for the tree-wide hits by file. Recorded rather than silently
corrected.

**Scope check.** Earlier freezes scanned only the file under test, so their boundary claims
are unaffected; the over-broad scan was introduced here.

## E7 — shared-name count over-credited independence, and has been corrected (new)

Until now replication strength was ranked partly by how many helper lemma names the two runs
shared, with 0 treated as strong evidence of architectural divergence — as it genuinely was
for P03b and P03d.

P04a scores **0 shared names and is confirmation-grade**. The two runs took the same route and
merely chose different names for the same eight lemmas (`cokerEquivE'` ↔ `cokerPhiEquiv`,
`mk_T'pt_ne_zero` ↔ `T'pt_class_ne_zero`, and so on). Name overlap measures vocabulary, not
architecture.

**Correction, effective here.** Shared-name counts are reported only alongside a **normalised
route comparison** — role-matched helpers α-renamed, comments stripped, unified diff — which
is in `receipts/PROOF_DIVERGENCE_MEASUREMENT.txt`. Earlier freezes' grades are not revised:
their route comparisons were done in prose and independently support what they claim. What
changes is that the number alone is no longer allowed to carry a grade.

## Not an erratum: P04a is confirmation-grade, and that was predicted

The handoff's own `TASK.md` and `receipts/nontautology_and_axioms.txt` said before it was sent
that the target is assembly and that the runs would likely converge. They did. Recorded so the
prediction and the measurement sit together.

## Not an erratum: "independent" means proof-search independence

Two independent Aristotle proof-search runs, same Lean kernel and same mathlib pin. This is
**not** independent proof-assistant verification, and the qualification is mandatory wherever
P04a is described.
