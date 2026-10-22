# Sixteenth addendum — `(D3)_M` PROVED: the operator-audited proof, sealed

**Tier: PROOF — OPERATOR-AUDITED, PASS.** Seals the proof of `(D3)_M` exactly as the operator audited it: `D3/D3_PROOF.md`
(`98782dfb…`), carried byte for byte with its generator, verifier and receipts, and the operator's audit text as
received (`audits/`). **With this seal, `(D3)_M` is PROVED.** Nothing here adds mathematics to the carried proof: the
only computation is digest checks, regeneration of the carried proof, and mechanical extraction of the quotations
below, each re-checked byte for byte (`receipts/VERBATIM_VERIFICATION.txt`). Prior objects unmodified and
byte-identical (`receipts/PRIOR_OBJECTS.txt`): `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`,
`0bfb6b5e…`, `3eb98a60…`, `da70ec51…`, `c1a6f8ea…`, `b7ebbf00…`, `8af7a2a5…`, `afae7941…`, `a2667972…`, `7f7c8a9d…`,
`ccc77e3f…`, `0b634bc9…`, `01b4774f…`.

## 1. The theorem

**Verbatim** — `H41_D3M_PROOF_ADDENDUM_016/D3/D3_PROOF.md` lines 196-196
```text
**Theorem D3 [derived].** `ω̄_η = ω̄_f` in `H⁰(X_{F₂}, Ω)`.
```

It is stated on exactly the objects `ADDENDUM_015` fixed, as M's Statement M11:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/M/M_DRAFT.md` lines 628-632
```text
**Statement M11 — `(D3)_M`.** In `H⁰(X_{F₂}, Ω)`,

    ω̄_η = ω̄_f,

with `X` and `Ω` as in §§1–2, `ω̄_f` as in §4, and `ω̄_η` as in §5 (it lies in `H⁰(X_{F₂}, Ω)` by Lemma M8).
```

**What PROVED rests on.** The operator audited the carried proof independently: the digest was recomputed as
`98782dfbc302a7daf2c36c9bb0c588ac5a085fc999b35ddd0937834fe49cf5a9`, the 20 verbatim blocks were verified, and each of
the five derived steps was checked against the sealed inputs. This is an independently audited ordinary proof, not a
machine-checked one. By the operator's decision, no formal-verification or maximum-effort run is spent on it; those
resources are reserved for R.

## 2. The audit, step by step (operator)

| step | verdict | the operator's basis, in brief |
|---|---|---|
| 1 · zero `q`-expansion ⟹ zero germ at `∞̄` | PASS | M gives `Ô_{X_{F₂},∞̄} ≅ F₂[[q]]` and M10 the zero expansion; the completed stalk of `Ω(cusps)` is free of rank one over it; completion of a noetherian local ring is faithfully flat; localizing the zero germ gives `δ_{ξ₁} = 0` |
| 2 · zero reduction at `ξ₁` ⟹ 2-divisibility upstairs | PASS | `X` is normal, so `O_{X,ξ₁}` is a DVR; the reduced special fibre makes 2 a uniformizer; the cusps miss `ξ₁`, so `Ω(cusps)_{ξ₁} = Ω_{ξ₁}`; hence `δ_{ξ₁} = 0 ⟺ δ̃_{ξ₁} ∈ 2Ω_{ξ₁}` |
| 3 · transport to the second component | PASS | Č16's interchange of the two vertical generic stalks, with involutivity, identifies the two lattices, `(w₂^*δ̃)_{ξ₂} = w₂^*(δ̃_{ξ₁})`; no global integral automorphism of `X` or `X_{F₂}` enters — which is why M9a is a lattice statement |
| 4 · the reduction of `w₂^*δ̃` is `δ` | PASS | M9b for `ω_η`; for the newform `w₂^*ω_f − ω_f = (ε − 1)·ω_f ∈ 2·H⁰(X, Ω)`, since `ε − 1` is 0 or −2 |
| 5 · vanishing at both generic points ⟹ `δ = 0` | PASS | `X_{F₂}` is reduced with exactly two components; after trivializing `Ω(cusps)` locally, the section lies in every minimal prime, hence in the nilradical, which is 0 |

The operator found no missing use of multiplicity one, no illicit special-fibre `w₂`, and no hidden
exceptional-component issue.

## 3. The dependency actually used — smaller than the preregistered envelope

`ADDENDUM_012` §2.2 preregistered a conservative envelope for any use of `(D3)`:

**Verbatim** — `H41_DEFINITIONS_ERRATA_BOUNDARY_ADDENDUM_012/ADDENDUM.md` lines 243-246
```text
**No single canonical hypothesis list for `(D3)` exists in the sealed record.** None is designated
canonical here. Any use of `(D3)` must discharge the union: `(B)`, `(D)`, `(D1)`, `(D2)`, and the
special-fibre description. The objects occurring in `(D3)` — `ω̄_η`, `ω̄_f`, and "global regular
dualizing differentials mod 2" — carry the specification defects frozen in §4.
```

The proof discharges less. Its own accounting:

