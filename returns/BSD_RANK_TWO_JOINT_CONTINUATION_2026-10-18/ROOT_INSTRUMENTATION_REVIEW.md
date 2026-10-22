# Independent review of the partial PARI candidate export

Date: 2026-10-18
Verdict: PASS_CANDIDATE_EXPORT_BOUNDARY. This is a source/build-interface audit, not authentication of the harvested ideals or a class-group certificate.

I compared the packet's original `buch2.c` byte-for-byte with the corresponding member of the supplied PARI2.17.3 source archive. The archive matches its recorded SHA-256. I reconstructed the complete modified file from three intended changes and obtained an exact match: rename `Buchall_param` to the isolated symbol; print the exact polynomial representative just before `add_rel`; append the uniquely named one-argument wrapper. No other source edits are present.

The wrapper's C arguments match the installed declaration `GEN Buchall_param(GEN,double,double,long,long,long)`. It passes the existing NF object, two doubles, and the three expected integer parameters; `nf_FORCE` is the same flag used by the original algebraic BNF path. The GP install declaration uses one GEN argument and a GEN result. Source headers and dynamically linked PARI library are all version2.17.3, and both GP and the added library are x86_64. The built library and modified C file match their recorded hashes. The smoke run demonstrates that the renamed entry is reached and emits the expected candidate markers. These checks address the actual interface rather than assuming that a private ABI is portable across versions.

At the export site, `gx` is an exact integral-basis vector. The search chooses it using numerical geometry, then forms it by exact integer matrix multiplication and, if necessary, exact content division. `lift(basistoalg(nf,gx))` converts that vector to an exact rational polynomial in the current NF generator. Because the input is already an NF object, the reviewed path preserves its defining polynomial while permitting numerical-precision updates. The print occurs before the rank filter can reject the candidate. Numerical search decisions affect which candidates are found; they need not be trusted for the arithmetic identity of the exported candidate.

The correct acceptance boundary is unchanged:

1. Parse only complete nonzero polynomial records in the bound field; reject interrupted or malformed output.
2. In an unmodified GP process, reconstruct each element and authenticate its FULL principal ideal, retaining every prime divisor.
3. Compute and verify the exact integer divisor matrix and every proposed integral kernel relation.
4. Only products whose full divisors vanish are admitted as global units. Their arithmetic residue rows may then lower-bound the image rank on the full unit space. No generator/basis or class-completeness claim follows from how they were found.

This is valid even if the modified BNF run is interrupted, uses heuristic/GRH bounds, or finds no complete BNF object. Conversely, a printed BNF summary or zero process exit is not a class certificate. No internal relation-vector, regulator estimate, rank assumption, or provisional class group is accepted by this interface audit.

The inserted output changes timing and search resource consumption, so the instrumented run is not claimed to reproduce the original algorithm's trajectory. That does not affect its role as a candidate generator once every accepted algebraic element and relation is independently checked.

The fixed inputs and build are bound in ROOT_INSTRUMENTATION_REVIEW.json. The harvest output was still being produced at audit time and is intentionally not sealed by this review. I did not rerun the large job, rebuild the library, or authenticate the final harvested collection here. Those are separate producer/verification stages.
