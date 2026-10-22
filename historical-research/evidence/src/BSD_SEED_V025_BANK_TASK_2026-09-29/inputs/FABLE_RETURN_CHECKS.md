# Cross-model pre-audits of the Opus-worker lanes (Fable coordinator, 2026-09-29)

Checker: Claude Fable 5.1. The workers were Claude Opus 5.5. This is a different model, but the same family (Anthropic).
These are pre-audits under the RUN_NOW checklist (a)–(g), not independent-family audits. Grade changes in
PARTS_MAP/UNIFORMITY_ATTEMPTS are the Opus coordinator's to record.

## Lane 4: TAME_CONSTANT_NORM (Opus): CONFIRMED at its stated grade, with two scope notes

- **Integrity.** MANIFEST 16/16. All four scripts were re-run from a scratch copy with gp 2.17.3 (kill 1.9 s, curves 44 s,
  controls 378 s, replay 0.9 s). stdout is byte-identical after removing PARI "increasing stack size" warnings, which my
  run sent to stderr and theirs captured in stdout.
- **(a) Domain.** 6 curves and 15 eligible (curve, p) pairs; 68 rows with R ≠ 0 and 7 with R = C2 = 0. Anomalous p = 5
  rows for 433a1 and 664a1 are correctly excluded. The table was hand-checked: K_E = 4·c∞·Tam/tors² gives 1615a1 = 16
  (5 mod 11, 3 mod 13), 664a1 = 16, 655a1 = 8, 1615a2 = 16, 433a1 = 4 and 389a1 = 8 (3 mod 5). All match.
- **(d) Checks test.** The controls reject each wrong variant on every row: power of 2, generator (a SIGN at p = 5),
  period, −K, K·c_N, and Tam/tors.
- **(f) Object identity.** The production symbols are Re λ/ω₁, confirmed by a Birch ratio to 38 digits and by the Arb
  pipeline at 389a1, l = 29. c_per = 1/c∞ agrees with Codex's A_REPAIR (c_per = 1/2 for Δ > 0).
- **(g) "Always" claims** were tested at p = 5 (c0 = c1 = 0; R = 0 ⟹ C2 = 0; c_N cancels; involution-invariant).
- **Scope note 1: the #Sha factor is DERIVED, not calibrated.** Every test curve has sha_an = 1, so "K ≡ 288 is
  evidence for #Sha ≡ 9 (mod p)" rests on the conjecture's form, not on data. A cheap test exists. In Cremona's local
  data (N < 500,000), the smallest-conductor rank-2 curve with sha_an ≠ 1 is **194040co6 (sha_an = 4)** (field 29 =
  rank, field 45 = sha_an). Exact msfromell at this level is heavy. The production numerical symbol method, as used on
  the seed, is not. 4 ≢ 1 (mod p) for p ≥ 5 separates the two predictions. Recommended; not run.
- **Scope note 2:** the Manin factor at c ≠ 1 is untested (no rank-2 example with N ≤ 5000). The return states this.

## Lane 6: UNIFORM_STEP_FRESH (Opus): CONFIRMED (NO_NEW_ROUTE_FOR_THESE, scoped), with one wording correction

- **Integrity.** MANIFEST 18/18. The listing count of 11,019 is the pages' own totals (NOTES l.52). An earlier chat
  figure of 11,053 is not in the record.
- **Source verification** (arXiv abstract and HTML pages, fetched 09-29). All seven theorem-level hits exist with the
  stated titles and dates:
  - 2510.10277 Van Order (central first derivatives);
  - 2603.28327 Fornea (plectic Heegner classes; "expected to provide finer control");
  - 2608.29470 Castella–Liu–Wan. Theorem A, verbatim: "N is squarefree". Corollary C: semistable and L(E,1) ≠ 0;
  - 2509.13894 Bullach–Burns. Verbatim: "L(E/K,s) does not vanish at s=1";
  - 2609.35626 Adachi–Katagiri–Shii ("at least one of the two cyclotomic p-adic height pairings is non-trivial");
  - 2607.07531 Bieker and 2608.07173 Feng–Yun–Zhang (function fields, shtukas).

  The first-failure hypotheses quoted in H04 and H05 are in the theorem statements, not only the abstracts.
- **Record claim.** Castella–Sano 2601.14504 is in the record (`BSD_CODEX6_EXACT_SHA_COVERAGE_2026-09-19/`, master
  STATE.json). Correct.
