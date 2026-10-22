# ADDENDUM_001 — node N5 and PARI's model-dependent 5-adic heights (2026-09-18)

This is an addendum. The frozen files (00_CERTIFICATE.md, BINDINGS.*, MANIFEST.sha256) are unchanged. This file's own hashes are in MANIFEST_ADDENDUM_001.sha256.

## Trigger

The Lane-2 session (bsm-28) reported, unverified, that PARI 2.17.x `ellpadicheight` / `ellpadicregulator` depend on the Weierstrass model. Its proposed offset from the canonical value is 2·truncate(b2/12)·log(P)². The seed model has b2 = −90940.

## Checks (`replays/n5_model_dependence.gp`, `replays/n5_height_valuations.gp`, under 10 CPU-s)

- **Model dependence is real.** For translations x → x + r (r = −3…3), for the b2 = −4 model (r = 7578) and for the minimal model, the regulator Reg₅ changes. Each difference from the seed-model value has ord₅ exactly 3.
- **So only Reg₅ mod 5³ is model-independent.** Printed digits of Reg₅ from 5³ upward (SW gate report, certificate node N5) are not canonical. Only the valuation is used anywhere.
- **The valuation is stable.** ord₅ Reg₅(⟨P₁,P₂⟩) = 2 in every model tried, including b2 = −4. In that model the reported offset vanishes, since truncate(−4/12) = 0.
- **Height-pairing entries.** They have ord₅ [h₁₁, h₁₂, h₂₂] = [1, 1, 2] in all three models checked. det H has ord 2, forced by h₁₂². The logs have ord₅ log P₁ = 2 and ord₅ log P₂ = 1.

## Why N5 is model-independent (proof)

1. Any change of normalization changes the pairing by a rank-one form: H′ = H + c·L·Lᵀ, where L = (log P₁, log P₂). Such a change comes from a translation, or from moving to the canonical Mazur–Tate σ; either one multiplies σ by exp(c z²/2).
2. For a rank-one update, det H′ = det H + c·Lᵀ adj(H) L. The added term is c·(l₁²h₂₂ − 2l₁l₂h₁₂ + l₂²h₁₁).
3. The three summands have ord₅ ≥ 6, 4 and 3 respectively. Whenever c ∈ Z₅, the change therefore has ord ≥ 3 > 2.
4. So ord₅ det H′ = 2 for every such c. Equivalently, ord₅ Reg₅ = 2 and ord₅ Reg_γ = 0.

The only input is c ∈ Z₅. That holds for model translations (c is an integer multiple of r). It also holds for the canonical normalization, because for good ordinary p ≥ 5 the p-adic E₂ value is 5-integral (Katz); this last point is standard but was not re-sourced here. Independently of it, the direct computation on the b2 = −4 model, which is the canonical model under the peer's formula, gives ord 2.

## Verdict

**N5 STANDS.** ord₅ Reg_γ = 0 is model-independent, and the chain N5 → N11 is unaffected. Correction for citations: never quote digits of Reg₅ beyond 5² as canonical.
