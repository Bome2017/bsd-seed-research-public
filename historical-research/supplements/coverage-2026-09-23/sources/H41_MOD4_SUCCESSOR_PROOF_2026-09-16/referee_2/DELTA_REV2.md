# Referee 2 — delta review of revision 2 against revision 1 (no repair)

## What was compared

- **Revision 2 (under review):** `PROOF.md`, 299 lines, sha256 `c5d806defa3bc55da33cadb2cfad57c1d2e7e09c883c82dd371f814e1c0ab791`.
- **Revision 1 (baseline):** `history/revision_1/PROOF.md`, sha256 `953d4d6c2fb711a53fc7c3c6ad2afe69cad8e4589092af30d26ccf3bacaa6ffc`. It is byte-identical to the file I refereed in `referee_2/VERDICT.md`.
- **Diff:** I computed my own diff (`referee_2/checks_delta_rev2/referee2_own_diff_rev1_to_rev2.txt`). I did not rely on the supplied `history/DIFF_rev1_to_rev2.diff`. My diff has 17 hunks:
  - the header;
  - I1, I3–I5 pins, I8, I9, I11;
  - sec 5, two hunks;
  - sec 6;
  - sec 7, one inserted sentence;
  - sec 10, the G5 line;
  - 11.R1, 11.R3;
  - 11.R4, two hunks;
  - 11.R5;
  - R10–R12, new.
- **Unchanged sections (byte-identical):** sec 0 (rev 2 lines 8–16), secs 2–4 (65–114), and secs 7 (apart from the inserted sentence), 8, 9 and the start of 10.
- **Line numbers:** "line N" means a line of revision 2.
- **Author material:** `src/author_recheck_2026-09-16/` was not opened.
- **Scope of writing:** nothing outside `referee_2/` was written.

---

## (a) Delta verdict

**ACCEPT WITH REMARKS. BLOCKING defects: 0.**

Every changed mathematical claim holds. The new route in 11.R3 is correct:
- the Γ_1(6l) fine chart;
- the local-algebra lemma;
- the free (Z/3)^× quotient;
- the explicit automorphisms of y² + y = x³.

The rewritten Lemma R (11.R1) is also correct, and it no longer uses CS Cor 8.5 or BL91.

Resolution of the earlier defects:
- my D1–D14: 13 RESOLVED, 1 PARTIALLY RESOLVED (D12, which the object itself still marks unverified);
- referee 1's defect 4: now RESOLVED.

New issues, none of which changes a conclusion:
- two citation misattributions (N1, N3);
- one regression in presentation: rev 2 deleted two justifications that rev 1 had (N2);
- wording and custody points (N4–N7).

---

## (b) My defects D1–D14 in revision 2

| # | Severity in VERDICT | Status | Rev 2 lines | Basis |
|---|---|---|---|---|
| D1 | CITATION (CS Cor 8.5 cited for the formal torus) | **RESOLVED** | 199, 209–215 | CS Cor 8.5 is gone. See note D1. |
| D2 | NON-BLOCKING ("open subgroup"; BL91) | **RESOLVED** | 199, 207–208, 216–219 | BL91 removed; no "open subgroup" claim. See note D2. |
| D3 | CITATION (Coleman Thm 4.1 not cited) | **RESOLVED** | 130–132 | Thm 4.1 / Cor 4.1.1 / Thm 4.2, pp. 320–322, cited accurately (they match what I read). |
| D4 | NON-BLOCKING (Néron X_J = Raynaud M implicit) | **RESOLVED** | 128–130, 202–203, 212–213 | The identification is now stated. It has correct support in Coleman §4 (p. 322). The BR §4.1 attribution is imprecise (new N1). |
| D5 | NON-BLOCKING ("constant term") | **RESOLVED** | 120–122 | Residue is now the Laurent constant, via the normal form. See note D5. |
| D6 | CITATION (Ces17 §4.4; (3.1.1) scope) | **RESOLVED** | 51–55, 227–229, 236–237 | Primary route now cites a statement that literally covers the level. See note D6. |
| D7 | NON-BLOCKING (elliptic locus versus global) | **RESOLVED** | 227, 238–240 | "All statements in R3 are on the elliptic-curve locus"; only a local quotient is used. |
| D8 | NON-BLOCKING (regular-node lemma missing) | **RESOLVED** | 229–232 | The lemma is stated with its proof; verified in (c) C18. |
| D9 | CITATION (R4 pointers) | **RESOLVED** | 258, 262 | Edixhoven p. 7 is correct. M_DRAFT §4 lines 410–415 and its paraphrase caveat are confirmed. |
| D10 | CITATION (I3–I5 pinned to an unsealed audit) | **RESOLVED** | 28–30 | Both digests pinned and verified. See note D10. |
| D11 | NON-BLOCKING (punctured curve; orientation) | **RESOLVED** | 115–116, 268–270 | Punctured curve is X \ {0, ∞}, rays explicit, one orientation for s_x, u_x, z_x and residues. |
| D12 | NON-BLOCKING (ε_p = −a_p unread) | **PARTIALLY RESOLVED** | 262–264 | Support added, primary text still unread. See note D12. |
| D13 | NON-BLOCKING (stale G5 text; I9; "BR (5.5)") | **RESOLVED** | 187, 44–45, 205 | G5 now cites CS Prop 6.5; I9 states the polarization hypothesis; R1 cites BR §4.2. Residual stale text at line 184 (N7). |
| D14 | NON-BLOCKING (no pointer for ℓ ≥ 11) | **RESOLVED** | 19–21 | Kenku pointer added; verified in (c) C2. |

