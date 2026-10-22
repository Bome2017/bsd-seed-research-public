# Recalculated certified workload by route (2026-09-23)

**Baseline** (pilot-prep S4, pinned): per-symbol identification at T_run = 3.912·10¹³, **110 622.5 local core-hours (lch)**.
* Coefficient production is 84% of that, verification 13%, and the engine 3%.
* **The cutoff is set by the kernel e^{−κn}**, with κ = 2π/(p²√Q) = 7.3345·10⁻¹³, **not by how many outputs are extracted.**
* A route saves dominant work only if it lowers the cutoff (or the analytic scale p²√Q), or replaces the coefficient range altogether.

The modelled totals below come from the same S4 model, imported read-only (`checks/workload_model.py` → `.txt`; it reproduces the baseline to 0.1 lch). The other figures are exact or closed-form (`checks/*.txt`).

| route | exact identity it gives | cutoff / space needed | vs current | modelled lch | verdict |
|---|---|---|---|---|---|
| **R0 current** | K ≡ c₃ = [T³]Σ_j Y_j(1+T)^j (mod p) | T_run = 3.912·10¹³ (scale 8.57·10¹², ×4.57) | 1 | 110 622.5 | baseline |
| **R1 W_Q pairing** (the additional relation) | Y_{−L−j} = −Y_j (L = 1989); Y₁₂₇ = 0; c₀ = 0; c₂ = −995·c₁; c₄ = 1247·c₃ + 511·c₁ (mod p) | unchanged: T_run | 1 (output halved only; already implicit in the engine formula) | 110 622.5 | **c₃ free** (rank 2 > 1) |
| R1 applied to U_p traces | row sums R_a = a_p·1024[a/p]⁺ | — | — | — | fixes c₀ only (Lemma T) |
| R2 Γ₀(N) loops | x_b = x_{1/p} + n_b, n_b = period of γ_b | base-point scale \|c_b\| = N\|k_b\| ≥ N = 6.50·10¹⁵ | ≥ 759×; actual 1.6·10⁸–1.8·10⁹× | not modelled | worse |
| R2 algebraic | f-projection on level-N symbols | dim M₂(Γ₀(N)) ≈ 2.17·10¹⁵; 1.30·10¹⁶ Manin symbols | — | — | prohibitive space |
| R2′ W_p, W_N moves | x_b = ±[x/(Qz)]⁺, or at −p/(Qb′) | scale ≥ Q√p = 1.37·10¹⁴ | ≥ 16.0× | not modelled | worse |
| R2′ W_Q move | x_b = s·x_{u_b} | — | = R1 | — | nothing new |
| R3 T_ℓ / U_ℓ | a_ℓx_b = Σ_t x_{(b+tm)/ℓm} + x_{ℓb} | denominators ℓp²; T₅ route T = 1.956·10¹⁴ | 5× cutoff | 735 762 (6.65×; producer rate extrapolated) | worse, and yields only ℓ-fold sums |
| R4 Hida / two-variable | — | S₂₂₄₄(Γ₀(N/p)) dim ≈ 1.08·10¹⁵, or 1.30·10¹⁶ overconvergent Manin symbols | — | — | prohibitive space |
| R5 Galois conjugacy | c₃ ≢ 0 ⟺ v_p(N_{Q(ζ_p)/Q}A(ψ)) = 3 | all p − 1 twists (= current); or one embedding to ~10⁴ digits plus a rank-2242 lattice reduction | ≳ 10³× cutoff | — | change of basis only |
| **R6 aggregation** (by-product) | Y_j from p + 2 wild class sums via Gauss periods (max\|G\| = 366.26) | T = 4.622·10¹³ (+7.10·10¹²) | 1.18× cutoff | **134 570.1 (1.216×)** | saves memory (no length-p² DFT, no 103 GB checkpoints); costs 22% more |
| R7 Kurihara / Kolyvagin | different sufficient certificate at n = ℓ₁ℓ₂ = 5.41·10¹⁶ | cutoff ≈ 1.99·10²⁵; ≈ 5.4·10¹⁶ symbols | 5.1·10¹¹× | not modelled | infeasible |
| R8 Mazur–Tate / MTT p-adic BSD | would give c₃ from Mordell–Weil data | — | — | — | unproved and circular (presupposes #Sha) |

**Already-certified data.**
* The certified a_q corpus reaches q < 1.485·10¹⁰, which is **3.8·10⁻⁴ of T_run**. Its a_n are reusable inside production and change nothing.
* The certified symbol tables (m = 25, 27, 81, …) are at denominators prime to 2243. Relations reach p² from them only through new level-p²m unknowns.

**Net: no route lowers the coefficient range.** The only routes that preserve it (R0, R1) leave c₃ as an unknown to be evaluated. Every other route raises the cutoff or needs a 10¹⁵–10¹⁶-dimensional symbol space.

**All-in dollar scenarios are unchanged** ($1,368 low / $2,162 central / $3,947 high-spot / $5,762 on-demand / $8,059 worst). They remain modelled scenarios, not quotes, and paid computation stays parked.
