# Referee 2 — delta check of revision 3 against revision 2 (no repair)

## What was compared

- **Revision 3 (under check):** `PROOF.md`, 320 lines, sha256 `71024db1ca0893acf7cd20bd271fc80be5a6faf209feb15635b3a8d24201f2e3`.
- **Revision 2 (baseline):** `history/revision_2/PROOF.md`, sha256 `c5d806defa3bc55da33cadb2cfad57c1d2e7e09c883c82dd371f814e1c0ab791`. It is byte-identical to the file I reviewed in `referee_2/DELTA_REV2.md`.
- **Diff:** I computed my own diff (`referee_2/checks_delta_rev3/referee2_own_diff_rev2_to_rev3.txt`). I did not rely on the supplied `history/DIFF_rev2_to_rev3.diff` (sha256 `6c6ab5df…`, not used). My diff has 21 hunks, at revision 2 lines 1, 38–39, 46–47, 127, 129–130, 184, 199, 203, 207, 212–213, 223, 227, 232, 240, 247, 251, 260, 278, 280–281, 288–289, and an insertion after 298. I read all of them.
- **Check script:** unchanged. `checks/run_all_checks.py` still has sha256 `782d706b…8ab0`, and `checks/run_all_checks_output.txt` still has `c3b39aff…b9e0`. That output is identical to the one I reproduced for revision 2, so I did not re-run it.
- **Line numbers:** "line N" means a line of revision 3. "BR" means the local `src/baker_rabinoff_1308.3864.txt` (sha256 `c5f798a4…`).
- **Not opened:** `src/author_recheck_2026-09-16/`, and referee 1's delta files.
- **Scope of writing:** nothing outside `referee_2/` was written.

---

## (a) Delta verdict

**ACCEPT WITH REMARKS. BLOCKING defects: 0.**

What revision 3 adds is correct:
- the Néron identification paragraph;
- the restored Y/G quotient argument;
- the restored effectiveness argument for the stabilizer;
- the h_3 orbit count;
- the explicit c_4 values;
- the transport of the pairing comparison from Frac R to C_2;
- the completed Ω(cusps) stalk at ∞.

Of my rev 2 delta items N1–N7, six are resolved. N6 (custody) is only partially resolved. D12 has not changed. Three new items are minor: a locator off by one line, a page pointer, and a custody page range.

---

## (b) My N1–N7 and D12 in revision 3

| Item | Status | Rev 3 lines | Basis |
|---|---|---|---|
| N1 (Néron identification wrongly credited to BR §4.1) | **RESOLVED** | 130–131, 200–201, 206–210, 219–220 | BR §4.1 is now cited only for "T and T_k share the character lattice". The Néron identification is credited to Coleman 2000 p. 322, which I read, and is also derived from BR's uniqueness clause (see (c)1). |
| N2 (Y/G quotient and effectiveness arguments deleted) | **RESOLVED** | 248–249, 256–257 | Both arguments are restored; see (c)2. |
| N3 (locators) | **RESOLVED** | 234; 38–39 | "sec 2.6 (L372–375)" matches the local Č16 text (regularity sentence at lines 372–374, continuing to 375). The Edixhoven pages are now right: p. 7 cusp placement, p. 9 W_d, p. 4 Tate-curve completion. |
| N4 (Manin at every prime) | **RESOLVED** | 302–303 | "applying it at EVERY prime p (p² ∤ N holds for all p) or by quoting its own 'In particular' sentence". Correct. |
| N5 (h_3 orbit count) | **RESOLVED** | 261–263 | The orbit count is now given; verified in (c)2. |
| N6 (custody of referee-read sources) | **PARTIALLY RESOLVED** | 294–295; still 38, 131, 133, 210, 220, 273 | See note N6 below. |
| N7 (stale BR Thm 2.3) | **RESOLVED** | 46–47, 185 | See note N7 below. |
| D12 (Atkin–Lehner sign) | **PARTIALLY RESOLVED** (unchanged since rev 2) | 275–277 | See note D12 below. |

### Notes on the table

- **N6.**
  - Fixed: R9 now lists Edixhoven and Coleman as "READ BY REFEREE_2, not re-read by the author", and Bosch–Lütkebohmert as not local. The rev 2 inconsistency is gone.
  - Still open:
    - The body still cites referees' readings as support: "read by referee_2" at lines 38, 131, 133, 210, 220, and "read by referee_1" at line 273.
    - R9's page ranges are incomplete. They list Edixhoven pp. 4, 7, 9 and Coleman pp. 320–322. But the body also relies on Edixhoven p. 6 (line 273) and on Coleman Thm 2.1, p. 319, which is behind BR Rem 6.3 (lines 127–128 and 229–230). See E2.
