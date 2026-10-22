> **Historical supporting record, preserved during the 2026-09-19 reconciliation.** The current mathematical status and claim-specific supersession are in [MASTER_BSD_DAG.md](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md). Tentative or outdated statements below do not override that record. The pre-reconciliation bytes are preserved in the archive identified by `RECONCILIATION_INVENTORY.json`.

# QUESTIONS CODEX MUST ANSWER BEFORE DESIGNING NEW MATH

Answer each INDEPENDENTLY of this project's conclusions (every audit so far was same-model-family). For each question the
hand-off gives the project's current position and where its evidence sits, so that you can attack it rather than rebuild it.

**Standing notes (2026-09-19):**
- A1/A2 conditional algebra is now Lean-machine-checked and frozen; do not spend premium reasoning on those layers.
- The [canonical research gate](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/CANONICAL_RESEARCH_GATE.md) governs all new work. The Albertson coverage requirement applies to prime-partition strategies: independent reduction, uniform infinite regimes, full-primary finite residue and assembly. A direct global Sha bound is also admissible. Complete the seven-point card and four kill checks before substantial work; this list is not permission to resume every older question.

**Q0 — KILL GATE (added 2026-09-19 after the cross-family WC result; answer BEFORE spending premium effort on constructing J_E).** **STATUS: answered on the good ordinary tail by Codex Theorem O1 (`BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md`): h_p = 0 ⟺ Sha[p^∞] = 0. The positive-depth transfer and the supersingular primes remain.**
Is WC genuinely a lower-complexity arithmetic target, or essentially equivalent to FIN on the ordinary tail?
1. Read the exact converse that would give Sha[p^∞] = 0 ⇒ a depth-0 Ota witness. Candidates: Kurihara's structure theorem for Kato's Kolyvagin system, and
   its non-vanishing/primitivity under the IMC (e.g. Kurihara; C.-H. Kim; Mazur–Rubin). These references are cited from memory; confirm them.
2. Check its hypotheses for this seed at the good ordinary primes p ∉ S0. For example, Skinner–Urban needs ρ̄_p ramified at some q ∥ N; v_2243(Δ) = 1
   suggests this holds for every odd p, but it is NOT verified.
3. Prove precisely whether Sha[p^∞] = 0 ⟺ existence/non-divisibility of the relevant Ota witness, or only one direction. Also settle depth > 0,
   and the supersingular p, where a ± IMC for non-squarefree N is unpublished.
4. Decide whether the uniform bounded-content version (one integer A) contains any cross-prime information beyond the collection of individual FIN statements.
5. Substantial work requires a new independent method under checked hypotheses. Equivalence alone neither proves difficulty reduction nor forbids a useful new tool. Without that input, stop after the bounded scout; do not pivot automatically to B or a successor object.

**Q1. Is FIN + FORMULA truly the cleanest top-level architecture for this seed (RANK being done)?**
Project position: yes (F2 §F.3; `MASTER_BSD_DAG.md` §0). Check: is any top-level condition hidden inside FORMULA (e.g. exactness of
Ω, Reg, Manin constant — F2 says the Manin constant does NOT enter) or inside RANK (Zywina's theorem is a preprint; PARI 2-descent replay)?

**Q2. Is there ANY old artifact or current theorem that already implies FIN?**
Project position: none found (F2 §E: "No older artifact implies S3, any infinite part of S≥7, S_4547, or SRAT"; F3 NOT_FOUND).
Caveats to test: Castella–Hsieh §6 + BD05 Cor 3 (instance-level, per (E,K,p), unverified); Fouquet–Wan (unpublished);
Nguyen 1309.7675 (not audited here); anything after 2026-09-18.

**Q3. Does LINE contain genuine new leverage, or does it only repackage FIN?**
Project position (hostile audit): per prime it is the Ota/Kurihara witness; its only new content is cross-prime rationality of one
scalar, which is MORE than FIN needs; no intermediate lemma; not finitely checkable. Decide whether any part of it is worth
premium effort, or whether it should be filed as a formulation only. Evidence: `FIN_FRONTIER.md` §1; audit ledger.

**Q4. Is there another characteristic-zero object that gives cross-prime control WITHOUT LINE?**
Known obstruction: every rank-two object in hand has coefficients in a product of finite rings (Ẑ-module, no rational line);
ideals without elements are equivalent to FIN. Candidates never excluded: a modular class in ∧²E(Q); a Kolyvagin-type bound
from a definite-quaternionic (Gross-point) θ_K whose leading term is LINEAR in P₁∧P₂ (second derived height is alternating —
HEURISTIC in the design lane, not audited); horizontal (p-varying) congruences of Beilinson–Kato elements.

**Q5. Can the same object plausibly yield BOTH FIN and FORMULA?**
Project position: the smallest statement found touching both is BKS Conj 1.6 (GPR) for almost all p WITH its complex scalar;
LINE ∧ GPR(one p) ⇒ q rational (conditional remark, audited). In ranks 0 and 1 one global object does both. `FORMULA_FRONTIER.md` §2, §4.

**Note for Q5/Q8 — the FORMULA target, stated so it cannot be conflated with a route.** Do NOT assume GPR is the required theorem.
Given FIN with #Sha = 9, the actual target is: q_∞ = L″(E,1)/(2ΩReg) is RATIONAL with an explicit SMALL DENOMINATOR (D ≤ 174 suffices with the
present rigorous ball, whose numerical premise is now PROVED_COMPUTER_ASSISTED (q_∞ ∈ (35.99427, 36.00573)); D < 3.3·10¹⁴ at the certified precision). GPR_an(p) and order-two Gross–Zagier are
candidate routes that are stronger than this. Determine the WEAKEST theorem that proves the target, and whether it reduces to executable
lemmas rather than a wholesale new rank-two theory — or whether rationality alone already contains the hard part. Already settled, do not
redo: Lemma U is BKS I Thm 7.3; the sealed p = 5 digit u₅ ≡ 1 (mod 5) is k-independent and is a consistency check only.
Cross-family update (2026-09-19): rationality is not the only certificate. Bounded algebraicity (Lemma E) and the one-sided common certificate B
are alternative sufficient architectures (`FORMULA_FRONTIER.md` §0b); under the retained interval the scalar certificates force the same q=36. FIN alone does not give #Sha = 9. The 441 bound is another sufficient endgame, not a demonstrated reduction in difficulty.

