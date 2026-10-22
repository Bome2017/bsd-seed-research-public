# A2_REPLAY — independent custodian replay of the Aristotle A2 return (2026-09-19)

## Inputs
| item | value |
|---|---|
| returned archive | `~/Downloads/319b9855-0c13-441d-ac5c-6d540f5f2472-aristotle.tar.gz`, sha256 `92ba674767e56012572b357ca29e5e90fc6b057a016611808f457df59ed3db50`, 80 036 bytes; byte-identical copy in the parent folder's `provenance/` |
| original package | `~/BSD_ARISTOTLE_PACKAGES_2026-09-19/ARISTOTLE_A2_PRIMARY_SUPPORT_2026-09-19.tar.gz`, sha256 `36005a0c92b8c847aea601ca87e33b6284a967ff1d8e295a112ed783b6b79bef` (also embedded unchanged in the return) |
| package path in the return | `ARISTOTLE_A2_PRIMARY_SUPPORT_2026-09-19_aristotle/pkg/A2_PRIMARY_SUPPORT/`. Aristotle nested it under `pkg/`, and the root wrapper lakefile adds a convenience library entry; the package's own frozen lakefile is untouched |
| Lean | 4.28.0 (commit 7e01a1bf5c70fc6167d49c345d3bf80596e9a79b); Lake 5.0.0-src+7e01a1b |
| mathlib | `8f9d9cff6bd728b17a24e163c9402775d9e6a365` (v4.28.0), as pinned in the unchanged package `lake-manifest.json` |
| host | macOS 26.7, Intel i9-10910. The prebuilt mathlib was attached as an APFS clone; there was no network access |

## Procedure (fresh directory; the returned logs were not trusted)
1. Fresh `tar -xzf`, then `shasum -a 256 -c scripts/FROZEN.sha256` gives **6/6 OK**.
2. `rm -rf .lake/build && lake build` gives **`Build completed successfully (8040 jobs)`** in 108.7 s wall.
   - There were **0 `sorry` warnings, 0 warnings in total, and 0 errors.**
   - All 14 library modules were built: Defs, Spec, Pairing, Content, Depth, Primary, Symplectic, Descent, LemmaB, Countermodels,
     Order, CodexExample, Targets, and the root.
3. `bash scripts/acceptance.sh` (the unchanged script, with a second clean build) gave:
   - frozen 6/6;
   - build OK;
   - **`LEVEL: A2_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, `STRETCH_CLEAN: ['alternating_square', 'CM_noncyclic_target', 'CM_codex_torsion_example']`**.
4. A fresh `lake env lean PrimarySupport/Acceptance.lean` showed, for all 28 targets, axioms ⊆ {propext, Classical.choice, Quot.sound}.
   `primary_zero_of_torsionfree` uses only {propext, Quot.sound}. **No `sorryAx`, and no other axiom.** The returned `axioms.log`
   has the same content.
5. The custodian meta-check `audit/TypeIntegrity.lean` passed three checks:
   - all **28/28** declared types are syntactically the frozen constants `PrimarySupport.Spec.<Name>`;
   - 12 kernel re-checks of the boundary-sensitive targets pass;
   - the `PrimarySupport.Spec` namespace holds exactly the 28 frozen constants.
6. **Source scan** of the 16 `.lean` files (code and comments):
   - the only `sorry` tokens are the two original docstring lines of `Targets.lean` ("replace every `sorry`"), which are comments;
   - no admit / axiom / unsafe / extern / implemented_by / native_decide / opaque / csimp / macro-elab / `set_option`;
   - no instance declarations;
   - the new definitions are helper data only (countermodel types, the cross product, `sumMap`, `depthProd`).

Evidence is in `replay/`.

## Custody defect found and repaired
- The returned package keeps the ORIGINAL pre-run `MANIFEST.sha256`. Against the returned tree it gives 21/24:
  `Targets.lean`, `STATE.json` and `RESUME.md` FAIL, and the 12 new files (10 Lean helpers, `build.log`, `axioms.log`) are unbound.
- It is retained byte-exactly in `source/` as a historical file.
- Custody is now the NEW `MANIFEST.sha256` of this directory. Neither the returned archive nor the original package was modified.