- **N7.**
  - I10 now lists BR (4.5.2), Thm 2.9 and Rem 6.3, and says Thm 2.3 "is NOT used by the proof".
  - The G2 gate text now reads "BR (4.5.2) / Thm 2.9 / Rem 6.3 / Cor 5.6 / Prop 6.1".
  - It still says "the Raynaud functoriality for pi". As a description of what the referee must check (that is, Lemma R), that is acceptable.
- **D12.**
  - Nothing changed in revision 3. The sign ε_p = −a_p still rests on two things:
    - the local primary statement in Conrad–Stein §7.3, "Frob_p = −W_p", which I verified;
    - the Frobenius action on X_{E_0} (+1 for split, −1 for nonsplit) together with W_p acting on E_0 by ε_p, which is the argument in the proof of CS Prop 7.1.
  - The derivation is only sketched in R4. Atkin–Lehner 1970 and Li 1975 are still unread, and the object still marks this "UNVERIFIED primary import". This is non-blocking.

---

## (c) Checks of the new and changed passages

### 1. NERON IDENTIFICATION paragraph (11.R1, lines 206–210): PASS WITH REMARKS

**The argument, step by step.**
1. **Where BR §4.1 applies.** BR §4.1 holds over any complete non-Archimedean field (BR line 419), so it applies over Frac R = W(F̄_2)[1/2]. J_0(N) and E_0 have split semi-abelian reduction there, because the residue field is algebraically closed.
2. **The input.** Take the formal completion of the Néron identity component A⁰ along its special fibre. Its generic fibre is a compact formal K-analytic subgroup of A^an, with semi-abelian special fibre A⁰_k.
3. **Uniqueness.** BR recalls (lines 422–424) that "there is a unique compact analytic domain A_0 ⊂ A^an which is a formal K-analytic subgroup … whose special fiber A_0 is an extension of an abelian variety B by a split torus T". So that generic fibre **is** A_0.
4. **Field extension.** Its formation is compatible with extension of the ground field (BR line 460: "The formation of (4.1.4) is compatible with extension of the ground field").
5. **Conclusion.** A_0's torus has the character lattice of the Néron special-fibre torus.

The logic is correct.

**The non-local input.** The input in step 2 is correctly marked as not local. Coleman 2000 p. 322, which I read, states the identification itself: "π|G⁰ is an isomorphism of G⁰ with the connected component of the origin in the rigid space associated to the formal completion of 𝒩 along its reduction", where 𝒩 is the Néron model (p. 321). That page supports the input in step 2 and, directly, the conclusion. I did not read Bosch–Lütkebohmert 1991.

**Remarks.**
- The uniqueness locator "L421–423" is off by one: the clause is at BR lines 422–424 (E1).
- The paragraph's non-local dependency is declared in R9.

### 2. Restored arguments in 11.R3 (lines 239–240, 248–249, 256–257, 261–263): PASS

- **Local-algebra lemma wording (239–240).** "the induced surjection R[[x,y]]/(xy−2) → A of 2-dimensional domains is an isomorphism; full proof: GRAPH_LEMMA Lemma 3.1". Correct, and it completes the Cohen-presentation argument.
- **Y/G quotient (248–249).**
  - On the elliptic-curve locus, Y → X is finite: it is the composite of the finite map X_1(6l) → X_0(6l) with the ±1 quotient. It is also G-invariant.
  - Y/G is normal.
  - On generic fibres, G = (Z/l)^×/{±1} acts simply transitively on the fibres of Y_Q → X_Q, so Y/G → X is birational.
  - X is normal and Y is connected (its generic fibre is geometrically connected, since det Γ_1 = Ẑ^×). A finite birational morphism onto a normal integral scheme is an isomorphism.
  - This is the argument I accepted in revision 1, and GRAPH_LEMMA Lemma 3.2 transfers.
- **Effectiveness (256–257).**
  - An automorphism trivial on Ô_{Y,y} is trivial on O_{Y,y}, by the Krull intersection theorem.
  - It is then trivial on the function field, and so on the separated integral scheme Y.
  - This contradicts G acting faithfully on the generic fibre. Correct.
