# Fifteenth addendum — M sealed: VERIFIED as a definition/model-resolution theorem; `(D3)_M` OPEN

**Tier: DEFINITION/MODEL-RESOLUTION OBJECT — OPERATOR-VERIFIED.** Seals M exactly as the operator verified it. It
carries the draft `M/M_DRAFT.md` (revision 2, `19c34c16…`) byte for byte, with its generator, checkers and receipts;
the audited revisions 0 and 1 (`history/`); and the operator's three audit texts as received (`audits/`). This object
is the authoritative status of M. **`(D3)_M` remains OPEN.** No new mathematics: the only computation is digest
checks, regeneration of the carried files, and mechanical extraction of the quotations below, each re-checked byte for
byte (`receipts/VERBATIM_VERIFICATION.txt`). Prior objects unmodified and byte-identical (`receipts/PRIOR_OBJECTS.txt`):
`ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`, `3eb98a60…`, `da70ec51…`, `c1a6f8ea…`,
`b7ebbf00…`, `8af7a2a5…`, `afae7941…`, `a2667972…`, `7f7c8a9d…`, `ccc77e3f…`, `0b634bc9…`.

## 1. Three audit rounds

| round | revision audited | verdict (operator) |
|---|---|---|
| audit 1 | 0 — `228f3cf95eec875f…` | **REVISE BEFORE SEAL.** Mathematically sound after local repairs: A, the stack→coarse cusp transfer; B, `M9` as a lattice operator; C, the exact `W₂` of `ADDENDUM_010`; the M2 wording; the `q`-expansion concern cleared by [CNS]. All 26 verbatim blocks verified. |
| re-audit 2 | 1 — `b6c9a2200d551b2e…` | **PASS AFTER ONE LOCAL INSERTION.** A and B pass; insert the `w₂` cusp-action proof and the precise [CNS] locator. Digest confirmed; all 31 verbatim blocks verified. |
| targeted re-audit 3 | 2 — `19c34c16594a6f37…` | **PASS.** Seal-ready as the M definition/model-resolution object. |

The texts are in `audits/`, extracted mechanically from the session transcript; their provenance is in
`receipts/CARRIED_ARTIFACT_CUSTODY.txt`.

## 2. The verified boundary

**M = VERIFIED**, as a definition/model-resolution theorem, at exactly this boundary (operator, re-audit 3):

* `X = X₀(2p)_{ℤ_(2)}`, the coarse Deligne–Rapoport model, is fixed (M1);
* `Ω` is fixed as the relative dualizing sheaf (M2);
* `ω̄_f` and `ω̄_η` are well-defined (M5; M6–M8);
* `(D1)` is resolved on that model (M8);
* `(D2)` is formulated as the reduction of the generic-fibre lattice operator `w₂^*` (M9a–M9c);
* the multiplicity-one input is attached to the same `X`, `Ω` and `𝔪` (M §8);
* the statement `(D3)_M` is well-formed:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 628-632
```text
**Statement M11 — `(D3)_M`.** In `H⁰(X_{F₂}, Ω)`,

    ω̄_η = ω̄_f,

with `X` and `Ω` as in §§1–2, `ω̄_f` as in §4, and `ω̄_η` as in §5 (it lies in `H⁰(X_{F₂}, Ω)` by Lemma M8).
```

**It is still not proved.** M's own line, sealed here, stands:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 644-644
```text
**`(D3)_M` is STATED, NOT PROVED.** M makes no implication to `(C)`.
```

These are the inputs available to a proof, as M reads them on its objects:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 636-642
```text
| hypothesis | statement on `X`, `Ω` | anchor |
|---|---|---|
| `(B)` | Lemma M10 | `ADDENDUM_005` (symbolic) + §4 |
| `(D)` | §8, `dim H⁰(X_{F₂}, Ω)[𝔪] = 1` | Č18 Proposition 2.2(ii) |
| `(D1)` | Lemma M8 | §§2–3 + **[derived]** |
| `(D2)` | Lemma M9b: `overline(w₂^*ω_η) = ω̄_η` | Č16 Lemma 2.7 proof + `ADDENDUM_010` §2 + **[derived]**; `w₂`'s cusp action is Lemma M9c |
| special-fibre description | two components; `w₂` interchanges the two vertical generic stalks — no special-fibre automorphism asserted | Č16 §2.6 and the proof of Lemma 2.7 |
```

