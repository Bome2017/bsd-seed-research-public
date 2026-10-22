# STEIN_WUTHRICH_P5_GATE_001 — report (2026-09-18)

**Return: SW_REGULATOR_DONE_LP_FEASIBLE.**
- The 5-adic regulator is computed, and **Reg_γ is a 5-adic unit** (ord₅ Reg₅ = 2).
- The only missing input is the T² coefficient of L₅(E, T) modulo 5. By SW Prop. 3.5 it is fixed by twelve plus modular symbols, the distinct values of [a/25]⁺ and [a/5]⁺.
- A numerical computation of them costs about 3·10⁹ Fourier terms, estimated at about 3.4 CPU-hours with PARI's `ellap`. That is far above this gate's 300 CPU-s / 4 GiB cap, so **the Lp computation was not run.** The installed Sage code cannot run it at this size.
- Total compute here was under 20 CPU-s.

**Seed.** (m, n) = (2243, 12), A = 4547, B = 5843, E: y² = x³ − 5Ax² + 4ABx, N = 6 503 188 012 738 584.

**Sources.**
- Stein–Wuthrich, Math. Comp. 2013 ("SW"): `src/SteinWuthrich2013_shark.txt`, identical to the H9-lane copy (sha256 `680283f8…`).
- Wuthrich, *Numerical modular symbols for elliptic curves*, Math. Comp. 87 (2018), arXiv:1608.06423: `src/Wuthrich2018*` (sha256 `bb53ae8e…`).

## Phase A — the formula (verified; no computation)

**Algorithm 11.1 hypotheses (SW §11).**
- p = 5 > 2. ✓
- E is not additive at 5 (good reduction). ✓
- ρ̄₅ = GL₂(F₅) (retained ALL_ODD_RESIDUAL_IMAGE_VERIFIED; ψ₅ irreducible and a Tate transvection at m). ✓

**Kato's divisibility (SW Thm 7.3)** needs semistable reduction at p and ρ₅ surjective. For p ≥ 5, ρ₅ is surjective iff ρ̄₅ is (SW Prop. 7.2). So f_E(T) | L₅(E, T) in Λ.

**Index lemma.**
- Let H = ⟨P₁, P₂⟩ and I = [E(Q)/tors : H]. For the bilinear p-adic height pairing, Reg₅(H) = I²·Reg₅(E(Q)).
- E(Q)/5E(Q) = ⟨P₁, P₂⟩ (merged SMALL_SEED_FIXED_PRIME_FAMILY_VERIFIED; the torsion Z/2 dies mod 5), so 5 ∤ I.
- Hence ord₅ Reg₅(H) = ord₅ Reg₅(E(Q)). Step 1 of Algorithm 11.1 (the full Mordell–Weil group) is therefore not needed for the 5-adic bound.

**Specialised bound.**
- SW's Step 4 bound is b₅ = ord₅ L*₅ − ord₅ ε₅ − Σ ord₅ c_v − ord₅ Reg_γ.
- For this seed:
  - ε₅ = (1 − 1/α)² is a unit: α ≡ a₅ ≡ 3 (mod 5), so 1 − 1/α ≡ 4.
  - Σ ord₅ c_v = 0 (Tamagawa product 16).
  - #E(Q)(5) = 1.
  - Reg_γ = Reg₅/log₅(6)², with ord₅ log₅(6) = 1.
- So

      b₅ = ord₅ L*₅(E, 0) − ord₅ Reg₅ + 2,     #Sha(E/Q)(5) ≤ 5^{b₅},

  valid once Step 3 shows ord_T L₅ = 2.
- Only the proved upper-bound direction is used: Kato, plus Schneider / Perrin-Riou (SW Thm 6.1). No p-adic BSD.

## Phase B — regulator (`runs/phaseB_regulator.gp`, PARI 2.17.4, 0.08 CPU-s, 8 MB)

**Normalization check.** On 446d1 at p = 5, PARI's `ellpadicregulator` equals SW's published value (their eq. 4.2) to within a factor 1 + O(5⁷). So PARI's normalization is SW's.

