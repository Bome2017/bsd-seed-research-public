> **Historical supporting record, preserved during the 2026-09-19 reconciliation.** The current mathematical status and claim-specific supersession are in [MASTER_BSD_DAG.md](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md). Tentative or outdated statements below do not override that record. The pre-reconciliation bytes are preserved in the archive identified by `RECONCILIATION_INVENTORY.json`.

# FORMULA_FRONTIER — CURRENT KNOWN FRONTIER TOWARD FORMULA (not "all that remains")

**Standing continuation rule:** [RESEARCH_GATE.md](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/RESEARCH_GATE.md) governs admission and supersedes inconsistent older strategic wording. Proof labels and carried provenance are unchanged; this update supplies no new arithmetic antecedent.

FORMULA := L″(E,1)/(2·Ω·Reg) = 4·#Sha(E/Q).   It presupposes FIN.
Numerical state: L″(E,1)/(2ΩReg) = 36 ± 3·10⁻¹⁵ — CERTIFIED_NUMERIC (Lane 3; floating-point model, certified truncation).
Rigorous-only state: L″(E,1)/2 ∈ [35.929604, 35.941023] — PROVED_COMPUTER_ASSISTED (Arb); with the CERTIFIED_NUMERIC C this
gives (L″/2)/C ∈ [8.9986, 9.0015].
RIGOROUS QUOTIENT (2026-09-19, cross-family): q_∞ ∈ (35.99427, 36.00573) is PROVED_COMPUTER_ASSISTED. It is the Arb ball above divided by a rigorous
Ω·Reg enclosure (Codex `REGULATOR_CERTIFICATE.md`; the Opus replay is identical at both settings). Reg and C were never only PARI values:
Lane 3 `B_invariants/06_period_regulator.md` already had an Arb interval computation, which is kept as a historical source.
What the numerics prove today (F4): q := L″/(2ΩReg) is 36, OR irrational, OR rational with denominator > 1/ε ≈ 3.3·10¹⁴. That is the CERT-NUM
level. Rigorously: q is 36, OR irrational, OR rational with reduced denominator ≥ 175.

