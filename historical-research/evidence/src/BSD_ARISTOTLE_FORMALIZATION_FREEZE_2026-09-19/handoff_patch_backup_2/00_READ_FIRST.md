# 00_READ_FIRST — BSD seed (2243,12): master hand-off for the Codex/Astra whole-program audit (2026-09-19)

Not a theorem-design document. Source-bound state only. NOTHING IS MERGED by this hand-off. No novelty claim is made anywhere.
Status labels used (and only these): PROVED · PROVED_COMPUTER_ASSISTED · CERTIFIED_NUMERIC · CONDITIONAL · FORMULATED · PROPOSED ·
SEMI_DECISION · COST_BLOCKED · ROUTE_BLOCKED · OPEN · SUPERSEDED · KILLED.

## 1. The seed
    E : y² = x³ − 22735x² + 106272484x        N = 2³·3·2243·4547²·5843        E(Q) = Z/2 × Z·P₁ × Z·P₂
    P₁ = (4547, 327384), P₂ = (5184, 281520);  ∏c_ℓ = 16;  #tors = 2;  w = +1;  ρ̄_ℓ = GL₂(F_ℓ) for every odd ℓ

## 2. Immutable finish line (this list must not grow)
    FULL BSD(E) = RANK ∧ FIN ∧ FORMULA
    RANK     rank E(Q) = ord_{s=1}L(E,s)                          — PROVED_COMPUTER_ASSISTED, done (= 2 on both sides)
    FIN      Sha(E/Q) finite                                      — OPEN
    FORMULA  L″(E,1)/(2·Ω·Reg) = 4·#Sha(E/Q)                      — OPEN
**Remaining top-level obligations: FIN, FORMULA.** Route-specific problems (p = 4547, supersingular primes, 2243, 5843, the
large-p tail) are nodes UNDER FIN. The older "S3 ∧ S≥7 ∧ SRAT" is a true and useful computational decomposition, not the finish line.

## 3. One-screen state
| claim | status |
|---|---|
| rank E(Q) = 2, exact basis P₁,P₂ | PROVED (Zywina PREPRINT Thm 1.2 + exact PARI 2-descent replay) |
| ord_{s=1}L(E,s) = 2 | PROVED_COMPUTER_ASSISTED (Arb ball L″/2 ∈ [35.929604, 35.941023]); the old numeric label is SUPERSEDED |
| full odd residual image; v₂(c₀) ≤ 8; 4547 ∤ c₀; local/Tamagawa data | PROVED (v₂(c₀) ≤ 8 is a DERIVED lemma, audited + partly Lean-checked; 4547 ∤ c₀ via published restatements of Edixhoven) |
| Sha[2^∞] = 0 | PROVED |
| **Sha[3^∞] ≅ (Z/3Z)², order 9** | **PROVED_COMPUTER_ASSISTED**, relative to Skinner (2016) Thm A as printed; a_{4,2} = 15480 ≡ 9 (mod 27), ord₃ = 2; **F1 notes carried, NOT closed: R1 (Jones 1989 unread); R2 remains OPEN as a provenance seam, narrowed to the canonical-vs-Gross period comparison for p = 3 with 3 ∣ N (source-reading addendum `P3_R2_PERIOD_PROVENANCE_AUDIT.md`)** |
| **Sha[5^∞] = 0** | **PROVED_COMPUTER_ASSISTED** — `P5_RIGOROUS_SHA5_ZERO_CONFIRMED` (sealed 2026-09-19): node N7 upgraded from CERT-NUM to PROVED_COMPUTER_ASSISTED; a_{2,2} ≡ 2 (mod 5) in the ω₁ normalisation, ord₅(a₂) = 0 (§5) |
| #Sha[30^∞] = 9 | PROVED_COMPUTER_ASSISTED (no CERT-NUM qualifier remains on the p = 5 input; inherits R1/R2 from p = 3) |
| L″(E,1)/(2ΩReg) = 36 ± 3·10⁻¹⁵ | CERTIFIED_NUMERIC (evidence only; proves nothing exact; NOT a rigorous ball) |
| q_∞ ∈ (35.99427, 36.00573), q_∞ := L″(E,1)/(2ΩReg) | **PROVED_COMPUTER_ASSISTED** (Arb L″/2 ball ÷ rigorous Ω·Reg enclosure: Codex `REGULATOR_CERTIFICATE.md`, 2026-09-19, replayed byte-identically by Opus). Hence q_∞ ∈ Q with reduced denominator ≤ 174 would force q_∞ = 36 |
| Sha[p^∞] for every p ≥ 7 | OPEN (per-prime procedures exist on paper; none run; no tail theorem). Good supersingular p: CRITERION_SS is a PROVED depth-2 SEMI_DECISION (hostile gate `CRITERION_SS_VALID_WITH_CORRECTIONS`); no bit computed |
| exact rationality / denominator bound for L″/(ΩReg) — or bounded algebraicity, or a one-sided common certificate B (`FORMULA_FRONTIER.md` §0b) | OPEN |
| WC finite algebra (A1 Lean package) | **A1 WC FINITE-ALGEBRA FORMALIZATION = MACHINE-CHECKED · STATUS = CONDITIONAL · LEVEL = A1_FULL · ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED · FIN STATUS = UNCHANGED** (successor freeze `~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A1_WITNESS_CONTENT_FULL_FREEZE_2026-09-19.tar.gz`, sha256 `dfe5f660d750cbe8…`; `FIN_FRONTIER.md` §5) |

