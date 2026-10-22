# The uniform step: reduction sheet (Fable coordinator, 2026-09-29)

**Target U.** An explicit finite set B_U such that Sha(E/Q)[p^∞] = 0 for every p ∉ B_U.
- U plus finiteness at the primes of B_U gives FIN. Those primes are finite checks and priced compute
  (COMPUTE_LEDGER_2026-09-29.md).
- ORDER9 additionally needs vanishing on B_U outside 3.
- Q36 is separate (RAT/DEN).

No published proof of U-type finite support exists for any rank-2 curve over Q, and no screen so far found a method.
Every formulation below is SUFFICIENT for the part it names. They are related, not proved equivalent, and none is proved
necessary (GAP_ATLAS_R1 wording). Grades are per their governing files.

## 1. Inputs on record that any attempt can use (with their grades; some are conditional)

| Input | Statement | Grade (governing file) |
|---|---|---|
| G2 | For p ∉ S₀: infinitely many auxiliaries ℓ ≡ 1+p (mod p²), Frob_ℓ ↦ −I, with tame regulator R_{p,ℓ} ≠ 0 | written proof; Codex PASS (BSD_G2_INDEPENDENT_AUDIT_CODEX_2026-09-26) |
| Ota 6.4 | C2(p,ℓ) ≢ 0 ⟹ Sha[p^∞] = 0; one-way; no ordinarity needed | imported (Pro source audit) |
| Kato determinant | C2 = u·x_Q·#A_p·det B if s_p = 2, else 0 (BKS scope) | Codex-retained with corrections; Lean core |
| Theorem W (+ level p^k) | w_p = C2/((a_ℓ−2)R) is independent of ℓ, for p ∉ B*; at level p^k this gives w_p^∞ ∈ Z_p | W: Codex CONFIRMED_WITH_CORRECTIONS (A_REPAIR). p^k: lane 5, Opus-checked, not cross-family |
| K_E | Under refined Mazur–Tate (a conjecture): w_p ≡ 4c∞·#Sha·Tam/tors² = 32·#Sha (mod p); seed data 288 = 32·9 at 17–47 | lane 4 derivation + calibration (Fable CONFIRMED); lane 7 (#Sha = 4 test) |
| Kato Thm 18.4 | corank Sel_{p^∞} ≤ ord_{s=1} L_{p,α}, for every p where E is not a Tate curve (−1 at split p) | source-checked (Fable); Opus cross-model CONFIRMED (REPORT addendum 3, route 3(a)) |
| B.5 / A3 | M₂(p) ≠ 0 ⟹ Sha[p^∞] = 0 at good p ≥ 5, p ∤ 7N (split AND inert; ordinary AND supersingular) | conditional bridge (BLV), Lean core; M₂ open at every prime |

## 2. The formulations (the first missing input for each)

