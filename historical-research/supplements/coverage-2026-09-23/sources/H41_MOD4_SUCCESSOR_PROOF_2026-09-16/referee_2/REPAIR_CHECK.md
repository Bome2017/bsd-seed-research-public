# Referee 2 — check of the revision 1 repairs against referee 1's defects

## What was compared

- **Referee 1's verdict:** `referee_1/VERDICT.md`, sha256 `d6f1f5350a84d57db897e6f7125a3432ec98ddaab6ec96e41be55bd2aba9adc6`. It reviewed **revision 0**, sha256 `0cf7a5f9…`, which is kept at `history/revision_0/PROOF.md`.
- **Revision under check:** revision 1, `PROOF.md`, sha256 `953d4d6c2fb711a53fc7c3c6ad2afe69cad8e4589092af30d26ccf3bacaa6ffc`.
- **Line numbers:** "line N" means a line of revision 1. Referee 1's own line numbers refer to revision 0.
- **Diff:** I ran `diff history/revision_0/PROOF.md PROOF.md`, read-only. The only changes are:
  - the header;
  - I2, I8 and I11;
  - the digest pins at lines 51–54;
  - sec 6, lines 116–119 and 128;
  - sec 7, lines 134–135;
  - sec 9, lines 157 and 160;
  - sec 10, line 178;
  - the new sec 11, lines 182–239.
- **Order of work:** `referee_2/VERDICT.md` and `referee_2/FILES_READ.sha256` were written before I opened `referee_1/` or `history/`. The verdict has not been revised since.

## Status of referee 1's defects 1–15

| # | Referee 1 severity | Status in revision 1 | Revision 1 lines | Notes |
|---|---|---|---|---|
| 1 | CITATION: functoriality trop(π(y))(ξ) = trop(y)(u) had no source or proof | **RESOLVED** | 119, 128, 183–195 (Lemma R) | See note 1. |
| 2 | CITATION: "BR Thm 2.3 ⇒ X_J = H_1(Γ,Z) with length pairing"; wrong theorem and identification | **RESOLVED** | 116–118, 196–200 | See note 2. |
| 3 | CITATION: undefined "Lemma 4.1 form (I9 + K2)" for the image of Φ(π) | **RESOLVED** | 134–135, 157 | See note 3. |
| 4 | CITATION: fine model's representability, regularity and local rings were cited to KM 13.4.7 | **PARTIALLY RESOLVED** | 43–46, 201–205, 211 | See note 4. |
| 5 | CITATION: nothing placed 0̄ on the étale component | **RESOLVED** | 31–35, 212–218 | See note 5. |
| 6 | CITATION: Tate-curve completion R[[q]] at ∞̄ was cited only for Γ_1(n) | **RESOLVED** | 31–35, 219–221, 235–237 | See note 6. |
| 7 | NON-BLOCKING: w_{N/2} preserving the components, and ε_p = −a_p, were uncited | **RESOLVED** | 213–216, 221–222 | See note 7. |
| 8 | NON-BLOCKING: no argument for X_R = Y_R/G or for completion = invariants | **RESOLVED** | 205–207, 211 | See note 8. |
| 9 | NON-BLOCKING: one-line linearization, branches and effectiveness; resolution of UV = 2³ uncited | **RESOLVED** | 207–211 | See note 9. |
| 10 | NON-BLOCKING: base change to an algebraically closed field, punctured curve and vertex set unstated | **RESOLVED** | 116, 223–226 | See note 10. |
| 11 | CITATION: I2 used for both signs but supported only for r = +2^m | **RESOLVED** | 19–20, 232–234 | See note 11. |
| 12 | NON-BLOCKING: BH 2.13 on the negative branch deferred to the unread vertex audit | **RESOLVED** | 159–160, 227–230 | See note 12. |
| 13 | NON-BLOCKING: negative inputs called "sealed" with no digest pins | **RESOLVED** | 51–54, 231 | See note 13. |
| 14 | NON-BLOCKING: the identity must be stated on universal covers | **RESOLVED** | 119, 195 | The identity is now stated on universal covers, with an explicit caveat about skeleta. |
| 15 | NON-BLOCKING: "proved optimal with Manin constant 1" rested on database flags | **RESOLVED** | 177–178 | Now "carries Cremona's flag opt = 1 … and mc = 1; database flags, not re-proved". |

**Tally:** 14 RESOLVED, 1 PARTIALLY RESOLVED (defect 4), 0 NOT RESOLVED. The partial item is at citation level and was already non-blocking.

### Notes

