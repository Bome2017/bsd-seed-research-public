# Referee 1 delta review: PROOF.md rev 0 → rev 2 (no repair)

Rev 0: `history/revision_0/PROOF.md`, sha256 `0cf7a5f9e598d8d8…` (the text I refereed in `VERDICT.md`).
Rev 2: `PROOF.md`, sha256 `c5d806defa3bc55da33cadb2cfad57c1d2e7e09c883c82dd371f814e1c0ab791`.
The supplied `history/DIFF_rev0_to_rev2.diff` is identical to `diff -u rev0 rev2`. `MANIFEST.sha256` verifies.
Line numbers `Lnn` are rev 2 lines.

Not read: `referee_2/`; the content of `src/author_recheck_2026-09-16/` (only its file names, and its hash lines in `MANIFEST.sha256`, were seen); the drafts and audit in `src/`. Nothing outside `referee_1/` was written by me. The WebFetch tool cached one arXiv PDF in the session tool-results directory (see (f)).

## (a) Delta verdict

**ACCEPT WITH REMARKS. BLOCKING defects: 0.**

Summary:
- Sec 0 is byte-identical between rev 0 and rev 2. So are sec 2, sec 3, sec 4 and sec 8 (section-wise sha256 compared).
- All new mathematics checks.
- One new CITATION defect (N1): Lemma R(2) and sec 6 attribute to BR §4.1 the fact that BR's compact formal subgroup A_0 has the Néron identity component as special fibre. BR §4.1 does not say this; the fact is true and load-bearing.
- Of my defects 1–15: 13 RESOLVED, 2 PARTIALLY RESOLVED (1, 8), none NOT RESOLVED.

## (b) Status of referee_1 defects 1–15 in rev 2

1. **Raynaud functoriality under π: PARTIALLY RESOLVED.**
   - Lemma R (L199–220) proves the needed identity on universal covers (L206), and sec 6 uses it (L134–135, L143).
   - Steps (1) and (3) check against BR (L425–428, L461–466, L604–605, L695, L878–879).
   - Residue: step (2) needs BR's A_0 for J to be the formal completion of the Néron identity component, and this is cited to a source that does not state it (N1).
2. **Pairing identification: RESOLVED.**
   - L127–128 and R2 L221–225 give the chain BR (4.5.2) (src:L552–554, L674), Thm 2.9 (src:L863–864), Rem 6.3 (src:L857–858, which cites Coleman 2000), plus the coarse-to-regular passage.
   - BR §5.1 (src:L639–644) allows arbitrary edge lengths val(ϖ_x), so the coarse model is admissible directly.
   - Remarks: N4 (base-change wording); Rem 6.3's content is Coleman's (not local).
3. **"Lemma 4.1": RESOLVED.** CS Prop 6.5 is cited at L149–151 and L173, and in G5 at L187. The direct computation (image of f ↦ f(u) is κZ, image κZ/n_0Z, κ | n_0) is correct.
4. **I11 / fine-model citation: RESOLVED.**
   - Primary route (L51–55, L226–235), checked against local text:
     - Česnavičius 1604.02165 (2.6.1) (src:L357–359);
     - the regularity of X_{Γ_1(n)} for n/2 ≥ 5 (src:L372–375);
     - transversal crossing (src:L684–687, [DR73 V.1.16(ii)]);
     - smooth components (src:L360–363);
     - the local-algebra lemma (= pinned GRAPH_LEMMA Lemma 3.1);
     - the free (Z/3)^× quotient.
   - The alternative route (Ces17 5.13(a), KM85 §2.7) is not local and not needed.
   - Remark N2: wrong line locator.
5. **Cusp 0 on the étale component: RESOLVED, and verified by me.**
   - Edixhoven arXiv:math/0312019v1 p. 7 (read by me; see (f)) says C_∞ contains the cusp ∞ "and hence C_0 the cusp 0".
   - It identifies C_∞ via (E, G, ker F) and C_0 via (E^(p), G^(p), ker V).
   - It also says "The automorphism W_N of X interchanges ∞ and 0."
   - Rev 2 uses this at L37–42, L257–259, L116 and L267–268.
