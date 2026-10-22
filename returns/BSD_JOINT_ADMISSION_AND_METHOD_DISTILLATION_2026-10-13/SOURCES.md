# Sources, dependencies and replay scope

## Project evidence

- `coverage/INPUT_BINDINGS.json`:43 hashed report/text inputs; `coverage/coverage.json` records every prime-level conclusion and dependence. This record includes proof grades and invalid or superseded runs.
- `synthesis/INPUT_BINDINGS.json`:47 copied and hashed raw inputs. `synthesis/SOURCES.md` identifies their original paths and roles. Actual quadratic moments are recomputed from the copied symbol tables; original rigorous recovery of those tables is retained.
- `controls/INPUT_BINDINGS.json`: copied descent libraries, model sources and resource bounds. Complete fresh torsion-field arithmetic is in each control directory.
- Prior sealed return `BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13`: `PROOF.md`, `REPORT.md`, `reviewer/INCIDENCE_NORM_REVIEW.md` supply the retained exact norm composition and unit-lattice deduction. The previous seed four-class filtration is a structural span statement independent of full class-group completeness. Do not promote the old cached source into a certified complete source.
- Current lab start: branch `research/state-sync-2026-10-04`, commit `628d802771ec80bd6f74121dcd4c7f7c496f0da4`. The current-state navigation and relevant historical reports were read. This was not a whole-repository mathematical audit.

## Primary sources consulted this turn

1. Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, long version: https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf . Relevant interfaces: Proposition4.6 (finite ramification/local set), Corollary7.9 and Proposition7.10 (scalar and incidence admission), Proposition7.11 (all-place local admission). The latter requires all places, not a selection of finite residue tests. Finite extra additivity rows in this packet are treated only as necessary equations.
2. PARI/GP official elliptic-curve documentation: https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html , `ellpadicregulator` and `ellpadics2`. Used for the canonical ordinary height convention and unit-root splitting. The computation does not take a Sha value as input.

The Ota, Kato, main-conjecture, original image/basis, local-factor and interval-certification chains remain their retained project inputs. They were not all re-proved or independently re-audited this turn.

## Execution and portability

`python3 checks/verify_package.py` verifies the sealed manifest and replays portable exact downstream checks in a temporary copy. It consumes the saved arithmetic producer outputs; it does not regenerate the underlying modular symbols or BNF computations.

To reconstruct all three control sources afresh, run

    python3 controls/replay.py --gp /path/to/gp

This builds in temporary directories and uses the included libraries. The accepted run uses PARI2.17.3,90-second per-script alarms and approximately1GB maximum stacks. GP input is supplied through stdin; return code alone is not accepted because GP can print an error and still exit zero. Markers and stderr are checked. `controls/REPLAY.json` records the fresh reconstruction already performed. Local image rows were checked again at higher precision and a different random seed.

For fresh point regulators, see the four GP scripts in `synthesis/checks/`; use the flags in `synthesis/RESULT.md`. These scripts need PARI, not the raw Fourier corpus. Higher precision in a regulator does not increase the saved numerator precision.

`coverage/build_coverage.py` is a host-bound audit of the named original paths, not a portable rebuild of the historical certificate engines. Its results and hashes are supplied. This limitation is distinct from the portable exact coefficient and matrix checks.

No hash check is represented as reading or proof. No global endpoint is inferred from a finite control panel.