### Notes on the table

- **D1.** π̃|_{T^an} is an analytic character, hence algebraic ("analytic characters are algebraic", BR proof of Prop 4.7, local line 605). The character is then identified by reduction on the affinoid torus.
- **D2.**
  - The lift comes from the universal cover, and the homomorphism property from uniqueness of lifts.
  - The identity is proved by comparing two homomorphisms on E(K) = T(K) + J_0(K) (BR proof of Prop 5.3, local line 695).
- **D5.** The residue is the Laurent constant after substituting V = 2^{e_x}/U. Equivalently it is Σ_i a_ii 2^{e_x i}, with UV·dU/U as the correct example. This is right.
- **D6.**
  - Primary route: Č16 (2.6.1) (local line 359) together with §2.6 (local lines 372–374), which state that for Γ = Γ_1(n) the model over Z_(2) is a regular scheme.
  - Č16 only needs n/2 ≥ 5, which it gets from the existence of a newform of level n. Here f has level N = 6l, so the statement applies literally to Γ_1(6l).
  - The alternative route cites Ces17 Thm 1.5 = 5.13(a), which I read.
  - The line pointer is wrong (N3).
- **D10.**
  - W audit: sha256 `dfa6291c…` matches.
  - ICR: sha256 `544e1c9c…` matches and is listed at `CODEX_H41_SEED_RESEARCH_FREEZE_001/MANIFEST.sha256` line 569.
  - I read the ICR. It proves I4: for positive E, P and −P lie on the bounded oval and 2P = (0,0) on the identity component, so t | 2; negative E has exponent 4.
  - It also gives I5's form: z = ν_0 δ_0 λ / h = A/t in lowest terms. Its s-column is consistent with I3.
  - The open custody item for the W audit's row statements is declared honestly.
- **D12.**
  - CS §7.3, "Frob_p = −W_p" on X_J, is quoted correctly (CS local lines 476–478).
  - Frobenius acts on X_{E_0} by +1 for split reduction and −1 for nonsplit. Together these give ε_p = −a_p on the f-line.
  - Atkin–Lehner 1970 and Li 1975 remain unread, and the object marks them "UNVERIFIED primary import". Nothing is wrong; a primary citation is simply still outstanding.

---

## (c) Every new or changed mathematical claim, revision 1 → 2

