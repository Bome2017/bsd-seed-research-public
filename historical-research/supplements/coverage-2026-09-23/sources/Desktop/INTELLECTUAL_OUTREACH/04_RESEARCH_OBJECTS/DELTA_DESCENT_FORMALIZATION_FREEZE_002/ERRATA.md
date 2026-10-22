# Errata

Recorded, never silently repaired.

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and nonsplit `I₁`
at 31 into a row about the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has
**nonsplit `I₄` at 2, split `I₁` at 31**. Tamagawa product `(2,1,2)` unaffected; no downstream
conclusion changes. Carried unedited in every packet since.

## E2 — both Aristotle returns ship input metadata as if it were output metadata

Carried forward from Freeze 001 and now confirmed to recur in Run B.

`01_run_A/tree/MANIFEST.sha256` and `02_run_B/tree/MANIFEST.sha256` are each byte-identical to
the **handoff** manifest (`e02195eb7edaefafa01062fa4315f94059b5e55932e07f113c7ce88fee5222e8`).
Replayed against the trees they accompany, each fails on the two files its run changed:

    README.md:                          FAILED
    RequestProject/Descent/Delta.lean:  FAILED
    18/20 OK

Both trees' `receipts/` are stale in the same way: `source_scan.txt` reports one `sorry`,
`build.txt` carries the `declaration uses sorry` warning, `nontautology_and_axioms.txt`
records `delta_descent` as depending on `sorryAx`, and `probe.lean` holds four deliberate
`sorry`s. All describe the input.

**Assessment.** A custody/packaging defect in the wrapper, not a proof defect, and now clearly
a systematic property of the wrapper rather than a one-off. Both runs' own summaries report
their state accurately; Run B additionally shipped `VERIFICATION.md`, which is current and
correct. Run A shipped no equivalent.

**Disposition.** Both trees are preserved **exactly as delivered**. Canonical metadata is this
object's root `MANIFEST.sha256` and `receipts/`. Each run directory carries a
`STALE_METADATA_NOTICE.md`.

**Standing instruction, now confirmed twice.** Never freeze an Aristotle return on its own
metadata. Regenerate the source scan, axiom audit, build receipt, manifest and archive from
the returned source before sealing.

## E3 — saturation Freeze 001's root manifest omits its nested manifests (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3. Cross-
referenced here because the same filter question applies: this object's root manifest excludes
only itself, so all three nested manifests
(`00_v1_handoff/`, `01_run_A/tree/`, `02_run_B/tree/`) are covered as ordinary entries. That
is deliberate — the two stale return manifests are evidence for E2 and must be under
integrity control.

## Not an erratum: the shared hint

Both Delta runs received the intersection-cubic/root-product mechanism in their input. That is
a property of the experiment design, not a defect, and it is disclosed in `STATUS.md` and
`AB_ARCHITECTURE_COMPARISON.md` §1. It is recorded here only so that nobody later "discovers"
it and reads it as something that was concealed.
