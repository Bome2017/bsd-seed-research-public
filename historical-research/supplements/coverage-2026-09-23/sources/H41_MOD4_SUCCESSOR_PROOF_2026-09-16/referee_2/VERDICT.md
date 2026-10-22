# Referee 2 — verdict on the H41 mod-4 successor proof, revision 1

- **Object:** `/Users/bsm/H41_MOD4_SUCCESSOR_PROOF_2026-09-16/PROOF.md`, 239 lines, sha256 `953d4d6c2fb711a53fc7c3c6ad2afe69cad8e4589092af30d26ccf3bacaa6ffc`. This matches the brief and the object's `MANIFEST.sha256`.
- **Referee:** second referee, fresh and hostile, under a no-repair mandate. 2026-09-16. Nothing outside `referee_2/` was edited.
- **Independence:** this file was written before I opened anything in `referee_1/` or `history/`, the three excluded drafts in `src/`, `~/H41_VERTEX_EXCLUSION_AUDIT_2026-09-16`, or `~/H41_POSITIVE_KILL_TEST_2026-09-16`. I did read the object's `MANIFEST.sha256`, which lists the file names and digests of `referee_1/`. I saw no content from `referee_1/`.
- **Line numbers:** "line N" means line N of `PROOF.md`.

---

## (a) Overall verdict

**PASS WITH REMARKS. BLOCKING defects: 0.**

I checked every step of the chain and found none that fails as written:

- T1 (sec 2)
- L2 (sec 3)
- the annular residues (sec 5)
- L1 with Lemma R (sec 6, 11.R1–R2)
- the positive graph (sec 4, 11.R3)
- Conrad–Stein (secs 7 and 9)
- conclusions (i)–(iii) on both branches
- the twist and BSD transfers (sec 8, 11.R6)

Every primary statement I could open matches what the object quotes. The defects in (c) fall into three kinds:

- citations that do not literally say what is claimed;
- wording that is imprecise;
- identifications that are standard but not cited.

None of them needs new mathematics. The regression evidence in (e) is consistent with every claim, but it is not proof.

Two primary texts outside the object's own `src/`, read by me, bear directly on the referee gates:

1. **Coleman, *The monodromy pairing*, Asian J. Math. 4 (2000) 315–330.**
   - **Thm 2.1, p. 319:** the pairing defined through uniformization equals Grothendieck's monodromy pairing.
   - **Thm 4.1, p. 320:** "Suppose ω ∈ H^0(J, Ω^1_{J/K}) and h ∈ H_1^{Bet}(Gr(X),Z) are such that f^*ω = h^* dz/z. Then, h = Σ'_e Res_e(α^*ω) e."
   - Thm 4.1 is stated for curves over a finite extension of the completion of Q_p^ur whose minimal model has semistable reduction with smooth components. It is exactly the integral identity that L1 needs.
   - Section 6 of the object re-proves this statement (Lemma R) and cites Coleman only for BR Rem 6.3.
2. **Edixhoven, arXiv:math/0312019v1, §§2.1–2.8** (the arXiv version of [Edi06]).
   - §2.1: the Tate curve identifies Spf Z[[q]] with the completion of X_0(N) along ∞.
   - Prop 2.5: S_2(Z) = H^0(X_∞, Ω^1).
   - For p ∥ N (p. 7): "C_∞ containing the cusp ∞, and hence C_0 the cusp 0". The components cross transversally, and Ω is invertible.
   - p. 9: "W_d interchanges C_∞ and C_0 if and only if p divides d."
   - These support I8, 11.R4 and gate G4.

---

## (b) Gate verdicts

| Gate | Verdict |
|---|---|
| G1 | PASS WITH REMARKS |
| G2 | PASS WITH REMARKS |
| G3 | PASS WITH REMARKS |
| G4 | PASS WITH REMARKS |
| G5 | PASS |
| G6 | PASS |
| G7 | PASS WITH REMARKS |

### G1 — positive graph (sec 4, lines 89–102; I11, lines 43–46; 11.R3, lines 201–211): PASS WITH REMARKS

**Regularity and local rings.**
- Č16 = Česnavičius arXiv:1604.02165, local text, §3.1: "The algebraic stacks X and X′ are regular" (Γ = Γ_0(n), ord_2 n = 1).
- Č16 §3.8: the μ and ét components meet at the supersingular points; by [DR73, V.1.16 (ii)] they cross transversally in the special fibre, and "due to the regularity of X_{Z(2)}" also in X_{Z(2)}.
- Čes17 = arXiv:1511.07475v2, Theorem 1.5 = 5.13(a) (read): "The Deligne–Mumford stack X_0(n) is regular."
- On the elliptic-curve locus, Y → X_{Γ_0(N)} is a (Z/l)^×-torsor, namely the generators of the étale subgroup C_l. So Y is regular there.
- A regular two-dimensional complete local ring with residue field F̄_2 whose reduction mod 2 is a transversal node has the form R[[x,y]]/(xy−2) after rescaling. The argument is GRAPH_LEMMA Lemma 3.1, and it transfers without change.