6. **Tate completion / q-expansion principle at ∞ for Γ_0(N): RESOLVED (citation level).**
   - At L37–42 and L260–262 rev 2 cites Edixhoven 2.5 as used in 1703 Lemma 5.4 (src:L1078–1087) and CNS §1.
   - Edixhoven p. 6 (read by me) carries out the completion argument at a smooth closed point, Ô = W(k)[[t]], applied at the cusp ∞. The identification t = q is implicit there.
   - Remark N5: the S_2 citation concerns holomorphic forms, while δ ∈ Ω(cusps).
7. **w_{N/2}, ε_p = −a_p: RESOLVED.**
   - R4 L254–257: an odd-degree isogeny carries connected (resp. étale) order-2 subgroups to connected (resp. étale) ones, so w_M preserves X^μ and X^ét. Correct.
   - The w_2 swap is supported by 1703 Lemma 5.4 proof (src:L1085–1086) and 1604 Lemma 2.7 proof. W_N as an automorphism of X is in Edixhoven p. 7.
   - Atkin–Lehner (L262–264): primary source (Atkin–Lehner 1970 / Li 1975) not local. The local support CS §7.3 "Frob_p = −W_p" (src:L476–477) is quoted accurately.
8. **X_R = Y_R/G: PARTIALLY RESOLVED.**
   - R3 L238–240 states the decomposition-group computation (completed local ring = invariants of the stabilizer, residue field algebraically closed). That is correct.
   - The identification of the coarse DR model with Y_R/G near the orbit is still only asserted (sec 4 L101, unchanged). It is supported only by the pointer "N = 2p analogues: GRAPH_LEMMA Lemma 3.2" (L252).
   - That argument transfers verbatim (Y proper, Y/G → X finite and birational onto normal X), but it is not written for N = 6l. NON-BLOCKING.
9. **Linearization, effectiveness, resolution: RESOLVED.** Explicit stabilizers (L241–246), eigenparameter (L247–251) and resolution (L252) are all checked in (c). Residue N7: effectiveness is assumed.
10. **Base change / punctured curve: RESOLVED.** L115–116 and R5 L265–270: C_2, D = {0, ∞}, V = {C_∞, C_0}, rays attached, and one global orientation (v(U) = 0 at the C_∞ end).
11. **I2 on the positive branch: RESOLVED.** I2 L22–23 and R8 L276–278: formulas valid for r = ±2^m (my earlier check C). Remark N6.
12. **BH 2.13 on the negative branch: RESOLVED.** R6 L271–274 matches my independent verification.
    - #E(F_3) = 4, so a_3 = 0 (re-checked for m = 3..17).
    - Frobenius at 5 excludes 3 and 7; Frobenius at 3 (disc −12 ≡ 3 mod 5) excludes 5.
    - Witnesses: p for residual 2, and 2 for residual p (0 < 4(m−2) < p).
    - q is ordinary.
13. **Custody pins: RESOLVED; all pins verified.**
    - KAPPA_PARITY_PROOF.md `825c91d2…` and GRAPH_LEMMA.md `290914001…` are byte-identical in `~/H41_KAPPA_PARITY_2026-09-14`, in `H41_KAPPA_PARITY_ADDENDUM_017/R/`, and inside `H41_KAPPA_PARITY_ADDENDUM_017.tar.gz` (sha256 `a0a62efb21a5…`).
    - IDENTITY_COMPONENT_REVIEW.md is `544e1c9c…` and the W audit is `dfa6291c…` (L28–30).
14. **Universal-cover notation: RESOLVED.** L134, L206, L220.
15. **"Proved optimal" wording: RESOLVED.** L193–194 now says "database flags, not re-proved". The phrase "proved optimal per Cremona's documentation" is not verified by me.

## (c) New mathematical claims (rev 0 → rev 2)

