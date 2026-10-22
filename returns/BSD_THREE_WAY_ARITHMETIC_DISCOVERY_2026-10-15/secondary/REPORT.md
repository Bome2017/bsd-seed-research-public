# Secondary arithmetic screen and exact countercontrol

Date: 2026-10-15. Status: `NORM_ROOT_INTEGRALITY_EXCLUDED_AS_SECONDARY_DISCRIMINATOR`; `NINE_LIFT_REPAIR_OBJECT_SPECIFIED_NOT_COMPUTED`.

The tested cheap candidate does **not** separate a known rational-point class from genuine excess. This is an exact test on actual field elements. It is not a new Selmer bound, a Cassels–Tate evaluation, or a nine-descent computation.

## What was calculated

The sealed question was whether requiring an integral (or unit) cube root of the affine incidence norm adds useful information after first-descent admission. The inputs are the literal degree-eight representatives from the preceding exact arithmetic, copied and hash-bound in `INPUTS.json`. Their labels come from that arithmetic and its independent rank/source checks, not from analytic Sha predictions.

| Curve / actual representative | Input a unit and not a cube | Affine norm a cube | Its cube root a unit |
|---|---:|---:|---:|
| 718b1, false antiunit | yes | no | not applicable |
| 718b1, unit equal to the class of P₂ | yes | yes | yes |
| 1913b1, excess unit 1 | yes | yes | yes |
| 1913b1, excess unit 2 | yes | yes | yes |
| 28042a1, excess unit 1 | yes | yes | yes |
| 28042a1, excess unit 2 | yes | yes | yes |

The producer reconstructs the incidence embedding from the curve and its specified torsion point, computes each norm by a resultant, and finds exact roots. It also verifies the literal cube identity binding the 718 point unit to the tangent evaluation of P₂. The second checker computes the norms instead as determinants of multiplication matrices. It verifies the roots and their unit ideals. The strict runner uses a temporary directory, verifies all six input hashes, rejects all stderr and nonzero exit codes, and checks the completion markers and generated-certificate bytes. GP's successful exit code alone is never accepted.

The original run took 285 ms of reported GP CPU time. The isolated replay passed. `ROOT_CERTIFICATES.gp` records every element, field, embedding, norm and root; `REPLAY_RECEIPT.json` records the executions. No class-group computation was rerun.

## Why this cheap candidate had to fail

Let α be a global algebraic unit in the torsion algebra. Its image in the incidence algebra is a unit. Its incidence norm N(α) is therefore a unit in the affine-line algebra. If s³=N(α), then for every finite valuation,

    3 v(s) = v(N(α)) = 0.

Hence s is automatically a unit. Requiring an integral or unit norm root adds no condition for these unit-source classes. The false antiunit is rejected by the existing first-descent norm condition itself. All genuine excess examples survive that condition and its proposed integrality refinement, just as the point example does.

A second sealed exact control also checks representative dependence. Replacing each genuine α by α/2³ leaves its Kummer class unchanged. The incidence extension has degree three, so its norm changes by 2⁻⁹ and the root changes from s to s/8. All five resulting roots have denominator exactly 8 in the target field's integral basis. Therefore root integrality is not even invariant under arbitrary cube rescaling of a source representative. Fixing a unit representative repairs that presentation issue, but then integrality is automatic and still does not separate point from excess.

`SCALING_TEST_SEAL.json`, `check_scaling.gp` and its saved output record the five additional actual controls. The strict replay includes them. This excludes this precise candidate, not all coherence conditions on a second descent.

## What genuinely new data the secondary operation needs

`SECONDARY_REPAIR_DEFECT.md` derives the next object from the exact sequence E[3] → E[9] → E[3]. It compares a **single global 9-lift** with local Kummer lifts, modulo adjustments supplied by one global class. First-descent norm roots do not supply that lift or its defects.

There are two established implementations of the underlying mathematics to distinguish:

* A Cassels–Tate computation needs normalized rational functions on a covering curve and local evaluations of those functions. Current source elements are not those functions.
* A second 3-descent needs an explicit plane-cubic covering. The current 1913b1/28042a1 packets supply exact source elements but no such cubic model. The documented Magma operations are `ThreeDescentCubic` and `NineSelmerSet`; no local Magma executable was available here, and no external job was launched.

The old seed B3 stop was reviewed before this screen. Its missing operation was an explicit global matrix-algebra splitting used to construct the normalized function, not a missing local residue calculation. Its seed-sized budget failure does not prove failure for the small control fields. Conversely, the smaller field discriminant does not certify that the missing conversion is cheap.

## What a secondary answer would and would not establish

A point class has a locally soluble 9-lift. A genuine excess class may or may not: a positive result can also mean that the excess is 3-divisible. Thus zero defect is not a rational-point certificate. A nonzero defect detects genuine excess and obstructs 9-lifting; it does not make Sha vanish. On a complete Selmer space, a nondegenerate pairing on the known excess can exclude higher 3-divisibility, which is a fixed-primary conclusion.

This gives an executable next arithmetic operation with exact input obligations in `NEXT_OPERATION.md`, not a new uniform mechanism. FIN, ORDER9 and Q36 are unchanged. No seed coefficient-prime was settled in this screen.
