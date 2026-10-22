# Errata

Recorded, never silently repaired.

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and nonsplit `I₁`
at 31 into a row about the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has
**nonsplit `I₄` at 2, split `I₁` at 31**. Tamagawa product `(2,1,2)` unaffected; no
downstream conclusion changes. Carried unedited in every packet since.

## E2 — the Aristotle return ships input metadata as if it were output metadata (new)

`01_run_A/tree/MANIFEST.sha256` is byte-identical to the **handoff** manifest
(`e02195eb7edaefafa01062fa4315f94059b5e55932e07f113c7ce88fee5222e8`). Replayed against the
tree it accompanies it fails on the two files the run changed:

    README.md:                          FAILED
    RequestProject/Descent/Delta.lean:  FAILED
    18/20 OK

`01_run_A/tree/receipts/` is stale in the same way:

- `source_scan.txt` reports "exactly ONE 'sorry'" — true of the input, false of the output;
- `build.txt` carries the `declaration uses sorry` warning — no longer emitted;
- `nontautology_and_axioms.txt` records `delta_descent` as depending on `sorryAx` — it no
  longer does;
- `probe.lean` contains four deliberate `sorry`s — it is the **handoff's** non-tautology
  probe, not evidence about the completed proof.

**Assessment.** This is a custody/packaging defect, not a proof defect. The mathematics is
sound: the completed source rebuilds clean, contains zero occurrences of the string `sorry`,
and its axiom footprint is standard. The run's own `ARISTOTLE_SUMMARY.md` reports the state
accurately and explicitly flags `receipts/probe.lean` as "untouched supplied evidence, not
part of the build" — so the defect is that the wrapper did not regenerate metadata, not that
the run misreported anything.

**Disposition.** `01_run_A/tree/` is preserved **exactly as delivered**. Nothing in it was
edited, regenerated, or deleted. The canonical metadata for this object is the root
`MANIFEST.sha256` and `receipts/`, both produced here after an independent rebuild.
`01_run_A/STALE_METADATA_NOTICE.md` warns any reader who opens the tree directly.

**Standing instruction this produces.** A future Aristotle return must not be frozen on its
own metadata. Regenerate the source scan, the axiom audit, the build receipt, the manifest
and the archive from the returned source before sealing.

## E3 — Freeze 001 of saturation omits nested manifests from its own manifest (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3. Summarised
here because the same manifest filter was used to build this object:
`ARISTOTLE_DELTA_DESCENT_V1` contains no nested `MANIFEST.sha256`, so the handoff was not
affected. **This** object does contain nested manifests
(`00_v1_handoff/MANIFEST.sha256` and `01_run_A/tree/MANIFEST.sha256`), and its root manifest
excludes only itself, so both are covered here. That is deliberate: the stale return manifest
is evidence and must be under integrity control.
