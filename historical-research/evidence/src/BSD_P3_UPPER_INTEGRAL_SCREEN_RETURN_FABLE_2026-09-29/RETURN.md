# RETURN — Lane R24: integral Kato-direction source at nonsplit multiplicative p = 3 (round 2)
**Worker:** Fable 5.1 (claude-fable-5-1), a NEW session, not the B1/R23 session. 2026-09-29.

## STATUS: REDUCED_TO
- **No printed PROOF of T-INT at nonsplit multiplicative p was found** in the list read (scoped
  NO_SOURCE_FOR_THESE for the direct question; NOT ACCESSIBLE items listed below).
- **Reduced to one LOCAL named statement, MS-R24** (an integral Coleman map at nonsplit multiplicative
  p = 3), plus bookkeeping obligations O1, O2, O4 and B1's chain O5. All are listed below, not just the first.
  - The route ("K") is: Kato Thm 12.5(4), which is integral, has no p ∤ N condition and holds for the
    seed at p = 3 (THEOREM, read at source), then Poitou–Tate, then MS-R24.
  - It uses no Hida family, no Skinner–Urban, no Skinner 2016 and no weight-k ≥ 8 comparison.
  - So it avoids MS-B1 and MS-R3 entirely.
- A second sufficient pair (route "M") is recorded too: a rational divisibility M1 (SECONDARY in print)
  plus µ^alg(E/Q∞, 3) = 0 (M2, open).
- Nothing here is a proof of T-INT. The chain to #Sha[3^∞] ≤ 9 is UNAUDITED.

## Collision check: PASS (NOTES.md)
- R24 uses the Kato (upper-bound, Euler-system) direction. That is not the failed Eisenstein
  lower-bound arrow in STRUCTURAL_STOP_REGISTER.
- R1/R2 (DNR rows 4, 27), lane-1 SU items, MS-B1 and MS-R3 are not reopened. There is no FIN claim.

## Item 1 — Stein–Wuthrich "Kato's Theorem 7.3" traced (SRC_SW2013_trace.md)
- **Stated support (SW l.1196-1199):** Kato 17.4, which requires p ∤ N, and Kobayashi 2006.
- **Kobayashi 2006, read in full (SRC_Kobayashi2006.md):**
  - It covers the Tate curve only (Kob l.199-201: "we assume that E is the Tate curve").
  - Its Coleman map is integral, and Col(z^Kato) = L_{p,γ} (l.325).
  - It contains **no divisibility and no Selmer group**, and it does **not** cover the nonsplit
    twist: the construction needs Ĝ_m ≅ Ê over Z_p (l.227).
- **Grigorov 2005:** NOT ACCESSIBLE.
- **Later citers read:**
  - GJPST 2009 (p ∤ 6N);
  - EPW 2006 Thm 5.1.2 (RATIONAL, attributed to Kato: SECONDARY);
  - C.-H. Kim's guide (the Coleman step is written only for good ordinary and supersingular p);
  - Skinner 2016 l.973-980 ("do not follow directly … additional arguments are required").
- **Verdict:** SW 7.3 at nonsplit p is SECONDARY with no located proof (K-R24b FAILS).
  - Its only other hypothesis, ρ₃ surjective, HOLDS for the seed (SRC_Elkies_rho3.md). So proof
    support is the sole defect.
- **By-product:** Elkies's printed j-map (math/0612734, p.5) has a sign typo. SEED_DATA copied it.
  - With "+", the two printed forms agree and Elkies's own examples are hit.
  - The seed's j has no preimage under either sign.

## MS-R24 — the named missing statement (LOCAL, at p = 3)
**Setting.**
- E/Q₃ has nonsplit multiplicative reduction; T = T₃E.
- T⁰ = T₃Ê ≅ Z₃(1)⊗η and T/T⁰ ≅ Z₃(η), with η the unramified quadratic character (η(Frob₃) = a₃ = −1).
- Λ = Z₃[[Gal(Q₃(μ₃∞)/Q₃)]], taken on the Δ-component of the trivial character.