**The seed.**

    Reg₅(⟨P₁,P₂⟩) = 5² + 2·5⁴ + 3·5⁵ + 3·5⁷ + 3·5⁸ + 4·5⁹ + … + O(5²⁶),    ord₅ = 2,

- The value is stable at precisions 5⁶, 5¹² and 5²⁴.
- It is nonzero, so the 5-adic height pairing is **nondegenerate** (SW Conjecture 4.1 holds here).
- **ord₅ Reg_γ = 0.** Hence b₅ = ord₅ L*₅(E, 0), and **Sha(E/Q)[5^∞] = 0 as soon as L*₅ is a 5-adic unit.**

## Phase C — minimal L₅ precision and exactly which symbols

**Order of vanishing.** ord_T L₅ ≥ 2 holds automatically: f_E divides L₅ and has order ≥ r = 2 (SW Thm 6.1). So a₀ = a₁ = 0, and **L*₅ = a₂** (the T² coefficient) whenever a₂ ≠ 0. We need a₂ mod 5.

**Depth.** SW Prop. 3.5: ord₅(a₂ − a_{n,2}) ≥ e_{n−1,2} − c, with e_{n−1,2} = n − 1 for p = 5.
- The denominators of the unitary plus symbols divide 2·c₀, which is prime to 5. This is Wuthrich Prop. 1: for unitary r, 2·#E(Q)_tors·[r]⁺/(c₀·c∞(E)) ∈ Z, with #E(Q)_tors = 2 and c∞(E) = 2.
- For c₀ this uses Mazur's result (5 ∤ c₀ since 5² ∤ 4N) and E[5] irreducible (every isogeny in the class has degree prime to 5). Hence c = 0.
- So **n = 2 suffices**: a₂ ≡ a_{2,2} (mod 5).

**The symbols.**

    P₂(T) = Σ_{a=1}^{4} Σ_{j=0}^{4} μ(ω(a)·6^j + 25Z₅)·(1+T)^j,   μ(b + 25Z₅) = α⁻²[b/25]⁺ − α⁻³[b/5]⁺,
    a_{2,2} = Σ_{a,j} μ(ω(a)6^j + 25Z₅)·C(j,2).

- The residues ω(a)·6^j run over all 20 units mod 25.
- Plus symbols are even. So the input is **10 values [b/25]⁺ and 2 values [b/5]⁺** (with [0]⁺ = 0 since the rank is 2), and α mod 25.
- These are needed only modulo 5 in Z₍₅₎. Their denominators are prime to 5.

## Phase D — numerical modular symbols: feasible, not within this cap (not executed)

**Wuthrich Theorem 12 applies.**
- The cusps a/5 and a/25 are unitary, since gcd(25, N) = 1.
- gcd(25, δ) = 1, where δ = 2A = 9094 and δ² is the largest square dividing N. Theorem 12 also assumes Manin's c₀ = 1 for non-semistable curves; only 5 ∤ c₀ matters here, see Phase C.
- All [a/m]^± for fixed m cost about m√Q terms, with Q = N here.
- His 234446a1 example gives 2 923 terms for m = 5 and 17 716 for m = 25 at √N ≈ 484, i.e. about 1.2·m√N and 1.46·m√N.

**Estimate for this seed** (`runs/phaseD_probe.gp`, 7.7 CPU-s):

| quantity | value |
|---|---|
| √N | 8.064·10⁷ |
| terms for m = 5 / m = 25 | about 4.8·10⁸ / **2.9·10⁹** |
| primes below 2.9·10⁹ | about 1.35·10⁸ |
| PARI `ellap` near 10⁹ / 3·10⁹ | 82 μs / 105 μs per prime |
| a_p for all p ≤ 2.9·10⁹ | about **1.2·10⁴ CPU-s ≈ 3.4 CPU-hours** (dominant) |
| composite aₙ and the partial sums | about 3·10⁹ multiply-adds, under 1 CPU-minute in compiled code |
| memory (streaming) | under 1 GB (segmented aₙ, a_p table as int32 about 0.5 GB) |
| precision | Ω ≈ 0.02804 and 0.03056i (rectangular, c∞ = 2), not small; double precision with compensated summation looks adequate, but it must be checked against Wuthrich's Lemma 6 |

