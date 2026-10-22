# Source register

## Archives

| file | sha256 | bytes |
|---|---|---:|
| `_external/originals/ARISTOTLE_S_DYADIC_V1.tar.gz` | `2cbc087a8835ce0a32d5ca2de6ea7aab6a848093dbebddbb89a410428df3c839` | 72884 |
| `_external/originals/ARISTOTLE_S_DYADIC_V2.tar.gz.sha256` | `879dff1b3c3feadb24ae705a9b1a528ab15b3cbfd92fff23c1852ab84fb5a172` | 95 |
| `_external/originals/RUN_A_ARISTOTLE_S_DYADIC_V2_COMPLETED.tar.gz` | `90402aeceebf633ada9d94ec101b10356b60ec6ee83ec9359811814158e936c4` | 182028 |
| `_external/originals/RUN_B_86c570b1-aristotle.tar.gz` | `843114347c59d6203955970d7ec0f2963266e58d2eb198345372dad5eadddd8d` | 379850 |
| `_external/originals/RUN_B_ARISTOTLE_S_DYADIC_V2.tar.gz` | `67c56e3b29e0e084c3fe59ed7742647ca276ace7e0d5183d937fe0b4e333c62b` | 190043 |

## The reported Run B hash, recomputed

```text
ARISTOTLE_S_DYADIC_V2.tar.gz
  computed  67c56e3b29e0e084c3fe59ed7742647ca276ace7e0d5183d937fe0b4e333c62b
  expected  67c56e3b29e0e084c3fe59ed7742647ca276ace7e0d5183d937fe0b4e333c62b   MATCH
```

The archive also ships its own `.sha256` sidecar, which agrees.

## Semantic-boundary files — byte-identical across V1, Run A and Run B

```text
4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947  Basic.lean     A==B==True
4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b  Selmer.lean    A==B==True
a866211d79a65fdf030e53f0ed9519ecf86bbc80c1fca2c778d3ba8f2499f2c3  Family.lean    A==B==True
```

## Lean sources

| file | sha256 | lines |
|---|---|---:|
| `01_run_A/tree/RequestProject/Main.lean` | `42bbbac344df474a…` | 5 |
| `01_run_A/tree/RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb062…` | 143 |
| `01_run_A/tree/RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd0…` | 147 |
| `01_run_A/tree/RequestProject/SDyadic/AnswerDefs.lean` | `e48ee71fff1976f7…` | 35 |
| `01_run_A/tree/RequestProject/SDyadic/CharSum.lean` | `86aae7f7ef626989…` | 364 |
| `01_run_A/tree/RequestProject/SDyadic/Count.lean` | `eb99ad26d397c3c2…` | 281 |
| `01_run_A/tree/RequestProject/SDyadic/CountAux.lean` | `2fa94bae034e863b…` | 128 |
| `01_run_A/tree/RequestProject/SDyadic/Family.lean` | `a866211d79a65fdf…` | 111 |
| `01_run_A/tree/RequestProject/SDyadic/FamilyAux.lean` | `5ddc0777a4d189c9…` | 121 |
| `01_run_A/tree/RequestProject/SDyadic/GlobalAux.lean` | `84462d345e0efb00…` | 185 |
| `01_run_A/tree/RequestProject/SDyadic/GlobalDual.lean` | `e08fee910068d737…` | 225 |
| `01_run_A/tree/RequestProject/SDyadic/GlobalPhi.lean` | `7873b9c8c036b9ff…` | 164 |
| `01_run_A/tree/RequestProject/SDyadic/LocalGeneric.lean` | `0eaa9ad161a156fa…` | 228 |
| `01_run_A/tree/RequestProject/SDyadic/LocalOdd.lean` | `218946d5a3f7d5c0…` | 533 |
| `01_run_A/tree/RequestProject/SDyadic/LocalTwo.lean` | `a5d354b2ff475e7a…` | 205 |
| `01_run_A/tree/RequestProject/SDyadic/Main.lean` | `c4beab3bacb4ddeb…` | 172 |
| `01_run_A/tree/RequestProject/SDyadic/PadicBasic.lean` | `77d66be1d48f79c2…` | 374 |
| `01_run_A/tree/RequestProject/SDyadic/RealPlace.lean` | `ef09bd1be7e6b822…` | 201 |
| `01_run_A/tree/RequestProject/SDyadic/ReprArith.lean` | `c9b0595dd8aa2b74…` | 339 |
| `01_run_A/tree/RequestProject/SDyadic/Residue.lean` | `0baefdee9778e4a1…` | 268 |
| `01_run_A/tree/RequestProject/SDyadic/SquareClass.lean` | `7c4ccd882bbc320c…` | 149 |
| `02_run_B/tree/RequestProject/Main.lean` | `42bbbac344df474a…` | 5 |
| `02_run_B/tree/RequestProject/Aux/FiniteField.lean` | `0d7706b32206ddc4…` | 375 |
| `02_run_B/tree/RequestProject/Aux/PadicSquares.lean` | `27b02b9a3c14f31e…` | 491 |
| `02_run_B/tree/RequestProject/Aux/PadicTwo.lean` | `3a20ec953d0c4537…` | 92 |
| `02_run_B/tree/RequestProject/Aux/Quadratic.lean` | `a2a815367905c9a8…` | 42 |
| `02_run_B/tree/RequestProject/Global/Answers.lean` | `4e9637f788364929…` | 335 |
| `02_run_B/tree/RequestProject/Global/Counting.lean` | `5ad9a0aa2cbe60dd…` | 424 |
| `02_run_B/tree/RequestProject/Global/Selmer.lean` | `b3122328baf3dd56…` | 567 |
| `02_run_B/tree/RequestProject/Global/Support.lean` | `7bf580f8dee0b0a3…` | 125 |
| `02_run_B/tree/RequestProject/Local/AtEllPhi.lean` | `97b13a503256d469…` | 292 |
| `02_run_B/tree/RequestProject/Local/AtQEll.lean` | `4d106de42cbe4565…` | 462 |
| `02_run_B/tree/RequestProject/Local/AtReal.lean` | `e469b23bbe429462…` | 165 |
| `02_run_B/tree/RequestProject/Local/AtTwoDual.lean` | `620b6230915c2263…` | 346 |
| `02_run_B/tree/RequestProject/Local/AtTwoPhi.lean` | `85ab568508eda576…` | 274 |
| `02_run_B/tree/RequestProject/Local/GoodPrime.lean` | `e660667193153dea…` | 304 |
| `02_run_B/tree/RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb062…` | 143 |
| `02_run_B/tree/RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd0…` | 147 |
| `02_run_B/tree/RequestProject/SDyadic/Facts.lean` | `fc1db9799f044a51…` | 260 |
| `02_run_B/tree/RequestProject/SDyadic/Family.lean` | `a866211d79a65fdf…` | 111 |
| `02_run_B/tree/RequestProject/SDyadic/Main.lean` | `19e7e30b008d919e…` | 190 |

## Custody

Both runs were copied, never moved.  `S_DYADIC_FORMALIZATION_FREEZE_001` was **not** modified and is
**not** replaced.  No frozen object was altered in assembling this one.

## Excluded

`.lake/`, vendored mathlib packages, `.olean`, build caches; the 62a1 / 66b1 / F-track project trees;
the composition packet and freeze, which are separate objects.

