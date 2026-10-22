# Replay

Run `python3 verify_support.py` to independently check eighty unique-prime support witnesses against every saved norm. It writes SUPPORT_VERIFICATION.json and PRIVATE_PIVOT_MATRIX.json; it does not overwrite the final RESULT.json.

To replay GP arithmetic, use isolated empty scratch output directories and the scripts reconstruct.gp, private_pivots.gp, scalar_pivots.gp in that order, with selected.gp/private.gp and the pinned input paths available. These GP scripts append output data; do not rerun them in the sealed artifact directory. The run_bounded.py wrapper gives external wall/RSS limits and retains stdout/stderr. Required completion markers are RECONSTRUCTION_COMPLETE, PRIVATE_PIVOT_COMPLETE=[80,80], and SCALAR_PIVOT_COMPLETE. Exit code alone is insufficient.

Original field/order/scalar provenance is retained; no full BNF is necessary or permitted by this replay. norm_trials.gp binds all14326norms but contains no full element vectors. Actual selected vectors are reconstructed.gp; actual prime ideals are private_pivots.gp.data and scalar_orbits.gp.data.

## Portable bundled replay

All required mathematical inputs are now bundled under inputs/. The two larger GP structures are gzip-compressed. INPUT_BINDINGS.json records both transport and uncompressed hashes. The original run scripts and original absolute paths are preserved as execution evidence.

Run `python3 portable_replay.py --gp /absolute/path/to/gp --output /new/scratch/directory`. The wrapper refuses an existing directory, verifies and unpacks the bundled inputs, substitutes those exact paths in copies of the original scripts, and replays only the selected eighty elements and their private/scalar witnesses. It does not rerun the broad search or a BNF. Each arithmetic process has a120-second external timeout and a1GB PARI maximum stack, with its internal alarm retained. The replay wrapper is provided for reproducibility; this worker did not rerun the arithmetic through it. Any independent review is recorded separately by the parent.