- **Counts (261–263).**
  - Each of the four order-3 subgroups of A_4 fixes one line of E[3] and 2 (l ≡ 1 mod 3) or 0 (l ≡ 2 mod 3) lines of E[l]. So it fixes 2 or 0 pairs.
  - A pair with stabilizer of order 3 is fixed by exactly one of them. Two distinct C_3's generate A_4, whose involutions fix no line of E[3]; this is consistent with lines 253–254.
  - Orbits of such pairs have size 12/3 = 4, so h_3 = 8/4 = 2.
  - Then h_1 = (l+1)/3 − h_3/3 = (l−1)/3 or (l+1)/3.
  - This matches the object's checks sec 3 (l = 11, 19, 43: 0, 2, 2 orbits of thickness 3) and my rev 1 enumeration (l = 43: 14 + 2; l = 19: 6 + 2).

### 3. c_4 formulas in 11.R8 (lines 291–292): PASS

With c_4 = b_2² − 24·b_4, and the minimal models [a_1, a_2, a_3, a_4, a_6] of the four vertices:

| Vertex | Model | b_2 | b_4 | c_4 |
|---|---|---|---|---|
| E | [1, −r/2, 0, r²/16, 0] | 1 − 2r | r²/8 | r² − 4r + 1 |
| B | [1, r, 0, r/4, 0] | 1 + 4r | r/2 | 16r² − 4r + 1 |
| F | [1, −2r, 0, r² − 3r/2, r(r−1)/4] | 1 − 8r | 2r² − 3r | 16r² + 56r + 1 |
| G | [1, 4r, 0, 2r, r/4] | 1 + 16r | 4r | 256r² − 64r + 1 |

- These are identical to my independent symbolic computation (`referee_2/checks/referee2_checks_output.txt`, section C).
- All four values are odd for even r.
- The models are integral for m ≥ 2, so certainly for m ≥ 3.
- Since v_2(c_4) = 0 < 4, each model is minimal at 2. Hence n_V = v_2(Δ_min) as stated.

### 4. Ω(cusps) completed-stalk citation (11.R4, lines 272–273): PASS WITH REMARKS

**The claim is correct.**
- The completion of X along ∞ is Spf Z[[q]]. This is on Edixhoven p. 4, "The Tate curve G_m/q^Z over Z((q)) gives an isomorphism from the formal spectrum of Z[[q]] to the completion of X along ∞", and in the CNS §1 sentence.
- So Ô_{X_R,∞̄} = R[[q]], and Ω is generated there by dq.
- ∞ is the only cusp through ∞̄, because cusps reduce to distinct smooth points.
- Hence Ω(cusps)^ at ∞̄ = R[[q]]·dq/q.
- The remark that δ has a simple pole at ∞, so the stalk (rather than the S_2 statement) is what is used, is right.

**Remark.**
- The pointer "Edixhoven … p. 6 completion argument with dq replaced by dq/q" is a derivation hint rather than a statement. Edixhoven p. 6 (which I read) shows that at smooth points Ô_{X,x} ≅ W(k)[[t]], and reads multiplicities along C from coefficients. The direct inputs are p. 4 and the definition of Ω(cusps) (E3).
- This page is cited as "read by referee_1"; see E2.

### 5. Other changed lines

| Lines | Change | Verdict | Basis |
|---|---|---|---|
| 1 | Header | — | Custody text only. |
| 38–39 | I8 page pointers | PASS | Checked against the Edixhoven pages I read. |
| 46–47 | I10 | PASS | |
| 127–128 and 229–230 | Frac R → C_2 transport of the pairing comparison | PASS | See transport note below. |
| 185 | G2 gate text | PASS | |
| 200–201 | R1 header | PASS | |
| 214 | R1(1): "BR L425–428: the universal cover" | PASS | BR lines 425–428 state that E^an is the topological universal cover, with a unique K-analytic group structure making the map a homomorphism. |
| 219–220 | R1(2): Coleman p. 322 | PASS | |
| 234 | R3 locator | PASS | |
| 294–295 | R9 | PASS WITH REMARKS | Page ranges incomplete (E2). |
| 302–303 | R11 | PASS | |
| 313–319 | R13 | PASS as to referee 2 | Its statements about my rev 2 delta are accurate. Its statements about referee 1's delta were not checked by me. |

**Transport note (lines 127–128 and 229–230).**
- BR Rem 6.3 compares the analytic and Grothendieck pairings when Λ = Z, which holds over Frac R.
- Coleman Thm 2.1 (p. 319, read) proves that comparison for K a finite extension of the completion of Q_p^ur; Frac R is exactly that completion.
- The Raynaud cross (4.1.4) is compatible with ground-field extension (BR line 460), and so are the trop sequences (4.2.1)–(4.2.2) (BR line 491). So M, M′ and the Λ-valued pairing are unchanged when passing to C_2.
- BR Thm 2.9 holds over any complete K.