**X = Y/G.**
- Y/G → X is finite and birational onto a normal target, so it is an isomorphism.
- The completed local ring of X is the ring of stabilizer invariants, because invariants commute with flat base change (GRAPH_LEMMA Lemma 3.2 argument).
- This is correct on the elliptic-curve locus, which is all that is used.

**Stabilizers.**
- Mazur 1977 (corpus text, lines 1536–1566, read) gives:
  - |Aut E_ss| = 24 and Aut/±1 ≅ A_4;
  - an order-3 subgroup fixes two cyclic subgroups of order N if N ≡ 1 mod 3, and none otherwise;
  - Aut(E, C_N) → (Z/N)^× is injective for N ≥ 5.
- Involutions of A_4 lift to elements of order 4 with characteristic polynomial x²+1, which is irreducible mod 3. So they fix no line of E[3].
- Hence Stab(C_3, C_l) is 1 or C_3, and e_x ∈ {1, 3}. The stabilizer in G is isomorphic to this group by Mazur's injectivity. Correct.

**Chart.**
- An odd-order group cannot swap the two branches, so branches are preserved.
- Averaging works because 3 is a unit in R. It gives eigen-coordinates, and the relation forces ζ′ = ζ^{-1}.
- The action is effective because G acts faithfully on the integral scheme Y.
- The invariants are R[[x³, y³]] = R[[U,V]]/(UV−8). Correct; this is GRAPH_LEMMA Lemma 3.5, which is stated for any faithful, branch-preserving action of order e ∈ {1, 3}.

**Mass.**
- There are 4(l²−1)/24 fine supersingular points, because an automorphism fixing a point of order l ≥ 5 is trivial.
- Dividing by |G| = (l−1)/2, which is odd, gives Σ 1/e_x = (l+1)/3, with 2-adic valuation 2 because l ≡ 3 mod 8. Correct.

**Φ_J ⊗ Z_2 = Z/4.**
- BR Cor 2.4 and Thm 2.5 (local text) apply on the minimal regular model: chains of e_x−1 (−2)-curves, all components smooth.
- The interior path blocks have odd determinant e_x.
- The Schur complement on the two principal vertices is S·[[1,−1],[−1,1]] with S = (l+1)/3. So Φ_J ⊗ Z_2 = Z_2/S = Z/4, generated by [v_0 − v_∞] = sp_J(c).
- Correct. The author's Smith-form regressions at l = 11, 19, 43 reproduce identically.

**Remarks:** D6, D7, D8.

### G2 — integral residue = character coordinate (sec 6, lines 114–128; 11.R1, lines 183–195; 11.R2, lines 196–200): PASS WITH REMARKS

**The Baker–Rabinoff chain (local text, verified).**
- (4.5.2): M = H_1(X^an, Z), from BL84.
- Proof of Thm 2.9: H_1(Γ,Z) is identified with M through τ_*, and trop ∘ α̃_* is the edge-length map μ. BR's own remark reads "trop : E^an → N_R is the (unique) lift of τ′ to universal covers" (BR lines 878–879). The quotation at line 186 is accurate.
- Rem 6.3: the analytic pairing equals Grothendieck's pairing when Λ = Z [Col00].
- Cor 5.6 and Prop 6.1 are quoted correctly.
- BR §5.1 allows nodes of the form R[[s,t]]/(st−ϖ_x) with edge length val(ϖ_x). The coarse model with UV = 2^{e_x} is therefore directly a split semistable model with edge lengths e_x, consistent with 11.R2.

**Lemma R, step by step.**
- **(1)** Néron functoriality over R, followed by base change. Correct.
- **(2)** The formal torus of J^0 maps into Ĝ_m and is rigid; its restriction is the character u. True by SGA 3 rigidity, but the citation is wrong (D1).
- **(3)** π̃ exists, is unique, and satisfies p_{E_0} ∘ π̃ = π ∘ p_J. True.
  - **BL91 is not genuinely needed.** By BR §4.1, E^an is the topological universal cover of J^an, with a unique analytic group structure. So π ∘ p_J lifts uniquely through G_m^an → E_0^an, with 0 ↦ 1.
  - The lift is a homomorphism: E_J^an × E_J^an is connected and qq^Z is discrete.
  - On the connected domain E_J^0 the lift agrees with the formal map.
  - The phrase "open subgroup" is inaccurate (D2).
- **(4)** Three facts, all correct:
  - E(K′) = T(K′) + A_0(K′) (BR proof of Prop 5.3: "E(K) = T(K) + J_0(K)");
  - trop^{-1}(0) = A_0 by definition (BR §4.2);
  - on T^an, trop is χ ↦ −log|χ| (BR §4.2).
  - Applied to K′-points for every complete extension K′ of K, these cover all Berkovich points.

**Slope = u_x, with no factor e_x.**
- A_x is contractible, so AJ lifts over it.
- trop_J of the lift differs from ∫_p^{τ(y)} by a locally constant element of μ(M).
- τ(y) lies at distance v(U(y)) along an edge of length e_x.
- Hence trop(·)(u) has slope u_x per unit t = v(U).
- On closed subannuli, g = γU^w(1+h) with |h| < 1 (BPR Prop 2.2), so Res(dg/g) = w, which is the slope of v(g). Correct.

