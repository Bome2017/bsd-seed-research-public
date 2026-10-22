# Symbol-lattice imports (claim A.4): source check

**Date:** 2026-09-23. **Scope:** claim A.4 of the reviewed v0.1.1 release. That claim is the lemma behind the identification lattice (1/1024)Z used by every modular-symbol certificate: S.3, S.5, S.7, S.11, S.13 and the 2243 route B.6. **The v0.1.1 package was not modified.** This folder is additive. Nothing was downloaded, uploaded or sent.

## Verdict

**SUPPORTED.** Two qualifications:
* one step is a derived lemma that no source states;
* the provenance items listed in §3 are read through secondary sources.

No gap was found in any step. The reviewed wording of A.4, restricted to the rational unitary cusps, is exactly what the argument proves. Every denominator the certificates use is of that type.

The chain is:

    c0 = 2^a (odd part: Mazur for semistable p, Edixhoven at the additive prime 4547),
    a <= 8 (derived 2-adic lemma),
    c_E | 2 c0 (isogeny),
    and for r = a/d with gcd(d,N) an exact divisor of N:  [r]^+- in (1/(2 c_E)) Z,  which lies inside (1/1024) Z.

## 1. Step by step

**Reading grades used below.**
* **At source** means that this check read the stated line in a local text.
* **Recorded quote** means that an earlier session read the primary source and recorded a verbatim quote; the source text is not stored locally.
* **Restatement** means read only through another paper's statement.
* **Standard** means a textbook fact, not re-read here.

