# Summary of changes for run be7a0018-356f-4d28-9163-900886aa5a94
I ran the W3 experiment you asked for on the actual seed, `[0,-22735,0,106272484,0]`. At p=17 the weight-two quadratic criterion fails: ℓ₂ ≡ 0 mod 17, so this calibration is negative. I then ran p=19, where it succeeds: ℓ₂ ≡ 18 mod 19. On the Heegner side, the "ν_p ≤ 2" target turns out to restate the original problem for all but finitely many primes. Write-ups are in `W3_P17_REPORT.md` and `HEEGNER_NU_NOTE.md`; code and data are in `w3_p17/`.

**The evaluator.** The frozen `arbcore msl` engine isn't in this project, so I wrote an equivalent one (`w3_p17/msl_sq.c`) that works for composite denominators like m = p².
- **Formula:** matches exact modular symbols on 11a1, 37a1 and 389a1 at m = 5, 7, 9, 25, 49, to within 3·10⁻¹⁴.
- **Point counts a_p:** each value is accepted only if it is the unique group order consistent with every tested point, then re-verified by explicit scalar multiplication. There were no failures across about 5.7·10⁹ point counts.
- **Check against your receipt:** in the same pass as m=289, it recomputed `[a/103]^+`. All 102 values equal the integers in `retained/P17_MSL.txt`, using the same Ω⁺.
- **Caveat:** the arithmetic is floating point, not arb-certified. The tail is estimated, not bounded with interval arithmetic.