| # | Claim (rev 2 lines) | Verdict | Basis |
|---|---|---|---|
| 1 | Sec 5 residue = constant Laurent coefficient after V = 2^e/U; for g = Σa_ij U^iV^j it is Σ_i a_ii 2^{ei}; UV·dU/U has residue 2^e (L120–122) | PASS | Substitution U^iV^j = 2^{ej}U^{i−j}; the Laurent map is injective (normal form). Regression sample. |
| 2 | Sec 6: Conrad–Stein's X_J (Néron special-fibre torus) is BR's M (L128–130) | PASS WITH REMARKS | True, but mis-cited (N1). BR §4.1 (src:L422–460) never mentions Néron models; BR mentions Néron only at src:L150, L214, L316. |
| 3 | Sec 6: Coleman 2000 Thm 4.1 / Cor 4.1.1 / Thm 4.2 give the residue–character identity (L130–132) | PASS WITH REMARKS | Not local; not verified. Not load-bearing, since Lemma R replaces it. |
| 4 | Lemma R setting (L200–205) | PASS WITH REMARKS | Matches BR §4.1–4.2 (src:L422–447, L461–466) and BR's proof of Thm 2.9 (src:L878–879), except the added "(same character lattice as the Neron special-fibre torus)" at L202–203 (N1). |
| 5 | Lemma R (1): unique identity-preserving lift π̃ is an analytic homomorphism (L207–208) | PASS | E_J^an is the universal cover and G_m^an → E_0^an is a covering (BR src:L425–428). Uniqueness of lifts applied to the multiplication diagram. Wording remark N8. |
| 6 | Lemma R (2): π̃ restricted to T^an is an algebraic character u', and u' = π*ξ (L209–215) | PASS WITH REMARKS | "Analytic characters are algebraic" (src:L604–605). The completion of the Néron map agrees with π̃ on the connected J_0 by uniqueness of lifts. Reduction of χ_{u'} gives the same lattice vector. Needs A_0(J) = generic fibre of the completed Néron identity component, cited to BR §4.1 and Coleman §1 (N1). |
| 7 | Lemma R (3): h_1 = h_2 on T(K) and on J_0(K), E(K) = T(K)+J_0(K), then all of E_J^an (L216–219) | PASS | BR src:L461–466 (trop on T), L465 (trop⁻¹(0) = A_0), L695. The alternative route (bounded subgroup of R is 0) does not need N1. |
| 8 | R2 chain and coarse-vs-regular statement (L221–225) | PASS WITH REMARKS | As defect 2, with remark N4. |
| 9 | R3 fine chart via Γ_1(6l) regular scheme (L227–229) | PASS | Local Česnavičius text as in defect 4. Locator N2. |
| 10 | Local-algebra lemma (L229–232) | PASS WITH REMARKS | Correct: the kernel is a height-1 prime of the UFD R[[X,Y]], f = XYv + 2g, and regularity forces g to be a unit. Compressed: residue field k and the final "surjection of 2-dim domains is an isomorphism" step are implicit (N9). The full proof is in pinned GRAPH_LEMMA Lemma 3.1. |
| 11 | Free (Z/3)^× quotient is finite étale of degree 2, including in residue characteristic 2 (L233–235) | PASS | Suppose (E,C_2,−P_3,P_l) ≅ (E,C_2,P_3,P_l). Then some α fixes P_l, so α = 1, contradicting −P_3 ≠ P_3. The action is free at all geometric points, so inertia is trivial everywhere and the quotient is étale (a Z/2-torsor). Completed local rings are unchanged. |
| 12 | Rigidity degree bound deg(α−1) = 2 − Tr α ≤ 4 < l (L234) | PASS | deg(α−1) = deg α − Tr α + 1. Regression: det(α−1) ≢ 0 mod l for all 23 Hurwitz units α ≠ 1, l = 11, 19, 43. |
| 13 | Alternative route (Ces17 5.13(a), KM85 §2.7) (L236–237) | PASS WITH REMARKS | Not local; not load-bearing. 1604 §3.1 (src:L499–501) does cite Čes17 5.13(a). |
| 14 | Local quotient (L238–240) | PASS WITH REMARKS | Decomposition-group formula correct; the global identification is by analogy only (defect 8). |
| 15 | Explicit automorphisms of y²+y = x³ (L241–243) | PASS | Hand check: the substitution returns y²+y+x³ using a³ = 1, s⁴ = s, t²+t = s⁶. Regression: exactly 24 automorphisms; t ∈ F_4; the t-pairs differ by [−1]; ψ_3 ≡ x⁴+x mod 2 with roots F_4; the induced group on the four 3-subgroups has order 12 (= AGL_1(F_4) ≅ A_4); point stabilizers have order 3. |
| 16 | Order-3 α: α²+α+1 = 0; 2 or 0 fixed lines on E[l]; nonidentity unipotent on E[3] (L244–246) | PASS | End(E) has no zero divisors. (α−1)² = −3α ≡ 0 on E[3], and deg(α−1) = 3 < 9. |
| 17 | Eigenparameter and invariants R[[U,V]]/(UV−8) (L247–251) | PASS WITH REMARKS | Faithful tangent action: averaging gives σ-fixed generators of m, hence σ = id. Eigen-average x' = cx with c ≡ 1; y' = 2/x' = y/c; invariants R[[x'³]] ⊕ y'³R[[y'³]]. Effectiveness of σ is assumed (N7). |
| 18 | Counts h_3 = 2 or 0, h_1 = (l∓1)/3, so Σ1/e_x = (l+1)/3 (L251) | PASS | Distinct order-3 subgroups fix disjoint pairs (two together generate A_4, which contains order-2 elements). Orbit sizes 4 and 12. Regression at l = 11, 19, 43, 67, 131. |
| 19 | Minimal resolution of UV = 2^e (L252) | PASS | Standard (A_{e−1}); GRAPH_LEMMA Lemma 3.6 for e = 3. |
| 20 | R4: w_2 swaps and w_M preserves the components, so w_N swaps them; ∞̄ ∈ X^μ; 0̄ ∈ X^ét (L254–259) | PASS | Edixhoven p. 7 (read by me), 1703 Lemma 5.4 proof, and the odd-isogeny argument. Remark N3. |
| 21 | R4 q-expansion principle citations (L260–262) | PASS WITH REMARKS | N5. CNS §1 is not local. |
| 22 | R4 a_p = −ε_p (L262–264) | PASS WITH REMARKS | Primary source not local; CS §7.3 quoted correctly (src:L476–477). |
| 23 | R5 analytic setting and orientation (L265–270) | PASS | BR §5.1 (src:L652–657) for skeleta and retractions. Residues are trivially compatible with base change. |
| 24 | R6 BH 2.13 on the negative branch (L271–274) | PASS | As defect 12. |
| 25 | R8 I2 for both signs (L276–278) | PASS | Symbolic Δ and c_4 parity (my earlier check C). Custody remark N6. |
| 26 | R10 fail-closed harness (L284–287) | PASS | The rerun output matches the recorded output exactly. A mutated copy (l = 13) raises `RuntimeError: component group check failed at ell=13` (exit 1). |
| 27 | R11 Manin wording (L288–289) | PASS | 1703 Thm 1.2 applied at each prime of the squarefree N. |
| 28 | I1 pointer: a rational l-isogeny plus ⟨(r,r)⟩ gives a rational cyclic 4l-isogeny, excluded by Kenku for l ≥ 5; l = 3 by Frobenius (L19–21) | PASS WITH REMARKS | Correct: gcd(4, l) = 1, and 4l is not in Kenku's list for any prime 5 ≤ l < 2000 (list-membership check), while 12 is. Kenku's theorem is not local. |
| 29 | I9 standing hypothesis (L44–45) | PASS | CS src:L86–89, L256–258. |
| 30 | Sec 7 image via CS Prop 6.5 plus the direct computation (L149–151); sec 9 (L173) | PASS | CS src:L395–423. |
| 31 | I3–I5 pins (L28–30) and negative pins (L60–63) | PASS | Hashes verified; see defect 13. |

