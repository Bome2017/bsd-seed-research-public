# Evidence layout and replay

The complete new-run archive expands into `BSD_SEED_P83_CERTIFICATE_2026-10-13/`. Its `MANIFEST.sha256` binds every included file except the manifest itself. The smaller browseable GitHub folder is an explicitly identified subset; its `MANIFEST.sha256` binds that subset separately. The published custody receipt binds the full ZIP and records the subset/full-archive distinction.

## Portable checks from the full archive

From the extracted archive root, using Python 3 without third-party packages:

```sh
python3 verify_bundle.py
python3 independent_verifier.py production/p83_l167/msl.txt --p 83 --ell 167 --generator 5 --denominator 1024
python3 verify_units.py production/p83_l167/units FROZEN_RUN_PACKAGE_p83_l167/corpus/PREFIX_3420_CUSTODY.json --out /tmp/bsd_p83_unit_replay.json
python3 selection/check_p83.py
```

The interval checker recomputes all 166 lattice values and both primitive-root projections. Its resolved `input_path` will change after relocation; mathematical fields and `msl_sha256` should agree with `INDEPENDENT_P83.json`. The unit checker checks the saved units rather than recomputing their Arb sums. Do not run Python with `-O`, which disables its assertions.

`verify_bundle.py` performs only byte-custody verification. A passing manifest is not proof of arithmetic correctness. Historical preflight and source-gate files retain their original pre-run statuses; the final result is in `REPORT.md`, `FINAL_MATHEMATICAL_REVIEW.md` and the completed output JSON files.

## Full numerical regeneration has an external dependency

The raw 3,420-segment Fourier-coefficient prefix is **not inside this archive**. Its original host path is

`/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/corpus_ext_6445/view/ap`.

Its size is 9,673,187,648 bytes and pinned receipt root is

`53de8838b356300dbb7aed6cfc57cab3498c82bd585954fd244095e338f997da`.

The included `FROZEN_RUN_PACKAGE_p83_l167/corpus/` contains receipts and hashes, not substitutes for those raw bytes. Pre- and post-run checks authenticated the actual local bytes. Their original arithmetic certification is retained, not freshly regenerated independently.

The archive contains the actual executable and source, the frozen command and run configuration. The binary is a macOS build with FLINT/MPFR/GMP dependencies; the source/runtime review records their observed loaded identities. A portable rebuild is a distinct operation and is not claimed completed by these replay instructions. Historical absolute paths in manifests, logs and receipts are preserved for custody. The saved launch script must not be run accidentally or into the completed output directory.

The unchanged frozen checker was replayed on the original host. Its invocation and before/after hashes are recorded in `selection/POSTRUN_CUSTODY.json`. Its `production_launched:false` field belongs to the verification helper and means that helper did not launch a new production run; the completed production is recorded separately.

## Scope

The independent output parser, work-unit audit and frozen checker share the same produced interval table or work units. They are separate checks, not independent complete modular-symbol implementations. This archive supports review and output/custody replay while explicitly retaining the missing raw-corpus and antecedent-proof dependencies.

No follow-up prime, paid resource, main merge or expert-repository promotion is part of this return.