**p = 17 (a₁₇ = −6, ordinary).** The m=289 pass used T = 5.8·10¹⁰ and took 1.9 h on 8 cores. All 288 symbols are within 1.1·10⁻⁶ of integers, and their gcd is 1. The Hecke U₁₇ relation linking the level-17 and level-289 sums holds in all 16 classes.
- ℓ₀..ℓ₄ mod 17 = 0, 0, 0, 0, 13, so μ = 0 and λ = 4.
- Since Ш(E/ℚ)[17] = 0 is already known, the vanishing of ℓ₂ points to the normalised 17-adic regulator being divisible by 17. This step relies on standard imported theorems (Kato's divisibility and the p-adic leading-term formula, plus the main conjecture).
- So W3 at 17 can't be decided from weight-two data. Of the three jet coefficients, c ≡ 0 and b = −c ≡ 0, leaving only the coefficient tied to Λ₂, which is still unknown.
- **Heuristic warning:** if ℓ₂ mod p behaves like a random residue, it should vanish at infinitely many primes. A cofinite bound built on ℓ₂ ≢ 0 should not be expected to hold.

**p = 19 (a₁₉ = 4).** This run used T = 7.3·10¹⁰ and took 2.4 h. All checks pass. ℓ₀, ℓ₁, ℓ₂ mod 19 = 0, 0, 18, so λ = 2.
- ρ̄₁₉ is surjective by Serre's criterion, checked with explicit Frobenius witnesses. The same check also gives surjectivity at 17 and 53.
- Through the imported theorems, this gives Ш(E/ℚ)[19] = 0 independently of the receipt route.
- Under the W3 imports (which include the unverified Hida-domain condition), some W3 node value is nonzero mod 19³.

**Lean (builds; no `sorry`; standard axioms only).**
- `Seed17.ell_low_mod17`, `Seed17.distribution_relation`, `Seed19.ell_low_mod19`, `Seed19.distribution_relation`. These check the mod-p arithmetic and the Hecke relation on the computed integer tables. They do not check the analytic computation that produced the integers.
- `Heegner.nu_succ_eq_max`, `nu_le_two_iff`, `nu_le_two_iff_of_rm_eq_one` (in `RequestProject/KolyvaginVanishingOrder.lean`). From Zhang's Lemma 8.4 with ε = +1 and dim Sel⁺ ≥ 2, they prove ν_p + 1 = max(dim Sel⁺, dim Sel⁻), and ν_p ≤ 2 ⟺ (dim Sel⁺ = 2 and dim Sel⁻ ≤ 3). If dim Sel⁻ = 1, then ν_p ≤ 2 forces ν_p = 1.

**Heegner conclusions.**
- Your p=53 correction holds up against the curve:
  - Δ = 2⁸·3²·2243·4547³·5843², and all five bad primes split in ℚ(√−23).
  - 53 divides none of ord_q Δ at the three multiplicative primes, so ρ̄₅₃ is ramified there.
  - H¹(ℚ_ℓ, E[53]) = 0 at the additive primes 2 and 4547.
  - 3391 is a valid Kolyvagin prime: 3391 ≡ −1 mod 53, a₃₃₉₁ = 0, and it is inert.
- I computed L′(E^(−23), 1) = 39.8472780641 numerically, confirmed by a functional-equation check to 7·10⁻¹². By Gross–Zagier–Kolyvagin, E^(−23) then has rank 1 and finite Ш, so dim Sel⁻ = 1 for all but finitely many p.
- Combined with the Lean results, for all but finitely many p: ν_p ≤ 2 ⟺ ν_p = 1 ⟺ Ш(E/ℚ)[p] = 0. A nonzero two-prime class is still a valid certificate at a single prime, but as a cofinite target ν_p ≤ 2 restates the original problem.
- Since ν_p is a function of the Selmer ranks, any uniform ν-bound *is* a Selmer bound. A mechanism that avoids assuming a Selmer bound has to come from explicit nonzero classes or from uniform indivisibility of c(ℓ).
- **Not done:** the value of c(3391) mod 53. It needs Heegner points over a ring class field of degree 10176 for a curve of conductor 6.5·10¹⁵, which is out of reach here.

The report also gives estimated running times for larger primes (for example about 9 h at p=31 and 29 h at p=53 on 8 cores).

# Summary of changes for run 4e7dc730-d90e-478b-a05b-50c08d5cb5d7
**Status: SPECIFIC_OBSTRUCTION.** I built and attempted the sparse construction concretely at p=31, but it did not produce an authenticated seed source value. Two smaller results came out of it. Full write-up: `W3_SOURCE_REPORT.md`; runnable code: `w3_source/`.

**Corrections adopted.**
- A dual certificate for one functional does not need global congruence-freeness. I withdrew my earlier remark suggesting it did.
- When gcd(31,N)=1, the cusp a/31 is Γ0(N)-equivalent to 0, not to ∞. The code never uses cusp equivalence; it breaks every path into explicit cosets.
- The size of the full presentation is not used as a lower bound.
- The elimination now records explicit multipliers λ. Every identity is rebuilt from scratch and re-checked column by column.

**What I built (seed level 31N, actual data a₅=a₇=−2, α₀=57776 mod 31⁴, ten-slot jet module).**
- **Equivariance and characters.** I derived the rule Ξ(γD)=σ(γ)₊Ξ(D) from the classical integral. It forces the character ω(d)^(−w), so weight 5 carries ω⁻³ and weight 6 carries ω⁻⁴; both are kept throughout.
- **Rows.** I implemented the actual relation rows (S, τ) and Hecke rows (T₅, U₃₁).
- **Validation.** I tested this code on a genuine 31-stabilised symbol of 389a1 at level 389·31, not on the seed. The S, τ, T₅ and U₃₁ rows held on 40 random cosets, and a deliberately wrong eigenvalue was rejected.
- **Target functionals.** All four V₍w,s₎ are written as exact rows mod 31⁴ over 74 named cosets.
- **First-order system.** I recorded the right-hand side of the first-order lift at one coset, keeping the eigenvalue derivative b₅ as an unknown.

**Certificates.**
- **Order 0 (closed).** A single U₃₁ row at the coset of {0,∞} gives V ≡ ±(α₀−1)·Ξ₀({∞,0}) mod 31 at all four nodes, with recombination verified. Since rank ≥ 2 forces L(E,1)=0, and given the retained source identification, this proves all four V vanish mod 31. That digit was already forced; this is a sparse proof of it, not a bound.
- **Order 1 (fails at the chosen support).** With 2072 rows, exactly one first-order column remains: the (1,0) slot at the {0,∞} coset (Λ₁ below). The U₃₁ eigenvalue derivative appears only multiplied by Ξ₀({∞,0})=0, so it drops out; b₅ does not survive either.
- **Order 2.** The only remaining second-order column is Λ₂. Also left are α₁Λ₁, a term in α₂ that vanishes, and lower-order terms kept as the right-hand side.
- **Divisor-level form (checked).** These residuals reduce to one Λ-adic function, Λ(T), the total mass of the family symbol at the single divisor {∞}−{0}.
- **Small-level calibration.** On levels 389 and 3023, ball-shaped certificates appeared only once the support covered essentially the whole coset space. This is evidence about this construction, not a theorem about sparse methods.

**Missing inputs, stated exactly.** No values were inserted.
- The seed's weight-two plus symbol on 3608 Manin symbols of level N. I tried to acquire these, but neither standard route can be run here; that is a resource statement, not an impossibility.
- Λ₂ mod 31, which none of the constructions tried here produces.

**Partial result.**
- **Proved in Lean, no `sorry`, standard axioms only:** `W3.quadratic_jet_forcing` in `RequestProject/QuadraticJetForcing.lean`. If all four node values vanish mod p³, then p divides each coefficient of the quadratic jet. It holds for every prime, because the node matrix contains a determinant-1 minor after one row operation.
- **Conditional reduction.** I tie the S²-coefficient to ℓ₂, the corresponding coefficient of the seed's weight-two p-adic L-function. This rests on retained inputs, including the Hida-domain condition at 31, which remains unverified. ℓ₂ mod 31 is a finite weight-two formula, calibrated on 11a1, 37a1 and 389a1.
- **What this removes.** Under those inputs, the mod-p³ layer of W3 at 31 no longer needs the weight-5/6 symbols. It needs only weight-two seed data plus Λ₁ and Λ₂.

No uniform-in-p bound was obtained. FIN, ORDER9 and Q36 are unchanged.