## (d) Sec 0 and gate verdicts

- **Sec 0.** No statement changes; sec 0 is byte-identical between rev 0 and rev 2.
- **Gate verdicts:**
  - **G1: PASS WITH REMARKS (unchanged).** Residue: defect 8 (global Y_R/G identification by analogy only), N2, N7.
  - **G2: PASS WITH REMARKS (unchanged).** Residue: N1, N4; Coleman 2000 (behind BR Rem 6.3) not local.
  - **G3: PASS WITH REMARKS → PASS.** Defect 10 resolved; the cusp placement behind the rays is verified from Edixhoven p. 7; the residue wording is correct.
  - **G4: PASS WITH REMARKS → PASS.** Defects 6 and 7 resolved. The w_M argument is correct, W_N is an automorphism by Edixhoven p. 7, and the completion principle at ∞ is in Edixhoven p. 6.
  - **G5: PASS WITH REMARKS (unchanged).** All G5-specific defects (3, 11, 13) are resolved. It still inherits N1, because ⟨X_J,u⟩ = n_0Z is combined with slope coordinates of the BR character.
  - **G6: PASS (unchanged).** Sec 2 is byte-identical.
  - **G7: PASS WITH REMARKS → PASS.** Defects 11, 12, 13 and 15 resolved; pins verified; the Kenku pointer is correct.
