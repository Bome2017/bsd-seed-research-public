# Check of the five RUN_NOW returns (Claude, Opus 5.5, 2026-09-29)

**Cross-model** (Opus checking Fable returns): lanes 1, 2 and 5. **Same-model** (Opus checking Opus returns): lanes 4 and 6.
The same-model checks are recorded at that grade, and a cross-model check by the Fable coordinator is still owed.
Lane 3 (bad primes) is still running and is not checked here.

**Integrity.**
- Manifests: lane 1 8/8, lane 2 67/67, lane 4 16/16, lane 5 32/32, lane 6 18/18.
- Every replay ran in a copy under Claude's scratchpad. The return folders were not touched.

## Lane 1: P3 residual. REDUCED. Verdict: CONFIRMED at source and arithmetic depth (cross-model)

**Verified against the SU author copy**
(`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/p3_r1_r2_2026-09-19/sources/SkinnerUrban_MC.txt`):
- **The Euler factors disagree.** (12.3.5.b) as printed has det(1 − ℓ⁻¹·trace(…)) (l.11768). SU's own (3.4.5.b) has
  det(1 − q_v⁻¹ε_Kρ(frob_v)) (l.2163).
- **The μ step.** "The µ-invariants of the left and right-hand sides of (12.3.5.b) are the same" is followed by "by
  Theorem 1.1 of [Va03] these µ-invariants are zero" (p.202). Vatsal's theorem controls only the primitive factor.
- **Prop 12.3.6.** Its hypotheses are exactly as quoted. The proof needs some φ(aᵢ) ∈ A^×.
- **SU cites 12.3.6 at four lines:**
  - l.2308, a remark;
  - l.6122, the use repaired here (U2): "by Proposition 12.3.6 ordP(L1) = 0 if …";
  - l.11788, the statement itself;
  - l.12827, the use still open (U1): "Part (ii) follows from part (i) and Proposition 12.3.6".

**Arithmetic.**
- kp1.gp and kp2.gp replay: a₂₂₄₃ = 1 (I₁), 5843 is I₂, and v₃(1 − q⁻²) = 1 at 2243 and at 5843.
- M⁻ must be 2243 or 5843.
- 2, 2243, 4547 and 5843 are all ≡ 2 (mod 9), which is condition (h) of Lemma U2.
- In general v₃(1 − q⁻²) ≥ 1 for every q ≠ 3.

**Logic.**
- E = 1 − 2243⁻²·(…) is a non-unit, since it is ≡ 0 mod 3.
- The printed 12.3.6 implies E ∤ L^Σ.
- So if L^Σ/E is integral, which is CONJECTURE, the printed Prop 12.3.6 fails for this seed.

**Not re-derived by Claude:** every step of the Lemma U2 proof (SU pp.37 and 98), and (S1)–(S3).

**Record consequence.**
- S.3 still rests on Skinner 2016 Thm A as printed.
- The recorded "provenance limit" is now one named statement: the printed proof, for this curve, needs
  (MS-13.4.1(ii)), and that is unproved.
- Proposed v0.2.5 wording: sharpen S.3's qualification. Changing its grade label is the user's decision.
- This is the most consequential finding of the five. A cross-family check is worth Codex's remaining budget if any
  is spent.

## Lane 5: Theorem W^(k) and G2^(k). PROVED and GAP-closed. Verdict: CONFIRMED at replay depth (cross-model)

- `checks/run_all.sh` replays all 7 scripts byte-identically: kpk1, kpk2, singletons, composita, g2k ×2, and
  level1 vs level2.
- **Lemma F** (the G2^(k) gap) was verified by Claude by hand.
  - For p ≥ 3, [GL₂(F_p), GL₂(F_p)] = SL₂(F_p), so the maximal abelian subextension of Q(E[p]) is Q(μ_p).
  - Then Q(E[p]) ∩ Q(μ_{p^{k+1}}) = Q(μ_p), and the fibered product is realized.
  - (−I, 1 + p^k) is admissible, since det(−I) = 1 ≡ 1 + p^k (mod p).
- **K-PK1** was independently confirmed by Claude. In Z/p^k[C_{p^k}], N = Σ C(p^k, j+1)(σ−1)^j, and the surviving terms
  have p | j+1. So N ∈ I^{p−1} ⊂ I³ for p ≥ 5.
- Lemma S (the Smith-form uniform version) is consistent with the retained, Codex-audited Kato factorization. Claude
  did not re-derive it line by line.
- **Value:** optional (Codex B item 12). No endpoint effect. The corrected G2^(k) is a genuine repair of an unreviewed
  sketch.

## Lane 6: fresh sweep. NO_NEW_ROUTE_FOR_THESE. Verdict: CONFIRMED as scoped (same-model spot-check)

- **Two hits spot-checked** at the level of their written reasoning:
  - H01 (Van Order 2510.10277): its main theorem is a FIRST-derivative formula. For the seed,
    ord L(E/K,s) ≥ ord L(E,s) = 2 for every K, so Λ′(E/K,1) = 0 and Cor 1.3's ord = 1 hypothesis fails. Sound.
  - H04 (Castella–Liu–Wan 2608.29470): "N squarefree" fails for the seed. Sound. It is kept as a WATCH item and does
    not bear on FIN's quantifier.
- **Part (b) was correctly not run.** No specific relation surfaced (PARTS_MAP l.269, l.891–895).
- **Limit:** a spot-check cannot rule out false negatives. The coverage (33 monthly listings, keyword and author filters,
  7 papers at theorem level) is recorded in `SWEEP_COVERAGE.md` and `coverage/`. A cross-model re-sweep is owed.

## Lane 2: audit of 17/19/23/29. PASS ×4 (same-family audit). Verdict: CONFIRMED at replay depth (cross-model)

- **Replayed in a copy with the original outputs removed:** items 2–4 for all four runs (exact intervals, coefficients,
  every primitive root, and the altered-table controls), plus item 1 for p = 23 (bindings).
- **Every item is identical** to the return's JSON, ignoring the timing fields.
- **Not replayed by Claude:** item 5 (the frozen checker replay), item 6 (hypotheses), and the recombination extra.
- **The c₂ values match the original certificates:** 7, 6, 9 and 6 at 17, 19, 23 and 29.
- **The grade is stated honestly:** MODEL_SAME_FAMILY. The observation about thin margins at 17 and 23 (radius ≈ 99% of
  the half-spacing) is worth keeping: the identification is exact, but it has little slack against an error in the
  retained tail bound.

## Lane 4: tame constant. DERIVED_AND_CALIBRATED. Verdict: CONFIRMED at replay depth (same-model)

- **All four scripts** (kill_389a1, controls, replay, curves) replay IDENTICALLY once PARI's "increasing stack size"
  warnings are removed.
  - The original outputs captured stderr; Claude's replay kept it separate.
  - There are no other stderr lines.
  - The raw "differences" are only those warnings, which probably explains what the Fable coordinator saw.
- **The result corrects Claude's hypothesis.** K_E = 4·c∞·#Sha·Tam/tors², where c∞ = #π₀(E(R)). That is 8·L^alg for
  Δ > 0 and 4·L^alg for Δ < 0.
  - The seed has Δ > 0, c∞ = 2 and Tam/tors² = 4, so K_E = 32·#Sha and 288 = 32·9.
  - "2³" is now derived (4·c∞), not fitted. This is consistent with Codex's c_per = 1/2 for the seed.
- **Grade.** The derivation is conditional on BKS Conj 2.3. The calibration is exact rational computation on 6 curves:
  68/68 rows with R ≠ 0, and 7/7 zero rows with C₂ = 0. K ≡ 288 is CONSISTENCY evidence for MT with #Sha = 9. It is not
  proof, and it says nothing about q (DNR 17).
- **Still owed:** a cross-model check by the Fable coordinator, which is in progress.

## Record actions proposed (the user decides; nothing below has been applied to the release)

1. **v0.2.5 draft, S.3 qualification.** Replace "recorded provenance limit" with the precise statement: the printed
   proof of Skinner Thm A for this seed needs SU Prop 13.4.1(ii) (MS-13.4.1(ii)), because SU Prop 12.3.6's printed proof
   fails at inert 2243 for p = 3. One consumer (U2) is repaired.
2. **v0.2.5 draft, the 17–29 qualifier:** "independent same-family model audit PASS (Fable 5.1), 1,140 intervals".
3. **K288 records:** replace the fitted "×2^k" with the derived K_E = 4·c∞·L^alg (MT_PRESCREEN, overview S5).
4. **Optional candidate rows:** Theorem W^(k) and the corrected G2^(k) (lane 5). The lane 6 preprints go on the
   watch list.
5. **If any Codex budget is spent,** lane 1 is the item that most deserves a cross-family check.

FIN, ORDER9 and Q36 are unchanged.

## Addendum (after the Fable coordinator's flags, 2026-09-29 ~11:50)