| # | Claim (rev 2 lines) | Verdict | Check |
|---|---|---|---|
| C1 | Header, lines 1–2 | — | Custody text only; no mathematics. |
| C2 | I1 Kenku pointer, 19–21 | PASS | See C2 below. |
| C3 | I3–I5 pins, 28–30 | PASS | See note D10. |
| C4 | I8 Edixhoven pointer, 38–39 | PASS WITH REMARKS | The content is correct, but only the first item is on p. 7 (N3). The object cites the referee's own reading as support (N6). |
| C5 | I9 polarization hypothesis, 44–45 | PASS | CS §6 hypothesis (CS local lines 257–259). |
| C6 | I11 rewritten, 51–55 | PASS WITH REMARKS | Matches 11.R3. Line pointer wrong (N3). KM85 §2.7 is not local; it is used only in the alternative route. |
| C7 | Sec 5: punctured curve X \ {0, ∞}; ray slopes −(l²−1) at C_∞ and l²−1 at C_0, 115–117 | PASS | BPR Thm 5.15(4)(5) (local text) gives Σ_x s_x = l²−1 at ζ_∞ and s_x·e_x = B − A. |
| C8 | Sec 5 residue normal form, 120–122 | PASS | See C8 below. |
| C9 | Sec 6: Conrad–Stein's X_J = Baker–Rabinoff's M, 128–130 | PASS WITH REMARKS | True, and supported by Coleman p. 322. BR §4.1 does not say it (N1). |
| C10 | Sec 6: Coleman Thm 4.1 / Cor 4.1.1 / Thm 4.2 citation, 130–132 | PASS | Accurate to Coleman pp. 320–322. "Apply on the regular model, coefficients constant along chains" is correct. Custody point N6. |
| C11 | Sec 7 direct image sentence, 150–151 | PASS | See C11 below. |
| C12 | Sec 10 G5 wording, 187 | PASS | Editorial. |
| C13 | 11.R1 setting, 200–205 | PASS WITH REMARKS | BR §4.1 and §4.2 are quoted accurately. "Same character lattice as the Néron special-fibre torus" rests on the Néron identification (N1). |
| C14 | 11.R1 step (1): lift and homomorphism, 207–208 | PASS | See C14 below. |
| C15 | 11.R1 step (2): u′ = π^*ξ with no rigidity theorem, 209–215 | PASS WITH REMARKS | See C15 below. Pointer "Coleman 2000 sec 1" should be §4, p. 322 (N1). |
| C16 | 11.R1 step (3): h_1 = h_2, 216–219 | PASS | See C16 below. |
| C17 | 11.R3 fine chart via Γ_1(6l), 227–229 | PASS WITH REMARKS | Č16 (2.6.1) at local line 359; §2.6 at local lines 372–374; §3.8 transversality within the §3.1 setup, which includes Γ_1(n). Applies literally with n = 6l. Pointer wrong (N3). |
| C18 | 11.R3 local-algebra lemma, 229–232 | PASS | See C18 below. |
| C19 | 11.R3 free (Z/3)^× quotient, 233–235 | PASS | See C19 below. |
| C20 | 11.R3 alternative route, 236–237 | PASS | Čes17 Thm 1.5 = 5.13(a) (read), cited in Č16 §3.1. KM85 §2.7 not local. |
| C21 | 11.R3 local quotient, 238–240 | PASS WITH REMARKS | The invariants formula is correct once X is locally Y/G, but rev 2 dropped the argument for that (N2). |
| C22 | 11.R3 explicit stabilizers, 241–246 | PASS | See C22 below. |
| C23 | 11.R3 eigenparameter, 247–251 | PASS WITH REMARKS | See C23 below. Effectiveness of σ on the ring is assumed without justification in rev 2 (N2). |
| C24 | 11.R3 counts h_3, h_1, 251 | PASS WITH REMARKS | Asserted without the orbit count (N5). Not load-bearing: Σ 1/e_x also follows from the mass count at line 108. |
| C25 | 11.R4 pointers, 258 and 262 | PASS | Edixhoven p. 7 (read); M_DRAFT §4 lines 410–415 with its paraphrase note (read). |
| C26 | 11.R4 Conrad–Stein §7.3 support, 263–264 | PASS | Quote verified. The object correctly keeps the primary import flagged as unverified. |
| C27 | 11.R5 orientation, 268–270 | PASS | See C27 below. |
| C28 | R10 fail-closed harness, 284–287 | PASS | See C28 below. |
| C29 | R11 Manin wording, 288–289 | PASS WITH REMARKS | The conclusion c_π = ±1 is right, but the stated derivation is incomplete (N4). |
| C30 | R12 custody, 290–298 | PASS | Accurate about my VERDICT and REPAIR_CHECK. "No statement in sec 0 changes" is verified (byte-identical). |

### Details for the (c) table