**Integrality.**
- a·u_x = c_π·Res_x(ω_f) and Res_x(ω_f) ≡ s_x ≡ 2 mod 4R. So v(u_x) = 1, and since u_x ∈ Z, u_x ≡ 2 mod 4.
- Negative branch: e_x u_x − e_y u_y ∈ 4R ∩ Z = 4Z.
- Correct.

**Independent support.** Coleman 2000, Thm 4.1, Cor 4.1.1 and Thm 4.2 (read) state this identity on the regular semistable model. On the regular model the coefficients along a chain are forced to be constant, so the coarse coordinate is u_x. Coleman Thm 2.1 gives "uniformization pairing = Grothendieck pairing".

**Remarks:** D1, D2, D3, D4.

### G3 — slope formula and residues (sec 5, lines 104–112; 11.R5, lines 223–226): PASS WITH REMARKS

**Setting.**
- The work is over C_2, because BPR assumes K algebraically closed (BPR lines 6 and 23). BR §5.1 gives compatibility with base change.
- The punctured curve is X \ {0, ∞}.
- V = {ζ_∞, ζ_0} is the semistable vertex set of the model (BPR Def 3.1 and §4).
- The cusps 0̄ and ∞̄ lie in distinct residue discs, on C_0 and C_∞ respectively (Edixhoven p. 7).

**Slope formula.** BPR Thm 5.15 (local text): (2) F is affine on edges; (4) F is harmonic; (5) the slope along the ray to x is ord_x(f).
- At ζ_∞ the ray to ∞ has outgoing slope −(l²−1). So Σ s_x = l²−1, and e_x s_x = B − A.
- Hence B − A = 3(l−1), and s_x ∈ {3(l−1), l−1}, both ≡ 2 mod 4.
- On the negative branch the analogue is KAPPA_PARITY_PROOF Theorem A (intersection theory), pins verified.

**Residues.**
- Res(dF/F) = s_x by BPR Prop 2.2 (local text matches line 110).
- For a section of Ω, the dualizing module of R[[U,V]]/(UV−2^e) is generated by dU/U, so the residue lies in R.
- With δ ∈ 4H^0 this gives Res_x(ω_f) ≡ s_x mod 4R. Correct.

**Remarks:** D5, D11.

### G4 — two-component lemma and instantiation (sec 3, lines 73–87; I8, lines 31–35; 11.R4, lines 212–222): PASS WITH REMARKS

**The lemma.** The proof is correct:
- the completion is faithfully flat;
- divisibility passes to the generization;
- w carries 2L_{ξ_1} to 2L_{ξ_2};
- L is invertible on a normal scheme, so the Hartogs property applies;
- then induction on k.

**The instantiation.**
- **ω_f ∈ H^0(X, Ω):** Č16 Lemma 2.7, local text.
- **θ = dF/F is regular in codimension one.** At the vertical generic points F = 2^A·unit and d(2) = 0; horizontally, the only simple poles are at 0 and ∞.
- **Ω(cusps) is invertible:** Č16 §2.6, local text.
- **Expansion at ∞̄.** It lies in R[[q]]dq/q (Edixhoven §2.1, read; CNS sentence, see (d)). θ_0 = −(l²−1) ≡ 0 mod 8 and θ_n ≡ a_n mod 4, so δ ∈ 4R[[q]]dq/q.
- **Component behaviour.** Edixhoven p. 9 ("W_d interchanges C_∞ and C_0 iff p divides d") gives: w_2 swaps the components, w_M preserves them, and w_N swaps them. This matches Č16's proof of Lemma 2.7 and Č18's proof of Lemma 5.4 (local text), and also the object's moduli argument.
- **Cusp positions.** 0̄ ∈ C_0 and ∞̄ ∈ C_∞ by Edixhoven p. 7.
- **F ∘ w_N = C/F exactly.** This uses r_{N/d} = −r_d and Σ r_d = 0 (verified).
- **ε_N = Π(−a_p) = −1.** This is the standard Atkin–Lehner/Li relation; I could not read the primary text (D12).

**Corroboration (regression).** Suppose δ ∈ 4H^0(X_R, Ω(cusps)). Then W_Q^*δ ∈ 4H^0 for every Q ∥ N, which forces:
- ε_Q·a_n ≡ ±θ^{(Q)}_n mod 4;
- θ^{(Q)}_0 ≡ 0 mod 4.

Here θ^{(Q)} is the log-derivative of Π η(dz)^{r_{d∗Q}}. Both conditions hold for all Q ∥ N at N = 62, 66, 114, 254, 258, for n ≤ 120 (`checks/referee2_cusp_test_output.txt`).

**Remarks:** D9, D12.

### G5 — Conrad–Stein for the actual optimal quotient (sec 7, lines 130–137; sec 9, lines 155–162; I9, lines 36–37): PASS

**CS local text, verbatim.**
- **Hypotheses of §6:** π is an optimal quotient; J has a symmetric principal polarization; J has semistable reduction; A has purely toric reduction.
- **Lemma 6.3:** the sequence X_J → Hom(π^*X_A, Z) → Φ_A → 0 is exact. Its proof uses Thm 8.2 (π_* surjective, any DVR).
- **Prop 6.5:** image(Φ_J → Φ_A) ≅ Φ_L, with L the saturation.
- **Ex. 4.3:** for a Tate curve, Φ_E is cyclic of order −ord j = ord Δ_min.

