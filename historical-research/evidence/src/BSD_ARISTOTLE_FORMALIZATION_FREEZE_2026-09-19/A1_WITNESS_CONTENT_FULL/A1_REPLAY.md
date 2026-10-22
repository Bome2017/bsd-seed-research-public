# A1_REPLAY — independent custodian replay of the Aristotle A1 return (2026-09-19)

## Inputs
| item | value |
|---|---|
| returned archive | `~/Downloads/0ee48359-59b9-4108-a7fd-0ee16939d0e4-aristotle.tar.gz`, sha256 `278588e0c570e39379e7dd2a495153d984be12e4269fee212e3830cc15e59948`, 83 397 bytes; byte-identical copy in the parent folder's `provenance/` |
| original package | `~/BSD_ARISTOTLE_PACKAGES_2026-09-19/ARISTOTLE_A1_WITNESS_CONTENT_2026-09-19.tar.gz`, sha256 `eba016585d080c5bf8578b3c4454d63a256712a6770ba50f3a0f671667a04763` (also embedded unchanged in the returned archive) |
| Lean | `Lean (version 4.28.0, x86_64-apple-darwin24.6.0, commit 7e01a1bf5c70fc6167d49c345d3bf80596e9a79b, Release)`; Lake 5.0.0-src+7e01a1b |
| mathlib | `8f9d9cff6bd728b17a24e163c9402775d9e6a365` (tag v4.28.0). This is the rev pinned by both returned `lake-manifest.json` files and the `git rev-parse HEAD` of the attached package |
| host | macOS 26.7, Intel i9-10910 |

**Offline mathlib.** mathlib was attached as `.lake/packages`: an APFS clone of the prebuilt
`~/run013-family-minimisation-successor-2026-09-10/.lake/packages`, with no network access. Only the package's own modules were
rebuilt.

## Procedure (fresh directory; nothing trusted from the returned logs)
1. `tar -xzf` into a fresh scratch directory. The package tree is `ARISTOTLE_A1_WITNESS_CONTENT_2026-09-19_aristotle/A1_WITNESS_CONTENT/`.
2. `shasum -a 256 -c scripts/FROZEN.sha256` gives **6/6 OK**.
3. `rm -rf .lake/build && lake build` gives **`Build completed successfully (8037 jobs)`**, in 133.3 s wall.
   - There were **0 `declaration uses 'sorry'` warnings, 0 warnings in total, and 0 errors.**
   - All 11 library modules were built: Defs, Spec, Depth, Instances, GroupRing, Primary, Countermodels, Stretch, WC, Targets,
     and the root.
4. `bash scripts/acceptance.sh` (the package's own, unchanged script; it does a second clean build) gave:
   - frozen 6/6 OK;
   - build OK;
   - token scan "(none)";
   - **`LEVEL: A1_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, `STRETCH_CLEAN: ['lemmaA_general', 'gr_finite_Z', 'gr_rational_trivial']`**.
5. A fresh `lake env lean WitnessContent/Acceptance.lean` showed, for all 20 targets, axioms ⊆ {propext, Classical.choice, Quot.sound}.
   `zero_infinitely_divisible` uses `propext` only. **No `sorryAx`, and no other axiom.**
6. The independent audit `audit/TypeIntegrity.lean`, via `lake env lean` (a custodian meta-check, not part of the library),
   passed three checks:
   - every target's declared type is **syntactically** the frozen constant `WitnessContent.Spec.<Name>`;
   - kernel re-checks through fully qualified names (`example : WitnessContent.Spec.WC_abstract := WitnessContent.WC_abstract`
     and the like) pass for WC_abstract, WC_groupRing, CM_uniform_denominator, CM_nonzero_everywhere and WC_abstract_nonvacuous;
   - the `WitnessContent.Spec` namespace contains exactly the 20 frozen constants.
7. **Source scan** of all 13 `.lean` files of the return (code and comments):
   - no `sorry` / `admit` / `axiom` / `unsafe` / `@[extern]` / `implemented_by` / `native_decide` / `opaque` / `@[csimp]` /
     macro-elab / `debug.*`;
   - no new instances or definitions;
   - only `set_option maxHeartbeats` and `synthInstance.maxHeartbeats` in `WC.lean`, which are performance limits, not soundness
     switches;
   - `RequestProject/Main.lean` is Aristotle wrapper boilerplate and is not imported by the library.

The returned `axioms.log` has the same content as the fresh probe. The returned `build.log` is superseded by the fresh logs.

## Evidence (in `replay/`)
- `frozen_and_file_comparison.txt`
- `fresh_lake_build.log`
- `fresh_acceptance.log`
- `fresh_axioms.log`
- `type_integrity.log`
- `source_scan.txt`
- `replay_driver.log`

## Custody defect found and repaired
- The returned package still carries the ORIGINAL pre-run `MANIFEST.sha256`. Against the returned tree it gives 21/24 OK:
  `Targets.lean`, `STATE.json` and `RESUME.md` FAIL, and the 9 new files (7 Lean helpers, `build.log`, `axioms.log`) are
  unbound. This is expected after a proof run, but it is not a valid freeze.
- **Repair.** That file is preserved byte-exactly inside `source/` for provenance (it is historical and stale by design).
  Custody of every retained file is now bound by the NEW `MANIFEST.sha256` of this freeze directory, generated after all files
  were stable. The returned archive and the original package are not modified.

## Replay of the freeze archive itself
- The first A1 freeze archive (sha256 `dfe5f660…`) was unpacked into a fresh directory.
  - Manifest 56/56 OK, file set exact.
  - A fresh mathlib clone was attached, and `bash scripts/acceptance.sh` ran on `source/…/A1_WITNESS_CONTENT`:
    `Build completed successfully (8037 jobs)`, 0 sorry, `LEVEL: A1_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, stretch 3/3.
  - `audit/TypeIntegrity.lean` gave 20/20 OK. There were 20 clean axiom lines and 0 `sorryAx`.
- The freeze was then regenerated after the A2 intake. Only `A1_FORMAL_BOUNDARY.md` (the Codex O1 note), this file and
  `STATE.json`/`RESUME.md` changed. The `source/` tree is byte-identical (bound by the manifest), so the source replay carries over.
  The regenerated archive was replayed again: see `../FREEZE_INDEX.md`.