**Q6. Can p = 4547 be absorbed by a genuinely global argument?**
Project position: yes by outright finiteness or a Kolyvagin-type theorem; NO by Kato/Iwasawa-type or Ota/LINE-type theorems
(they invert or exclude p ∣ N / additive p). Matrix in `MASTER_BSD_DAG.md` §2. F2 flags the Kolyvagin-type reading as FROM MEMORY.

**Q7. Are the current H9 stops actually relevant now that rank = analytic rank = 2 and Sha[3^∞], Sha[5^∞] are known?**
Project position: H9 objects are per-p p-adic classes, equivalent per prime to finiteness of Sha[p^∞] (with the proving direction
assuming it); they do not address the tail or FORMULA. `ROUTES_AND_STOPS.md` §1. Is there a use of H9 we are missing
(e.g. as the p-adic realisation of a future global object)?

**Q8. What is the smallest GENERALIZABLE theorem — not a seed-specific computation — that most directly advances full BSD in analytic rank 2?**
Candidates on the table, none ranked by probability (the project forbids manufactured odds): (a) a write-up of
CRITERION_SS (hostile gate DONE 2026-09-19: VALID_WITH_CORRECTIONS; generalizable, finite-cost consequence); (b) the tame-pairing = Tate–Lichtenbaum lemma and ρ_n ≡ unit·det² as a
clean bridge MT ↔ Kurihara numbers; (c) closing F1's R2 (canonical vs Gross period at p ∥ N, p = 3) — hardens every p ∣ N
application of Skinner's Thm A; (d) the ± local theory at additive potentially supersingular primes (Forrás–Lei transported to
non-CM) for p = 4547-type primes; (e) anything toward p-independence (Q3/Q4).

**Q9. Which candidate nodes are sufficiently formal for Aristotle/Harmonic (Lean) to attack?**
Already Lean-checked: see `ROUTES_AND_STOPS.md` §6. Plausibly formal now: the lattice lemma; the Gram/Cauchy–Binet computation
ρ_n = ∏c_i·det(M)²; Theorem C′ as a purely formal implication from stated hypotheses (Ota 5.17/6.4 as axioms); the CRT remark
"(L2) has no finite-level content"; group theory of core-pair existence (elements of GL₂(Z/p^{k+1}) with v_p det(g−1) = k;
−I disjointness); F4 §1 logic (rationality + denominator bound ⇒ exact value). NOT formal yet: anything touching modular
symbols, Euler systems, Selmer complexes, heights.

**Q10. What should NOT consume premium Codex/Astra tokens?**
- Re-running or re-auditing the a_q streams, the p = 3 run, the p = 5 upgrade, the analytic-rank ball (hash-bound, replayed).
- Repeating F3's or F4's literature hunts (61 + ≈ 145 sources; query logs on disk) — only a dated delta after 2026-09-18.
- Re-deriving v₂(c₀) ≤ 8, the residual-image theorem, Lane 2's regulator congruence, (N), or BKS II linearity.
- H41 / 62a1 / 66b1 (frozen rank-0 programme); C1 class-group and Stark-system routes (closed).
- Degree-24 class-group computations; Kolyvagin/Kurihara witnesses at p ≥ 30 or at 4547, 2243, 5843 (n ≈ 10¹¹–10¹⁷).
- Computing more digits of L″(E,1): 15 digits already exceed any use short of a denominator bound.
- Testing LINE numerically as if a pass could prove it.
Spend instead on: Q2–Q5, a genuine cross-family check of F1's R1/R2 and of CRITERION_SS (which has a same-family gate only), and the logic of the DAG itself.
