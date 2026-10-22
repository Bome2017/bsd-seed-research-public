# P3_R2_PERIOD_PROVENANCE_AUDIT: optional source reading on F1's R2 seam (2026-09-19)

**Scope.**
- Source reading only. No computation; no change to any label.
- This is an addendum to the p = 3 run directory. `SHA3_THEOREM.md`, `P3_MANIFEST.sha256` and every other existing file are unchanged.
- It was written during an idle wait of the p = 5 upgrade run and is not part of that certificate.

## 1. The seam (restated from F1 Finding 1 / R2)

**The route.**
- Skinner's proof of Thm A for p ∣ N goes through SU Thm 3.6.4 applied to the Hida family of f.
- SU Prop. 12.3.6 then needs μ = 0 for the anticyclotomic p-adic L-function of the weight-2 member **normalised by Hida's canonical period** Ω_f = (f,f)/η_f(N).
- For the seed that member is f itself, with p = 3 ∥ N.
- Skinner patches Vatsal's p ∤ N restriction with Chida–Hsieh Thm C. CH's Θ_∞ is normalised by the **Gross period**, i.e. by ξ_f(N⁺,N⁻), the quaternionic analogue of the congruence number.

**The gap.** Passing between the two normalisations needs ord_λ η_f(N) = ord_λ ξ_f(N⁺,N⁻). This is Pollack–Weston's Theorem 2.3(2): the μ-invariant with respect to the canonical period is ord_p(η_f(N)/ξ_f(N⁺,N⁻)).

In the literature the identity is obtained in two steps:
- **(a) freeness.** The definite-quaternionic Hecke module is free over the localized Hecke algebra, which gives ξ_f(N⁺,N⁻) = η_f(N⁺,N⁻). This is PW Remark 2.4 and Theorem 6.2.
- **(b) the level-lowering formula.** ord η_f(N) = ord η_f(N⁺,N⁻) + Σ_{q∣N⁻} t_f(q). This is PW's conjecture, proved by Kim–Ota.
- For the seed, with N⁻ = 2243 and ρ̄₃ ramified at 2243, the Tamagawa exponent t_f(2243) = 0, so (b) would read η_f(N) = η_f(N⁺,N⁻).

## 2. Sources read (hashes in `sources/SOURCES.sha256`)

| source | setting and hypotheses (read at the source) | covers the seed (p = 3, 3 ∥ N, N non-squarefree)? |
|---|---|---|
| **Pollack–Weston**, "On anticyclotomic μ-invariants of modular forms", Compositio 147 (2011); arXiv math/0610694v1 (local text l. 1–80, 205–435, 1211–1330) | Standing setting: weight-2 newform of **squarefree level** N = N⁺N⁻; intro: "a prime p ≥ 5 of good reduction". Hypothesis CR: ρ̄ surjective, and ρ̄ ramified at every q ∣ N⁻ with q ≡ ±1 (mod p). **Theorem 6.2 (freeness):** under CR, the character group X̂_r(J) is free of rank one over the localized Hecke algebra; the proof uses mod-p multiplicity one for J₀(N) and Mazur's principle. Remark 2.4: Vatsal's paper replaced ξ_f by η_f; the two agree when the module is free | **No.** Its setting assumes squarefree N and p ≥ 5 of good reduction; the seed has 2³, 4547² ∥ N, p = 3 and 3 ∣ N. (CR itself holds for the seed: ρ̄₃ = GL₂(F₃), ramified at 2243) |
| **Kim–Ota**, "On the quantitative variation of congruence ideals and integral periods of modular forms", Res. Math. Sci. 10 (2023), arXiv:1905.02926v4 (pp. 1–3 read directly) | **"Let p ≥ 5 be a prime"** (§1.1.1). Theorem 1.1 assumes (1) **(N, p) = 1**; (2) ρ̄ restricted to G_{Q(√p*)} absolutely irreducible; (3) 2 ≤ k ≤ p − 1; (4) (N⁺,N⁻) = 1; (5) N⁻ squarefree; (6) ramification at q ∣ N⁻ with q ≡ ±1. Assumption 2.1 (FL) repeats p ∤ N. It proves PW's level-lowering formula (1.1) by R = T (Diamond–Flach–Guo, Dimitrov). Its §6 applies this to the comparison of Hida's canonical and Gross periods and to the μ-part of the anticyclotomic main conjecture. **It removes the squarefree restriction on N⁺ and the ramification restriction of PW / Chida–Hsieh** (Remark 1.2(2)) | **No.** p = 3 < 5, and 3 ∣ N violates (N, p) = 1. For p ≥ 5 with p ∤ N it would cover the non-squarefree N⁺ part |
| **Chida–Hsieh**, Crelle 741 (2018), Prop. 6.1 (read by F1) | freeness under (CR⁺)(1): "p > k + 1 and p ∤ N" | **No** (F1 CP-A2): 3 > 3 fails, and 3 ∣ N |
| **Skinner–Zhang**, "Indivisibility of Heegner points in the multiplicative case", arXiv:1407.1099 (abstract only) | multiplicative reduction at **p ≥ 5** | **No** (p = 3). Abstract only; it is not a period-comparison source |

