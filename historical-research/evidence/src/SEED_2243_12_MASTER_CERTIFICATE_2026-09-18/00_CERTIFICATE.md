# SEED_2243_12_MASTER_CERTIFICATE (frozen 2026-09-18)

**Statement.** Let E: y² = x³ − 22735x² + 106272484x, the Zywina curve for (m, n) = (2243, 12), with A = 4547 and B = 5843. Then **Sha(E/Q)[5^∞] = 0**.

**Status: `SMALL_SEED_2243_12_SHA5 = PROVED_ZERO`, via the derived v₂(c₀) ≤ 8 lemma.** Ledger: `~/H9R19_WEIGHTED_RECIPROCITY_2026-09-15/08_PROGRAM_STATUS_FREEZE.md`, block MANIN_2_PRIMARY_GATE_2243_12 (ledger sha256 `7062cfd0…`).

This file holds only the dependency DAG of that proof. Nothing exploratory is recorded here. Every node points to a merged record, and every record is bound by sha256 in `BINDINGS.sha256`. Run `verify_bindings.sh` to check them.

## 1. The DAG

The operator's chain (Zywina rank 2 → saturation → GL₂(F₅) → Reg_γ unit → a₂ ≡ 2 → v₂(c₀) ≤ 8 → Sha[5^∞] = 0) has the same nodes. The real dependencies are not linear; the edges below are the actual ones.

Complete edge list (node ← its direct inputs):

| node | direct inputs | what flows along the edge |
|---|---|---|
| N0 CURVE | — | model, N, local types, a₅ |
| N1 MW | N0 | Zywina's hypotheses (m, A, B prime, ≡ 11 mod 24) |
| N2 SAT5 | N0, N1 | the points P₁, P₂; reductions at 31 and 181 |
| N3 IMG5 | N0 | ψ₅, v_m(Δ) = 1 |
| N4 KATO | N0, N3 | good ordinary at 5; ρ₅ surjective |
| N5 REG | N0, N1, N2 | P₁, P₂; 5 ∤ I; α, Tamagawa numbers, torsion |
| N6 SW FORMULA | N0 | α ≡ 13 (mod 25); 5 ∤ c_E (Mazur) |
| N7 NUMERICS | N0, N1 | L(E,1) = 0 (rank 2 ⇒ L(E,1) = 0 by Kato/Kolyvagin), so c_E·x_b ∈ Z |
| N8 MANIN | N0 | v₂(N) = 3, 3 \| N, type III at 4547, 2-isogeny class of size 2 |
| N9 A2 | N6, N7, N8 | c_E ≤ 512 < 3 999, so the symbols are identified; six-symbol value 152 |
| N10 ORD | N1, N4, N9 | ord_T L₅ ≥ 2 (rank 2 with Kato); a₂ ≢ 0 (mod 5) |
| N11 SHA5 | N4, N5, N10 | SW Thm 6.1 bound with b₅ = 0 |

## 2. Nodes

Type legend:

| tag | meaning |
|---|---|
| **EXACT** | exact machine computation (PARI), script and output bound |
| **PUB** | published theorem, hypotheses checked on the seed |
| **PUB-R** | published theorem used through a published restatement (primary not read) |
| **DER** | derived lemma (not stated verbatim in any source), refereed |
| **CERT-NUM** | certified-error numerical computation plus integrality |

