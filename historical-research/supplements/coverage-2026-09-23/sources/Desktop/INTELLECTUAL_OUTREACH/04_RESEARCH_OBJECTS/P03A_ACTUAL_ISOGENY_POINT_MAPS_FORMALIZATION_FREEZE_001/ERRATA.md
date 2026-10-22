# Errata

Recorded, never silently repaired.

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and nonsplit `I₁` at
31 into a row about the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has
**nonsplit `I₄` at 2, split `I₁` at 31**. Tamagawa product `(2,1,2)` unaffected. Carried
unedited in every packet since.

## E2 — wrapper metadata defects, now in two distinct forms

**Run B — the familiar form, sixth consecutive occurrence.** Its `MANIFEST.sha256` is
byte-identical to the handoff's and replays 25/27, failing exactly the two files it changed.
Its `receipts/` still report one `sorry`, the `declaration uses sorry` build warning, and
`sorryAx` on `isogeny_coords_nonsingular`, `phiPoint`, `dualPhiPoint` and the branch lemmas.
All describe the **input**.

**Run A — a new form: an incomplete wrapper.** It returned 17 of the handoff's 28 files. Absent:
`MANIFEST.sha256`, `TASK.md`, `FORMALIZATION_BOUNDARY.md`, `SOURCE_REGISTER.md`, all five
`receipts/` and all four `references/`. Present: the entire `RequestProject/` source tree, the
three project pins, `README.md`, `ARISTOTLE_SUMMARY.md` and the input archive.

**Assessment.** Neither is a proof defect. Both rebuild clean here with zero `sorry` and
standard axioms, and all nine inherited Lean sources came back byte-identical in both. Run A's
missing files are the handoff's own documentation, preserved unchanged in `00_v1_handoff/`;
nothing needed to audit the proof is absent.

**Disposition.** Both trees preserved exactly as delivered, each with a
`STALE_METADATA_NOTICE.md`. This object's root `MANIFEST.sha256` and `receipts/` are canonical.

**Standing rule, confirmed across six returns and now in two failure modes:**

> **Never certify an Aristotle return from its own receipts.** The returned source is the
> object to audit; build, axiom, source-scan, manifest and deterministic-archive evidence is
> always regenerated externally.

The Run A form makes the rule easier to follow, not harder: there were no receipts to be
tempted by.

## E3 — both summaries under-count their own lemmas (upstream, cosmetic)

| | prose says | source has |
|---|---|---|
| Run A `ARISTOTLE_SUMMARY.md` | "four proved auxiliary lemmas" | **6** (`phiA_eq`, `phiB_eq`, `four_dualA_eq`, `sixteen_dualB_eq`, `phi_cubic_identity`, `dualPhi_cubic_identity`) |
| Run B `ARISTOTLE_SUMMARY.md` | "five proved auxiliary lemmas" | **7** (the four `family_*`, `isogeny_core`, `phi_coords_equation`, `dualPhi_coords_equation`) |

Both name every lemma correctly; only the numeral is wrong, and both err in the same
direction. This is the third instance of the pattern (P01 Run B said "four" and listed five).

Counted mechanically from source in `receipts/TARGET_STATEMENT_COMPARISON.txt` and both
`RUN_*_INDEPENDENT_REBUILD.txt`. No claim depends on the numbers. Uncorrected in the frozen
summaries.

**Standing practice:** count declarations from the source, never from a run's prose.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3.
Cross-referenced because the same filter question applies: this object's root manifest excludes
only itself, so both nested manifests (`00_v1_handoff/` and `02_run_B/tree/`) are covered as
ordinary entries. Run A returned no manifest, so there is none to cover there — itself part of
the E2 evidence.

## Not an erratum: the supplied route

The P03a handoff's `TASK.md` gave the pivotal identity, the substitution, the rescaling and
both coefficient bridges. Both runs therefore converged on the same four coefficient lemmas.
That is experiment design, disclosed in `STATUS.md` and `AB_ARCHITECTURE_COMPARISON.md` §1,
recorded here only so it is never read as something concealed.