## 0. FROZEN: two levels that must NOT be conflated
    ONE SUFFICIENT SCALAR CERTIFICATE (given FIN with #Sha = 9):
        q_∞ := L″(E,1)/(2·Ω_E·Reg(E)) ∈ Q  with an explicit small denominator D  (D·q_∞ ∈ Z).
        Threshold: D ≤ 174, and its numerical premise is now PROVED_COMPUTER_ASSISTED: q_∞ ∈ (35.99427, 36.00573), ε = 5.73·10⁻³,
        174·ε = 0.99702 < 1, and 175 fails (Codex `REGULATOR_CERTIFICATE.md`, replayed by Opus). D < 3.3·10¹⁴ with the CERTIFIED_NUMERIC value 36 ± 3·10⁻¹⁵.
        [Historical: this line previously read "once Ω·Reg has a rigorous enclosure … (Ω is Arb; Reg is not yet)". δ = 5.7192859·10⁻³ was the upper
        deviation only; the two-sided ε = 5.72003·10⁻³ gives the same D ≤ 174.]
    STRUCTURED CANDIDATE ROUTE (one way to get it; STRONGER than needed; not known to be necessary):
        GPR_an(p): ι_p(q_∞) = m_p (rank-two generalized Perrin-Riou archimedean comparison), or an order-two
        Rankin–Selberg / Gross–Zagier comparison implying the same rationality.
Do not tell the project it must prove all of GPR because GPR is the best-known framework. OPEN and decisive: whether rationality
with a small denominator can be had more cheaply, or whether rationality alone already contains the hard rank-two theory.

## 0b. Three sufficient certificate architectures for FORMULA (cross-family, 2026-09-19) — no antecedent is proved
Rigorous interval (PROVED_COMPUTER_ASSISTED): q_∞ ∈ (35.99427, 36.00573); ε = 5.73·10⁻³.
(i)   **Bounded rationality** (Codex Lemma D). If q_∞ ∈ Q with reduced denominator ≤ 174, then q_∞ = 36.
      174·ε < 1, while 175 fails. A reduced-denominator bound is not the same hypothesis as "174·q_∞ ∈ Z".
(ii)  **Bounded algebraicity** (Codex Lemma E). Suppose q_∞ is algebraic, with primitive irreducible f ∈ Z[X], leading coefficient a and conjugates
      q_∞ = q₁, …, q_d. If |a|·∏_{j>1} |36 − q_j| ≤ B and ε·B < 1, then q_∞ = 36.
      - Rationality is not needed first.
      - A degree bound alone is insufficient: conjugate/height control is essential.
(iii) **One-sided common certificate B** (Codex COMMON_OBJECT_ANALYSIS, Proposition). Suppose B is a positive rational with q_∞ = 4B, and for every
      prime p, Sha[p^∞] is finite with v_p(#Sha[p^∞]) ≤ v_p(B). Then:
      - v_p(B) ≥ 0 for all p, so B ∈ Z;
      - the interval forces B = 9;
      - Sha[p^∞] = 0 for p ≠ 3, and #Sha = 9 (from the known 3-part);
      - q_∞ = 36 = 4·#Sha.
      So **FIN ∧ FORMULA** follow together. Only one-sided bounds are needed, with no exact unit equality at any prime.
**Caveat for (i) and (ii).** They give q_∞ = 36, which is FORMULA only together with #Sha = 9. FIN alone allows #Sha = 9t² with gcd(t,30) = 1
(Cassels–Tate; Codex Lemma H). (iii) supplies both. As a common-object target, (iii) is currently more interesting than WC, which is not
shown to be easier than FIN (`FIN_FRONTIER.md` §5).

F4's literature hunt (≈ 90 full texts, 21 mandated topics, dated sweep to 2026-09-16): **NOT_FOUND** — no theorem gives exact
rationality or a denominator bound for L″(E,1)/(Ω·Reg) at a genuine primitive double zero over Q. This is a statement about
the sources searched, NOT a statement of impossibility.

Logic that any proposal must respect (F4 §1):
1. Rationality alone does not give q = 36. Rationality + an explicit D with D·q ∈ Z and D·δ < 1 does: D < 3.3·10¹⁴ for q = L″/(2ΩReg) at the certified precision (1.6·10¹⁴ for L″/(ΩReg)); D ≤ 174 with the rigorous ball alone (a larger D only costs digits).
2. Per-prime information (ord_p q for finitely many p) cannot replace the denominator bound.
3. First-derivative formulas (Gross–Zagier, GKZ, YZZ, KRY, Li–Liu AIPF, arithmetic GGP) read 0 = 0 on the seed.
4. "(1,1)-type" rank two (L(E/K,s) = L(E,s)·L(E^K,s), both of order 1; BSV Cor B, DLR proved cases) is Gross–Zagier twice; the seed has ONE primitive L-function with a double zero.
5. q is a complex-analytic number; even a proof of Sha ≅ (Z/3)² does not give q = 36, and q = 36 does not give FIN.

---------------------------------------------------------------------------------------------------------------------------
## 1. An order-2 Gross–Zagier / archimedean reciprocity object
**Shape wanted.** L″(E,1) = c·Ω·det(⟨z_i,z_j⟩), c ∈ Q^× explicit, z₁∧z₂ ∈ ∧²E(Q) constructed and computable. For the seed
∧²(E(Q)/tors) = Z·(P₁∧P₂), so this collapses to ONE scalar identity; the index [∧²E(Q) : Z·z₁∧z₂]² would be q/(c/2)-type data.
**Theorem support.** Function fields only: Yun–Zhang I/II (Cor 1.4 of II has exactly the right shape), Feng–Yun–Zhang, etc.
Authors (2017, 2018, 2024, 16 Sep 2026): no number-field space of shtukas with r > 1 legs is known; "the existence of a story for
higher derivatives is a distinctive feature of the function field setting". Plectic / mock plectic constructions: conjectural,
p-adic, degenerate to rank one over Q; Banwait (8 Sep 2026): "No construction is known that attaches an algebraic number to L″(E,1)."
**Exact missing implication.** The object itself, plus a complex-analytic formula for its height. Design extraction (LINE lane,
TEST 5): over F_q the product X×X makes ∧²H¹ an honest H² receiving cycle classes; over Q nothing plays the role of X×X.
**Seed-specific?** No. **Finite computation?** No (numerics are already at 15 digits and prove nothing exact).

## 2. Generalized Perrin-Riou / Burns–Kurihara–Sano comparison with the COMPLEX scalar
**Theorem support.** BKS, JMSJ 76 (2024): Conj 1.1/1.6 (GPR); Cor 1.11: GPR ⇒ "p-adic Beilinson formula"
(1−1/α)⁻¹(1−1/β)·L_{S,p}^{(r)} = [L_S^{(r)}(E,1)/(Ω⁺R_∞)]·R_p; Thm 1.14 (p-part of BSD) ASSUMES Sha finite, IMC, GPR, R^{Boc} ≠ 0.
PROVED only for r = 1 (Perrin-Riou, Kobayashi; BDV, BPS) and r = 0 with an exceptional zero. For r = 2: CONDITIONAL on an open conjecture.
The complex number enters only through a fixed embedding R ↪ C_p.
**What it would give.** GPR at ONE prime p for every embedding ⇒ q ∈ Q and ord_p q — NOT a denominator bound (F4 CP-1).
GPR for almost all p with its complex scalar is the smallest statement found that touches BOTH FIN and FORMULA: it implies
q ∈ Q, implies LINE with a/b = q·#tors²/∏c, hence (Theorem C′) finiteness at good p ≥ 5, then BKS Thm 1.14 prime by prime.
Conditional remark confirmed by the LINE audit: LINE ∧ GPR(p₀) ⇒ q = a/b·(constants) is rational (LINE asserts existence of the
scalar, not its value).
**Exact missing implication.** GPR for r = 2 at even one prime; equivalently an explicit reciprocity law computing the Bockstein
derivative of Kato's class in terms of L″(E,1). **Seed-specific?** No. **Finite computation?** Only consistency checks
(e.g. the 5-adic one: a₂^{SW} ≡ 1 mod 5 matches 4·9·Reg_γ·ε₅ ≡ 1 — Lane 2).

## 3. Determinant / motivic alternatives
- ETNC: rationality of the zeta element is Flach's Conjecture 2; proved cases for elliptic curves are CM rank 0 / non-central. "Progress … in the case ord ≤ 1 (but none for higher vanishing order)".
- Kontsevich–Zagier: Ω·Reg is a period (theorem); "L^{(r)}(f,k/2) is a period" is Problem 4, open for r ≥ 2; even if solved, equality of two periods has no decision procedure. A pointer, not a route.
- Lattice lemma (LINE lane §8, confirmed): a p-independent determinant/Fitting IDEAL exists iff FIN; it carries valuations only and can never produce the complex identity; one needs an ELEMENT (the zeta element), i.e. §1 or §2.
- Mazur–Tate leading terms are ALGEBRAIC (#Sha·∏c/#tors² times a tame regulator): they contain no L″ even conjecturally (F4 D2). LINE therefore has NO implication for FORMULA — confirmed by the hostile audit (item 9).
- Leading-term theorems of order ≥ 2 that DO exist over number fields (Stark–Tate for rational characters, Borel, Samart–Tao Mahler-measure determinants) are at NON-central points where the zero is forced by Γ-factors and the regulator lives in units or K-theory.

## 4. Exact reason the existing p-adic formulas do not imply the complex identity
Every rank-two p-adic theorem found (Stein–Wuthrich/Schneider/Perrin-Riou leading terms, Castella–Hsieh generalized Kato
classes, Darmon–Rotger, BSV, Fornea–Gehrmann, Banwait, BKS Thm 1.9) compares a p-adic analytic object with the ALGEBRAIC side
(#Sha, Reg_p, Tamagawa) or with another p-adic object. None contains the value L″(E,1). In rank 1 the bridge is a single global
object — the Heegner point — that feeds BOTH the complex Gross–Zagier formula and the p-adic one; in rank 0 it is Kato's
reciprocity law landing on L(E,1)/Ω. In rank 2: Kato's classes come from K₂ (Beilinson elements), whose ARCHIMEDEAN regulator
sees L(E,2) ~ L′(E,0), not the central point; the centre is reached only by p-adic twisting, which has no complex counterpart;
and no rank-two global object exists to play the Heegner point's role. Wherever a p-adic leading-term formula is written with
L^{(r)}(E,1) on the right for r ≥ 2 (Disegni 2016, BKS 2024), rationality of L^{(r)}/(ΩR) is a HYPOTHESIS of the formulation or a
consequence of the conjecture — never the output of a theorem.

---------------------------------------------------------------------------------------------------------------------------
## 5. Record of the R2 leading-term bridge design and its self-audit (2026-09-19; same-family; no computation; NOT merged)
Folder `~/BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/` (`R2_LEADING_TERM_BRIDGE_DESIGN.md`, `LEMMA_U_AND_P5_UNIT_AUDIT.md` — the audit governs).
- Classification: **R2_BRIDGE_ONE_MAJOR_THEOREM_MISSING.** Three scalars: q_∞ = L″/(2ΩReg) (real), m_p (p-adic, from Kato's determinantal
  zeta element), L^{alg} = ∏c·#Sha/#tors². Tame LINE (T1) has no archimedean content and cannot give FORMULA; FORMULA ⟸ FIN ∧ (denominator
  theorem T0) ∧ numerics; every p-adic route needs GPR_an (ι_p(q_∞) = m_p) at one prime at least, and given that arrow FORMULA ⟺ u_p = 1
  exactly, so GPR_alg(p₀) must never be used as an independent input. FIN fixes valuations only; nothing collapses after FIN.
- **Lemma U = LEMMA_U_PROVED_FROM_EXISTING_RESULTS:** z_Q = u_p·η^{alg}, u_p ∈ Z_p^×, is BKS I (arXiv:1910.07404) Theorem 7.3
  (Hyp 2.2 — only Sha[p^∞] finite — plus the IMC EQUALITY, integrally). At p = 5 and p = 3 it needs no global FIN. It says nothing about
  u_p beyond being a unit. Unread: BKS I Thm 7.8, §5.1–5.2.
- **Sealed p = 5 unit digit:** m₅ := a₂/(ε₅·Reg_γ) ≡ 1 (mod 5) with no FIN assumption (a₂ ≡ 1 in the L-value/Néron normalisation ÷2ω₁,
  ε₅ ≡ 1, Reg_γ ≡ 21 mod 25); with #Sha = 9, u₅ ≡ 1 (mod 5), i.e. u₅ = 1 + 5a with a ∈ Z₅ UNKNOWN. **Independent of k = v₂(c_E)** —
  confirmed at source: Stein–Wuthrich define [r]⁺ from the NEWFORM over the BSD real period (their l.287–296), BKS I §6.1 uses the MTT
  interpolation with Ω⁺ = v_ξ·Ω_ξ; the Manin constant enters integrality only. The design's claim that the test was blocked by k is WITHDRAWN.
  Label: **strongly supported; L/period side closed at source; height side closed for the MTT/SW unit (SW footnote 4 calibrates the height
  to MTT's exact Conj 5.1); identification with the BKS determinant-line unit pending Nekovář [31] / Benois [2] (unread; a sign is
  invisible for r = 2, a scalar c would enter as c²).** One digit; already noted by Lane 2 at numeric grade. Consistency evidence
  only — NOT closure of FORMULA, NOT evidence about the archimedean arrow.
- **Denominator threshold reconciled:** D ≤ 174 (criterion D·δ < 1 because 36·D ∈ Z); the design's earlier "86" used D·δ < 1/2 and is superseded.
- **Exact first remaining unproved arrow:** ι_p(q_∞) = m_p at ONE prime (GPR_an; BKS I Conj 4.9 / (6.2.1) for r = 2).


## 6. Canonical arithmeticity boundary

The [canonical gate](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/CANONICAL_RESEARCH_GATE.md) retains bounded rationality and bounded algebraicity as sufficient scalar certificates; it does not require a full higher-rank height formula. Under the interval, the 174 certificate is equivalent to q=36, as is the retained degree-at-most-two, totally positive integral, trace-at-most-246 certificate. These equivalences do not establish easier mathematics. See [exact endgames E3–E5](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/EXACT_ENDGAMES.md).

M1 remains an exact period identity. Its literal finite-monodromy, algebraic Tate-character, ordinary elliptic-homology, and specified finite exact-correction routes are constrained by the [register](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/CONSTRAINT_REGISTER.md); arithmeticity of a different realization is not ruled out. A q-only result still needs FIN and order nine. A common B remains admissible only with independent real and full-primary interfaces.
