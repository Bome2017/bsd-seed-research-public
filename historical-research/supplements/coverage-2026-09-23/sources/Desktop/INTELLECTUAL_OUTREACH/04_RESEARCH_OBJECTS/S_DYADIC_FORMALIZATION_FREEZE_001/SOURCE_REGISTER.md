# Source register

## Imported archives, byte-for-byte

| file | origin | sha256 | bytes |
|---|---|---|---:|
| `_external/originals/RUN_A_697d1858-aristotle.tar.gz` | `/Users/bsm/Downloads/697d1858-1614-489a-95af-3c6dc2f8cbe9-aristotle (1).tar.gz` | `018a6a67a893976c48de5ed5383deae679410deb4bd1da4c8eddf62bfe95dae7` | 369889 |
| `_external/originals/ARISTOTLE_S_DYADIC_V1.tar.gz` | `/Users/bsm/Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS/ARISTOTLE_S_DYADIC_V1.tar.gz` | `2cbc087a8835ce0a32d5ca2de6ea7aab6a848093dbebddbb89a410428df3c839` | 72884 |
| `_external/originals/ARISTOTLE_S_DYADIC_V2_COMPLETED.tar.gz` | inner archive of the wrapper | `90402aeceebf633ada9d94ec101b10356b60ec6ee83ec9359811814158e936c4` | 182028 |

All imports byte-identical to their origins.

## The two reported hashes, recomputed

```text
ARISTOTLE_S_DYADIC_V2_COMPLETED.tar.gz  90402aeceebf633ada9d94ec101b10356b60ec6ee83ec9359811814158e936c4  MATCH
MANIFEST_COMPLETED.sha256               58a03dff9cef0a940e9682a08f2f13ac8ba2ebae6c73d88525837237a7548c55  MATCH
```

## Semantic-boundary files — byte-identical through the whole chain

```text
4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947  Basic.lean
4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b  Selmer.lean
a866211d79a65fdf030e53f0ed9519ecf86bbc80c1fca2c778d3ba8f2499f2c3  Family.lean
```

Each is identical to the V1 handoff copy; `Basic.lean` and `Selmer.lean` are additionally identical
to the audited 62a1 development they were vendored from.

## Completed-proof Lean sources

| file | sha256 | lines |
|---|---|---:|
| `RequestProject/Main.lean` | `42bbbac344df474a…` | 5 |
| `RequestProject/SDyadic/AnswerDefs.lean` | `e48ee71fff1976f7…` | 35 |
| `RequestProject/SDyadic/CharSum.lean` | `86aae7f7ef626989…` | 364 |
| `RequestProject/SDyadic/Count.lean` | `eb99ad26d397c3c2…` | 281 |
| `RequestProject/SDyadic/CountAux.lean` | `2fa94bae034e863b…` | 128 |
| `RequestProject/SDyadic/Family.lean` | `a866211d79a65fdf…` | 111 |
| `RequestProject/SDyadic/FamilyAux.lean` | `5ddc0777a4d189c9…` | 121 |
| `RequestProject/SDyadic/GlobalAux.lean` | `84462d345e0efb00…` | 185 |
| `RequestProject/SDyadic/GlobalDual.lean` | `e08fee910068d737…` | 225 |
| `RequestProject/SDyadic/GlobalPhi.lean` | `7873b9c8c036b9ff…` | 164 |
| `RequestProject/SDyadic/LocalGeneric.lean` | `0eaa9ad161a156fa…` | 228 |
| `RequestProject/SDyadic/LocalOdd.lean` | `218946d5a3f7d5c0…` | 533 |
| `RequestProject/SDyadic/LocalTwo.lean` | `a5d354b2ff475e7a…` | 205 |
| `RequestProject/SDyadic/Main.lean` | `c4beab3bacb4ddeb…` | 172 |
| `RequestProject/SDyadic/PadicBasic.lean` | `77d66be1d48f79c2…` | 374 |
| `RequestProject/SDyadic/RealPlace.lean` | `ef09bd1be7e6b822…` | 201 |
| `RequestProject/SDyadic/ReprArith.lean` | `c9b0595dd8aa2b74…` | 339 |
| `RequestProject/SDyadic/Residue.lean` | `0baefdee9778e4a1…` | 268 |
| `RequestProject/SDyadic/SquareClass.lean` | `7c4ccd882bbc320c…` | 149 |
| `RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb062…` | 143 |
| `RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd0…` | 147 |

## Excluded

- `.lake/`, vendored mathlib packages, `.olean`, build caches.
- The 62a1 / 66b1 / two-curve / hostile-review / F-track project trees.
- `STAGE_I_COUNTEREXAMPLE_SEARCH.json` and `exact_local_search.py` — corroborative finite search,
  no proof step depends on them; digests are in the referee receipts.