## 3. Custody

* **Recomputed independently by the operator:** `M/M_DRAFT.md` has SHA-256
  `19c34c16594a6f378bc1e25e45c942851b86c055b84da06e6e50a680be9cb48d`, and a rerun of
  `M/computation/verify_w2_cusp_action.py` is byte-identical to `M/receipts/W2_CUSP_ACTION.txt`, with every symbolic
  check passing (re-audit 3). Revision 1 was likewise confirmed as `b6c9a220…` (re-audit 2).
* **Re-checked at sealing** (`receipts/REPRODUCTION.txt`). Each of revisions 0, 1 and 2 regenerates byte for byte from
  its own carried generator and the sealed sources, and so do its verbatim receipts. The `w₂` checker reproduces its
  receipt, and `M/receipts/REVISION_1_TO_2.diff` regenerates from `history/revision_1/M_DRAFT.md`.
* **Every carried file** is listed with its digest in `receipts/CARRIED_ARTIFACT_CUSTODY.txt`, against the digest
  recorded when it was delivered for audit.

## 4. Citations and checks confirmed by the operator

* **[CNS]** — confirmed as Česnavičius–Neururer–Saha, *The Manin constant and the modular degree*, JEMS 26 (2024),
  no. 2, 573–637, DOI 10.4171/JEMS/1367. Its introduction states that the formal completion of the coarse `X₀(N)`
  along `∞` is `Spf ℤ[[q]]` and that `X₀(N)^∞` is a `ℤ`-smooth open. M's sealed entry gives the Crossref publication
  date instead of the volume year, and stays as sealed:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 30-36
```text
* **[CNS]** K. Česnavičius, M. Neururer, A. Saha, *The Manin constant and the modular degree*, J. Eur. Math. Soc. 26,
  no. 2, pp. 573–637, doi:10.4171/jems/1367 (Crossref record: published 2023-09-14); arXiv:1911.09446v3 (2 Nov 2022).
  **Locator:** §1 (Introduction), the paragraph right after the display `(⋆)`, beginning "The containment (⋆) is
  straight-forward". It states that at general level `N` the formal completion of the coarse `X₀(N)` along `∞` is
  `Spf ℤ[[q]]`, and that the open `X₀(N)^∞` through `∞` — the complement of the `ℤ`-fibral components missing `∞` — is
  `ℤ`-smooth (used in §4). Located in arXiv's HTML rendering of v3 on 2026-09-13 and paraphrased here, not quoted; the
  journal version was not read.
```

* **The `w₂` representative.** The operator independently checked the normalizer question implicit in calling
  `W₂ = (2, 1; 2p, p+1)` the standard `w₂` representative, and found no remaining operator-typing gap.
* **Still supplied, not read here:** the trivial cusp field at squarefree level, used in M §2, step A1.

## 5. `ADDENDUM_012` §4 — the lemma it waited for

`ADDENDUM_012` made admissibility conditional on a sealed definition/model-resolution lemma:

**Verbatim** — `H41_DEFINITIONS_ERRATA_BOUNDARY_ADDENDUM_012/ADDENDUM.md` lines 369-375
```text
**PROHIBITION.** Until a definition/model-resolution lemma fixes them, none of the following may be used
in any proof of the bridge: the symbol `ω̄_f`; the symbols `Ω` and `ω` as they occur in `(D)`, `(D1)` and
`(D3)`; `X₀(2p)_{F₂}` as an unspecified special fibre. A bridge proof using any of them before that lemma
is sealed is not admissible to the architecture. The lemma must fix, at minimum: the model over `ℤ_(2)`,
and whether statements transfer between it and its resolution; the sheaf, including whether the `Ω` of
`(D)` is the dualizing sheaf; and the normalization and integral structure of `ω_f`, including its link to
`E₀`.
```

