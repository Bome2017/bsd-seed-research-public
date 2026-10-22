# Source register

## Imported archives, byte-for-byte

| file | origin | sha256 | bytes |
|---|---|---|---:|
| `_external/originals/RUN_A_67b663c6-aristotle.tar.gz` | `/Users/bsm/Downloads/67b663c6-7fe9-43d4-8b29-aa93ceda3ffa-aristotle.tar.gz` | `65ba91b7334f2dab140ce867f58d4090adc645762e1e627c3724d7f372261bd6` | 68703 |
| `_external/originals/RUN_B_a634ecf8-aristotle.tar.gz` | `/Users/bsm/Downloads/a634ecf8-bcb5-4c2b-9d31-c99489aa5bf6-aristotle.tar.gz` | `8fd189f8a92b94d26f391bb02c349bcd829fd27901c081779e5a60e57045a932` | 51620 |
| `_external/originals/ARISTOTLE_ORDER4_FINITE_FIELD_V1.tar.gz` | `/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/ARISTOTLE_ORDER4_FINITE_FIELD_V1.tar.gz` | `40d4b1e0bc3a7b1898fede186df810999b1b274e91fbc8a9f8252415d4ea66ae` | 13695 |

All 3 archives byte-identical to their origins.

## Run identity, verified against the reported receipts

```text
RUN_A internal V2 = 8b565a3e6ac9f62ec77ea46281e6cf97d0e1c7aea424c3afe4c6a76a3076e3a0   MATCH
RUN_B internal V2 = f031b93a7d4c963e1b6f36830716643d0374b89e04fdd3b018cca2c717b6ac6d   MATCH
```

Each wrapper contains an `ARISTOTLE_ORDER4_FINITE_FIELD_V2.tar.gz`; those two digests were
recomputed here and match the reported values exactly, tying the receipts to these artefacts.

## Lean sources

| file | sha256 | lines |
|---|---|---:|
| `01_primary_proof_B/RequestProject/Curve.lean` | `42ccc6238f25746a…` | 52 |
| `01_primary_proof_B/RequestProject/CurveBasic.lean` | `2caedfc85b6692df…` | 122 |
| `01_primary_proof_B/RequestProject/CurveGroup.lean` | `c5c4243493080edf…` | 141 |
| `01_primary_proof_B/RequestProject/CurveHalving.lean` | `e3ed5d4e8949d751…` | 154 |
| `01_primary_proof_B/RequestProject/CurveTorsion.lean` | `f9125205be6bf6cc…` | 80 |
| `01_primary_proof_B/RequestProject/FieldFacts.lean` | `9292af4d677c3a5c…` | 33 |
| `01_primary_proof_B/RequestProject/GroupFacts.lean` | `23e4e27a0a96a933…` | 244 |
| `01_primary_proof_B/RequestProject/Main.lean` | `df08a18ea407b714…` | 64 |
| `01_primary_proof_B/RequestProject/Verify.lean` | `6cce233dff909657…` | 7 |
| `02_alternate_proof_A/RequestProject/CurveBasic.lean` | `b72a8ec4566e462b…` | 124 |
| `02_alternate_proof_A/RequestProject/CurveHalving.lean` | `498d5e938f5bfdf2…` | 113 |
| `02_alternate_proof_A/RequestProject/CurveTorsion.lean` | `fd065d1fc83b7ba1…` | 194 |
| `02_alternate_proof_A/RequestProject/FieldLemmas.lean` | `96f72b53a856aeec…` | 32 |
| `02_alternate_proof_A/RequestProject/GroupLemmas.lean` | `e39c9d643eb3251e…` | 175 |
| `02_alternate_proof_A/RequestProject/Main.lean` | `abe06fcd6ab652c4…` | 151 |
| `00_v1_handoff/RequestProject/Main.lean` | `bfd5c4f0b64fb351…` | 50 |

## Excluded

- `.lake/`, vendored mathlib packages, `.olean` files, build caches.
- The 62a1 / 66b1 / two-curve / hostile-review / S-track project trees.
- The `S_dyadic` handoff, which is a separate object.