- **Part (b) not run.** This is correct under the task's condition (no specific named relation). R1–R7 are listed.
- **Correction (wording).** H08's header treats nine abstract-level items as exclusions ("scope fixed by the abstract").
  By the project rule, never exclude from an abstract, they are TRIAGE, UNCHECKED at theorem level, like the title-only
  rows. RETURN.md registers only the theorem-level H01 and H03–H07 as "screened, not applicable", so no record claim is
  affected. When H08's items are cited, cite them as unchecked.

## Lane 3: BAD_PRIME_STREAMING (Opus): CONFIRMED (READY_FOR_DECISION) at its stated grade

- **Integrity.** MANIFEST 954/954. The frozen engine source (56a43aac), the pinned binary
  (`BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/arbcore`, 47d07f2e, mtime Sep 19) and the p = 23 pinned corpus root (a83f42e3,
  `PINNED_ROOT_p23_l47.json`) are unchanged.
- **Re-run from a scratch copy** (the suites write under the return's scratch/, so I ran a copy):
  - `tests/multiunit_test.sh`: 22/22 PASS (ordering, restarts from 0 and from a non-zero checkpoint, truncation path,
    tamper controls, the table-segment wait bug's two regression tests), 2 min 58 s;
  - `tests/orch_restart_test.sh`: 12/12 PASS (lost spool regenerated with an identical receipt, shared pass, output
    byte-identical).
  - Not re-run: 3a (1.1 CPU-h) and 3b. Their byte-identity claims rest on the return's logs plus these suites.
- **(f) Object identity.** The certification chain is unchanged: `wverify_distinct` re-verifies every segment and the
  engine hashes what it consumes. `apwit_v` is an untrusted producer, so its speed affects cost, not soundness. The
  bit-identical witnesses on 3 segments are an extra check.
- **Cost claims.** The frozen `apwit` measured 324.5 s/segment at 10¹³ vs 151.8 for `apwit_v` (2.14×). rates.json's 10¹³
  anchor agrees with M1v to 0.3%. Rates between 10¹³ and 3.9·10¹³ are interpolated (stated). The dollar figures are
  labelled scenarios with assumed prices (PLAN §5).
- **Gates before any paid run (PLAN):** the Linux port with a bit-identity re-run, the pinned `apwit_v`, split heavy
  units, a ≈ 2 h pilot to measure e.
- **Scope.** The BH criterion stays at its preprint/retained-input grade (Codex-validated earlier). Lane 3 engineered and
  priced the evaluation; it settled no prime. The ledger is updated.

## Not mine to grade (Fable workers; the Opus coordinator checks them)

Lanes 1, 2 and 5. Risks worth that check's attention:
- **Lane 5.** Lemma S claims the modular element = one scalar × regulator mod I³ "whatever the structure of Sha". Check
  that it does not use H¹_f ≅ Z_p⊗E(Q), which needs T_p Sha = 0, or any other finiteness input.
- **Lane 1.** It asserts that SU's (12.3.5.b) is inconsistent with (3.4.5.b), and that SU Prop 12.3.6 as printed would be
  false for the seed if the 2243-primitive function is integral. These are claims about a published paper; they need a
  source-level check of the author copy against the journal version.
- **Lane 2.** PASS at the retained grade, same-family. The tight radius margins at p = 17 and 23 (about 99% of the half
  spacing) rest on the engine's tail bound.

FIN, ORDER9 and Q36 are unchanged.

## R23: UPPER_REPAIR_SCREEN (worker was FABLE, not Opus; folder name says OPUS). My check is SAME-MODEL; Opus's governs

- **Integrity.** MANIFEST 16/16. Sources were downloaded to `sources/` (Kato via B1, Ochiai published PDF, Wake v3, Kim).
- **Kato Thm 18.4: CONFIRMED at source** (`Kato2004_AST295.txt` l.8665–8720).
  - The only assumption is §18.1: α with 1 − αu | the Euler factor and ord_p(α) < k − 1. There is no restriction on p.
  - At multiplicative p the factor is 1 − a_p u, so α = a₃ = −1; ord = 0 < 1.
  - "The choices of ω and γ are not important": the order does not depend on normalization, so B1's MS-B1 does not arise.
  - Thm 18.4: corank_O Sel(T) ≤ ord_{s=k/2} L_{p-adic,α} when α ≠ p^{(k−2)/2}. Rem 18.3: that equality holds for E
    exactly when E is a Tate curve; the seed at 3 is nonsplit. The α ≠ 1 case is proved via Perrin-Riou (cited).
  - **Deduction (mine; same-model):** a_{4,2} = 15480 ≡ 9 (mod 27) and SW Prop 3.5 (a₂ ≡ a_{4,2} mod 27, an existing S.3
    import) give a₂ ≠ 0, so ord ≤ 2. Rank 2 then gives corank Sel = 2, so Sha[3^∞] is FINITE with no Skinner, SU or Jones
    input. It gives no bound on the ORDER. To confirm in the cross-check: Kato's Sel(T) (Ka 14.1) = the classical
    3^∞-Selmer group, and Kato's L_{p,α} for α = a_p at p ∥ N matches the MTT function SW use, up to a nonzero constant.
- **Ochiai 2006: CONFIRMED statements.** "We fix a prime number p ⩾ 3" (Oc l.248). Thm 3 (l.553–567) assumes (Ir) and
  H^{n.o}_F ≅ O[[X₁,X₂]], plus τ, τ′. The one-sided reading of Cor 7.5's proof is the worker's (marked UNCHECKED); fine.
  - **Note on MS-R3's sufficient condition.** "No mod-3 congruence at weight 2, level N ⟹ H^ord_F ≅ O[[X]]" also needs
    Hida's control theorem at p = 3, which Wake Rem 1.6 reports as proved for p ≥ 5. Flag it.
  - A possible local test of MS-R3 (my suggestion, unverified): the mod-3 adjoint Selmer group via class field theory
    of the degree-24 S₄ field cut out by ad⁰ρ̄₃. Its vanishing ⟹ R = T = Λ-type regularity, under TW-type hypotheses at
    p = 3 to be checked.
- **CORRECTION: arXiv:1303.0406 (Wake) is WITHDRAWN.** v4 (22 Aug 2017), verbatim: "This paper contains many mistakes,
  and would require substantial revisions … (see the articles arXiv:1407.5707 and arXiv:1407.5709 of B. Cais)".
  - The return cites v3's Cor 1.7 as "a p = 3 extension exists". That must be WITHDRAWN.
  - Route 2's lead is Cais 1407.5707/5709 (reported p > 2; not read).
  - Wake's Rem 1.8 ("Ohta requires p > 3") is secondhand AND from a withdrawn paper. Treat it as UNCHECKED.

## B2: LOWER_HALF_3DESCENT (Opus worker): CONFIRMED (CERTIFIED), cross-model pre-audit

- **Integrity.** MANIFEST 90/90. `verify_certificate.gp` (170 lines) has no file reads or external calls. Re-run standalone
  in an empty scratch directory: exit 0, 0.20 s. CERTIFICATE RESULT: PASS (79 degree-1 primes × 4 classes, F₃-rank 4).
  NEG(b), NEG(b′) rank 3 (rejected); NEG(c2), NEG(c3) wrong Jacobian (rejected); SELF-TEST 1.
- **Independent checks (my own code, not the verifier's):**
  - Jacobian: PARI `ellfromeqn` + `ellminimalmodel` on each cubic gives exactly E's reduced minimal model
    [0,−1,0,−66020924,−65074271436]. Δ(E) = 2⁸·3²·2243·4547³·5843² from PARI's `E.disc` matches the verifier's disc(Cᵢ).
  - Local points: smooth F_p-points on z = 1 (F ≡ 0, gradient ≢ 0 mod p, so Hensel lifts) at every bad prime:
    C₁: [1,1,1]₂, [0,0,1]₃, [0,2190,1]₂₂₄₃, [0,1019,1]₄₅₄₇, [0,4267,1]₅₈₄₃ (the same as the verifier's);
    C₂: [0,1,1]₂, [0,1,1]₃, [1,1133,1]₂₂₄₃, [0,2364,1]₄₅₄₇, [0,4914,1]₅₈₄₃.
    Other primes: smooth reduction (disc = Δ(E)), so Hasse–Weil and Hensel apply. R: odd degree.
- **Independence (code read):** κ(P) via the tangent-line function at T ∈ E(L)[3], and the cubic class via the
  Hesse-pencil flex triangle and Cardano, both computed from coefficients. Cubic residue symbols kill cubes, so rank 4 ⟹
  independent in L^×/L^×³ ⟹ independent in H¹(Q,E[3]) (injectivity of the descent map is not needed). The self-test
  checks the two constructions agree up to inversion on Kummer cubics (P₁, P₂, P₁+P₂); rank is unaffected.
- **Grade.** Explicit certificate, exact and GRH-free. It rests on published descent theory (the class map for plane
  cubics) and on rank E(Q) ≤ 2 (R.1) and E(Q)[3] = 0. **dim Sha[3] ≥ 2, i.e. #Sha(E/Q)[3] ≥ 9, with no Skinner/SU input.**
- **Combined with R23 (Kato 18.4, same-model-checked):** Sha[3^∞] is FINITE and contains (Z/3)². The exact value (≤ 9)
  remains open without Skinner as printed: B3 (GRH + ⟨C₁,C₂⟩), or Ochiai + MS-R3.

## ChatGPT deep-research report ("deep-research-report 9.md", iCloud, sha256 f745f145f4631077…, 30 lines): FACT-CHECKED, LOW RELIABILITY

It gives no verbatim theorem statements (the prompt required them) and cites dangling references [38], [54], [88].
Checked at source 09-29:
- **Wrong:**
  - Kato 2004 is Astérisque 295 (local copy header), not the Annals.
  - eclib's latest release is 20250627 (GitHub releases), not "v20160206".
  - "ndescent (Oisin Kyriazis), Magma/C++ 3-descent" is actually "pari/gp script for n-descent on elliptic curves
    (experimental)": 2 commits, file 5desc.gp.
  - The CT-pairing author is T. Fisher, not "D. Fisher".
  - Fukaya–Kato 2006 is not Annals. The "Skinner–Sangiovanni Vincentelli (2017)" Ohta generalization is still unpublished
    ("revisions in progress", his page).
- **Incomplete:**
  - "No published theorem proves char ⊇ (L_p) at p | N": it omits Ochiai 2006 Thm 3 + Cor 7.5 (source-checked: p ⩾ 3; a
    Hida-family divisibility specializing to weight-2 points; needs Hecke regularity).
  - It omits Kato Thm 18.4 (source-checked corank bound at non-Tate p | N).
- **Unverified leads worth one check each:**
  - "Kitagawa [Kit94] assumes p ≥ 5". Ochiai (p ⩾ 3 throughout) imports Kit94 Thm 1.1 and needs an H^ord-basis of B^±. If
    Kit94 needs p ≥ 5, Ochiai's route at p = 3 needs its own justification.
  - "Ohta [Oht99/00] assume p > 3" (agrees with the withdrawn Wake remark; both secondhand).
- **Consistent with the records:** there is no public 3-descent or 3-Selmer Cassels–Tate code outside Magma (B2 wrote its
  own 3-descent; B3 must implement Fisher's pairing from scratch).
- **Net:** use it only as leads. Nothing in it enters the record as fact.

## B3: CASSELS_TATE (Opus worker): CONFIRMED as INCONCLUSIVE_AT (cross-model pre-audit)

- **Integrity.** MANIFEST 29/29. `replay.gp` re-run from a scratch copy: exit 0, 0.10 s, output as reported.
  - |d_L| seed 10^58.67, 681b1 10^14.67, 1913b1 10^16.47, FN's 17127b1 10^7.51.
  - dim H¹(Q_v, E[3]): v = 2, 2243, 4547 → 0; v = 3, 5843 → 2; v = ∞ → 0. So only 3 and 5843 can contribute.
  - The flex fields of C₁, C₂ have degree 9, |d| 10^58.67 and 10^59.63. The Jacobians re-confirmed.
- **Scope of the verdict is correct.** The blocker is Fisher–Newton's global step (Problem 3.5: an explicit
  A ≅ M₃(L) over L of degree 8, |d_L| ≈ 10^58.7). "Out of reach within 12 CPU-h / 16 GB" is an ESTIMATE from worst-case
  Ivanyos–Rónyai–Schicho bounds, stated as such, not an impossibility.
- **Checker's note (untested suggestion).** B2 did succeed at LLL zero-divisor searches in 9-dim algebras over Q at this
  curve (297-digit structure constants). A CAPPED probe of the 72-dim (over Q) splitting via a maximal order and LLL
  might beat the worst-case bound in practice. That is a bounded experiment, not a claim.
- **CONSEQUENCE.md logic checks.**
  - If ⟨C₁,C₂⟩ ≠ 0, then S = span is an orthogonal direct summand of Sha[3^∞]: the restriction map to Hom(S, Q/Z) is onto
    and S ∩ S^⊥ = 0; no finiteness is needed.
  - With Kato 18.4 the complement is finite of the form B×B; with GRH (B2's dim Sel₃ = 4), Sha[3^∞] ≅ (Z/3)².
  - The Mazur citation correction ("Visualizing elements of order three…", Asian J. Math. 3, 1999) is right.
- **Net.** The 3-part's GRH route is blocked at one global step; its unconditional routes are reduced to research-level
  local statements (MS-R24 from R24, MS-R3, MS-B1). S.3's exact value still rests on Skinner's printed theorem.

## A1: MODP_NONVANISH, row F2 (Opus worker): CONFIRMED as NO_SOURCE_FOR_THESE (cross-model check, 17:45)

- **Integrity.** Return MANIFEST 25/25 OK. Task bundle unchanged (17/17).
- **FKK boundary, checked at source** (arXiv 0711.1771 v3, J. LMS; PDF text).
  - Thm 3.9 is verbatim as quoted: "Let E/Q be an elliptic curve such that L(E, 1) ≠ 0. Then for all but a finite
    number of primes ℓ, there is a set of primes S_ℓ of positive density such that L(E, 1, χ) ≠ 0 …".
  - Thm 3.5: L_alg(f,1,χψ) ≡ (a_p − δ(p) − 1)·L_alg(f,1,χ) mod l.
  - Depth 0 only; the seed fails the hypothesis.
- **Kriz–Nordentoft boundary, checked at source** (arXiv 2310.20678 v3, 16 Nov 2025; PDF text).
  - Thm 1.4 and Cor 5.20 are stated at one p. The hypothesis is Conj 5.12 at that p, with "≫_{E,p}" and a bound
    v_p ≤ r/(p−1), where r is the length of the Kurihara witness.
  - Cor 1.5 concludes L(E,χ,1) ≠ 0 for "100% of primes p". Its proof covers only primes with p ∤ M_E, good ordinary
    reduction and non-anomalous p.
  - Thm 5.13 (Kim) needs p ≥ 5, surjective ρ̄, p ∤ c_E, E[p](Q_p) = 0 and p ∤ Tam. Under these hypotheses Conj 5.12 is
    equivalent to Kato's Kolyvagin system being nonzero mod p, which is equivalent to the IMC at p. All of these are
    Sha-blind, so A1's O2 point stands.
- **Withdrawal sweep.** I ran an arXiv API query over all 37 ids cited in A1 and A2. None is withdrawn.
  - One comment flag: 2010.12403 v2 fixed "a small mistake in Theorem 1.5". A1 uses Thm 1.1, so this has no effect.
- **Triage items that collide with earlier lanes** (I checked the abstracts):
  - Castella–Sano 2601.14504 (lane 6 H02: per-p statements);
  - Wei–Zhai 2605.09251 (complex Taylor coefficients in quadratic-twist families; archimedean).
  - Both correctly left out.
- **"Why not REDUCED" holds.** FKK's uniformity comes from one nonzero rational number, L_alg(E,1). The depth-2 analogue
  is F1/T2, which is already on record. A uniform bound r(p) = 2 would already be FIN-b support at good ordinary p (the
  record, flagged for referee).

## A2: PADIC_HEIGHT, rows F3-O3/F4 (Fable worker): integrity only. The Opus coordinator grades it.

- **Integrity.** MANIFEST 17/17 OK. Task bundle unchanged (19/19). Its 10 source ids are in the withdrawal sweep above:
  none withdrawn.
- **Task-text slip, confirmed by me (PARI 2.17).**
  - P₁ = (−3031, 327384) and P₂ = (−2394, 281520) lie on the minimal model [0,−1,0,−66020924,−65074271436]. They do not
    lie on y² = x³ − 22735x² + 106272484x.
  - The two models are isomorphic (same j and conductor).
  - The slip is in my TASK seed-facts line only. The bundle stays frozen; the correction is recorded here and in the
    sheet.
- **Content grading is pending with Opus.** The claims to check are:
  - the H06 scope correction (AKS Cor 1.3 applies at every good p);
  - the "no det ≠ 0 at a single prime for any rank-≥2 curve" boundary (Burungale–Disegni 2020; Banwait 2026);
  - the F4-at-p ⟺ (O3-at-p ∧ Sha[p^∞] finite) bookkeeping at good ordinary p.