---

## (d) Section 0

**Unchanged.** Revision 3 lines 8–16 are byte-identical to revision 2 lines 8–16 and to revision 1 lines 7–15, checked with `diff` of `sed -n` ranges.

---

## (e) New defects in revision 3

### BLOCKING

None.

### E1 [CITATION, trivial] — line 208

**What is wrong.** "BR's uniqueness clause (L421–423)". In the local BR text the clause is at lines 422–424. Line 421 closes the previous paragraph, and line 424 contains "whose special fiber A_0 is an extension of an abelian variety B by a split torus T".

**What would be needed.** Correct the locator.

### E2 [NON-BLOCKING, custody] — lines 294–295, against 127–128, 229, 273

**What is wrong.** R9 records the texts read only by referees as "Edixhoven … pp. 4, 7, 9" and "Coleman 2000 pp. 320–322". The body also relies on:
- Edixhoven p. 6 (line 273, cited as "read by referee_1");
- Coleman Thm 2.1 on p. 319, which is the result behind BR Rem 6.3 (lines 127–128, 229).

Referees' readings are also still used as support in the body (this is the part of N6 that remains open).

**What would be needed.** Complete the R9 page ranges, or add local copies with digests.

### E3 [CITATION, minor] — line 273

**What is wrong.** The completed stalk Ω(cusps)^ = R[[q]]·dq/q is not stated on Edixhoven p. 6. It follows from the Tate-curve completion (Edixhoven p. 4; CNS §1) and the definition of Ω(cusps). The claim is correct; see (c)4.

**What would be needed.** Point to p. 4 and to the definition of Ω(cusps).

---

## (f) Consolidated gate verdicts for revision 3

| Gate | Rev 1 VERDICT | Rev 2 delta | **Rev 3** | Reason |
|---|---|---|---|---|
| G1 positive graph | PASS WITH REMARKS | PASS WITH REMARKS | **PASS** | D6–D8, N2, N3 and N5 are all resolved. The Γ_1(6l) chart, the local-algebra lemma, the free (Z/3)^× quotient, the Y/G quotient, the explicit stabilizers, effectiveness, the eigenparameter invariants and the mass/orbit counts are all verified. |
| G2 residue = character coordinate | PASS WITH REMARKS | PASS WITH REMARKS | **PASS** | D1–D4 and N1 are resolved. Lemma R and the Néron identification are verified against BR (local) and Coleman pp. 319–322 (read by me). Only the trivial locator E1 remains. |
| G3 slope formula and residues | PASS WITH REMARKS | PASS | **PASS** | Unchanged since rev 2. |
| G4 two-component lemma | PASS WITH REMARKS | PASS WITH REMARKS | **PASS WITH REMARKS** | D12 still partial: the load-bearing Fricke sign ε_N = −1 rests on a primary citation I could not read, supported by Conrad–Stein §7.3. Also E3 (page pointer) and the custody remark E2 on the Edixhoven p. 6 pointer. |
| G5 Conrad–Stein | PASS | PASS | **PASS** | Unchanged. |
| G6 T1 | PASS | PASS | **PASS** | Unchanged. |
| G7 imports | PASS WITH REMARKS | PASS WITH REMARKS | **PASS** | D10, D14 and N4 are resolved; the c_4 values are explicit and verified. The open custody item for the W audit's row statements is declared, and I cross-checked I3–I5 against the sealed identity-component review (sha256 `544e1c9c…`) and by re-derivation. |

**Overall for revision 3:** PASS WITH REMARKS, 0 BLOCKING. The only gate still carrying a remark is G4, because of D12.

---

## Commands run for this delta

1. `uptime`: 1-minute load 3.18.
2. `shasum -a 256` of revision 3, revision 2, the supplied diff, the check script and its output, and BR.
3. `diff history/revision_2/PROOF.md PROOF.md`, saved as `referee_2/checks_delta_rev3/referee2_own_diff_rev2_to_rev3.txt` (sha256 `d96bfe9b…`).
4. `diff` of the sec 0 line ranges against revisions 2 and 1: identical.
5. `grep -n` and `sed -n` on BR to confirm lines 422–424, 425–428, 460, 491 and 695.

No compute job was run. The check script and its output are byte-identical to the revision 2 artifacts I had already reproduced.
