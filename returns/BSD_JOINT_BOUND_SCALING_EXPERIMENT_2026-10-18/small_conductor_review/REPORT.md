# Actual unit authentication at coefficient7 on11a1

All26 supplied compact unit candidates are authenticated as global units independently of GRH. This removes unitness as a qualification when they are evaluated by the separate character/incidence computation. It does not prove the complete ordinary class group trivial.

The new arithmetic input is the11a1 model [0,-1,1,-10,-20], at coefficient7. Its degree48 point field, maximal order and scalar3 action are retained from the parent's exact construction. I read and hashed the newly saved BNF and compact expressions; I did not use rankzero or any Sha information.

The compact expressions involve144 distinct field factors. Exact factorization and complete principal-ideal reconstruction give116 finite prime-ideal coordinates. Keeping every original integer exponent, their116-by144 divisor matrix multiplied by the144-by26 exponent matrix is exactly zero. Thus each product has zero valuation at every finite prime, so it and its inverse lie in the maximal order: each is an actual ordinary unit. Negative exponents and fractional factors are retained; no residue reduction is used in this proof.

`authenticate_units.gp` completed with the required marker after59.07 wallseconds. The field/maximal-order certificate is an antecedent input, not reproved here. A separate standard-library Python calculation checks all3016 integer divisor equations exactly from the exported matrices. No fundamental-unit completeness or independence claim is needed for this authentication. If the separate residue calculation achieves character rank4, the theoretical character dimension4 supplies completeness of that particular mod7 unit component; it does not certify the ordinary class group.

## Class qualification remains

A separate quotient-only `bnfcertify(B,1)` attempt was made on this NEW field, with a58-second internal alarm and60-second wall cap. It printed Zimmert bound1593360910660456325376 and hit its alarm at57.911 seconds. Its GP exitcode was0 but the required certificate marker and certificate file were absent. Consequently the provisional class group1 is NOT upgraded. There was no retry.

The whole-source bound must therefore continue to retain the unknown ordinary faithful7-class contribution (or a genuinely independently proved containing class bound). The conditional variant may explicitly assume completeness of the provisional class presentation. An S-class calculation would not silently remove ordinary virtual-unit class lifts.

This is an actual coefficient7 arithmetic source authentication on a smaller-conductor control, not a new seed or rank-two result. No known Selmer dimension enters either computation. FIN, ORDER9 and Q36 are unchanged.

Files: compact source and BNF are hash-bound in INPUT_BINDINGS.json. AUTHENTICATION_DATA.gp retains exact factors, prime ideals, divisors and exponents. UNIT_DIVISOR_MATRIX.json supports the cheap Python replay. The two process receipts preserve completion/error distinctions.

The evaluator source was also rebound exactly: check_evaluator_binding.py compares all26 exported compact expressions with the local evaluator's864-by26 exponent matrix on144 atoms and six scalar positions. Every integer exponent matches, and the field polynomial, universal point and scalar map are identical. The evaluator therefore consumes the authenticated units, with no unrecorded normalization or source replacement.
