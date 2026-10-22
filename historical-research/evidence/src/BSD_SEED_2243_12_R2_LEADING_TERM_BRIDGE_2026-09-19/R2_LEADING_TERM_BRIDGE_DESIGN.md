# R2_LEADING_TERM_BRIDGE_DESIGN — seed (2243,12), 2026-09-19 (35-minute design session)

Fixed frame: FULL BSD(E) = RANK + FIN + FORMULA; RANK done. **Design assumption for this file only: FIN holds with #Sha = 9**
(so far proved: Sha[2^∞] = 0, Sha[3^∞] ≅ (Z/3)² with R1/R2 carried, Sha[5^∞] = 0). Then FORMULA ⟺ q_∞ = 36, where
q_∞ := L″(E,1)/(2Ω_E·Reg(E)), L^{alg} := #Sha·∏c/#tors² = 9·16/4 = 36, ω = P₁∧P₂.
No computation was run. No novelty claim. Nothing merged. Labels: PROVED / CONDITIONAL / OPEN as in the master hand-off.
Sources used: BKS I (arXiv:1910.07404: Prop 2.6, Conj 4.9, Thm 1.9, Cor 1.11, Thm 1.14), BKS II (2103.11535: Def 4.3, Prop 4.4,
Thm 4.6, §5.5–5.6), Ota (Thm 5.17, 6.4), the LINE hostile audit, F4, the sealed p = 3 and p = 5 certificates.

