# LANE3_SEED_2243_12_FULL_BSD: `BSD_DISTANCE_MAPPED` — rank 2 (PROVED) = r_an (CERTIFIED_NUMERIC), L″(E,1)/2 certified, Sha_an = 9 (NUMERIC); full BSD OUT_OF_REACH (four audits PASS_WITH_CORRECTIONS; the two BLOCKING items, in B and D, were resolved on re-audit)

**How far from full BSD (one sentence).** The seed is two open theorems short of full BSD — finiteness of Sha (no "Sha[p^∞] = 0 for almost all p" is known for any curve over Q with r_an ≥ 2) and rationality of L″(E,1)/(Ω·Reg) — and below that level only Sha[2^∞] and Sha[5^∞] are closed, while p = 3, the one prime where BSD predicts non-trivial Sha (order 9), can be decided by a feasible ≈ 14 CPU-h run (awaiting authorization; decisive when ord₃ a₂ ≤ 2) whose answer would be CONDITIONAL on the Skinner Thm A identifications.

Seed (m, n) = (2243, 12): E: y² = x³ − 22735x² + 106272484x, N = 2³·3·2243·4547²·5843, T = (0,0), P₁ = (4547, 327384), P₂ = (5184, 281520). Lane files: `A_analytic/`, `B_invariants/`, `C_frontier/`, `D_primes/`. Audits: `audits/`.

**What this report is.** A synthesis. It does not re-derive anything. Where an audit corrected a label and the lane did not apply the correction, this report uses the corrected label; audits govern. No label is upgraded. Nothing assumes BSD, Manin's conjecture, p-adic BSD, GRH or finiteness of Sha unless the label says CONDITIONAL. Every Sha[p^∞] statement for p ≠ 2 carries the qualifier **"via the derived v₂(c₀) ≤ 8 lemma"** (gate MANIN_2_PRIMARY_GATE_2243_12: reviewer-accepted; **operator merge of SHA5 pending**).

## 1. Analytic result (lane A; AUDIT_A PASS_WITH_CORRECTIONS, no blocking item)

