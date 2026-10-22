# Fourteenth addendum — status: G VERIFIED at its stated boundary

**Tier: STATUS OBJECT.** Records the operator's independent re-audit of `ADDENDUM_013` (`ccc77e3f…`) and the
resulting promotion. **`ADDENDUM_013` is not modified** and keeps its sealed historical status line; this object is
the authoritative current status. No new mathematics; no computation beyond digest checks and mechanical extraction
of the quoted `ADDENDUM_013` text, each quotation re-checked byte for byte (`receipts/VERBATIM_VERIFICATION.txt`).
Prior objects unmodified and byte-identical: `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`,
`0bfb6b5e…`, `3eb98a60…`, `da70ec51…`, `c1a6f8ea…`, `b7ebbf00…`, `8af7a2a5…`, `afae7941…`, `a2667972…`,
`7f7c8a9d…`, `ccc77e3f…`.

## 1. The verdict and the exact verified boundary

**RE-AUDIT VERDICT: PASS** (operator). **G is promoted to VERIFIED**, at exactly the statement sealed in
`ADDENDUM_013` §3:

**Verbatim** — `H41_G_GENERIC_FIBRE_IDENTIFICATION_ADDENDUM_013/ADDENDUM.md` lines 129-139
```text
    T_p  := [D] ∈ J[2](ℂ),    D := (k/2)·([0] − [∞]),   2D = div F              (k is even)
    S₀^B := ι_{E₀}(v̄),       v a primitive generator of H₀^{τ=−1} = ker(1+τ)    (sign of v irrelevant)

    (C_gen)    T_p = q̂(S₀^B)    in  J[2](ℂ)

**Theorem G.** For every `x ∈ H₁(X,ℤ)`:

    (G1)  (−1)^{χ_p(x)} = e_J(T_p, ι_X(x̄))
    (G2)  (−1)^{α_p(x)} = e_J(q̂ S₀^B, ι_X(x̄))
    (G3)  (C)  ⟺  (C_gen)
    (G4)  (C_gen)  ⟹  S₀^B ∈ E₀(ℚ)[2]
```

that is,

    (C)  ⟺  (C_gen),        (C_gen):   T_p = q̂(S₀^B) ∈ J[2](ℂ).

**This does not prove `(C)`.** It proves that the Betti-character statement `(C)` is equivalent to this specific
equality of geometric 2-torsion points. That distinction is binding. Also verified with it: given `(C_gen)`,
`S₀^B ∈ E₀(ℚ)[2]` — rationality is a derived consequence, not a hypothesis.

**What "VERIFIED" rests on.** The operator audited the sealed wording of the four repairs (line-numbered packet
`c7fcae4f…`, cut mechanically from the sealed file) and did not reopen the previously audited (G3)/(G4) logic
except for type and functoriality effects of the `q/φ/q̂` split. It is an independent audit of an ordinary proof
that relies on classical facts (§4). It is not a machine-checked proof.

**`ADDENDUM_013`'s sealed status line is historical and stays as sealed:**

**Verbatim** — `H41_G_GENERIC_FIBRE_IDENTIFICATION_ADDENDUM_013/ADDENDUM.md` lines 3-3
```text
**Tier: PROOF — OPERATOR-AUDITED, REPAIRED AS SPECIFIED; NOT VERIFIED.** The operator audited the draft preserved
```

## 2. Custody, recomputed independently by the operator

* Archive SHA-256 `ccc77e3f23b01db4cd29754d01e11e948056ae218e56a3bc2dea4926f480e684`; all 17 manifest entries verified.
* The separately delivered `ADDENDUM.md` is byte-identical to the archive copy, SHA-256
  `17d387ed6175bb9077087a1157e1a237683df6a5f53a82a0d18d61cebc5229f1`.
* The replacement lattice checker was rerun: 84 involutions, the 42/42 split between indices 1 and 2, all stated
  finite checks passed, all three negative controls caught.

The same digests are re-checked here at sealing (`receipts/REAUDITED_OBJECT_CUSTODY.txt`).

## 3. Verdict by repair (operator)

| repair | verdict | operator's basis, in brief |
|---|---|---|
| 1 · crosswalk `π ⇝ (φ, q, q̂)` | PASS | fixes the type error; curve-cycle pushforwards are `φ_*`, kernels, restrictions, dualization and `q̂` belong to `q`; `φ_* = q_* ∘ (AJ_∞)_*` and its cohomological dual correctly typed; `(AJ_∞)_*` an isomorphism, with no hidden quotient or finite index in `J = Hol(X)^∨/H₁(X,ℤ)` |
| 2 · literal branch cut, (G1) | PASS | the rotated ray avoids all finite nonzero critical values, so its inverse image is an unramified covering giving an integral chain `K` with `∂K = div F`; `Log∘(κF)` single-valued on the slit complement gives the winding formula and `∫_K ψ = 0`; the `O(ε\|log ε\|)` endpoint estimate is right; `K − 2c = β` gives both `T_p = ι_X(β̄)` and `(−1)^{χ_p(x)} = (−1)^{x·β}`; the sign ambiguity is harmless mod 2 |
| 3 · uniform lattice lemma (a)–(e) | PASS | `2h = (h+τh) + (h−τh)` makes `H/(L⁺+L⁻)` cyclic and killed by 2; unimodularity gives the index `\|v·u\|`; `f = v·(–)` is the primitive generator with mod-2 dual `v̄`; (e) since `ū, v̄ ≠ 0` in the two-dimensional `F₂`-space; the finite computation is corroboration and regression testing, not proof |
| 4 · functoriality, (G2) | PASS | the adjunction `e(a, q^∨b) = e(qa, b)` with principal polarizations gives `e_J(q̂s, t) = e_{E₀}(s, qt)` with no degree factor; `q(ι_X x̄) = ι_{E₀}(φ_* x̄)` holds because the analytic linear map of `q` sends `ℓ` to `ℓ ∘ φ^*` |
| (G3), (G4) | valid | nondegeneracy gives `(C) ⟺ T_p = q̂(S₀^B)`; the dual of an optimal quotient with connected kernel is a closed immersion, so equality with the rational `T_p` forces `S₀^B` to be Galois-fixed |