## 4. The two literature hunts and the one candidate mechanism
- **F3 (large p):** NOT_FOUND — no published theorem gives Sha[p] = 0 for all large p for this rank-2 seed. Strongest near miss:
  Ota's Mazur–Tate leading-term theorem — a p-independent source θ_S exists and per-p non-vanishing implies Sha[p] = 0, but the
  leading term lives in a FINITE augmentation quotient, so one fixed S controls only finitely many p.
- **F4 (archimedean):** NOT_FOUND — no theorem gives rationality or a denominator bound for L″(E,1)/(ΩReg) at a genuine primitive
  double zero over Q. Neither hunt is an impossibility statement.
- **LINE** (one rational scalar a/b with b·δ_n = a·ρ_n at all core pairs, all good p): FORMULATED. Hostile audit:
  `LINE_THEOREM_C_PASS_WITH_CORRECTIONS`. Tame LINE is meaningful and non-circular; normalisation N survived (ρ_n ≡ unit·det(localisation
  matrix)²); Theorem C′ is CONDITIONAL on LINE (finite Sha[p^∞] at every good p, zero for p ∤ a). BUT: LINE is not known, is not a
  reduction to an easier finite problem, is per prime essentially the Ota/Kurihara witness, has all its content in CROSS-PRIME
  RATIONALITY (no intermediate lemma found; not finitely checkable), is silent at {2,3,2243,4547,5843} and on L″; and
  "LINE ⟺ determinant-line RZ" is WITHDRAWN. It is one serious candidate architecture for part of FIN whose exact stopping point is known — not "the route".
