# Reconciliation of the two composition runs

No substantive mathematical disagreement. Every headline flag matches. Recorded below are the
findings both produced, the boundaries they found, and — **preserved rather than harmonised** — the
places where their wording or provenance labels differ.

## 1. Findings both reached independently

| # | finding |
|---|---|
| 1 | The comparison kernel is `K = E'_q(ℚ)[φ̂] / φ(E_q(ℚ)[2]) = {1, [D]}`, **order 2** — *not* the full four-element rational 2-torsion image of `E'_q`. Both computed it; neither assumed it. |
| 2 | On `H₄₁`, `Sel₂(E_q) ≃ ⟨[D],[q]⟩/⟨[D]⟩ ≃ C₂`. |
| 3 | From `0 → E_q(ℚ)/2E_q(ℚ) → Sel₂ → Ш[2] → 0` and `2 = 2^{rank+1}·\|Ш[2]\|`: rank 0 and `Ш[2] = 0` occur **jointly**. |
| 4 | `Ш[2^∞] = 0` follows by the elementary order argument, **without** full Ш finiteness. |
| 5 | **A logical correction both caught:** `rank = 0 ⟹ Ш[2] = 0` is **false on its own**. The two conclusions come together from the order equation, not one from the other. |
| 6 | **A refinement neither was asked for.** For an arbitrary rational degree-2 isogeny with actual Selmer shape `(4,1)`, if `t = \|E(ℚ)[2]\| ∈ {2,4}` then `\|Sel₂(E)\| = t`. So unique rational 2-torsion is needed specifically for `\|Sel₂\| = 2`; **rank 0 and `Ш[2] = 0` follow in either case.** |
| 7 | `Σ_ℓ v₂(c_ℓ) = 2` uniformly across the `S_dyadic` family: at 2, nonsplit `I_{4m−8}` with `c₂ = 2`; at odd `ℓ \| D`, `I_{v_ℓ(D)}` with odd Tamagawa factor; at `q`, `I₀*` with `c_q = 2`. |
| 8 | Uniform torsion: `E_q(ℚ)_tors ≃ C₂` and `E'_q(ℚ)_tors ≃ C₂²`, hence `τ(E_q) = 1`. |
| 9 | The two period factors kept distinct: `Ω_R = c_∞·Ω⁺` versus `ω_desc = ½·ω_min`. |
| 10 | On `H₄₁`, `m` must be **odd**, hence `(r/q) = −1`; with `(D/q) = −1`, certified F gives `v₂(N_q) = 2` and `a_q ≡ 2 (mod 8)`. The ordinarity part of the analytic input is therefore uniform. |
| 11 | Unconditional BSD(2) does **not** follow from `S_dyadic`; a **bounded, base-conditioned** transfer theorem does. |

## 2. Boundaries and counterexamples — the reason the review was worth running

Both runs refused to endorse the expected chain in general.

**`(4,1) ⟹ \|Sel₂\| = 2` is false without the torsion hypothesis.** Witness:

    E : y² = x(x − 1)(x − 9)     full rational 2-torsion

has actual isogeny Selmer shape `(4,1)`, yet `\|K\| = 1` and `\|Sel₂(E)\| = 4`.

**`H₄₁` is genuinely load-bearing — "S implies rank zero" is false.** Inside `S_dyadic` but outside
`H₄₁`:

    r = 128,  D = −511 = −7·73,  q = 29

has certified shape `(8,1)` and an explicit **non-torsion** point. Rank is not zero there.

**The complete Tamagawa product is not uniform, even though its 2-valuation is.** Witness:

    r = −128,  D = 513 = 3³·19,  q = 5   →   (c₂,c₃,c₁₉,c₅) = (2,3,1,2),  product 12

while `v₂(∏c_ℓ) = 2` still. So the invariant BSD(2) needs is uniform; the product is not.

## 3. Differences between the two runs — preserved, not harmonised

None is mathematical.

| # | difference |
|---|---|
| 1 | **Provenance label for uniform Tamagawa control.** One classifies it `IMPORTED_FROM_LITERATURE`; the other `UNIFORM_AFTER_PART_A`, while explicitly stating it comes from an independent conventional Tate-algorithm calculation. Same computation, different provenance bucket. |
| 2 | **Banwait–Huang numbering.** One cites the inspected result as headed *Theorem* 2.14; the other as *Lemma* 2.14(3). To be source-normalised before any write-up; changes no argument. |
| 3 | **Reference for the isogeny comparison sequence.** Different primary references — but **both independently computed the actual kernel**, and **both warn** against importing an `E'(ℚ)[2]` numerator where `E'[φ̂]` is required. |

## 4. What both recommend next

Identical: **formalize explicit rational saturation plus the order-two descent quotient**; keep the
base-conditioned BSD(2) transfer conventional and separate; do **not** promote `S_dyadic` to
unconditional BSD(2).

Neither recommends formalizing `H¹`, rank, Ш or BSD now. Both insist the explicit quotient be called
an **explicit descent quotient**, never a formal `Sel₂`.
