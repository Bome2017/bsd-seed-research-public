# Integral Bertolini–Darmon reciprocity at a fixed admissible prime: REPORT (Claude, Opus 5.5, 2026-10-07)

**Verdict: `INTEGRAL_LAW_NOT_AVAILABLE_IN_BD`.**
- Scope: BD05 and H06 as read (§1).
- Trigger: clause (i) of the pre-registered kill test. Thm 5.17 and the freeness / multiplicity-one inputs are stated and proved only after p is chosen, and neither source has an integral version.
- Clause (ii) did **not** fire. The unit ambiguity is not intrinsic.
- Step 3 (the seed's depth-2 statement and the first lemma for GATE.md) was **not run**, per the rule.
- FIN, ORDER9 and Q36 are unchanged.

**Sub-finding `UNIT_AMBIGUITY_NOT_INTRINSIC` (DERIVED, same-session, unreviewed).**
- The "unavoidable" ambiguity of BD's remark (p. 37) comes from stating the laws in Λ/pⁿ, that is, in the cohomology of T_{f,n} = E[pⁿ].
- Restated in BD's own integral modules, every unit except a global sign disappears. The Thm 5.17 unit cancels in a u-balanced depth-2 invariant.
- So the stop is a stop on what the sources contain, not an impossibility.

**The answer in six points**

1. **The geometric half of BD's chain is already integral in BD05.** These are statements over Z with no p:
   - Čerednik–Drinfeld (Thm 5.1), character groups (Props 5.2–5.9) and JL (Cor 5.10);
   - component groups (Props 5.11, 5.13, 5.14);
   - the reduction of Heegner points to CM vertices (§8).
2. **p enters at exactly three non-tower places:**
   - the freeness hypothesis of Thm 5.15 (a completion at m_f);
   - the isomorphism u : Ta_p(J^{(ℓ)})/I ≅ T_{f,n} of Thm 5.17 (existence only, unique up to (Z/pⁿ)^×);
   - the "by multiplicity one … up to (Z/pⁿZ)^×" step of §8 (p. 69).

   Everything else p-adic (Λ, α_p, conductor p^{m+1}, p | N⁺, the p-tree) belongs to the anticyclotomic tower and is absent at the bottom layer. Howard is p-local by definition, and his laws record only valuations.
3. **Depth 1, the endpoint's best case: exists, and is vacuous for the seed.**
   - Read Φ_ℓ/I through f by ρ_f(ω̄_ℓ(x,y)) = f(x) − εf(y). This is BD's p. 59 computation done over Z (checked: 16/16 cases).
   - The first law then becomes one identity mod m for all p | m at once: ρ_f(∂_ℓ[D_ℓ]) = ±Σ_σ f(x_σ).
   - It needs neither Thm 5.17 nor multiplicity one.
   - For the seed both sides are 0, since L(E,1)·L(E^{−7},1) = 0 (record R4).
4. **The CRT trap.** Gluing BD's p-local laws by CRT gives laws mod m up to (Z/m)^× = ∏_p(Z/p^{n_p})^×. That is the same information, so integrality alone adds nothing across p. The Thm 5.17 isomorphism has no geometric source, because Hom(J^{(ℓ)}, E) = 0.
5. **Depth 2 can be normalized with no unit at each p.** Define

     **C(ℓ₁,ℓ₂) := Ξ₁(β₁(x′_K)) / R(ℓ₁,ℓ₂) ∈ Φ_ℓ₁/I ≅_{ρ_f} Z/m.**

   - β₁(x′_K) is the image of the Gross divisor of S′ (disc N⁻ℓ₁ℓ₂) under BD's §9 maps (62)–(65).
   - R(ℓ₁,ℓ₂) is the 2×2 determinant of the reductions of a basis P₁, P₂ of E(ℚ).
   - Ξ₁ is a canonical isomorphism, built from Hom_{G_ℚ}(E[m], T(J₁)/I) (a module, no generator), Cor 5.18 and Tate duality for E.
   - u never appears. Every u-dependent object has total u-weight 0, so C is canonical up to a single global sign.
   - C is Ш-free by definition.
   - BD + Howard prove only v_p(C) = δ_p, independent of the pair.
6. **The natural law has the strength of FIN.** Call it RIGID_LR: C(ℓ₁,ℓ₂) ≡ ±C_E for one rational C_E. By H06 Thm 2.3.7 it implies Ш(E/K)[p] = 0 for every good p ∤ C_E. So it is a target statement in a new coordinate (the number of level-raising primes), not a way around the open problem (equivalent ≠ circular).

---

## 0. Endpoint check and kill test (written first; RESUME.md, start of session)

**Endpoint.**
- No FIN effect.
- Best case: a p-free (integral) depth-1 law at fixed ℓ, as an identity in Φ_ℓ ⊗ (T/I), holding for all p dividing the level-raising congruence modulus at once.
- This matters only if a depth-2 version at fixed (ℓ₁, ℓ₂) can then be pinned without unit ambiguity.

**Kill test (verbatim).** "If Thm 5.17's identification or the multiplicity-one/freeness input exists only after choosing p (no integral version in the sources), or if BD's remark shows the unit ambiguity is intrinsic → record INTEGRAL_LAW_NOT_AVAILABLE_IN_BD (scoped) and stop."

**Outcome against the endpoint.**
- The best-case depth-1 law exists in derived form (point 3), and is 0 = 0 for the seed.
- The depth-2 object can be pinned without a unit at each p (point 5).
- A depth-2 *law* with a fixed constant is not in the sources, and has the strength of FIN (point 6).
- No FIN effect, as predicted.

## 1. Sources read

| Tag | Source | Version | Parts read |
|---|---|---|---|
| BD05 | Bertolini–Darmon, *Iwasawa's main conjecture for elliptic curves over anticyclotomic Z_p-extensions*, Ann. of Math. 162 (2005) 1–64 | preprint from Darmon's site, dated 5 Sep 2007; page numbers are the preprint's; local text `~/BSD_YUN_ZHANG_MECHANISM_READING_2026-10-07/sources/BD2005.txt` | §1 in full (pp. 7–16); §2.1–2.3 (pp. 16–25); §3.2–3.3 (pp. 26–36); §4.1 and the end of §4.2 (pp. 36–43); §5 in full (pp. 44–65); §§6–9 in full (pp. 65–76) |
| H06 | Howard, *Bipartite Euler systems* | arXiv 1202.6353v1; the J. reine angew. Math. 597 (2006) citation was not re-verified | §1; §2.1–2.3 (pp. 3–9) with Def 2.3.2 and Thm 2.3.7; Thm 2.5.1 and its proof (p. 13) |
| record | `BSD_ARISTOTLE_RANK2_ANCHOR_RETURN_2026-10-06/RESULT_RANK2_ANCHOR.md` R4 and §3; `BSD_YUN_ZHANG_MECHANISM_READING_2026-10-07/REPORT.md` §4, §8; `BSD_TAME_LAW_EXACTNESS_TEST_2026-10-07/REPORT.md` §6; GATE.md | — | as cited |

`checks/pageof_output.txt` maps every cited line of the text files to its PDF page. The monotone footer chain has 81 pages.

## 2. Step 1: Thm 4.1, its proof chain, and where p enters

Full table: `notes/02_step1_p_entry_map.md`.

**Statement (p. 36).** For an n-admissible ℓ, v_ℓ(κ(ℓ)) = 0 and ∂_ℓ(κ(ℓ)) = L_f (mod pⁿ) in Ĥ¹_sing(K_∞,ℓ, T_{f,n}) ≃ Λ/pⁿΛ, "up to multiplication by elements of Z_p^× and G_∞".

**Remark (p. 37), verbatim.** "Note that the ambiguity in the statement of theorem 4.1 is unavoidable, since the identification of H¹_sing(K_∞,ℓ, T_{f,n}) with Λ/pⁿΛ, and the element L_f, are both only defined up to multiplication by elements in Z_p^× and G_∞."

**Chain:**
- C0: the form f on the p-tree, Prop 1.4.
- C1–C2: the integral geometry, §5.1–5.5.
- C3: Thm 5.15.
- C4: Thm 5.17.
- C5: Cor 5.18.
- C6: §§6–7, the Heegner points and the class κ.
- C7: Lemma 8.1.
- C8: the reduction step of §8.
- C9: the multiplicity-one step of §8.

| Class | Where p enters | Removable at the bottom layer? |
|---|---|---|
| **T** (tower) | Λ and G_∞ (edges e_j, primes λ_m); α_p^{−j}; conductor p^{m+1}; p ∣ N⁺ in §5.6 and §9; strong approximation to the p-tree (p. 69) | yes: use conductor-1 Heegner points on X_{N⁺,N⁻ℓ} with p ∤ N⁺ (not BD's setting; the C8 argument does not use p) |
| **C** (coefficients) | Z/pⁿ, Ta_p, the p-part of Φ_ℓ/I | yes: Z/m, T(J) = ∏_{p∣m} Ta_p, Φ_ℓ ⊗ T_ℓ/I |
| **N** (normalizations, the unit sources) | N1: f up to Z_p^× (p. 12, p. 16). N2: G_∞. N3: abstract isomorphisms Φ_ℓ/I ≃ Z/pⁿ (Thm 5.15), H¹_sing ≅ Z/pⁿ (Lemma 2.6), H¹_fin(K_ℓ₂) ≅ Z/pⁿ (p. 70). N4: u (Thm 5.17; Aut = (Z/pⁿ)^×). N5: the (Z/pⁿ)^× of C9, which is caused by N3 | N1: ±1. N2: trivial. N3, N5: replaced by ρ_f. **N4: cancels in C(ℓ₁,ℓ₂)** (§3) |
| **H** (hypotheses on p) | H1: admissibility (p ∤ ℓ²−1, pⁿ ∣ ℓ+1−εa_ℓ). H2: GL₂(F_p) image, p ≥ 5. H3: p-isolated (Prop 3.6, via Wiles R = T). H4: p ∤ modular degree. H5: Assumption 6.4. H6: non-Eisenstein | finitely many p for fixed (E,K), or a set fixed by ℓ. They are conditions, not choices |
| **E** (proved one p at a time, existence only) | E1: [BoLeRi]. E2: Nakayama (Thm 5.17). E3: [DT] Ihara lemma + Nakayama (Prop 9.2). E4: freeness (Thm 5.15(2)) | used only for existence; the choices they leave cancel (§3) |

**Howard.**
- The setting is local by definition: "Let R be a principal Artinian local ring with maximal ideal m and residue characteristic p > 3" (p. 3).
- The laws are "there exists an isomorphism of R-modules R/(λ_n) ≅ H¹_ord(K_l,T)/R·loc_l(κ_{nl})" (Def 2.3.2, pp. 7–8).
- The rigidity proof modifies "the vertex-to-edge maps (3) by an element of R^× if needed" (Thm 2.5.1, p. 13).

**Why neither source pins the unit.** BD's Thm 4.4 needs only Fitting ideals (pp. 37–43), and Howard needs only ind(·). Neither ever needs the unit. So its absence from the sources is not evidence that it is intrinsic.

## 3. Step 2: the integral test

Full derivations: `notes/03_step2_integral_test.md`.

### 3.1 What BD05 already proves over Z (SOURCE)

- Thm 5.1.
- Props 5.2–5.9. Prop 5.9's remark says the identifications "can be made entirely canonical" (p. 53).
- Cor 5.10; Props 5.11, 5.13 (Eisenstein kernel and cokernel) and 5.14.
- Sequence (49).
- The reduction step of §8.
- The relations of Lemma 9.1 and Ihara's isomorphism (66).

Together they give, in Φ_ℓ itself: the component of a Heegner divisor is ω_ℓ of the divisor of its CM vertices.

### 3.2 Derived integral statements

| # | Statement | Inputs | Grade |
|---|---|---|---|
| D1 | Integral Thm 5.15: for m ∣ ℓ+1−εa_ℓ prime to the bad set B (2, 3; primes dividing ℓ²−1, N or η_f; the primes failing H2–H6; Eisenstein primes), ρ_f : Φ_ℓ/I ≅ Z/m, ω̄_ℓ(x,y) ↦ f(x) − εf(y), canonical up to a global sign | Prop 5.13; the p. 59 matrix computation over Z (`checks/integral_2x2_check_output.txt`: Smith normal form diag(1, ℓ+1−εa_ℓ), 16/16 seed cases); (m, η_f) = 1 as a sufficient integral form of hyp. (2) | DERIVED |
| D2 | Integral first law: ρ_f(∂_ℓ[D_ℓ]) = ±Σ_σ f(x_σ) (mod m), for all p ∣ m at once. For the seed it reads 0 = 0 | D1 and §3.1; the parity of the CM vertices is consistent with (61) (HEURISTIC detail) | DERIVED; tautological |
| D3 | Transport to E[m]: u exists (Thm 5.17 at each p, then CRT) with Aut = (Z/m)^×, and is not induced by any morphism J^{(ℓ)} → E. So BD's laws as printed carry an independent unit at each p | Thm 5.17; Schur; V_p(E) is unramified at ℓ while J^{(ℓ)} is ℓ-new | DERIVED from SOURCE |
| D4 | **C(ℓ₁,ℓ₂) is canonical up to a global sign** (definition in point 5). If Ш(E/K)[m] = 0, then C(ℓ₁,ℓ₂) = −c_J(ℓ₁), independent of ℓ₂, and v_p(C) = δ_p (H06 Thm 2.5.1) | Cor 5.18's geometric map; Tate duality for E; Hom_{G_ℚ}(E[m],T(J₁)/I) free of rank 1; BD (62)–(65); Thms 4.1–4.2 | DERIVED |
| D5 | RIGID_LR (C ≡ ±C_E) implies Ш(E/K)[p] = 0 for every good p ∤ C_E | H06 Thm 2.3.7 (p. 9); the strict Selmer group lies inside Sel_{F(ℓ₁ℓ₂)}; Chebotarev (BD Thm 3.2 / H06 Lemma 2.3.3) | DERIVED |

### 3.3 Kill test

- **(i): FIRES as worded.**
  - Thm 5.17 is proved through [BoLeRi] mod p, Nakayama over Z/pⁿ and the GL₂(F_p) image (pp. 61–62).
  - Freeness is a completion at m_f (p. 58). Multiplicity one enters mod pⁿ (p. 69). The Ihara step is mod p plus Nakayama (p. 73).
  - H06 is local by definition.
  - Neither source has an integral version.
- **(ii): does not fire.**
  - The remark blames normalizations, not lost information.
  - D1–D4 dispose of each of N1–N5: N1 and N2 are trivial or ±1, N3 and N5 are replaced by ρ_f, and N4 cancels.

## 4. Consistency with the record

No kill is resurrected and no grade changes.
- **R4 (rank-two anchor return).** Consistent and sharpened.
  - R4 at the trivial character is the 0 = 0 of D2.
  - R4's "input that would change it" asks for a derived formula with an exact Ш-free constant against a 2×2 regulator. C(ℓ₁,ℓ₂) is the BD-side object of exactly that shape, in the level-raising coordinate.
  - Its constancy is open (D5).
- **Derived-Gross return.** The augmentation direction is vacuous on E(ℚ). C(ℓ₁,ℓ₂) lives in the level-raising direction (number of primes), so the two do not overlap.
- **YZ reading §4.** "BD and Howard give only δ_p" is confirmed (D4). The new point is that the unit part is **definable** without p; it is just not determined by the sources.
- **Tame-law RIGID.** RIGID_LR is the level-raising analogue of the record's tame law. Both are integral identities, one per level, with a Ш-free definition. Like G1, RIGID_LR has the strength of FIN (D5, and RESULT_RANK2_ANCHOR §3, "any success needs new input").
- **Seed facts (light check, `checks/seed_facts2_output.txt`).**
  - N = 2³·3·2243·4547²·5843. N⁻ = 3·2243·5843: three primes inert in ℚ(√−7), so the setting is definite. N⁺ = 2³·4547².
  - Root numbers +1 (E) and +1 (E^{−7}). Torsion ℤ/2. Tamagawa product 16.
  - ℓ = 283 is admissible for p = 5 and p = 7 with the same sign ε = −1 (ℓ+1+a_ℓ = 280). So one law at ℓ = 283 covers both primes.
  - The seed's definite Shimura set has mass ≈ 5.4·10¹⁴ (`checks/integral_2x2_check_output.txt`). Seed-size quaternion computations are infeasible.

## 5. What this does not show

- C(ℓ₁,ℓ₂) is **defined**, not shown to be constant. No numerical value was computed for any curve.
- D1–D5 are same-session derivations, unreviewed. The record's own rule says same-session re-checks repeat slips, so they need an independent check before use.
- The bottom-layer setting (conductor-1 Heegner points, p ∤ N⁺) is not BD's. The §8 argument transfers, but it was not checked against integral models at non-squarefree N⁺; the seed has 4547² ∣ N⁺, with additive reduction (types III and I₁*).
- η_f (needed for D1) is not computed for any curve, and is infeasible for the seed.
- Sign conventions are not fixed.
- Nothing links C(ℓ₁,ℓ₂), which lives over K in the level-raising coordinate, to the record's tame scalar s_p, which lives over ℚ in the cyclotomic-tame coordinate. That would need a separate comparison.
- The conjectural value of C_E is not derived. By analogy with Gross / Gross–Zagier, the known formulations' constants include #Ш (record R3/R4, HEURISTIC).

## 6. Next attack (named, not run; this stop is by the rule)

1. **NA-1, reading (cheap).** Does any source state a BD-type law with an explicit generator (like ρ_f), or compare canonical normalizations exactly across level raising?
   - Candidates, not yet read: Pollack–Weston (Compositio 2011); Kim–Pollack–Weston (freeness of anticyclotomic Selmer groups); Chida–Hsieh (Compositio 2015; Crelle 2018); W. Zhang, "Selmer groups and the indivisibility of Heegner points" (Camb. J. Math. 2014), Jochnowitz-congruence normalization; BD 1999 (AJM, Jochnowitz congruences); Vatsal (Duke 2003); Gross–Parson; Ribet–Takahashi; Darmon 1992 (refined conjecture).
   - **Kill:** if each states its laws only up to units or one p at a time, record `NO_UNIT_PINNED_LAW_IN_LITERATURE` (scoped).
   - **Endpoint:** none on FIN.
2. **NA-2, the first lemma, then a sealed probe.**
   - First lemma: a formula for Ξ₁∘β₁ computable from definite data only (Brandt modules at discriminants N⁻ and N⁻ℓ₁ℓ₂, with Ribet's canonical bimodule maps), so that no Heegner points on X^{(ℓ₁)} are needed.
   - Then a sealed RIGID_LR probe on small rank-2 curves in the definite setting. Example: 389a1 with K such that 389 is inert and rank E^K(ℚ) = 0. Then S has mass ≈ 32, and S′ at disc 389·ℓ₁·ℓ₂ with ℓ ≈ 50 has mass ≈ 8·10⁴.
   - **Kill:** C(ℓ₁,ℓ₂) mod p varies over a sealed set of pairs (beyond the global sign) → `RIGID_LR_FALSE` (scoped).
   - **Endpoint:** none on FIN; evidence-only, like the tame-law test.
   - **Gate pre-screen:** RIGID_LR is itself the cross-p input (gate check 2). Like G1, it is a target, not an admitted lane.

## 7. Files

- `RESUME.md`, `STATE.json`: endpoint check and kill test (written first), then the log.
- `notes/01_reading_log.md`: line-cited reading notes for BD05 §§1–9 and H06.
- `notes/02_step1_p_entry_map.md`: step 1 (statement, chain C0–C9, p-entry classification).
- `notes/03_step2_integral_test.md`: step 2 (§2.0 CRT trap; D1–D5; kill test clause by clause).
- `checks/pageof.py`, `checks/pageof_output.txt`: citation → page map for BD05 and H06.
- `checks/seed_facts.gp`, `checks/seed_facts2.gp`, `checks/seed_facts_output.txt`, `checks/seed_facts2_output.txt`: seed conductor, N^±, root numbers, admissible-prime census for p ∈ {5, 7, 11, 13}. The first script's analytic-rank call timed out at 60 s; the record has the ranks.
- `checks/integral_2x2_check.py`, `checks/integral_2x2_check_output.txt`: the integral 2×2 step (16/16) and the seed's Shimura-set mass.