**Local implementation.** SageMath (python 3.13) ships Wuthrich's `sage/schemes/elliptic_curves/mod_sym_num.pyx`. It **cannot** run at this size:
- `_add_an_coefficients(self, int T)` takes a C `int`, which overflows past 2³¹ ≈ 2.1·10⁹.
- It keeps `int _ans[]` and `double _ans_num[]` arrays, 12 bytes per coefficient (about 35 GB), filled from a full aₙ list; bulk PARI `ellan` measured about 27.6 bytes per coefficient.
- The machine has 16 GB of RAM.
- A **streaming adaptation** of Wuthrich's partial-sum method is required: accumulate S_b = Σ_{n≡b (25)} aₙ/n·e^{−2πn y} while generating aₙ in segments, then take the character or FFT step.

**Decision.** The estimate is about 40× the 300 CPU-s cap and needs new code, so **Lp was not run** (per the task's rule). The work is embarrassingly parallel over prime ranges: about 11 minutes of wall time on this machine's 20 cores, if the one-process rule were relaxed.

## What a run would decide

- **Positive direction** (Kato and SW only): if a₂ ≢ 0 (mod 5), then ord_T L₅ = 2, L*₅ is a unit, b₅ = 0, and **Sha(E/Q)[5^∞] = 0** for the seed.
- **Negative direction** (remark only; not needed for the positive conclusion). Skinner–Urban, as quoted in SW Thm 7.5, would make the test an equivalence: good ordinary, ρ₅ surjective, and multiplicative q = m with ρ̄₅ ramified since v_m(Δ) = 1. Then a₂ ≡ 0 (mod 5) would mean Sha[5] ≠ 0. That use of Skinner–Urban must be checked against its original hypotheses before being relied on.
- **Validation before a real run.** Reproduce known values with the streaming code:
  - Wuthrich's 234446a1, where the fourth coefficient of L₅ is ≡ 1 (mod 5);
  - SW's 446d1 series at p = 5;
  - 389a1 at p = 5.

  Also check [0]⁺ = 0 for the seed.

## Return

    SW_REGULATOR_DONE_LP_FEASIBLE
      Reg_5(<P1,P2>) = 5^2 + 2*5^4 + ... (ord 2, nondegenerate; PARI = SW normalization, checked on 446d1); ord_5 Reg_gamma = 0
      b_5 = ord_5 L_5*(E,0); Sha[5^inf] = 0  <=  a_2 (T^2 coefficient) is a 5-adic unit   (Kato + SW Thm 6.1 only)
      needed: a_2 mod 5 = T^2 coefficient of P_2 (SW Prop 3.5, c = 0): [b/25]^+ (10 distinct), [b/5]^+ (2 distinct), alpha mod 25
      cost: about 2.9e9 Fourier terms (Wuthrich Thm 12, m = 25), about 3.4 CPU-h (a_p-bound), <1 GB streaming; stock Sage mod_sym_num
            unusable at this T (C-int overflow past 2^31, 12 B/coefficient + full a_n list); NOT executed (cap 300 CPU-s / 4 GiB)

**Non-claims.** No p-adic BSD is assumed. No Sha statement is made yet. Full 5-descent and the degree-24 class groups were not reopened.

## Proposed ledger block (not merged; needs operator acceptance)

```
STEIN_WUTHRICH_P5_GATE_001 (seed (2243,12)) — SW_REGULATOR_DONE_LP_FEASIBLE (2026-09-18)
  SW Algorithm 11.1 hypotheses hold at p = 5 (good ordinary, rho-bar_5 = GL2(F5)); Kato Thm 7.3 applies (semistable at 5, rho_5 surjective).
  Index lemma: Reg_5(<P1,P2>) = I^2 Reg_5(E(Q)) with 5 not dividing I (E(Q)/5 = <P1,P2>), so the full Mordell-Weil group is not needed.
  Reg_5(<P1,P2>) = 5^2 + 2*5^4 + 3*5^5 + ... + O(5^26): ord 2, nondegenerate. PARI normalization = SW (446d1 value reproduced to O(5^7)).
  ord_5 Reg_gamma = 0; epsilon_5, Tamagawa (16), torsion are 5-units => b_5 = ord_5 L_5*(E,0). Hence Sha(E/Q)[5^inf] = 0 follows if the
  T^2 coefficient a_2 of L_5(E,T) is a 5-adic unit (ord_T >= 2 is automatic). By SW Prop 3.5 with c = 0, a_2 mod 5 = T^2 coefficient
  of P_2: needs [b/25]^+ (10 distinct) and [b/5]^+ (2 distinct) — unitary cusps (gcd(25,N) = 1, gcd(25,2A) = 1).
  Wuthrich Thm 12 cost: about 1.46*25*sqrt(N) = 2.9e9 Fourier terms; PARI ellap 82-105 us/prime => about 3.4 CPU-h, <1 GB streaming.
  Stock Sage mod_sym_num cannot run it (C-int T overflow, about 35 GB of arrays). Not executed (cap 300 CPU-s / 4 GiB). No Sha claim yet.
```

Files:
- `runs/phaseB_regulator.gp` and `phaseB_output.txt`;
- `runs/phaseD_probe.gp` and `phaseD_probe_output.txt`;
- `src/` (SW, Wuthrich);
- `MANIFEST.sha256`.

## Addendum (operator review, 2026-09-18): six-symbol simplification; Manin-constant identification caveat

**Six-symbol formula (operator-supplied, independently re-derived here).**
- For fixed a, 6^j ≡ 1 (mod 5) and Σ_{j=0}^{4} C(j,2) = 10 ≡ 0. So the α⁻³[b/5]⁺ part of a_{2,2} vanishes mod 5.
- Teichmüller lifts mod 25 are 1, 7, 18, 24, and 6^j ≡ 1, 6, 11, 16, 21. Folding by [b]⁺ = [25−b]⁺:
  - the j = 2 terms give 2([2] + [11]);
  - the j = 3 terms give 6([9] + [12]);
  - the j = 4 terms give 2([3] + [4]).
- α ≡ 13 (mod 25), so α⁻² ≡ 4 (mod 5). Hence

      a₂ ≡ 3([2/25]⁺ + [3/25]⁺ + [4/25]⁺ + [11/25]⁺) + 4([9/25]⁺ + [12/25]⁺)   (mod 5).

- Only six denominator-25 plus symbols are needed.

**Rigor note: normalization versus identification.**
- (i) Every cusp b/25 is Γ₀(N)-equivalent to 0, and λ(0) = L(E,1) = 0. The latter holds because rank 2 and Kolyvagin exclude L(E,1) ≠ 0. So λ(b/25) lies in the period lattice Λ_f of f, with no torsion denominators.
- (ii) Mazur (p | c ⇒ p² | 4N) and Abbes–Ullmo (p | c ⇒ p | N), as quoted in Agashe–Ribet–Stein Thms 2.3 and 2.5, give c₀ = 2^a·4547^b. In particular **5 ∤ c₀**, so every normalization in play differs from the Néron one by a 5-unit, and the mod-5 bit is normalization-independent.
- (iii) Recovering the exact rational values [b/25]⁺ from floating-point data needs an a priori **denominator bound**: they lie in (1/(2c_E))Z. No published theorem bounds a or b.
  - Edixhoven's claim that only 2, 3, 5, 7 can divide c, with uniform valuation bounds, is unpublished.
  - Česnavičius–Neururer–Saha prove c | deg φ, which is not computable at this N.
- A certified error ε therefore certifies the identification only for c_E < ω₁/(8ε). A favourable bit is recorded as proving Sha[5^∞] = 0 **provided the Manin constant is below that explicit threshold**. Manin's conjecture (c₀ = 1), proved for semistable curves and verified for all optimal curves of conductor < 500 000, would make it unconditional.
