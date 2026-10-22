# Independent parity replay

The sealed folder contains deterministic gzip archives, not their large raw copies. Decode them into an external temporary working directory. Check each compressed SHA-256 and then each decoded SHA-256 against CAPTURE_COMPRESSION.json before parsing. Do not decompress into the sealed packet.

For the original-GP parity check, create a temporary root with two entries:

- `work/`: copy `parity_audit.gp` here and decode `captured_generators.gp.gz` here under `captured_generators.gp`.
- `twist_source`: a read-only reference or symlink to the sealed sibling twist_source directory, so the audit's relative field and scalar-matrix paths resolve.

Run the original GP binary pinned in ARITHMETIC_BINDINGS.json from the temporary `work/` directory. Expected complete output is `PARITY_AUDIT_DONE=[1424, 0, 0]`. This is an exact polynomial/basis calculation; it does not load either patched library.

The raw stderr can separately be decoded and checked to reproduce the count of complete `BSD_RELGEN=` lines. The capture stopped by an explicit external signal after enough candidate rows were obtained; EARLY_STOP.json and harvest.gp.receipt.json preserve that boundary. Its incomplete BNF is not an arithmetic class certificate.

The mixed pass exported no candidates. Its filter-trial count is replayable from mixed_harvest.gp.err, but those rejects have not each been factored independently. Do not reinterpret the count as a theorem that all those elements are nonsmooth.
