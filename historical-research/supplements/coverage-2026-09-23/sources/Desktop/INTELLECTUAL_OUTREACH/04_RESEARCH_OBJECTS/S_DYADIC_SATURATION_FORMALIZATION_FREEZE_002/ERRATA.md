# Errata

Recorded, never silently repaired.

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and nonsplit `I₁`
at 31 into a row about the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has
**nonsplit `I₄` at 2, split `I₁` at 31**. Tamagawa product `(2,1,2)` unaffected, no
downstream conclusion changes. Carried unedited in every packet since.

## E2 — none found in Run B

Run B's return was checked for the packaging defects found in the Delta return
(stale manifest, stale receipts describing the input rather than the output). Run B's
`MANIFEST.sha256` replays **30/30 against its own tree**, and its receipts describe its own
completed state. No defect found.

## E3 — Freeze 001's root manifest does not cover its nested manifests (Claude's error, new)

`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_001/MANIFEST.sha256` was generated with a filter
that excluded **every** file named `MANIFEST.sha256`, not just the root one. Two files in
that tree are therefore outside its own integrity check:

    00_v1_handoff/MANIFEST.sha256          7166fb7999d186726300e7d09495b674b8237e47b39f7e7b6387f2b6684340a4
    01_run_A/tree/docs/MANIFEST.sha256     7166fb7999d186726300e7d09495b674b8237e47b39f7e7b6387f2b6684340a4

Freeze 001 reports 65 entries for a tree of 67 files. A modification to either nested
manifest would not be caught by replaying Freeze 001's root manifest.

**Assessment.** No content is wrong and no conclusion changes — both nested manifests are
present and both hash to `7166fb79…`, the expected V1 handoff manifest, which is itself the
evidence that Run A consumed the exact handoff. The defect is coverage, not correctness.

**Disposition.** Freeze 001 is **not** edited. Its manifest, entry count, and zip stay as
sealed. This object fixes the filter for itself: Freeze 002's manifest excludes only its own
root manifest and covers all three nested ones, which is why it reports 107 entries rather
than 104.

The same filter was used for `POST_SATURATION_SEL2_BRIDGE_FREEZE_001` and
`ARISTOTLE_DELTA_DESCENT_V1`; neither contains a nested `MANIFEST.sha256`, so neither is
affected.

## Nothing else carried from Freeze 001

Freeze 001 recorded no errata of its own. Its content is reproduced here unchanged.