- **Flag on lane 5 ("does Lemma S hide a finiteness assumption?"): none found at source.**
  - BKS Prop 5.1 is Kato's explicit reciprocity plus interpolation (3).
  - Prop 5.2 is pure homological algebra: RΓ_f(F,T) = [P_F → E₁(F_p)* ⊕ Q_F], and π_{F,f} is ∧ψ_{f,i}, i.e. det ψ_f.
  - Cor 5.3 combines the two. [7, Th. 4.3] and Kataoka L4.2 need only Hyp 2.2.
  - Lemma S's own steps (2)–(3) use H¹_f(Q,T) ≅ Z_p^{2+d_p} and H²_f = Sel^∨ in general. They do NOT use BKS's
    finite-Sha identification H¹_f ≅ Z_p⊗E(Q).
  - Case (a) is multilinearity: the last s rows lie in I. Case (b) is the audited Kato factorization.
- **Flag on lane 1** (a source-level check of the SU inconsistency): done above, from the SU text, l.2163, l.11768,
  p.202, l.6122 and l.12827.
- **Flag on lane 2** (thin margins at 17 and 23): the identification is exact at the retained tail-bound grade.
  - Optional hardening: re-run 17/103 and 23/47 at T ≈ 1.08·10¹¹, inside the existing corpus. That is about
    13–14 CPU-h each, locally. It would shrink the radii to about the v2 level (1.2·10⁻⁴).
  - It is not new prime production. It is the user's call, and it goes on the compute list.
- **Lane 6 wording:** the Fable coordinator's correction is accepted. The nine abstract-level rows in H08 are unchecked
  triage, not exclusions.
- **Lane 7 was built** from the Fable coordinator's recommendation: the #Sha-factor test on 194040co6, sha_an = 4.

## Addendum 2 (~13:10): lane 7 and B1 (both Fable-produced; Claude checked cross-model)

