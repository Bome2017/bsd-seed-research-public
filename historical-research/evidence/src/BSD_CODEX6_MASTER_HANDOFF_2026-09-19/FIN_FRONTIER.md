> **Historical supporting record, preserved during the 2026-09-19 reconciliation.** The current mathematical status and claim-specific supersession are in [MASTER_BSD_DAG.md](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md). Tentative or outdated statements below do not override that record. The pre-reconciliation bytes are preserved in the archive identified by `RECONCILIATION_INVENTORY.json`.

# FIN_FRONTIER — CURRENT KNOWN FRONTIER TOWARD FIN (not "all that remains")

**Standing continuation rule:** [RESEARCH_GATE.md](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/RESEARCH_GATE.md) governs admission and supersedes inconsistent older strategic wording. Proof labels and carried provenance are unchanged; this update supplies no new arithmetic antecedent.

FIN := Sha(E/Q) finite ⟺ (every Sha[p^∞] finite) ∧ (Sha[p] = 0 for almost all p).
Known so far: p = 2 (0), p = 3 ((Z/3)², R1/R2 carried), p = 5 (0, PROVED_COMPUTER_ASSISTED, rigorous N7, sealed); so #Sha[30^∞] = 9. See `SEED_PROVED_STATE.md`.
F3's literature hunt (61 candidate blocks): **NOT_FOUND** — no published theorem or credible preprint gives Sha[p] = 0 for all
large p, or finiteness, for this analytic-rank-2 seed. "Not found" is not "impossible".

Exact form of the open tail (F3 §4, derived by that coordinator; flag for referee): for good p ≥ 5,
   Sha[p^∞] = 0 ⟺ (ordinary p; Kim + Castella–Sano) some two-prime Kurihara number δ_{ℓ1ℓ2} is a p-unit
              ⟸ (any good p ≥ 5; Ota Thm 1.5/6.4) some θ̃_S ≢ 0 mod p with all ℓ ∣ S ≡ 1 (p), E(F_ℓ)[p] cyclic.
Every known certificate chooses its auxiliary primes RELATIVE TO p. That is the wall.

---------------------------------------------------------------------------------------------------------------------------
## 1. LINE — cross-prime rational scalar (candidate mechanism; stopping point known)

**Statement (tame, prime-by-prime form — the only meaningful one).** There are coprime non-zero integers a, b such that for
every prime p ≥ 5, p ∤ N, and every core pair n = ℓ1ℓ2 of every level p^k (ℓ_i ≡ 1 mod p^k, E(F_{ℓi})[p^∞] ≅ Z/p^k, (π_{ℓi}(P_j))
invertible mod p):      b·δ_n = a·ρ_n   in (G_{ℓ1}⊗G_{ℓ2}) ⊗ Z_p,
δ_n = multilinear component of the Mazur–Tate element θ_n mod I³ (defined unconditionally: Ota Thm 5.17),
ρ_n = multilinear component of Mazur–Tate's corrected discriminant of P₁∧P₂.  Status of LINE: **FORMULATED** (not known).