**(MS-R24)** There is a Λ-linear map Col : H¹_Iw(Q₃, T)/H¹_Iw(Q₃, T⁰) → Λ such that:
- it is injective, with cokernel of trivial characteristic ideal;
- Col(loc₃ z_γ) = L₃(E, ω_E, γ) up to Λ^×. Here z_γ are Kato's zeta elements (Ka 12.5), γ is a
  Z₃-generator of T^±, ω_E is the Néron differential, and L₃(E, ω_E, γ) is the Mazur–Tate–Teitelbaum
  3-adic L-function with α = a₃ = −1.

**Why it is plausible, and why that is not a proof.**
- η is nontrivial on G_{Q₃(μ₃∞)}, which is a totally ramified tower. So no trivial zero occurs, and
  H⁰-type cokernels vanish. The nonsplit case is formally the good-ordinary Coleman map with unit
  root −1.
- This is the §17.13 pattern of Kato (p ∤ N) and Kobayashi's Tate-curve map, twisted by η.
- It is NOT in print in the list read. Grade: UNCHECKED.

**Possible discharges of MS-R24 (none read):**
- Rubin 1998, Durham LMS 254, Appendix (Coleman map, ordinary formal groups): NOT ACCESSIBLE.
- Ochiai 2003 (Amer. J. Math. 125), the Λ-adic Coleman map, restated as OS Thm 7.1(iii): integral,
  injective, pseudo-null cokernel under (NOR)+(IRR).
  - Specializing it at the f-point would need (NOR) and a trivial specialized cokernel.
  - The paper itself is NOT ACCESSIBLE.
- Kato–Kurihara–Tsuji 1996 preprint: unpublished.

## Every obligation of route K (T-INT ⟸ O1 ∧ O2 ∧ MS-R24 ∧ O4)
**O1 — Kato 12.5(4) for T₃E at p = 3 (SRC_Kato2004_12.5.md).** THEOREM, with these gradings:
- (12.5.2) holds because ρ₃ is surjective. That is COMPUTED via Elkies's X9; the completeness of the
  Elkies criterion is SECONDARY.
- Alternatively, Skinner's (a)+(b) replacement holds with τ ∈ I_2243 (REMARK grade).
- The absence of (12.5.1) exceptions at nonsplit p is UNCHECKED as a written deduction.

**O2 — Poitou–Tate bookkeeping, from Kato's H²(Z[1/3], T⊗Λ) and H¹/Z(f,T) to the classical
Sel_{3^∞}(E/Q∞)^∨.** It needs:
- (a) the exact sequence 0 → H¹_Iw(T)/Λz → H¹_Iw(Q₃,T)/(H¹_Iw(Q₃,T⁰) + Λ·loc z) → Sel^∨ → Sel₀^∨ → 0.
  Injectivity at the left holds because H¹_Iw(T) is free of rank 1 (Ka 12.4(3), ρ̄ irreducible) and
  loc z ≠ 0 (L₃ ≠ 0).
- (b) Greenberg's local condition at 3 equals the classical one (standard for nonsplit p; the source,
  Greenberg LNM 1716, was not read).
- (c) the local terms at ℓ ∈ {2, 2243, 4547, 5843}. **At ℓ = 5843 this term is NOT trivial.**
  - 5843 is inert in Q∞: ⟨5843⟩ = −5843 ∈ 1+3Z₃ has v₃(−5843−1) = 1.
  - v₃(5843^{3ⁿ}+1) = n+1, so E(Q_{∞,5843})[3^∞] is infinite.
  - So the unramified-versus-classical comparison there has a nonunit characteristic ideal (an
    Euler-factor term), which must be shown to cancel or to go the right way.
  - UNCHECKED; this is the item most likely to hide a power of 3.
- (d) passing to the Δ-trivial component, and Z(f,T) there equal to Λ·z_{γ⁺} (sign rule in Ka 12.5(1)).

**O3 = MS-R24.**