**Consequences.**
- With π^*X_A = Zu, the image of X_J is ⟨X_J, u⟩ = n_0·Z.
- Since ⟨z, u⟩ ∈ 4Z for all z, 4 | n_0.
- By I2 (verified by me) only E has 4 | n_V, so E_0 = E.
- Prop 6.5 with L = Zv gives image ≅ Z/(n_0/κ).
  - **Positive branch:** v_2(κ) = 1, so the 2-part of the image is Z/2. Hence 2 | t, and with t | 2, t = 2.
  - **Negative branch:** κ is odd, so the image contains Φ_E[2^∞] = Z/4, hit by sp_J(c) through (K1). Hence t = 4.
- I5 then gives 4λ odd. Correct.

**Seed checks (independent re-derivations).**
- **I5.** The elliptic logarithm of φ(0) along the imaginary axis is c_π·L(E,1), taken modulo Ω_0^+ = Ω_{0,R}/δ_0. So z = ν_0 δ_0 λ / h, and t is its reduced denominator.
- **I4, positive branch (t | 2).**
  - The real roots of y² = x(x² + (1−2r)x + r²) are e_1 < e_2 < 0.
  - P = (r, r) has r < 0, so P lies on the non-identity component.
  - Therefore C_4 ∩ E(R)^0 = ⟨(0,0)⟩.
  - The real path from ∞ to 0 lands in E(R)^0.
- **I4, negative branch (t | 4).** #E(F_3) = 4, so E(Q)_tors = C_4.

**Corroboration.**
- **Conrad–Stein Table 1.** Row 66B at p = 2: #Φ_X = 2, m_X = 2, m_A = 4, #Φ_A = 4. This is image order 2 with κ = 2 at m = 3.
- **Cremona modular degrees at all ten levels.** CS Thm 6.1 gives ⟨u,u⟩ = n_0 · deg. The claimed residue classes are consistent with it for the Cremona degrees:
  - positive branch: 4·Σ e_x ≡ n_0 · deg mod 32;
  - negative branch: Σ e_x ≡ n_0 · deg mod 8.
- **Levels 66 and 62.** The CS constraints together with Cremona's degree force u to be exactly what the object claims:
  - N = 66: u = ±(2, 2, −2, −2);
  - N = 62: u = ±(1, 1, −1, −1) with e = (3, 3, 1, 1).

**Minor points, not affecting this gate:** D13.

### G6 — T1 (sec 2, lines 56–71), including m = 7: PASS

**Eta side, all verified.**
- The E_2 log-derivative formula, with θ_0 = Σ r_d d/24.
- The weights w_d, and holomorphy of E±.
- (1−V_p) sends σ(p^k) to p^k, and (1−pV_p) sends it to 1.
- E+_n = 3^b l^c σ(m) and E−_n = p^c σ(m).
- The congruences −r_d d ≡ ±w_d mod 4, symbolic in l = 4k+3.

**Newform side, all verified.**
- P = (r, r) has order 4, so a_{v^j} ≡ σ(v^j) mod 4 at good odd primes.
- At 2: b is even, the reduction is a split node, and a_2 = 1.
- At primes ≡ 3 mod 4 dividing D: c_4 = 16(1−4r+r²) is a unit there, the reduction is nonsplit, and a = −1.
- m = 7: N = 114, v_3(Δ) = 3, and c_4 = 16897 ≡ 1 mod 3.

**Regression.** θ_n ≡ ±a_n mod 4 for n ≤ 150, and θ_0 ≡ 0 mod 8, at N = 62, 66, 114, 254, 258. Here θ_n comes from explicit power series and a_n from independent point counts.

### G7 — literal imports, twist 2-part, Zhai, BH, I2 (sec 1; sec 8, lines 139–153; 11.R6; 11.R8): PASS WITH REMARKS

**I1.**
- Matches master map §G: "eliminates all odd rational isogenies, so the four vertices exhaust the rational isogeny class".
- Independently: E, F, G each have exactly one rational 2-torsion point and B has full 2-torsion, so the 2-isogeny graph is closed (`checks/referee2_extra_output.txt`).
- 3-, 5- and 7-isogenies are excluded by the Frobenius discriminants (verified).
- Primes ≥ 11 rely on Mazur–Kenku, not read.

**I2 / 11.R8.** Verified symbolically in r:
- all four minimal models are isomorphic to the displayed curves via u = 2;
- the discriminants are r⁴D/256, r²D²/16, rD⁴/4 and −rD/4;
- c_4 is odd;
- the edges E–B, B–F and B–G are the stated 2-isogenies;
- ord_2 Δ = (4, 2, 1, 1)·(m−2) for r = ±2^m, m = 3..15.

**I3–I5.** Verbatim equal to the W audit §1 table and identities (1)–(2) (D10).

**I6.** Divisor (l²−1)([0]−[∞]) verified.
- Symbolically in l by Ligozat's formula.
- Numerically at l = 11, 19, 43, 683, 2731.
- Negative unit: divisor ((p²−1)/8)([0]−[∞]) at p = 31, 127, 8191.
- This matches ROOT_ARITHMETIC §4 and KAPPA_PARITY_PROOF Input 2.

