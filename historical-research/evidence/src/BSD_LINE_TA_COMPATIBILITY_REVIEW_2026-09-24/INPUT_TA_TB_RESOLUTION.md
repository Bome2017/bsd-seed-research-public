# What the LINE tests T-a, T-b and T-c would actually test (local resolution, 2026-09-24)

**Verdict: `T_A_T_B_RECHECK_ONLY`. Do not fund these as LINE tests.**
- Neither T-a nor T-b can test LINE's cross-prime content (L2).
- The only non-retained content in either is the audit's open item (1b), whether m₅(Σ) is independent of Σ, plus the normalization.
- (1b) should be closed on paper.
- The only cross-prime test, T-c, tests Mazur–Tate's predicted *value*, not LINE.

This answers the reviewer's question: "what assertion would this test investigate that is not already supplied by the retained fixed-p theorem and the known 5-primary result?"

**Sources:**
- `~/BSD_SEED_2243_12_RANK2_GLOBAL_OBJECT_2026-09-18/RANK2_GLOBAL_OBJECT_COMPOSITION.md`: §4, §6.5, §6.7 and §9.
- `~/BSD_SEED_2243_12_LINE_HOSTILE_AUDIT_2026-09-19/LINE_HOSTILE_AUDIT.md`: items 1–3, C2, C5 and C7, and Theorem C′.
- `~/BSD_SEED_P13_RUN_2026-09-21/`: measured costs.

## 1. Exact statements (composition §6.7)

- **T-a.** At p = 5, the ratio θ̃_ℓ / (n_ℓ·det h_ℓ) mod 5 must agree, up to sign, at ℓ = 11, 61 and 71, where det h_ℓ = 2, 4, 1.
- **T-b.** The tame ratio at ℓ = 11 must agree with the completed cyclotomic L₅ run (a₂ ≡ 2, Reg_γ ≡ 21 mod 25).
- **T-c.** The residues of m at p = 5, 7, 11, 13 (using ℓ = 11, 29, 23, 53) must all have the form ±9·2^j for one j.

## 2. Regime (verified here, PARI 2.17.3)

| ℓ | #E(F_ℓ) | a_ℓ | E(F_ℓ) | 5 \| #E? | ℓ mod 5 |
|---|---|---|---|---|---|
| 11 | 14 | −2 | Z/14 | no | 1 |
| 61 | 74 | −12 | Z/74 | no | 1 |
| 71 | 74 | −2 | Z/74 | no | 1 |

- The reviewer's counts are correct.
- These ℓ are **regime A** by design (p ∤ n_ℓ, ℓ ≡ 1 mod p), not core pairs. Theorem C′ needs E(F_ℓ)[5^∞] ≅ Z/5^k.
- So T-a and T-b cannot bear on Theorem C′'s core-pair hypothesis.

## 3. What the retained theorem already supplies

Audit items 1–2 and C7 prove (L1) in regime A. The hypotheses are Hyp 2.2 and Sha[p^∞] finite.
- At p = 5, Hyp 2.2 holds: for the seed it excludes only 19, 59, 487 and 4547.
- Sha[5^∞] = 0 is proved.

The linearized BKS II Thm 4.6 then gives θ_{F,S} = ±m₅(Σ)·∏_{ℓ∈S}(#E^ns(F_ℓ)/ℓ)·R_F. For S = {ℓ}, T-a's ratio is therefore ±m₅(Σ_ℓ)/ℓ ≡ ±m₅(Σ_ℓ) (mod 5), since ℓ ≡ 1 (mod 5).

## 4. New falsifiable content

**T-a.** The only content beyond the retained theorem is **(1b)**. Here Σ_ℓ = {5, ℓ} ∪ primes(N) changes with ℓ, and the audit left independence from Σ unverified.
- (1b) is the expected Euler-factor compatibility of Kato's elements.
- The normalizing factor #E^ns(F_ℓ)/ℓ = 1 − a_ℓ/ℓ + 1/ℓ in the definition of m_p(Σ) is exactly the bottom-layer Euler factor P_ℓ(1). Adding ℓ to Σ should therefore leave m_p unchanged.
- This is a paper check against BKS II's definition of z_{Q,Σ}. It is not settled here: the local BKS II text is no longer on disk, and fetching arXiv 2103.11535 needs the user's approval.

**T-b.** It adds a comparison of tame and cyclotomic normalizations at the same p, covering the unit-root and Euler factors of L₅. It is the same linear image of z_Q, again with (1b).

**Neither touches (L2).** LINE's content is one rational m across all p. For any finite set of primes, the Chinese remainder theorem gives an integer matching the observed residues. So no computation at a fixed p, or at finitely many p, can confirm (L2) without a predicted value or a bound.

**Pre-registered criterion, if T-a is ever run.**
- If the three residues disagree mod 5 beyond sign, there is either a normalization error or a failure of (1b).
- The first is far likelier: the p = 13 run's C13 value was wrong through two scaling errors (see `SUPERSEDED_BY_NORMALIZATION.md`).
- Agreement says nothing about LINE.

## 5. T-c tests Mazur–Tate's value, not LINE

LINE alone allows any nonzero rational m. At p = 5, 7, 11, 13, the Iwasawa main conjecture (IMC) together with Sha[p^∞] = 0 makes m a p-adic unit, but its residues are otherwise unconstrained.

The pattern ±9·2^j is **Mazur–Tate's prediction** m = #Sha·(an unknown 2-power normalization), with #Sha = 9 assumed. So a T-c failure refutes "Mazur–Tate with #Sha = 9 and this normalization", not LINE. A failure would also be ambiguous between three causes:
- Mazur–Tate itself failing;
- a normalization error;
- #Sha = 9t² with t > 1 coprime to 2·3·5·7·11·13, which FIN alone allows.

The composition's line "a failure KILLS LINE" overstates the case.

## 6. Measured feasibility

- **Cutoffs scale linearly in the denominator.** Measured: m = 169 gives T = 5.505·10¹⁰, and m = 13 gives T = 4.03·10⁹.
- So m = 11, 61 and 71 need about 3.4·10⁹, 1.9·10¹⁰ and 2.2·10¹⁰. All are inside the sealed coefficient corpus: 3281 segments up to 5.5·10¹⁰, re-verified 2333/2333 after the incident.
- The symbol stage took 44 min 49 s wall-clock at m = 169. So T-a would take under an hour of wall time, a few CPU-hours, and about 1.1 GB peak.
- **Not included:** adapting stage A from p-power denominators to tame ℓ, and deriving the I²/I³ coefficient of the tame Mazur–Tate element in the ω-normalization. Both are review-sensitive.
- This is a local-scale job, never a paid-cloud one.

## 7. Recommendation

1. **Close (1b) on paper** from BKS II §2–4 (or Kato's Σ-truncated norm relations). This needs the source text.
2. **Run T-a only if a later route needs a validated tame Mazur–Tate pipeline**, for example Kurihara witnesses in regime K, and only with §4's criterion registered in advance.
3. **Do not present T-c as a LINE test.**

No computation was run for this note other than the three point counts. Nothing was sent, committed or pushed.
