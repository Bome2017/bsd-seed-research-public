# Read-only source and coordinate review

Reviewer: joint-control worker. Date: 2026-10-15. This is an audit of the saved source interfaces plus independent finite arithmetic, not a rerun of all number-field certificates or a new descent.

## Bound inputs

Every file in INPUT_BINDINGS.json was compared byte-for-byte with its recorded original, and its SHA-256 matched. The complete-source matrices are:

- `/Users/bsm/BSD_JOINT_REPAIR_TARGET_EXPERIMENT_2026-10-15/arithmetic/1913b1/matrices.json`;
- `/Users/bsm/BSD_JOINT_ADMISSION_AND_METHOD_DISTILLATION_2026-10-13/controls/389a1/matrices.json`;
- the same control root's `433a1/matrices.json`.

The 1913 signature run reads G=D[6] from a literal identical copy of the original data.gp (SHA-256 bdbac56d60e62907a577cee78d3e0a6c563f20bf41b3aab68bce8c9e39e6addf). The 389 copy likewise matches (5e0bca36fcb33d1038150080cc13ffef0002a7b456a79453e601b4ce5570bd2a). Every fresh source-residue row has respectively 9 or 10 columns in this unchanged G order. The known-class matrix is used only for a subsequent assertion, not to generate the residue rows, local point annihilators or first-eligible-prime selection. No coordinate mismatch was found.

## Completeness grades

All three fields have signature (2,3), hence global unit rank four; their real embeddings exclude nontrivial odd roots of unity. Their retained BNF records return bnfcertify=1 and class group one. The numbers of S-primes are respectively 5,6,9, so the full S-ramified multiplicative sources modulo cubes have dimensions 9,10,13. The saved residue maps prove independence of the displayed generators in these dimensions. These are complete-source inputs at their retained computer-assisted grades, not extrapolations from a list of known Selmer classes.

1913b1's certificate took 58.4 seconds in the prior run, 389a1's 7.1 seconds and 433a1's 0.84 seconds. None was rerun in this audit. Completeness is not transferred to 28042a1 (certification timeout) or to the seed's historically conditional ambient source.

## Independent rank audit without point columns

A separate standard-library elimination calculation, not importing pilot.py, gives:

| Source | Dimension | Scalar kernel | Scalar + finite-additivity kernel | Scalar + local kernel | All three kernel |
|---|---:|---:|---:|---:|---:|
|1913b1|9|3|2|2|2|
|389a1|10|4|2|2|2|
|433a1|13|6|3|2|2|

These are full-source calculations. The point or known excess lists are unnecessary for constructing these kernels. They enter only afterward to certify actual admission and identify the resulting quotient.

For 1913 and 389, scalar plus finite-additivity equations alone already give a two-dimensional containing space. Those equations are necessary for genuine global cohomology classes, so this upper bound does not require sufficiency of sampled local images. The two recovered directions are known to be actually admitted by separate retained inputs: exact global/local certificates for1913, actual point Kummer identities for389. This permits a full-source upper/lower sandwich without treating finite residue success as a positive admission proof.

433 differs: its global necessary kernel has a third direction. The saved exponent vector is (1,2,0,2,1,2,0,0,1,0,0,0,1). Its local defect is nonzero at both3 and433, and the saved 35- and45-digit row spaces agree. I have not located an independent exact rational Hensel witness certificate for this older433 calculation. Therefore the pilot must retain the original local-computation grade; matrix replay alone does not newly certify that local interface. The source completeness certificate is unaffected by that distinction.

## What is new, and the useful next arithmetic target

Recovering these same two-dimensional kernels after suppressing the supplied true-class lists is a retrospective completeness check and a check of the proof architecture. It is not a new control Selmer result, and withholding files now is not a genuinely blinded historical run.

A new bounded arithmetic target exists at433: compute the actual affine-line norm of the extra exponent vector above, without fitting it to the known points, and authenticate its nonzero local defect using exact rational Hensel witnesses. This would decide whether the full-source residual direction is a genuine global cohomology class rejected locally, or merely a false global class that escaped the six saved split-prime blocks. The literal extra element is already printed in controls/433a1/analyze.out. The dual field and norm machinery can be constructed from the saved certified BNF; no new BNF is needed. The meaningful outcome is an exact description of that residual kernel and its first failed arithmetic gate, not another detection of supplied Sha columns.

A larger version replaces the single false-class norm field with the norm map on a complete scalar-source basis (dimensions3,4,6 here). Exact cube relations would certify the entire global norm kernel; noncube residue witnesses certify its complement. This remains a fixed-coefficient-prime experiment and cannot by itself establish a uniform seed bound.
