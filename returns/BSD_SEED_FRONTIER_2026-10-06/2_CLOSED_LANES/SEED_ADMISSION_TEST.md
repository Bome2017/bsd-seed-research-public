# Seed-admission test, W3 and Heegner/Kolyvagin: RESULT

Claude (Opus 5.5), 2026-10-06. Paper only; no primewise computation; $0. Assignment: Pro's "SEED-ADMISSION TEST", relayed by the user.

**Verdict: `NO_SEED_OBJECT_IDENTIFIED`.** Neither lane produces a prime-independent integral object I_E with a proved mechanism Ш(E/ℚ)[p] ≠ 0 ⇒ p | I_E for all good p outside an explicit finite set. This negative is scoped to the candidates examined below; it is not an impossibility theorem.

## 0. Checks of the 10-06 Codex review this rests on

| Claim (Codex review, `~/BSD_HEEGNER_JET_RETURN_REVIEW_CODEX_2026-10-06/REPORT.md`) | My check |
|---|---|
| ℓ₂ ≡ 2 (mod 5) from the certified m = 5, 25 seed symbols | **Confirmed independently.** My own code (`checks/ell_check.py`, built from the XB rational candidates) gives (ℓ₀, ℓ₁, ℓ₂, ℓ₃) ≡ (0, 0, 2, 0) mod 5 with both the full measure and the level-p² term alone. The 09-19 certificate `evidence/P5_DOWNSTREAM.txt` records the same value as a₂,₂ ≡ 2. |
| The level-p correction cancels in ℓᵢ mod p for i ≤ p−2 | **Confirmed by proof.** For a = b + pj, ω(a) = ω(b) and log⟨a⟩ ≡ log⟨b⟩ + pj/b (mod p²), so u(a) = u₀ + j/b runs over all of F_p. Then Σⱼ C(u(a), i) = C(p, i+1) ≡ 0, and [a/p]⁺ is constant on each fibre. Also checked on the p = 5 fibres. |
| The W3 λ-multipliers replay byte-for-byte | Reported by Codex (re-ran `cert_seed.py`). I did not re-run it. |
| Heegner: on the cofinite ordinary domain ν_p = 1 + s_p, so ν_p ≤ 2 ⟺ ν_p = 1 ⟺ Ш(E/ℚ)[p] = 0 | **Confirmed by re-derivation.** Zhang, Lemma 8.4: the larger eigenspace has dimension ν+1 and the smaller has dimension ≤ ν. The + side is Sel_p(E/ℚ), of dimension 2+s_p; the − side is Sel_p(E^{−23}/ℚ), of dimension 1+t_p. So ν_p + 1 = max(2+s_p, 1+t_p), and t_p = 0 off the finite support of Ш(E^{−23}). |

## 1. W3 lane (two-variable Hida jet a T² + b TS + c S², with b = −c)

**What the coefficients are.**
- c is a unit times ℓ₂(p), the S²-coefficient of the seed's weight-2 MTT p-adic L-function. ℓ₂(p) **is the existing cyclotomic depth-2 coefficient**: at p = 5 it is the 09-19 a₂,₂, and the A4 package formalized the same criterion at p = 5, 7, 11 and 13. W3's c-branch therefore adds nothing to the per-prime criterion already in use.
- W3's new content is the weight branch. The coefficient a is tied to Λ₂(p) (with Λ₁(p) and α₁) through the U₃₁ identity, where Λ(T) is the total mass of the Hida family symbol at {∞}−{0}.

| Candidate I_E | Independent of p? | Mechanism Ш[p] ≠ 0 ⇒ p ∣ I_E? | Status |
|---|---|---|---|
| ℓ₂(p) itself, as the reduction of a fixed integral object | No. It is computed from the MTT measure at level p², i.e. from twists of conductor N·p⁴. | Kato's divisibility gives Ш[p] ≠ 0 ⇒ ℓ₂(p) ≡ 0. The converse fails: ℓ₂(p) ≡ 0 also whenever the normalized cyclotomic p-adic regulator vanishes mod p. **The seed does this at p = 17**: Reg_γ = 17·13 + O(17²) (PARI and Sage agree), while Ш[17] = 0 (Ota singleton). A fixed I_E catching ℓ₂ ≡ 0 would make this regulator-degeneracy set finite. That is a Wieferich-type statement: unproved, and heuristically false, since Σ 1/p diverges. | **dead as I_E** |
| Λ₁(p), Λ₂(p), as reductions of a fixed object | No. They are Taylor coefficients of a Hida family through f at p, a different Λ-adic object for each p. | None. The four-node test fails only where a ≡ b ≡ c ≡ 0, i.e. where the whole quadratic jet (a two-variable regulator form) vanishes mod p. That is two conditions, so heuristically only finitely many failures (Σ 1/p² converges). This is W3's real attraction. **No theorem turns the heuristic into an object.** | no object |
| Congruence number η_f / modular degree (the integers behind the "cofinite Hida domain" p ∤ D) | Yes | "Ш[p] ≠ 0 ⇒ p ∣ η" is **false in general**: the 10-01 invisible-Ш test bank has 32 strong counterexamples at p ≥ 5. So it cannot come from a general theorem. | dead as a general route |
| #Ш (the p-independent factor of the p-adic leading term) | Yes | Circular: it presupposes FIN and the leading-term formula. | circular |