**Lane 7 (the #Sha factor): SHA_FACTOR_CONFIRMED. Verdict: CONFIRMED at replay depth.**
- Manifest 38/38.
- The kill-test replay (s3_kill.gp, in a copy) is IDENTICAL to the original, except for `time -p` lines the original
  saved. All 5 rows give w ≡ 32 and reject the Sha-free 8.
- The symbol files match. The originals hold the same vector twice, because s3 and s4 both append.
- Claude's independent ecdata scan: exactly 42 rank-2 curves with sha_an ≠ 1 below N = 500k, all with sha_an = 4. The
  first is 194040co6.
- **Caveat (the worker's own):** the co6 constants are all powers of 2. The attribution of 2² to #Sha rests on the
  Sha = 1 calibration and on the Sha = 1 partner curves co1–co5 (40/40). An odd Sha like the seed's 9 cannot be tested
  locally.

**B1 (upper half): GAP_AT K-B1a. Verdict: CONFIRMED at source.**
- Manifest 9/9.
- **SU Thm 3.5.6** (SU l.2275–2279) states Kato's divisibility, integrally when the image contains SL₂(Z_p), in SU's
  canonical-period normalization, citing "Theorem 17.14 of [Ka04]". It gives no argument for the period comparison.
- **SU 3.6.4's proof** (l.2400–2405) invokes "Kato's Theorem 3.5.6".
- **Kato 17.4(3)** is for a "good" ω (the §17.5 lattice condition). The canonical-versus-good comparison at k_m ≥ 8 > 3 is
  MS-B1.
- The image-condition replacement, via inertia at 2243 per Skinner, passes.
- **Coordinator note:** whether SU 3.6.4's argument needs the INTEGRAL (3-power) form is not re-derived by Claude. B1's
  observation that Skinner's Thm A proof "goes through the same transcription" is plausible and unverified.
- **For B1's own goal (#Sha[3^∞] ≤ 9)** the integral form IS needed, so MS-B1 is the gap.

## Addendum 3 (~15:00): R23 (Fable-produced, same session as B1; Claude checked cross-model)

**R23: route 3 REDUCED (MS-R3), finiteness SOURCE_FOUND, route 2 NO_SOURCE. Verdict: CONFIRMED WITH CORRECTIONS.**
- Manifest 16/16. Every quote below was re-read in R23's `sources/` or in B1's Kato text.
- **Kato (checked at source):**
  - Thm 18.4 (Ka l.8707–8723): corank Sel(T) ≤ ord_{s=k/2} L_{p,α}(f) when α ≠ p^{(k−2)/2}. There is no p ∤ N and
    no image hypothesis.
  - Rem 18.3: for k = 2, α = 1 iff E ⊗ Q_p is a Tate curve.
  - 14.1: Sel(Q, T_pA) is the usual Selmer group.
  - 17.1: §17 assumes p ∤ N, so 17.4 does not reach p = 3 here (as Skinner l.75–81 says).
- **Seed (PARI, run040 env, under 1 s):**
  - a₃ = −1, so α = −1 ≠ 1;
  - the isogeny class is {1, 2}: there is no 3-isogeny, so ρ̄₃ is irreducible;
  - v₂₂₄₃(Δ) = 1, so ρ̄₃(I₂₂₄₃) ≠ 1 and P_τ is a unit;
  - v₂(j) = 4 and v₄₅₄₇(j) = 0 (potentially good);
  - v₃(φ(N)) = 0.
- **Route 3(a) CONFIRMED.** corank Sel₃^∞(E/Q) ≤ ord L₃ ≤ 2 (a₂ ≠ 0), and rank = 2, so Sha[3^∞] is finite.
  - Grade: a printed theorem plus the retained certificate. There is no SU, Skinner or Jones input.
  - It gives orders only; it gives no bound ≤ 9.
- **Ochiai 2006 (checked at source):**
  - p ≥ 3 (Oc l.248);
  - (Ir) (l.298);
  - the Thm 2/3 hypotheses, including H^n.o_F ≅ O[[X₁,X₂]] (l.510–567);
  - Cor 7.5, an equivalence of main conjectures under "P_τ a unit" plus the local condition;
  - Rem 7.6;
  - the proof's steps (12)–(14), including "C_{p,I,b} is known to be a p-adic unit by Kitagawa's construction".
  All read as R23 quotes them.
  - Lemma 7.2, used in (13), also assumes (Nor): H^n.o_F is integrally closed. R23 omits (Nor). It follows from MS-R3
    (regular ⇒ normal), so it adds no obligation.
- **The rest (checked at source):**
  - arXiv:1303.0406v3 is by Preston Wake;
  - Rem 1.8 (Ohta needs p > 3) and Rem 1.6 (Hida's control for p ≥ 5; Wake needs Np > 4);
  - Kim–Nakamura assume additive reduction (l.31–33);
  - Skinner l.973–980.

**Corrections**
1. **The headline "REDUCED, to one named statement, MS-R3" undercounts the obligations.** MS-R3 is the only
   unverified HYPOTHESIS of the printed theorem. Specializing to f also uses:
   - step (14), at remark grade inside a proof: that C_{p,f,b} is a unit ([Kit94] at p = 3 was not read);
   - Rem 7.6's local condition;
   - R23's own one-sided reading of the proof of Cor 7.5;
   - Ochiai's Sel_I equal to the classical Sel.
   R23's Grades section lists all of these; the headline should too.
2. **Why MS-B1 does not arise, and what replaces it.** Ochiai gets integrality from Λ-adic objects and specializes at
   weight 2 only. No integral comparison at k_m ≥ 8 is used. The period question does not disappear: it moves to (14),
   at weight 2. Supporting check (Claude, reading grade): 3 ∤ φ(N), so the Γ₁(N) canonical period of Ochiai's Def 6.6
   agrees 3-adically with the Γ₀(N) period that S.3 uses.

**Consequence for S.3 (draft; nothing applied)**
- **Finite:** Kato 18.4. New, and independent of SU.
- **≥ 9:** B2's explicit cubics, unconditionally, once B2 is CERTIFIED and checked. Lane 1's MS-13.4.1(ii) (the
  lower-bound direction) is then no longer needed for S.3.
- **≤ 9:** still needs exactly one of:
  - Skinner as printed (MS-B1);
  - Ochiai (MS-R3 plus the remark-grade steps);
  - GRH (B2's dim Sel₃ = 4 plus B3's pairing).
- **Independence:** R23 and B1 come from one Fable session. This check is cross-model, not cross-family.

## Addendum 4 (~15:20): B2 (Opus-produced). Checked by the Fable coordinator (cross-model) and pre-checked by Claude

**B2: CERTIFIED, #Sha(E/Q)[3] ≥ 9 with no GRH and no SU. Both checks PASS.**
- The Fable coordinator's check is the designated cross-model check (user relay, ~15:15). It covered:
  - a solo replay;
  - its own ellfromeqn Jacobians;
  - its own smooth points mod p at the 5 bad primes;
  - a reading of the independence method.
- **Claude's pre-check** (same-model as the worker, but independent implementations):
  - The manifest is 90/90 OK.
  - `verify_certificate.gp` was replayed alone in an empty scratch folder in 0.26 s. Its output is IDENTICAL to
    `logs/verify_certificate.log`, apart from the original's appended `time -p` lines.
  - **Sage `Jacobian()`** (invariant_theory ternary_cubic; different code from the worker's Hessian calibration):
    Jac(Cᵢ) ≅ E over Q for both cubics. Sage's S/c₄ = −1/1296 and T/c₆ = 1/5832 for both, so the normalized
    (c₄, c₆) equal E's exactly and disc(Cᵢ) has E's primes.
  - **Hensel, Claude's own code:** every tabulated point satisfies v(U(P)) > 2·min v(∇U(P)) at 2, 3, 2243, 4547 and
    5843, for both cubics.
  - **Consistency:** there is no rational point with (X:Z)-height ≤ 400 on either cubic (194,712 pairs). Evidence
    only.
  - The certifying 4×4 minor was re-evaluated by hand: det ≡ 2 (mod 3).
- **Not re-derived by Claude:** the cubic-side columns of the symbol matrix (the Cardano class). They rest on the
  verifier, its Kummer self-test (80 primes, 3 points) and the Fable coordinator's reading.
- **Status of S.3 now:**
  - finite (Kato 18.4; addendum 3);
  - ⊇ (Z/3)² (B2, unconditional);
  - exact order open. It needs ≤ 9, from one of: B3 + GRH, MS-R3, or MS-B1.
- **Note for B3's consequence (Claude).** Given Kato finiteness, if ⟨C₁, C₂⟩ ≠ 0 then H = span(C₁, C₂) ≅ (Z/3)² is
  an ORTHOGONAL DIRECT SUMMAND of Sha[3^∞]. The reason: the pairing on the finite group Sha[3^∞] is nondegenerate
  and alternating, and nondegenerate on H, so Sha = H ⊕ H^⊥. This part is GRH-free. GRH (dim Sha[3] = 2) then gives
  H^⊥ = 0.
- B2's work/ (≈636 MB bnf) is KEPT until B3 returns. B3 lists it as a read-in-place input.

## Addendum 5 (~16:20): R24 (Fable-produced, new session; Claude checked cross-model), and B3 (Opus; pending Fable)

**R24: REDUCED_TO MS-R24, plus O2 and O4. Verdict: CONFIRMED WITH CORRECTIONS.**
- Manifest 48/48 OK.
- **O1, Kato 12.5(4) for T₃E at p = 3: CONFIRMED at source (Ka l.5711–5738).**
  - (12.5.1) is a joint condition that ENDS with "length(H²_loc(V)_P) = 1".
  - H²_loc(T) ≅ H⁰(Q₃(ζ₃^∞), T^∨)^∨(−1) (Ka l.5650–5655), and T^∨ ≅ E[3^∞] for T ⊂ V(f) = V₃E(−1).
  - At nonsplit 3, E[3^∞] is an extension of Q₃/Z₃(η) by μ₃^∞⊗η. Here η ≠ 1 on G_{Q₃(ζ₃^∞)}, because that field is
    totally ramified. So H⁰ = 0 and H²_loc = 0, and (12.5.1) never holds.
  - Hence 12.5(4) holds at EVERY height-one P, including (3). R24's "UNCHECKED as a written deduction" is now
    discharged at reading grade.
  - (12.5.2) holds: ρ₃ is surjective, so the image of G_{Q(ζ₃^∞)} is SL₂(Z₃).
- **Elkies test: reproduced.**
  - With the "+" sign, both printed forms agree, f(∞) = 4374, f(0) = −44789760, and 419904 and −44789760 are hit.
  - The seed has no preimage under either sign. So ρ₃ is 3-adically surjective (completeness via RSZB: SECONDARY).
- **Local data: reproduced.** E(Q₅₈₄₃)[3] ≅ Z/3 (5844 = 2²·3·487, nonsplit I₂). 5843 is inert in Q∞
  (v₃(−5843−1) = 1).
- **Spot-checked at source:**
  - Kobayashi covers the Tate curve only (Kob l.199–201). But l.318–328 prove Col(z_Kato) = L_{p,γ}(E,X) ∈ Z_p[[X]]:
    the SPLIT analogue of MS-R24.
  - Ochiai–Shimomoto (iii′) fails at 5843, since H²(Q₅₈₄₃, T₃E) ≅ E(Q₅₈₄₃)[3^∞]^∨ ≠ 0.
  - Fouquet–Wan's residual shape η ⊕ ωη is excluded.
  - EPW 2022 is correctly attributed (Emerton–Pollack–Weston, arXiv 2210.02013), and its (Irred) fails.
- **Correction 1 (wording).** "Reduced to one LOCAL named statement" is fine for MS-R24 itself. T-INT also needs O2 and
  O4 (R24 lists them). O2(c) at 5843 is a real risk: the Euler factor (1 + 5843⁻¹) has v₃ = 1. The bound becomes ≤ 27
  unless it provably cancels.
- **Addition (Claude, a lead, not a proof).** MS-R24 looks like Kobayashi's Tate-curve map twisted by η.
  - The quotient T/T⁰ = Z₃(η) is unramified, like the unit-root quotient in Kato §17.
  - The expected interpolation factors cancel. Coleman's (1−φ)(1−p⁻¹φ⁻¹)⁻¹ at φ = −1 is 2·(3/4). Kato's L_{p} is
    (4/3)·L(E,1). Their product 2·L(E,1)/Ω = (1−α⁻¹)·L/Ω is exactly MTT's value at T = 0.
  - Candidate proofs: Rubin's appendix (height-one formal groups; not accessible); Coleman theory over Q₉ (where
    E is split) restricted to the η-part; or Perrin-Riou's map for an unramified character.
- **Corrections to Claude's own inputs.**
  - SEED_DATA's Elkies j-map carried Elkies's printed sign typo. Harmless: no preimage under either sign.
  - B3's TASK credited "Visualizing elements of order three in Sha" to Fisher. It is Mazur (Asian J. Math. 3, 1999).
- **B3 (Opus): INCONCLUSIVE_AT the global step** (splitting a degree-3 CSA over L, |d_L| ≈ 10^58.7; Fisher–Newton's
  Problem 3.5). The Fable coordinator's check is pending.
  - Consequence: route 1 (GRH + pairing) stalls on computation, not on mathematics.
  - Its alternative, Creutz's second 3-descent, puts GRH into the pairing and needs new PARI code. That is the user's
    call. Claude recommends route K (R25) first, because it is unconditional.

## Addendum 6 (~17:50): A2 (Fable-produced; Claude checked cross-model), and A1 (Opus; pending Fable)

**A2 (rows F3-O3 and F4): NO_SOURCE_FOR_THESE (scoped). Verdict: CONFIRMED.**
- Manifest 17/17 OK.
- `checks/regcheck.gp` rerun: IDENTICAL, apart from the header comments the worker added.
- **Minimal model (PARI).** ord_p Reg_γ = 0 at the good ordinary p in 5–47, except ord₁₇ = 1, which matches the
  record. This is numeric only (precision 12), not a certificate.
- **Checked at source** (arXiv PDFs fetched by Claude and hashed in the scratchpad):
  - Burungale–Disegni 1803.09268 l.60: nondegeneracy "is not known in any cases of rank higher than 1". Verbatim.
  - AKS 2609.35626 Cor 1.3 has hypotheses (i) α ≠ β and (ii) a nonzero localization map, which holds for positive
    rank by Rem 1.4(1).
    - So it applies at EVERY good p, ordinary included. A2's H06 scope correction is right; Cor 1.5 is the
      non-ordinary case.
    - The conclusion is "either N_α or N_β is non-trivial". That does not give the unit-root pairing, and does not
      give det ≠ 0.
- **Task-text slip: CONFIRMED (PARI).** P₁ = (−3031, 327384) and P₂ = (−2394, 281520) are on the MINIMAL model
  [0,−1,0,−66020924,−65074271436], not on y² = x³ − 22735x² + 106272484x.
  - This is a STANDING correction for every task text that prints both together.
  - It matters for heights: PARI p-adic heights depend on the model.
- **No correction to A2's conclusions.** Its bearing on F3-O3 and F4 is scoped correctly, and it makes no necessity
  claims.

**A1 (row F2; Opus): NO_SOURCE_FOR_THESE, per the user relay. Its cross-model check belongs to the Fable
coordinator (pending).**
- The closest results are Kriz–Nordentoft 2310.20678 (per-p Kurihara witnesses, with r(p) uncontrolled) and FKK
  0711.1771 (uniform in p, but depth 0 and L(E,1) ≠ 0).

**Reduction sheet (the Fable coordinator's file, not edited by Claude).**
- Its Kato 18.4 row still says "Opus check pending". It is DONE: CONFIRMED (addendum 3).
- Both first attempts in §4 are now scoped-negative. Every row F1–F9 still lacks its first input.

## Addendum 7 (~18:10): grading the three A2 claims the Fable coordinator passed on
1. **"AKS Cor 1.3 applies at every good prime": CONFIRMED** (checked at source, arXiv 2609.35626).
   - (Hyp 1) holds.
   - (Hyp 2) holds: V_p is crystalline.
   - (Hyp 3) holds:
     - at ℓ ≠ p, H^i(Q_ℓ, V_pE) = 0, since E(Q_ℓ)[p^∞] is finite and the Euler characteristic is 0;
     - at p, φ has no eigenvalue 1.
   - (Hyp 4) holds because E is non-CM (AKS l.153–155).
   - (i) α ≠ β, because a_p² = 4p is impossible.
   - (ii) holds: log_p P₁ ≠ 0 (Rem 1.4(1)).
   - Scope: the conclusion is "N_α or N_β is non-trivial". That is neither the unit-root pairing nor det ≠ 0.
2. **"No rank-≥2 curve has a nonzero p-adic regulator proved at even one prime": FALSE AS WORDED.**
   - It fails at the smallest eligible case, the seed itself. The S.3 height certificate gives a nonzero 3-adic
     determinant, and the record also has certified nonzero values at p = 5 (the SW gate) and p = 17.
   - Stein–Wuthrich 2013 certify many (E, p) by computation.
   - Correct wording: "No GENERAL theorem gives it for any rank-≥2 curve at any prime. It is known only per (E, p),
     by rigorous computation." That is what Burungale–Disegni l.55–60 and A2's boundary item 1 say; the condensed
     wording dropped it.
3. **"At good ordinary p, F4 at p ⟺ (O3 at p and Sha[p^∞] finite"): HALF.**
   - (⟹) is unconditional. Kato 18.4 and rank 2 give ord L_p = 2. Kato's divisibility gives ord f_E ≤ ord L_p, and
     Schneider/Perrin-Riou give ord f_E ≥ 2, with equality iff R_p ≠ 0 and Sha[p^∞] is finite.
   - (⟸) needs the IMC at p, at the recorded SU grade. A2's own text includes that qualifier.
   - Watch (UNCHECKED): 2243² − 1 = 2³·3·11·17·19·59. So lane 1's Euler-factor failure mode in SU Prop 12.3.6 could
     recur at p = 11, 17, 19 and 59, if 2243 is again the forced inert prime. The p ≤ 47 settlements use Ota
     singletons, not SU, so they are unaffected.
- **The Fable coordinator's A1 check (CONFIRMED) is noted.** Both uniform-step screens are closed. Claude agrees:
  no more literature screens on rows F2–F4.

## Addendum 8 (~18:25): corrections to Claude's own board
- **B3 was already checked.** The Fable coordinator's CONFIRMED-as-INCONCLUSIVE_AT check was written before 16:30
  (RETURN_CHECKS.md, "## B3", l.155).
  - Addenda 5–7 and the RUN_NOW boards called it "pending". That was wrong: Claude did not grep the checker's log
    first.
  - The Fable coordinator now has NO pending checks.
- **Scope note accepted.** The "four-exponentials" comparison in Claude's chat reply is an analogy, not a reduction on
  record. It was never written into any record file.
- **Short-model coordinates** (PARI, Claude): (4547, 327384) and (5184, 281520) lie on y² = x³ − 22735x² + 106272484x.
  x_min = x_short − 7578 maps them onto the minimal-model points. This matches the Fable coordinator's sheet §5.

## Addendum 9 (~18:55): R25 (Opus-produced). Claude's PRE-AUDIT; the designated cross-model checker is the Fable coordinator
**R25: T_INT_PROVED_MODULO (unaudited).** Manifest 23/23 OK. Claude read D5, D6 and D8 in full.
- **D5 (MS-R24): structure sound.**
  - Local: H²_Iw(T⁰) = 0, so the norms are onto. Nakayama–Rim gives Ê(m_n) free of rank 1 over Z₃[Γ_n].
  - log c₀ = 3/2 generates 3Z₃, so Col is an isomorphism onto Λ.
  - Interpolation follows Kobayashi l.266–298. The value at χ = 1 is (1−α⁻¹)(1−α/p)⁻¹ = 3/2, matching Claude's
    pre-computation.
  - Equality comes from the "finitely many zeros" argument.
  - Ka 16.4/16.6 are used only as a cross-check (the KKT caveat). The primary route uses Ka 12.5(1).
- **D6 (O2): structure sound.**
  - The four-term sequence is 0 → H¹/Z → Λ/(L₃) → X → H² → 0. With Ka 12.5(4) it gives char X | L₃.
  - The 5843 term does not appear. Ka 17.10's ℓ ≠ p step kills every local condition at ℓ ≠ 3 in the limit, because the
    residue tower contains the Z₃-extension of F_ℓ. The zeta elements and j_* cohomology are both primitive at 5843.
    This agrees with Claude's own computation (H¹_ur(Q∞,5843, E[3^∞]) = 0) and with K-R25c's 126 curves.
- **D8 step 7 (the height normalization; R25's own WARNING).**
  - The release already states the input: v0.2.4 `paper/sections/04_primary.tex` l.91 says the independent certificate
    gives "ord₃ Reg_γ = 0". Evidence: `f1_indep_height.gp` and its output (F1 hostile audit, PASS_WITH_CORRECTIONS).
  - R25 pairs that certificate with Jones Thm 3.1 exactly as S.3's existing chain does, so it adds no new
    normalization. The fallback v₃ ≥ −1 (with #Sha a square) gives margin.
  - Fable should confirm the value in the output file.
- **Convention risk (χ ↔ χ⁻¹): cannot change the bound.** Under T ↦ (1+T)⁻¹ − 1, ord_T and the valuation of the T²
  coefficient are unchanged. So a mismatch affects only the exact identity Col(z) = L₃, not ≤ 9.
- **For Fable to confirm at source:**
  - Ka 12.5(1)'s proof (§13.12, through §9–10) carries no p ∤ N, crystalline or KKT dependence;
  - D2's Dwork-lemma integrality;
  - Česnavičius Thm 2.11 (3 ∤ c when 3 ∥ N).
- **If Fable passes it:** S.3 holds with NO Skinner, NO Skinner–Urban and NO GRH.
  - Its imports: Kato 2004; Kobayashi (mechanics); Česnavičius; Jones Thm 3.1 (forward); the height and a₂
    certificates; B2.
  - Its grade: a written derivation, cross-model checked, not cross-family, no human review.
  - V025-BANK excludes R25, so bank it in a follow-on commit before any push.

## Addendum 10 (~19:10): the Fable coordinator's R25 check, and the second reader
- **Fable: CONFIRMED_WITH_QUALIFICATIONS** (`~/BSD_P3_MS_R24_COLEMAN_CHECK_FABLE_2026-09-29/CHECK.md`).
  - Kato 12.5(4), 12.4(2), 17.10, 17.13 and 17.4 were checked at source.
  - R25's nonsplit lemmas were hand-verified.
  - coleman_family.gp replays identically.
  - New: a rank-1 normalization test, 23/23.
  - New: Jones 1989 Thm 3.1 READ AT SOURCE from the author's copy (a preprint copy, not the Duke print). Its hypotheses
    are p ≠ 2, Sha(p) finite and a nondegenerate pairing, and the (log κγ)^r convention matches Reg_γ.
  - Schneider 1985 II is not a substitute: it assumes good reduction at p.
- **Grade.** Claude AGREES with Fable's proposal: S.3's upper half is PROVED_MODULO_SECOND_READER. The release grade
  stays unchanged, and R25 stays OUT of the bank until a second reader passes D5 Steps 2–3 and D6. This supersedes
  addendum 9's "bank it as a follow-on commit".
- **Second reader BUILT:** `~/BSD_P3_R25_SECOND_READER_TASK_2026-09-29/` (27 files).
  - It holds only the derivations under review and the primary sources. The first reader's report is withheld.
  - Reader: Codex if credit remains; otherwise a fresh Opus session as hostile referee.
  - Kill tests: a replay, and an independent recomputation.

## Addendum 11 (~19:20): Fable confirmed Claude's three items; there are two second-reader bundles, so launch ONE
- **The Fable coordinator confirmed at source:**
  - Kato 12.5(1) and §13.12 carry no p ∤ N, crystalline or KKT dependence. KKT appears only at 16.4 and in 18.4's α = 1
    case; ours is α = −1.
  - The D2 Dwork lemma was read, and its check replayed.
  - Česnavičius Thm 1.2 is per-prime, and 3 ∥ N suffices (release claim A.4). R25's D7 cites "Thm 2.11"; the note
    should say Thm 1.2.
  - Paper l.91's ord₃ Reg_γ = 0 is confirmed.
  - The grade stays PROVED_MODULO_SECOND_READER.
- **Duplicate bundles.** The Fable coordinator built `~/BSD_R25_SECOND_READER_TASK_2026-09-29/` at 18:55, before
  Claude's `~/BSD_P3_R25_SECOND_READER_TASK_2026-09-29/`.
  - LAUNCH FABLE'S. Its targets are more detailed (T1–T5, and a kill test that probes ≤ 27).
  - Claude's bundle now carries SUPERSEDED.md; its manifest was refreshed.
  - Fable's bundle lacks the rendered Kato PDF (the OCR garbles 12.5(1) and 16.2). Claude supplies it in
    `~/Downloads/BSD_R25_SECOND_READER_UPLOAD_2026-09-29.zip` (12c867e6: Fable's bundle unchanged, plus
    extra/Kato2004_AST295.pdf), and a prompt line gives the local path.
- **Independence note.** Fable's bundle includes the first reader's CHECK.md, with the instruction to read it only after
  forming a view. That is acceptable. A cross-family reader (ChatGPT Pro given the zip, or Codex) would be the strongest
  choice.

## Addendum 12 (~19:35): A3 returned (Opus; Fable checks it); Wake is withdrawn; memory index trimmed
- **A3 (p-free rank-2 constructions): NO_CONSTRUCTION_SURVIVES.** Five candidates (the elliptic surface, a Yun–Zhang
  template, composite-modulus W, plectic points, first-derivative formulas) each died at a stated first failure.
  - By-products:
    - "288 = 2·den(t₀)" is a coincidence: another fiber gives w = 24, not 10;
    - K_E fits one more curve (w = 24 = 4c∞·Tam·Sha/tors², 22 auxiliaries), conjecture-grade;
    - Fornea arXiv:2603.28327 is watched at 2243 and 5843 only;
    - a PARI trap: `ellanalyticrank` returns L^(r)(1), not L^(r)(1)/r!.
  - Claude has not checked A3; the Fable coordinator is the checker. For the map: FIN stays at the current known
    frontier.
- **Wake arXiv:1303.0406 is WITHDRAWN by its author (v4).** Claude checked the abs page.
  - R23 read v3. Its route-2 remark "Ohta needs p > 3" (Wake Rem 1.8) and the Wake citations in addendum 3 therefore
    rest on a withdrawn preprint. That remark is now UNSUPPORTED (Ohta was not read).
  - No effect on route K or R25, which do not use Wake. BANK_SCOPE does not cite Wake.
- **Memory index.** Other sessions' new lines pushed MEMORY.md over its size limit. Claude shortened nine index lines
  without dropping any entry.

## Addendum 13 (~20:45): A3 confirmed by Fable; a wording fix; the Pro construction brief (the user's call)
- **The Fable coordinator CONFIRMED A3** as NO_CONSTRUCTION_SURVIVES. The 2900 fiber was recomputed (N = 2900, rank 2,
  Tam 12, tors 2, c∞ 2, Sha_an 1). So K_E = 4·2·1·12/2² = 24, matching w on 22 auxiliaries. Claude rechecked the
  arithmetic.
- **Wording fix.** Addendum 12 and RUN_NOW ~19:35 said the Yun–Zhang space "doesn't exist over number fields". The
  record should say "NO KNOWN analog". The quote is YZ §1: "only exist (at least for the time being) when r ≤ 1".
  Memory is corrected.
- **The Fable coordinator's proposed $0 attempt:** a math-state construction brief for ChatGPT Pro. Its target is one
  rational Z with w_p = Z for all large p. Claude's view:
  - It is admissible and cheap.
  - It is as hard as what is missing. By K_E (conjecture grade), a Sha-free Z would have to equal 32·#Sha, i.e. 288
    on the seed and 24 on the 2900 fiber, so it would compute #Sha.
  - Expect NO_CONSTRUCTION. Its kill tests make any answer cheap to grade.
  - If the user says yes: the Fable coordinator writes the brief, and Claude reviews it before it is pasted (math
    state only; exact statements; the kill tests).

## Addendum 14 (~21:05): Claude's review of the Fable coordinator's Pro brief. PASS WITH CORRECTIONS; a reviewed copy is written
- **File reviewed:** `~/BSD_BUILD_MAP/PRO_BRIEF_UNIFORM_STEP_2026-09-29.md`, left untouched.
- **Reviewed copy:** `~/BSD_BUILD_MAP/PRO_BRIEF_UNIFORM_STEP_2026-09-29_REVIEWED.md` (also on the Desktop). Paste THIS one.
- **Definitions match TARGET_R1 §1:**
  - λ_f (same integral written two ways), [r]⁺ over ω₁, the (1/1024)Z lattice;
  - C2 = Σ binom(ind_g(a) mod p, 2)[a/ℓ]⁺ over all ℓ−1 labels;
  - the least primitive root, used for both symbols and tame logs;
  - h_ℓ = ind_g(−a/b), R = M⁻⁴det, w = C2/((a_ℓ−2)R), the auxiliary conditions and B*.
  - The brief's M (component exponent × exp E(F_ℓ)) differs from TARGET_R1's 16·#E(F_ℓ). R is independent of M by
    bilinearity, so this is fine.
- **Arithmetic checked:**
  - K_E on N = 2900: 4·2·1·12/4 = 24.
  - The family y² = x(x² − 5tx + 4t(t+9)) at t₀ = 4547/144 gives the seed after x ↦ x/144 (1728² = 144³).
  - 8q = 288.
- **Corrections applied in the reviewed copy:**
  - (1) **§6, substantive.** "Not known at even one prime for any curve of rank ≥ 2" is FALSE for this E: regulators
    are certified at 3, 5 and 17 (addendum 7). Now: "no GENERAL theorem …; known only per (E, p) by computation".
  - (2) **§3, substantive.** G2's exceptional set is S₀ = {2, 3, 5, 2243, 4547, 5843} (G2_PROOF l.19), not B*: G2
    excludes 5. The consequence's exceptions are now B* ∪ {5}, num(Z), and Ota's exclusions.
  - (3) **Precision.** Ota 6.4's hypotheses as in TARGET_R1: p ∤ 6N·#E(F_p)·Tam, full p-adic image, p ≥ rank, and
    E(F_ℓ)[p] cyclic.
  - (4) **Precision.** Ω = ∫|ω| = 2ω₁ and a BSD-normalized Reg, so q = 36 is unambiguous. ω₁ is the least positive
    real period.
  - (5) **Precision.** θ_ℓ ∈ I² comes from Ota's augmentation theorem on his domain, not from L(E,1) = 0 alone.
  - (6) **Precision.** 19 ∈ B*, so at 19 the ℓ-independence is observed, not proved. The height bound is 3.7·10⁹, or
    7.08·10¹⁰ with 19.

## Addendum 15 (~21:40): both second readers PASS_WITH_CORRECTIONS; the R25 readings reconciled; a correction to Claude's own citations
- **The two readings.**
  - Reader A (`~/BSD_R25_SECOND_READER_RETURN_OPUS_2026-09-29/`, 19/19) and reader B (`…_OPUS_B_…`, 17/17) are independent,
    fresh Opus sessions. Each opened the Fable check only after writing its own verdicts.
  - Both found no false step and no power of 3 that fails to cancel.
  - The Fable coordinator's reading was CONFIRMED_WITH_QUALIFICATIONS.
- **Consensus correction E1 (verified by Claude from the OCR of Kato Thm 13.4, l.5911–5943).**
  - The printed 12.5(4) inequality is for V, so it is vacuous at P = (3). The integral statement at every height-one
    prime is Kato 13.4(3), applied to the zeta elements through 13.14. Its hypotheses hold for the seed (ρ₃ surjective,
    residual irreducibility, p ≠ 2).
  - **Claude's addenda 3 and 5 said "12.5(4) holds integrally at every height-one P, including (3)". That was
    IMPRECISE: the right citation is 13.4(3).** The conclusion is unchanged.
- **The other corrections** are in `~/BSD_BUILD_MAP/R25_ERRATA_2026-09-29.md` (E1–E7):
  - χ ↔ χ⁻¹: cite Kato 12.5(1) and SW directly; Kobayashi's two slips cancel.
  - Kato's L-function is SW's shifted by κ.
  - The regulator normalization (E4): the γ-normalized v₃ = 0 is needed and satisfied; otherwise ≤ 81.
  - The (12.5.1) parsing is moot.
  - Dwork has a unit factor; D7 is unnecessary; Česnavičius is Thm 1.2.
- **Grade proposal.** Route K is a WRITTEN PROOF with three model readers: one cross-model and two fresh same-model
  sessions. All are Anthropic, so it is NOT cross-family. It has no human referee.
  - The Fable coordinator's condition (a second reader passes D5 Steps 2–3 and D6) is MET, twice.
  - Banking route K as a follow-on commit is now eligible. Whether S.3's release label changes is the user's call.

## Addendum 16 (~22:30): ChatGPT's answer to the uniform-step brief (A4; cross-family). Graded by Claude
- **Files:** `~/BSD_UNIFORM_A4_CHATGPT_RETURN_2026-09-29/`, byte-identical to ~/Downloads (created by another session).
  ChatGPT used the ORIGINAL brief. Its two substantive errors (§6 and G2's S₀) enter none of its arguments. GP was not
  available in its sandbox, so its arguments are algebraic.
- **Status claimed: REDUCED. Claude's grade: CONFIRMED as NO_CONSTRUCTION. "REDUCED" here is a reformulation of the
  missing cross-prime law, not a new, narrower named statement.**
- **Mathematics checked:**
  - I(C_n)²/I(C_n)³ ≅ Z/n, so compatibility over all finite levels lands in Ẑ (∏_{p∉S} Z_p), a profinite scalar.
    Correct.
  - Diagonalization lemma: x ∈ ∏_{p∉S} Z_p lies in Z[1/S] iff, after clearing an S-supported D, the balanced residues
    of Dx are uniformly bounded. Correct: once n > 2B, compatibility plus the bound force the lifts to stabilize.
  - Conditional uniqueness: if the rank-2 Mazur–Tate leading term holds at infinitely many p, any rational n_Y equals
    K_E = 32·#Sha. Correct, since two rationals congruent modulo infinitely many p are equal. This matches lane 4.
  - Ota 6.4 and Theorem W constrain only where w_p vanishes, never its nonzero values. Correct as logic.
  - The rejections (CRT, the 1/1024 denominators, the parity functional equation, per-p norm relations, 8q, residue
    interpolation, the 3-Selmer quotient = Sha[3]) each fail a test as stated.
- **Citations checked at source (local BKS II text):**
  - Thm 1.1 needs (a)–(c), (d) BSD over Q, and (e) the generalized Perrin-Riou conjecture if r > 0 (l.112–122);
  - §2 assumes Sha finite (l.238).
- **What it adds.** A clean formal criterion: rationality of (w_p^∞) is equivalent to uniformly bounded balanced lifts,
  i.e. to an archimedean or global input. Under BKS, a Sha-free Z must equal 32·#Sha. Useful framing; no progress on FIN.
- **The Fable-max run of the same brief has not returned.**

## Addendum 17 (~22:40): consensus on the ChatGPT A4 answer is NO_NEW_REDUCTION
- The Fable coordinator graded it NO_NEW_REDUCTION. Claude's addendum 16 grade ("NO_CONSTRUCTION; 'REDUCED' is a
  reformulation") says the same thing.
- **Consensus label: NO_NEW_REDUCTION.**
  - (a) is LINE / the BKS determinant line plus the CRT observation (A3's CAND_03).
  - (b) the diagonalization lemma is true, but it is logically equivalent to rationality.
  - (c) is the K-B admission rule.
- Nothing new enters the record. Claude agrees with the Fable coordinator's rule: "REDUCED" must be strictly sharper
  than the target.

## Addendum 18 (~23:00): the Fable-max answer to the uniform-step brief (A4). Claude checked it cross-model: CONFIRMED
- **Status: NO_CONSTRUCTION_SURVIVES.** `~/BSD_UNIFORM_A4_FABLE_MAX_RETURN_2026-09-29/`: manifest 15/15. Its three
  PARI checks were replayed in a scratch copy and are IDENTICAL: p1 (trace lift), p2 (the 11a1 depth-0 identity), p3
  (389a1 depth parity with a generator control).
- **N4, the adelic Kummer index of (E; P₁, P₂): a new p-free, Sha-free object.** It passes K-P, K-F and K-C and dies at
  K-num, because its 3-part is 1.
  - The argument checks out. Jones–Rouse Thm 5.2 (as quoted in Lombardo–Tronto) applies because ρ₃ is surjective and
    every nonzero (a, b) mod 3 gives a 3-indivisible aP₁ + bP₂ (saturation).
  - For the pair, a Galois-stable proper submodule of Ē ⊕ Ē would be a graph killed by some such combination, so the
    joint image is everything (Nakayama).
  - Record N4 as dead, so it is not re-proposed.
- **N8, the tame constant 32:** dies at K-num (Lemma A.1). The missing Sha-free invariant would have to equal 9 on E and
  1 on the 2900 curve.
- **(b):** the natural L-side lift Λ is p- and g-dependent. Functional equations act as the identity on I²/I³ (correct:
  ι sends T² to T² mod I³). The chat summary's "only canonical lift" is not in the file, which says "natural lift".
- **(c), a record correction, correct:** the brief's "p-free constant ⟺ FIN" is mis-scoped in both directions.
  - (M1) The constant gives finite support only, not finiteness at 59, 487, 2243, 4547 and 5843.
  - (M2) FIN alone gives no constant; that needs the Kato-residue law.
  - The reviewed brief's §5(c) is now corrected, so Pro gets the right scope. The Fable coordinator's original still
    has the old wording.
- **Both brief answers are now in:** ChatGPT (NO_NEW_REDUCTION) and Fable-max (NO_CONSTRUCTION_SURVIVES). Running Pro
  on the reviewed copy is optional; a third OpenAI-family reading adds little. The uniform step PAUSES at the current
  known frontier.

## Addendum 19 (~23:40): V025-BANK returned BANKED_LOCAL (Opus; the Fable coordinator checks it). Claude's quick pre-check
- **Branch `v0.2.5-bank`:** c4e4b83 (content) and 706efb5 (source stamp). Local only; v0.2.4 is untouched at 001a49f.
- **The worker reports:**
  - 83 claims: 7 new and 7 revised;
  - 114 evidence files appended;
  - the old rows preserved byte for byte;
  - verify_release 18/18 (20/20 with Lean);
  - the new transition check passes, and all 16 negative controls fail as they should.
  - The user approved the `--retained-source-changes` extension for the 5 master files that Codex's reconciliation
    edited.
- **Claude's pre-check found ERRATA E1 in the banked text.** "Kato 12.5(4), which holds for T_3E" appears as the
  integral step of MS-R24 at part1_core.py l.261, 04_primary.tex l.121 and RECHECK l.41.
  - This is where the slip that ran through Claude's addenda 3 and 5 surfaces.
  - The fix, "13.4(3) via 13.14", is now a MANDATORY item in V025-BANK-K (manifest refreshed), with a negative control.
    It applies whatever the user decides on the label.
- **Items for the Fable coordinator's check** (from the worker's CHECK_REQUEST.md):
  - the tool extension;
  - Ota graded as a preprint;
  - the stale O.1/O.2 wording (p ≥ 17, < 2601), out of scope;
  - the scripted SOURCE_SNAPSHOT stamp;
  - frozen check-report copies. The bound CLAUDE_CHECK_REPORT copy is addenda 1–8, which contains the imprecise
    12.5(4) wording; the E1 errata will be bound in BANK-K.

## Addendum 20 (~23:55): USER DECISION. S.3 label: route K PRIMARY, Skinner Thm A as the SECOND route, the label kept verbatim ("yes on 1"). Recorded in the V025-BANK-K TASK (manifest refreshed). Launch after the Fable coordinator's check of V025-BANK.

## Addendum 21 (~00:15): the Fable coordinator's V025-BANK check PASSED with required fixes F1 and F2. Folded into V025-BANK-K
- **The check** (`~/BSD_SEED_V025_BANK_CHECK_FABLE_2026-09-29/CHECK.md`):
  - custody is clean;
  - all 5 verifiers pass on a git-archive copy;
  - --retained-source-changes is tight, accepting only the five Codex-edited master rows, whose released bytes equal
    v0.2.4's;
  - v0.2.4's PROVENANCE is a byte-prefix of v0.2.5's;
  - claims 76 → 83, with no grade change; S.3's statement is identical; R25 is not claimed.
- **F1: the E1 slip is in 4 outward places** (the paper, RECHECK, CLAIM_INDEX, and the spec → claims.json) plus 2 review
  files. Claude's pre-check had found 3.
  - The BANK-K TASK now lists all of them and requires a whole-tree negative control, with an explicit allowlist of
    historical records.
  - Claude's refinement: `review/V025_BANK_APPLIED.json` is the replayed record of v0.2.5's declared edits, so it must
    NOT be rewritten. The correction goes into BANK-K's own declared-edits record.
  - SYNTHESIS_CHECK_BRIEF is fixed by regeneration.
- **F2:** Ota is published (Amer. J. Math. 140 (2018) 495–542). The print is cited in the 17–47 qualification; the label
  may stay; the numbering was not re-checked against the print.
- **The precondition for BANK-K is MET,** and the user's S.3 decision is recorded. BANK-K is ready to launch.

## Addendum 22 (09-30 ~00:40): V025-BANK-K returned BANKED_LOCAL (9828eae). Claude's pre-check, and the push facts
- **Branch:** 9828eae → 706efb5 → c4e4b83 → 001a49f. No upstream, no tag. v0.2.4 is untouched at 001a49f.
- **E1 scan** (all tracked files, except review/history):
  - In the outward text (RECHECK, CLAIM_INDEX, claims.json, spec), every "12.5(4)" now reads "printed for V; not the
    integral step". The integral step cites 13.4(3) via 13.14.
  - The other hits are in byte-identical HISTORICAL evidence copies (R25's D5/D6/D8/RETURN, Fable's CHECK, B1, R24).
    They are correctly unchanged, and the bound ERRATA correct them. R25's D5 l.45 uses the T-part of 12.5(4),
    Z(f,T) ⊂ H¹(T), which is right.
- **S.3K is present.** S.3's primary_support is route K with the label. Ota's print is cited (AJM 140 (2018) 495–542;
  numbering not re-checked).
- **Loose end:** SOURCE_SNAPSHOT.json still names c4e4b83. A one-file stamp commit naming 9828eae (like 706efb5) is
  recommended before any push. The Fable coordinator decides; the worker deferred it because the task asked for one
  commit.
- **Push facts (checked):**
  - GitHub Bome2017/bsd-seed-research main = 2a72621 (v0.2.2), which IS an ancestor of 9828eae.
  - 9 commits are not on GitHub (8ed37c5 v0.2.3 … 9828eae).
  - They share the same root (6831af0) as GitHub main, so no new or leaky history is introduced.
  - A privacy grep over the added lines (emails, privaterelay, ghp_/sk- tokens, api keys, passwords) found nothing.
- **Push plan** (only on the user's explicit go, after the Fable coordinator's check of BANK-K):
  - optionally, the stamp commit;
  - then `git push https://github.com/Bome2017/bsd-seed-research.git v0.2.5-bank:refs/heads/v0.2.5` as a NEW branch,
    with main fast-forwarded only if the user says so;
  - then verify with ls-remote.

## Addendum 23 (09-30 ~07:00): Codex's CROSS-FAMILY reading of route K. PASS at the retained input grade, with corrections
- **Files:** `~/BSD_ASTRA_CATCHUP_RETURN_2026-09-30/` (25/25).
  - ITEM_1 PASS_AT_RETAINED_INPUT_GRADE.
  - K_ASTRA_1 PASSED: no hidden factor of 3 or 9.
  - A fresh PARI check gives v₃(Reg₃) = 2 and v₃(Reg_γ) = 0.
  - ITEM_3 CONFIRMED_WITH_CORRECTIONS.
- **Claude agrees with every correction:**
  - (i) The paper's "γ-free determinant (valuation 2) would give ≤ 81" is WRONG. v₃(#Sha) ≤ 4 − v₃(Reg₃), so the actual
    valuation 2 gives ≤ 9; ≤ 81 needs a γ-free valuation of 0. The proof is unaffected.
  - (ii) "12.5(4) is printed for V" is imprecise. Only its FINAL LENGTH INEQUALITY is for V; the containment
    Z(f,T) ⊂ H¹(T) is retained and used.
  - (iii) S.3K's label should now record the cross-family reading.
  - (iv) The Col(z) = L₃ sentence must carry the κ-shift dictionary (E3).
  - (v) K-num was over-scoped. 288 and 24 are conjectural benchmarks, not requirements. This is the "sufficient ≠
    mandatory" discipline, and it also applies to Claude's own earlier phrasing ("any p-free constant would have to
    equal 32·#Sha" holds only under the BKS conjecture).
- **Applied now:** K-num replaced with Codex's wording in the reviewed brief (Desktop copy updated).
- **Built:** `~/BSD_SEED_V025_BANK_K2_TASK_2026-09-30/`, with fixes (i)–(iv), Codex's return bound as evidence, and the
  SOURCE_SNAPSHOT stamp commit. The label change (iii) needs the user's OK before launch.

## Addendum 24 (09-30 ~07:50): Codex's reopening review (cross-family). NO_RESCUED_GLOBAL_PROOF; gates re-scoped
- **Report:** `~/BSD_REOPENING_REVIEW_CODEX_2026-09-30/REPORT.md` and ADMISSION_REPAIRS.md.
- **Claude agrees with each point:**
  - **R1:** K-P in the reviewed brief conflicted with §5. The requirement is a uniform PROOF (∃ finite S ∀ p ∉ S ∃ Y_p
    with a witness proved nonzero), not a uniform object; G2 is the model. K-P now binds only the common-scalar
    architecture.
  - **R2:** proved Sha data (the certified Sha[3^∞] ≅ (Z/3)²) is legitimate input; only ASSUMING that it exhausts Sha
    is circular.
    - So A4's N7 and ChatGPT's A.5/C.5 had over-scoped rejection REASONS. Their VERDICTS stand for the right reason:
      no cross-prime transport.
  - **R3:** exact 288 is not universal (already applied). 32 genuinely fails a recorded residue.
  - **R4:** A3's surface kill was broader than its evidence. It is narrowed: the fixed MW lattice and index don't
    determine the multiplier; the other fibers' Sha orders are BSD-grade numerics; no specialization map exists.
- **Applied to the reviewed brief** (Desktop copy updated):
  - scoped K-S (it applies to the endpoint mechanism; intermediate lemmas are allowed with their new input stated);
  - scoped K-P (common scalar vs direct uniform theorem);
  - scoped K-F (no ASSUMED conclusions; proved finite arithmetic allowed);
  - the narrowed surface wording;
  - the §5 "most useful answer" (a concrete upper-bound or nonvanishing relation, with how excess Selmer torsion is
    excluded and which primes it covers; the Kriz–Nordentoft gap named);
  - the §6 reopening rule.
- **Codex's ranking** (proximity, not odds):
  1. direct uniform depth-2 nonvanishing, with p-dependent tools allowed;
  2. a uniform annihilator or one-sided integral bound;
  3. a geometric map from P₁, P₂, only with the analytic or Hecke relation.
  - Keep U22 paused, and no new prime ladder or exact-288 lists.
  - Codex supplies no new relation, and a scope correction alone authorizes no construction campaign. Claude agrees.

## Addendum 25 (09-30 ~10:30): Codex's uniform synthesis. A real source change: Kurihara witnesses exist at EVERY good p ≥ 5; the target is now "r_p < 4"
- **Files:** `~/BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/` (and the .zip for Pro, 26 entries).
- **Verdicts:** SOURCE_UPDATE_APPLIES_AT_RETAINED_INPUT_GRADE; ALL_GOOD_PRIME_KURIHARA_EXISTENCE;
  UNIFORM_LOW_DEPTH_BOUND_STILL_OPEN.
- **Checked by Claude at source** (Claude fetched the PDF: CLW2.pdf, sha256 0686fa414b242e8e…):
  - Castella–Liu–Wan, "Kato's main conjecture for nonordinary modular forms", author-hosted, dated September 21, 2026.
    Theorem A: newform of weight k, p > 2 good nonordinary; (i) 2 ≤ k < p; (ii) either k = 2 and (ram), i.e. some
    ℓ ∥ N with ρ̄ ramified at ℓ, or (rtn); (iii) p-regular.
  - No squarefree hypothesis. For the seed: ℓ = 2243 (v(Δ) = 1, so ramified at every p ≥ 5), k = 2 < p, and a_p = 0 at
    supersingular p gives α ≠ β. Theorem A APPLIES.
  - Castella–Sano arXiv 2601.14504 (v1, not withdrawn), "On refined nonvanishing conjectures by Kurihara and
    Kolyvagin".
- **Codex's chain:**
  - the main conjecture at every good p ≥ 5 (ordinary from the known results; supersingular from the CLW revision),
    plus Castella–Sano, gives a Kurihara quantity nonzero mod p at every good p ≥ 5;
  - plus Kim's higher Fitting theorem (2203.12159 Thm 1.8): r_p = dim Sel_p, even and ≥ 2, and r_p = 2 ⟺
    Sha[p^∞] = 0.
  - So FIN-b ⟺ r_p < 4 for all p outside one finite set.
  - A broader sufficient test (from the BH argument): some order-p character value of the normalized θ with
    λ-depth < 4, with a composite conductor allowed.
- **Status:** coverage improved and the target is exact; NOT a proof. The independent upper bound "< 4" is the open
  core. The application (normalizations, the passage to Castella–Sano, Kim's indices) awaits an independent check:
  Pro, per Codex, or a pre-check by the Fable coordinator.
- **Corrections Codex made to CLAUDE's user overview** (09-30), all accepted:
  - (1) "no method exists for any rank-2 curve" was overstated. Correct: no applicable finite-support theorem was
    located in our screens, and Keller reported knowing none.
  - (2) "with rationality, the interval pins 36" is WRONG. A denominator or height bound is also needed (Q.1: ≤ 174),
    or another exact characterization.
  - (3) The exceptional prime set must be DERIVED from the eventual uniform theorem, not fixed in advance as the five
    named primes.
  - (4) "everything provable prime by prime has been proved" was too strong. More per-prime results remain possible
    (53, 59, 487; the bad primes via BH); they simply do not settle FIN.

## Addendum 26 (09-30 ~11:30): V025-BANK-K2 BANKED_LOCAL (7b311d5 content, 4344c6a stamp). Claude's pre-check clean
- **Branch:** head 4344c6a → 7b311d5 → 9828eae. Clean tree, no upstream, no tag. SOURCE_SNAPSHOT names 7b311d5
  (the loose end is closed).
- **The "81" text:**
  - the remaining mentions are all correct (RECHECK l.143 and l.194–195 describe the fix; l.228 is the negative
    control);
  - no wrong sentence remains in the paper or claims;
  - the negative controls reject restoring it, in the paper and in the spec.
- **Label:** the approved cross-family label is in claims.json (3 places) and in the paper (1).
- **Privacy grep** on the added K2 lines: 0 hits. The branch is 11 commits ahead of GitHub main 2a72621, with the same
  root.
- **The user's mid-run decision:** Codex's 12 third-party `source_checks/` files (rendered Kato/Jones pages and a Jones
  text extraction) are bound by path and sha256, NOT copied. Claude agrees: don't redistribute copyrighted page
  renders.
- **Claude's view on the three questions in CHECK_REQUEST_K2** (the Fable coordinator decides):
  - (1) Correcting the ≤ 81 line inside RECHECK's route-K addendum is right. RECHECK is outward prose, not a replayed
    record. The K2 addendum records the change, and git keeps the original.
  - (2) The README wording is the Fable coordinator's call.
  - (3) The hash-bind choice: accept.
- **Next:** the Fable coordinator checks BANK-K and K2 together, then the user's explicit push go. The plan: push as a
  new branch v0.2.5, with main fast-forward optional, then verify with ls-remote.

## Addendum 27 (09-30): PUSHED. v0.2.5 is on GitHub as branch `v0.2.5` (the user's explicit "push")
- **Pre-push checks:**
  - head 4344c6a, clean;
  - 11 commits ahead of main 2a72621, with the same root 6831af0;
  - the privacy scan of added lines (emails, privaterelay, the user's alias, tokens, keys, passwords): 0 hits;
  - the largest blob is 1.2 MB.
- **Push:** `git push https://github.com/Bome2017/bsd-seed-research.git v0.2.5-bank:refs/heads/v0.2.5` → [new branch].
- **Verified with ls-remote:** refs/heads/v0.2.5 = 4344c6a85e6940d6477807ef5d8dda761134bc2e (= the local head).
  refs/heads/main is UNCHANGED at 2a72621 (v0.2.2). No tag was created, and main was not fast-forwarded.

## Addendum 28 (09-30 ~15:30): ChatGPT's independent review of Codex's uniform synthesis. ACCEPT_AT_IMPORT_GRADE; Claude closed its caveat and checked Part B
- **The package:** ~/Downloads/BSD_UNIFORM_SYNTHESIS_INDEPENDENT_REVIEW_2026-09-30.zip.
  - Its manifest is 24/24 OK, checked in Claude's scratch extract.
  - The canonical filing is left to the Codex session that "is looking too".
- **The review's findings:**
  - Part A: 5/5 checks pass. At every good p ≥ 5, M_∞(δ) = 0, so a finite-length mod-p unit Kurihara witness exists. The
    integral normalizations are tracked, the Euler factors at 19, 59 and 487 are kept, and there is no extra exclusion.
  - Part B: its deductions hold (details below).
- **Caveat CLOSED by Claude:** Claude's own live fetch of CLW2.pdf (09-30) has sha256 0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98.
  This EXACTLY equals the pinned hash in Codex's SOURCE_BINDINGS.json.
- **Claude's Anthropic-side check of PART_B_DEPTH.md: all three deductions verified.**
  - (i) r_p = dim Sel_p: Kim Thm 1.8's Fitting formula with M_∞ = 0; Fitt_i = Z_p iff i ≥ μ(M); parity.
  - (ii) r_p = 2 ⟺ Sha[p^∞] = 0: the dual Kummer sequence splits over the free Z_p²; Nakayama; any divisible part is
    also excluded.
  - (iii) The depth test: BH θ^# ∈ Fitt₀ ⊂ (t)^d over F_p[t]/t^p. For p ≥ 5, v_λ(χ(θ)) = d₀ < 4 fixes the lowest-degree
    term, so d ≤ d₀ ≤ 3. E(K)[p] = 0 (the image contains SL₂(F_p) = the commutator), so restriction is injective and
    Y_G ↠ X_p, giving d_p ≤ 3. Parity gives d_p = 2, and so Sha[p^∞] = 0.
  - The strictness is needed; the "≤ 4" countermodel is correct.
- **Grade:** IMPORTED_PREPRINT for the coverage statement.
  - The author (Codex) and the reviewer (ChatGPT) are both OpenAI.
  - The Anthropic checks: source statements (Claude, Fable), the Δ-bridge (Fable) and Part B (Claude).
  - So it is cross-family at the statement and deduction level. There is no human review.
- **The exact open target:** ∃ finite S ∀ p ∉ S, ∃ a real cyclic degree-p K (conductor prime to pN; composite allowed)
  and a faithful χ with v_{ζ_p−1}(χ(θ_K^MT)) < 4. Or a two-prime unit Kurihara witness, or an independent Selmer bound.
  No mechanism is known.

## Addendum 29 (09-30 ~17:00): Codex's Pro-6 low-depth package CHECKED (PASS). Fable's three V026 fixes verified and folded in. One proposed kill test declined.
- **The package:** ~/Downloads/BSD_UNIFORM_LOW_DEPTH_FOR_PRO6_2026-09-30.zip and the matching _PROMPT.md.
  - Manifest 44/44 OK in Claude's scratch extract.
  - The PROMPT.md in the zip is byte-identical to the Downloads copy (sha256 28de1ff6…).
  - COPY_BINDINGS: 25/25 byte-identical to their originals on this Mac.
  - checks/check_controls.py re-run: PASS, 9 cases.
- **The math, checked at source.** CORRELATION_SETUP §1 matches Castella–Sano §1.1.1: the prime set L, the ideal
  I_ℓ = (ℓ−1, a_ℓ−ℓ−1)Z_p ∩ Z so that I_n ⊆ pZ, [a/n] normalized by Ω_E^+ = ∫_{E(R)} ω_E, and δ_n with discrete logs.
  - The least-positive-period convention differs by a factor 2, which is a unit for p ≥ 5.
  - Changing primitive roots multiplies δ by a unit.
  - The positivity identity is exact, and correctly labelled a reformulation only.
  - The marginal control Σ ij(i+j) = 0 over F_p is correct.
  - The Fitting ideals of Z_p² ⊕ (Z/p)² are (p²), (p), Z_p. The strict "< 4" is kept.
  - It claims no bound and gives no odds.
- **Relation to brief v2.** The target is the same: (ii) is primary and (i) is the alternative; (iii) ⟺ (ii) by B.21.
  The package is narrower (one mechanism), carries the primary PDFs and gates at 25/90 min.
  - Claude recommends ONE uniform session: the package on Pro. Brief v2 is held as the reference and the fallback, so
    that a later worker gets the package's return and does not repeat the screened mechanism.
- **The Fable coordinator's proposed prompt addition is DECLINED as written:** "must fail at (E,3): Ш[3] ≠ 0 ⇒ every
  two-prime δ ≡ 0 mod 3".
  - 3 | N (nonsplit multiplicative), and B.21 (r_p = dim Sel_p) is accepted only for good p ≥ 5. So "every two-prime
    δ ≡ 0 mod 3" follows from nothing accepted, and the prompt would hand Pro an unproved statement.
  - The target allows a finite exceptional S, so failure at one prime cannot kill a mechanism.
  - The correct uniform form is already item 4 of COLLISIONS_AND_KILL_TESTS.md: the mechanism must name the
    seed-specific input that excludes Z_p² ⊕ (Z/p)².
  - Paste Codex's prompt unchanged.
- **Fable's V026 fixes: all three verified at source and folded into inputs/V026_SCOPE.md.**
  - (1) Version caveat. The live arXiv 2608.29470 lists only v1 (checked 09-30).
  - (2) Ordinary coverage. Castella–Sano Thm B as printed requires p > 3, (sur) and p ∤ c_φ; its ordinary proof cites
    [Wan15, BCS25]; its supersingular clause needs squarefree N. a_19 = 4, a_59 = −4 and a_487 = −28 (Claude's point
    count; the worker re-derives them with ellap), so all three are ordinary.
  - (3) Frontier wording. At least one of (i)/(ii)/(iii) holds, each of which implies Ш[p^∞] = 0 (B.21, B.22); (i) is
    sufficient, and its converse is not claimed.
  - TASK.md gains two negative controls. The bundle manifest was regenerated: 13 files, OK.

## Addendum 30 (09-30 ~17:30): Codex's check of the three items (CONFIRMED_WITH_CORRECTIONS) verified by Claude. Corrections installed; label placement merged with the v0.2.5 precedent
- **The bundle:** ~/BSD_THREE_BRIEFS_REVIEW_CODEX_2026-09-30/ (the zip in ~/Downloads is identical).
  - Manifest 22/22 OK.
  - Codex's reconciled_inputs/ equal the live V026 files after Fable's three fixes, and its originals/ equal the live
    briefs. So nothing was lost to the concurrent edit.
- **Verified on the merits:**
  - Q.2 needs "irreducible". Counterexample: (X−36)(1000X−36001) has root 36.001 inside the interval and other root
    36, so the product is 0, a false certification.
  - Q.3 is correct: B ∈ Z_{>0}, and the interval forces B = 9.
  - K-D is too strong: a rationality-only proof is now RATIONALITY_ONLY partial progress.
  - A map merely to Reg proves nothing about q.
  - Grade names: common.py has PROVED_WRITTEN ("possibly combining imported theorems") and IMPORTED_PREPRINT, and no
    DERIVED. B.22 has kind CONDITIONAL.
  - The countermodel is an abstract dual module, not Sel_p.
  - B.22 uses the actual conductor m.
  - S must contain {2, 3, 2243, 4547, 5843}.
  - Denominator primes are exceptions for a rational scalar.
  - Unit and nonzero are kept distinct.
  - S.17–47 has one auxiliary per prime.
  - The level-p^k construction is candidate only.
  - The §6 negatives are scoped. Claude's earlier Heegner line holds only under the Heegner hypothesis.
  - First-derivative products need H holomorphic at 1.
- **One deviation from Codex: label placement.** Codex put the model-review label only in the verification/evidence
  records. But v0.2.5 carries it in the paper's S.3K theorem header and in the README S.3 row, as the user approved.
  - Merged: the verbatim label goes in the claims verification record; the paper and README get grades, citations and
    a one-line provenance clause.
  - TASK's "process markers" rule is clarified: gate statuses, lane names and draft banners.
- **Codex's binding point applied.** Fable's source-statement and Δ-component bridge check is reduction sheet §9
  (sha256 e9268897…746ec5707). It is copied into the evidence and bound.
- **Installed:**
  - corrected TASK.md and V026_SCOPE.md, plus the label merge, a changelog line and Codex's REPORT in inputs/;
  - manifest regenerated, 14/14 OK;
  - corrected Q36 and uniform v2 briefs, in BUILD_MAP and on the Desktop.
- **Launch implication, agreeing with Codex:** one Q36 session with the mechanism gate, not three copies. Its status set
  gains RATIONALITY_ONLY. The uniform Pro package is unchanged (Codex: "usable unchanged").
