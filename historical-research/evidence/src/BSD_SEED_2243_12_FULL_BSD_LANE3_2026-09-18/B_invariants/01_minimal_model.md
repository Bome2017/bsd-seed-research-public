# B.1 — Minimal model, Néron differential, sign of Δ, real components

Scripts: `scripts/s01_03_local.gp` (PARI 2.17.3) → `out/s01_03_local.out`; `scripts/s01_03_sage.sage` (Sage, eclib/PARI) → `out/s01_03_sage.out`.

| item | value | label |
|---|---|---|
| model | E₀: y² = x³ − 22735x² + 106272484x = [0, −5A, 0, 4AB, 0] | given |
| Δ | 16586638656786071143743744 = 2⁸·3²·2243·4547³·5843² | PROVED (exact integer arithmetic; PARI and Sage agree) |
| c₄ | 3169004368 = 2⁴·43·1013·4547 | PROVED (exact) |
| global minimality | E₀ is globally minimal: for every p, v_p(Δ) < 12 (max is 8, at p = 2), so no p-adic scaling u with p ∣ u can exist (u⁻¹² Δ must stay integral with v_p(c₄) ≥ 4, v_p(Δ) ≥ 12 required). PARI `ellminimalmodel` returns [u,r,s,t] = [1, 7578, 0, 0] (u = 1); `ellglobalred` returns the same change; Sage `is_global_minimal_model()` = True. | PROVED (Tate/Kraus minimality criterion v_p(Δ) < 12 ⇒ minimal at p) |
| reduced minimal model | E_r: y² = x³ − x² − 66020924x − 65074271436 = [0, −1, 0, −66020924, −65074271436], obtained by x = x_r + 7578 (u = 1, translation only). Sage's `is_minimal()` = False only because Sage's `is_minimal` tests the *reduced* form (a₁,a₂,a₃ normalised), not minimality. | PROVED |
| Néron differential | ω = dx/(2y + a₁x + a₃) = dx/(2y) on E₀ (u = 1, so E₀'s invariant differential is the Néron differential; the translation to E_r does not change ω) | PROVED |
| sign of Δ | Δ > 0 | PROVED |
| real components | 2. The 2-division cubic 4x³ + b₂x² + 2b₄x + b₆ = 4x(x² − 5Ax + 4AB) has the three real roots e₃ = 0 < e₂ = (5A − 3√(mA))/2 < e₁ = (5A + 3√(mA))/2 (25A² − 16AB = 9mA > 0 and 25A > 9m), numerically e₁ = 16157.8624…, e₂ = 6577.1375…; Sage `real_components()` = 2. | PROVED (exact roots) |
| j | 1322372123614064/689197281363 | PROVED |
| conductor | N = 6503188012738584 = 2³·3·2243·4547²·5843 | PROVED (PARI `ellglobalred` and Sage agree; matches brief) |