**O4 — normalization.** L₃ in S.3's certificate (SW convention; a_{4,2} = 15480 in ω₁ normalization,
7740 in Néron) must equal L₃(E, ω_E, γ⁺) up to Z₃^×. That needs:
- the Manin constant prime to 3 (SEED_DATA, reading grade);
- γ⁺ generating H₁(E,Z)⁺⊗Z₃ (Ω⁺ versus ω₁ differ by a factor of 2 at most);
- the interpolation factor (1 − α⁻¹) = 2, a unit.
None of this is re-derived here.

**O5 — B1's upper-half steps (as input, UNAUDITED):** ord_T L₃ = 2, the independent height
certificate, and Jones 1989 Thm 3.1 (forward).

## The one-way chain to #Sha[3^∞] ≤ 9 (UNAUDITED; grades of the inputs as above)
1. O1 ∧ O2 ∧ MS-R24 ∧ O4 give char(Sel^∨) | L₃ in Λ:
   char(Sel^∨)·char(H¹/Λz) = L₃·char(Sel₀^∨), and char(Sel₀^∨) | char(H¹/Λz) by O1. This is T-INT.
2. Kato 18.4 and rank 2 give ord_T L₃ ≥ 2. The certificate gives a₂ ≠ 0 with v₃(a₂) = 2, so
   L₃ = T²h with v₃(h(0)) = 2. Schneider/Jones give ord_T f_E ≥ 2, so f_E = T²g, g | h, and
   **v₃(g(0)) ≤ 2**.
3. Sha[3^∞] is finite (Kato 18.4; R23 route 3(a), checked).
4. Jones Thm 3.1 forward, with B1's height certificate, turns v₃(g(0)) ≤ 2 into #Sha[3^∞] ≤ 9.
5. With B2 (⊇ (Z/3)², certified) and Cassels–Tate: Sha[3^∞] ≅ (Z/3)².
   This would bypass Skinner Thm A, SU and GRH.

## Route M — a second sufficient pair (recorded; neither half proved)
- **Lemma (mine, elementary).** f_E | L₃ in Λ ⟺ [f_E | L₃ in Λ⊗Q₃] and [µ(f_E) ≤ µ(L₃)].
  - Proof: if µ(f_E) = 0, write f_E = P·U with P distinguished. Weierstrass division gives L₃ = qP + r
    with q ∈ Λ. Rational divisibility plus uniqueness of division (after scaling by pⁿ) gives r = 0.
  - The general case is the same, with µ-exponents.
- **M1:** rational divisibility at nonsplit p. SECONDARY only: EPW06 Thm 5.1.2 and SW 7.3 ⊗ Q, both
  attributed to Kato, whose printed §17 excludes p | N. Kato §18 prints only the corank bound at s = 1.
- **M2:** µ^alg(E/Q∞, 3) = 0. This is equivalent to Sel(Q∞, E[3^∞])[3] being finite (EPW06 Thm 3.1.1, l.1266-1270).
  - It transfers between members of the Hida family H(ρ̄) (EPW06 Thm 1). The seed's ρ̄ is
    p-distinguished: ωη ≠ η.
  - It is an instance of Greenberg's µ = 0 conjecture. No member with µ^alg = 0 is known here.
  - No local test.