M is that lemma. Its own audited table reads:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 658-658
```text
| `ADDENDUM_012` §4 prohibition | this draft is the required lemma | lifts only after audit and seal |
```

M fixes each item §4 names:

| `ADDENDUM_012` §4, at minimum | fixed in M |
|---|---|
| the model over `ℤ_(2)`, and whether statements transfer between it and its resolution | M1 fixes the coarse Deligne–Rapoport model. For `(D)`, Č18's remark that its conditions hold on either model is quoted in M §1. Every other statement of M is made on the Deligne–Rapoport model only. |
| the sheaf, and whether the `Ω` of `(D)` is the dualizing sheaf | M2: `Ω` is the relative dualizing sheaf, which is the `Ω` of Č18 Proposition 2.2(3). |
| the normalization and integral structure of `ω_f`, and its link to `E₀` | M3–M5: `a₁ = 1`, and `ω_f ∈ H⁰(X, Ω)` by Č16 Lemma 2.7. The link to `E₀` is Č18 Theorem 2.13, recorded in M §4 for R, quoted below. |

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 419-420
```text
**Normalization note, for R — not used in M.** Č18's Theorem 2.13 gives `ord₂(c_π) = 0` for the optimal quotient,
so the `q`-expansion normalization of `ω_f` agrees up to a unit with the pullback of a Néron differential:
```

**Consequence, by `ADDENDUM_012` §4's own terms.** From this seal, `ω̄_f`, `Ω`, `ω` and `X₀(2p)_{F₂}` are admissible
only with the meanings M fixes; in any other sense they remain inadmissible. This object contains no bridge proof and
admits none. Nothing about `(C)` or R follows from it.

## 6. Two readings — not repairs

**(i) M's own status line is historical.** The draft is sealed as audited, so its line still reads:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 3-4
```text
**Status: DEFINITION DRAFT, REVISION 2 — TARGETED RE-AUDIT PENDING, NOT SEALED.** Audit 1 of revision 0 (`228f3cf9…`):
**REVISE BEFORE SEAL**. Re-audit 2 of revision 1 (`b6c9a220…`): **PASS AFTER ONE LOCAL INSERTION**. Both rounds of
```

This object supersedes that line. The draft is unchanged.

**(ii) `ADDENDUM_010` §2(d):**

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 51-53
```text
**(d) The `W₂` cusp action is not assumed — it is forced by the matrix's own rows.** Row 1 is `N/d`
(so `c₁ = [0]`), row 4 is `d` (so `c₄ = [∞]`), and permuting the divisor indices of row 1 gives row 2
exactly, of row 4 gives row 3 exactly. Hence `c₂ = W₂[0]` and `c₃ = W₂[∞]`, which is precisely what (c)
```

"Not assumed" is relative to `ADDENDUM_010`'s convention (a), the index interchange `a ↦ 1−a`; the permuted rows check
that convention against the cusp labels. M's Lemma M9c now derives the cusp action `w₂[0] = [1/2]`, `w₂[∞] = [1/p]`
directly from the representative `(2, 1; 2p, p+1)`, independently of (a). `ADDENDUM_010` is unchanged.

## 7. What is and is not promoted

* **VERIFIED:** M, at the boundary of §2 — definitions and model resolution only.
* **OPEN:** `(D3)_M`.
* **Not promoted:** `(C)`; R, the implication from `(D3)_M` to `(C)`; uniform optimality `E₀ = E`; the H41 seed; the
  positive branch.

## 8. Next — prove `(D3)_M`

The operator's direction: stop refining the architecture. The next job is to **prove `(D3)_M`**. M has put its
prerequisites in place, and it is the next real theorem bottleneck.

## 9. Status ladder

    M sealed          =  M verified      definitions and model resolution
    M verified        ≠  (D3)_M          OPEN — the next theorem
    (D3)_M            ≠  (C)             R
    G verified        ≠  (C)             ADDENDUM_014

**The H41 seed remains unproved.**