- **C2 — I1 Kenku pointer.**
  - ⟨P⟩ with P = (r, r) is a rational cyclic subgroup of order 4. Adding a rational ℓ-isogeny kernel gives a rational cyclic 4ℓ-isogeny.
  - Kenku's list of levels whose X_0(N) has non-cuspidal rational points contains no 4ℓ with ℓ ≥ 5. I did not read Kenku; this is standard.
  - ℓ = 3, 5, 7 are also excluded by the Frobenius computations, which I verified.
  - With the closed 2-isogeny graph (my check F), this gives exactly {E, B, F, G}.
- **C8 — sec 5 residue formula.**
  - Substituting V = 2^e/U turns U^i V^j into 2^{ej} U^{i−j}. So the U⁰ coefficient is Σ_i a_ii 2^{ei}, which converges 2-adically.
  - The normal form is unique (GRAPH_LEMMA Lemma 3.5).
  - The example UV·dU/U has residue 2^e.
  - The residue lies in R and is R-linear.
- **C11 — sec 7 direct image sentence.**
  - Grothendieck / Conrad–Stein functoriality: the image of Hom(X_J, Z) → Hom(Zu, Z), f ↦ f(u), is κZ, because v is primitive.
  - Since n_0 Z = ⟨X_J, u⟩ ⊂ κZ, κ divides n_0.
  - So the image in Z/n_0 has order n_0/κ. This agrees with CS Prop 6.5 and with KAPPA Lemma 4.1.
- **C14 — 11.R1 step (1).**
  - E_J^an is simply connected (BR §4.1: it is the topological universal cover), and G_m^an → E_0^an is a covering map and a local analytic isomorphism. So π∘p_J lifts uniquely with 0 ↦ 1, and the lift is analytic.
  - Both (y, y′) ↦ π̃(y+y′) and (y, y′) ↦ π̃(y)·π̃(y′) lift the same map on the connected (E_J × E_J)^an and agree at (0,0). So π̃ is a homomorphism.
- **C15 — 11.R1 step (2).**
  - π̃ restricted to T^an is an analytic, hence algebraic, character χ_{u′} (BR local line 605).
  - π̃ restricted to J_0 equals the formal Néron map, by uniqueness of lifts on the connected J_0.
  - On the affinoid torus T_0, χ_{u′} reduces to the special-fibre character with the same lattice vector u′. The formal Néron map on T_0 reduces to π^*ξ. Hence u′ = u. Correct.
- **C16 — 11.R1 step (3).**
  - h_1 and h_2 are homomorphisms on E_J(K).
  - They agree on T(K), by (2) and the definition of trop in BR §4.2.
  - Both vanish on J_0(K): trop^{-1}(0) = A_0, and π̃(J_0) ⊂ {|T| = 1}.
  - E(K) = T(K) + J_0(K) holds at BR local line 695, for K algebraically closed, which is the setting used.
  - The identity extends to all Berkovich points by field extension (BR states that formation is compatible with extension of the ground field) or by density and continuity.
- **C18 — 11.R3 local-algebra lemma.**
  - Surjection R[[X,Y]] → A. Its kernel is a height-1 prime in a UFD, hence principal: (f).
  - f mod 2 is XY·unit, so f = XYv + 2g.
  - A is regular exactly when f ∉ (2,X,Y)², which forces g to be a unit.
  - Rescaling x gives xy = 2, and A ≅ R[[x,y]]/(xy−2) because both sides are two-dimensional domains (as in GRAPH_LEMMA Lemma 3.1).
- **C19 — 11.R3 free (Z/3)^× quotient.**
  - A fixed point would need α ∈ Aut(E) with α(P_l) = P_l and α(P_3) = −P_3.
  - Any α ≠ 1 has deg(α−1) = 2 − Tr α ≤ 4 < l, so α cannot fix a point of order l.
  - The action is therefore free, its inertia groups are trivial, and the quotient map is étale even though 2 is not invertible.
  - Completed local rings at points with algebraically closed residue field are unchanged.
  - The same reasoning shows −1 ∈ (Z/l)^× acts trivially on Y.
