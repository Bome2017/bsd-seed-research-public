# SEED_PROVED_STATE — what is established for the seed, with provenance (2026-09-19)

Labels: PROVED · PROVED_COMPUTER_ASSISTED · CERTIFIED_NUMERIC · CONDITIONAL · FORMULATED · PROPOSED · SEMI_DECISION ·
COST_BLOCKED · ROUTE_BLOCKED · OPEN · SUPERSEDED · KILLED. Nothing here is merged by this handoff.
"Record" = the on-disk artifact that carries the claim (sha256 in `SOURCE_AND_HASH_INDEX.md`).

## 0. The curve

    E : y² = x³ − 22735x² + 106272484x        (Zywina family, (m,n) = (2243,12), A = 4547, B = 5843)
    N = 2³·3·2243·4547²·5843 = 6 503 188 012 738 584          Δ = 2⁸·3²·2243·4547³·5843² > 0 (two real components)
    minimal model: [u,r,s,t] = [1,7578,0,0] (x-shift only)
    P₁ = (4547, 327384),  P₂ = (5184, 281520),  T = (0,0)

| local datum | value | status |
|---|---|---|
| Kodaira types / c_ℓ | 2: I₁* (2) · 3: I₂ (2) · 2243: I₁ (1) · 4547: III (2) · 5843: I₂ (2); ∏c_ℓ = 16 | PROVED (exact; re-derived by F2) |
| a_ℓ at bad ℓ | a₃ = −1 (non-split), a₂₂₄₃ = +1 (split), a₅₈₄₃ = −1 (non-split), a₂ = a₄₅₄₇ = 0 | PROVED (exact) |
| root number | w = +1 (local: +1,+1,−1 at 2243,+1,+1; ∞: −1) | PROVED |
| 4547 | additive III, potentially good SUPERSINGULAR (j ≡ 1728, 4547 ≡ 3 mod 4), inertia cyclic of order 4, no abelian base change to good reduction | PROVED (F2 §B) |
| good supersingular p < 2000 | 23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823 (a_p = 0) | PROVED (exact) |
| anomalous good p | none (#E(F_p) is even; p ∣ #E(F_p) forces p ≤ 5; #E(F₅) = 8) | PROVED |

## 1. RANK — DONE

| claim | status | record / provenance |
|---|---|---|
| E(Q) ≅ Z/2 × Z², basis P₁,P₂ of E(Q)/tors (index 1) | PROVED | Zywina arXiv:2502.01957v1 Thm 1.2 (a 2025 PREPRINT, 2-isogeny descent) + exact PARI replay `ellrank` = [2,2,0], `ellsaturation`; master certificate N1, N2 |
| rank E(Q) = 2 | PROVED | same |
| L(E,1) = 0, L′(E,1) = 0 | PROVED | P₁ of infinite order + Kolyvagin/Kato (L(E,1) ≠ 0 ⇒ finite E(Q)); w = +1 |
| **ord_{s=1} L(E,s) = 2** | **PROVED_COMPUTER_ASSISTED** | `BSD_RIGOROUS_STREAM_CORE_2026-09-19/ANALYTIC_RANK_CERTIFICATE.md`: Arb ball L″(E,1)/2 = 35.93531375275170089 ± 5.709·10⁻³ ⊂ [35.929604, 35.941023], 8 444 396 a_q independently verified, no floating-point model; trust base FLINT/Arb 3.3.1, GMP, MPFR, clang, verifier+engine, hardware |
| earlier label "analytic rank = 2 CERTIFIED_NUMERIC" (Lane 3, floating point) | SUPERSEDED | kept only as a consistency check (its value lies inside the Arb ball) |

## 2. Galois image, Manin constant, periods, regulator

| claim | status | provenance notes that must travel |
|---|---|---|
| ρ̄_{E,ℓ} = GL₂(F_ℓ) for every odd ℓ (hence ρ_ℓ onto GL₂(Z_ℓ) for ℓ ≥ 5) | PROVED | derived theorem ALL_ODD_RESIDUAL_IMAGE_VERIFIED (inertia of order 4 at A, Tate transvection at m, Mazur for ℓ = A); reviewed in `BSD_C1_RESIDUAL_IMAGE_REVIEW_2026-09-17` |
| 4547 ∤ c₀ (Manin constant of the optimal curve) | PROVED | Edixhoven [Edi91 Thm 3] used through two published RESTATEMENTS (CNS, Česnavičius); primary paywalled, unread |
| v₂(c₀) ≤ 8, so c₀ = 2^a, a ≤ 8, c_E ∣ 2⁹, symbols lie in (1/1024)Z | PROVED | DERIVED lemma (no source states it): Pasten §10 + CNS 6.12(c) + ARS 3.6(a) + intersection theory on X_{Γ0(N)∩Γ1(5)}; Lane 4 audit PASS (five tracks) + 4 Lean files. Secondary-source inputs: Katz–Mazur 13.4.7/12.2.1, Liu 9.1.37 |
| v₂(c₀) ≤ 4 | CONDITIONAL | on KM 13.4.7 contact orders; not needed |
| ω₁ = 0.0280449015194364044483094018079 ± 3.04·10⁻³², Ω_E = 2ω₁ | PROVED_COMPUTER_ASSISTED | Arb AGM (P3 certificate §1) |
| Reg(P₁,P₂) ∈ (17.79651747249034020748, 17.79651747249034039153) (BSD normalisation); the PARI value 17.7965174724903402991749412194360384… lies inside | PROVED_COMPUTER_ASSISTED | Codex `REGULATOR_CERTIFICATE.md` (2026-09-19; directed-rounding Decimal, exact tail bound, exact 2R ∈ E⁰ checks), replayed byte-identically by Opus at both settings. Historical: Lane 3 `B_invariants/06_period_regulator.md` (Arb, labelled CERT-NUM there); the earlier note "PARI; not an Arb enclosure" was wrong |
| C := Ω·Reg·∏c/#tors² = 3.99281263923936691806855200220915… (= 4Ω·Reg, Ω·Reg ∈ (0.99820315980984172437, 0.99820315980984173470)) | PROVED_COMPUTER_ASSISTED | same certificate (independent AGM for Ω). Historical: two normalisation paths agree (direct, PARI `ellbsd`) |
| L″(E,1)/2 = 35.9353137531543022480 ± 3.008·10⁻¹⁵ | CERTIFIED_NUMERIC | Lane 3 run B (floating-point model, certified truncation); 15 significant digits |
| (L″/2)/C = 9 ± 7.54·10⁻¹⁶, i.e. L″(E,1)/(2ΩReg) = 36 ± 3·10⁻¹⁵ | CERTIFIED_NUMERIC | arithmetic downstream of the rows above; the 15-digit L″ is floating-point, NOT a rigorous ball. Rigorous version: q_∞ ∈ (35.99427, 36.00573), PROVED_COMPUTER_ASSISTED (Arb L″/2 ball ÷ certified Ω·Reg); equivalently (L″/2)/C ∈ (8.99856, 9.00144) |

## 3. Sha, prime by prime (everything here sits UNDER the top-level obligation FIN)

| prime(s) | claim | status | record / provenance |
|---|---|---|---|
| 2 | Sha[2^∞] = 0 | PROVED | Zywina Thm 1.2 (Sha[2] = 0); PARI `ellrank` s = 0 consistent |
| **3** | **Sha[3^∞] ≅ (Z/3Z)², #Sha[3^∞] = 9** | **PROVED_COMPUTER_ASSISTED**, relative to Skinner (2016) Thm A **as printed**; F1 notes **R1, R2 carried, NOT closed** | `BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/SHA3_THEOREM.md`, `P3_CERTIFICATE.md`: rigorous depth-4 run, 663 685 727 a_q verified (root `5f9994d9…`), 144 symbols in Arb balls identified in (1/1024)Z (all integers), **a_{4,2} = 15480 = 2³·3²·5·43 ≡ 9 (mod 27)** (ω₁ normalisation; SW/Néron normalisation 7740 ≡ 18), **ord₃ = 2**, a_{4,0} = 0, a_{4,1} = −54. Chain: SW Prop 3.5 (c = 0) → Skinner Thm A (both divisibilities) → SW Thm 6.1 (equality clause: finiteness + non-degenerate height) → leading term (ε₃ = 2, ∏c = 16, Reg_γ 3-unit, #tors = 2) → 9 → Cassels–Tate ⇒ (Z/3)² |
| 3 — R1 | Jones 1989 (Duke 59; multiplicative case behind SW Thm 6.1) UNREAD | OPEN (provenance note, carried) | supporting only: F1 universal-norm argument, exact p-adic BSD numerics on 57a1, 681c1 |
| 3 — R2 | R2 remains OPEN as a provenance seam, narrowed to the canonical-vs-Gross period comparison for p = 3 with 3 ∣ N. In print the comparison behind SU Prop 12.3.6 exists only for p ≥ 5, p ∤ N (Kim–Ota 2023 removes Pollack–Weston's squarefree restriction there); **no located source covers p = 3 ∥ N**; load-bearing (no second source: Kato excludes 3 ∣ N) | OPEN (provenance seam, carried; label of Sha[3^∞] unchanged per the addendum's recommendation) | `addenda/P3_R2_PERIOD_PROVENANCE_AUDIT.md` (source reading only, no computation). "No located source" ≠ failure; nothing found shows the comparison fails. If R2 failed, BOTH finiteness and the order at 3 would lose their proof. Cheapest next steps listed there: Wan 2023 on canonical vs Gross periods; integral Jacquet–Langlands at p ∣ N; ask an author |
| 3 — R8 | floating-point certification of the run | SUPERSEDED (discharged) | the run is Arb + independently verified coefficients |
| **5** | **Sha[5^∞] = 0** | **PROVED_COMPUTER_ASSISTED** — `P5_RIGOROUS_SHA5_ZERO_CONFIRMED` (finished and sealed 2026-09-19; `P5_MANIFEST.sha256`, 9 424 files) | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/{P5_RIGOROUS_REPORT, P5_CERTIFICATE, SHA5_RIGOROUS_THEOREM, P5_REPLAY, P5_RESOURCE_LOG}.md`. Same chain as the frozen master certificate (DAG N0–N11; Kato + SW Thm 6.1 only; uses v₂(c₀) ≤ 8) with **node N7 upgraded from CERT-NUM to PROVED_COMPUTER_ASSISTED**: 360 542 141 a_q independently verified (root `fcd02437…`, byte-identical to the p = 3 run on the shared range); the 20 symbols [b/25]⁺ recovered rigorously by Arb in (1/1024)Z = (−54, 16, 90, −52, −76, 16, 76, −52, −54, 90, 90, −54, −52, 76, 16, −76, −52, 90, 16, −54), identical to LP5; six-symbol value 152; **a_{2,2} ≡ 2 (mod 5) in the ω₁ normalisation** (≡ 1 Néron), **ord₅(a₂) = 0**. The master certificate file is frozen and unedited (it still prints N7 = CERT-NUM); the successor governs. Remaining weakest links: v₂(c₀) ≤ 8 DERIVED; Edixhoven via restatements; Zywina preprint. Nothing merged |
| 30 | #Sha[30^∞] = 9 | PROVED_COMPUTER_ASSISTED | follows from the three rows; **no CERT-NUM qualifier remains on the p = 5 input**; inherits R1/R2 from p = 3; equals the certified numerical Sha_an = 9 |
| good ordinary p ≥ 7 | Sha[p^∞] = 0 | OPEN (per-prime decision procedure on paper: Kato + SW 6.1, ≈ 0.23·p² CPU-h in Lane 3's cost model; none run; p = 7 NOT authorised) | F2 §F.2; Lane 2 ONE-BIT (no Reg/saturation gate needed) |
| good supersingular p | Sha[p^∞] = 0 | **SEMI_DECISION via CRITERION_SS** — the route is PROVED (hostile gate `CRITERION_SS_VALID_WITH_CORRECTIONS`, 2026-09-19); no bit computed for the seed (≈ 270 / 460 CPU-h at 23 / 29); old "depth 5–6, ROUTE_BLOCKED" SUPERSEDED | F2 §B.1; SS gate |
| 2243, 5843 | Sha[p^∞] = 0 | COST_BLOCKED (decision on paper: Skinner Thm A + SW; ≈ 2·10⁴ / ≈ 10⁵ CPU-h, architect's figures, not re-derived) | F2 §F.2 |
| 4547 | Sha[4547^∞] = 0 | SEMI_DECISION + ROUTE_BLOCKED (theory gap AND cost; see `FIN_FRONTIER.md` §4) | F2 R1 |
| all p > p₀ | Sha[p] = 0 | OPEN (F3: NOT_FOUND in the literature; not an impossibility claim) | F3 |

## 4. Same-family caveat (applies to every "audited" label above)
Every audit cited (Lane audits, F1–F4, Lane 4, LINE hostile audit) was run by fresh-context sessions of the SAME model family as
the authors. None is independent in the project charter's sense. The Codex/Astra audit is the first cross-family review.
