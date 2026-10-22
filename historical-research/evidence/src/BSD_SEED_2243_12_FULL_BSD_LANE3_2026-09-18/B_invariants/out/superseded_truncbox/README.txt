Superseded outputs (AUDIT_B correction #1, 2026-09-18). These were produced with scripts/superseded_truncbox/s04b_enum_lib.gp,
whose enumpts() called hyperellratpoints(Q,[Mmax,min(emax,Mmax)]) and so truncated the denominator range e <= Mmax for the
8 quartics with |s| > 7579 (s = +-2A, +-2B, +-AB, +-2AB). They are kept for provenance only and support no claim.
The current outputs in out/ were regenerated with the corrected library (hyperellratpoints(Q,[Mmax,emax])).