- **C22 — 11.R3 explicit stabilizers.**
  - **Change-of-variables computation.** It gives u³ = 1, r = s², s⁴ = s and t² + t = s⁶. So there are 24 automorphisms, and the two choices of t differ by [−1]: (x, y) ↦ (x, y+1).
  - **3-division polynomial.** ψ_3 = x⁴ + x (b_2 = b_4 = b_8 = 0, b_6 = 1). Its roots are F_4, and E(F_4)\{O} = E[3].
  - **Action on the four 3-subgroups.** The action is x ↦ a²x + s², i.e. AGL_1(F_4) ≅ A_4, with kernel ±1 and stabilizers of order 3.
  - **Regression.** Confirmed over GF(64): 24 maps preserve E(F_64) bijectively; the induced group on the four subgroups has order 12; each stabilizer has order 3; the kernel is {(1,0,0), (1,0,1)}.
  - **Order-3 elements.** α² + α + 1 = 0 and deg(α−1) = 3. So α is a nonidentity unipotent on E[3], and fixes 2 or 0 lines on E[l].
- **C23 — 11.R3 eigenparameter.**
  - An odd-order element cannot swap the two branches.
  - "Trivial on the cotangent space ⇒ trivial on the ring" is correct for the regular ring B, since gr_m B = k[X,Y] and 3 ∈ R^×.
  - Averaging gives x′ ∈ (x) with x′/x a unit.
  - y′ = 2/x′ has eigenvalue ζ^{-1} automatically.
  - The invariants are R[[U,V]]/(UV−8) when ζ ≠ 1 (GRAPH_LEMMA Lemma 3.5).
- **C27 — 11.R5 orientation.** The convention is consistent with each place it is used:
  - sec 5: s_x·e_x = B − A;
  - sec 6: slope per unit v(U);
  - sec 7 and sec 9: Σ z_x = 0, which needs one common orientation;
  - KAPPA Theorem B: U is a coordinate on C_∞.
- **C28 — R10 fail-closed harness.**
  - With the supplied ecdata, the rev 2 script reproduces `checks/run_all_checks_output.txt` byte-identically.
  - Without ecdata it ends with `DATABASE_STATUS=NOT_REPLAYED_NO_ECDATA`.
  - I made four mutants of the script. Each raised exactly the stated RuntimeError at its first case:
    - mod-4 comparison changed to mod-8: fails at N = 66;
    - component-group 2-part changed from 4 to 8: fails at ell = 11;
    - Manin flag check changed from "1" to "2": fails at N = 66;
    - slope residue set changed from {2} to {0}: fails at ell = 11.
  - The count is labelled "CURVE-PRIME PAIRS".

---

## (d) Referee 1's defect 4 in revision 2

**RESOLVED** (lines 51–55 and 227–237). Referee 1 asked for three things; all three are now present:

1. **A verifiable source for representability, regularity and the local rings of the fine model.**
   - Č16 §2.6 (local lines 372–374) states it for Γ = Γ_1(n), n/2 ≥ 5, and applies literally to Γ_1(6l).
   - Č16 §3.8 gives the transversal crossing.
   - The passage to the (E, C_2, C_3, P_l) model is a free, hence étale, (Z/3)^× quotient.
2. **A regular-node lemma:** stated and proved at lines 229–232.
3. **An étale forgetful step:** lines 233–235. The alternative Γ_0(N)-stack route (lines 236–237) is also correctly cited.

What remains is a line-pointer error (N3) and the dropped quotient argument (N2). Neither concerns defect 4's content.

---

## (e) Changes to sec 0 or to my gate verdicts

**Sec 0 statements:** unchanged. Rev 2 lines 8–16 are byte-identical to rev 1 lines 7–15, and I do not change any statement of Theorem P or Corollary N.

**Gate verdicts (revision 1 → revision 2):**

| Gate | Rev 1 | Rev 2 | Reason |
|---|---|---|---|
| G1 | PASS WITH REMARKS | PASS WITH REMARKS | Unchanged. D6–D8 resolved; new remarks N2, N3, N5. |
| G2 | PASS WITH REMARKS | PASS WITH REMARKS | Unchanged. D1–D4 resolved; new citation remark N1. |
| **G3** | PASS WITH REMARKS | **PASS** | D5 and D11 resolved; no new issue. The pointer "annular residues compatible with base change (BR sec 5.1)" is unchanged from rev 1 and trivial: BR §5.1 covers skeleta, and residue compatibility is elementary. |
| G4 | PASS WITH REMARKS | PASS WITH REMARKS | Unchanged. D9 resolved; D12 partially resolved; N3 (I8 page pointers). |
| G5 | PASS | PASS | Unchanged; the new direct-image sentence is verified. |
| G6 | PASS | PASS | Unchanged. |
| G7 | PASS WITH REMARKS | PASS WITH REMARKS | Unchanged. D10 and D14 resolved; new remark N4; W-audit custody item declared open. |

