# F2 — Hostile audit of the minimal set: FULL BSD(E) ⟺ S3 ∧ S≥7 ∧ SRAT (seed (2243,12))

Auditor: independent theorem architect / hostile referee (fresh context). Started 2026-09-18.
Target: `../FULL_BSD_SEED_DAG.md` (sha256 `3e1c96b0…0985d20`), §4 equivalence and §3 "two OPEN roots".
Rules honoured: read-only outside `fable_audits/`; nothing merged; no ledger/memory/seal edits; every computation
≤ 60 CPU-s, single process, `nice 15` (scripts + outputs in `F2_work/`); F1 (parallel session) untouched.

**Status of this file: COMPLETE (2026-09-18). One interruption: the session usage limit hit mid-audit; both web scouts died there but
had checkpointed to `F2_work/`; their unfinished parts (Wall-1 items C7–C10, all of Wall-2) were covered by my own narrower searches.**

---

## §0. VERDICT

# MINIMAL_SET_NEEDS_REPAIR

**The equivalence itself is TRUE.** Given the proved/certified nodes, FULL BSD(E) ⟺ S3 ∧ S≥7 ∧ SRAT holds in both directions; every
factor of the BSD formula was independently reproduced (Ω = 2ω₁, Reg at index 1, ∏c = 16, #tors = 2, C via PARI's `ellbsd`,
36 = 16·9/4; also C′ = C on the isogenous curve); the three statements are irredundant relative to every theorem I could find.
**No FATAL finding.** What needs repair is the DAG built around the equivalence — above all its claim that only *two* genuine
roots remain and that every single prime is blocked "by cost, not theory".

| # | severity | finding | where |
|---|---|---|---|
| R1 | **REPAIRABLE — structural** | **A third root, W3 = Sha[4547^∞] = 0.** The only chain at the additive, potentially supersingular prime 4547 (Kim Thm 1.8) is a *semi*-decision whose witness is guaranteed only by an unproved localized IMC at an additive prime, **and** its cost was mis-estimated by ~8 orders of magnitude: 9095 = 5·17·107 is not prime, 18191 ≡ 3 (mod 4547), and the condition a_ℓ ≡ 2 (mod p) was ignored. True smallest Kolyvagin pair: 87 256 931 · 92 849 741 ≈ **8.1·10¹⁵** (not 1.6·10⁸), i.e. ≳ 10²⁴ terms. Kim–Nakamura (JNT 2020): "neither a Mazur–Greenberg style main conjecture nor a control theorem" is available under additive reduction; I found no usable p-adic L-function for a non-CM curve at a potentially supersingular prime (Forrás–Lei, Sept 2026, is CM-only). A Kato/Iwasawa-type solution of Wall 1 would *not* absorb this prime | §B, §F.2 |
| R2 | **REPAIRABLE — label** | **G19 (supersingular p) is wrongly ROUTE_BLOCKED.** Lane 3's "depth 5–6, 10⁷–10⁹ CPU-h" comes from Riemann sums for L_α and the false remark that ± extraction needs the same depth. Pollack Prop. 6.18 gives θ₁ ≡ L_p^+ (mod ω₁) *exactly*; with Kobayashi's divisibility, the ± control theorem and B.D. Kim's no-finite-submodule theorem this yields **Criterion SS: c₂(θ₁) ≢ 0 (mod p) ⟹ Sha[p^∞] = 0**, from the same [a/p²]⁺ symbols as an ordinary prime (≈ 120 CPU-h at 23, ≈ 190 at 29). Verified at source; **not yet gate-audited** | §B.1 |
| R3 | REPAIRABLE — edges | On the ⇐ side FULL BSD's rank part follows from **SRAT ∧ G9** (L″ = 72·Ω·Reg > 0): the certified computation G10 is *not* an input of G28. On the ⇒ side the equivalence rests on CERTIFIED (not PROVED) nodes G5, G6, G10; the headline "given the proved nodes G1–G15" overstates | §A.3–A.4 |
| R4 | REPAIRABLE — wording | "SRAT is independent of both" ⟶ "no implication is known". In ranks 0 and 1 one global object proves both walls, and BKS Conj. 1.1 (ii)+(iii) is a common conjectural ancestor of W1 and W2 | §C.3 |
| R5 | REPAIRABLE — completeness | H(p₀) must be *effective* with *small* p₀ (finite part ≈ 0.23·p₀² CPU-h per pass) and must say whether it covers bad primes. The alternative architecture **{FIN, FORMULA}** — which needs no per-prime work and makes W3 and the cost-blocked primes vanish — is never mentioned | §F.2–F.3 |
| R6 | COSMETIC | DAG §4(c) still says "4547: OPEN (no chain)" against G22/§5; Cassels–Tate is not needed for S3 ∧ S≥7 ⟺ #Sha = 9; SU's IMC is over-cited in G17/G18 (Kato alone proves, SU only guarantees termination); the per-p saturation gate is redundant given G2; "D < 10⁷, 36 ± 10⁻¹³" is inconsistent with the certified radius (D ≲ 3·10¹⁴) | §A, §B, §D, §F |
| R7 | omissions (no label change) | Fouquet–Wan (unpublished; would make supersingular p *and 4547* decision procedures — non-split ℓ ∈ {3, 5843}, not 2243); Kim 2609.15328; BCGS; Sweeting at the seed's non-ordinary p; Kim–Nakamura; Forrás–Lei; BSS-III; SU-ICM; BKS-MT; Lane 2's unused ONE-BIT results; BD05 Cor. 3 | §E′ |

**Walls.** I could not break either: Wall 1 (uniform vanishing) **NOT_FOUND**, Wall 2 (rationality) **NOT_FOUND** — neither is
claimed impossible. Special-seed escapes: **none found** (§D). Older artifacts: **none implies an open node** (§E).

