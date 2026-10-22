# A4 return replay — custodian verdict: FROZEN, A4_FULL (both returns), 2026-09-24

| return | archive sha256 | new proof files |
|---|---|---|
| R1 | `14bef1c1-…-aristotle.tar.gz` → `1eaa2f8e8021fe4568b4adef209b202822ecbeb55a9fef649a3d8cb965f5be12` | Criterion, Gauss, Full, Folded |
| R2 | `b2b41135-…-aristotle.tar.gz` → `cece61f459ed9f69096440f8f119b7a2f809316d4a09b170ca79b28a533a5173` | Criterion, Stretch, Full, Folded |

Both archives have 39 entries and no absolute or `..` paths. Each was replayed from a fresh unpack in this folder.

## Checks (identical outcome for R1 and R2)

1. **Frozen files.** `Defs.lean`, `Spec.lean`, `Acceptance.lean`, `lakefile.toml`, `lean-toolchain` and
   `scripts/level.py` match the ORIGINAL shipped hashes (6/6). The returned `FROZEN.sha256` and `lake-manifest.json`
   are byte-identical to the shipped ones.
2. **Changed files.** Only `Targets.lean`, `STATE.json` and `RESUME.md` changed. The added files are the proof files,
   `ARISTOTLE_SUMMARY.md`, `README.md`, `build.log` and `axioms.log`.
3. **TypeIntegrity: 39/39.** Each target is declared exactly once as `theorem <name> : Spec.<Name> :=`.
4. **Red-flag scan.**
   - None of these appear: `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`,
     `ofReduceBool`, `debug.skipKernelTC`.
   - There is no macro, syntax, elab, notation, `run_cmd`, `#eval`, `addDecl`, `open Lean`, instance or attribute.
   - The only token hits are in the Targets header comment.
   - R2 sets `maxRecDepth 100000`, which is harmless.
5. **Independent compile.** Lean `v4.28.0` against Mathlib `8f9d9cff…`, using the custodian's read-only prebuilt oleans
   with the identical manifest pins. Every module compiles with rc=0 and zero diagnostics.
6. **Axioms.** All 39 targets report `[propext, Classical.choice, Quot.sound]`.
7. **Level** (the original `level.py`): `A4_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, and
   `STRETCH_CLEAN: ['foldedFormula_general', 'localGaussSumEichler']`.

The two returns are independent formal proofs, with different file structures and different S2 files. So every target
now has two machine-checked proofs.

## What this establishes

**Machine-checked**, with every Iwasawa-theoretic theorem as an explicit hypothesis (`FixedPrimeInputs`) and the
certified symbol tables as sha-bound data:
- the chain from the certified depth-two coefficients to `Sha(E/ℚ)[p^∞] = 0` at p = 5, 7, 11, 13;
- all finite certificate arithmetic, including the weight tables derived from their definition;
- the α⁻² regression;
- the bridge algebra: squareclass, square valuation, the Néron multipliers, and the local Gauss sum (Eichler case);
- the general folding theorem for every prime p ≥ 5.

**Not established:**
- the imported theorems' own proofs, and their applicability hypotheses beyond the records' checks;
- the numerical certificate of the symbol values (Arb engine and coefficient verifier; no independent end-to-end
  implementation);
- FIN, `#Sha = 9`, any prime ≥ 17, and the bad primes.
