# LINE_HOSTILE_AUDIT — hostile referee ledger for LINE/RZ and Theorem C (seed (2243,12))

Referee session 2026-09-19 (fresh task; same model family as the author — see memory note "same-session re-derivation repeats
slips": every load-bearing claim below is re-read in the primary text, not taken from the target file).
Target: `~/BSD_SEED_2243_12_RANK2_GLOBAL_OBJECT_2026-09-18/RANK2_GLOBAL_OBJECT_COMPOSITION.md` (sha256 6b347683…), brief
`HOSTILE_REFEREE_PROMPT.md` (sha256 3938191f…). Read-only outside this folder. Nothing merged. Append-only ledger.

Severity labels: FATAL / REPAIRABLE / COSMETIC / UNVERIFIED. Priority order of the operator brief; STOP at first FATAL.

## ITEM 1 — definition of m_p (13:40Z). RESULT: SOUND, with an exact scope; one REPAIRABLE wording defect (RZ form).

Read in BKS II (arXiv:2103.11535, local txt; line numbers of the txt):
- l. 713–797 (§4.2, Lemma 4.2 (Kataoka), text after it): z_{F∞} = (z_{M,Σ})_M ∈ H¹(Z_Σ,T_{F∞}) is Kato's norm-compatible element;
  π_{F∞}: det⁻¹_Λ RΓ(Z_Σ,T_{F∞}) → H¹(Z_Σ,T_{F∞}) is built from SS₁ ≅ KS₁ (BSS, Burns–Sano); z_{F∞} ∈ im π_{F∞} (Kataoka) and
  π_{F∞} is injective because Ann(z_{F∞}) = 0. Hence the determinantal element **z_{F∞} exists and is unique under Hyp 2.2 alone**;
  Def 4.3: z_Q := its projection. No Conj 3.4, no BSD, no Sha hypothesis enters the EXISTENCE of z_Q ∈ det⁻¹_{Z_p}RΓ(Z_Σ,T).
- l. 491–495: "(11) E(Q)⊗Z_p ≃ H¹(Z_Σ,T)" is asserted from r > 0 and "H¹(Z_Σ,V) = H¹_f(Q,V)" with a pointer to BKS I (2.2.1).
  Referee check: H¹_f(Q,T) = lim Sel_{p^n} sits in 0 → E(Q)⊗Z_p → H¹_f(Q,T) → T_pSha → 0, so (11) holds **iff T_pSha = 0, i.e. iff
  Sha[p^∞] is finite** (local quotients H¹/H¹_f are torsion-free, so no further index). (13), (16), ψ_Q (l. 1239–1260) need
  exactly the same thing: rank H¹(Z_Σ,T) = r, rank H²(Z_Σ,T) = r − 1.
- §2.1 (l. 237–238) assumes ALL of Sha(E/Q) finite, but that is used only to write L^{alg} (l. 247–250, (2), (17)).
  Nothing in Def 4.3, (11), (13), (16), ψ_Q uses more than Sha[p^∞] finite.

Conclusion. For a prime p and a field F (F = Q allowed) satisfying Hyp 2.2, and **under the single extra hypothesis
"Sha(E/Q)[p^∞] finite"**, the scalar m_p(Σ) ∈ Q_p with ψ_Q(z_{Q,Σ}) = m_p(Σ)·(∏_{ℓ∈Σ}#E^{ns}(F_ℓ)/ℓ)·(x⊗x) exists and is unique,
because the target of ψ_Q is a Q_p-line. Not circular with respect to Conj 3.4 / BSD / global finiteness. 

Defects found:
 (1a) REPAIRABLE. The determinant-line form "RZ" (z_Q^{(p)} is the realisation of m·ω^{⊗2} for every good p ≥ 5) is only MEANINGFUL
      at p once Sha[p^∞] is known finite. As a standalone statement over all p it presupposes part (b) of Theorem C. The target
      file's "LINE ⟺ RZ" (§9.2, §9.1) is therefore NOT an unconditional equivalence. Only the TAME form of LINE is
      unconditionally meaningful, and only the tame form is used in Theorem C. RZ must be demoted to "a posteriori reformulation".
 (1b) REPAIRABLE/UNVERIFIED. z_Q = z_{Q,Σ} depends on Σ = {ℓ | pmN}, hence on F. Independence of m_p(Σ) from Σ is not proved in the
      text read. It follows IF the regulator is primitive along some tower (compare θ_{F′,S′} ↦ θ_{F,S}: (m_p(Σ′) − m_p(Σ))·Eul_S·R_F = 0),
      or from the Euler-factor relation for Kato's elements under enlargement of Σ; neither is written in the target.
 (1c) SCOPE. Hyp 2.2(iii) excludes p | ∏_{ℓ|N}#E^{ns}(F_ℓ) (for the seed: the prime factors ≥ 5 of 2243∓1, 5843∓1, and 4547) and
      requires p ∤ #E(F_ℓ) for ℓ | m (regime A only). So the BKS-II definition of m_p is NOT available at every p ≥ 5, p ∤ N.
      (Computed below in ITEM 4 run.) This does not touch Theorem C, which never uses m_p.

## ITEM 2 — linearity (13:50Z). RESULT: CONFIRMED IN PRINT.

Proofs read (not only statements): Prop 5.1 (l. 949–975), Prop 5.2 + proof (l. 1026–1113), Cor 5.3 (l. 1135–1136),
§5.3 (l. 1137–1171), Prop 5.4 statement (l. 1173–1205; proof is a citation of [11, Th 3.3.7]), Lemma 5.5 + proof (l. 1236–1300),
§5.5 (l. 1302–1315), §5.6 (l. 1317–1336).
- (27): θ_{F,S} = (Reg_F ∘ π_{Q,f} ∘ ν_f ∘ φ_F)(z_F) in I^r/I^{r+1} is derived from Cor 5.3 + Prop 5.4(ii) ONLY. No Conj 3.4.
- (25): (ν_f ∘ φ_F)(z_F) = φ_Q(z_Q). Unconditional.
- So θ_{F,S} ≡ (Reg_F ∘ π_{Q,f} ∘ φ_Q)(z_Q), a Z_p-LINEAR function of z_Q. η^{alg} enters only through the hypothesis z_Q = η^{alg}.
- **BKS II use the linearised statement themselves**: §5.6, l. 1335–1336: "it therefore follows that z_Q = u·η^{alg}. The latter
  equality then combines with the argument of §5.5 to imply that the equality …[holds after multiplying by u]".
  So "the proof uses L^{alg} only through linearity" is not my inference; it is how the authors prove Cor 1.2.
- Hidden hypothesis inherited: Prop 5.4 uses H¹_f(Q,T) ≅ Z_p⊗E(Q) (l. 1155), i.e. Sha[p^∞] finite — same scope as ITEM 1.
Consequence (theorem-level, under Hyp 2.2 + Sha[p^∞] finite): θ_{F,S} = (−1)^{ν(m)}·m_p(Σ)·(∏_{ℓ∈S}#E^{ns}(F_ℓ)/ℓ)·R_F in I^r/I^{r+1}.
This is the target's (L1) in REGIME A. Status: PROVED modulo (1b). The target's §5.1 regime-K derivation is NOT covered by this.

## ITEM 3 — Mazur–Tate normalisation (N) (14:35Z). RESULT: (N) IS CORRECT (derived + numerically confirmed); no extra cross terms.

Source for MT's definitions: the original Duke paper is not open access and was NOT read. I read instead Tan, Ann. Inst. Fourier 45
(1995) 317–374 (Numdam, open access; scanned pages read visually), §2.1–2.3, §3.1, which restates MT's construction with
equation-level detail: local trivialisations (L1)–(L5) p. 330, global S-pairing Def 2.6, disc_S p. 339, maps Z_{T,S}, U_{S,T}
(33)–(35), j_S Def 2.14, corrected discriminant (36), compatibility (38), φ_S (43), Conjecture 1 (44). Cross-checked against
Ota Conj 2.4 and BKS II (7)–(9) (both local primary texts). UNVERIFIED residue: that Tan's (35)–(36) equal MT's (2.6), (3.1)
verbatim (Tan says "recall … see [MT2]"; Ota's Conj 2.4 has the same alternating shape with μ_{S,T}, d_T, J_T).

**3.1 The T ≠ S terms carry no multilinear component.** (35): U_{S,T}∘Z_{T,S} = ∏_{v∈S−T}(q_v−1)·id, and Z_{T,S} is onto, so
U_{S,T}(t) = ∏_{v∈S−T}(q_v − 1)·(any lift of t). Lifting through the splitting C_T ↪ C_S (2 inverted) gives
U_{S,T}(Sym_r(C_T)) ⊂ ∏(q_v−1)·Sym_r(C_T) ⊂ Sym_r(C_S): no component involving C_v, v ∈ S−T. For S = {ℓ1,ℓ2}, r = 2:
   𝒟_S = 0 [T=∅: Sym_2 of the trivial group] − (ℓ2−1) j_{ℓ1} disc_{ℓ1} − (ℓ1−1) j_{ℓ2} disc_{ℓ2} + j_S disc_S,
the middle terms lying in Sym_2(G_{ℓ1}), Sym_2(G_{ℓ2}). **So the G_{ℓ1}⊗G_{ℓ2}-component of 𝒟_S is that of j_S·disc_S alone.**
Independent θ-side confirmation (my computation from the interpolation formulas): the modular-symbol element (Ota Def 2.1,
imprimitive factor a_ℓ − χ(ℓ) − χ̄(ℓ)) and Darmon's element used in BKS II (7) (factor a_ℓ − ℓχ(ℓ) − χ̄(ℓ)) differ by
N_ℓ·Fr_ℓ·θ_{S/ℓ}-type terms; N_ℓ ≡ |G_ℓ| mod I_{G_ℓ} and θ_{S/ℓ} ∈ I², so the difference is |G_ℓ|θ̃_{S/ℓ} ∈ gr²(G_{S/ℓ}) mod I³:
diagonal only. Both sides of the conjecture therefore have the same multilinear component in MT's and in Darmon's/BKS's form.
[Side remark: the target's §0/§1 worry about a_ℓ − 2 versus #E(F_ℓ) is exactly this difference between the two elements.]

**3.2 Local lemma (DERIVED here).** ℓ good, n = #E(F_ℓ), a, a′ ∈ E(Q) with a′ ∈ E⁰ everywhere, R ∈ E(Q) with R, a+R ≢ O mod ℓ.
Take D_a = (a+R) − (R). The tame splitting (L4) is trivial on (D_a, (b)−(O)) for b ∈ E_1(Q_ℓ) because a local equation of D_a is a
unit on the residue disc of O. Hence ⟨a,b⟩^{(ℓ)} = ∏_{q≠ℓ} q^{[D_a,(b)−(O)]_q} mod ℓ = d(a+R−b)d(R)/(d(a+R)d(R−b)) mod ℓ  (d = √denominator of x).
For b = n a′ write (na′) − (O) = n((a′)−(O)) + div(g). Then ⟨a, na′⟩^{(ℓ)} ≡ [g(a+R)/g(R)] mod (F_ℓ^×)^n, and ḡ = 1/f_{n,ā′} is the
inverse Miller function of the n-torsion point ā′. Therefore
      **⟨a, n a′⟩^{(ℓ)} = τ_n(ā′, ā)^{-1}  (Tate–Lichtenbaum pairing E(F_ℓ)[n] × E(F_ℓ)/n → F_ℓ^×/n), a PERFECT pairing.**
With E(F_ℓ)⊗Z_p cyclic: ⟨a, n a′⟩^{(ℓ)} ⊗ Z_p = c_ℓ·π_ℓ(a)π_ℓ(a′)·g_ℓ, c_ℓ a unit.

**3.3 The determinant.** If M_n = (π_{ℓi}(P_j)) is invertible mod p and v_p(#E(F_{ℓi})) = k for i = 1,2, then B_S⊗Z_p = ker π = p^k(A⊗Z_p),
b_j = N_0 P_j (v_p(N_0) = k) is a Z_(p)-basis, the Gram matrix is u_1 M^T diag(c_1 g_1, c_2 g_2) M (u_i = N_0/n_{ℓi} units), and the
g_1⊗g_2-coefficient of its determinant is u_1u_2c_1c_2[(x_{11}x_{22})² + (x_{21}x_{12})² − 2x_{11}x_{12}x_{21}x_{22}] = unit·det(M_n)².
j_S and |A_tor||B_tor| are p-units (π onto; p ∤ 2). **(N) holds exactly as the target states it**, under the explicit side
conditions: p ∤ 2·Tam·#tors, E(F_{ℓi})[p^∞] cyclic of the SAME order p^k, p^k | ℓ_i − 1, and the pairing read mod p^k.

**3.4 Numerical confirmation** (`runs/n_check.gp/.out`, `runs/n_check2.gp/.out`; PARI 2.17.3, exact arithmetic):
 - TEST 1 (regime A, ℓ=11, p=5): the denominator formula gives ⟨Q1,Q2⟩ = ⟨Q2,Q1⟩ = 4, ⟨Q1,Q1⟩ = 3, ⟨Q2,Q2⟩ = 1, identical to the
   design lane's B(Q1,Q2) = 4, 2h(Q1) = 3, 2h(Q2) = 1 from h = dlog(t/d). Two independent formulas for the MT pairing agree; the
   design lane's "heuristic normalisation" flag can be lifted (up to the universal sign/factor 2 conventions).
 - TEST 2 (regime K, ℓ=31, p=5, n=40, π(P1)=π(P2)=2): ⟨a, nP_i⟩ = 3,3,1,0 for a = P1, P2, P1+P2, P1−P2 (both i), and
   π(a)π(P_i) = 4,4,3,0: ratio c_31 = 2 in all 8 cases, including the predicted zero. Matches 3.2.
 - ℓ = 181 and ℓ = 151 (v_5(ℓ−1) = 2 > v_5(n) = 1) running in background (`runs/n_check3`); appended when done.
Bad-prime data computed on the way: a_3 = −1, a_2243 = +1, a_5843 = −1, so ∏_{ℓ|N}#E^{ns}(F_ℓ) = 2·4·2242·4547·5844 and BKS II
Hyp 2.2(iii) excludes p ∈ {19, 59, 487} (and 4547) for the seed — feeds ITEM 1(1c).
 - (appended 15:05Z) `runs/n_check3.out`: ℓ=181 (n=180, π(P1)=2, π(P2)=0): all 8 values = 1·π(a)π(P_i) (4,0,4,4 | 0,0,0,0);
   ℓ=151 (n=160, v_5(ℓ−1)=2 > v_5(n)=1, π(P1)=0, π(P2)=2): all 8 values = 1·π(a)π(P_i) (0,0,0,0 | 0,4,4,1).
   Total: 24/24 values fit c_ℓ·π_ℓ(a)π_ℓ(a′) with units c_31 = 2, c_181 = 1, c_151 = 1. For n = 31·181: M = [[2,2],[2,0]],
   det M = −4 ≡ 1 (5), predicted multilinear component c_31c_181·det² = 2 ≠ 0. (N) confirmed on a genuine core pair.

## ITEM 4 — Chebotarev / existence of core pairs at every level p^k (15:10Z). RESULT: TRUE, but the target's one-line proof is incomplete (REPAIRABLE).

What is needed for each k: primes ℓ1, ℓ2 ∤ pN with (i) ℓ_i ≡ 1 (p^k); (ii) E(F_{ℓi})[p^∞] cyclic of order EXACTLY p^k (so that
ker π = p^k(A⊗Z_p) and (N)'s side conditions hold; this is a condition on Frob mod p^{k+1}: v_p det(Fr−1) = k, e.g.
Fr ~ [[1,1],[p^k,1]]); (iii) (π_{ℓi}(P_j)) invertible mod p. Inputs:
 - Image of ρ_p is all of GL_2(Z_p): mod-p surjectivity + p ≥ 5 (Serre's lemma: a closed subgroup of SL_2(Z_p), p ≥ 5, onto
   SL_2(F_p) is everything) + det = cyclotomic. **So mod-p surjectivity DOES suffice for every p^k, but only via this lemma
   and only for p ≥ 5** — the target did not say so. (Ota's Thm 5.17 also assumes p-adic surjectivity; same remark.)
 - Kummer theory: Gal(L_1(p^{-1}P1,p^{-1}P2)/L_1) ≅ E[p]² (P1,P2 independent in E(Q)/p since they are a Z-basis mod torsion and
   p ∤ #tors; H¹(GL_2(F_p),E[p]) = 0). π_ℓ(P_j) is the class of κ_{P_j}(Fr_ℓ) in E[p]/(Fr_ℓ−1)E[p].
 - Linear disjointness over L_1 of L_{k+1} and the mod-p Kummer field: Gal(L_{k+1}/L_1) has only ad/trivial constituents on which
   −I acts trivially, E[p]² is −I-odd. So the conditions (i)–(ii) and (iii) can be imposed simultaneously; take (π(P1),π(P2)) =
   (1,0) at ℓ1 and (0,1) at ℓ2.
 - Admissibility: Ota's p-adic theorems (5.17, 6.4 with R = Z_(p)) need only E(F_ℓ)[p] cyclic — true here (Fr ≠ 1 on E[p]).
Defect (4a) REPAIRABLE: the target's 𝒮 demands E(F_ℓ)[p′] cyclic for ALL p′ ≥ 5 and its Theorem C proof applies Chebotarev at p
only, so it never shows its core n lies in 𝒮. Repair: state LINE prime-by-prime (for each p, over S admissible AT p, with a
COMMON pair (a,b)); θ_S ∈ Z_p⊗I_S² is then Ota Thm 5.17. (Alternative repair by a density argument over all p′ is possible but
needs a uniform tail bound; not needed.)

## ITEM 5 — the infinite-Sha step (15:15Z). RESULT: SOUND. Better reference than the target's.

Arrow by arrow:
 1. Sha[p^∞] infinite ⇒ r_{p^∞} := corank Sel_{p^∞} ≥ 3. ✓ (rank 2 + corank Sha ≥ 1.)
 2. p-parity (Dokchitser–Dokchitser; cited by Ota as [8, Thm 1.4]): (−1)^{r_{p^∞}} = w(E) = +1 ⇒ r_{p^∞} ≥ 4. ✓ Needs only w = +1,
    which is a root-number fact, not the certified analytic rank.
 3. **Ota Thm 5.17 (read in the text, l. 2069–2089): p ∤ 6N·#E(F_p)·∏m_ℓ, ρ_p onto GL_2(Z_p), S squarefree, good primes with
    E(F_ℓ)[p] ≅ Z/p or 0 ⇒ θ_S ∈ I^{min{r_{p^∞},p}} ⊂ Z_p[G_S].** With r_{p^∞} ≥ 4, p ≥ 5: θ_S ∈ I⁴ ⊂ I³. The target quoted the
    weaker intro formula (1.2) (exponent min{r_{p^∞}−1,p}) plus parity; the conclusion I³ is the same. Exponent check: p = 5
    gives min(4,5) = 4 ✓; no small-p loss for p ≥ 5.
 4. Scope of S: every squarefree S admissible at p, in particular every core n of ITEM 4 ✓ (not a restricted set).
 5. Hypotheses at the seed: Tam = 16, #E(F_p) even so p ∤ #E(F_p) for p ≥ 7 and #E(F_5) = 8 ✓; all p ≥ 5, p ∤ N qualify.
 6. mod p → mod p^k: (G_{ℓ1}⊗G_{ℓ2})⊗Z_p ≅ Z/p^{min(e_1,e_2)}, e_i = v_p(ℓ_i−1) ≥ k. By (N) the multilinear component of the
    regulator side is ≢ 0 mod p, hence a GENERATOR of this cyclic group. LINE gives a·(generator) = b·0 = 0, so
    p^{min(e_1,e_2)} | a, in particular p^k | a. All k ⇒ a = 0. ✓ No gap.

## ITEM 6 — the Sha[p] = 0 step (15:18Z). RESULT: SOUND.

 - p ∤ b: if p | b then a·(generator) ≡ 0 mod p forces p | a, contradicting gcd(a,b) = 1 ✓.
 - p ∤ a ⇒ δ_n ≡ (a/b)·unit·det(M_n)² ≢ 0 mod p ⇒ θ̃_n^{(p)} ≠ 0 in Z/p ⊗ I²/I³ (a non-zero component).
 - Ota Thm 6.4 (statement l. 2146–2156 and PROOF l. 2162–2238 read): with R := Z_(p) the only non-invertible prime is p, so
   "S as in Thm 6.1" means E(F_ℓ)[p] cyclic; all ℓ | n are ≡ 1 (p), so S_1 = n, S_2 = 1. Conclusion: **Sha(E/Q)[p] = 0**, p ∤ J_n.
   The proof is unconditional (Cor 4.19; no IMC, no finiteness, no ordinarity).
 - Sha[p] = 0 ⇒ Sha[p^∞] = 0: Sha[p^∞] is a p-primary torsion group; a non-zero element of order p^j gives the non-zero element
   p^{j−1}x of Sha[p]. In particular the divisible part is 0 as well (Q_p/Z_p has p-torsion). ✓ Not merely "no p-torsion".

## ITEM 7 — circularity (15:20Z). RESULT: tame LINE is NOT circular; the RZ form IS (see 1a).

Tame LINE mentions only θ_S (modular symbols), the MT corrected discriminant of P1,P2 (heights and reductions of points) and
two integers. It is meaningful whatever Sha is, because θ_S ∈ Z_p⊗I_S² holds unconditionally (Ota 5.17 with r_{p^∞} ≥ 2).
It IMPLIES finiteness at good p (acceptable). The determinant-line form RZ needs ψ_Q, hence (11), hence Sha[p^∞] finite,
BEFORE it can be stated at p: as an all-p statement it presupposes what Theorem C(b) concludes (not acceptable as a primary
formulation). The target's "LINE ⟺ RZ" must be withdrawn; what survives is: for p satisfying Hyp 2.2 with Sha[p^∞] finite,
RZ_p ⇒ (regime-A components of LINE at p) by the linearised Thm 4.6; the converse needs a primitive R_F (the unproved Lemma P).

## ITEM 8 — what LINE omits (15:22Z).

 - vs Mazur–Tate (Tan Conj 1 / Ota Conj 2.4), p-parts at p ≥ 5, p ∤ N: MT = [Sha finite] ∧ [θ̃_S = |Sha|·φ_S·d(𝒟_S) ∀S]. LINE replaces
   |Sha| by an unspecified non-zero rational and asserts nothing at inverted primes or about finiteness. MT ⇒ LINE (a = |Sha|,
   b = 1) is immediate. Converse: given LINE, the IMC at good ordinary p (known for the seed) pins v_p(a/b) = v_p(#Sha[p^∞]), so
   LINE = "MT up to a rational constant supported on {2, 3, p | N, supersingular p}" plus nothing at the inverted primes. I
   cannot PROVE non-equivalence (both are open); "strictly weaker" should read "formally weaker; converse not known".
 - vs BKS II Conj 3.4 at all p: omits R^{Boc} ≠ 0 (a Schneider-type non-degeneracy of the cyclotomic Bockstein regulator), the
   value L^{alg}, and the standing assumption that all of Sha is finite (§2.1).
 - vs BKS Conj 3.1 / GPR: omits every archimedean ingredient (L^{an}_Σ ∈ C_p via a fixed embedding R ↪ C_p).

## ITEM 9 — Wall 2 (15:24Z). RESULT: NOT TOUCHED.

LINE involves only twisted central VALUES (through θ_S) and points. L″(E,1) does not occur in it, in Theorem C, or in any of
Ota 5.17/6.4, BKS II §5. There is no non-conjectural implication from LINE to q_∞ = L″(E,1)/(2ΩReg): not rationality, not a
denominator bound, not a p-adic valuation. The target's conditional remark "LINE ∧ GPR(p_0) ⇒ q_∞ = m" is correct (κ = m_{p_0}·Eul_Σ·R^{Boc}
holds unconditionally by the diagram in Prop 4.4 + linearity; GPR then gives ι(q_∞) = m_{p_0}, and LINE makes it rational), but
GPR(p_0) is open for r = 2 and "with known value" overstates: LINE asserts existence of m, not its value.

## NARROW NOVELTY CHECK (15:26Z) — no claim of novelty is supported.
Checked: Ota (intro, §6; grep for "almost all / finitely many / converse": nothing), BKS II (§1–5; same grep: nothing), Tan
(intro, §2–3: his theorems go BSD ⇒ MT up to a constant, the opposite direction), one web query. Not re-read: Darmon 1992,
Bullach–Honnor 2511.07203, Mazur–Tate 1987 itself. Theorem C is a formal corollary of Ota Thm 5.17 + Thm 6.4 + the
Tate–Lichtenbaum description of the tame pairing once LINE is posited; MT's own conjecture already CONTAINS "Sha finite", so
"MT ⇒ FIN" is trivial and only the scalar-free version has content. Verdict: "not found in the sources read", nothing more.

---
# FINAL VERDICT (15:35Z): **LINE_THEOREM_C_PASS_WITH_CORRECTIONS**

No FATAL flaw in items 1–9. Theorem C is mathematically sound once LINE is stated in its tame, prime-by-prime form; the
normalisation (N) it relies on is correct. The corrections are about formulation and scope, and one of them changes what the
result MEANS (C5).

## Corrections (all REPAIRABLE)
C1. RZ (determinant-line form) is meaningful at p only if Sha[p^∞] is finite; "LINE ⟺ RZ" is withdrawn. Primary statement = tame LINE.
C2. m_p via BKS II exists only under Hyp 2.2 + Sha[p^∞] finite: regime A only, and NOT at p ∈ {19, 59, 487} for the seed
    (2243 split, 5843 non-split). Σ-independence of m_p(Σ) is unproved in the target. None of this is used by Theorem C.
C3. LINE must be quantified prime-by-prime over S admissible AT p with a common (a,b) (or the target must prove its core n are
    admissible at all p′). Cite Ota Thm 5.17 and Thm 6.4 with R = Z_(p), not "(1.2)" and "Thm 1.5".
C4. The Chebotarev step needs conditions mod p^{k+1}, the image GL_2(Z_p) (Serre's lemma, p ≥ 5) and disjointness of the Kummer and
    division towers (−I argument). True; not written in the target.
C5. **Interpretation.** Per prime, "LINE at p with p ∤ a" is EQUIVALENT (at good ordinary p, by Kim / Castella–Sano) to the existence
    of a Kurihara witness, i.e. to Sha[p] = 0: Theorem C is a thin wrapper around Ota 5.17 + 6.4. All of the content of LINE is
    the p-independence of the scalar, which is strictly MORE than Wall 1 needs (Wall 1's tail ⟺ v_p(m_p) = 0 for almost all p;
    LINE adds coherence of the unit parts, which Wall 1 never uses). LINE is a sufficient mechanism, not a reduction of Wall 1
    to something easier, and no finite computation can confirm it (the target says this itself in §6.5; it stands).
C6. "Strictly weaker than MT" → "formally weaker; converse not known" (ITEM 8). Novelty: not established (narrow check only).
C7. §5.1 of the target (regime-K rigidity sketch, assumes Sha[p^k] = 0) remains an unrefereed sketch; (L1) is PROVED only in regime A
    under Sha[p^∞] finite (linearised BKS II Thm 4.6 — which the authors themselves use in §5.6 with z_Q = u·η^{alg}).

## Strongest surviving theorem (corrected statement)
**Theorem C′.** E the seed; p ≥ 5 prime, p ∤ N. Call n = ℓ1ℓ2 a core pair of level p^k if ℓ_i ∤ pN, ℓ_i ≡ 1 (p^k), E(F_{ℓi})[p^∞] ≅ Z/p^k,
and (π_{ℓi}(P_j)) is invertible mod p. Let δ_n ∈ (G_{ℓ1}⊗G_{ℓ2})⊗Z_p be the multilinear component of the image of θ_n in Z_p⊗I_n²/I_n³
(defined unconditionally by Ota Thm 5.17) and ρ_n the multilinear component of φ_n·d(𝒟_n) (MT corrected discriminant of P1∧P2).
 (i) [PROVED here] core pairs exist at every level, and ρ_n ≡ unit·det(π_{ℓi}P_j)² mod p; in particular ρ_n generates (G_{ℓ1}⊗G_{ℓ2})⊗Z_p.
 (ii) [PROVED from Ota 5.17, 6.4] if coprime non-zero integers a, b satisfy b·δ_n = a·ρ_n for all core pairs of all levels at p, then
      p ∤ b, Sha(E/Q)[p^∞] is finite, and Sha(E/Q)[p^∞] = 0 when p ∤ a.
 (iii) Hence if one pair (a,b) works for every p ≥ 5, p ∤ N (= LINE restricted to core pairs), then Sha[p^∞] = 0 for all p ∤ 6Na and
      is finite for p | a, p ∤ 6N. Nothing is obtained at p ∈ {2, 3, 2243, 4547, 5843}.
Dependencies outside this audit: Ota's published theorems; p-parity; MT's construction as restated by Tan (Duke text unread).