- **CRITERION_SS** (good supersingular primes at depth 2): **hostile gate PASSED — `CRITERION_SS_VALID_WITH_CORRECTIONS`** (2026-09-19; `~/BSD_SEED_2243_12_CRITERION_SS_HOSTILE_GATE_2026-09-19/CRITERION_SS_HOSTILE_GATE.md`, sha256 `7c58bb16…`).
  Surviving theorem (PROVED from published inputs): E/Q non-CM, p ≥ 5 good supersingular (a_p = 0), ρ̄_p surjective, r = rank E(Q) ≤ p − 1; θ₁ = Mazur–Tate element of the [a/p²]⁺; if θ₁ mod p = c_r·X^r + O(X^{r+1}) in F_p[X]/(X^p) with c_r ≢ 0 (mod p), then Sel(E/Q,E[p^∞]) ≅ (Q_p/Z_p)^r and Sha(E/Q)[p^∞] = 0.
  Inputs: Pollack Prop 6.18 at n = 1 (θ₁ ≡ unit·L_p^+ mod ω₁, no cyclotomic factor; unit = −½ in Kim–Kurihara's conventions); Kato–Kobayashi integral
  one-sided divisibility (L_p^+) ⊆ char(X⁻); level-0 control INJECTIVITY (p ∤ Tam not needed); B.D. Kim 2013 (no finite Λ-submodule). No IMC, no BSD, no p-adic BSD.
  **For the seed it is a proved SEMI_DECISION route at 23, 29, 131, …, not a result: no bit has been computed, and a failed bit proves nothing.**
  Re-derived cost (rigorous pipeline): T_min(23²) = 1.76·10¹¹, T_min(29²) = 2.83·10¹¹ ⇒ ≈ 270 / 460 CPU-h (≈ 500 shared; witnesses ≈ 200–310 GB,
  not storable); cost grows like p². **A per-prime FALLBACK, not the global FIN solution.** Same-family gate; Pollack 2003, Kobayashi 2003 and
  B.D. Kim 2013 were read only through faithful restatements (Kim–Kurihara, Pollack–Rubin, Kitajima–Otsuki).
- p = 4547: SEMI_DECISION + ROUTE_BLOCKED under a prime-by-prime strategy; disappears if FIN is proved globally.
- **FORMULA frontier, frozen at two levels (`FORMULA_FRONTIER.md` §0, §5):** MINIMAL TARGET = q_∞ = L″/(2ΩReg) ∈ Q with an explicit small denominator (D ≤ 174; its numerical premise is now PROVED_COMPUTER_ASSISTED); STRUCTURED CANDIDATE ROUTE = GPR_an(p) or an order-two Rankin–Selberg/Gross–Zagier comparison — stronger than the target, not known necessary; do not conflate. R2 bridge design: `R2_BRIDGE_ONE_MAJOR_THEOREM_MISSING`; Lemma U is BKS I Thm 7.3 (published, not a missing theorem); sealed p = 5 unit digit u₅ ≡ 1 (mod 5), k-independent, one digit (u₅ = 1 + 5a), consistency only.
- **Cross-family frontier attack** (Codex, 2026-09-19; `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/`, verdict `BSD_FRONTIER_UNKNOWN`; Opus cross-check in `~/BSD_SEED_2243_12_FIN_ASSUMED_FORMULA_AUDIT_2026-09-19/ADDENDUM_CROSS_FAMILY_2026-09-19.md`):
  - **WC (witness content).** If a nonzero integer A lies in J_E, then Sha[p^∞] is finite for every p ∉ S0 = {2,3,5,2243,4547,5843}, and zero for p ∤ A.
    - The implication is PROVED from Ota Thms 5.17/6.4. The antecedent J_E ≠ 0 is OPEN.
    - WC is **weaker than LINE**, but that does **not** make its antecedent easier than FIN.
    - At good ordinary primes, a Kurihara/Kim-type converse (its hypotheses are UNCHECKED for the seed) would turn Sha[p^∞] = 0 into the required
      witness. On the ordinary tail, J_E ≠ 0 may then be FIN written in Ota coordinates.
    - So WC is a clean interface, not yet a reduction in difficulty (`FIN_FRONTIER.md` §5; kill gate `CODEX_QUESTIONS.md` Q0).
    - A compiled Lean/Aristotle proof of WC proves only the implication.
    - **Formal status (2026-09-19, A1 successor freeze):**
      - A1 WC FINITE-ALGEBRA FORMALIZATION = MACHINE-CHECKED · STATUS = CONDITIONAL · LEVEL = A1_FULL · ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED · FIN STATUS = UNCHANGED.
      - Freeze: `~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A1_WITNESS_CONTENT_FULL_FREEZE_2026-09-19.tar.gz` (sha256 `dfe5f660d750cbe8…`).
      - A2 (primary support): no successor freeze yet — its result is NOT recorded here; when it exists it goes to `~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A2_PRIMARY_SUPPORT_FULL/`.
  - **FORMULA has three incomparable sufficient certificates** (`FORMULA_FRONTIER.md` §0b). None has its antecedent proved.
    - Bounded rationality: denominator ≤ 174.
    - Bounded algebraicity: Lemma E.
    - The one-sided common certificate B: q_∞ = 4B and v_p(#Sha[p^∞]) ≤ v_p(B) for all p. This forces B = 9 and gives FIN ∧ FORMULA together.
  - **FIN does not give #Sha = 9.** Finiteness alone allows #Sha = 9t² with gcd(t,30) = 1.
  - **Numerics.** Ω·Reg is rigorously enclosed, so q_∞ ∈ (35.99427, 36.00573) is PROVED_COMPUTER_ASSISTED. The old statement that Reg and C were only
    PARI values was wrong: Lane 3 had an Arb interval method, which remains a historical source.

## 5. The p = 5 rigorous upgrade — FINISHED and SEALED (`P5_RIGOROUS_SHA5_ZERO_CONFIRMED`)
`~/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/`: `P5_RIGOROUS_REPORT.md`, `P5_CERTIFICATE.md`, `SHA5_RIGOROUS_THEOREM.md`,
`P5_REPLAY.md`, `P5_RESOURCE_LOG.md`, `P5_MANIFEST.sha256` (9 424 files; reported verified by the owning session; this architect
checked that the five report files' hashes are in it and that its STATE.json carries `return = P5_RIGOROUS_SHA5_ZERO_CONFIRMED`,
`merged = false`). Theorem: **Sha(E/Q)[5^∞] = 0, PROVED_COMPUTER_ASSISTED**, same Kato + Stein–Wuthrich chain as the frozen master
certificate with ONE change: node N7 is upgraded from CERT-NUM (LP5 double-precision stream) to PROVED_COMPUTER_ASSISTED.
- 360 542 141 a_q verified by the independent integer verifier (= PARI `primepi`; root `fcd02437…`; byte-identical to the p = 3 run on all 467 shared segments).
- The 20 symbols [b/25]⁺ recovered rigorously by Arb, each ball of radius < 1/2048 containing one point of (1/1024)Z:
  (−54, 16, 90, −52, −76, 16, 76, −52, −54, 90, 90, −54, −52, 76, 16, −76, −52, 90, 16, −54) — identical to the historical LP5 values.
- Exact residue **a_{2,2} ≡ 2 (mod 5)** in the ω₁ normalisation (≡ 1 in the Néron normalisation; non-zero in every normalisation since 5 ∤ c_E), hence **ord₅(a₂) = 0**; forced checks a_{2,0} = 0, a_{2,1} ≡ 0 (mod 5) hold; two independent evaluation routes agree.
- Replays PASS (cross-run 467/467, Stage W sample 32/32, fresh-directory Stage A byte-identical at W = 12 and W = 16, integrity 19/19).
- The frozen master certificate is NOT edited (it still prints N7 = CERT-NUM); the successor governs the grade of N7. Nothing is merged.
- Unchanged weakest links of the p = 5 theorem: v₂(c₀) ≤ 8 is a DERIVED lemma; 4547 ∤ c₀ via restatements of Edixhoven; Zywina's theorem is a preprint (rank replayed).
No computation of this project is running at hand-off time.

## 6. Independence caveat
Every audit cited in this folder (lane audits, F1–F4, Lane 4, the LINE hostile audit) was performed by fresh-context sessions of
the SAME model family as the authors. None is independent in the project charter's sense. Yours is the first cross-family review.

## 7. File map (read in this order; stop when you have enough)
1. `MASTER_BSD_DAG.md` — the DAG under RANK ∧ FIN ∧ FORMULA, and which future theorem type would absorb which sub-node.
2. `SEED_PROVED_STATE.md` — every established claim with status and the provenance notes that must travel (R1/R2, N7, Manin gate).
3. `FIN_FRONTIER.md` / `FORMULA_FRONTIER.md` — CURRENT KNOWN FRONTIER (four architectures each: theorem support, missing implication, generalizable?, can computation help?).
4. `DO_NOT_RESURRECT.md` — 41 killed, superseded or not-established claims with corrected versions (rows 30–33 were renumbered on 2026-09-19 from a duplicated 28–31).
5. `ROUTES_AND_STOPS.md` — H9, Lane 2, C1 gates, H41/62a1/66b1, LINE lane, Lean lemmas, custody infrastructure.
6. `CODEX_QUESTIONS.md` — the Q0 kill gate (is WC easier than FIN?) plus the ten questions to answer before designing new mathematics.
7. `SOURCE_AND_HASH_INDEX.md` — on-disk sources with sha256; what this architect read versus carried from records.
`STATE.json`, `RESUME.md`, `MANIFEST.sha256` — custody.

## 8. Known unreconciled items (full list in `SOURCE_AND_HASH_INDEX.md` §3)
No mathematical contradiction was found between the sources. Open seams a reader must not smooth over: R2 remains OPEN as a provenance seam, narrowed to the canonical-vs-Gross period comparison for p = 3 with 3 ∣ N — and it is load-bearing for
the whole p = 3 result; the rank rests on a preprint (replayed by PARI); Reg and C ARE now rigorously enclosed (Codex `REGULATOR_CERTIFICATE.md`, replayed by Opus). The earlier wording "not Arb enclosures" was wrong: Lane 3 already had an Arb interval computation, kept as a historical source; F2 labels 4547 a "third root" (true under a prime-by-prime strategy; a sub-node of FIN here).