- **Overall.** The rev 0 verdict line "PASS WITH REMARKS, 0 BLOCKING" carries over to rev 2 through this delta.

## (e) New defects in rev 2

- **N1 — CITATION.** L129, L202–203, L212–213; also L199 and L281.
  - **What is wrong:**
    - "BR sec 4.1 (A_0 has special fibre the Neron identity component …)", "(same character lattice as the Neron special-fibre torus)", and "the special fibre of J_0 is the Neron identity component J^0_k (BR sec 4.1; Coleman 2000 sec 1)" attribute to BR §4.1 something it does not state. BR §4.1 (src:L422–460) defines A_0 intrinsically and mentions no Néron model.
    - The identification is load-bearing. It is needed for u' = π*ξ in Lemma R(2), and hence to combine CS Lemma 6.3 with BR's slope coordinates.
    - The header claim "the Bosch–Lutkebohmert dependency is removed" (L199) is overstated, and R9 (L281) still lists BL1991.
  - **Needed:** either an explicit derivation or a verifiable source (Coleman 2000 §1 or Bosch–Lütkebohmert; neither is local). The derivation would show that over Frac R the Raynaud generic fibre of the formal completion of the Néron identity component 𝒥⁰ is a compact formal analytic subgroup with semi-abelian special fibre 𝒥⁰_k, hence equals A_0 by BR's uniqueness clause (src:L422–425), with formation compatible with ground-field extension (src:L460).
  - I judge the statement true, so this is not BLOCKING.
- **N2 — NON-BLOCKING.** L227: locator "sec 2.6 (L377-378)". The regularity sentence is at stevens_v2.pdf.txt L372–375; L377–378 is the (2.6.2) identification. The content is correct.
- **N3 — NON-BLOCKING.** L38–39: "W_d swaps the components iff 2 | d" is attributed to Edixhoven p. 7. It does not appear on pp. 5–8, where p. 7 has only "The automorphism W_N of X interchanges ∞ and 0". Not load-bearing, because R4 argues w_M and w_2 separately.
- **N4 — NON-BLOCKING.** L127–128 and L222–223: Rem 6.3 is the case Λ = Z, and Grothendieck's pairing needs the discretely valued field. Sec 6 now "works over C_2" but does not say that the pairing comparison is made over Frac R and then transported (BR src:L460, L491). Only wording.
- **N5 — NON-BLOCKING.** L260–262: Edi06 Prop 2.5 as used in 1703 Lemma 5.4 concerns S_2 (holomorphic differentials). Sec 3 applies the q-expansion principle to δ ∈ Ω(cusps), which has a simple pole at ∞. The operative fact is the completed stalk at ∞̄ with generator dq/q. Edixhoven p. 6's completion argument covers it verbatim after replacing dq by dq/q; CNS §1 is not local and is only paraphrased in ADDENDUM_015.
- **N6 — NON-BLOCKING (custody).** L278: minimality at 2 is supported by "referee_1 check C", which is a referee's regression script, not part of the proof object. The c_4 values of the four minimal models are elementary and should be written in the object.
- **N7 — NON-BLOCKING.** L247 (and sec 4 L107): effectiveness of the order-3 stabilizer on Ô_{Y,y} is assumed ("effective"). The argument is: Y_R is integral and G acts faithfully on Y_Q (GRAPH_LEMMA Lemma 3.4 for N = 2p). It is not written for N = 6l.
- **N8 — NON-BLOCKING.** L207: "p_{E_0} a local isomorphism". Lifting needs the covering property, which holds because G_m^an is the topological universal cover (BR src:L425–428). Only wording.
- **N9 — NON-BLOCKING.** L231–232: "replacing x by −xv/g gives f = xy − 2" compresses the change of presentation. The residue field k = R/2 and the isomorphism of the two 2-dimensional domains are implicit; they are proved in the pinned GRAPH_LEMMA Lemma 3.1.

