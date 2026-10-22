# Bounded replay

Run from this folder.

1. `python3 checks/exact_control.py` verifies the rational isogeny identity, point-image matrix, finite-field 5-saturation certificates and leading-unit arithmetic using only the standard library.
2. `python3 checks/check_saved_digits.py` recomputes the valuation difference and corrected quotient from saved numerator/regulator digits, without trusting the printed quotient.
3. With PARI/GP 2.17.3, `gp -fq -s 128M checks/candidate43737_exact.gp` repeats the rank/local/isogeny computation. Read errors and require DONE. The last exact Python checker supplies an independent check of the point algebra, not a separate rank-descent implementation.
4. `gp -fq -s 128M checks/candidate43737_geometry.gp` repeats the logarithm/height geometry.
5. Numerator regeneration: `gp -fq -s 4000M checks/candidate43737_replay.gp`. The valid observed run took about ten seconds for the numerator and used a fixed 4 GB stack allowance. It writes the small moments object for reuse. Do not use a memory-failed output even if GP exits zero.

The initial n8/256MB and n6/1400MB attempts are invalid and retained. The two accepted n5 outputs agree on NUMERATOR, VALUES, VALUATIONS and PRECISION; wall time is intentionally not byte-identical.

The discovery screens are included for provenance and are not prerequisites for replaying the final control. The source downloads have separate hash bindings and are not required for the standard-library checks.