## 0. The three scalars (this is the whole structure)
    q_∞ ∈ R          archimedean:   L″(E,1)/2 = q_∞·Ω·Reg_∞(ω^{⊗2})
    m_p ∈ Q_p        p-adic:        ψ_Q(z_Q^{(p)}) = m_p·Eul_Σ·ω^{⊗2}   (z_Q = Kato's determinantal zeta element, BKS II Def 4.3)
    L^{alg} = 36 ∈ Q  algebraic (given FIN)
    GPR_an(p)  (BKS Conj 3.1):  m_p = ι_p(q_∞), R^{Boc} ≠ 0          GPR_alg(p) (BKS II Conj 3.4):  m_p = L^{alg}
    FORMULA:  q_∞ = L^{alg}.        Any two of {GPR_an(p), GPR_alg(p), FORMULA} imply the third (for one p and one embedding ι_p: R → C_p).

## 1. Exact candidate statements
**T0 (archimedean denominator theorem).** There is an explicit integer D_E ≥ 1 with D_E·q_∞ ∈ Z, and
 (i) D_E < 1.6·10¹⁴ if one uses the CERTIFIED_NUMERIC value q_∞ = 36 ± 3·10⁻¹⁵, or
 (ii) D_E ≤ 86 if one uses only the present RIGOROUS Arb ball (L″/2 ∈ [35.929604, 35.941023] gives |q_∞ − 36| < 0.0058),
 together with rigorous enclosures of Ω (available, Arb) and Reg (NOT yet an Arb enclosure). Then q_∞ = 36.
**T1 (rank-two universal leading term; = tame LINE).** There is m_E ∈ Q^× with δ_n = m_E·ρ_n for every prime p ≥ 5, p ∤ N and every
 core pair n of every level p^k (notation of the LINE audit: δ_n the multilinear Mazur–Tate leading term, ρ_n = multilinear part of
 the corrected discriminant of ω^{⊗2}, ρ_n ≡ unit·det(loc)²).
**T2 (two-realization theorem).** There is m_E ∈ Q^× such that (p-adic) m_p = m_E for every p satisfying BKS II Hyp 2.2, and
 (archimedean) q_∞ = m_E. Equivalently: GPR_an(p) for all such p, with a rational scalar. [T2 ⟹ T1; T2 ⟹ q_∞ ∈ Q.]

## 2. Classification
| | vs BSD for the seed | circular? | what existing results already give | first unproved implication |
|---|---|---|---|---|
| T0 | WEAKER than FORMULA (FORMULA ⟹ T0 with D = 1); given FIN ∧ #Sha = 9 it is EQUIVALENT to FORMULA via numerics | no | nothing: F4 NOT_FOUND (no rationality, no denominator bound at a primitive double zero over Q) | any integral structure on the archimedean side at order 2 (rank 0: modular symbols; rank 1: Heegner index) |
| T1 | not comparable to FORMULA (purely algebraic/p-adic; NO archimedean content — audit item 9); implied by MT conjecture; after FIN ∧ IMC it says "u_p := m_p/36 ∈ Z_p^× is one rational number" | no (tame form) | Ota 5.17/6.4, normalisation N, BKS II linearised Thm 4.6; after FIN: m_p defined and v_p(m_p) = v_p(36) | p-independence of the UNIT part u_p |
| T2 | STRONGER than FORMULA-up-to-S₀-parts, weaker than BKS Conj 1.6 for all p with all its side statements; T2 ∧ (m_E explicit) ⟹ FORMULA | no | per-p: BKS I Thm 1.9 (generalised Rubin formula) turns GPR_an(p) into the order-2 "p-adic Beilinson formula" L_p^{(2)}/2 = ε_p·q_∞·Reg_p; proved only for r ≤ 1 | GPR_an(p) at even ONE prime |

## 3. Derivations attempted
- **T1 ⟹ T0: IMPOSSIBLE without an archimedean input.** Every object in T1 is built from twisted central VALUES and points; L″(E,1)
  does not occur (LINE audit item 9; F4 D2). PROVED negative (structural).
- **T0 ⟸ T1 ∧ GPR_an(p₀) for ONE p₀** (then ι(q_∞) = m_{p₀} = m_E ∈ Q, so q_∞ = m_E; if the proof of T1 exhibits m_E, numerics finish). CONDITIONAL.
- **T0 ⟸ GPR_an(p) for ALL good p ∉ S₀ ∧ FIN ∧ Kato's divisibility** (only the integrality half of the IMC is needed): one prime
  gives q_∞ ∈ Q (F4 CP-1: ι(q_∞) independent of ι); every prime gives v_p(q_∞) = v_p(m_p) ≥ 0. Then D_E is supported on
  S₀ = {2, 3, 19, 59, 487, 2243, 4547, 5843} (small/bad primes and the Hyp 2.2 failures). **Gap: nothing bounds the S₀-part of the
  denominator**, and an S₀-unit can be within 10⁻¹⁵ of 1 without exponent bounds. So this route needs extra statements at S₀
  (BKS Cor 1.11 covers non-split multiplicative p, so p = 3 and 5843 are in range of GPR; 2, 2243 (split), 4547 are not).
- **From ETNC / determinant lines:** rationality of the zeta element is Flach's Conj 2 (open at a central double zero); the p-adic
  lattices are known after FIN (BKS I Prop 2.6: BSD_p(E) ⟺ Z_p·η^{BSD} = #H²_tors·∧^rH¹). Identifying the archimedean zeta
  element with z_Q is GPR_an. Nothing weaker found.
- **From Mazur–Tate / Ota / Kato / heights:** all land in T1 or in valuations of m_p. None reaches q_∞.
- **One-prime route:** FORMULA ⟸ GPR_an(p₀) ∧ GPR_alg(p₀). But GIVEN GPR_an(p₀), GPR_alg(p₀) ⟺ FORMULA. So GPR_alg(p₀) cannot be
  an independent input unless the UNIT u_{p₀} = 1 is proved p-adically — no method in any rank determines such a unit
  (in rank 0 the exact formula comes from modular-symbol integrality + all p-parts; in rank 1 from Gross–Zagier + all p-parts).

## 4. What FIN unlocks, and what stays genuinely new
**FIN unlocks (all CONDITIONAL on FIN only, plus printed theorems):**
 1. m_p is DEFINED at every p satisfying BKS II Hyp 2.2 (ψ_Q needs T_pSha = 0). The determinant-line form RZ becomes meaningful,
    so "LINE ⟺ RZ" is valid AFTER FIN (it stays withdrawn as an unconditional statement).
 2. **Unit form (Lemma U, §9):** with the IMC at good ordinary p (Kato + Skinner–Urban; holds for the seed at p ≥ 5, and at 3 via
    Skinner Thm A as printed), z_Q is a Z_p-basis of the determinant lattice and so is η^{alg}; hence **m_p = 36·u_p, u_p ∈ Z_p^×**.
 3. Therefore, at every such p: p-adic BSD UP TO THE UNIT u_p (L_p^{(2)}/2 = ε_p·36·u_p·Reg_p when Reg_p ≠ 0 — PROVED non-zero for
    the seed at p = 5 and p = 3), and the Mazur–Tate leading-term formula in regime A up to the same u_p.
 4. BKS I Thm 1.3 / Thm 1.14 lose their "Sha finite" hypothesis; Thm 1.14's conclusion then needs GPR_an only.
**Still genuinely new after FIN:** (a) p-independence of u_p (T1); (b) u_p = 1 for even one p (exact p-adic BSD, = GPR_alg);
 (c) ANY archimedean statement: GPR_an at one prime, rationality of q_∞, T0. FIN determines VALUATIONS; every open statement
 is about UNIT PARTS or about the real number q_∞. The bridge does NOT collapse after FIN.

## 5. Can the m_p reconstruct m_E once FIN is known?
No. After FIN ∧ IMC each m_p = 36·u_p with u_p an unknown p-adic unit. (i) For any finite set of primes CRT supplies a rational
with those residues, so finitely many digits never establish rationality; (ii) if T1 held, m_E/36 would be a rational number
that is a unit at every good ordinary p, i.e. supported on {±1, 2, 3, 19, 59, 487, bad primes, supersingular primes} — still not
determined by finite data without a height bound. What finite data CAN do is refute: the first digit u_p ≡ 1 (mod p) is
testable from sealed data (p = 5: a_{2,2}, ε₅ ≡ 1, Reg_γ ≡ 21 mod 25, 36 ≡ 1), but the test is currently blocked by one
normalisation unknown: the 2-power k = v₂(c_E) in the modular parametrisation (the p = 5 certificate lists the residue as
2^k-dependent: 1, 2, 4, 3, … for k = 0, 1, 2, 3, …). See Lemma K in §9.

## 6. Statements weaker than an order-two Gross–Zagier formula that would still suffice
 W1. T0 itself (bounded denominator; no cycle, no formula). Sufficient given FIN. Status OPEN.
 W2. "Comparison of two regulators": for ONE good ordinary p₀ with Reg_{p₀} ≠ 0 (e.g. p₀ = 5),
        [L″(E,1)/2]/(Ω·Reg_∞)  =  ι⁻¹( [L_{p₀}^{(2)}(E)/2]/(ε_{p₀}·Reg_{p₀}) ).
     This is GPR_an(p₀) rewritten by BKS I Thm 1.9/Cor 1.11. It involves no new geometric object, only the two leading terms and
     the two regulators of the SAME ω^{⊗2}. It gives FORMULA only together with u_{p₀} = 1 (or T1 with explicit m_E).
 W3. Rationality of q_∞ alone is NOT sufficient (F4 §1); algebraicity even less.
 W4. Determinant-line equality at all p (ETNC_p ∀p) is sufficient only with rationality first; = BSD.
 Ranking by logical strength: order-2 GZ ⟹ T0 ⟹ FORMULA (given FIN);  GPR_an(∀p) + S₀-control ⟹ T0;  W2 alone does not.

## 7. Decomposition of the missing theorem (not stopping at "higher Gross–Zagier is missing")
The missing node is an ARCHIMEDEAN ORDER-TWO RECIPROCITY. Pieces, each stated so it can be attacked or refuted:
 M2.a  (analytic, provable) Rankin–Selberg identity differentiated twice at the centre: for a Dirichlet χ with L(E,χ,1) ≠ 0,
       L″(f,1)·L(f,χ̄,1) = C(χ)·⟨ f , E^{(2)}·E_χ ⟩, E^{(2)} := ∂_s²E_s at the centre. The identity in s is classical; what is
       missing is an ARITHMETIC description of E^{(2)} (a "second Kronecker limit formula": first order gives log|Siegel units| =
       Beilinson's regulator; second order is an iterated-Eisenstein / depth-2 object). Kontsevich's remark (F4) is exactly that
       this integrand is not the logarithm of an algebraic function.
 M2.b  (p-adic mirror, mostly PROVED) the second Taylor coefficient of Perrin-Riou's big logarithm of Kato's class = ε_p·m_p·Reg_p
       (BKS I Thm 1.9 + FIN). So the p-adic side of W2 is in hand; only the archimedean side lacks an object.
 M2.c  (comparison) a depth-2 "regulator" on a motivic object of the modular curve with BOTH realisations: archimedean = the
       pairing in M2.a, p-adic = M2.b. For depth 1 this object is Beilinson's element in K₂; for depth 2 no candidate is in the
       project's inventory. THIS is the single major missing construction; M2.a is its first concrete lemma.
 M1    (unit) u_{p₀} = 1. Equivalent to FORMULA once M2 holds at p₀; no independent route known in any rank.
 T0-direct  an integral structure making D_E·q_∞ ∈ Z: would follow from M2.c with integral coefficients at all p ∉ S₀ plus S₀-control.

## 8. Theorem DAG
PROVED: RANK · Sha[2^∞], Sha[3^∞] (R1/R2), Sha[5^∞] · Reg₅ ≠ 0, Reg₃ ≠ 0 (finite precision suffices) · IMC at good ordinary p ≥ 5 for
 the seed (Kato + SU) · existence of z_Q under Hyp 2.2 (BKS II Lemma 4.2) · linearised Thm 4.6 · BKS I Thm 1.9 · Ota 5.17/6.4 · normalisation N ·
 L″(E,1)/2 ∈ [35.929604, 35.941023] (Arb).
CONDITIONALLY AVAILABLE (given FIN): m_p defined · Lemma U: m_p = 36·u_p, u_p ∈ Z_p^× · p-adic BSD up to u_p at 3, 5 and every good
 ordinary p with Reg_p ≠ 0 · MT leading terms up to u_p (regime A) · LINE ⟺ RZ · GPR_an(p) ⟹ v_p(q_∞) = 0.
GENUINELY MISSING: M2 (archimedean order-two reciprocity; first lemma M2.a's arithmetic form) · M1 (u_p = 1) or T1 with explicit m_E ·
 S₀-denominator control · hence T0 and FORMULA.
    FORMULA ⟸ FIN ∧ T0 ∧ numerics          T0 ⟸ {M2 at all p ∉ S₀} ∧ Kato ∧ FIN ∧ S₀-control     or   T0 ⟸ order-2 GZ
    FORMULA ⟸ FIN ∧ M2(p₀) ∧ M1(p₀)        M1(p₀) ⟸ T1 with m_E = 36                              T1 ⟸ MT conjecture

## 9. ONE first lemma worth trying immediately
**Lemma U (unit form of the rank-two zeta element after FIN).** Let p ≥ 5 be good ordinary for E, satisfying BKS II Hyp 2.2, with
Sha[p^∞] finite. Then z_Q^{(p)} = u_p·η^{alg} with u_p ∈ Z_p^×; consequently κ_p = u_p·L^{alg}_Σ·R^{Boc}, θ_{F,S} = ±u_p·L^{alg}_S·R_F for
every F in regime A, and (Reg_p ≠ 0) L_p^{(2)}(E)/2 = ε_p·u_p·L^{alg}·Reg_p.
 Proof plan (source reading only, no computation): (i) IMC ⟺ z_{Q_∞} is a Λ-basis of det⁻¹RΓ(Z_Σ,T_{Q_∞}) (BKS I §3–4 / Kataoka);
 (ii) bases descend along Λ → Z_p (perfect complexes, base change); (iii) η^{alg} generates the Z_p-lattice (BKS I Prop 2.6 read
 with L^{alg} in place of L^{an}; Euler-characteristic computation); (iv) linearity as in BKS II §5.5–5.6.
 Why this one: it is provable now; it converts every remaining rank-two question at p into a statement about ONE p-adic unit
 (T1 ⟺ u_p rational and constant; M1 ⟺ u_p = 1; M2 ⟺ ι(q_∞) = 36u_p); it holds for every E/Q of any rank r ≥ 1 with the same
 proof (generalizable); and it yields the first falsifiable numerical consequence of the whole picture from SEALED data:
**Companion Lemma K (normalisation; seed-specific; no computation beyond reading the sealed symbol tables).** Determine k = v₂(c_E)
 for the parametrisation used to normalise L_p(E) (all 192 rigorous symbols are integers in the ω₁ normalisation with gcd 1;
 c_E ∣ 2⁹). Then u₅ mod 5 is read off from the sealed p = 5 certificate: u₅ ≡ 1 (mod 5) ⟺ 2^k-normalised a_{2,2} ≡ 36·Reg_γ·ε₅ ≡ 1.
 A residue ≠ 1 would refute exact 5-adic BSD with #Sha = 9 (hence BSD ∧ GPR); a residue 1 proves nothing but fixes conventions
 for every later test.

## 10. Classification returned
**R2_BRIDGE_ONE_MAJOR_THEOREM_MISSING.** After FIN everything on the p-adic/algebraic side reduces to explicit statements about
the units u_p (Lemma U is attackable now), but FORMULA needs an archimedean order-two reciprocity (M2) — or T0 directly — for
which the project holds no object; its first concrete lemma is the arithmetic form of M2.a. The architecture is not circular
(provided GPR_alg(p₀) is never used as an independent input), and it does not collapse after FIN.

## 11. CORRECTIONS from the hostile audit (`LEMMA_U_AND_P5_UNIT_AUDIT.md`, 2026-09-19) — these govern
- Lemma U is NOT new work: it is BKS I Theorem 7.3 (Hyp 2.2 + IMC equality ⟹ κ_∞ = u·L^{alg}_S·R^{Boc}, u ∈ Z_p^×), needing only Sha[p^∞] finite — so at p = 5 and p = 3 no global FIN assumption.
- §5 and §9 "Lemma K": WITHDRAWN. k = v₂(c_E) does not enter u₅; the relevant normalisation is L-values over the Néron period Ω⁺ = 2ω₁. Sealed data give u₅ ≡ 1 (mod 5) (m₅ ≡ 1 with no FIN assumption), one digit, already noted by Lane 2 at numeric grade; conditional on an unread unit-level normalisation match BKS ↔ SW.
- Classification unchanged: R2_BRIDGE_ONE_MAJOR_THEOREM_MISSING; first remaining unproved arrow: ι_p(q_∞) = m_p at one prime.
- (later) T0(ii): the threshold is **D_E ≤ 174**, not 86 (criterion D·δ < 1; audit file §E.1); T0(i): D < 3.3·10¹⁴ for q_∞ (1.6·10¹⁴ is the bound for L″/(Ω·Reg)). Two-level frontier: minimal target = rationality + small denominator; GPR_an is a stronger candidate route (audit §E.5).
