# Qualification status

This file is canonical only when supported by the proof ledger, checker
output, and current manifest.  `PASS` means proved or independently replayed
at the level named; generated counts or successful parsing do not establish a
mathematical lemma.

```text
EXACT_CURVE_MODELS             = PASS
ISOGENY_ORIENTATION            = PASS
F_62_INFINITY                  = PASS
PHI_SELMER                     = PROVED
DUAL_PHI_SELMER                = PROVED
FULL_2_SELMER_CONSEQUENCE      = PROVED
SHA_2_INFINITY_TRIVIAL         = PROVED
TAMAGAWA_TABLE                 = PROVED
PERIOD_NORMALIZATION           = PROVED
BSD_AT_2_CHAIN                 = PASS
STRONG_BSD_ASSEMBLY            = PASS
CERTIFICATE                    = PASS
INDEPENDENT_REVIEW             = PASS
ARISTOTLE_ARCHIVE              = NOT_AUTHORIZED
```

Scope qualifiers:

```text
STRONG_BSD_ASSEMBLY_SCOPE      = PUBLIC_PREPRINT_QUALIFIED
CERTIFICATE_SCOPE              = FINITE_REPLAY_PLUS_EXACT_BASE_LATTICE
UNIFORM_THEOREM_MACHINE_PROOF  = NO
PRIVATE_PRIORITY_CAVEAT        = DISCLOSED_UNRESOLVED
FULL_BSD_ATTEMPT               = NO
```

The symbolic theorem is proved conventionally and independently reviewed.
The finite JSON certificate does not promote its hard-coded local predicates
to a uniform machine theorem; `--require-theorem` continues to fail closed.
No gate was upgraded on the strength of a sample-prime computation alone.