## Candidates: K-R24a (first failing hypothesis) and K-R24b
| Source | Grade | K-R24a first failure | K-R24b |
|---|---|---|---|
| SW 2013 Thm 7.3 | SECONDARY | none (ρ₃ surjective by computation) | FAILS (cited proofs exclude nonsplit) |
| Kobayashi 2006 | THEOREM | nonsplit (Tate curve only); no divisibility at all | n/a |
| Grigorov 2005 | — | NOT ACCESSIBLE | — |
| Kato 2004 12.5(4) | THEOREM | "p-adic L attached": fails (Kato's formulation) | covers p ∥ N: yes |
| Büyükboduk IMRN 2011 | THEOREM | p = 3 (Kato example needs p > 3); no p-adic L | not reached |
| Büyükboduk 1303.1407 | PREPRINT copy | p = 3 (p ≥ 5); squarefree level | not reached |
| Ochiai–Shimomoto 1706.01571 | PREPRINT | (iii) at ℓ = 5843: H²(Q_5843, T) ≠ 0 (3 ∣ 5844) | not reached |
| Fouquet–Wan 2107.13726 | PREPRINT | residual (ρ̄|G_Q3)^ss = η ⊕ χ̄cyc·η excluded | not reached |
| Delbourgo 2006 | THEOREM | p = 3 (p ≥ 5); rank 0 | not reached |
| Delbourgo 2008 book | — | NOT ACCESSIBLE | — |
| Kitagawa 1994 | — | NOT ACCESSIBLE; step (14) graded via OS Thm 6.10 | — |
| EPW 2006 | THEOREM | Thm 5.1.2 rational (integrality fails) | SECONDARY |
| EPW 2022 | PREPRINT | (Irred) at p fails; constant C | not reached |
| arXiv sweep 2016–2026 | — | see SRC_SEARCH_2016_2026.md: none applies | — |

## Changes to earlier records (proposals for the checker; NO record edited)
- **2(b):** arXiv:1706.01571 is Ochiai–Shimomoto. It does NOT weaken MS-R3 checkably: it trades
  regularity for (NOR) but adds hypothesis (iii), which FAILS at 5843.
- **2(e):** Ochiai's step (14) (the p-adic period is a unit) at the weight-2 point: REMARK → SECONDARY,
  via OS Thm 6.10 (restating Kitagawa, weight ≥ 2 including 2, p > 2, under (IRR)).
  - An intermediate reading of mine that flagged weight 2 as excluded was WRONG and was corrected
    (NOTES.md).
- **SEED_DATA:** "ρ₃ surjective: UNCHECKED at source" can become COMPUTED (Elkies; completeness
  SECONDARY). SEED_DATA's recalled j-map carries Elkies's printed sign typo.
- **New seed fact (PARI):** E(Q_5843)[3] ≅ Z/3, and it grows along Q∞. This affects any source with a
  local H² = 0 or Tamagawa-type hypothesis at 5843, and obligation O2(c).

## NOT ACCESSIBLE / NOT LOCATED (no claim either way)
Grigorov 2005 thesis; Delbourgo 2008 (LMS LN 356); Kitagawa 1994; Rubin 1998 (Durham appendix);
Ochiai 2003 (AJM); Kato–Kurihara–Tsuji 1996 preprint; Sakamoto "Kolyvagin systems for p = 3" (not on
arXiv by author query); the Glasgow Math. J. paper on potentially ordinary p; Kobayashi's journal PDF
(EMIS mirror refused; the arXiv v1 text was read instead).

## Grades (kept separate)
- **THEOREM, read at source:** Kato 12.5(4) and 18.4; Kobayashi 4.1/4.2; Delbourgo 1.4;
  Büyükboduk Thm A; EPW06 Thms 1, 2, 5.1.3.
- **REMARK:** Skinner's (a)+(b) replacement; Büyükboduk 1303.1407 Rem 1.8.
- **SECONDARY:** SW 7.3 at nonsplit p; EPW06 Thm 5.1.2; OS Thm 6.10 (Kitagawa); completeness of the
  Elkies criterion.
- **PREPRINT:** OS 1706.01571; Fouquet–Wan; EPW 2022; Kim 2203.x and 2404.05186.
- **UNCHECKED:** MS-R24; O1's (12.5.1) remark; O2(a)–(d); O4; the Route-M lemma is mine but
  elementary; the whole chain.
- **COMPUTED:** ρ₃ surjective; the local data at the bad primes (checks_*.gp; PARI 2.17, run040 env).
  Total CPU is a few seconds, one process at a time, no subagents.

## Files
- NOTES.md, RESUME.md, STATE.json (written first)
- SRC_*.md (11 files); checks_elkies_rho3.gp and checks_local_data.gp
- sources/ with SOURCES.sha256 (URL + sha256 per file)
- MANIFEST.sha256
- No pushes, messages, prime runs or paid compute. Nothing was written outside this folder except scratchpad files and one
  early /tmp download (claude_k.pdf, deleted at once; see NOTES).

FIN, ORDER9 and Q36 are unchanged.