| node | claim | type | record (bound in BINDINGS) | audit layers |
|---|---|---|---|---|
| **N0 CURVE** | m, A, B prime (APR-CL) and all ≡ 11 (mod 24). N = 2³·3·2243·4547²·5843 = 6 503 188 012 738 584. Types: 2: I₁\* (c=2); 3: I₂ (2); m: I₁ (1); A: III (2); B: I₂ (2). Tamagawa product 16; root number +1; E(Q)_tors = Z/2. Good ordinary at 5: a₅ = −2, #E(F₅) = 8. | EXACT | small-seed report §1; `runs/step1_seed_checks.gp` and its output | author plus independent check at merge |
| **N1 MW** | E(Q) ≅ Z/2 × Z² with P₁ = (A, 6nA), P₂ = (36n², 12n(m−2n²)); Sha(E/Q)[2] = 0. | PUB (Zywina arXiv:2502.01957v1 Thm 1.2, local source l. 35–56; 2-isogeny descent) **plus** EXACT replay | `34_SRC_zywina…` l. 35–56; `replays/rank_replay.gp`: PARI `ellrank` = [2, 2, 0], so the rank is exactly 2 by 2-descent, independent of the preprint | Zywina's paper is an arXiv preprint (v1, Feb 2025); the rank is independently replayed here |
| **N2 SAT5** | Reduction rows at ℓ = 31: (1,1); at ℓ = 181: (1,0). det = −1 ≢ 0 (mod 5), so E(Q)/5E(Q) = ⟨P₁, P₂⟩ and 5 ∤ I = [E(Q)/tors : ⟨P₁,P₂⟩]. | EXACT | small-seed report §1 (S8, S9); replay: `ellsaturation(E,[P1,P2],50)` returns an index-1 basis (regulator ratio 1) | author plus merge check plus this replay |
| **N3 IMG5** | ρ̄₅(G_Q) = GL₂(F₅): ψ₅ is irreducible of degree 12, and there is a Tate transvection at m (v_m(Δ) = 1). Hence ρ₅ is surjective (SW Prop 7.2, p ≥ 5). | EXACT + PUB | small-seed report §1 (S10); general theorem ALL_ODD_RESIDUAL_IMAGE_VERIFIED (ledger) | two independent routes |
| **N4 KATO** | f_E(T) divides L₅(E,T) in Λ (SW Thm 7.3; needs semistable at 5 and ρ₅ surjective). | PUB | SW gate Phase A; SW text `27_SRC_stein_wuthrich_shark.txt` | merged gate |
| **N5 REG** | Reg₅(⟨P₁,P₂⟩) = 5² + 2·5⁴ + 3·5⁵ + … + O(5²⁶), ord 2, nondegenerate. PARI's normalization = SW's (446d1 reproduced to O(5⁷)). Index lemma Reg₅(H) = I²·Reg₅(E(Q)) with 5 ∤ I (N2). So ord₅ Reg_γ = 0. ε₅ = (1 − 1/α)² is a unit (α ≡ 13 mod 25), the Tamagawa product (16) is a 5-unit, and #E(Q)(5) = 1. | EXACT + PUB | SW gate Phase A–B; `runs/phaseB_regulator.gp` and its output | merged gate |
| **N6 SW FORMULA** | SW Prop 3.5 at n = 2 with c = 0: a₂ ≡ T²-coefficient of P₂ (mod 5), which reduces to **a₂ ≡ 3([2/25]⁺+[3/25]⁺+[4/25]⁺+[11/25]⁺) + 4([9/25]⁺+[12/25]⁺) (mod 5)**. c = 0 because 5 ∤ c_E: Mazur gives p \| c₀ ⇒ p² \| 4N, and u ∈ {1, 2}. | PUB + algebra | SW gate addendum (six-symbol, independently re-derived); LP5 `runs/p2check.gp` (the full 20-symbol P₂ gives the same bit) | merged gate |
| **N7 NUMERICS** | All 20 [b/25]⁺ computed by Wuthrich 2018 §4 streaming. Certified truncation errors: 2.5·10⁻⁴ (T₁ = 7 682 510 690) and 2.5·10⁻⁶ (T₂ = 9 134 686 292). Every value is within 2.63·10⁻¹² of an integer. Since b/25 ~ 0 under Γ₀(N) and L(E,1) = 0, c_E·x_b ∈ Z, so the identification is exact whenever **c_E ≤ 3 999 (T₁) or c_E ≤ 399 575 (T₂)**. The six-symbol value is **152**. | CERT-NUM | LP5 report §1–4 and addendum; `MANIFEST.sha256`; `runs/seed_eval.gp` and its output | validation on 37a1, 389a1, 446d1 and 234446a1; T₁ and T₂ agree; 417 382 PARI spot checks with 0 mismatches |
| **N8 MANIN** | c₀ = 2^a:<br>– Mazur gives p \| c₀ ⇒ p² \| 4N.<br>– 4547 ∤ c₀ by Edixhoven [Edi91 Thm 3]: the reduction there is type III and potentially supersingular (j ≡ 1728, 4547 ≡ 3 mod 4).<br>– **a ≤ 8** by the derived lemma (Pasten §10 method + CNS 6.12(c) + ARS Thm 3.6(a) + intersection theory on the Γ₀(N) ∩ Γ₁(5) regular model at 2).<br>– c_E \| 2c₀.<br>Hence **c_E ≤ 512**. | PUB-R (4547) + **DER** (2-part) | 4547 check report; Manin gate report §2–3, §6 (referee), §8 (operator acceptance); `referee/` | 4547: two published restatements (both co-authored by Česnavičius). 2-part: independent referee PASS_WITH_CORRECTIONS plus operator reconstruction of Steps A and B |
| **N9 A2** | a₂(L₅) ≡ 152 ≡ **2 (mod 5)**, unconditionally, since 512 < 3 999. | from N6 + N7 + N8 | Manin gate §4, §8 | — |
| **N10 ORD** | ord_T L₅ ≥ 2: f_E has order ≥ r = 2 by SW Thm 6.1 with Kato (N4). a₂ ≢ 0 then gives ord_T L₅ = 2, and L₅* = a₂ is a 5-adic unit. | PUB | SW gate Phase C | — |
| **N11 SHA5** | By SW Thm 6.1 (the upper-bound direction: Kato + Schneider/Perrin-Riou), #Sha(E/Q)(5) ≤ 5^{b₅}, where b₅ = ord₅ L₅* − ord₅ ε₅ − Σ ord₅ c_v − ord₅ Reg_γ = 0. So **Sha(E/Q)[5^∞] = 0**. | PUB | SW gate "specialised bound"; Manin gate §8 | — |

