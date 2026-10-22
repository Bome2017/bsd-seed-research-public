# Replay boundary

Three new submitted Lean files were compiled from their exact delivered bytes,
with Lean 4.28.0 and the dependency revisions in the submitted lake-manifest.
The build reused the existing pinned Mathlib/package compiled libraries. It
was not a fresh compilation of all Mathlib.

`checks/LEAN_BUILD.json` records three successful exits. The independent
`replay/Audit.lean` imports those compiled modules and prints the dependencies
of all 18 theorem declarations. Every declaration has at most propext,
Classical.choice and Quot.sound; the four EtaCheck evaluations use no axioms.
No sorry or native_decide occurs in the three new source files.

The older four BFR modules were reviewed and compiled in the previous return;
they were not rebuilt this time. The supplied old build and axiom receipts
remain historical, not substitutes for the fresh new-module receipts.

The eta Boolean functions implement finite arithmetic. Their formal statements
do not themselves establish the Galois-cohomological local identification.
The independent torus checker verifies the needed six group values by a
separate formula. The written proof connects them to the Kummer conditions.

Portable small arithmetic check:

    python3 checks/independent_torus.py

It regenerates ETA_INDEPENDENT_TORUS.json. The received eta script is preserved
under input/research_return/checks/ and its replay stdout is in checks/.

For Lean, use the provided lake-manifest and lean-toolchain to obtain pinned
dependencies, compile RequestProject/Seed/NoLift, Exceptional and EtaCheck,
then run replay/Audit.lean. Absolute cached paths in the review receipt record
the local environment; they are not portable project requirements.