**What I did not verify** (so nobody reads this as a clean bill): the p = 3 chain (F1's remit); the p = 5 certificate and the DER
lemma (Lane 4's); the value of L″(E,1) (no long computations — only the arithmetic downstream of it); the cost figures at 2243 and
5843; the correctness of the Fouquet–Wan preprint; Criterion SS beyond reading its four published inputs as quoted in Kim–Kurihara
(IMRN 2021) — it needs its own hostile gate; items marked FROM MEMORY. The web scouts' quotations were obtained through a
summarising fetcher except where they say "read directly"; re-check before citing outward.

Corrected DAG: §F. Omitted routes: §E′ (and §B.1, §C). Ranking: §G.

---

## §A. Logical completeness (Task A) — reconstructed from first principles, DAG edges not trusted

### A.1 What FULL BSD(E) is, for this curve

For E/Q with r := ord_{s=1} L(E,s), full BSD is the conjunction of

- (R)  rank E(Q) = r;
- (F)  Sha(E/Q) is finite;
- (L)  L^{(r)}(E,1)/r! = Ω_E · Reg(E(Q)/tors) · ∏_p c_p · #Sha(E/Q) / (#E(Q)_tors)²,

with Ω_E = ∫_{E(R)} |ω_Néron| (so Ω_E = 2ω₁ when Δ > 0), Reg the determinant of the pairing
⟨P,Q⟩ = ĥ(P+Q) − ĥ(P) − ĥ(Q) with ⟨P,P⟩ = lim h(x(nP))/n² ("BSD normalization", = 2 × Silverman's ĥ), on a **Z-basis**
of E(Q)/tors. The Manin constant does **not** enter (L) (the period is the Néron period of E itself).

### A.2 Independent recomputation of every factor (PARI 2.17.3, `F2_work/f2_check1.gp`, 0.03 CPU-s)

| factor | DAG value | my recomputation | verdict |
|---|---|---|---|
| model minimal | u = 1 | `ellminimalmodel` returns [u,r,s,t] = [1, 7578, 0, 0]: same Δ, x-shift only | ✓ |
| N | 2³·3·2243·4547²·5843 | 6503188012738584, same factorization | ✓ |
| Kodaira / c_p | I₁*(2), I₂(2), I₁(1), III(2), I₂(2); ∏ = 16 | `elllocalred`: [−5,2], [6,2], [5,1], [3,2], [6,2]; ∏ = 16 | ✓ |
| torsion | Z/2 | [2,[2],[[0,0]]] | ✓ |
| w | +1 | `ellrootno` = 1 | ✓ |
| Ω | 2ω₁ = 0.0560898030388728… | Δ > 0, 2·E.omega[1] = 0.056089803038872808896618803615860768342 | ✓ |
| Reg(P₁,P₂) | 17.7965174724903402991749412194360384… | 17.796517472490340299174941219436038417 | ✓ |
| C = Ω·Reg·∏c/#tors² | 3.99281263923936691806855200220915… | `ellbsd(E)`·Reg = 3.9928126392393669180685520022091539474 | ✓ (independent normalization path: PARI's `ellbsd`) |
| (L″/2)/C with the lane's L″/2 | 8.99999999999999999634 | 8.99999999999999999634 | ✓ (arithmetic only; L″ itself NOT recomputed — no long computations) |
| isogeny class | size 2 | `ellisomat`: 2 curves, degree matrix [1,2;2,1] | ✓ |
| 23, 29 supersingular | a_p = 0 | a₂₃ = a₂₉ = 0; ss primes < 2000: 23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823 | ✓ |
| anomalous good p < 2000 | none | none | ✓ |

No missing or doubled torsion, Tamagawa, period (real-components factor 2 present), regulator (index 1 is a PROVED node; BSD
normalization confirmed against `ellbsd`), or Manin factor. **The constant 36 = ∏c·9/#tors² = 16·9/4 is right.**

### A.3 The implication (⇐): S3 ∧ S≥7 ∧ SRAT ⟹ FULL BSD — **correct, and it needs less than the DAG says**

1. Sha is a torsion group, so Sha = ⊕_p Sha[p^∞]. With G13 (2-part = 0), G15 (5-part = 0), S3 and S≥7: Sha = Sha[3^∞], finite of
   order 9. ⟹ (F) and #Sha = 9. *(Cassels–Tate is not used here; the DAG's parenthetical "(Cassels–Tate, …)" in §4 is
   unnecessary. C–T is only needed for the structure statement ≅ (Z/3)² and inside the p = 3 outcome logic.)* **COSMETIC.**
2. SRAT gives L″(E,1) = 72·Ω·Reg. Since Ω > 0 and Reg > 0 (Néron–Tate is positive definite on E(Q)⊗R and P₁, P₂ are independent —
   G1/G2), **L″(E,1) ≠ 0 follows from SRAT itself**. With G9 (L(E,1) = L′(E,1) = 0, PROVED) this gives r_an = 2 = rank. ⟹ (R).
   **So the ⇐ direction does not use the certified computation G10 at all.** The DAG lists G11 ← G10 as an input of G28; on the
   ⇐ side that edge is redundant. **REPAIRABLE (label hygiene): FULL BSD's rank part is *implied by* SRAT ∧ G9; G10 is needed only
   (i) to know that the target constant is 36 rather than 4k² for another k, and (ii) for the ⇒ direction.**
3. (L): L″/2 = 36·Ω·Reg = Ω·Reg·16·9/4. ✓.

### A.4 The implication (⇒): FULL BSD ⟹ S3 ∧ S≥7 ∧ SRAT — **correct, but only relative to the CERTIFIED nodes G5, G6, G10**

FULL BSD gives #Sha = (L″/2)/C ∈ Z. The certified enclosure (L″/2)/C ∈ [9 − 7.54·10⁻¹⁶, 9 + 7.54·10⁻¹⁶] then forces #Sha = 9,
hence Sha = Sha[3^∞] of order 9 (S3), every other primary part 0 (S≥7, and it re-proves G13/G15), and SRAT. Without G10 the
⇒ direction degrades to "FULL BSD ⟹ ∃k: #Sha = k², L″/(2ΩReg) = 4k²". So the equivalence **inherits the trust base of G10**
(custom C streaming code + a-posteriori FP analysis; Lane 3 AUDIT_A). This is stated in the DAG ("with G10 and G5–G7
certified") — fine — but the headline "given the proved nodes G1–G15" should read "given G1–G15, of which G5, G6, G10, G12 are
CERTIFIED_COMPUTATION, not PROVED".

### A.5 Verdict on Task A

The equivalence is **logically correct in both directions**. No factor is missing. Two repairs of bookkeeping (A.3-2, A.4) and
one cosmetic (A.3-1). Irredundancy ("minimal") is examined in §C/§F below: it can only ever mean "no *known* implication".


---

## §B. Prime decomposition (Task B) — every prime, route by route

Legend for the route type: **CERT** = exact finite certificate already in hand; **DEC** = finite computation that is *guaranteed*
to terminate with the exact answer (needs an IMC equality / primitivity that is a THEOREM for this curve at this p, plus
Reg_p ≠ 0); **SEMI** = finite computation that proves the statement *if* it succeeds, success not guaranteed by any theorem;
**COST** = order of magnitude; **GAP** = missing theory.

Independent computations: `F2_work/f2_check2.gp` (1.9 CPU-s) — Kolyvagin primes in Kim's sense
(P₁ = {ℓ ∤ Np, ℓ ≡ 1 (p), a_ℓ ≡ ℓ+1 (p)}, definition re-read at `KIM_2203.12159.txt` l.184) and j ≡ 1728 (mod 4547).

| p | reduction | claimed route(s) | my classification | remarks / errors found |
|---|---|---|---|---|
| 2 | additive I₁* (pot. good, v₂(j) = 4) | 2-isogeny descent, dim Sel₂ = 3 = r + dim E[2](Q) | **CERT (PROVED)** | 0 → E(Q)/2 → Sel₂ → Sha[2] → 0 with dims 3, 3 ⟹ Sha[2] = 0 ⟹ Sha[2^∞] = 0. Sound. |
| 3 | non-split mult. I₂ | Skinner Thm A (IMC equality) + SW Thm 6.1 (Jones) + depth-4 L₃ run | **DEC, pending run (≈ 14 CPU-h)**, *subject to F1's verdict on the chain* (not re-audited here) | An Sha-nontrivial prime: needs the **equality**, not just Kato-type divisibility. Independent algebraic cross-routes (3-descent + Cassels–Tate pairing à la Fisher–Newton; visibility G16′) are lower-bound/structure routes with UNKNOWN cost. |
| 5 | good ordinary, a₅ = −2 | Kato divisibility + SW 6.1 + a₂ ≢ 0 (5) | **CERT (PROVED via DER lemma v₂(c₀) ≤ 8)** | Not re-audited (Lane 4 did). Trust base: custom C streaming code + the derived Manin lemma. |
| good ordinary p ≥ 7 | — | Kato divisibility + SW 6.1 + depth-2 (or 3) L_p run | **DEC per p** (Kato ⊂ Λ integrally since ρ_p surjective; SU equality with q = 2243 guarantees that the unit test succeeds iff Sha[p^∞] = 0 and Reg_γ unit; deeper run otherwise) | **DAG over-cites**: G17/G18 list SU's IMC as an input. For *proving* Sha[p^∞] = 0 only Kato's divisibility is used (exactly as at p = 5, whose certificate §3 says "does not use Skinner–Urban"). SU matters only for termination. COSMETIC but it changes the trust base of each future per-p certificate. Cost ≈ 5p²√N terms. |
| good supersingular p (23, 29, 131, …) | a_p = 0 | (i) Kato + Kobayashi ±/Perrin-Riou (SW §6 supersingular) at depth 5–6; (ii) Kim Thm 1.8 two-prime Kurihara witness | **SEMI** (both): an upper bound is all that is needed and both give one unconditionally *if the number computed is a unit*; **witness/unit existence is guaranteed only by a ± IMC / localized IMC, which is printed only for semistable or square-free N** (seed: N not square-free) — pending the literature agent's check of Fouquet–Wan | **COST, corrected:** Kim route needs n = ℓ₁ℓ₂ with *Kolyvagin* primes: p = 23: ℓ = 829, 5107 ⟹ n ≈ 4.2·10⁶ (≈ 2·10¹⁵ terms ≈ 10⁶ CPU-h — already cheaper than the 10⁷–10⁹ CPU-h the DAG quotes for the ± route; **but both are superseded by Criterion SS, §B.1, at ≈ 10² CPU-h**); p = 29: 11833·17981 ≈ 2.1·10⁸; p = 131: ≈ 10¹¹. |
| 2243 | split mult. I₁ (exceptional zero) | Skinner Thm A + SW split case (L-invariant ≠ 0 by Barré-Sirieix–Diaz–Gramain–Philibert) at cusps b/2243²; Kim | **DEC on paper, COST ≈ 2·10⁴ CPU-h** (architect's figure, not re-derived) via L_p; Kim route: Kolyvagin primes 224829349, 240431657 ⟹ n ≈ 5.4·10¹⁶ — astronomically out of reach | — |
| 5843 | non-split mult. I₂ | Skinner Thm A (q = 2243) + SW; Kim | **DEC on paper, COST ≈ 10⁵ CPU-h**; Kim route n ≈ 149113361·466692097 ≈ 7·10¹⁶ | — |
| **4547** | additive III, pot. good **supersingular** (j ≡ 1728, p ≡ 3 (4); inertia image cyclic of order 4, decomposition image non-abelian, e = 4 ∤ p − 1 so no abelian base change makes the reduction good) | Kim Thm 1.8 only (no cyclotomic p-adic L-function is *known*: U_p-eigenvalue 0, so no finite-slope stabilization; Delbourgo's Compositio 1998 construction is, FROM MEMORY and unverified, for reduction made good ordinary by an abelian twist — impossible here) | **SEMI + GAP + astronomically blocked** | **Two errors in the DAG.** (1) "n ≥ 9095·18191 ≈ 1.6·10⁸" is wrong: 9095 = 5·17·107 is composite, 18191 ≡ 3 (mod 4547), and the condition a_ℓ ≡ 2 (mod p) (density ≈ 1/p) was ignored. The smallest Kolyvagin primes are **87 256 931 and 92 849 741, so n ≈ 8.1·10¹⁵**, i.e. ≈ 3·10²⁴ terms — not "prohibitive", *unreachable by any foreseeable computation*. (2) §4(c) still says "p = 4547: OPEN (no chain)" while G22/§5 say ROUTE_BLOCKED — internal inconsistency. **Substance:** the route is conditional on witness existence (Kim Conj. 1.7 at 4547 ⟸ localized IMC at an additive, potentially supersingular prime: not a theorem) *and* infeasible. This is a **third genuine root**, see §F. |

**Answer to "does every single prime really have at least one theorem route?"** On paper, yes (Kim's Thm 1.8 has no reduction
hypothesis; hypotheses p ≥ 5, ρ̄ surjective, p ∤ Manin constant hold at every p ≥ 5 incl. 4547 by the merged Edixhoven
check). But the architect's sentence *"The residual obstruction at any single prime is cost, not theory"* (DAG §5) is
**too strong** in two ways: (a) at supersingular p and at 4547 the route is a semi-decision whose success rests on an unproved
primitivity/IMC statement for this non-semistable curve; (b) at 4547 (and via Kim at 2243/5843) the cost is ≳ 10²⁴ elementary
operations, which is a *de facto* wall. Any Kolyvagin-system computation at a prime p needs Kolyvagin primes ℓ ≳ p²·log p, so
n = ℓ₁ℓ₂ ≳ p⁴: the horizontal route is intrinsically useless beyond p ≈ 30. Only the vertical (cyclotomic L_p) route scales
(≈ p²√N), and it does not exist at 4547.

### B.1 OMITTED ROUTE (found by this audit): supersingular primes at *depth 2* via Pollack's exact Mazur–Tate congruence

**Claim under attack.** DAG G19 / Lane 3 `D_primes/05_SUPERSINGULAR.md`: "depth 5–6 costs 10⁷–10⁹ CPU-h … ROUTE_BLOCKED", with the
side remark "even if [a ± leading-term theorem] exists, extracting L^± from the same symbols needs the same p-power depth, because
the coefficients of log^± have p-power denominators". **That remark is wrong.** One never divides by log^±:

- **[Pol03, Prop. 6.18]** (Duke 118), quoted verbatim as Prop. 1.11 of Kim–Kurihara, IMRN 2021 = arXiv:1804.00418 (text saved:
  `F2_work/src/KimKurihara_1804.00418.txt` l.265–269, pdf sha256 `9c0b995c…f72ddaedb`): for a_p = 0,
  **θ_n(f) ≡ ω̃_n^∓ · L_p^∓(Q_∞, f) (mod ω_n) in Λ_n = Z_p[Gal(Q_n/Q)] for n even/odd**, with ω̃_n^+ = ∏_{2≤m≤n, m even} Φ_m(1+X),
  ω̃_n^- = ∏_{1≤m≤n, m odd} Φ_m(1+X). For **n = 1**: ω̃₁^+ = 1, so **θ₁ ≡ L_p^+ (mod ω₁)**, an exact congruence of *integral* objects.
  θ₁ lives on the first layer Q₁ ⊂ Q(μ_{p²}): it is built from the symbols [a/p²]⁺ — exactly the "depth 2" data of the ordinary runs.
  Corroboration: Pollack–Weston, Duke 156 (arXiv:0906.1741, `F2_work/src/PollackWeston_0906.1741.txt` l.41–47, Thm 4.1):
  λ(θ_n) = q_n + λ^± with q₁ = 0, q₂ = p − 1.
- **[Kob03, Thm 4.1] + Kato** (KK Thm 3.6(2); also BSTW 2409.01350 Thm 10.4(b) as read by my literature scout — *no square-free
  hypothesis*): for a_p = 0, p odd, non-CM, ρ̄ surjective: (L_p^∓) ⊆ char_Λ(Sel^±(Q_∞,E[p^∞])^∨), integrally.
- **[Kob03, Thm 9.3]** (KK Thm 3.9): if p ∤ Tam(E), Sel(Q,E[p^∞]) ≅ Sel^±(Q_∞,E[p^∞])^Γ.
- **[B.D. Kim 2013, Thm 1.1]** (KK Thm 3.8): X^± := Sel^±(Q_∞,E[p^∞])^∨ has no non-zero finite Λ-submodule.

**Criterion SS (derived here; every input is a published theorem; NOT yet gate-audited).** Let p ≥ 5 be good supersingular for the
seed (a_p = 0 automatic), ρ̄_p surjective, p ∤ Tam = 16, rank 2. Then X² | char(X^∓) | L_p^± =: X²·g. If the image of θ₁ in
F_p[X]/(X^p) is c₂X² + O(X³) with **c₂ ≠ 0**, then g is a unit, char(X^-) = (X²), X^- ↪ (Λ/X)² ≅ Z_p² with finite index (the Λ/X²
shape is excluded because rank (X^-)_Γ ≥ 2), so (X^-)_Γ ≅ Z_p² is torsion-free, Sel(Q,E[p^∞]) ≅ (Q_p/Z_p)² is divisible, and
**Sha(E/Q)[p^∞] = 0**. Theorem-forced self-checks: the X⁰ and X¹ coefficients of θ₁ must vanish mod p.

**Consequence.** At 23 and 29 (and every supersingular p) the certificate needs the *same* symbols [a/p²]⁺ as an ordinary prime:
≈ 0.23·p² CPU-h in Lane 3's own cost model (≈ 120 CPU-h at 23, ≈ 190 CPU-h at 29; and ≈ 0 marginal cost inside a shared pass),
not 10⁷–10⁹ CPU-h. **G19 should be relabelled FINITE_CERTIFICATE_CANDIDATE (per p)**, with two caveats: (i) it is a SEMI-decision
(if c₂ ≡ 0 mod p one falls back to θ₂ ≡ Φ₁(1+X)·L_p^- mod ω₂, i.e. depth 3, or deeper; *guaranteed* success needs the ± main
conjecture, which for non-square-free N rests only on unpublished work — Wan [Wan18a] as cited in KK Rem. 3.7, Fouquet–Wan
arXiv:2107.13726v3); (ii) it needs its own theorem gate (sign conventions [Pol03] = −[Kob03]; integrality of θ₁ uses c_E | 512 and ρ̄
irreducible; the normalization γ ↦ 1+X). Lane 3 had flagged exactly this question as "UNKNOWN (O-8)"; the answer is: it helps decisively.

---

## §C. Attack on the two "global walls" (Task C)

Sources: my own analysis; two web scouts that died at the session limit but checkpointed (`F2_work/LIT_WALL1_LARGE_PRIMES.md`,
C1–C6 complete; `F2_work/LIT_PERPRIME_AND_RATIONALITY.md`, Part I complete, Part II not reached — I covered Part II myself with
targeted searches); sources saved under `F2_work/src/`. "NOT_FOUND" means not found, never "impossible".

### C.0 Why every known method is per-p (the structural reason, stated once)

A p-uniform bound on Sha has only ever come from a **characteristic-zero global object with a non-zero index**: L(E,1)/Ω via Kato's
reciprocity law (rank 0), the Heegner point y_K via Gross–Zagier (rank 1). For a *primitive* double zero of L(E,s) no such object is
known: all Heegner points y_K are torsion (L′(E/K,1) = L(E,1)L′(E^K,1) + L′(E,1)L(E^K,1) = 0); Kato's bottom class z_Q vanishes iff
r_an > 1 (Venerucci Thm B, quoted in BSS-III Rem. 6.6); every "derived" replacement (Kolyvagin derivatives, Kurihara numbers,
generalized Kato classes, BD theta-element derivatives) lives in a group killed by ∏(ℓ±1) or is a p-adic limit, so it only sees the
primes p it was built for. Base change cannot help: for any F/Q, L(E/F,s) still contains the primitive factor L(E,s) with its double
zero, and Sha(E/Q)[p^∞] ↪ Sha(E/F)[p^∞] for p ∤ [F:Q].

### C.1 Wall 1 (Sha[p^∞] = 0 for all large p) — route-by-route

| route (operator's list) | exact statement checked (source) | hypotheses vs seed | what it gives | verdict |
|---|---|---|---|---|
| Kolyvagin systems / Kato (Mazur–Rubin; Kim AJM 148 (2026) = arXiv 2203.12159 Thm 1.4, 1.8, 1.10) | Sel structure ⟺ Kurihara numbers; witness exists ⟺ IMC (Thm 1.10) | p ≥ 5, ρ̄ surj., p ∤ c₀: OK at every p ≥ 5 | per-p; Kolyvagin primes ℓ ≡ 1 (p), a_ℓ ≡ 2 (p) force n ≳ p⁴ | **PER_PRIME_ONLY** (in DAG) |
| W. Zhang, CJM 2014, Thm 1.1/1.2/1.4 | Kolyvagin's conj.; ord κ^∞ = max r^± − 1. Hyp. (♠) explicitly allows non-square-free N: "no requirement … at primes where E has additive reduction" | good **ordinary** p ≥ 5, ρ̄ surj., Ram ⊇ {3, 2243, 5843}: **OK** | Sha[p^∞] finite ⟺ ν_p = 1 ⟺ one derived class c(ℓ) ≠ 0; Rem. 3 "r_p independent of p" works **only for corank 1** (routes through the p-independent y_K) | PER_PRIME_ONLY (in DAG) |
| Sweeting arXiv 2012.11771v3 Thm A, Cor. B | same, incl. **non-ordinary** p when some ℓ ∥ N is non-split toric (3, 5843) or image ⊇ SL₂(Z_p) | OK at every p ∤ 2N | Kolyvagin's conjecture is a *theorem* for the seed at essentially every good p; still per-p | PER_PRIME_ONLY (in DAG; the extension to the seed's supersingular p is not noted there) |
| BCGS arXiv 2312.09301 (CJM, to appear) Thm A–C | ord κ^Heeg = max r^± − 1; ord κ^Kato = r_str; refined M_∞ = Σ ord_p c_ℓ | good ordinary p > 3 | per-p | PER_PRIME_ONLY (**not in DAG §3**; in bridges C4) |
| **C.-H. Kim, arXiv 2609.15328 (14 Sep 2026)** "…Sha via Kolyvagin's conjecture" Thm 1.1 | Sha[p^∞] finite ⟺ explicit p-divisibility pattern of derived Heegner points; "as far as we know, there is almost no theoretical result towards the finiteness … when the analytic rank is > 1" | good p ≥ 5; supersingular case assumes E semistable: FAILS | a per-p *criterion*, not a proof | PER_PRIME_ONLY (**omitted by the architect; 4 days old**) |
| Castella Thm A / Castella–Hsieh (FoM Σ 2022) Thm A, Cor. B, C | κ_{α,α⁻¹} ≠ 0 ⟺ dim Sel_str = 1; non-vanishing in their examples is *deduced from* BD05 Cor. 3 (Θ_{E/K} of exact order 2 ⟹ Sha(E/K)[p^∞] finite) | ordinary p; Brandt module of size ≈ N/12 ≈ 5·10¹⁴ | per-p equivalence; p-adic-limit class | PER_PRIME_ONLY (in DAG) |
| Castella–Sano arXiv 2601.14504 Thm A–C | refined Kurihara conj. ⟺ IMC; proved for good ordinary, or supersingular **with N square-free** | ordinary OK; supersingular FAILS | per-p | PER_PRIME_ONLY (bridges C4) |
| Burns–Kurihara–Sano, JMSJ 76 (2024) Conj. 1.1, Thm 1.3, Cor. 1.11, Thm 1.13 (local text re-read, l.117–147) | Thm 1.3(b) **assumes Sha[p^∞] finite**; Thm 1.13 assumes Sha finite + IMC + Conj. 1.1 | — | nothing unconditional in rank 2 | ASSUMES_SHA_FINITE / conjecture (in DAG) |
| Burns–Sakamoto–Sano III (arXiv 1902.07002) Thm 6.11 | assumes BSD_p incl. Sha finite; for rank > 1 the input z_Q = 0, bound vacuous; "higher rank" = core rank, which is 1 for T_pE over Q | — | nothing | NOT_APPLICABLE (**not in DAG**) |
| Mazur–Tate refined conj.: Ota AJM 2018 (order of vanishing only); BKS arXiv 2103.11535 Thm 1.1 (needs full BSD + Conj. 1.1), and their own sentence: for r > 0 the leading term "has remained stubbornly mysterious … no theoretical evidence … numerical evidence only for r = 1" | — | — | no Sha bound | NOT_A_ROUTE (DAG mentions MT only under G26) |
| Darmon–Rotger / BSV (Astérisque 434) | BSV's triple product factors as **two rank-one** Rankin L-functions over K, p ∣ N multiplicative; DR16 rank-2 statement is a conjecture | — | — | NOT_APPLICABLE / conjecture (in DAG) |
| Skinner–Urban ICM 2006 | *lower* bounds on Selmer rank; authors: "Unfortunately, this excludes the case of elliptic curves" | — | wrong direction | NOT_APPLICABLE (**not in DAG**) |
| visibility; level raising; congruence ideals | visibility constructs Sha (lower bounds: G16′). Level raising at admissible ℓ₁ℓ₂ (BD, W. Zhang) lowers Selmer rank by 2 and reduces to a rank-0 value on a definite quaternion algebra of discriminant N⁻ℓ₁ℓ₂ — per-p, Brandt module of size ≈ N·ℓ₁ℓ₂/12 ≫ 10¹⁸ | — | per-p, infeasible | PER_PRIME_ONLY (**not in DAG**) |
| p-uniform residual / modularity-lifting arguments | p-uniform Bloch–Kato results exist for **ad⁰ρ** (Diamond–Flach–Guo) because L(ad⁰f,1) is a non-zero critical value (= the "global index"). For the standard representation at a double central zero there is no critical value to play that role | — | — | NOT_FOUND |
| base change / Hilbert modular | C.0: the primitive double zero survives every base change | — | — | NOT_A_ROUTE |
| 2-isogeny, rational 2-torsion | give Sha[2^∞] = 0 and Sha(E)[odd] ≅ Sha(E′)[odd]; I re-verified C′ = C (`f2_check3.out`) | — | nothing new | NOT_A_ROUTE |
| Zywina family | E_{m,n}: y² = x(x² − 5Ax + 4AB), A = m + 16n², B = m + 25n², a² − 4b = 9mA. Non-CM, not a Q-curve. BSD for the generic fibre over a function field does not specialize | — | — | NOT_FOUND |
| function-field implication "one ℓ-part finite ⟹ Sha finite" (Tate–Milne) | no number-field analogue found | — | — | NOT_FOUND |
| Banwait arXiv 2609.08431 (CM rank 2) | "does not prove finiteness of Sha for any elliptic curve of rank two"; per split prime, CM only | seed non-CM | — | NOT_APPLICABLE |
| Logachev math/0411346; Nguyen 1309.7675 | programme for Siegel sixfolds with "large gaps"; Nguyen unrefereed (F5's remit) | — | — | NOT_USABLE |
| IMC infrastructure | SU Thm 3.6.4 (no square-free hypothesis; one q ∥ N with ρ̄ ramified; integral under SL₂(Z_p)); Yan–Zhu arXiv 2412.20078v4 (ordinary, no condition on N, up to Q_p); **Fouquet–Wan arXiv 2107.13726v3 Thm 1.7/1.13** (Kato's IMC, integral, *no* square-free hypothesis, **π_p may be supercuspidal**, needs a **non-split** ℓ ∥ N with ρ̄ ramified: seed OK with ℓ = 3 or 5843, *not* 2243) | FW is unpublished; CLW arXiv 2608.29470 (29 Aug 2026, co-authored by Wan) still assumes N square-free and says the FW argument was "outlined" | would upgrade supersingular p **and 4547** from SEMI to DEC | per-p; **FW omitted by the architect** |

**Result for Wall 1: NOT_FOUND.** Nothing p-uniform exists for r_an = 2; two September-2026 preprints say so in print. The
architect's §3 table is correct as far as it goes. Omissions are listed in §E′ below; none of them breaks the wall.

**One sharpening the architect did not state.** For good ordinary p, Kato + SU + Schneider/Perrin-Riou give the *theorem*
a₂(L_p) = u_p · (∏c/#tors²) · ε_p · Reg_γ(p) · #Sha[p^∞], u_p ∈ Z_p^×. So Wall 1 (ordinary part) is *equivalent* to: "for all large p,
ord_p a₂(L_p) = ord_p Reg_γ(p)", i.e. to the **mod-p leading-term part of the Mazur–Tate refined conjecture at conductor p², r = 2**
("Σ_a [a/p²]⁺·w(a) ≡ 36·ε_p·det⟨P_i,P_j⟩_MT (mod p) up to a unit"). Both sides are computable from characteristic-zero data.
This is the smallest exact formulation I can find; it is the statement BKS call "stubbornly mysterious".

### C.2 Wall 2 (rationality of L″(E,1)/(Ω·Reg) with a denominator bound)

| candidate | finding | verdict |
|---|---|---|
| Yun–Zhang I, II (Annals 2017/2019) and follow-ups (arXiv 2607.07531 deeper level; 2607.25237; Liu–Wang 2504.00275) | function fields only. W. Zhang (Oberwolfach report): over a number field "the analogous spaces only exist (at least for the time being) when r ≤ 1" | FUNCTION_FIELD_ONLY |
| Li–Liu arithmetic inner product formula (arXiv 2412.00688); arXiv 2603.15795; KRY; arithmetic Siegel–Weil; AGGP/AFL; YZZ triple product | all are **first** central derivatives. A first-derivative formula can only see a simple zero; L(E,s) is primitive with a double zero, so no auxiliary Λ(s) = L(E,s)·L(G,s) has Λ′ ∝ L″(E,1) (Λ′(centre) = 0). E.g. L(f×f×f,s) = L(Sym³f,s)L(f,s−1)² vanishes to order ≥ 4 | NOT_APPLICABLE |
| GKZ / Heegner cycles on products | need w = −1; here all y_D are torsion | NOT_APPLICABLE |
| rank-2 of GL₂-type surfaces (L = L(f)L(f^σ), two simple zeros) | rationality follows from GZ twice — but an elliptic curve over Q has a rational newform, no such splitting | NOT_APPLICABLE |
| Beilinson (K₂, non-central values); Rodriguez-Villegas–Zagier (central *values*) | not the central second derivative | NOT_APPLICABLE |
| p-adic bridges: BKS Cor. 1.11 / Thm 1.13; Büyükboduk–Pollack–Sasaki; Disegni | rank-1 only, or conditional on BKS Conj. 1.1 and Sha finite | CONDITIONAL_ON_CONJECTURE |
| 2024–26 sweep ("second derivative", "higher Gross–Zagier number field", "rank 2 BSD formula") | Wei–Zhai 2605.09251 (averages of twists), 2507.20297 (rank-one quadratic fields), 2510.10277 (real quadratic, first derivative) — none | NOT_FOUND |

**Result for Wall 2: NOT_FOUND.** Rationality of L^{(r)}(E,1)/(Ω·Reg) is not known for a single E/Q with r ≥ 2.

### C.3 The two walls are *not known to be independent* (repair of DAG §4's "SRAT is independent of both")

Logically, no implication between S≥7 and SRAT is known in either direction — that is all "independent" can mean. But in every
strategy that has ever worked (ranks 0, 1) **the same global object proves both**, and the only conjectural framework for r = 2
does the same: **BKS Conj. 1.1(ii)** (integrality of η^BSD = [L″(E,1)/(2Ω·R_∞)]·x₁∧x₂ in ∧²H¹(Z_S,T_p) for every p) *is* SRAT with a
denominator bound, and **Conj. 1.1(iii) + IMC_p ⟹ BSD_p(E)** (their Thm 1.13) gives Sha[p^∞] = 0 for every p ∤ 6 at once. So the
honest picture is one conjectural ancestor with two children, not two unrelated walls. Consequence for planning: effort on a
"rank-2 Perrin-Riou/Gross–Zagier" object attacks W1 and W2 simultaneously; effort on W1 *alone* (e.g. uniform Kolyvagin) has no
known analogue of how it could avoid producing W2 on the way.

---

## §D. Special-seed escapes (Task D): does this curve's extra structure turn the general open problem into a special-case theorem?

**Answer: NO escape found.** Each feature below is real and useful, but each one only removes *exceptional primes or hypotheses*
from per-p theorems; none supplies a p-uniform object or a formula for L″.

| feature | verified here? | what it actually buys | why it is not an escape |
|---|---|---|---|
| 2-isogeny class of size exactly 2 | ✓ `ellisomat` | Sha(E)[odd] ≅ Sha(E′)[odd]; BSD(E) ⟺ BSD(E′) (Cassels); C′ = C ✓ (`f2_check3.out`: Tam′ = 16, tors′ = 2, Reg′ = Reg, Ω′ = Ω). No third curve to transfer to | E′ has the same N, same L, same local types: nothing is easier on E′ |
| Sha[2^∞] = Sha[5^∞] = 0 | not re-audited | removes 2 and 5 from the per-p list; Monsky parity ⟹ w = +1 | finite facts |
| predicted #Sha = 9 | ✓ arithmetic | makes p = 3 the single prime needing an IMC *equality* (or a descent + Cassels–Tate); visibility gives an independent lower bound | raises, not lowers, the difficulty at 3 |
| ρ̄_p = GL₂(F_p) for every odd p | taken as merged | every per-p theorem applies with **no exceptional p**: Kato integral divisibility, SU integral equality, Kim 1.8/1.10, Kobayashi (L^±) ⊆ char, W. Zhang, Sweeting. Any *future* uniform theorem of Kolyvagin/Kato type would have exceptional set ⊆ {2, 3} ∪ {bad p} ∪ {p ∣ index} | hypotheses, not conclusions |
| Tam = 2⁴, #tors = 2; no anomalous p < 10⁵ | ✓ (< 2000 re-checked) | for odd p: control theorems are isomorphisms (KK Thm 3.9), Kim Thm 1.10's E(Q_p)[p] = 0 and p ∤ Tam hold, BKS (d) holds | idem |
| explicit index-1 generators | ✓ heights reproduced | p-adic regulators computable at every p; p-saturation at **every** p is automatic (so the DAG's per-p gate "E(Q)/pE(Q) = ⟨P₁,P₂⟩" in G18 is redundant given G2 — COSMETIC) | idem |
| w = +1, primitive double zero | ✓ | — | this is precisely what kills the rank-one machinery (C.0) |
| conductor 2³·3·2243·4547²·5843 | ✓ | **two non-split multiplicative primes (3, 5843) with ρ̄_p ramified for every odd p** (v(Δ) = 2): this is exactly Fouquet–Wan's hypothesis at p with ρ̄\|G_p irreducible — *including the additive prime 4547* — and Sweeting's hypothesis at non-ordinary p; one split prime (2243, v(Δ) = 1) for SU/Skinner. W. Zhang's (♠) imposes *no* condition at the additive primes 2, 4547 (his own note, quoted by my scout from CJM p.195) | makes per-p theorems *applicable*; N ≈ 6.5·10¹⁵ makes every Heegner/Brandt computation infeasible |
| 4547: type III, j ≡ 1728 (mod 4547), p ≡ 3 (mod 4) | ✓ | locally at 4547 the seed has the same shape as a Z[i]-CM curve at an inert additive prime — the setting of **Forrás–Lei arXiv 2609.13063 (11 Sep 2026)**, whose ± theory is proved for CM curves only. The *local* half of that theory depends only on E/Q_p; the global half could be replaced by Kato's Euler system. This is a research direction for W3 (§F), not a theorem | global input there is elliptic units / CM |
| Zywina family E_{m,n} | ✓ algebra (a = −5A, b = 4AB, a² − 4b = 9mA) | explicit sections; 2-descent gives rank exactly 2 uniformly | no CM, no Q-curve structure, no extra endomorphisms or correspondences; Lane 2 already showed that even at fixed p = 5 the per-curve modular-symbol bit does not transport along the family |

---

## §E. Older-project composition (Task E)

Method: a read-only gap agent swept all 426 top-level directories of `~` against the architect's three archaeology logs
(transcribed in `F2_work/ARCHIVE_GAPS.md`); I then tested each candidate against the open nodes myself.

| artifact | what it proves (own label) | plugged into the new seed facts | effect |
|---|---|---|---|
| Lane 2 `U_UNIFORMITY/00_REPORT.md` (sha `43c0c6b6…`): Lemma INTEG, Prop. KATO-ONE-BIT, Thm ONE-BIT-EQUIVALENCE (DERIVED, refereed inside Lane 2). **Not used by the architect**, who read only `LANE2_REPORT.md` | for good ordinary non-anomalous p with p ∤ ∏c: Reg_γ ∈ Z_p for free; a₂(L_p) ≢ 0 (p) ⟹ Sha[p^∞] = 0 **and** ord_p Reg_γ = 0; ord_p #Sha[p^∞] = ord_p a₂ − ord_p Reg_γ | hypotheses hold at every good ordinary p ≥ 7 of the seed | **sharpens G17/G18**: the "unit Reg_γ" and "saturation" gates are *consequences / already proved*, not per-p hypotheses; exactly one mod-p bit per ordinary p. Closes no prime; nothing p-uniform |
| Lane 2 `B_A2_MECHANISM` survey | "None found for odd p" for a mechanism controlling a₂ | — | an in-house *negative* record consistent with §C.1 |
| 62a1 / 66b1 strong-BSD chains | rank-0 assemblies (φ-descent + Zhai 1.7 + Banwait–Huang 2.13 + Kato); the "all large p" step there is Kato's theorem with L(E,1) ≠ 0 | L(E,1) = 0 | **nothing survives at rank 2** (agrees with bridge C1) |
| H41 (frozen), H9R16–18 towers, Lane 1 NC5 | rank-0 twist families / a CH-branch tower that misses the strict line at p = 5 | — | no bearing on S3, S≥7, SRAT (agrees with C6) |
| Lean: Lane 4 (35 theorems), Aristotle `Descent.delta_descent` | algebraic glue; generic 2-isogeny descent | — | hardening only |
| `BSD_RIGOROUS_STREAM_CORE_2026-09-19` | **empty skeleton** | — | H-a/H-b (rigorous streaming core; PROVED r_an) are *planned, not built* — relevant to §A.4's trust-base remark |
| post-saturation artifacts | NOT_FOUND anywhere | — | — |
| any 3-descent / Sel₃ / Cassels–Tate computation; any ± / Kurihara / theta-element computation on the seed at p ≥ 7 | NOT_FOUND (one Kurihara witness at p = 5, n = 5611, in Lane 1) | — | — |

**New composition found by this audit (not in the archive, not in the DAG):** Lane 3's shared streaming pass (cusps b/p²) +
Pollack Prop. 6.18 + Kobayashi + B.D. Kim ⟹ **Criterion SS** (§B.1): the supersingular primes ride along in the *same* pass as the
ordinary ones. This is the only place where plugging known theorems into existing infrastructure changes a label (G19).

**No older artifact implies S3, any infinite part of S≥7, S_4547, or SRAT.**

### §E′. Every route / fact the architect omitted (consolidated)

1. **Criterion SS** — supersingular p at depth 2 (§B.1). *Changes a label* (G19: ROUTE_BLOCKED → FINITE_CERTIFICATE_CANDIDATE).
2. **Fouquet–Wan arXiv 2107.13726v3** — the only IMC *equality* that would cover supersingular p **and the additive prime 4547** for this
   non-square-free N (non-split ℓ ∈ {3, 5843}); unpublished, and called an outline by Castella–Liu–Wan (Aug 2026). *Changes
   SEMI → DEC if accepted*; a hostile referee should not accept it yet.
3. **Kim–Nakamura JNT 2020** — at additive p > 7: a non-zero Kurihara number ⟹ Kato's IMC at p; "neither a Mazur–Greenberg style
   main conjecture nor a control theorem" exists there. (Confirms 4547 is a theory gap, not only a cost gap.)
4. **Forrás–Lei arXiv 2609.13063** — ± theory at potentially supersingular additive primes, CM only (direction for W3).
5. **C.-H. Kim arXiv 2609.15328**, **BCGS 2312.09301 Thm C / Cor. C**, **Sweeting for non-ordinary p on the seed**, **Yan–Zhu
   2412.20078**, **BSS-III**, **SU ICM 2006**, **BKS 2103.11535** — all checked, all per-p / conditional / wrong direction.
6. **Lane 2's ONE-BIT results** — in-house, unused; simplify the per-p gates.
7. **BD05 Cor. 3 / Castella–Hsieh §6** — a second genuine per-p *proof* route in rank 2 (Θ_{E/K} of exact order 2), infeasible here.
8. **Common conjectural ancestor of W1 and W2** (BKS Conj. 1.1 (ii)+(iii)) and the **Mazur–Tate mod-p reformulation of W1** (§C.1, C.3).
9. **Alternative two-statement architecture** {FIN, FORMULA} (§F.3), which needs *no* per-prime computation at all.
10. **Corrected Kolyvagin-prime data** (§B): the horizontal (Kim) route is useless beyond p ≈ 30; at 4547, n ≈ 8.1·10¹⁵.

---

## §F. Corrected minimal DAG (repair, not replacement)

### F.1 The equivalence, restated with its true inputs

    Given   PROVED:     G1 rank = 2;  G2 index 1;  G3 tors = Z/2;  G4 ∏c = 16;  G8 w = +1;  G9 L(E,1) = L′(E,1) = 0;
                        G13 Sha[2^∞] = 0;  G15 Sha[5^∞] = 0 (via the DER lemma v₂(c₀) ≤ 8)
            CERTIFIED:  G5 Ω;  G6 Reg;  G10 L″(E,1)/2   (⟹ G12: (L″/2)/C ∈ 9 ± 7.54·10⁻¹⁶)

    (⇐)  S3 ∧ S≥7 ∧ SRAT  ⟹  FULL BSD(E)        uses only the PROVED nodes  (r_an = 2 follows from SRAT ∧ G9; G10 NOT needed)
    (⇒)  FULL BSD(E)  ⟹  S3 ∧ S≥7 ∧ SRAT        uses the CERTIFIED nodes    (to force #Sha = 9)

Edge repairs to `FULL_BSD_SEED_DAG.md` §2: delete G28 ← G11 on the ⇐ side (keep G11 as a free-standing certified fact);
add SRAT ∧ G9 ⟹ G11; in §4 drop "(Cassels–Tate …)"; replace "SRAT is independent of both" by "no implication is known in either
direction; both descend from BKS Conj. 1.1".

### F.2 S≥7 decomposed honestly (this is where the DAG needs repair)

    S≥7  ⟺  S_ord(p₀) ∧ S_ss(p₀) ∧ S_2243 ∧ S_5843 ∧ S_4547 ∧ H(p₀)          for any p₀ ≥ 7 (p₀ < 2243 in practice)

| node | statement | corrected label | basis |
|---|---|---|---|
| S_ord(p₀) | Sha[p^∞] = 0, good ordinary 7 ≤ p ≤ p₀ | FINITE_CERTIFICATE_CANDIDATE per p, **DEC** | Kato divisibility + SW 6.1 (proof); SU 3.6.4 (termination only); Lane 2 ONE-BIT (no Reg/saturation gate). ≈ 0.23p² CPU-h; shared pass ≈ cost of the largest p |
| S_ss(p₀) | same, supersingular p ≤ p₀ (23, 29, 131, 167, 281, …) | **FINITE_CERTIFICATE_CANDIDATE per p, SEMI** *(was ROUTE_BLOCKED)* | Criterion SS (§B.1), same symbols and cost as an ordinary p; needs a theorem gate; DEC only if a ± IMC for non-square-free N is accepted (FW / Wan18a, unpublished) |
| S_2243, S_5843 | Sha[p^∞] = 0 at the multiplicative primes | ROUTE_BLOCKED by cost (≈ 2·10⁴ and ≈ 10⁵ CPU-h, architect's figures, not re-derived), **DEC on paper** | Skinner Thm A + SW (split case: L-invariant ≠ 0). The Kim alternative is *not* an alternative (n ≈ 5·10¹⁶–7·10¹⁶) |
| **S_4547** | Sha[4547^∞] = 0 | **OPEN ROOT W3** *(was ROUTE_BLOCKED)* | only chain: Kim Thm 1.8 = SEMI (witness existence = Kim Conj. 1.7 at an additive prime: unproved; FW would give it), n = ℓ₁ℓ₂ ≥ 87 256 931 · 92 849 741 ≈ 8.1·10¹⁵ ⟹ ≳ 10²⁴ terms. No cyclotomic p-adic L-function, no main conjecture, no control theorem at this prime (Kim–Nakamura Rem. 1.8). **Both a theory gap and a de-facto computational wall** |
| **H(p₀)** | Sha[p] = 0 for every p > p₀, p ∉ {2243, 4547, 5843} | **OPEN ROOT W1** | §C.1: NOT_FOUND. Must be *effective*, and p₀ must be small: the finite part costs ≈ 0.23·p₀² CPU-h per shared pass (p₀ = 100: ≈ 7·10³; p₀ = 1000: ≈ 2·10⁵; p₀ ≈ 6000: ≈ 8·10⁶) |
| S3 | #Sha[3^∞] = 9 | FINITE_CERTIFICATE_CANDIDATE, DEC, ≈ 14 CPU-h — *label subject to F1* | Skinner Thm A + SW 6.1; cross-routes: visibility (lower), 3-descent + Cassels–Tate (algebraic, cost UNKNOWN) |
| **SRAT** | L″(E,1)/(2ΩReg) = 36 | **OPEN ROOT W2** | §C.2: NOT_FOUND. Sufficient form: ∈ (1/D)Z with explicit D ≲ 3·10¹⁴ (the DAG/NEXT_3_TARGETS figure "D < 10⁷, 36 ± 10⁻¹³" is inconsistent with its own certified radius 3·10⁻¹⁵; harmless) |

**Roots after repair: W1 = H(p₀), W2 = SRAT, W3 = S_4547** — three, not two — plus finite work
{S3, S_ord, S_ss, S_2243, S_5843} of which only the last two are cost-blocked. If a future uniform theorem is of Kolyvagin type
(valid for every odd p with surjective ρ̄_p and p ∤ index, bad primes included — as Kolyvagin's rank-≤1 theorem is in Gross's formulation; that reading is FROM MEMORY, not re-checked at source), W3 and S_2243/S_5843 are absorbed
into W1; if it is of Kato/Iwasawa type (p ∤ N, or p semistable), **W3 survives it**. That asymmetry is why W3 must be listed.

### F.3 The alternative architecture the DAG never mentions

    FULL BSD(E)  ⟺  FIN ∧ FORMULA          FIN: Sha(E/Q) finite (non-effective is enough)
                                            FORMULA: L″(E,1)/(2ΩReg) = 4·#Sha

Given G12, FORMULA forces #Sha = 9, hence S3, S≥7 (every prime, including 4547, 2243, 5843 and all supersingular p) and SRAT,
*with no per-prime computation at all*. This is how ranks 0 and 1 were actually done (Kato/GZ formula + IMC at all p), and it is
the shape BKS Conj. 1.1 + IMC would deliver. The architect's three-statement set is equivalent (any two sets equivalent to FULL
BSD are), and it is the better *computational* decomposition; but "smallest set" is a statement about presentation, and a reader
should know that W3 and the cost-blocked primes disappear entirely in the {FIN, FORMULA} architecture. "Minimal" can only mean
*irredundant relative to known theorems*; in that sense {S3, S≥7, SRAT} **is** irredundant (I found no known implication among
them), and so is {FIN, FORMULA}.

---

## §G. Ranking of the surviving open nodes

Scales: difficulty 1 (routine) – 5 (famous open problem); leverage = how far FULL BSD moves if the node falls; "frontier-model
suitability" = how much a fresh Fable/Mythos-class session (reading + small computations, no big compute) can contribute.

| rank | node | difficulty | leverage | frontier-model suitability | recommended form of attack |
|---|---|---|---|---|---|
| 1 | **Gate for Criterion SS** (supersingular p at depth 2) | 1–2 | medium: unblocks 23, 29, 131, … so that S≥7 below any p₀ ≈ 100–300 is *entirely* feasible; removes a whole class from "blocked" | **very high** — source reading (Pollack §6, Kobayashi §§4, 9, B.D. Kim Thm 1.1, KK §3), sign/normalization bookkeeping, then a 60-s validation on a small-conductor curve with exact modular symbols (e.g. a rank-2 curve at a supersingular p in Sage) | hostile gate exactly like `P3_THEOREM_GATE.md`; then add 23, 29 to the Tier run |
| 2 | **S3** (p = 3 run) | 2 | high: the only non-trivial Sha; after it #Sha[210^∞] is known | high for the audit (F1, in progress), none for the compute | as planned; keep the visibility/3-descent lower bound as an independent cross-check |
| 3 | **G10 → PROVED** (rigorous interval L″ ≠ 0) and the rigorous streaming core | 1–2 | low for FULL BSD (the ⇐ side never uses G10), but it is the trust base of the ⇒ side, of the constant 36, and of every future per-p certificate; the core directory is still empty | high (engineering + audit) | build once, use for H-a and all tiers |
| 4 | **S_ord(p₀), S_ss(p₀)**, p₀ ≈ 100 | 1 (compute) | low–medium: finite progress only; valuable as *data* for W1 (tests the Mazur–Tate mod-p identity at r = 2 on a curve with Sha = 9) | low (compute-bound) | one shared pass; ≈ 7·10³ CPU-h for p₀ = 100 incl. 23, 29 |
| 5 | **W3 = S_4547** | 4 | necessary for FULL BSD unless W1 arrives in Kolyvagin form | **medium–high, and neglected**: a sharply posed local question — transport Forrás–Lei's ± local theory (potentially supersingular, e = 4, j ≡ 1728) from CM curves to E/Q_p, and feed it Kato's Euler system instead of elliptic units, to get a signed divisibility and a Mazur–Tate-element criterion at additive p. Even success leaves a ≈ 5·10⁶ CPU-h vertical computation, so the *real* hope is that W1's eventual exceptional set excludes nothing at 4547 | theory session first; separately, have a referee read Fouquet–Wan §5 for the supercuspidal-at-p case |
| 6 | **S_2243, S_5843** | 2 (theory done) / cost 10⁴–10⁵ CPU-h | low until W1 exists | low; possibly medium for an algorithmic look (the cusps b/p² at p ∥ N have width N/p — is the ≈ 5p²√N term count really optimal?) | defer |
| 7 | **W1 = H(p₀)** | 5 | maximal (first proof of finiteness of Sha in analytic rank 2) | low for a direct proof. **Medium for a precise-formulation + experiment session**: state the Mazur–Tate mod-p leading-term identity at conductor p² for r = 2 (§C.1), verify it numerically for many p on 389a1/433a1 (exact modular symbols, seconds), and look for a p-independent characteristic-zero expression for Σ_a [a/p²]⁺w(a) mod p — the only place a "global object" could be hiding in plain sight | do not spend compute; spend reading |
| 8 | **W2 = SRAT** | 5 | maximal but only after (or together with) W1 | low. No route, no partial result for any curve; by §C.3 any credible attack is the same attack as on W1 (a rank-2 Perrin-Riou/Gross–Zagier object) | none separately |

Relative order of the three roots by *tractability*: W3 (a local-theory gap with a one-week-old CM template) ≫ W1 ≈ W2.
Relative order by *leverage*: W1 ≈ W2 ≫ W3.
