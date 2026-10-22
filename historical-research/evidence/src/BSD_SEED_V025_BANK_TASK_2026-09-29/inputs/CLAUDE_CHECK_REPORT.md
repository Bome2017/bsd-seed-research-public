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