**Verbatim** — `H41_D3M_PROOF_ADDENDUM_016/D3/D3_PROOF.md` lines 238-252
```text
**Uses:**
* `(B)`, through M10;
* the completion at `∞` from [CNS], through M §4;
* `(D1)` (M8), which places the result in `H⁰(X_{F₂}, Ω)`;
* `(D2)` in lattice form (M9a, M9b, with M9c);
* Č16's interchange of the two vertical generic stalks, and the `±1` action of `w₂` on `f`;
* the special fibre: reduced, exactly two components;
* the cusp geometry of M §2.

**Does not use:**
* `(D)`, Č18's multiplicity one — the argument applies no Hecke operator and never uses `𝔪`;
* any automorphism of `X` or of `X_{F₂}` — only the lattice operator on the two generic stalks, as the operator
  anticipated in audit 1;
* exceptional components — the coarse Deligne–Rapoport model has none;
* the constant `c` in `F_p|W₂ = c·F_p·G_p²`, or the sign `ε`.
```

As the operator records it:

    (B) + (D1) + (D2) + the reduced two-component special fibre + (w₂ f = ± f)   ⟹   (D3)_M.

`(D)`, multiplicity one, is not needed. It would be needed to identify a scalar if all that were known was that
`ω̄_η` and `ω̄_f` lie in the same one-dimensional Hecke eigenspace; the proof instead has exact vanishing on one
component from the `q`-expansion, carried to the other by mod-2 `w₂`-invariance. The envelope with `(D)` stays
historically correct as a conservative preregistration; it was not minimal. `ADDENDUM_010` §5's step through
exceptional `P¹`s also disappears, because M fixed the coarse Deligne–Rapoport model, which has none.
`ADDENDUM_010`, `ADDENDUM_011` and `ADDENDUM_012` are unchanged.

## 4. `ADDENDUM_012` §4 — confirmed ended at `ADDENDUM_015`

`ADDENDUM_015` recorded:

**Verbatim** — `H41_M_MODEL_RESOLUTION_ADDENDUM_015/ADDENDUM.md` lines 134-136
```text
**Consequence, by `ADDENDUM_012` §4's own terms.** From this seal, `ω̄_f`, `Ω`, `ω` and `X₀(2p)_{F₂}` are admissible
only with the meanings M fixes; in any other sense they remain inadmissible. This object contains no bridge proof and
admits none. Nothing about `(C)` or R follows from it.
```

The operator confirms that reading. The prohibition lasted until the definition/model-resolution lemma was sealed,
and `ADDENDUM_015` is that lemma. The operator's earlier instruction not to lift it applied while M was a draft.
From `ADDENDUM_015` onward the symbols are used with M's fixed meanings; nothing keeps the prohibition alive until
`(D3)_M` or R.

## 5. Custody

* **Recomputed independently by the operator:** `D3/D3_PROOF.md` has SHA-256 `98782dfb…`, and all 20 of its verbatim
  blocks are byte-identical to the sealed sources.
* **Re-checked at sealing** (`receipts/REPRODUCTION.txt`): the proof regenerates byte for byte from its carried
  generator and the sealed sources, and so do its receipts.
* **Every carried file** is listed with its digest in `receipts/CARRIED_ARTIFACT_CUSTODY.txt`.

## 6. What is and is not promoted

* **PROVED:** `(D3)_M`.
* **VERIFIED, unchanged:** G (`ADDENDUM_014`); M (`ADDENDUM_015`).
* **Not promoted:** `(C)`; R; uniform optimality `E₀ = E`; the H41 seed; the positive branch. `(D3)_M` does not by
  itself give `(C)`, as recorded from the start:

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 23-25
```text
The operator's own caveat is recorded and endorsed: **`(D3)` does not give `(C)`.** In characteristic 2
two 2-torsion classes can share a differential realisation while differing in the étale/unit-root part.
`(C) χ_p = α_p (mod 2)` remains the target; `(X) T_p ∈ π̂(E₀)[2]` from `ADDENDUM_009` §5 is untouched.
```

## 7. Next — R, the torsion-realisation bridge

G fixed the exact target:

**Verbatim** — `H41_G_VERIFIED_STATUS_ADDENDUM_014/ADDENDUM.md` lines 33-33
```text
    (C)  ⟺  (C_gen),        (C_gen):   T_p = q̂(S₀^B) ∈ J[2](ℂ).
```

**Verbatim** — `H41_G_VERIFIED_STATUS_ADDENDUM_014/ADDENDUM.md` lines 35-37
```text
**This does not prove `(C)`.** It proves that the Betti-character statement `(C)` is equivalent to this specific
equality of geometric 2-torsion points. That distinction is binding. Also verified with it: given `(C_gen)`,
`S₀^B ∈ E₀(ℚ)[2]` — rationality is a derived consequence, not a hypothesis.
```

R asks whether `(D3)_M` recovers it:

    (D3)_M   ⟹?   T_p = q̂(S₀^B).

As the operator puts it, this is where it must be determined exactly what a mod-2 differential retains about a
geometric 2-torsion point, and what it loses in the étale, unit-root and component directions. It is the next real
bottleneck, and it is no longer architecture or differential bookkeeping.

## 8. Status ladder

    G         VERIFIED   ADDENDUM_014    (C) ⟺ T_p = q̂(S₀^B)
    M         VERIFIED   ADDENDUM_015    definitions and model resolution
    (D3)_M    PROVED     ADDENDUM_016    this object
    R         NEXT                       (D3)_M ⟹? T_p = q̂(S₀^B)
    (C)       OPEN

**The H41 seed remains unproved.**
