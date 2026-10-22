# A5 proof replay: A5_FULL, Sha[3^∞] ≅ (ℤ/3)² deduction machine-checked (custodian, 2026-09-25)

| | |
|---|---|
| frozen statements | `ARISTOTLE_A5_SHA3_v2_2026-09-24.tar.gz`, sha256 `cb374846…379d` (unchanged since its audit) |
| proved package | `ARISTOTLE_A5_SHA3_proved_2026-09-25.tar.gz` (one proof run by the author's proof tooling) |

## Checks (fresh copy, fresh build directory)

1. **Frozen files.** `Defs.lean`, `Spec.lean`, `Acceptance.lean`, `lakefile.toml`, `lean-toolchain` and `scripts/level.py`
   all match the ORIGINAL v2 archive (6/6).
2. **Changes.** Only `ShaThree/Targets.lean`, `STATE.json` and `RESUME.md` changed. Five proof files were added
   (`Criterion`, `CasselsTate`, `CasselsTateSquare`, `Finite`, `Witness`), plus two logs. Nothing was removed.
3. **TypeIntegrity: 23/23.** Each target is declared exactly once, as `theorem <name> : Spec.<Name> :=`, and exactly one
   declaration carries each target name.
4. **Red-flag scan, comments stripped.** None of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`,
   `extern`, `opaque`, `ofReduceBool` or `skipKernelTC` appear; there is no macro, syntax, elab, notation, `run_cmd`,
   `#eval`, `addDecl`, `open Lean` or attribute.
5. **Independent compile.** Lean v4.28.0 against the pinned prebuilt Mathlib `8f9d9cff` (read-only, via `LEAN_PATH`),
   modules in import order. Every module gives rc = 0 and zero diagnostics.
6. **Axioms.** All 23 targets report a subset of `[propext, Classical.choice, Quot.sound]` (`axioms_fresh.log`).
7. **Level** (the original `level.py`): `A5_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, `STRETCH_CLEAN: ['casselsTate_square']`.

## What this establishes

**Machine-checked.** Every Iwasawa-theoretic input is an explicit hypothesis (`ThreeInputs`, in the governing order of
inference), and the certified symbol tables are sha-bound data. Given those:
- the chain from the certified depth-four coefficient `a_{4,2} = 15480` to `Sha(E/ℚ)[3^∞]` finite of order 9 and
  isomorphic to `(ℤ/3)²`;
- all finite certificate arithmetic at `p = 3`;
- the Cassels–Tate step, and its general square-order form.

**Not established.**
- The imported theorems themselves: Skinner Thm A, with its recorded SU provenance limit; the control argument; the
  height certificate; Jones Thm 3.1; SW Prop. 3.5.
- The numerical symbol certificate.
- Anything at other primes, or FIN.

**Notes.**
- This is one proof run, with no Aristotle run. A second, independent proving run can still be made by submitting the
  frozen v2 archive to Aristotle.
- `lake build` was not used; the direct `lean` recipe compiles the same sources against the same pinned Mathlib.
