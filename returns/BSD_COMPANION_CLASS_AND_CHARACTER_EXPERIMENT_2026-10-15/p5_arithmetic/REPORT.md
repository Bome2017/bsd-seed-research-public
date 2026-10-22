# Actual coefficient-five whole-source bound experiment

Completed 2026-10-17 from the sealed 2026-10-15 computation. Status: **CONDITIONAL_ARITHMETIC_UPPER_BOUNDS_OBTAINED; CLASS_CERTIFICATION_TIMED_OUT**.

This is an actual p=5 extension test on 389a1 (rank two) and 37a1 (rank one). It constructs their degree-24 nonzero-torsion-point fields, exact scalar automorphisms and primitive prime-divisor actions. It does not merely enumerate known Selmer classes. The resulting bound covers the entire scalar-compatible global source, including any unlisted class-supported elements, **conditional on the GRH-dependent class-group computation**.

| Control | Actual field degree; signature | Provisional ordinary class group | Faithful source divisor dimensions | Whole global norm-kernel upper bound |
|---|---|---|---|---|
| 389a1 at 5 | 24; (4,10) | C3 | 0 above 5; 1 above 389 | 3, conditional on class-5 absence |
| 37a1 at 5 | 24; (4,10) | C2 | 0 above 5 and 37 | 3, conditional on class-5 absence |

For 389, the ramification-weighted primitive divisor norm on the remaining character line is a unit, so it contributes no valuation-kernel dimension. For 37, the source character divisor module is already zero. The ordinary unit character rank is three in each field. Therefore class-5 absence bounds the entire admitted source by three, without using a known Selmer/Sha value. The detailed proof is in `BOUND.md` and the parent's `general_character/PROOF.md` and `LOCAL_DIVISOR_PROOF.md`.

## Certification outcomes, including failed work

- **389:** BNF initialization returned C3 in about 3.5 seconds. Full certification was stopped at 63.10 seconds after warning of a large Zimmert bound. The separately sealed quotient-only repair ran another 54.04 seconds and hit its GP alarm. Total construction and these stages remained within the sealed 120-second field budget. Neither produced a certification marker.
- **37:** BNF initialization returned C2 in 390 milliseconds. Quotient-only `bnfcertify(B,1)` then hit its alarm after 116.840 seconds; total stage wall time was 117.052 seconds. The GP process exited zero despite the alarm, so the exit status is explicitly rejected as evidence of certification.

PARI documents `bnfcertify(B,1)` as proving that the true class group is a quotient of the computed one. That would suffice here because both candidate class orders are prime to five. It did not complete. The public function documentation supplies no coefficient-prime-only certification switch. No such undocumented shortcut is claimed, and no further field search or extension of the sealed computation caps was made.

The exact field/point/scalar and ideal-permutation checks do pass independently of the BNF class computations. `replay.py` reruns those cheap checks and checks the saved completion/error markers without retrying BNF or certification. It will not upgrade either class result.

## What this says about the experiment

The larger-prime construction is executable on actual fields, and the primitive divisor correction removes the apparent ramified-place factor five for 389. The outcome is a **conditional numerical upper bound on the whole global source**, not a stronger detector. It is not yet an unconditional p=5 certificate, a bound for the seed at p=5, or evidence for an all-prime bound. The elementary unit-rank constant becomes (p+1)/2, so this particular upper-bound mechanism does not stay at three as p increases.

No claim of parity, rank equality, primary vanishing, FIN, ORDER9 or Q36 follows from this return. No known control Selmer dimension was used to manufacture the class or upper-bound outputs.

Sources: retained scalar-descent interpretation from Schaefer–Stoll, as mapped in the parent's character proof; Tate multiplicative inertia; Dirichlet unit theorem. Freshly checked PARI documentation: https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify and the same page's class group/GRH warning. This is a written deduction with exact computer-algebra checks; it is not a formal proof-assistant certificate.