**Theorem support (exact).**
- Ota, AJM 140 (2018): Thm 5.17 θ_S ∈ Z_p⊗I^{min{r_{p^∞},p}} (r_{p^∞} = Selmer corank); Thm 6.4 (= 1.5 with R = Z_(p)): θ̃_S ≢ 0 mod p ⇒ Sha[p] = 0. Unconditional, any good p ≥ 5 for the seed, supersingular included. — PROVED (published; proofs read by the referee).
- Normalisation N: ρ_n ≡ unit·det(π_{ℓi}(P_j))² mod p; the T ≠ S terms of the corrected discriminant carry no multilinear component; at a Kolyvagin prime ⟨a, n_ℓ a′⟩_ℓ = (Tate–Lichtenbaum pairing)^{-1}. — PROVED in the hostile audit (derivation + 24/24 exact numerical checks at ℓ = 31, 181, 151, p = 5; regime-A cross-check at ℓ = 11). Provenance: Mazur–Tate 1987 itself unread; Tan (AIF 1995) restatement used; same-family referee.
- Core pairs exist at every level p^k (needs ρ_p onto GL₂(Z_p) via Serre's lemma p ≥ 5, conditions mod p^{k+1}, −I disjointness of Kummer and division towers). — PROVED in the audit.
- **Theorem C′ — CONDITIONAL on LINE:** Sha[p^∞] finite for every p ≥ 5, p ∤ N; Sha[p^∞] = 0 for p ∤ a. Verdict `LINE_THEOREM_C_PASS_WITH_CORRECTIONS`.
- BKS II (arXiv:2103.11535): z_Q exists under Hyp 2.2; ψ_Q identifies the p-adic determinant line with Q_p⊗(∧²E(Q))^{⊗2} WHEN Sha[p^∞] is finite; Thm 4.6 is linear in the scalar (the authors use z_Q = u·η^{alg} in §5.6). So m_p exists only in "regime A", under Hyp 2.2 + Sha[p^∞] finite, and not at p ∈ {19, 59, 487} for the seed.

**Exact missing implication.** p-independence of the scalar: (m_p)_p ∈ ∏Z_p is ONE rational number. No intermediate lemma toward
it was found. Known global sources of such a number: #Sha (needs FIN: circular), L″/(2ΩReg) (needs an archimedean reciprocity
law = BKS Conj 1.6), the index of a geometric class in ∧²E(Q) (no such class exists over Q).

**What LINE is NOT (hostile-audit corrections; binding).**
- NOT known. NOT a reduction to an easier finite problem.
- For each fixed p, "LINE at p with p ∤ a" is essentially equivalent to finding the Ota/Kurihara witness, i.e. to Sha[p] = 0.
  The ENTIRE new content is cross-prime rationality — which is MORE than FIN needs (FIN's tail only needs v_p(m_p) = 0 for
  almost all p; LINE also asserts coherence of unit parts).
- No finite computation can prove it (for finitely many p the Chinese remainder theorem always supplies an integer); finite
  computations can only refute it.
- It does NOT cover p ∈ {2, 3, 2243, 4547, 5843} and does NOT touch L″(E,1).
- "LINE ⟺ determinant-line RZ" is WITHDRAWN: RZ is only meaningful at p once Sha[p^∞] is finite.

**Seed-specific or generalizable?** Generalizable in form (any non-CM E/Q, any rank r: core n with r primes, ρ_n ≡ unit·det²).
The seed only simplifies bookkeeping (∧²E(Q) has rank one, basis known).
**Can finite computation help?** Only as a kill test: residues of the scalar at p = 5, 7, 11, 13 (modular symbols of
denominator ℓ = 11, 29, 23, 53 at N ≈ 6.5·10¹⁵) must fit ±9·2^j for one j. Not run; needs authorisation. A pass proves nothing.

---------------------------------------------------------------------------------------------------------------------------
## 2. Any alternative p-independent rank-two Euler / Kolyvagin / Mazur–Tate object

**Theorem support.** Rank 0: L(E,1)/Ω (Kato). Rank 1: Heegner point, index I_K (Kolyvagin; Cha, Jetchev, GJPST). Rank 2:
- Θ_E = (θ_S)_S is a p-independent characteristic-zero object (= the distribution of twisted central values); all per-p
  Kurihara/Ota witnesses factor through its leading term. — PROVED (assembled in the design lane, confirmed by the audit).
- Obstruction (exact): that leading term lives in ∏_S gr²(G_S), a product of finite groups = a Ẑ-module with no rational line;
  "non-zero" there says nothing about almost all p. Kolyvagin derivatives of Beilinson–Kato elements give motivic classes
  with FINITE coefficients only. — PROVED (elementary).
