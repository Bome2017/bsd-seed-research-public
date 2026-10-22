# SHA5_RIGOROUS_THEOREM: Sha(E/Q)[5^∞] = 0 for the seed, with a proof-grade p = 5 numerical node

**Curve.** E : y² = x³ − 22735x² + 106272484x (Zywina's (m, n) = (2243, 12); A = 4547, B = 5843).

## Theorem

> **Sha(E/Q)[5^∞] = 0.**

**Label.** PROVED (computer-assisted).
- This is the same theorem and the same proof chain as the frozen master certificate (`~/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md`, status `SMALL_SEED_2243_12_SHA5 = PROVED_ZERO`, via the derived v₂(c₀) ≤ 8 lemma).
- **One change:** the evidence for node **N7** is upgraded from **CERT-NUM** (the LP5 double-precision stream) to a **proof-grade computer-assisted** certificate (`P5_CERTIFICATE.md`): Arb ball enclosures with every a_q proved by the independent verifier.
- Every other node and its label is unchanged.
- The frozen certificate is not edited; this file is a successor, and nothing is merged.

## 1. The chain (master certificate nodes; only N7 is replaced)

| node | claim | type | status here |
|---|---|---|---|
| N0 CURVE | model, N, local types, a₅ = −2, #E(F₅) = 8, E(Q)_tors = Z/2 | EXACT | unchanged (a₅ = −2 re-read from this run's verified a_q file) |
| N1 MW | E(Q) ≅ Z/2 × Z² (Zywina Thm 1.2, with an ellrank replay) | PUB + EXACT | unchanged |
| N2 SAT5 | 5 ∤ [E(Q)/tors : ⟨P₁,P₂⟩] | EXACT | unchanged |
| N3 IMG5 | ρ̄₅(G_Q) = GL₂(F₅), hence ρ₅ surjective | EXACT + PUB | unchanged |
| N4 KATO | f_E(T) ∣ L₅(E,T) in Λ (SW Thm 7.3; Kato) | PUB | unchanged |
| N5 REG | ord₅ Reg_γ = 0; ε₅ a unit; ∏c_v = 16 and #E(Q)(5) = 1 | EXACT + PUB | unchanged, including the model-independence of ADDENDUM_001/002 (only ord₅ Reg₅ = 2 is used) |
| N6 SW FORMULA | a₂ ≡ a_{2,2} (mod 5), SW Prop. 3.5 with c = 0 (5 ∤ c_E); six-symbol form 3([2]+[3]+[4]+[11]) + 4([9]+[12]) | PUB + algebra | unchanged; re-evaluated by two independent routes (§2) |
| **N7 NUMERICS** | the 20 symbols [b/25]⁺ **exactly**: (−54, 16, 90, −52, −76, 16, 76, −52, −54, 90, 90, −54, −52, 76, 16, −76, −52, 90, 16, −54) for b = 1..24, 5 ∤ b | **was CERT-NUM → now PROVED computer-assisted** | `P5_CERTIFICATE.md` §2–§3. Each symbol is enclosed in an Arb ball of radius < 1/2048 containing exactly one point of (1/1024)Z, which is an integer. The a_q come from 360 542 141 verified primes, root `fcd02437…`. The values equal the LP5 values |
| N8 MANIN | c_E ≤ 512 (c₀ = 2^a, a ≤ 8, 4547 ∤ c₀; c_E \| 2c₀) | PUB-R + DER | unchanged (theorem input for the lattice) |
| N9 A2 | a₂(L₅) ≡ 152 ≡ 2 (mod 5) in the ω₁ normalisation; ≡ 1 in the Néron normalisation; nonzero in every normalisation (5 ∤ c_E) | from N6 + N7 + N8 | **recomputed from the rigorous N7**: route A = route B = 2 (mod 5) |
| N10 ORD | ord_T L₅ ≥ 2 (Kato + SW Thm 6.1); with a₂ ≢ 0: ord_T L₅ = 2 and L₅* = a₂ is a 5-adic unit | PUB | unchanged; the forced a_{2,0} = 0 and a_{2,1} ≡ 0 (mod 5) are verified |
| N11 SHA5 | SW Thm 6.1 (Kato + Schneider/Perrin-Riou): #Sha(E/Q)(5) ≤ 5^{b₅}, b₅ = ord₅ L₅* − ord₅ ε₅ − Σ ord₅ c_v − ord₅ Reg_γ = 0 | PUB | unchanged: **Sha(E/Q)[5^∞] = 0** |

## 2. Inputs, by kind

**PROVED mathematical inputs:** N0, N2, N3 (exact computations), and the lattice statement "x_b ∈ (1/c_E)Z", derived as follows:
- every b/25 and b/5 is Γ₀(N)-equivalent to 0;
- λ(0) = L(E,1) = 0 (rank 2, Kolyvagin);
- c_E Λ_f ⊆ Λ_E, and Λ_E is rectangular.

**PROVED computer-assisted inputs:**
- **N7 (this run):** the 20 + 20 symbols at m = 25 and 4 + 4 at m = 5, with a₂ ≡ 2 (mod 5).
- Optional and not needed by the chain: ord_{s=1} L(E,s) = 2, with L″(E,1)/2 ∈ [35.929604, 35.941023] (`~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/ANALYTIC_RANK_CERTIFICATE.md`). This settles the master certificate's non-claim "Analytic rank exactly 2 is not certified".

**Published theorems** (the master certificate's list, unchanged):
- Kato's divisibility (SW Thm 7.3);
- SW Prop. 3.5 and Thm 6.1 (Schneider, Perrin-Riou);
- Zywina Thm 1.2 (arXiv preprint; rank independently replayed);
- Mazur / Abbes–Ullmo (via Agashe–Ribet–Stein) for 5 ∤ c₀;
- Edixhoven via published restatements (4547 ∤ c₀);
- the derived lemma v₂(c₀) ≤ 8 (DER, refereed);
- modularity.

**Not used:** the Manin conjecture, p-adic BSD, Skinner–Urban, Wuthrich 2018 Prop. 1 as printed.

**Purely consistency checks:**
- route C (LP5 equality);
- T₅ Hecke identities;
- symmetries;
- the (1/512)Z lattice;
- a_{2,0} = 0 and a_{2,1} ≡ 0 (mod 5);
- the cross-run byte equality with the p = 3 run's coefficient files;
- PARI `primepi`;
- the replays (`P5_REPLAY.md`).

## 3. Weakest links after this upgrade (compare master §4)

1. **N8, 2-part (DER):** unchanged. The derived lemma v₂(c₀) ≤ 8 has no source that states it.
2. **N8, 4547 (PUB-R):** unchanged. Edixhoven was read only through restatements.
3. **N7: resolved.** The master certificate listed "no second implementation has evaluated the seed's symbols end to end". A second, independent and rigorous implementation now has:
   - an Arb engine with an integer-only witness verifier, sharing no floating-point code with LP5's `swstream.c`;
   - it agrees with LP5 exactly on all 20 symbols.
4. **N1 (PUB + EXACT):** unchanged. Zywina's theorem is an arXiv preprint; the rank is replayed.

## 4. Related successor note (p = 3)

The p = 3 result `~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/SHA3_THEOREM.md` flagged that the p = 5 input to its corollary #Sha(E/Q)[30^∞] = 9 was CERT-NUM. **After this upgrade that qualifier no longer applies to the p = 5 node.** The corollary's p = 5 input now carries the same computational grade as its p = 3 part. The p = 3 file itself is not edited.