**I7.**
- Č18 = Česnavičius arXiv:1703.02951v3: Thm 1.2 = Thm 2.13, verbatim.
- The alternative, Č16 Thm 1.4(i) and 1.5(i)/(ii), verbatim.
- The disambiguation note at line 30 is correct.

**I12.** The statements of Theorem A and Theorem B match their files.

**I13.**
- BH 2.13 (i)–(vii) are quoted verbatim.
- In BH Remark 2.11, [6] = Burungale–Skinner–Tian–Wan, [8] = Castella–Çiperiani–Skinner–Sprung, and [23] = Keller–Yin. This matches the qualifier at line 152.

**Twist 2-part (lines 140–143).** Correct:
- the quadratic factor of the 2-division polynomial has nonsquare discriminant, so the 2-Sylow subgroup is cyclic;
- (r/q) = −1 on both signs when q ≡ 5 mod 8 and m is odd;
- the duplication formula shows P is not a double;
- a cyclic 2-group containing P of order 4 but no half of P has order 4.

**Zhai (local text).**
- **Thm 1.7 hypotheses:** optimal curve; odd Manin constant; Δ > 0; E[2](Q) ≠ 0; L(E,1) ≠ 0; q ≡ 1 mod 4; (q, C) = 1; ord_2 N_q = 1 − ord_2 L^alg.
- **Thm 1.7 conclusion:** ord_2 L^alg(E^(q), 1) = 1, where Ω^+ is the least positive period.
- Since Ω_R = 2Ω^+ for both the base and the twist (Δ_twist = q⁶Δ > 0), the full-period valuation is 0.
- **Thm 1.5 (negative):** applies with M = q (q ≡ 1 mod 4 forces ε = +1) and Ω_R = Ω^+.
- Correct.