## 3. Finding

- **R2 remains OPEN** as a published-provenance item. It is now located more precisely:
  - The squarefree-N obstruction that F1 noted (PW11) is **removed by Kim–Ota 2023** for p ≥ 5 with p ∤ N.
  - **The residual gap is exactly "p = 3 and p ∣ N".**
  - No located source proves the canonical-versus-Gross period comparison (freeness, or the level-lowering congruence formula) for a weight-2 form with p = 3 ∥ N.
  - The methods in the sources read (R = T with Fontaine–Laffaille at p ∤ N; Taylor–Wiles at p ≥ 5; Mazur's principle plus mod-p multiplicity one) all rely on p ≥ 5 or p ∤ N.
- **Nothing found shows that the comparison fails for the seed.** "No located source" is not an impossibility statement.
- Heuristically the relevant hypotheses hold: ρ̄₃ = GL₂(F₃), ramified at 2243 with t_f(2243) = 0, and p-distinguished (F1 CP-A1). This is **not** evidence of a proof.
- **Label recommendation: unchanged.** Keep F1's "PROVED, citing Skinner (2016) Thm A as printed", with R2 recorded, now sharpened to "the canonical-versus-Gross period comparison needed behind SU Prop. 12.3.6 is available in print only for p ≥ 5 and p ∤ N (Kim–Ota 2023; Pollack–Weston 2011 for squarefree N); the seed's case p = 3 ∥ N is not covered".

## 4. Cheapest next steps (not done; reading only)

1. **Wang (Wan?) 2023**, cited by Kim–Ota §1.1.3 as [Wan23] for "the comparison between Hida's canonical periods and Gross periods". Check whether it allows p = 3 or p ∣ N.
2. **p = 3 / p ∣ N integral Jacquet–Langlands:** Helm's work on maps between modular and Shimura-curve Jacobians (PW's [18]); later p ∣ N multiplicity-one results (ordinary Hida-theoretic freeness of the quaternionic module localized at a p-distinguished maximal ideal).
3. **Ask an author.** Skinner, or Chida–Hsieh, on whether SU Prop. 12.3.6 really needs the canonical normalisation at the weight-2 p-new point, or whether the Gross-period μ = 0 of CH Thm C suffices for the Λ-integrality used in Skinner's argument.

Sources (web, read-only):
- [Kim–Ota, arXiv:1905.02926](https://arxiv.org/abs/1905.02926)
- [Skinner–Zhang, arXiv:1407.1099](https://arxiv.org/abs/1407.1099)
- Pollack–Weston, arXiv math/0610694 (local copy)