| step | statement | sources and exact location | reading grade | verdict |
|---|---|---|---|---|
| **L1** Lattice from c_E | For a rational cusp r, φ_E(r) ∈ E(Q)_tors = Z/2. So 2·c_E·λ(r) ∈ Λ_E. The lattice Λ_E is rectangular since Δ > 0, so [r]^± ∈ (1/(2c_E))Z | Manin–Drinfeld (cusp differences are torsion in J₀(N)); φ_E is defined over Q with φ_E(∞) = O; φ_E\*ω_E = ±c_E·2πi f dz (the definition of c_E); E(Q)_tors = Z/2 (claims A.1, R.1); Δ > 0 (A.1, exact replay) | standard, plus exact | **verified** |
| **L1′** The cusps used are rational | For r = a/d with gcd(d,N) an exact divisor of N: the cusp classes of 0 (gcd 1) and of 1/p (p ∥ N) are images of ∞ under the Atkin–Lehner involutions W_N and W_{N/p}, which are defined over Q | `checks/local_4547_and_cusps.py`: every certificate denominator (25, 49, 121, 169; 27, 81; 2243²) has gcd(d,N) ∈ {1, 3, 2243}, an exact divisor | exact, plus standard | **verified** |
| **L2** Odd primes dividing c₀ are additive | "p ∤ c_φ for those p > 2 at which E has semistable reduction, see [Maz78]". For this curve the only odd additive prime is 4547 | CNS arXiv:1911.09446 l. 74 (§1); Česnavičius arXiv:1703.02951 l. 71 (§1.2: "[Maz78, Cor. 4.1] … cover … the case of an odd p") | restatement, two concordant sources read at source; Mazur 1978 itself not read | **verified** |
| **L3** 4547 ∤ c₀ | Edixhoven: for p ≥ 11, ord_p(c) = 0 unless the reduction is additive, **potentially ordinary**, of type II, III or IV. Both curves in the seed's 2-isogeny class have type III at 4547 with j ≡ 1728 and 4547 ≡ 3 (mod 4), so the reduction is potentially **supersingular** and the exception does not apply | CNS l. 76–78; Česnavičius l. 75–78; **Edixhoven's thesis, Thm 4.6.3**, recorded quote in `BSD_TWIST_SHA_SUPPORT_2026-09-22/MANIN_GATE_CORRECTION.md` §3 (hypotheses: p > 7; additive, not I₀\*/I_ν\*; no Q-isogeny of degree p; potentially supersingular ⇒ p ∤ c); `checks/local_4547_and_cusps.txt` (exact local data for both curves) | two restatements at source, plus the primary thesis via recorded quote. Edixhoven 1991 (Progr. Math. 89) is not read | **verified.** This upgrades A.4's "Edixhoven only through restatements" (see §4) |
| **L4** v₂(c₀) ≤ 8 | Derived lemma (Pasten's method, sharpened with CNS). **Step A:** v₂(c₀) ≤ e′, where e′ is the 2-adic exponent of S₂(Γ₀(N), Z₍₂₎)/H⁰(X₀(N), Ω). **Step B:** e′ ≤ 8, by intersection theory on the regular model of X_{Γ₀(N)∩Γ₁(5)} at 2 | CNS Thm 5.15 (l. 2693); Prop 6.2 (l. 2749); **Thm 6.12(c) (l. 3016: p = 2 and a prime ≡ 3 mod 4 divides N; here 3 \| N)**; §5.9 (l. 2454: components (a,b), multiplicity φ(p^min(a,b))); 6.10(vi) (l. 2970: the supersingular level structure is the Frobenius kernel); Lemma 7.1 (l. 3050: π∘π^∨ = [deg φ]). ARS "Modular degree…" **Thm 3.6(a)** ñ_A \| r̃_A with the congruence exponent defined through S₂(Z)/(S₂(Z)[I_f] + S₂(Z)[I_f]^⊥) (moddeg3 text, Def. 3.4 and eq. (2), l. 350–380) | each CNS and ARS statement read at source at the cited line; the argument re-derived (§2) | **verified**, as a derived lemma |
| **L5** c_E \| 2c₀ | "For any isogeny ψ: E′ → E … ψ\*(ω_E) = c_ψ·ω_{E′} for some c_ψ ∈ Z with c_ψ \| deg(ψ)". The class has two curves joined by a 2-isogeny, so c_E ∈ {c₀, 2c₀} whichever curve is optimal | CNS proof of Cor. 7.3, l. 3110 | at source | **verified** |
| **L6** Arithmetic | c₀ \| 2⁸ ⇒ c_E \| 2⁹ ⇒ 2c_E \| 2¹⁰ = 1024 ⇒ (1/(2c_E))Z ⊆ (1/1024)Z | — | exact | **verified** |

## 2. What was re-derived rather than cited

**Step A** (`BSD_MANIN_2_PRIMARY_GATE_2243_12_2026-09-18/00_REPORT.md` §2, with the referee's corrections in §6):
1. H = H⁰(X, Ω) equals the Néron lattice, by CNS 6.12(c) and 6.2.
2. H_χ = R·ω_f, by CNS 5.15, since a₁ = 1 makes ω_f primitive.
3. π•ω = c₀ω_f lies in H.
4. deg φ·ω = c₀·2^κ·u·ω. This follows from (π^∨)• factoring through the Petersson projection (anemic Hecke algebra plus strong multiplicity one) and from π∘π^∨ = [deg φ].
5. By ARS 3.6(a), v₂(deg φ) ≤ e′ + κ.
6. The unknown κ cancels, giving v₂(c₀) ≤ e′.

Each implication was checked. It uses only the statements confirmed at source in §1.

**Step B**, the arithmetic of the intersection bound, was recomputed:
* ω·F = 2g_m − 2 = 2μ − 4c′. The PSL₂-index is 12μ, and there are 4c′ cusps, since Γ₀(8) has 4 cusps at a coprime level.
* For each of the other three components, adjunction gives ω·C_i ≥ 2g′ − 2 + 3s, with 2g′ − 2 = μ/6 − c′ and s = μ/12.
* Hence ω·C_{j*} ≤ 3μ/4 − c′.
* With ω·C_{j*} ≥ K·C_∞·C_{j*} and C_∞·C_{j*} ≥ μ/12, this gives **K ≤ 9 − 12c′/μ < 9**.
* So 2⁸ clears every vertical pole, and e′ ≤ 8.

The descent to X (α étale at the generic points of the special fibre, and the S2 property of the dualizing sheaf) is as stated in the gate.

## 3. Still read only through secondary sources (unchanged by this check)

* Mazur 1978, Cor. 4.1: two published restatements agree (L2).
* Edixhoven 1991, Thm 3: the primary is paywalled and unread. Two restatements, and the thesis Theorem 4.6.3 via a recorded verbatim quote, agree (L3).
* Katz–Mazur 1985: 13.4.7, 13.5.6, 12.2.1, 6.6.1 (the component structure, multiplicities and regularity at 2), read through CNS only (L4 step B).
* Liu, Thm 9.1.37 (the adjunction formula): the sign was checked only by internal consistency.
* The Deuring mass formula (s = μ/12) and Conrad's appendix to BDP17: standard, not re-read.
* Manin–Drinfeld, and the definition of the rational cusps of X₀(N): standard.

## 4. Review grade and what an expert should check

**Who has checked it.** Every check of this lemma, including this one, was made by model sessions: the gate's author and its fresh-context referee, the operator review, and this check. **No independent human expert has checked the derived 2-adic lemma.** It is also the one step that no published source states for this class. An expert's time is best spent on three things:
1. **Step B's geometry at 2.** Check the four reduced components of the regular model of X_{Γ₀(N)∩Γ₁(5)} over Z₍₂₎, that all of them pass through each supersingular point (the Frobenius-kernel structure), and the q-expansion principle along the component carrying ∞.
2. **Step A.4–A.5.** Check that ARS 3.6(a), localized at 2, is compatible with the Petersson-projection factorization of (π^∨)•.
3. **L3.** A direct reading of Edixhoven 1991, Thm 3, would retire the last secondary-source item at 4547.

**Sensitivity.** The certificates need only 2c_E \| 1024, a margin of 9 in the 2-adic exponent relative to what Step A plus Step B give. If Step B failed, a weaker 2-adic bound could still suffice for some certificates, but no such fallback is recorded. As the first review noted, the certificates' own interval checks cannot detect a wrong lattice.

## 5. Proposed update to claim A.4 (not applied)

* **Qualification.** Replace "Edixhoven enters only through published restatements" with:
  > "Edixhoven: two published restatements read at source (CNS §1, Česnavičius §1.2) and the thesis Theorem 4.6.3 via a recorded verbatim quote; hypotheses at 4547 verified exactly for both curves of the isogeny class; Edixhoven 1991 itself unread."
* **Evidence.** Add `checks/local_4547_and_cusps.py` and its output.
* **Verification.** Add "symbol-lattice source check 2026-09-23: every cited CNS/ARS statement confirmed at its line; Steps A/B re-derived (model session, not human review)."