## Statements still not verified from a primary source

- Coleman 2000 (Thm 4.1, Cor 4.1.1, Thm 4.2, §§1, 4, and the content of BR Rem 6.3).
- Česnavičius–Neururer–Saha §1.
- Ces17 Thm 1.5 = 5.13(a); KM85 §2.7; DR73 V.1.16 and VI.6.9 (only as quoted by Česnavičius).
- Kenku's classification; Atkin–Lehner 1970 and Li 1975.
- Cremona's optimality documentation.
- Everything already listed in `VERDICT.md` (d) that rev 2 does not newly cite.
- Edixhoven p. 7 and pp. 5–6 are now **verified** by me. Edixhoven's own claim at p. 7 rests on its references, which I did not read.

## (f) Commands run

The load was checked with `uptime` before each computation (1-minute load 3.3–4.9). Every run used `nice -n 19`, one process at a time, and nothing took longer than 10 s.
- `shasum -a 256 PROOF.md history/revision_0/PROOF.md`; `diff -u` compared with the supplied diff (identical); `shasum -a 256 -c MANIFEST.sha256` (all OK); section-wise sha256 of sec 0, 2, 3, 4, 8 in rev 0 and rev 2 (identical).
- `nice -n 19 python3 checks/run_all_checks.py …/ecdata/opt_man`: exit 0; output in `referee_1/delta_rev2_run_all_checks_rerun.txt`, identical to `checks/run_all_checks_output.txt`.
- Mutation test: `sed 's/^for l in (11, 19, 43):/for l in (11, 13):/'` into `referee_1/delta_rev2_mutation_run_all_checks.py`, then run: exit 1, `RuntimeError: component group check failed at ell=13` (in `referee_1/delta_rev2_mutation_output.txt`).
- `nice -n 19 python3 referee_1/delta_rev2_checks.py`: `DELTA_REV2_CHECKS_OK`, output in `referee_1/delta_rev2_checks_output.txt`. It covers:
  - the explicit automorphism group and ψ_3;
  - the free quotient at l = 11, 19, 43;
  - h_1 and h_3 at l = 11, 19, 43, 67, 131;
  - the residue formula;
  - the Kenku 4l list;
  - #E(F_3) = 4 on the negative branch.
- Pin hashes:
  - `shasum -a 256` on IDENTITY_COMPONENT_REVIEW.md;
  - on H41_KAPPA_PARITY_ADDENDUM_017/R/{KAPPA_PARITY_PROOF,GRAPH_LEMMA}.md;
  - on H41_KAPPA_PARITY_ADDENDUM_017.tar.gz;
  - `tar -xzOf … | shasum -a 256` for the two files inside the archive.
- `grep -n` on the BR, Česnavičius and CS local texts for the cited locators.
- WebFetch of `https://arxiv.org/pdf/math/0312019v1`. The tool itself cached the PDF at `~/.claude/projects/-Users-bsm/2c6faf50-99be-4089-8939-52abc4c35596/tool-results/webfetch-1789615540555-wuogkz.pdf` (sha256 `b6ebb9ad0a7ee27a414829cb52be7c5ed805ead9a817baf7fc5858e7ebace781`). I read pages 1 and 5–8 of it.
- Hashes of the files used in this delta: `referee_1/DELTA_FILES_READ.sha256`.
