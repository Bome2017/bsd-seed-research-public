# PRELAUNCH_GATE: rigorous p = 5 upgrade (seed 2243,12), recorded 2026-09-19T06:28:43-0700

| # | gate item | result | evidence |
|---|---|---|---|
| 1 | rigorous-core MANIFEST.sha256 (1718 files; manifest sha256 f94c90c7…) | **1718/1718 OK** before and after rebuild | core_manifest_verify.txt, core_manifest_after_rebuild.txt (0 mismatches) |
| 2 | rebuild from source (`./build.sh`) | exit 0; the rebuilt binaries are byte-identical to the MANIFEST (arbcore 47d07f2e…, apwit c21429cc…, wverify 9f4b136a…) | build_output.txt, source_and_binary_hashes.txt |
| 3 | rebuilt binaries reproduce existing validation artifacts | **11/11 byte-identical**: 389a1 msl and ms at m = 25 (s = +1); 37a1 msl at m = 25 (s = −1); 446d1 msl at m = 5; the full 24a1 run_p3 pipeline (7 artifacts) | rebuild_reproduction.txt |
| 4 | no stale heavy project process | 0 apwit / wverify / arbcore / sage / gp / run_p3 / monitor / replay; load ≈ 1.5 | stale_and_system.txt |
| 5 | exact truncation (`arbcore tmin`, recomputed) | m = 25, LATDEN 1024: **T_min = 7 825 119 335** (T_min − 1 fails), which is the recorded value; operational T = 7 834 959 871 = 467·2²⁴ − 1. m = 5: T_min = 1 511 545 536, T = 1 526 726 655 = 91·2²⁴ − 1 | tmin_p5.txt |
| 6 | lattice / Manin assumptions | Audited p = 5 gate: every b/25 and b/5 is Γ₀(N)-equivalent to 0, and λ(0) = L(E,1) = 0. So λ(b/m) ∈ Λ_f and x_b ∈ (1/c_E)Z (master N7), or conservatively (1/(2c_E))Z (gate addendum (iii)). With c_E \| 2c₀, c₀ = 2^a, a ≤ 8 and 4547 ∤ c₀ (master N8), c_E \| 512, so (1/(2c_E))Z ⊆ **(1/1024)Z = LATDEN 1024**. This is a theorem input, not verified by the run. The same argument applies to the minus symbols (Λ_E rectangular) | master certificate N6–N8; SW gate addendum |
| 7 | resources at launch | disk: 142Gi free of 932Gi; memory free: 62%; swap: total = 3072.00M  used = 1596.50M  free = 1475.50M  (encrypted); thermal: CPU_Speed_Limit 100, no warnings | stale_and_system.txt |

**Specification agreement with the audited p = 5 gate:**
- m = 25, Q = N (5 ∤ N, M = 1), sign s = w = +1;
- measure μ(b + 25Z₅) = α⁻²[b/25]⁺ − α⁻³[b/5]⁺, α the unit root of x² − a₅x + 5 with a₅ = −2 (α ≡ 13 mod 25);
- a₂ ≡ a_{2,2} (mod 5) (SW Prop 3.5, c = 0).

m = 5 is added to supply the exact [b/5]⁺ term and the T₅ Hecke check; it does not change the formula. **No disagreement found.**

**Pipeline:** `p3plan/run_p3.sh` (generic target list), TARGETS="25:1:1 5:1:1", LATDEN = 1024, J = W = 16, OUT = <this dir>/run. The guard's environment variable is named P3_AUTHORIZED. It is set to "yes" for this run under the operator's explicit p = 5 authorization of 2026-09-19; no guard code is modified or bypassed.

**Workers:** J = W = 16 (80 % of 20 logical CPUs). The governor may reduce to 12 / 10 on sustained memory pressure, swap growth or throttling.

**Witness retention:** KEEP_WIT auto (free disk ≥ 60 GB, so 1). Projected ≈ 9.7 GB of witnesses plus 1.4 GB of a_q.

**Source identities:** identical to the p = 3 run (see source_and_binary_hashes.txt). **Start time:** 2026-09-19T06:28:43-0700.
