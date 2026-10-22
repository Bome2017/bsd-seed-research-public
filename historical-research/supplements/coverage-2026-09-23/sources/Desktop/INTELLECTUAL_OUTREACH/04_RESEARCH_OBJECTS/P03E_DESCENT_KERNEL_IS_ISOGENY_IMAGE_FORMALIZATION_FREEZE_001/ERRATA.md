# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error)

Base-curve Tamagawa data transcribed into a row about the twist. `BSD_CHAIN.md` §4 is
authoritative: the twist has nonsplit `I₄` at 2, split `I₁` at 31. Product `(2,1,2)`
unaffected.

## E2 — wrapper metadata defects, twelfth and thirteenth occurrences

Run A: **partial wrapper**, 19 of the handoff's 33 files — no manifest, no receipts, no
references. Third occurrence of this mode (P03a Run A, P03d Run A).

Run B: **stale metadata**, replay 30/32 OK, failing exactly the two files it changed
(`README.md`, `RequestProject/P03e/Bridge.lean`). Ninth occurrence. Run B additionally shipped
an unrequested `P03E_RESULT.md`; it is the run's own report, not a receipt, and is preserved
unedited.

Neither is a proof defect. Both rebuild clean here — 8040 jobs, exit 0, zero `sorry`, standard
axioms — and all twelve inherited Lean sources came back byte-identical in both.

> **Never certify an Aristotle return from its own receipts.** Regenerate build, axiom,
> source-scan, manifest and archive evidence externally; count declarations from source with
> block comments stripped.

Thirteen returns, thirteen defective metadata sets. The rule is not a precaution any more; it
is the observed base rate.

## E3 — Claude's declaration-counting regex could match prose (carried forward)

Recorded in full in `P03D_ISOGENY_COMPOSITES_FORMALIZATION_FREEZE_001/ERRATA.md` E3. A
line-anchored `^(theorem|lemma|def|abbrev) NAME` regex also matches the word `theorem` where
it begins a sentence inside a block comment. All counts in this object are comment-stripped.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (carried forward)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3. This object's
root manifest excludes only itself, so all nested manifests are covered.

## E5 — the earlier handoff-size figure was 32, the correct figure is 33

While drafting this object's receipts the V1 handoff was first described as 32 files. The
archive contains **33**. Corrected here and in `receipts/RUN_A_INDEPENDENT_VERIFICATION.txt`
before the manifest was built; no frozen object carries the wrong figure. The Run B stale-replay
figure 30/32 is correct as stated — a manifest does not list itself, so 33 files yield 32
entries.

## E6 — earlier freeze archives embed host xattrs (found here, earlier objects NOT repaired)

Rebuilding `P03D_…FREEZE_001.tar.gz` from its own frozen directory to confirm the archive
recipe produced a different digest. The uncompressed tar streams differ at byte 2: every
earlier freeze archive was written in pax format carrying macOS extended attributes —
`com.apple.provenance` and `com.apple.macl` — one pair of pax records per entry (about
164 KiB of host-specific metadata in the P03d archive). Entry list, modes, uid/gid and
timestamps are otherwise identical.

**Assessment.** Not a content defect: every earlier archive still hashes to its recorded
digest, and every file inside it is intact. It is a *reproducibility* defect — those archives
cannot be rebuilt byte-identically on another machine, because the embedded xattrs encode this
host. Entry order was also filesystem-walk order rather than sorted.

**Not repaired.** No frozen object is rewritten. This object's archive uses the corrected
recipe, recorded verbatim in `SOURCE_REGISTER.md`, and was built twice and compared to confirm
it is byte-reproducible.

## Not an erratum: four shared helper names

`cls_phiB_ne_one`, `dualPhiPoint_Qpt`, `exists_phi_preimage`, `exists_dualPhi_preimage` appear
in both runs. They are forced by the statement and by the handoff's own TASK.md, which named
the two exceptional behaviours as required self-consistency checks. The **reverse
constructions**, which are the substance of the theorem, are organised differently in the two
runs; `receipts/PROOF_DIVERGENCE_MEASUREMENT.txt` measures the gap and calibrates it against
every earlier stage.

## Not an erratum: "independent" means proof-search independence

Two independent Aristotle proof-search runs, same Lean kernel and same mathlib pin. This is
**not** independent proof-assistant verification, and the qualification is mandatory wherever
P03e is described.