- Darmon 1992 (Heegner θ′ elements, Prop 5.9) and Bullach–Honnor 2511.07203 (θ^# ∈ Fitt⁰) fail uniformity for the same reason (F3 rows 0′, 0″).
- Mazur–Rubin: core rank of T_pE over Q is 1; κ₁ = z_Kato = 0 in MW rank 2; "higher rank Euler systems" in print mean higher CORE rank. Extending ω = δ(P₁)∧δ(P₂) to a residual Stark system is EQUIVALENT to Sha[p] = 0 (tautology; closed lane).
- A p-independent Fitting/determinant IDEAL exists iff FIN (lattice lemma) — the element cannot be avoided.
**Exact missing implication.** One non-zero integral (Z- or Q-coefficient) rank-two object whose reduction at p feeds a proved
per-p machine for all large p — e.g. a modular construction of a class in ∧²E(Q) ("a long-standing open problem",
Fornea–Gehrmann), or a Kolyvagin-type bound in terms of it. Posed as OPEN in print (Banwait 2609.08431 §1.5 Q3; Kim 2609.15328 Q4.6).
**Seed-specific?** No. **Finite computation?** No (it can only produce per-p witnesses).

---------------------------------------------------------------------------------------------------------------------------
## 3. A global finiteness theorem by another route

**What was checked and why it does not apply (F3 §2–3).** Coates–Liang–Sujatha (CM only; growing corank bound);
Diamond–Flach–Guo (uniform in ℓ but for ad⁰, wrong motive); visibility (constructs Sha — wrong direction); effective bounds
(assume BSD); class groups of Q(E[p]) (Prasad–Shekhar: an equivalence — a GL₂ Vandiver-type statement); plectic / mock plectic
(conjectural; only multiplicative p); Destrempes–Malinin Thm 5 (FALSE: 20806a1, ℓ = 11); Nguyen arXiv:1309.7675 (not credible;
NOT separately audited in this project).
**Instance-level caveat that must be stated (whole-map audit, 2026-09-16):** Castella–Hsieh §6 asserts Sha(E/K)[p^∞] finiteness
for its rank-2 tables via Bertolini–Darmon 2005 Cor 3 (exact order 2 of Θ_{E/K}). That is per (E, K, p) and BD05 was NOT
verified here; it is not a global FIN theorem. Do not say "no printed theorem gives any rank-2 finiteness" without this caveat.
**Exact missing implication.** Anything of the form "analytic rank 2 ⇒ Sha[p] = 0 for p outside an explicit finite set".
**Seed-specific?** A theorem would be general. **Finite computation?** No.

---------------------------------------------------------------------------------------------------------------------------
## 4. Prime-by-prime fallback (including the bad primes) — can never give FIN without a tail theorem H(p₀)

| class | theorem support | status | finite computation |
|---|---|---|---|
| good ordinary p ≥ 7 | Kato divisibility + SW Thm 6.1 (upper bound); Skinner–Urban guarantees termination only; Lane 2 ONE-BIT: a₂ ≢ 0 mod p ⇒ Sha[p^∞] = 0 with no regulator/saturation gate when p ∤ #E(F_p)∏c_v | OPEN per prime (decision procedure on paper) | yes: ≈ 0.23·p² CPU-h (Lane 3 cost model; shared pass ≈ cost of the largest p). p = 7 NOT authorised |
| good supersingular p (23, 29, 131, …) | **CRITERION_SS** — hostile gate `CRITERION_SS_VALID_WITH_CORRECTIONS` (2026-09-19): Pollack Prop 6.18 at n = 1 (θ₁ ≡ unit·L_p^+ mod ω₁, no cyclotomic factor) + Kato–Kobayashi integral divisibility (L_p^+) ⊆ char(X⁻) (ρ̄_p surjective) + level-0 control injectivity (p ∤ Tam not needed) + B.D. Kim (no finite Λ-submodule) ⇒ for rank r ≤ p − 1: c_r(θ₁) ≢ 0 mod p ⇒ X⁻ ≅ Z_p^r, Sel ≅ (Q_p/Z_p)^r, Sha[p^∞] = 0 | **SEMI_DECISION; the implication is PROVED** (a failed bit proves nothing; guaranteed success would need a ± IMC for non-squarefree N: unpublished) | yes, depth 2 only, but costly: T_min(23²) = 1.76·10¹¹, T_min(29²) = 2.83·10¹¹ ⇒ ≈ 270 / 460 CPU-h (≈ 500 shared; witnesses not storable). F2's ≈ 120 CPU-h and the older "depth 5–6" are SUPERSEDED. A fallback, not the global FIN solution |
| any good p ≥ 5 via Ota | Thm 6.4 with ONE ℓ ≡ 1 (p): leading term of θ_ℓ mod p | PROPOSED (cost claim UNVERIFIED; normalisation to be matched); SEMI_DECISION | yes; by-product of the LINE audit: det h_ℓ mod p (seconds, points only) pre-screens which (p,ℓ) can succeed |
| 2243 (split), 5843 (non-split) | Skinner Thm A + SW Thm 6.1 (split case needs L-invariant ≠ 0) | COST_BLOCKED (≈ 2·10⁴ / ≈ 10⁵ CPU-h; architect's figures, not re-derived). Note: an R2-type period-comparison question may recur at p ∣ N (not examined) | in principle |
| **4547** | only chain: Kim Thm 1.8 two-prime Kurihara witness | **SEMI_DECISION + ROUTE_BLOCKED**: additive III, potentially supersingular; no cyclotomic p-adic L-function (U_p-eigenvalue 0), no main conjecture, no control theorem (Kim–Nakamura); witness existence = Kim Conj 1.7 at an additive prime (unproved; Fouquet–Wan unpublished would give it); smallest Kolyvagin pair 87 256 931 · 92 849 741 ≈ 8.1·10¹⁵ (≳ 10²⁴ terms) — the earlier 1.6·10⁸ estimate was wrong by ≈ 8 orders | no. Research direction only: transport Forrás–Lei's ± local theory (CM, e = 4, j ≡ 1728) to E/Q_p with Kato's Euler system. **This node disappears if FIN is proved globally (type G or Kolyvagin type); it survives Kato/Iwasawa-type and Ota/LINE-type theorems** |
| tail H(p₀) | none | OPEN | no |

## 5. WC — Codex's witness-content criterion (cross-family, 2026-09-19): a clean interface, NOT a reduction in difficulty
Sources: `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` (sha256 `556ecfa5…`); Opus cross-check `~/BSD_SEED_2243_12_FIN_ASSUMED_FORMULA_AUDIT_2026-09-19/ADDENDUM_CROSS_FAMILY_2026-09-19.md`.

**Setup.**
- S0 = {2, 3, 5, 2243, 4547, 5843}, and P = the primes outside S0.
- For p ∈ P, S runs over squarefree products of good primes ℓ ∤ pN with ℓ ≡ 1 (mod p) and E(F_ℓ)[p] cyclic.
- t(p,S) is the degree-two image of θ_S in M(p,S) = I_S²/I_S³ ⊗ Z_p, a finite p-primary module.
- depth(t) = max{j : t ∈ p^j M}, defined only for t ≠ 0.
- h_p = the minimum depth over the nonzero t(p,S), and ∞ if there are none.
- J_E = {a ∈ Z : v_p(a) ≥ h_p for every p ∈ P}.

**Theorem WC** (conditional; PROVED from Ota Thms 5.17/6.4 as quoted). If J_E contains a nonzero integer A, then:
1. Sha[p^∞] is finite for every p ∈ P;
2. Sha[p^∞] = 0 for every p ∈ P with p ∤ A;
3. Sha is finite, provided the primary groups at S0 are finite.

**Status.**
- The implication is PROVED: Codex wrote the proof, and Opus checked the logic. Ota's hypotheses for p ∈ P are as checked by Codex; Opus did not re-verify them.
- The antecedent J_E ≠ 0 is OPEN: nothing has been constructed.
- LINE ⇒ WC (Codex, using the retained core-pair inputs), so **WC is weaker than LINE**.

**What that does NOT mean.** "Weaker than LINE" does not mean "its antecedent is easier than FIN".
- **Opus caveat** (2026-09-19; the converse hypotheses were NOT checked for the seed). At a good ordinary p where the IMC holds, a Kurihara/Kim-type
  converse (non-vanishing / primitivity of Kato's Kolyvagin system and Kurihara's structure theorem) should turn Sha[p^∞] = 0 into a depth-0 Ota witness.
- If so, then on the ordinary tail J_E ≠ 0 is essentially FIN written in Ota coordinates. Its only content beyond the prime-by-prime FIN statements would be
  the uniformity packaging (one integer A).
- **WC is a clean interface and gives formal structure. It is not yet a reduction in mathematical difficulty.**
- A compiled (Lean/Aristotle) proof of WC proves only the implication from the stated antecedent. It establishes neither that the antecedent is easier
  than FIN nor that FIN has been reduced (DO_NOT_RESURRECT rows 37–38).

**Kill gate before any premium effort on constructing J_E:** `CODEX_QUESTIONS.md` Q0.

**Formal status of WC's finite algebra and of the primary-support machinery (2026-09-19, successor freezes):**
```
    A1: CONDITIONAL WC FINITE ALGEBRA = LEAN MACHINE-CHECKED         LEVEL = A1_FULL
    A2: PRIMARY SUPPORT / CONTENT / ASSEMBLY = LEAN MACHINE-CHECKED  LEVEL = A2_FULL
    ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED
    FIN STATUS = UNCHANGED      FORMULA STATUS = UNCHANGED
```
- Freezes are in `~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/`: A1 sha256 `baa0435220954626b3f14a82fb874062d44267447ff1400748175ea55b276de0`, A2 sha256 `fd55eab35ef1e51e5caaadc729f2f99d986e6158b2f4ca54d0b31d224f5d541c`. The combined boundary is `FORMALIZATION_BOUNDARY.md`.
- Custodian replay from fresh unpacks: A1 20/20 and A2 28/28 targets are clean, with axioms ⊆ {propext, Classical.choice, Quot.sound}.
  Every hypothesis stays explicit: the antecedent, the Ota/Selmer/Sha inputs, and exceptional-prime finiteness.
- #Sha = 9t² (gcd(t, 30) = 1) is formally checked under its exact abstract hypotheses (A2 `order_nine_t_sq`: finite G, |G[2^∞]| = 1, |G[3^∞]| = 9, |G[5^∞]| = 1, every odd-primary order a square); it is NOT #Sha = 9 (countermodel `CM_order_441`, order 441).
- Q0 answered on the good ordinary tail by Codex Theorem O1 (`~/BSD_CODEX6_WC_INTEGRAL_DESCENT_2026-09-19/ORDINARY_CONVERSE_GATE.md`, sha256 `7a5ac582f42c8f7c…`): h_p = 0 ⟺ Sha[p^∞] = 0 at every good ordinary p ∉ S0 (a written deduction from Kim Thm 1.10 + Castella–Sano Thm B with the seed hypotheses checked; the positive-depth transfer and the supersingular primes are not covered). So WC's antecedent is FIN's ordinary vanishing tail in Ota coordinates; the formalizations close proof-engineering uncertainty only and do not reduce arithmetic difficulty.
- This does NOT prove FIN, J_E ≠ 0 or uniform prime support, and it does not show that WC is easier than FIN.

## 6. Canonical endgame and coverage update

With the retained primary results and finite-Sha square order, `Sha finite and #Sha < 441 => #Sha=9`. The stronger usable hypothesis `#Sha[n] < 441 for every positive n` proves finiteness too, by the cofinal chain Sha[m!]. See the [written proof](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/EXACT_ENDGAMES.md). Neither estimate is proved for this seed, and both are equivalent to order nine under the retained inputs. This is not established easier mathematics.

Direct global bounds are admissible without a displayed finite/tail partition. Partition-based routes must cover the infinite supersingular set and full primary depths. Finite prime support alone does not imply FIN. The [DM audit](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/00_VERDICT.md) supplies no valid uniform tail or finite exceptional set. The [canonical gate](/Users/bsm/BSD_CODEX6_CANONICAL_RESEARCH_GATE_2026-09-19/CANONICAL_RESEARCH_GATE.md) governs every proposed successor.