**BH 2.13 for the original E on both branches.**
- **(i)** The field discriminant q is prime to 3N.
- **(iv)** a_3 = −1 (positive) and a_3 = 0 (negative: r ≡ 2 mod 3 gives #E(F_3) = 4).
- **(v)** a_5 = ±2 for r ≡ 2, 3 mod 5, and a_7 ∈ {4, 0, −4} for r ≡ 3, 5, 6 mod 7. On the negative branch the object uses a_5 and a_3. All the discriminants are nonsquares as stated.
- **(vi)** The witnesses are as stated: E[p] is ramified at a multiplicative prime q exactly when p ∤ ord_q Δ.
- **(vii)** a_q ≡ 2 mod 4, so the reduction at q is ordinary.
- Line 153 is correct: optimality is not a hypothesis of BH 2.13.

**Remarks:** D10, D14.

---

## (c) Defects

### BLOCKING

None.

### D1 [CITATION] — 11.R1 step (2), line 190

**What is wrong.** "Conrad–Stein Cor 8.5: unique and functorial" is cited for the formal torus of J lifting T_{J,k}, and for its functoriality. CS Cor 8.5 (local text, lines 749–769) is about something else: the unique multiplicative ℓ-divisible group Γ_ℓ inside the Néron model over a henselian DVR that lifts the ℓ-divisible group of the torus.

**What would be needed.** A citation to the lifting and rigidity of tori and multiplicative-type groups over a complete local base (SGA 3 Exp. IX/X), or an explicit passage from Γ_2 to the formal torus. The mathematical claim is true.

### D2 [NON-BLOCKING] — 11.R1 step (3), lines 191–193

**What is wrong.**
- **(a)** "agreeing on the open subgroup E_J^0": E_J^0 = trop^{-1}(0) is a compact analytic domain. It is not a topologically open subset of E_J^an.
- **(b)** BL91 (not local) is cited for functoriality, but it is not needed. As G2 shows, BR §4.1's characterization of E^an as the topological universal cover already gives existence, uniqueness and the homomorphism property of π̃.

**What would be needed.** Either invoke the identity principle for analytic maps on a connected smooth space that agree on a nonempty affinoid domain, or replace the step with the universal-cover lifting argument. This is a wording fix, not a repair.

### D3 [CITATION] — secs 6 and 11.R1–R2, lines 116–128 and 183–200

**What is wrong.** The object does not cite Coleman 2000 Thm 4.1 / Cor 4.1.1 / Thm 4.2 (pp. 320–322). These state the integral residue–character identity that Lemma R re-derives, for curves whose minimal model is semistable with smooth components. Coleman is cited only for BR Rem 6.3.

**What would be needed.** Nothing is missing from the argument. Citing Thm 4.1 on the regular model, where the chain over a coarse node carries constant coefficients, would reduce G2 to a published statement.

### D4 [NON-BLOCKING] — lines 116–118 and 186–188

**What is wrong.** Two identifications are used without citation:
- Conrad–Stein's X_J (the character group of the torus in the closed fibre of the Néron model over the DVR R) with Baker–Rabinoff's M (the character lattice of the torus of the Raynaud extension over K, and then over C_2);
- CS's π^* with the character u of 11.R1 (2).

They are standard: BR §4.1 lifts the torus of A_0, whose special fibre is the Néron identity component for semiabelian reduction; see also BL/BLR. Coleman §1 and §4 use the same identification.

**What would be needed.** An explicit sentence with a citation.

### D5 [NON-BLOCKING] — line 111

**What is wrong.** "Res_x(s) = constant term of g" is not well defined for g ∈ R[[U,V]]/(UV − 2^{e_x}). For example, g = UV has constant term 0 or 2^{e_x}, depending on the representative.

**What would be needed.** Take the U⁰-coefficient of the normal form Σ_{a≥0} c_a U^a + Σ_{b≥1} d_b V^b, which is the same as the Laurent coefficient on A_x. The conclusion Res_x(s) ∈ R is correct.

### D6 [CITATION] — line 44 (I11), 11.R3 line 203, 11.R3 line 205

**What is wrong.**
- Regularity of the Γ_0(N)-stack is attributed to "[Ces17 sec 4.4]". In Čes17 (arXiv:1511.07475v2), Γ_0(n) regularity is Theorem 1.5 = 5.13(a); §4.4 treats Γ_1(n). Č16 §3.1 cites both places.
- "Y is a scheme (Γ_1(l), l ≥ 5, rigidifies: 1604.02165 (3.1.1) ...)": (3.1.1) is stated for Γ = Γ_1(n) with n/2 ≥ 5. It does not cover the mixed level Γ_0(2)×Γ_0(3)×Γ_1(l).

**What would be needed.** Correct pointers: Čes17 5.13(a), and KM85 for rigidity of Γ_1(l)-structures with l ≥ 5 on elliptic curves. The claims themselves are true.

### D7 [NON-BLOCKING] — 11.R3, lines 201–207

**What is wrong.** Y is not specified as either the elliptic-curve locus or a compactified moduli problem. Two claims are argued only on the elliptic-curve locus:
- "finite etale over Z_(2)" (for Y → X_{Γ_0(N)});
- "Y/G → X is finite and birational onto the normal X, hence an isomorphism".

They are correct there, and that locus is all that the local rings at supersingular points need. Nothing is argued at the cusps.

**What would be needed.** Restrict both statements to the elliptic-curve locus.

### D8 [NON-BLOCKING] — 11.R3, line 204

**What is wrong.** "cross transversally ..., which pulls back: completed local ring W[[x,y]]/(xy − 2·unit)". Getting from transversal crossing in a regular two-dimensional scheme to this presentation needs a local-algebra step:
- a Cohen presentation;
- regularity forces the coefficient of 2 to be a unit.

That step is GRAPH_LEMMA Lemma 3.1. 11.R3 cites Lemmas 3.2 and 3.4–3.6 as the N = 2p analogues, but not 3.1.

**What would be needed.** Cite, or state, Lemma 3.1.

### D9 [CITATION] — 11.R4, lines 216–217 and 220–221

**What is wrong.**
- **(a)** "the 'mu-model' descent of inf, L315" points to Č16's remark about Γ_1(n) q-expansions. That remark is not the statement ∞̄ ∈ X^μ for Γ_0(N). The direct source is Edixhoven arXiv:math/0312019v1 p. 7: C_∞ is identified with X_0(N/p) via ker F, "C_∞ containing the cusp ∞, and hence C_0 the cusp 0".
- **(b)** "(M Lemma M8)": in ADDENDUM_015's M_DRAFT the CNS citation is used in §4 ("[derived] ω̄_f ≠ 0", lines 410–415), not in Lemma M8. M records it as a paraphrase, not a quotation.

**What would be needed.** Correct pointers.

### D10 [CITATION] — lines 21–24 (I3–I5)

**What is wrong.** These tier-[A] imports are pinned to `H41_W_MECHANISM_AUDIT.md`, which calls itself "Hostile theorem-design audit; unsealed". Neither its digest nor the digest of the sealed Stage II identity-component review it relies on is recorded. The quoted statements do match the W audit verbatim.

**What would be needed.** Pin the sealed source by digest. Independently of this defect I re-derived I5 and I4 from standard facts (see G5).

### D11 [NON-BLOCKING] — lines 106–108 and 11.R5 line 224

**What is wrong.**
- Line 106 applies BPR Thm 5.15 "on X minus the cusps", and line 107 speaks of "the rays to the cusps" at C_∞. 11.R5 instead uses the punctured curve X_{C_2} \ {0, ∞}. Both work, since the other six cusps reduce to distinct smooth points and carry slope 0, but the text is inconsistent.
- One orientation convention is used simultaneously for s_x, u_x and z_x: a coordinate U with v(U) = 0 at C_∞ and v(U) = e_x at C_0. It is only implicit ("one global orientation", line 108). It carries weight on the negative branch, where e_x u_x ≡ C mod 4 involves odd numbers and so depends on sign.

**What would be needed.** State the punctured curve once, and state the orientation convention explicitly.

### D12 [NON-BLOCKING] — line 71; 11.R4 lines 221–222

**What is wrong.** I could not check the relation ε_p = −a_p for p ∥ N (Atkin–Lehner 1970 Thm 3; Li 1975 Thm 3) against a primary text, because neither was accessible. Edixhoven (read) supports the component behaviour of W_d but not the eigenvalue relation. The relation is standard, and I do not believe it is wrong.

**What would be needed.** A local copy of the primary text.

### D13 [NON-BLOCKING] — lines 171, 36–37, 194

**What is wrong.**
- The G5 gate text in sec 10 (line 171) still mentions "Lemma 4.1's image formula". Secs 7 and 9 now use CS Prop 6.5.
- I9 (lines 36–37) omits CS's standing hypothesis of a symmetric principal polarization on J (J_0(N) satisfies it).
- 11.R1 (4) (line 194) cites "BR (5.5)" for trop on T^an; the definition is in BR §4.2.

**What would be needed.** Editorial corrections.

### D14 [NON-BLOCKING] — line 18 (I1), used at lines 133 and 157

**What is wrong.** E_0 = E needs the isogeny class to be exactly {E, B, F, G}. Two parts of that are now verified here: the closure of the 2-isogeny graph, and the absence of 3-, 5- and 7-isogenies. The exclusion of ℓ-isogenies for ℓ ≥ 11 still rests on the imported audit, which uses Mazur–Kenku. The object does not show this step or point to a published statement for it.

**What would be needed.** A one-line pointer: a rational ℓ-isogeny together with the rational 4-torsion point would give a cyclic 4ℓ-isogeny, which Kenku's classification excludes for ℓ ≥ 5.

---

## (d) Statements not verified from a primary text

**Sources I opened and read.**
- **Coleman, Asian J. Math. 4 (2000).** Read pp. 315–326 (the intlpress PDF, via page images): Thm 1.3, Thm 2.1, Thm 3.1, Thm 4.1, Cor 4.1.1, Thm 4.2, §5, Lemma 6.1, Lemma 6.2. Pages 327–330 were not read. Thm 3.1 is Coleman's restatement of Grothendieck's SGA 7 IX theorem; I did not read SGA 7 itself.
- **Edixhoven, arXiv:math/0312019v1.** Read pp. 1–9. The published J. Inst. Math. Jussieu version was not compared; the "2.5" numbering matches the citations.
- **Česnavičius, arXiv:1511.07475v2.** Read pp. 1–3 (Theorem 1.5 = 5.13(a)). Items 4.1.4 and 4.4.4 were not read.
- **Česnavičius–Neururer–Saha, arXiv:1911.09446v3.** Only two sentences were obtained, through a fetch tool that summarizes pages, so these are not guaranteed verbatim quotations:
  - "The containment (⋆) is straight-forward in the semistable case, that is, for squarefree N, thanks to q-expansions and the Atkin–Lehner involution."
  - "since the formal completion of X₀(N) along ∞ is Spf(ℤ⟦q⟧) ..."

**Not verified from a primary text.**
1. Deligne–Rapoport 1973, V.1.16(ii) and VI.6.9. Only as quoted in Č16 §§2.6 and 3.8; the content is restated in Edixhoven p. 7 (read).
2. Katz–Mazur 1985, 2.7.4 and 5.1.1 (rigidity; regularity of Y_0(n)). Only as cited in Č16 and Čes17.
3. Bosch–Lütkebohmert 1984, the source of BR (4.5.2). Not read.
4. Bosch–Lütkebohmert 1991. Not accessible (ScienceDirect returned 403).
5. SGA 3 (rigidity and lifting of tori) and SGA 7 IX 11.5 (Grothendieck's exact sequence, as used in CS §4.1 and BR §2.1). Not read.
6. BLR90 §§9.2, 9.5–9.7; Conrad 2000. Not read.
7. Atkin–Lehner 1970 Thm 3 and Li 1975 Thm 3 (ε_p = −a_p). Atkin–Lehner's GDZ link returned 404; Li was not accessed.
8. Mazur's isogeny theorem and Kenku's classification, needed for I1 at ℓ ≥ 11. Not read.
9. The Stage I/II material behind I1 and I3–I5: the "latest ordinary audit", the identity-component review (ICR), and STAGE_II_COMPARISON. Not opened. Statements were compared only with master map §G and W audit §1. I re-derived I4 and I5 from standard facts, and I2 in full.
10. The proofs of Composition Theorems A and B (`01_pro_C`, `02_pro_D`). Not opened; statements only.
11. The proofs of Zhai 1.5 and 1.7, of BH 2.13, and of BH's external dependencies [6], [8], [23]. Not read; statements only.
12. Yoo 1908.06411v4 Thm 3.6 and Chua–Ling 1997. Not read. The eta divisors were checked instead with Ligozat's standard formula (the formula itself not re-read).
13. Cremona's optimality flags, Manin-constant flags and modular degrees. Database values only.
14. GRAPH_LEMMA and KAPPA_PARITY_PROOF were read in full, but their external standard facts (F1)–(F5), BLR90 9.6/1, [DR73 VI.6.7], and the Mazur–Rapoport appendix beyond the quoted lines were not.

---

## (e) Commands run and regression evidence

**Environment.**
- Load was checked with `uptime` before every compute run; the highest 1-minute load seen was 7.60.
- Every compute run used `nice -n 19`, one process at a time, with no background jobs.
- Tools: `/opt/miniconda3/bin/python3` with sympy 1.14.0. PARI/GP, Sage and Magma are not installed.
- Scripts and outputs are stored under `referee_2/checks/`.
- **Disclosure.** Working copies were first written to the session scratchpad (`/private/tmp/claude-501/-Users-bsm/2c6faf50-99be-4089-8939-52abc4c35596/scratchpad/`, temporary). The fetch tool also saved three PDFs automatically under `~/.claude/projects/-Users-bsm/2c6faf50-99be-4089-8939-52abc4c35596/tool-results/`. Nothing in the object or its source directories was modified.

**Bash commands.**
1. Inspection:
   - `uptime`; `ls -la` of the object directory, `checks/` and `src/`;
   - `shasum -a 256 PROOF.md`; `wc -l PROOF.md`;
   - `mkdir referee_2`; `cat MANIFEST.sha256`; `shasum -a 256 src/*.txt`.
2. Reading with `grep`, `sed`, `awk` and `cat`:
   - `stevens_v2.pdf.txt` (Č16), lines 1–720;
   - `cesnavicius_1703.02951v3.reextracted.txt`, lines 40–80, 425–450 and 1040–1110;
   - master map, lines 40–70 and 336–515;
   - `H41_W_MECHANISM_AUDIT.md`, lines 1–140;
   - BPR, lines 100–470 and 1000–1215;
   - Zhai, lines 20–260;
   - `THEOREM_A_...md` and `THEOREM_B_...md`, in full;
   - BH, lines 125–380 and the reference list;
   - ADDENDUM_017 `MANIFEST.sha256`, with `shasum` of the pinned copies and of `H41_KAPPA_PARITY_ADDENDUM_017.tar.gz`;
   - ADDENDUM_015 `M/M_DRAFT.md`, lines 20–40, 400–460 and 660–672;
   - GRAPH_LEMMA.md and KAPPA_PARITY_PROOF.md, in full;
   - ROOT_ARITHMETIC.md, lines 25–57;
   - `mazur_1977.txt`, lines 1530–1580;
   - `checks/run_all_checks.py` and its output;
   - Cremona `opt_man.00000-09999` rows at N = 62, 66, 114, 254, 258;
   - `scripts_files.py`, lines 630–662.
3. `nice -n 19 python3 checks/run_all_checks.py /Users/bsm/run013-bsd-scout-2026-08-22/_data/ecdata/opt_man` followed by `diff` against `checks/run_all_checks_output.txt`: **IDENTICAL**. The copy is at `referee_2/checks/rerun_run_all_checks_output.txt`.
4. `nice -n 19 python3 cremona_fields.py`: extracts Cremona curvedata fields for the ten H41 curves.
   - The modular degrees are 2, 4, 60, 24, 60, 7980, 91008, 145332, 15060864 and 35702628.
   - Every λ = sha_an·Πc/16 has 4λ odd.
5. `nice -n 19 python3 referee2_checks.py`. The first run crashed in section C (a sympy/int bug in my script); I fixed it and re-ran. Results:
   - **A.** Ligozat divisors of both eta units: div = k([0]−[∞]); Π d^{r_d} is a square; r_{N/d} = −r_d.
   - **B.** From power series, θ_n ≡ ±a_n mod 4 for n ≤ 150 and θ_0 ≡ 0 mod 8, at N = 62, 66, 114, 254, 258.
   - **C.** I2/11.R8 verified symbolically, together with the 2-isogenies.
   - **D.** Local data for BH (iv) and (v).
   - **E.** CS Thm 6.1 congruences against the Cremona degrees: all ten levels consistent.
6. `nice -n 19 python3 referee2_cusp_test.py`. The first run hit an IndexError at N = 254 (a script bug); I patched it and re-ran. Result: the congruence holds at every cusp W_Q(∞), for Q ∥ N, at five levels.
7. `nice -n 19 python3 referee2_extra.py`:
   - **F.** 2-torsion structure of E, B, F, G, so the 2-isogeny graph is closed.
   - **G.** Ligozat divisor of the positive unit, symbolic in l.
   - **H.** #E(F_3) = 4 on the negative branch.

**Web and PDF reads** (authorized for the NOT LOCAL sources in 11.R9).
- WebFetch of arxiv.org/abs/1911.09446v3 and arxiv.org/html/1911.09446v3 (two calls).
- WebFetch of arxiv.org/abs/math/0312019 and of its PDF, then `Read` of PDF pages 1–9.
- WebSearch for Coleman 2000; WebFetch of the intlpress PDF; `Read` of pages 1–12 (journal pp. 315–326).
- WebSearch for BL91; WebFetch of ScienceDirect: 403.
- WebSearch for Atkin–Lehner; WebFetch of EuDML; WebFetch of the GDZ link: 404.
- WebFetch of arxiv.org/abs/1512.06225 returned an unrelated paper (Bruggeman–Choie) and was discarded.
- WebSearch for Čes17; WebFetch of arxiv.org/pdf/1511.07475; `Read` of pages 1–3.

**Regression summary** (evidence, not proof). Every regression matches the object's claims:
- the object's checks reproduce identically;
- Conrad–Stein Table 1 (66B at p = 2) is consistent with κ = 2 at m = 3;
- the Cremona modular degrees satisfy the Thm 6.1 congruences implied by the claimed residues at all ten levels;
- at N = 62 and N = 66 the CS constraints and the Cremona degree force exactly the claimed u;
- the necessary consequence of L2 at all cusps holds at five levels.