---

## (f) New defects in revision 2

### BLOCKING

None.

### N1 [CITATION] — lines 128–130 (sec 6) and 202–203, 212–213 (11.R1)

**What is wrong.** Two sentences attribute the Néron identification to Baker–Rabinoff §4.1: "BR sec 4.1 (A_0 has special fibre the Neron identity component …)" and "the special fibre of J_0 is the Neron identity component J^0_k (BR sec 4.1; Coleman 2000 sec 1)". BR §4.1 does not mention Néron models at all. In the local text, Néron models appear only in §2.1–2.7 (lines 150, 214, 316), where BR notes they "are not available in the non-Noetherian situation".

**What is true.** The identification follows from BR §4.1's *uniqueness* clause applied to the generic fibre of the formal completion of the Néron identity component, but that argument is not written. It is stated explicitly by Coleman 2000 in §4, p. 322: "π|G⁰ is an isomorphism of G⁰ with the connected component of the origin in the rigid space associated to the formal completion of 𝒩 along its reduction". Coleman §1 does not state it, so line 213's pointer to "sec 1" misses the right place. Line 130 says "secs 1, 4", which does include p. 322.

**What would be needed.** Cite Coleman p. 322 (or BLR), or write the uniqueness argument. The mathematics is unaffected.

### N2 [NON-BLOCKING, regression] — 11.R3 lines 238–240 and 247 (sec 4 lines 101 and 107 unchanged)

**What is wrong.** Rev 2 deleted two justifications that rev 1 had (rev 1 lines 205–206 and 209–210):
- **(a)** Why X_R is locally Y_R/G near supersingular points: Y → X is finite and G-invariant, and Y/G → X is finite and birational onto the normal X, hence an isomorphism.
- **(b)** Why the order-3 stabilizer acts effectively on the completed local ring: G acts faithfully on the integral Y, and the Krull intersection theorem passes this to the completion.

Rev 2 now simply asserts "the completed local ring of X_R at its image is (Ô_{Y,y})^{G_y}" and speaks of the "effective order-3 stabilizer σ".

**Why it is non-blocking.** Both statements are true. GRAPH_LEMMA Lemmas 3.2 and 3.4, cited at line 252 as the N = 2p analogues, contain proofs that transfer verbatim. Still, at the level of wording this reopens referee 1's defect 8 (X_R = Y_R/G), which rev 1 had closed.

**What would be needed.** Restore the two sentences, or state that GRAPH_LEMMA Lemmas 3.2 and 3.4 apply verbatim with H replaced by G.

### N3 [CITATION] — line 227; lines 38–39

**What is wrong.**
- **Line 227:** "sec 2.6 (L377-378)". In the local Č16 text (`stevens_v2.pdf.txt`, sha256 `f8ba8212…`), the Γ_1(n) regularity sentence is at lines 372–374. Lines 377–378 hold (2.6.2) and the Ω-line-bundle sentence.
- **Lines 38–39 (I8):** "Edixhoven … p. 7 …: C_inf contains inf, C_0 contains 0, W_d swaps the components iff 2 | d, Tate-curve completion at inf". Only the first item is on p. 7. The W_d statement is on p. 9, and the Tate-curve completion is on p. 4 (§2.1).

**What would be needed.** Correct page and line pointers.

### N4 [NON-BLOCKING] — R11, lines 288–289

**What is wrong.** "c_pi = +-1 follows by applying it at every prime of the squarefree conductor N." Applying Thm 1.2 only at primes dividing N says nothing about ord_p(c_π) for p ∤ N. The theorem must be applied at every prime p (for squarefree N, p² ∤ N holds for all p). Alternatively, quote its own "In particular … squarefree … c_π = ±1" sentence (1703.02951v3, local lines 62–63). I7 at line 34 is correct and unaffected.

**What would be needed.** A wording fix.

### N5 [NON-BLOCKING] — 11.R3 line 251

**What is wrong.** The values h_3 = 2 (for l ≡ 1 mod 3) and h_1 = (l−1)/3 or (l+1)/3 are asserted without the orbit count. The count is short: each of the four order-3 subgroups of A_4 fixes one C_3 and two C_l, and the resulting 8 fixed pairs form 2 orbits of size 4.