## 4. Citation record, as confirmed or clarified by the operator

None of these sources is in the corpus; they are recorded as the operator's checked citations.

* **Milne, *Abelian Varieties*, Proposition 13.2** — the adjunction `e(a, q^∨b) = e(qa, b)` and skew-symmetry of the
  polarized pairing.
* **Milne, Example 13.3** — the polarized Weil pairing is the Riemann form on integral homology up to the conventional
  sign, and the Jacobian's Riemann form is the intersection form.
* **Milne** — the intersection form supplies the Jacobian's Riemann form, and Abel–Jacobi identifies divisor classes
  modulo principal divisors with `Pic⁰ ≅ J`.
* **Stein–Conrad, Proposition 3.3** — the dual of an optimal quotient with connected kernel is a closed immersion.
  **Clarification:** `ADDENDUM_013` §9 recorded this citation as "Stein, Proposition 3.3":

**Verbatim** — `H41_G_GENERIC_FIBRE_IDENTIFICATION_ADDENDUM_013/ADDENDUM.md` lines 298-299
```text
* **[F6]** The dual of an optimal quotient (connected kernel) is a closed immersion. *Operator cites Stein,
  Proposition 3.3;* also asserted in the seal at `ADDENDUM_005` l.83.
```

  The operator's re-audit names it Stein–Conrad. It is recorded so here; `ADDENDUM_013` is unchanged.
* **McMullen** — the inverse-image-of-a-ray and branch-cut proofs used for Lemma 1, as cited in `ADDENDUM_013`.

## 5. Two non-blocking editorial readings of the sealed text

These are **readings**, not repairs; the sealed `ADDENDUM_013` text is unchanged and the proof has no gap.

**(i) Lemma 1, the slit plane.**

**Verbatim** — `H41_G_GENERIC_FIBRE_IDENTIFICATION_ADDENDUM_013/ADDENDUM.md` lines 156-156
```text
`∂K = Σ_P ord_P(F)·P = div F`, which is (1). On `X∖K` the function `κF` takes values in `ℂ∖[0,∞]`, where the branch
```

`ℂ∖[0,∞]` is to be read as the usual slit plane `ℂ∖[0,∞)`. As subsets of `ℂ` the two coincide, since `∞ ∉ ℂ`; the
notation is simply unusual.

**(ii) Lemma 2, "take `u, v` primitive".**

**Verbatim** — `H41_G_GENERIC_FIBRE_IDENTIFICATION_ADDENDUM_013/ADDENDUM.md` lines 202-202
```text
`+1` and `−1` once each; so `L⁺`, `L⁻` have rank one. Take `u, v` primitive. (a) `H/L⁻ ≅ ℤ` because `v` is
```

The omitted justification is immediate and is supplied here for completeness: `ker(τ ∓ 1)` is saturated in the
torsion-free lattice `H` — if `m·y ∈ ker(τ ∓ 1)` with `m ≠ 0`, then `m·(τ ∓ 1)y = 0`, so `(τ ∓ 1)y = 0` — hence each
rank-one kernel is generated by a primitive vector.

## 6. What is and is not promoted

* **VERIFIED:** `(C) ⟺ (C_gen)`; and, given `(C_gen)`, `S₀^B ∈ E₀(ℚ)[2]`.
* **Not promoted:** `(C)` itself; `(D3)`; any characteristic-2 or integral-model geometry; uniform optimality
  `E₀ = E`; the H41 seed; the positive branch.
* `ADDENDUM_013` §8's level-specific items remain dependencies on earlier sealed results and are not promoted by this
  re-audit.

## 7. M — authorized, with its scope fixed

**M may begin.** Its permitted scope is purely definitional and geometric:

1. fix the integral model;
2. fix the sheaf;
3. define `ω̄_f`;
4. formulate a repaired `(D3)` on exactly those objects;
5. show that the repaired formulation matches what the earlier arithmetic arguments were actually establishing.

**M makes no implication to `(C)`.** Whether the resulting mod-2 differential equality sees enough of the 2-torsion
point to recover `T_p = q̂(S₀^B)` is R.

## 8. Status ladder

    ADDENDUM_013 sealed  ≠  G verified          — now satisfied by the independent re-audit
    G verified           ≠  (C)
    M (definitions)      ≠  R (implication to (C))

**The H41 seed remains unproved.**