**Remaining input:** a proof that the seed's two-variable p-adic regulator form is nonzero mod p for cofinitely many p, or a p-independent object controlling it. Neither is in the record.

## 2. Heegner/Kolyvagin lane (K = ℚ(√−23))

The target is **an equivalence**: ν_p = 1 ⟺ Ш(E/ℚ)[p] = 0 on the cofinite ordinary domain (§0). That is shape 4, a restatement, not a reduction.

| Candidate I_E | Independent of p? | Mechanism? | Status |
|---|---|---|---|
| The Heegner index [E(K) : ℤ y_K] (the rank-one I_E of Kolyvagin) | Yes | **The index is infinite.** y_K is torsion because ord L(E/K, s) = 3. The same holds for every K satisfying the Heegner hypothesis: ord ≥ 3 because L(E, s) already vanishes to order 2. | none exists in any K |
| The content of the derived classes κ_ℓ | No. They need ℓ inert with p ∣ ℓ+1 and p ∣ a_ℓ. A fixed finite set of ℓ serves only the finitely many p dividing gcd(ℓ+1, a_ℓ). | — | auxiliary primes p-dependent by construction |
| Darmon's refined (Mazur–Tate-type) Heegner conjecture: θ_n ∈ I^r, with leading term #Ш × (derived regulator) | Only the #Ш factor | The derived regulator lies in the p-dependent group G_n ⊗ ℤ_p. This is the same regulator-type obstruction as W3, and the #Ш factor is circular. | circular |
| A higher Heegner cycle with a height formula for L″ (a number-field Yun–Zhang analog) | Yes | It would be the right object, but no such theorem exists over number fields (record: Q36 blocker T2). | missing |

**Remaining input:** control of the genuine derived classes mod p for cofinitely many p through a p-independent mechanism. Nothing in the record provides it. The finite-batch Chebotarev results give only the existence of eligible auxiliary primes.

## 3. Where a p-independent object could live

The ranks 0 and 1 template (Gross–Zagier + Kolyvagin) is the only known source of a prime-independent I_E. There, the Heegner index is tied by GZ to the archimedean leading term. For the seed:
- the only p-independent integral quantity of the right shape on record is the **archimedean leading term q = L″(E,1)/(2ΩReg)**. It is pinned to a rigorous interval around 36; its rationality is open.
- If q = 36, then q·tors²/Tam = 9 is the natural I_E.
- The missing mechanism, "Ш[p] ≠ 0 ⇒ p ∣ 9 cofinitely", is a rank-2 Gross–Zagier–Kolyvagin analog. Both halves are absent: a height formula for L″, and a descent bound from that object.
- This is **the same missing object as Q36's blocker T2**. Pro's fallback ("Q36 or a genuinely different global-support construction") is consistent with this.

## 4. The p = 31 relay (second Pro message)

Its premise is false. **p = 31 is already settled:** Ota singleton at ℓ = 311, c₂ = 330990 ≡ 3 (mod 31), Codex Batch C PASS (map §4.2). In addition:
- **W3's c-branch at 31 is the existing cyclotomic criterion.** ℓ₂(31) would be a second certificate for an already-proved fact. Endpoint effect: none.
- **The cost does not fit the machine.** The m = 961 table needs a 20,340-segment corpus; 6,445 segments exist. At the Stage-W rate (38 CPU-h and about 32 GB per 1,643 segments), the remaining ~13,900 segments come to about 320 CPU-h and about 270 GB. Free disk is 110 GB against an 80 GB floor.
- **Aggregation into one functional does not lower the coefficient cutoff.** w(a) = C(u(a), 2) depends only on the wild part of a. So its Fourier support is the trivial character (whose term vanishes, since L(E,1) = 0) plus the p−1 characters of order p, of conductor p². Each twisted value L(E, ψ, 1) needs about p²√N ≈ 7.7·10¹⁰ coefficients before safety factors. Aggregation saves separate evaluations, not corpus.
- The only prime where a W3 computation would test something new is one where ℓ₂ ≡ 0. On the seed that is **p = 17** (also settled). There the weight branch Λ₂ would have to carry the test, and no construction produces Λ₂.

Per the standing rule (per-prime runs only on "run it anyway"), neither 31 nor 17 was started.

FIN, ORDER9 and Q36 are unchanged.