## 3. What the proof does not use

- the Manin conjecture;
- the p-adic BSD conjecture;
- Skinner–Urban or any converse theorem;
- class groups or degree-24 fields;
- Wuthrich 2018 Prop. 1 as printed (its last line misplaces c₀; see memory `wuthrich-2018-prop1-manin-direction`).

## 4. Weakest links (a hostile audit should start here)

1. **N8, 2-part (DER).** No source states v₂(c₀) ≤ 8. Its inputs read only through secondary sources: Katz–Mazur 13.4.7, 13.5.6, 12.2.1 and 6.6.1 (via CNS); Liu 9.1.37 (sign checked by internal consistency); Deuring's mass formula (s = μ/12); Conrad's BDP17 Appendix B. ARS Thm 3.6(a) was read in the original by the operator's review, not locally.
2. **N8, 4547 (PUB-R).** Edixhoven [Edi91] is paywalled and was not read. The statement used is the one given in two published restatements by CNS and Česnavičius.
3. **N7 (CERT-NUM).** Correctness rests on the custom C code (`src/fastap.c`, `src/swstream.c`) and the certified truncation lemma (Deligne plus the Berkane–Bordellès–Ramaré divisor bound). Validation covered four curves and in-run spot checks. No second implementation has evaluated the seed's symbols end to end.
4. **N1 (PUB + EXACT).** Zywina's theorem is a 2025 arXiv preprint. The rank (= 2) is replayed by PARI's 2-descent. Sha[2] = 0 is taken from Zywina (ellrank's s = 0 is consistent with it).

## 5. Non-claims

- This is **not** full BSD for the seed.
- No ℓ-primary Sha statement is made for ℓ ∉ {2, 5}. (Sha[2^∞] = 0 follows from Zywina's Sha[2] = 0, but it is not part of this certificate's target.)
- The complex analytic rank is ≥ 2 only: L(E,1) = 0 by Kato/Kolyvagin since the rank is 2, and the root number is +1. Analytic rank exactly 2 is **not certified**.
- Nothing is claimed about other members of the fixed-prime family, C1, or C60.
- Nothing is claimed about the H9 bridge.

## 6. Files

- `BINDINGS.list` and `BINDINGS.sha256`: 23 upstream files, bound by sha256 at freeze time.
- `verify_bindings.sh`: recomputes the bindings from `~` and reports any drift.
- `replays/rank_replay.gp` and its output: PARI 2.17.3 (sage-env), under 10 CPU-s. It gives ellrank [2, 2, 0], the height regulator of ⟨P₁,P₂⟩ (17.7965…), torsion Z/2, and ellsaturation to 50 with an index-1 basis.