**Why it is non-blocking.** Only Σ 1/e_x and the oddness of e_x are used. Σ 1/e_x also follows from the mass count at line 108. The object's checks (sec 3) cover l = 11, 19, 43.

**What would be needed.** One sentence with the count.

### N6 [NON-BLOCKING, custody] — lines 38 and 132, against R9 lines 279–281

**What is wrong.** The object cites "read by referee_2" as the support for Edixhoven arXiv:math/0312019v1 and Coleman 2000. Neither text is in the object's `src/`, and a referee's reading is not a primary text in the object. R9 also still lists "Edixhoven 2006 Prop 2.5 (as cited …)" and "Coleman 2000" as unverified, which is inconsistent with lines 38 and 132.

**What would be needed.** Add local copies with digests to `src/`, or keep both explicitly in R9 as unverified without citing the referee's reading.

### N7 [NON-BLOCKING, editorial] — line 184 (G2 gate text); lines 46–48 (I10)

**What is wrong.**
- The G2 gate text still reads "BR Thm 2.3 / Cor 5.6 / Prop 6.1 as quoted; the Raynaud functoriality for pi".
- I10 still lists Thm 2.3.
- Sec 6 and 11.R1 no longer use Thm 2.3 or an imported "Raynaud functoriality".

**What would be needed.** Update the gate text and I10.

---

## Files read for this delta, and commands run

**Digests** (sha256). All were read in full unless noted.

| sha256 | File | Notes |
|---|---|---|
| `c5d806de…ab791` | `PROOF.md` (rev 2) | |
| `953d4d6c…a6ffc` | `history/revision_1/PROOF.md` | |
| `58b0b61e…dc53a521` | `history/DIFF_rev1_to_rev2.diff` | First 5 lines only; my own diff was used instead. |
| `782d706b…8ab0` | `checks/run_all_checks.py` (rev 2) | Read via diff against rev 1. |
| `c3b39aff…b9e0` | `checks/run_all_checks_output.txt` (rev 2) | |
| `1ad06d48…c1c7d` | `history/revision_1/checks/run_all_checks.py` | |
| `6b642b82…86d5b` | `history/revision_1/checks/run_all_checks_output.txt` | |
| `544e1c9c…d7a84f` | `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/reports/optimal_cusps/IDENTITY_COMPONENT_REVIEW.md` | |
| `0ab81dc1…128a68` | `CODEX_H41_SEED_RESEARCH_FREEZE_001/MANIFEST.sha256` | grep only. |
| `dfa6291c…5fbfc5` | `H41_W_MECHANISM_AUDIT.md` | Digest re-verified. |

I re-checked passages in the local Č16, BR and CS texts by line number (grep and sed): Č16 lines 359 and 370–380; BR lines 150, 214, 316 and 605; CS lines 257–259 and 476–478. Coleman pp. 315–326 and Edixhoven pp. 1–9 had already been read for VERDICT.md. `src/author_recheck_2026-09-16/` was not opened.

**Commands.** Every compute command was run under `nice -n 19`, one at a time, after `uptime`; the highest 1-minute load seen was 4.49.
1. `diff history/revision_1/PROOF.md PROOF.md`, saved as `referee_2/checks_delta_rev2/referee2_own_diff_rev1_to_rev2.txt`. Section-by-section identity checks with `diff` of `sed -n` ranges.
2. The rev 2 check script with ecdata: output IDENTICAL to `checks/run_all_checks_output.txt`. Saved as `rerun_rev2_checks_with_ecdata.txt`.
3. The rev 2 check script without ecdata: `DATABASE_STATUS=NOT_REPLAYED_NO_ECDATA`. Saved as `rerun_rev2_checks_no_ecdata.txt`.
4. `r3_automorphisms_f64.py`: the GF(64) verification of the 11.R3 automorphism claims (output saved).
5. `make_mutants.py`, then four mutant runs with ecdata. All raised the expected RuntimeError. Results are in `mutation_test_summary.txt` and the `mutant_*.out` files.
6. `shasum -a 256` of the files listed above.

All delta artifacts are in `/Users/bsm/H41_MOD4_SUCCESSOR_PROOF_2026-09-16/referee_2/checks_delta_rev2/`. My VERDICT.md, FILES_READ.sha256 and REPAIR_CHECK.md, which cover revision 1, were not modified.