1. **Defect 1 — Lemma R.**
   - Lemma R proves the identity in four steps: Néron functoriality; rigidity of the formal torus; lifting to the Raynaud cover; computation of trop.
   - My G2 check found the lemma correct.
   - Both points referee 1 asked for are covered: π̃(A_0(J)) ⊆ {|T| = 1} is step (1), and the character is u by steps (2) and (4).
   - The repair adds two new defects:
     - it cites Conrad–Stein Cor 8.5 (about ℓ-divisible groups) for the formal torus (my D1);
     - it calls E_J^0 an "open subgroup" and relies on BL91, which is not local and not needed (my D2).
   - Coleman 2000 Thm 4.1 would give a direct published statement (my D3).
2. **Defect 2 — the identification chain.**
   - Sec 6 now uses BR (4.5.2) + Thm 2.9 + Rem 6.3 with Coleman cited (not local).
   - The coarse-versus-regular passage is in 11.R2.
   - I read Coleman Thm 2.1 (uniformization pairing = Grothendieck's pairing), which confirms Rem 6.3.
   - Two stale mentions of Thm 2.3 remain in non-load-bearing text: the I10 import list (lines 38–39) and the G2 gate text (line 168).
   - The identification of the Néron X_J with the Raynaud torus lattice M is still implicit (my D4).
3. **Defect 3 — the image of Φ(π).**
   - Secs 7 and 9 now use CS Prop 6.5 with L = Zv, giving image Z/(n_0/κ). I checked this against the CS text.
   - The stale phrase "Lemma 4.1's image formula" remains in the sec 10 gate list (line 171), outside the proof (my D13).
4. **Defect 4 — the fine model (partially resolved).**
   - KM 13.4.7 is gone.
   - Referee 1's suggested route is implemented: Č16 §3.1 (the Γ_0(n) stack is regular), §3.8 (transversal crossing), and étaleness of P_l ↦ ⟨P_l⟩.
   - **Not yet resolved:**
     - The "regular-node lemma" that referee 1 listed as needed is not supplied. Line 204 only asserts "which pulls back: … W[[x,y]]/(xy − 2)". GRAPH_LEMMA Lemma 3.1 would do it, but it is not cited (my D8).
     - Representability is still cited to Č16 (3.1.1), which is stated for Γ_1(n) with n/2 ≥ 5 and not for Γ_0(2)×Γ_0(3)×Γ_1(l). This is the same kind of scope mismatch referee 1 flagged.
     - Regularity of the Γ_0(n) stack is attributed to "[Ces17 sec 4.4]"; in Čes17 it is Theorem 5.13(a) (my D6).
     - Y is not restricted to the elliptic-curve locus (my D7).
   - The mathematics is correct (my G1).
5. **Defect 5 — the cusp 0̄.**
   - Derived as referee 1 suggested: w_2 swaps the components, w_M preserves them, and ∞̄ ∈ X^μ, so 0̄ = w_N(∞̄) ∈ X^ét.
   - Two sources confirm the conclusion directly: Edixhoven arXiv:math/0312019v1 p. 7 ("C_∞ containing the cusp ∞, and hence C_0 the cusp 0") and p. 9 ("W_d interchanges C_∞ and C_0 iff p divides d"). Both were read by me.
   - The pointer "L315" used for ∞̄ ∈ X^μ is imprecise (my D9).
6. **Defect 6 — the Γ_0(N) q-expansion statement.**
   - It is now cited at its sources, [Edi06] and CNS §1, both marked not local.
   - I read Edixhoven §2.1 ("The Tate curve G_m/q^Z over Z((q)) gives an isomorphism from the formal spectrum of Z[[q]] to the completion of X along ∞"), which covers X_0(N).
   - I also obtained the CNS sentence "the formal completion of X₀(N) along ∞ is Spf(ℤ⟦q⟧)" through a summarizing fetch tool, so it is not a verbatim guarantee.
   - The pointer "(M Lemma M8)" is imprecise: in M_DRAFT the CNS citation appears in §4 (my D9).
7. **Defect 7 — w_M and ε_p.**
   - The moduli argument for w_M is correct on the elliptic-curve locus, which is all that is needed.
   - Atkin–Lehner/Li are cited but not local, and I could not access them (my D12).
8. **Defect 8 — the quotient.**
   - The requested outline is given: Y → X finite and G-invariant; Y/G → X finite and birational onto a normal target; completion = stabilizer invariants.
   - GRAPH_LEMMA Lemma 3.2 is cited as the N = 2p analogue.
   - Residual: the statement is global, but the argument covers only the elliptic-curve locus (my D7).
9. **Defect 9 — the chart.**
   - Branch preservation (odd order), averaging, the normalization ζ′ = ζ^{-1}, effectiveness, the invariants and the A_{e−1} resolution are all written out.
   - GRAPH_LEMMA (sha pinned) Lemmas 3.4–3.6 are cited. Lemma 3.5 applies verbatim.
10. **Defect 10 — the analytic setting.**
    - 11.R5 states the base change to C_2, the punctured curve X \ {0, ∞}, V = {ζ_∞, ζ_0}, and the ray attachments.
    - Residual: unchanged line 106 still says "on X minus the cusps" and line 107 says "rays to the cusps". Both choices are valid, but the text is inconsistent (my D11).
    - "annular residues are compatible with this base change (BR sec 5.1)": BR §5.1 covers skeleta and retractions; residue compatibility is elementary.
11. **Defect 11 — I2 for both signs.**
    - 11.R8 derives n_V for both signs from the master-map minimal models via c_4 odd.
    - It cites "referee_1 check C" as the minimality verification, which is a custody oddity.
    - The isomorphism of these models with the displayed isogenous curves is taken from the master map.
    - I verified all four models symbolically in r (isomorphic via u = 2, discriminants as stated, c_4 odd) and the 2-isogeny edges (my G7).
12. **Defect 12 — BH 2.13 on the negative branch.**
    - (i), (iv), (v), (vi) and (vii) are written in 11.R6. (ii) and (iii) come from Zhai 1.5 together with I12 (lines 159–160).
    - I checked a_3 = 0, a_5 = ±2 and the discriminants (my G7).
13. **Defect 13 — digest pins.**
    - I verified that `~/H41_KAPPA_PARITY_2026-09-14/{KAPPA_PARITY_PROOF,GRAPH_LEMMA}.md` have sha256 `825c91d2…99ba1` and `29091400…482082`.
    - The ADDENDUM_017 `R/` copies are byte-identical.
    - The archive `H41_KAPPA_PARITY_ADDENDUM_017.tar.gz` has sha256 `a0a62efb…9bca`.
    - The pins in the object are 16-hex-character prefixes, not full digests.

## Where I differ from or add to referee 1

I found no mathematical disagreement: like referee 1, I find 0 BLOCKING defects. The differences are additions and refinements.

1. **Coleman 2000 Thm 4.1** (Asian J. Math. 4, p. 320, read by me) directly states the integral residue–character identity that referee 1's defect 1 asks to have cited. Neither revision 0, revision 1 nor referee 1 mentions it. This makes G2 rest on a published statement, not only on Lemma R.
2. **Sources referee 1 listed as unverifiable.** Three items in referee 1's (d) are now verified from primary texts that I read:
   - (d)2, the cusp 0 reducing to the étale component: Edixhoven p. 7.
   - (d)3, the Tate-curve completion for Γ_0(N): Edixhoven §2.1, plus the CNS sentence.
   - (d)8, Aut(E_ss) ≅ SL_2(F_3): Mazur 1977 corpus text, lines 1554–1566, which referee 1 did not open.
   - Referee 1 did not access Coleman (their (d)5); I read Thm 2.1 and Thm 4.1.
3. **Defect 4.** Referee 1 treated it as needing a regular-node lemma. I agree, and I mark it **partially** resolved because that lemma is still missing and the representability citation still points to a Γ_1(n) statement.
4. **Wording in referee 1's G3.** Referee 1 accepts "Res_x = constant term" by reading it through the normal form. The text of line 111 itself is ill-defined without the normal form (my D5). This is non-blocking, and referee 1's reading is the right one.
5. **Issues not raised by referee 1.** Some are introduced by revision 1, some were present already; all are non-blocking or citation-level:
   - D1: the CS Cor 8.5 mis-citation inside Lemma R.
   - D2: "open subgroup"; BL91 not needed.
   - D6: the Čes17 §4.4 and (3.1.1) scope mismatches in the new I11/11.R3.
   - D8: the missing regular-node lemma.
   - D9: imprecise pointers in 11.R4.
   - D10: I3–I5 pinned to an audit that is unsealed by its own statement, without digests.
   - D11: the sec 5 versus 11.R5 punctured-curve inconsistency.
   - D13: stale gate text at lines 168 and 171.
   - D14: no pointer for the ℓ ≥ 11 isogeny exclusion behind I1.
6. **A refinement of referee 1's G3 "consistency observation".** Since w_N swaps the components and F∘w_N = C/F, we get B = v_2(C) − A. Combined with A = 0 (the q-expansion of F at ∞ has unit content), this gives B − A = v_2(C) = 3(l−1). This is a second derivation of the potential drop, independent of the slope formula. It agrees with sec 5 and with KAPPA Theorem A.