| # | Formulation | Gives | Primes covered | First missing input | Notes / collisions |
|---|---|---|---|---|---|
| F1 | Tame reciprocity law (B's T): w_p ≡ ι(Z) for p ∉ B, Z Sha-free, q-free, ≠ 0 | FIN-b off B ∪ P(num Z) | all p ∉ B | a THIRD formula for Z (MT value is #Sha-type; GPR value 8q needs RAT) | K_E now pins the predicted Z = 288 exactly. K-B is an admission rule, not a refutation (B_CORRECTIONS 8) |
| F2 | Witness nonvanishing: for almost all p, some admissible ℓ has C2(p,ℓ) ≢ 0 (mod p) | FIN-b | all p outside G2/Ota exclusions | ANY uniform nonvanishing mechanism for depth-2 Mazur–Tate coefficients mod p | a Sha-free statement about modular symbols. Must "see" the Sha support (B's O2). Flagged 09-27 (K288 note §5(3)). Screened 09-29 by A1: NO_SOURCE_FOR_THESE (§5) |
| F3 | d-∞ chain O1–O3 | FIN-b on the ordinary tail | good ordinary p | O1 RAT; O2 the finiteness-free p-adic Beilinson formula; O3 R_p ≠ 0 (Schneider's conjecture for E) | VERDICT_R1: CONDITIONAL_COMPARISON_SPECIFIED |
| F4 | Kato 18.4 analytic form (NEW): ord_{s=1} L_{p,α} ≤ 2 for every p | FIN-a at every non-Tate p (2243 needs ord ≤ 3) | all p except the additive primes 2 and 4547 (no α; Sha[2^∞] = 0 is already proved) | a uniform-in-p nonvanishing of the quadratic coefficient of L_p | Sha-free and RAT-free. Gives finiteness, not vanishing; with IMC and integral Kato at ordinary p, a unit version approaches F3 |
| F5 | Uniform Selmer upper bound dim Sel_p ≤ 2 (U22 I1; Euler systems) | FIN-a and FIN-b support | per construction | a rank-2 Euler/Kolyvagin system with uniform nonvanishing | V6: none among 9 (Codex: DLR enhanced regulators may be nonzero; LTXZZ uniform for its own motive only) |
| F6 | Identity C2 = u·det 𝔥 with a Sha-free unit u (U22 I3) | FIN-b | ordinary p split in Q(√−7) | the identity | U22 PAUSED (user, 09-29); revival condition |
| F7 | M₂(p) ≠ 0 for almost all p (B.5) | FIN-b | good p ≥ 5, p ∤ 7N | nonvanishing of M₂ at ANY prime; no evaluation method (mass ≈ 5.4·10¹⁴) | the widest coverage of the conditional bridges |
| F8 | LINE: one rational m on core pairs at every p-power level | finiteness for p ≥ 5, p ∤ N, and vanishing off P(num m) | p ≥ 5, p ∤ N | p-independence of m | Theorem C (hostile PASS). NOT equivalent to K288 (Codex 09-29) |
| F9 | Visibility: a fixed C annihilating i_*Sha(E) in J₀(N) | FIN | all p ∤ κ | C | FIXED_DEGREE_ALONE_INSUFFICIENT (Codex) |

## 3. What a new attempt must supply (admission)

1. Name an object, a map and a uniform statement, and say which row it attacks.
2. Pass the collision check: DNR (51 rows), STRUCTURAL_STOP (09-19 Eisenstein lower-bound arrow), B's K-B ledger
   (K1–K11, as corrected), V6 (C1–C9), lane 6 (H01–H08, R1–R7) and the 09-27 LOCAL1/LOCAL2/level-raising/DKV/Urban records.
3. Say how it avoids reducing to x_Q·#A_p, or to q ∈ Q. Either route is allowed if it proves the missing theorem
   independently (B_CORRECTIONS 8).
4. Run its cheapest kill test before anything else, and write the verdict at the scope of its cited statements.

## 4. Proposed first attempts (at most two; both $0 targeted source screens; the user's go)

- **A1 (row F2): mod-p nonvanishing of depth-2 Mazur–Tate coefficients, uniformly in p.** Search for any theorem giving,
  for a FIXED weight-2 newform and ALL large p, nonvanishing mod p of a twisted modular-symbol sum over characters of
  order p. That covers mod-p (non-archimedean) distribution of modular symbols, and μ-type or Washington-type
  nonvanishing with the character order varying with p.
  - *Kill test K-A1:* is any found result BOTH mod p AND uniform in p for a fixed form? Archimedean distribution
    (Petridis–Risager, Bettin–Drappeau style) and fixed-p/varying-character results do not qualify alone.
- **A2 (rows F3-O3 and F4): p-adic height nondegeneracy, or L_p″(1) ≠ 0, for almost all p.** Search for any
  unconditional result giving nondegeneracy of cyclotomic p-adic height pairings (Schneider's conjecture) or
  nonvanishing of the second derivative of L_p, for all but finitely many p, for a NON-CM curve of rank ≥ 2. Examples:
  p-adic transcendence (Bertrand-type, known for CM), and "four exponentials"-type inputs.
  - *Kill test K-A2:* is there any such theorem for any non-CM curve of rank ≥ 2? If not, record the exact CM or rank-1
    boundary of what is known.

Expected output of both: a scoped NO_SOURCE_FOR_THESE, or a named missing statement. A SOURCE_FOUND for either would be
the first uniform input on record. FIN, ORDER9 and Q36 are unchanged by this sheet.

## 5. Results (09-29, 17:45): both NO_SOURCE_FOR_THESE, scoped to the sources read

- **A1 (row F2; Opus worker, Fable check CONFIRMED).** Return: `~/BSD_UNIFORM_A1_MODP_NONVANISH_RETURN_OPUS_2026-09-29/`.
  The boundary among the sources read:
  - Uniform in p, mod p, at DEPTH 0 only, and only if L(E,1) ≠ 0 (FKK Thm 3.9, checked at source).
  - At depth r, known one p at a time from a length-r Kurihara witness (Kriz–Nordentoft Thm 1.4/Cor 5.20, checked at
    source). Their Cor 1.5 ("100% of primes") concludes only L ≠ 0, with r(p) uncontrolled.
  - FKK's uniformity comes from ONE nonzero rational, L_alg(E,1). The depth-2 analogue is F1/T2, already on record, so
    there is no new reduction.
  - WATCH: Kriz–Nordentoft successors.
- **A2 (rows F3-O3, F4; Fable worker; Opus grading pending).** Return:
  `~/BSD_UNIFORM_A2_PADIC_HEIGHT_RETURN_FABLE_2026-09-29/`. The boundary as found:
  - No theorem gives the p-adic regulator det ≠ 0 at even ONE prime for any curve of rank ≥ 2 (Burungale–Disegni
    2020; Banwait 2609.08431, CM, preprint).
  - Non-CM rank 1: even non-triviality of the unit-root height is open (Adachi–Katagiri–Shii §1).
  - Bertrand (CM, one point) is the one all-ordinary-p theorem located.
  - At good ordinary p: F4-at-p ⟺ (O3-at-p and Sha[p^∞] finite), under Kato + IMC at the recorded grade.
  - H06 scope correction: AKS Cor 1.3 applies at every good p of the seed, but its conclusion is only "one of two
    splittings non-trivial".
- **Seed-facts correction.** P₁ = (−3031, 327384) and P₂ = (−2394, 281520) are points of the MINIMAL model, not of
  y² = x³ − 22735x² + 106272484x. The models are isomorphic; PARI check by the Fable coordinator.
  - STANDING for task texts (Opus confirmed, addendum 6): on the short model (x = X + 7578) the basis is
    (4547, 327384) and (5184, 281520), PARI-checked.
  - Compute heights on the minimal model (PARI p-adic heights are model-dependent).
  - SEED_BSD_STATE_FOR_PRO_2026-09-27.md already states this correctly.
- **Where this leaves U.**
  - F2 lands on F1 (a Sha-free Z; the MT value is #Sha-type and the GPR value needs RAT).
  - F3-O3 and F4 land on Schneider's nondegeneracy conjecture for E, which is open even at a single prime in rank ≥ 2.
  - F5 needs a rank-2 Euler/Kolyvagin system (V6: none among 9).
  - Current known frontier: U, with the formulations above. PARTS_MAP posture applies: the next attempt must name a
    specific relation to construct; a further literature screen of these same rows is not the next step.

## 6. A3 (09-29, 20:40): NO_CONSTRUCTION_SURVIVES (Opus worker; Fable CONFIRMED)
- Five p-free candidates, each killed at its first test: the elliptic surface (Sha varies across its fibers: 1 or 4 on
  621 rank-2 fibers, 9 at the seed; index 1 ⇒ 32 ≠ 288); Yun–Zhang as template (no known number-field analog of the
  two-leg moduli space, "at least for the time being", §1); Theorem W at composite moduli (CRT assembly, = LINE);
  plectic points (p-dependent; archimedean version an open question); first-derivative height formulas (0 = 0).
- By-product, conjecture grade: K_E = 4c∞·Tam·#Sha/tors² fits a second rank-2 curve (t = −36/5, N = 2900, w = 24).
- 288 = 2·144 (den t₀) is a coincidence: the N = 2900 fiber gives 24, not 2·5.
- **Where U stands:** three attempts negative (A1, A2 literature; A3 construction). No candidate on record passes K-P.
  Return: `~/BSD_UNIFORM_A3_RANK2_HEEGNER_ANALOG_RETURN_OPUS_2026-09-29/`.

## 7. Scoping corrections from Astra's cross-family view (2026-09-30)
- K-num is a BENCHMARK for the conjectural refined-MT constant (288 on E, 24 on N = 2900), not a necessity for every FIN
  route. The finite residues force only Z ≡ 288 (mod p) at the settled primes; "Z = 288 or height > 3.7·10⁹" needs the
  recorded height bound. Lemma A.1's "Ш-free invariant equal to 9 on E and 1 on the 2900 curve" is conditional on
  targeting that exact constant; a candidate with 3-part 1 fails that target, which alone refutes no other
  finite-support identity. A route may instead aim at a uniform upper bound or a direct nonvanishing theorem with no
  scalar at all.
- "Ш-free" means not ASSUMING the unknown conclusion; an independently PROVED statement equivalent to it is admissible.
  Same for rationality of q.
- Admission rule 5 (paired-state test): does the proposed relation exclude nonzero excess Selmer torsion? If it holds
  unchanged with and without such torsion, it cannot force the witness nonvanishing (B's O2, made operational).
- Astra: no new relation identified; no objection to pausing broad attempts after Pro; reopening needs a new source,
  an exact map, an independent bound or a geometric construction, not a reworded obstruction.

## 8. Admission rules, corrected after Codex's reopening review (2026-09-30; `~/BSD_REOPENING_REVIEW_CODEX_2026-09-30/`)
Status of that review: NO_RESCUED_GLOBAL_PROOF; SEARCH_GATES_NEED_FURTHER_SCOPING. Nothing below is new FIN progress.
- **R1 (replaces the blanket K-P).** "Defined independently of p" is the test for the p-free-scalar architecture (F1,
  LINE, K288) only. A uniform FIN theorem may use p-dependent objects and auxiliary choices, provided ONE argument and
  ONE finite exceptional set cover every p outside it (G2 is the model). Fixed-p or density-one theorems are not enough.
  Consequence for the record: the A3/A4 kills at K-P (trace lift, derived classes, horizontal measures, Kummer index)
  are kills of the p-free-scalar target, not refutations of uniform strategies built on those objects; their real
  remaining failure is a missing bound, nonvanishing, coverage or comparison, and must be named as such.
- **R2 (replaces the blanket K-F).** Do not assume finiteness or orders of unknown primary parts, the witness
  nonvanishing, or q ∈ Q. Independently PROVED finite arithmetic (the certified Ш[3^∞] ≅ (Z/3)²; the primes ≤ 47) and
  independently proved equivalent criteria are admissible. Inserting 9 into a constant is not a new arrow.
- **R3 (K-num, role stated).** Certified residues are mandatory for an identity that claims to reproduce w_p; they are
  not a test for an annihilator or one-sided bound. Exact 288 needs the height bound, never the residues alone.
- **R4 (paired-state test on the endpoint mechanism).** The claimed complete mechanism must change when excess Selmer
  torsion is present. An intermediate lemma may lack a standalone FIN consequence, but must say what it supplies.
- **Reopening test.** Name the prior first failing step, the new input that changes it, and the proposed map or
  inequality. A scope correction alone authorizes no construction work.
- **Reframed target for Pro (and any future lane):** write ONE concrete upper-bound or nonvanishing relation, under
  these rules, that says how excess Selmer torsion is excluded and which infinite prime sets it covers; p-dependent
  tools allowed; no obligation to derive 288 or Q36. First location named: uniform depth-two nonvanishing of the
  quadratic witness (Kriz–Nordentoft Thm 1.4 / Cor 5.20 give v_p ≤ r(p)/(p−1) with r(p) the per-p Kurihara length,
  uncontrolled; a proposal must bound that depth independently of the Ш conclusion). Second: an independent uniform
  annihilator D of Ш, or a one-sided integral bound on cofinal torsion layers. Third, only with a concrete map: a
  point/cycle construction from P₁, P₂ that also supplies the analytic/Hecke relation.
- U22 stays paused (Link 2's missing upper/exact relation is untouched by gluing/primitivity). The surface stop is
  "no map transfers a bound from the surface to this fiber", not "cannot help".

## 9. New input (2026-09-30): mod-p Kurihara existence at EVERY good p ≥ 5, supersingular included
Source-version change found by Codex (`~/BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/`, 26/26; Fable and Opus verified both
sources at statement level):
- Castella–Liu–Wan, "Kato's main conjecture for nonordinary modular forms", AUTHOR-HOSTED revision dated 2026-09-21
  (`web.math.ucsb.edu/~castella/CLW2.pdf`), Thm A: k = 2 < p, p > 2 good nonordinary, p-regular (a_p = 0 ⇒ α ≠ β), and
  (ram): some ℓ ∥ N with ρ̄ ramified at ℓ — the seed's I₁ prime 2243 gives this for EVERY p. Remark 1.5(3): the old
  squarefree-N condition of the arXiv version is replaced by (ram). Bridge: l.983 "Conjecture 2.19 (for η) is
  equivalent to Conjecture 1.1 (for ηω^{k−1})"; at k = 2 the proved component ω^{k/2} = ω is the cyclotomic one for E.
- Castella–Sano arXiv 2601.14504 v1: Thm A (p > 3, (sur), p ∤ c_φ): refined Kurihara ⟺ IMC 2.2.2 (= Kato Conj 12.10);
  Cor A adds p ∤ Tam ⇒ some Kurihara number δ̄_n ≠ 0. Thm B as printed: good ordinary p (no extra condition), or
  supersingular with N squarefree (citing the OLD CLW; superseded for the seed by CLW2).
- **Statement (IMPORTED_PREPRINT; author-hosted revision; Pro check pending):** for every good p ≥ 5, some Kurihara
  number of E is nonzero mod p. The seed meets (sur) for all odd p, c_φ | 2⁹, Tam = 16.
- **What it does NOT give:** any bound on r_p := the minimal witness length. By Kim's structure theorem (2203.12159
  Thm 1.8, as applied by Codex) r_p = dim_{F_p} Sel_p(E/Q) ≥ 2, even; so r_p = 2 ⟺ Ш[p^∞] = 0. Sha-blind.
- **Consequence for the map:** the uniform part of FIN-b on good primes is exactly ONE inequality: r_p < 4 for all
  but finitely many p. Equivalent sufficient form (Codex, from the retained Bullach–Honnor argument): for each large p
  an order-p character, composite conductor allowed, whose correctly normalized Mazur–Tate value has depth < 4. The
  field and auxiliaries may depend on p; no G2 singleton, no 288, no Q36 needed. The supersingular primes are no
  longer a separate gap for the EXISTENCE statement (DNR 46 and the definite-theta note are superseded on that point;
  the depth bound is the wall at every p).
- Kriz–Nordentoft's bound v_p ≤ r(p)/(p−1) takes r(p) as input; it does not bound it. No one has a mechanism for
  "r_p < 4" that does not assume the Ш conclusion. No campaign is authorized by this input alone.
- First job for Pro when it resets: check Codex's application (the bundle `~/BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30.zip`),
  in particular the ω-bridge, the integral normalization into Castella–Sano, and Kim's indices.

### 9a. Codex review-check of its own synthesis (2026-09-30; `~/BSD_UNIFORM_SYNTHESIS_REVIEW_CHECK_CODEX_2026-09-30/`, 31/31)
Verdicts: SOURCE_UPDATE_APPLIES_AT_RETAINED_INPUT_GRADE; ALL_GOOD_PRIME_KURIHARA_EXISTENCE; UNIFORM_LOW_DEPTH_BOUND_STILL_OPEN.
- Source pinned: CLW2.pdf sha256 0686fa41… (Codex pinned copy = Codex fresh download = Fable download); arXiv
  2608.29470v1 is a different file (955f9d70…). The version difference is real.
- 19, 59 and 487 are INCLUDED in the existence statement (good ordinary primes; Castella–Sano Thm B ordinary case
  has no condition beyond (sur), p ∤ c_φ, and Cor A's p ∤ Tam). They stay excluded from Theorem W's domain only.
- Countermodel that shows why existence cannot finish: a rank-2 free module plus an extra (Z/p)² has r_p = 4 while
  still having a unit Kurihara witness. Existence at unspecified depth is exactly Sha-blind.
- Broader sufficient test (DEPTH_TARGET.md, written deduction from Bullach–Honnor Thm 1.4(b) + Kim Thm 1.8 + even
  Selmer dimension): for p ≥ 5 good and K/Q any real cyclic degree-p field of conductor m prime to pN, a faithful
  value with v_λ(χ(θ_K)) < 4 (λ = ζ_p − 1, θ_K fully normalized) gives Ш[p^∞] = 0. Composite squarefree m allowed.
- Decisions adopted: supersingular coverage reopened narrowly (this application only); uniform low-depth bound is
  THE target; U22 paused; 288/LINE/rationality are alternatives, not gates; prime ladder and bad-prime compute frozen
  for this objective; no transfer from Selmer statistics over varying twists/extensions.
- Independence note: this check is Codex reading Codex (same model). Pro's check (different model) is still the
  independent one; Fable and Opus verified both sources at statement level. Model readings are checks at their grades,
  not a human referee or formal verification.