| claim | value | label | evidence |
|---|---|---|---|
| root number | w = +1 | PROVED | Product of local root numbers (2: +1, 3: +1, 2243: −1, 4547: +1 by Rohrlich, 5843: +1, ∞: −1). Independently, Monsky's 2-parity theorem with rank 2 and Sha[2] = 0. `A1_ORDER_GE_2.md`; AUDIT_A item 5 |
| L(E,1) = 0; ord_{s=1} L(E,s) even and ≥ 2 | — | PROVED | P₁ has infinite order, so Kato 2004 Thm 14.2 (or Gross–Zagier + Kolyvagin) gives L(E,1) = 0; w = +1 gives even order |
| formula | L″(E,1)/2 = 2Σ(aₙ/n)·G₂(2πn/√N), G₂(x) = ∫₁^∞e^{−xy}log y dy/y | PROVED (given L(1) = L′(1) = 0) | `A2_FORMULA.md`; re-derived by the referee (item 1), no factor-2 slip |
| **L″(E,1)/2** | **35.9353137531543022480 ± 3.008·10⁻¹⁵** (relative 8.4·10⁻¹⁷). Certified interval [35.93531375315429924, 35.93531375315430526]. **15 significant digits: 35.9353137531543** (AUDIT_A C2 corrects the lane's "16") | **CERTIFIED_NUMERIC** | Run B: PARI a_q, T = 5.5·10⁸, 7 workers, checkpointed; tail 3.1·10⁻¹⁸, fp+kernel 3.005·10⁻¹⁵. Run 1 (certified BSGS counter, T = 4.5·10⁸) agrees to 5.8·10⁻¹⁹ on the common range |
| **analytic rank = 2 exactly** | — | **CERTIFIED_NUMERIC** (AUDIT_A C1 replaces the lane's compound "PROVED, given … CERTIFIED_NUMERIC"). Evenness and ord ≥ 2 are PROVED; the interval above excludes 0 | A1 + run B |
| end-to-end checks from the same pass | L(E,1) = −1.6·10⁻¹⁹ ± 6.5·10⁻¹⁵; Φ(1.1) + Φ(1/1.1) = −5.4·10⁻¹⁹ ± 1.6·10⁻¹³ | CERTIFIED_NUMERIC | Both intervals contain 0. The Φ-check also excludes w = −1 by about 20 orders of magnitude (AUDIT_A item 15) |

**Trust base of the certified value** (AUDIT_A; it must travel with the label):
- theorems:
  - Deligne |aₙ| ≤ d(n)√n;
  - Berkane–Bordellès–Ramaré 2012, |Δ(x)| ≤ 0.961√x. It is cited from memory and checked empirically to be sharp at x = 12. The tail is 10³ below the fp term, so the result is insensitive to this constant;
  - modularity and the functional equation;
- software:
  - PARI 2.17.3/2.17.4 `ellap`/`Fl_elltrace`;
  - PARI's 80-digit G₂ values, independently confirmed by mpmath at 102 points and 32 per-node bounds;
  - Apple clang with `-ffp-contract=off` and x87 64-bit round-to-nearest.

**Referee reproduction.**
- The referee re-derived the certified value from the checkpoint logs: all 1665 blocks, FNV checksums, exact tiling, and the fp and tail budgets.
- The run-B binary is byte-identical to a rebuild from the present source, once the random LC_UUID is masked.
- An independent end-to-end run on 563a1 falls inside its certified bound.

## 2. Arithmetic invariants (lane B; AUDIT_B PASS_WITH_CORRECTIONS, BLOCKING #1 resolved, AUDIT_B_R2 PASS_WITH_CORRECTIONS)

| invariant | value | label | evidence |
|---|---|---|---|
| model | global minimal, u = 1. Δ = 2⁸·3²·2243·4547³·5843² > 0 (two real components); ω = dx/(2y) | PROVED | B.1; re-derived by hand (AUDIT_B, AUDIT_C item 4) |
| torsion | E(Q)_tors = Z/2 = ⟨T⟩ | PROVED | B.2; referee point counts |
| Tamagawa | c₂ = 2 (I₁*), c₃ = 2 (I₂ non-split), c₂₂₄₃ = 1 (I₁ split), c₄₅₄₇ = 2 (III), c₅₈₄₃ = 2 (I₂ non-split); **∏ = 16** | PROVED | c₂ by three routes, including the referee's 2-adic point count, calibrated on 16 curves |
| rank | 2 | PROVED | 2-descent upper bound (mwrank, PARI `ellrank`); Reg ≠ 0 certified; also Zywina Thm 1.2 |
| **generators, saturation** | **E(Q) = ⟨T⟩ × ⟨P₁, P₂⟩, index exactly 1** | PROVED | **(a)** eclib saturation: index bound 2, 2-saturation proved, "full Mordell–Weil basis determined unconditionally". **(b)** Silverman 1990 bound B = 20.329 (the maximum of all published forms), complete ratpoints enumeration of the 16 quartic covers to naive height 22.829, λ = min ĥ = ĥ(P₁+P₂) = 4.12847755086578674699…, and Hermite: index ≤ (2/√3)·√Reg/λ = 1.948 < 2. Route (b) holds after the AUDIT_B #1 fix. Also E(Q)/pE(Q) = ⟨P₁,P₂⟩ by two-prime certificates for every odd p ≤ 100 (lane D; referee re-derived p = 3, 7, 13, 17) |
| **Ω_E** = 2ω₁ | 0.05608980303887280889661880361586076834227009573 | CERTIFIED_NUMERIC | Arb AGM enclosure, radius < 10⁻¹⁰⁰⁰; referee by AGM and by quadrature to 60 digits |
| **Reg(E)** (ĥ ≈ h(x) normalization) | 17.79651747249034029917494121943603841630497246 | CERTIFIED_NUMERIC | Tate series with a rigorous tail, radius 4.4·10⁻⁶⁵. The referee reproduced it with an independent Tate series and fixed the normalization by the doubling limit |
| **C := Ω·Reg·∏c_p/#tors²** | **3.99281263923936691806855200220915394735533662** | CERTIFIED_NUMERIC | radius 10⁻⁶⁵. Calibrated: 389a1, 1088j1 and 1088j2 reproduce Cremona to 29 digits |
| **Sha(E/Q)[2^∞]** | **0** | PROVED | dim Sel^ψ = dim Sel^ψ̂ = 2 and dim Sel₂ = 3 = 2 + 1; three descent implementations; also Zywina |
| E′ = E/⟨T⟩ | [0, 45470, 0, 91790289, 0], global minimal, ψ*ω′ = ω; c′ = (2, 2, 2, 2, 1), ∏ = 16; E′(Q) = ⟨T′⟩ × ⟨R′ = (−2243, −107664), ψP₁⟩ | PROVED | B.7, Kummer map + #Sel^ψ = 4 |
| **Sha(E′/Q)[2^∞]** | **0** | PROVED | B.5 |
| Ω′, Reg′, C′ | Ω′ = Ω, Reg′ = Reg, **C′/C = 1 exactly** | PROVED | Ω′/Ω ∈ {1/2, 1}; the ball selects 1, and so does a topological argument (T lies on the egg) |
| Sha(E) ≅ Sha(E′) | as groups | PROVED | ψ is an isomorphism on odd-primary parts; both 2-parts are 0 |

**Saturation certificate: what was repaired.**
- **The defect.** As first delivered, route (b) capped the *denominator* range of `hyperellratpoints` at Mmax for the 8 quartics with |s| > 7579. So the completeness of that route was not established by the lane's own artifacts (AUDIT_B #1, BLOCKING).
- **The fix.** The cap was removed and all dependent scripts were rerun. The only change: s = +AB gains X = ±48/4115 and ±96/6275, with h_r = 24.93 and 24.70, both above H. The enumerated set, λ ≥ 2.5, n ≤ 1.948 and index 1 are unchanged.
- **Re-audit.** AUDIT_B_R2 reran the enumeration twice, including once with a call that satisfies PARI's documented contract (D ≤ N). It found the identical set, and marked #1 RESOLVED.
- Route (a) (eclib) was never affected.

## 3. Sha_an and what BSD predicts

**Definition.** Sha_an := (L″(E,1)/2)/C, with A's certified L″/2 and B's certified C.

**Value.** Sha_an = **8.99999999999999999634**, |error| ≤ **7.54·10⁻¹⁶**. The interval is [8.999999999999999243, 9.000000000000000750].
- **Label: NUMERIC.**
- The enclosure follows by interval arithmetic from two CERTIFIED_NUMERIC inputs and their trust bases (propagated error = δL/C + L·δC/C², dominated by lane A's 3.008·10⁻¹⁵).
- No theorem gives Sha_an an arithmetic meaning.
- **9 lies inside the interval.** 9 − Sha_an = 3.7·10⁻¹⁸, which is 200 times smaller than the error bound.
- Script and output: `audits/synth_sha_an.py`, `audits/synth_sha_an.out` (Python `decimal`, 60 digits). AUDIT_B and AUDIT_C recomputed the same ratio independently (8.99999999999999999634).

**Robustness.**
- Nothing was tuned toward 9. A's planning estimate assumed Sha = 1 (L″/2 ≈ 4), and the timestamps show the ratio was computed after the certified value (AUDIT_A items 10, 15).
- Each single normalization slip would have moved the ratio: Ω halved → 18; #tors² = 16 → 36; ĥ halved → 36; c₂ = 4 → 4.5. AUDIT_B excluded each one by an independent computation of that invariant.

**BSD prediction. This is a prediction, not a theorem.** CONDITIONAL(BSD for E):
- **#Sha(E/Q) = 9**;
- **Sha(E/Q)[3^∞] ≅ (Z/3)²**;
- **Sha(E/Q)[p^∞] = 0 for every p ≠ 3**.

Why the 3-part must be (Z/3)²: on a finite Sha[3^∞] the Cassels–Tate pairing is non-degenerate and alternating, so Sha[3^∞] ≅ A × A. Order 9 then forces A = Z/3.

The prediction is consistent with the proved Sha[2^∞] = Sha[5^∞] = 0, since 9 is prime to 10.

**Check on E′.**
- L(E′,s) = L(E,s), and C′ = C exactly (§2). So Sha_an(E′) = Sha_an(E) = 9 (NUMERIC), and BSD for E′ predicts #Sha(E′) = 9.
- This agrees with the PROVED isomorphism Sha(E) ≅ Sha(E′). Together with C′/C = 1 it is consistent with Cassels' isogeny invariance of the BSD quotient.

**Cross-lane 5-adic consistency (NUMERIC; it uses p-adic BSD only as a heuristic, which is not proved).**
- Lane 2 (bsm-28, V_B F8; recorded in `coord.json`, not audited here) observes a₂^SW ≡ 1 (mod 5), with canonical Reg_γ ≡ 21 (mod 25).
- p-adic BSD would predict a₂^SW ≡ 4·#Sha (mod 5), so the observation gives #Sha ≡ 4 (mod 5). Sha_an = 9 ≡ 4 (mod 5): the complex and 5-adic sides agree.

## 4. Distance to full BSD (one table)

BSD for E asserts three things: (i) rank = r_an; (ii) Sha is finite; (iii) L″(E,1)/2 = Ω·Reg·∏c_p·#Sha/#tors² = C·#Sha.

| item | status label | source / evidence | next action, cost |
|---|---|---|---|
| rank E(Q) = 2 | **PROVED** | Zywina Thm 1.2; lane B 2-descent + certified Reg ≠ 0 | none |
| r_an = rank (= 2) | **CERTIFIED_NUMERIC** | ord even and ≥ 2 PROVED (A1). The certified L″/2 interval excludes 0 (AUDIT_A C1 label) | none. A PROVED label would need the computation itself formally verified (lane 4's remit) |
| leading-coefficient value L″(E,1)/2 | **CERTIFIED_NUMERIC**: 35.9353137531543022480 ± 3.008·10⁻¹⁵ (15 significant digits) | §1; run B, cross-checked by run 1 | none |
| rationality of L″(E,1)/(Ω·Reg) | **OUT_OF_REACH**(a number-field Gross–Zagier-type formula for the second central derivative, giving rationality with an explicit denominator) | Not known for any curve over Q with r ≥ 2. The only higher-derivative formula (Yun–Zhang 2017) is over function fields (C2 (b); AUDIT_C item 9) | none; not a computation |
| Sha[2^∞] (E and E′) | **PROVED = 0** | Zywina Lemmas 3.1–3.3; lane B (three descent codes) | none |
| **Sha[3^∞]** (BSD predicts order 9, ≅ (Z/3)²) | **UNKNOWN** (feasible finite computation; not run) | Non-split multiplicative 3; ρ̄₃ = GL₂(F₃); E(Q)/3E(Q) = ⟨P₁,P₂⟩ certified; ord₃ Reg_γ = 0 (PARI only) | **Upper and exact route:** the depth-4 L₃ run (a₂ mod 27, unitary cusps b/81). It decides ord₃ #Sha[3^∞] = ord₃ a₂. The result is CONDITIONAL(Skinner Thm A identifications (1)–(3); ord₃ Reg_γ = 0 under PARI's normalization at non-split 3), plus the Manin qualifier. Cost: Phase A + Tier 1′ ≈ 14 CPU-h (shared with p = 7). **Lower-bound route:** four independent 3-Selmer classes would give dim Sha[3] ≥ 2 unconditionally. The implication is PROVED, but no classes are computed; it needs new code (no Magma), cost UNKNOWN. Fisher–Newton Cassels–Tate pairing: expensive, UNKNOWN |
| Sha[5^∞] | **PROVED = 0, via the derived v₂(c₀) ≤ 8 lemma** | Kato + SW Thm 6.1; gates reviewer-accepted, operator merge of SHA5 pending | none |
| good ordinary p ≥ 7 (every odd p ∤ N with a_p ≢ 0 (mod p); BSD predicts 0) | **UNKNOWN** per p | SU 2014 Thm 1 / Thm 3.6.9 (q = 2243) gives the IMC at every such p, so the SW computation is exact. The cheap gates pass for every ordinary p ≤ 97. p = 17 needs depth 3 (ord₁₇ Reg_γ = 1) | One shared pass (Phase A ≈ 2 CPU-h on top): {3, 7} ≈ 12 CPU-h; {3, 7, 11, 13} ≈ 54; + 19: ≈ 132; all odd p ≤ 97 except 23 and 29: ≈ 7 170 CPU-h (NUMERIC model). For p > 100 the cost is ≈ 5p²√N terms, growing like p^{2.3} (2·10⁴ CPU-h at p ≈ 150) |
| supersingular p (23, 29, 131, 167, …; 54 below 10⁵) | **UNKNOWN** | Kato + Perrin-Riou/Kobayashi give upper bounds only. The printed supersingular main conjectures **do not apply**: BSTW 2409.01350 needs E semistable; CLW and Castella–Sano Thm B need N squarefree. This says the printed results do not apply, not that the route is impossible | 23 and 29: NOT_WITH_THIS_METHOD at authorizable cost (depth 5–6, 10⁷–10⁹ CPU-h; NUMERIC model, not an impossibility claim). Whether a ± leading-term theorem helps is UNKNOWN (O-8) |
| bad p = 2243 (split multiplicative, exceptional zero) | **UNKNOWN** | IMC for L_f by Skinner 2016 Thm A with q = 5843 or 3 (identification with L_p(E,T) as at p = 3); Kobayashi divisibility; Jones's split case | infeasible with present code: cusps b/2243² need ≈ 4·10¹³ terms, ≈ 2·10⁴ CPU-h |
| bad p = 5843 (non-split multiplicative) | **UNKNOWN** | IMC for L_f by Skinner Thm A with q = 2243 (identification as at p = 3) | infeasible: ≈ 1.6·10¹⁴ terms, ≈ 10⁵ CPU-h |
| bad p = 4547 (additive, III) | **UNKNOWN** | No cyclotomic p-adic L-function in SW's framework. Kim 2203.12159 Thm 1.8 applies (a Kurihara witness would prove Sha[4547^∞] = 0), but a witness is not guaranteed to exist: the IMC at additive 4547 is not known | semi-decision only; prohibitive (ℓ ≡ 1 mod 4547) |
| all large p at once ("Sha[p^∞] = 0 for almost all p") | **OUT_OF_REACH**, needing any one of: (H1) a number-field higher-derivative Gross–Zagier/Kolyvagin theorem giving one global class that controls almost all p; (H2) a uniform-in-p Kolyvagin conjecture with an effective exceptional set; (H3) BKS 2024 Conj. 1.1 for r = 2 at almost all p | Open for every rank-2 curve over Q (Banwait 2609.08431 says so in print). Every known method is per p: Heegner points are torsion here, Kurihara n depends on p, and L_p depends on p (C3 §7) | none; this is a theorem, not a computation |
| finiteness of Sha | **OUT_OF_REACH**(the horizontal theorem above with an explicit bound M, plus the finitely many p ≤ M) | Known for no E/Q with r_an ≥ 2. No refereed theorem. One unrefereed preprint (Nguyen, arXiv 1309.7675, 2013) claims it for every E/Q; it is not assessed here (AUDIT_C correction 8) | none |
| exact leading-term equality L″(E,1)/2 = 4·Ω·Reg·#Sha (BSD-c) | **OUT_OF_REACH**(finiteness of Sha with the exact #Sha, **and** rationality with an explicit denominator) | Numerics give 9 ± 7.5·10⁻¹⁶ (§3, NUMERIC). Without a denominator bound no amount of precision proves the identity. The "3-part of BSD" as an identity involving L″ is OUT_OF_REACH for the same reason, even if #Sha[3^∞] = 9 is proved | none |

**Reading the table.**
- Done: rank, r_an (certified), the leading-coefficient value, Sha[2^∞], Sha[5^∞].
- Sha[3^∞] is the only open row that BSD predicts is non-zero, and it is feasible.
- The good-ordinary rows can be closed one prime at a time, but only finitely many of them.
- Supersingular and bad primes are open with no feasible route at present.
- The four OUT_OF_REACH rows are the well-known open problems for rank ≥ 2. Nothing here is special to the seed.

## 5. Per-prime closure plan (lane D). **Nothing has been launched.**

The request is **`D_primes/AUTHORIZATION_REQUEST.md`**, with supporting files `01_GATES.md`, `02_IDENTIFICATION.md`, `03_COST.md`, `04_P3.md` and `05_SUPERSINGULAR.md` in the same directory. It is an operator decision. AUDIT_D and AUDIT_D_R2 found the chain, weights, truncations, cost model and checkpoint design sound once the p = 3 chain was repaired.

**Method.** This is the method that closed p = 5: Stein–Wuthrich + Kato (SW Thm 6.1; Alg. 11.1 step 4), fed by certified streamed modular symbols [b/p^k]⁺.
- One shared streaming pass costs about what its largest target costs. Separate passes would cost up to 6× more.
- Depth 2 suffices at the 19 ordinary primes ≤ 97 with a unit Reg_γ (7, 11, 13, 19, 31, …, 97; 01_GATES §3). p = 17 needs depth 3.

| option | buys (if every test comes out as BSD predicts) | CPU-h (NUMERIC model) | wall, 12 workers, **idle** host |
|---|---|---|---|
| Phase A only | the driver built and validated (A0–A5, including a kill-and-restart drill and bit-identical reduction); no seed claim | ≤ 2 | ≤ 1 h |
| **Phase A + Tier 1′** | **#Sha[3^∞] decided (= 9, ≅ (Z/3)², CONDITIONAL; see below)**; Sha[7^∞] = 0 | **≈ 14** | ≈ 1.5 h |
| Phase A + Tier 2′ (**lane D's recommendation**) | Tier 1′ + Sha[11^∞] = Sha[13^∞] = 0 | ≈ 56 | ≈ 6 h |
| Phase A + Tier 3 | + Sha[19^∞] = 0; the forced check 17 ∣ a_{2,2} | ≈ 134 | ≈ 13 h |
| Phase A + Tiers 4 / 5 / 6 | + p = 31…47 / + 53…71 and 17 at depth 3 / + 73…97 | ≈ 1 200 / 3 310 / 7 170 | ≈ 5 / 14 / 30 days |

- The coordinator's notes (`coord.json`) propose the narrower **Phase A + {3, 7} (≈ 14 CPU-h)**.
- Wall time on the shared host is UNKNOWN. It is not modelled and will be measured in Phase A5 (AUDIT_D correction 7).
- Every run is append-only and segment-checkpointed, launched with nohup, with watchdog stop rules (load1 > 30, swap growth, disk floor, any counter mismatch). AUDIT_D [14] found the design compliant with the CHECKPOINT POLICY.

### The p = 3 plan (highlighted: the only prime where BSD predicts non-trivial Sha)

**Theorem chain (as repaired after AUDIT_D #1).**
- **Why Kato is replaced.** Kato Thm 17.4 excludes 3 ∣ N (Skinner 1407.1093 p. 2). SW's Thm 7.3 cites no source for the non-split case.
- **What replaces it.** The divisibility input is **Skinner 2016 Thm A**. It gives both divisibilities (Ch = (L_f) in Λ) and a torsion Selmer dual.
- **Hypotheses of Thm A**, discharged from merged facts and re-verified by AUDIT_D_R2 [1]:
  - p = 3, k = 2, a₃ = −1 a unit;
  - ρ̄₃ = GL₂(F₃), which is irreducible;
  - q = 2243 ∥ N, and v₂₂₄₃(Δ) = 1, so E[3] is ramified at 2243.
- **Remaining inputs:**
  - SW Thm 6.1, Jones's multiplicative case;
  - ε₃ = 2, ∏c = 16 and #tors = 2, all 3-units;
  - ord₃ Reg_γ = 0 (PARI only);
  - symbols in (1/1024)Z, since c_E ∣ 512, so c = 0 in SW Prop. 3.5.

**Computation.**
- Target: a_{4,2} ≡ a₂ (mod 27), from the unitary cusps b/81 (width N/3) via W_{N/3}.
- The sign −w·a₃ = +1 was validated against eclib on 6 curves to ≤ 6·10⁻¹⁷; the opposite sign fails by ≥ 0.56. Lanes C and D agree on the sign (AUDIT_C item 11).
- T = 1.73·10¹⁰ at error 2.5·10⁻⁶. At ≈ 0 marginal cost this sits inside Tier 1′.
- Depth-4 weights were validated against Sage `padic_lseries(3)` on 681c1, 681b1 (Sha = 9), 57a1 and 33a1.

**Outcomes.**
- **ord₃ a_{4,2} = 2** ⇒ ord_T L₃ = 2, Sha[3^∞] is finite, **#Sha[3^∞] = 9 and Sha[3^∞] ≅ (Z/3)²**.
- ord₃ a_{4,2} = 0 ⇒ Sha[3^∞] = 0. This contradicts the BSD prediction: **stop and audit**.
- ord₃ a_{4,2} = 1 is impossible under the chain, because a finite Sha[3^∞] has square order: **stop and audit**.
- a_{4,2} ≡ 0 (mod 27) ⇒ #Sha[3^∞] ≥ 81 or infinite: **stop and audit**.

**Built-in theorem-forced checks.**
- [1/3]⁺ = 0;
- a_{4,0} = 0 and a_{4,1} ≡ 0 (mod 27);
- the Hecke relations;
- T₁ and T₂ give identical integer vectors;
- lattice membership.

Per AUDIT_D_R2 #1, a *uniform* rescaling of all symbols is caught only by lattice membership, and only up to 3-adic units. That cannot change ord₃ a₂.

**Label of the outcome, carried here: CONDITIONAL**, via the derived v₂(c₀) ≤ 8 lemma. The conditions are:
- the Skinner Thm A identifications:
  1. Greenberg Selmer = classical Selmer at multiplicative 3;
  2. L_f = L₃(E,T) up to a Λ-unit;
  3. T_f = T₃E;
- ord₃ Reg_γ = 0 under PARI's normalization at non-split 3.

**Open reconciliation (operator), not a blocking dispute.**
- AUDIT_C (item 6) finds identifications (1) and (2) sourced: SU §3.6.7 p. 45; SU Thm 3.6.9; Skinner Thm C with the Néron period at p ∣ N; 3 ∤ c_E. It calls the criterion PROVED.
- AUDIT_D_R2 [1] re-derived (3), lattice uniqueness up to homothety, as correct.
- AUDIT_D and AUDIT_D_R2 keep the label CONDITIONAL until the coordinator accepts.
- Under the "never upgrade" rule this report keeps the lower label.
- If the operator accepts AUDIT_C item 6 and AUDIT_D_R2 [1], the label reduces to **CONDITIONAL(ord₃ Reg_γ = 0 under PARI's normalization at non-split 3)** plus the Manin qualifier.

**Cheap pre-step (not in the request; lane C's C5 (a) item 4, cost: seconds).**
- Check PARI's `ellpadicregulator` normalization at a non-split multiplicative prime against SW §4 on a known curve.
- Sage's `padic_height` does not support multiplicative p, so PARI is the only implementation at 3 (D O-4).
- PARI takes the Tate-curve E₂ path (`ellpadics2_tate`) there, so only the normalization constant is unchecked (AUDIT_C item 7).

**Fallbacks (not requested).**
- Explicit 3-descent: given finiteness, one class outside the Kummer image suffices for ≥ 9; otherwise two independent classes give #Sha[3] ≥ 9.
- Visibility.
- Both give lower bounds only.

## 6. Audit trail

The audits were hostile, fresh-context and read-only, with CPU caps. No `REBUTTAL.md` exists anywhere in the tree: every correction was accepted. The critic stage runs after this report; `audits/CRITIC.md` did not exist when this report was written.

| lane | audit (file, finished) | BLOCKING | repair | re-audit | what this report does with the non-blocking items |
|---|---|---|---|---|---|
| A | `AUDIT_A.md`, 23:07Z: **PASS_WITH_CORRECTIONS** | none | none (no blocking) | — | **Applies** C1: the analytic-rank label becomes CERTIFIED_NUMERIC. **Applies** C2: 15 significant digits, not 16. C3 (coverage wording of validation rows (b)), C4 (BBR/Kato/Monsky/Rohrlich/Carayol cited from memory; no local text) and C5 (the run-1 binary is not retained; custody by hash only) are documentation items, still open in the lane files |
| B | `AUDIT_B.md`, 23:09Z: **PASS_WITH_CORRECTIONS** | #1: the route-(b) enumeration box truncated denominators for 8 quartics | 23:10–23:18Z: all 5 corrections applied (fix, reruns, λ re-attained with B = 20.329, dead artefact marked, wording) | `AUDIT_B_R2.md`, 23:29Z: **PASS_WITH_CORRECTIONS**; #1 **RESOLVED** | New non-blocking item: the repaired call `hyperellratpoints(Q,[Mmax,emax])` has D > N, outside PARI's documented contract. The substance was verified from `ratpoints.c` and by a contract-compliant rerun giving the identical set. Still pending: a one-line fix or one sentence in 04 §4.2. Nit: one mtime claim in caveat 2 is no longer checkable |
| C | `AUDIT_C.md`, 23:12Z: **PASS_WITH_CORRECTIONS** (13 items) | none | none (no blocking) | — | **Applies** #1 (5-adic identity written with #Sha[5^∞]), #3 (per-row wording in §4), #5 (supersingular IMC in rule-3 form), #6 in its stricter form (the criterion and its evaluation are both carried CONDITIONAL, following AUDIT_D; §5), #7 (final L″/2 and ratio), #8 (Nguyen qualifier), #11 (sign question closed), #12 (r_an now certified). #2 (replace "SU §3.4 not read" with SU §3.6.7/3.6.9 and Skinner Thm C), #4 (unitary-cusp wording), #9 (4547 surjectivity wording), #10 (reduced-model regulator rerun) and #13 (self-contained lifting in the ρ₃ lemma) are still open in the lane files |
| D | `AUDIT_D.md`, 23:05Z: **PASS_WITH_CORRECTIONS** (8 items) | #1: the p = 3 chain cited SW 7.3/Kato 17.4, which do not cover 3 ∣ N | ≈ 23:11–23:20Z: all 8 applied, text only (Skinner Thm A chain, single CONDITIONAL label, C11 asymmetry withdrawn, O-3 upgraded) | `AUDIT_D_R2.md`, 23:31Z: **PASS_WITH_CORRECTIONS**; #1 **RESOLVED** | **Applies** R2 #2: C11 is stated in rule-3 form, "the printed Kato 17.4 / SW 7.3 statement does not apply at 3 ∣ N; not an impossibility claim", not "PROVED (source reading)". R2 #1 (drop "or lattice scaling" in 04_P3 §4) is reflected in §5. Still open in the lane files: R2 #1, R2 #3 (mark `audit_repair/p3_new_sections.md` SUPERSEDED) and the R2 #4 nits |

**Corrected and resolved.**
- B #1 and D #1, the only BLOCKING items, were resolved on re-audit.
- The C-versus-D Atkin–Lehner sign question in `coord.json` is closed. ε_{N/3} = w·a₃ = −1, and Wuthrich's (8) uses −ε_Q = +1 = D's "−w·a₃" (AUDIT_C item 11; AUDIT_D [2]).
- O-1 (the C_frontier/STATE.json clobber) is resolved, subject to the coordinator's confirmation.

**Still disputed.** No claim is left under an unresolved BLOCKING correction, so nothing is downgraded or marked DISPUTED. One cross-audit label question remains open for the operator: the p = 3 identifications. AUDIT_C calls them sourced; AUDIT_D and AUDIT_D_R2 keep CONDITIONAL. This report carries CONDITIONAL (§5).

**Audit continuity.** Audit batches 1 and 2 died at the session usage limit (≈ 18:36Z) with partial files on disk. Batch 3 resumed at ≈ 22:52Z: the successor referees kept their predecessors' items verbatim and marked the resume point in each file.

### Coordination incident (duplicate instances, 18:01–18:10Z)

**What happened.**
- At about 18:00Z the coordinator delivered the mid-run CHECKPOINT POLICY by SendMessage to the four running workflow agents.
- Each reply said "Resuming agent": the message had **forked a second live copy** of every lane agent. For about 18:01–18:10Z two writers worked in each lane directory.
- At 18:07Z the coordinator stopped workflow `wzmlp0edp`, which killed the originals. The four forks (same ids) continued as standalone subagents and were told to reconcile the dead copies' files.

**How each lane was reconciled, and what the audit verified.**

| lane | what the other instance wrote | reconciliation | audit verification |
|---|---|---|---|
| A | `A3_IMPLEMENTATION.md`, `runs/seed_eval*`, `NOTE_FROM_ORIGINAL_INSTANCE.md`. Run 2 (not checkpointed) was killed at 18:02:17Z; the log mislabels it "run1_fast_W8 KILLED" | Checked and kept; same numbers | AUDIT_A item 9: the final value depends only on pre-fork files and the survivor's files |
| B | B.7 (`s07_bsd_const*`); `rig_lib.sage` carries edits from both | The author reran B.7: byte-identical | AUDIT_B A1, B3: s06 and s07 outputs reproduced byte-for-byte from the reconciled tree |
| C | C2, `SOURCES.md`, QUERY_LOG rows 5–22 | Read in full and kept; items read only by that instance are flagged | AUDIT_C item 5: 29/29 artifact hashes match. No PROVED label depends on an item read only by the parallel instance; three were spot-checked at source |
| D | `src/weights*`, `validation_formula/*`, `cost/separate_vs_shared*`, part of `02_IDENTIFICATION.md` (18:00–18:06Z) | Weights re-run: byte-identical; numbers verified | AUDIT_D [6], [12]: 111/111 artifact hashes match; weights byte-identical on a second rerun |

**Knock-on incident.**
- At 18:09:59Z lane D ran the shared-scratchpad `mkstate.py` (lane C's) and overwrote `C_frontier/STATE.json` with lane-D content.
- Lane C regenerated it from its own state by 18:25:15Z.
- Both state writers now live inside their lane directories and assert their root.
- AUDIT_D_R2 [7] found no cross-lane side effect from D's repair.

**Rule adopted.** Never SendMessage a running workflow agent by id. A reply of "Resuming agent" means a fork.

## 7. Side findings (not part of the seed's BSD map)

| # | finding | label | evidence |
|---|---|---|---|
| S1 | **Destrempes–Malinin, arXiv 1703.02215, Thm 5** ("Sha(E/Q)[ℓ] = 0 for ℓ ∉ {2,3,5,7,13} when ρ_ℓ = GL₂(Z_ℓ) and ℓ ∤ 4A³+27B², any rank, non-CM") **is false as printed.** Counterexample: 20806a1 at ℓ = 11. It is non-CM, ρ₁₁ = GL₂(Z₁₁), 11 ∤ 6Δ_min, and #Sha[11^∞] = 11² by SU Thm 2(a) with Cremona's exact L(E,1)/Ω = 242. Second witness: 8350c1. Where the paper goes wrong was not located | PROVED | C2 (c), `C_frontier/runs/dm_counterexample*`; AUDIT_C item 8 re-checked every hypothesis |
| S2 | SW 2013 Thm 7.3 is printed for "semistable at p", but its attribution covers only good ordinary p (Kato 17.4) and split multiplicative p (Kobayashi). Skinner 1407.1093 p. 2 states that p ∣ N is excluded from Kato 17.4. So the non-split multiplicative case has no cited source in SW. This is a statement about printed sources, **not** a claim that the divisibility is false | source reading (rule-3 form; no label) | SW l.1192–1199, 1300–1302; Skinner local text l.59–64; AUDIT_D [7], AUDIT_D_R2 [5] |
| S3 | ρ₃(G_Q) = GL₂(Z₃) for the seed. Proof: the Tate curve at 2243 gives a unipotent of order 9 mod 9; its conjugates span sl₂(F₃); a det/abelianization argument; then lifting via (1+3X+9Y)³ ≡ 1+9X (mod 27). The p = 3 chain no longer needs it (Skinner footnote 1) | PROVED (derived lemma) | C3 §2.2, D `gates/step1d`; re-derived independently by AUDIT_C item 3 and AUDIT_D [3] |
| S4 | PARI p-adic heights. (a) Lane-2 finding (in `coord.json`; not audited here): on a non-reduced model, `ellpadicheight`/`ellpadicregulator` is off by 2·⌊b₂/12⌋·log(P)². ord_p Reg is immune: on the reduced model the AUDIT_C rerun gives ord₃ = ord₇ = 2, as before. (b) On the seed, PARI and Sage `padic_height` agree in valuation (ord₇ = 2, ord₁₇ = 3) but differ in the unit part (ratio ≡ 9 mod 17). Whether (b) is caused by (a) was not checked. (c) At non-split p PARI takes the `ellpadics2_tate` path | (a) NUMERIC (not audited); (b) CERTIFIED_NUMERIC valuations, unit parts NUMERIC; (c) source reading | AUDIT_C item 7; AUDIT_D [9], [13]; `coord_checks/padic_reg_sage.out` |
| S5 | PARI documents `hyperellratpoints(Q,[N,D])` only for D ≤ N. The implementation (`src/modules/ratpoints.c`: `args_h`, `find_points_work`, `sift`) is complete for D > N as well | source reading + reproduction | AUDIT_B_R2 [R2-2] |
| S6 | The certified functional-equation check Φ(1.1) + Φ(1/1.1) = −5.4·10⁻¹⁹ ± 1.6·10⁻¹³ is a third determination of w = +1. It is independent of the local root-number table and of Monsky | CERTIFIED_NUMERIC | AUDIT_A item 15 |

Nothing in S1–S6 has been communicated outside this tree.

## 8. Resources

**CPU used, against caps.**

| agent | CPU used | cap | notes |
|---|---|---|---|
| lane A | ≈ 2 765 s ≈ 0.77 CPU-h | 2 CPU-h, 8 threads | run B 1 714 s, run 1 606 s, killed run 2 ≈ 224 s, tests and validation ≈ 220 s; ≤ 8 workers; peak RSS < 0.3 GB in total |
| lane B | ≈ 567.5 s ≈ 9.5 CPU-min, including a 178.9 s repair | 30 CPU-min | RSS ≤ 0.3 GB; ≤ 2 heavy processes |
| lane C | ≈ 4.3 CPU-min | 5 CPU-min | two slow group-check runs hit their 120 s timeouts |
| lane D | ≈ 1.8 CPU-min, plus < 5 s for the repair | 10 CPU-min pilot | max RSS 233 MB; single thread |
| audits | A ≈ 23 s; B ≈ 26 s; B_R2 ≈ 42 s; C ≈ 4 s; D ≈ 6.3 s; D_R2 ≈ 0.1 s | 10 CPU-min each (R2: 5) | one process at a time, nice 15 |
| synthesis | < 1 CPU-s (one Python ratio script, `shasum`) | — | — |
| **total** | **≈ 1.06 CPU-h** | | |

**Run conditions.**
- Everything ran at `nice -n 15` under `timeout`. Host load1 was about 6–10 during the lane work and 6.0 at 23:37Z, never above 30.

**Wall-clock timeline (UTC).**

| time | event |
|---|---|
| ≈ 17:38Z | workflow launched |
| 18:01–18:10Z | duplicate-instance window |
| ≈ 18:16–18:25Z | lane work complete (author level) |
| 18:24–18:36Z | audits start |
| ≈ 18:36–22:52Z | stop at the session usage limit |
| 23:05–23:12Z | audits complete |
| 23:10–23:21Z | repairs |
| 23:29Z, 23:31Z | re-audits complete |
| 23:32Z | synthesis starts |

**Output discipline.**
- No production streaming job was run after lane A's two seed runs. L₅ was not rerun.
- Nothing was published or hosted.

## 9. Proposed ledger block (NOT merged; awaiting operator acceptance)

```
SEED_2243_12_FULL_BSD_LANE3 — BSD_DISTANCE_MAPPED  (lanes A-D; audits A, B, C, D PASS_WITH_CORRECTIONS;
  the only BLOCKING items, B#1 and D#1, RESOLVED on re-audit B_R2 / D_R2; no REBUTTAL)
  E: y^2 = x^3 - 22735x^2 + 106272484x, N = 2^3*3*2243*4547^2*5843, w = +1 (local product; Monsky; certified Phi-check).
  ANALYTIC: ord_{s=1} L(E,s) even and >= 2 PROVED (Kato 2004 Thm 14.2 + w = +1).
    L''(E,1)/2 = 35.9353137531543022480 +- 3.008e-15 CERTIFIED_NUMERIC (G_2 streaming, PARI a_q, T = 5.5e8, checkpointed;
    independent run 1 agrees to 5.8e-19; 15 significant digits). r_an = 2 CERTIFIED_NUMERIC (AUDIT_A C1).
  INVARIANTS: E(Q) = <T> x <P1,P2>, P1 = (4547,327384), P2 = (5184,281520), index 1 PROVED (eclib saturation; Silverman
    B = 20.329 + ratpoints to h = 22.829 + Hermite, n <= 1.948, after AUDIT_B #1 fix). tors Z/2. prod c_p = 16 PROVED.
    Omega = 0.05608980303887280889661880361586..., Reg = 17.79651747249034029917494121943..., C = Omega*Reg*16/4 =
    3.99281263923936691806855200220915... CERTIFIED_NUMERIC. Sha[2^inf] = 0 for E and E' = E/<T> PROVED.
    E': C'/C = 1 and Sha(E) ~= Sha(E') PROVED.
  SHA_AN := (L''(E,1)/2)/C = 8.99999999999999999634 +- 7.54e-16 (NUMERIC). BSD PREDICTION (CONDITIONAL(BSD); not a
    theorem): #Sha = 9, Sha[3^inf] ~= (Z/3)^2 (square order by Cassels-Tate), Sha[p^inf] = 0 for p != 3; same for E'.
  PER PRIME: Sha[2^inf] = 0 PROVED. Sha[5^inf] = 0 PROVED (via the derived v_2(c0) <= 8 lemma;
      reviewer-accepted, operator merge of SHA5 pending).
    Sha[3^inf] UNKNOWN: the depth-4 L_3 run (a_2 mod 27, unitary cusps b/81) decides ord_3 #Sha[3^inf] = ord_3 a_2,
      CONDITIONAL(Skinner 2016 Thm A identifications: Greenberg = classical Selmer at multiplicative 3; L_f = L_3(E,T) up to
      a Lambda-unit; T_f = T_3 E), via the derived lemma. [ord_3 Reg_gamma = 0 at nonsplit 3: PARI normalization calibrated at
      valuation level on 13 curves, section 10 C7 — no longer a separate condition.]
    good ordinary p >= 7: UNKNOWN per p, feasible (IMC by SU 2014, q = 2243). Supersingular 23, 29, ...: UNKNOWN,
      NOT_WITH_THIS_METHOD at authorizable cost (not an impossibility claim). 2243, 5843: UNKNOWN (infeasible cost);
      4547: UNKNOWN (Kurihara semi-decision only).
  OUT_OF_REACH: Sha[p^inf] = 0 for almost all p (needs H1 / H2 / H3); finiteness of Sha; rationality of
    L''(E,1)/(Omega*Reg); the exact leading-term identity. Not known for any E/Q with r_an >= 2.
  PLAN (NOT LAUNCHED): D_primes/AUTHORIZATION_REQUEST.md. Phase A (<= 2 CPU-h) + Tier 1' {3,7} ~ 14 CPU-h
    (coordinator) or Tier 2' {3,7,11,13} ~ 56 CPU-h (lane D). CPU-h NUMERIC (model); shared-host wall UNKNOWN.
  OPEN FOR THE OPERATOR: the p = 3 identifications label (AUDIT_C item 6: sourced; AUDIT_D / D_R2: keep CONDITIONAL);
    [PARI normalization check at nonsplit 3: DONE, section 10 C7]; non-blocking documentation items A C3-C5, B_R2 (contract sentence),
    C #2 #4 #9 #10 #13, D_R2 #1 #3 #4.
SIDE: DESTREMPES_MALININ_1703_02215_THM5 = FALSE_AS_PRINTED (counterexample 20806a1 at l = 11; second witness 8350c1;
  PROVED; AUDIT_C item 8).
```

## 10. Coordinator corrections after the completeness critic (2026-09-19; `audits/CRITIC.md`, 2 MUST_FIX + 12 GAP)

In-place edits (pre-edit copy: `state/00_REPORT.pre_critic_fixes.md`): §0 and §4 and §9 now say the SHA5 gate is
reviewer-accepted with the **operator merge pending** (critic 2); §5 says **19** ordinary primes (critic 1); §9 drops the PARI
condition at 3 per C7 below. Everything else is appended here; no label is upgraded.

| # | critic item | resolution |
|---|---|---|
| C3 | 5-adic cross-check normalization | The merged a₂(L₅) ≡ 2 (mod 5) is in the LP5 normalization, which is **2 × Wuthrich/SW** (`~/BSD_SW_LP5_STREAMING_2026-09-18/00_REPORT.md` l.60, l.145). So a₂^SW ≡ 2⁻¹·2 ≡ 3·2 ≡ 1 (mod 5). With ε₅ ≡ 1, ∏c/#tors² = 4 and lane 2's canonical Reg_γ ≡ 21 (mod 25), the (heuristic) p-adic BSD formula gives a₂^SW ≡ 4·#Sha; #Sha = 9 ⇒ 36 ≡ 1 ✓. The factor 2 is a 5-adic unit, so Sha[5^∞] = 0 is unaffected. NUMERIC consistency only. |
| C4 | root number, w₂ | Route (i)'s local factor w₂ = +1 (I₁*) comes from PARI's implementation of Halberstadt's 2-adic table and was not hand-checked (A1 l.14; AUDIT_A item 5). w = +1 is PROVED by route (ii) (Monsky 2-parity with rank 2 and Sha[2] = 0) and corroborated by the certified Φ-check. |
| C5 | referee evidence only in /private/tmp | Whole session scratchpad copied verbatim to `audits/session_scratch_2026-09-18/` (108 files, 7.6 MB, `diff -r` identical; provenance in its README). MANIFEST regenerated. |
| C6 | optimal curve | Which of E, E′ is the strong Weil curve is **UNKNOWN** (C1 l.21–22). Nothing here needs it: c_E ∣ 2c₀ holds either way (CNS, proof of Cor. 7.3), so c_E ≤ 512 and the (1/1024)Z lattice statement of §5 stand. |
| C7 | PARI normalization at non-split 3 not checked | **Done (coordinator calibration, NUMERIC).** `coord_checks/nonsplit3_calib.{sage,out}` and `nonsplit3_sharp.{sage,out}`: on 13 Cremona curves with non-split multiplicative reduction at 3, ρ̄₃ surjective, 3 ∤ ∏c·#tors·Sha_an, reduced models (PARI's raw-model offset is 0), the valuation predicted from PARI's `ellpadicregulator`, ord₃ L₃* = ord₃ Reg₃ − r (ord₃ log₃ 4 = 1), equals the valuation of the leading coefficient of Sage's exact-modular-symbol 3-adic L-series **in all 13 cases**: 8 generic (4 of rank 1, 4 of rank 2; predicted 0) and 5 sharp rank-1 cases with ord₃ Reg₃ = 2 or 3 (312b1, 354f1, 390a1 → 1; 357b1, 474a1 → 2). This excludes any 3-power normalization offset in PARI's non-split path (`ellpadics2_tate`). Caveat: the sharp cases are rank 1 only. On the seed (reduced model, AUDIT_C item 7) ord₃ Reg₃ = 2, so **ord₃ Reg_γ = 0**. The p = 3 outcome is therefore CONDITIONAL only on the Skinner Thm A identifications (1)–(3) (operator decision, §5), plus the Manin qualifier. Side finding: PARI 2.17.3 (sage-env) `ellpadicregulator` raised `e_BUG` ("bug in ellpadicheight, please report") on 983 of 9459 non-split-at-3 curves scanned (first: 507c1; `coord_checks/scan_reg3.out`); not on the seed. |
| C8 | outcome rule at p ≥ 7 | Under the chain the report asserts (SU IMC equality, SW Thm 6.1, unit ε_p and Reg_γ, index 1), X_p ≡ 0 (mod p) would give ord_p a₂ ≥ 1, i.e. #Sha[p^∞] ≥ p² or Sha[p^∞] infinite, contradicting the numerical prediction (Sha_an = 9). The plan's "no conclusion at this depth" is deliberately conservative. **Coordinator rule:** any X_p ≡ 0 (mod p) at p ≥ 7 triggers STOP-AND-AUDIT, exactly as at p = 3. |
| C9 | p > 100 gates | Each p > 100 needs its own cheap gates (non-anomalous; unit Reg_γ; E(Q)/pE(Q) = ⟨P₁,P₂⟩): 01_GATES §6, 03_COST l.86. Lane C: no anomalous good p in [5, 10⁵) (`C_frontier/runs/local_data_output.txt`). |
| C10 | breadth of "ord_p Reg immune" | Checked directly at p = 3, 7 (reduced model, AUDIT_C) and p = 7, 11, 17 (Sage canonical `padic_height`, `coord_checks/padic_reg_sage.out`). The other 15 gate values ord_p Reg_p = 2 rest on PARI's raw model plus the unaudited rank-one argument (correction c·ℓᵀ adj(H) ℓ with v(ℓ) ≥ 1, v(adj H) ≥ 1). Cost planning only; no PROVED claim depends on them. |
| C11 | Silverman constant | B = 20.329 is the maximum of the forms the lane transcribed; the crude form is unconfirmed from a primary source and is not load-bearing. Only the refined lower-side constant (Sage l.2745–2756, eclib source) is. Route (a), eclib, is independent. |
| C12 | rank ≥ 2 evidence | Exact inputs: Zywina Thm 1.2, and the mod-p certificates (the image of ⟨P₁,P₂⟩ in E(Q)/pE(Q) has F_p-dimension 2 for every odd p ≤ 100, `D_primes/gates/`). The certified Reg ≠ 0 is corroboration. |
| C13 | a_q custody in run B | On (4.5·10⁸, 5.5·10⁸] run B's a_q come from PARI `ellap` only. The run-1-only certified bound (1.53·10⁻¹⁴, certified counter) still excludes 0 and gives Sha_an = 9 ± 3.9·10⁻¹⁵. No label changes. |
| C14 | audit timestamps | Nits; the audit files' own times govern. |
