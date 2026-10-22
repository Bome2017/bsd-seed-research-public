# Referee 1 delta check: PROOF.md rev 2 → rev 3 (no repair)

Rev 2: `history/revision_2/PROOF.md`, sha256 `c5d806defa3bc55da33cadb2cfad57c1d2e7e09c883c82dd371f814e1c0ab791` (the text of my `DELTA_REV2.md`).
Rev 3: `PROOF.md`, sha256 `71024db1ca0893acf7cd20bd271fc80be5a6faf209feb15635b3a8d24201f2e3`.

Custody:
- `history/DIFF_rev2_to_rev3.diff` is identical to `diff -u rev2 rev3`.
- `MANIFEST.sha256` verifies (all entries OK).
- The check script `checks/run_all_checks.py` (`782d706b…`) and its output (`c3b39aff…`) are hash-identical to rev 2. I replayed them in the rev 2 delta, so they were not rerun.

Not read: `referee_2/` and `src/author_recheck_2026-09-16/`. Line numbers `Lnn` are rev 3 lines. Nothing outside `referee_1/` was written by me.

## (a) Delta verdict

**ACCEPT WITH REMARKS. BLOCKING defects: 0.**

- Every item from my rev 2 delta (N1–N9) and my two partial defects (1, 8) is resolved.
- The new Néron derivation and the restored R3 arguments check.
- The only new finding is one cosmetic locator slip (R3-1).
- The standing remark is unchanged: the load-bearing Néron-completion input and BR Rem 6.3 rest on non-local published sources (Coleman 2000; Bosch–Lütkebohmert). These are declared in R9; I did not read them.

## (b) Status of referee_1 items

| Item | Status | Rev 3 lines | Check |
|---|---|---|---|
| N1 Néron identification mis-cited to BR §4.1 | RESOLVED | L130–131, L200–201, L205, L206–210, L219–220 | BR §4.1 is now cited only for "T and T_k share the character lattice". The Néron identification is derived (see (c)) and its external input is attributed to Coleman 2000 p. 322 / Bosch–Lütkebohmert. The overstated "BL dependency removed" is corrected at L200–201, and R9 L295 lists BL1991 as an alternative source. |
| N2 locator §2.6 | RESOLVED | L234 | "(L372-375)" matches stevens_v2.pdf.txt L372–375. |
| N3 "W_d swaps iff 2∣d" page | RESOLVED | L38–39 | Verified in Edixhoven arXiv:math/0312019v1, read by me from the arXiv PDF. p. 9: "W_d interchanges C_∞ and C_0 if and only if p divides d". p. 7: "C_∞ containing the cusp ∞, and hence C_0 the cusp 0". p. 4: "The Tate curve G_m/q^Z over Z((q)) gives an isomorphism from the formal spectrum of Z[[q]] to the completion of X along ∞". |
| N4 Rem 6.3 over Frac R, then transport to C_2 | RESOLVED | L127–128, L230 | BR L460 ((4.1.4) compatible with extension of the ground field) and L491 ((4.2.1), (4.2.2) compatible) verified. They carry trop(M′), hence the analytic pairing, and the (4.5.2) coordinates (BR §5.1 L652–657). |
| N5 Ω(cusps) completed stalk vs the S_2 statement | RESOLVED | L272–273 | The operative fact is now stated: Ω(cusps)^ = R[[q]]dq/q. Supported by Edixhoven p. 4 (Tate-curve completion; expansions as Σ a_n q^n dq/q) and p. 6 (completion argument), both verified. |
| N6 explicit c_4 | RESOLVED | L291–292 | Values E: r²−4r+1; B: 16r²−4r+1; F: 16r²+56r+1; G: 256r²−64r+1. Rederived by hand from c_4 = b_2² − 24b_4 and verified symbolically (`delta_rev3_checks.py`). All odd, and the models are integral, for r = ±2^m, m odd in 3..39. |
| N7 effectiveness of σ | RESOLVED | L256–257 | G is faithful on the connected generic fibre. Y_R is regular and connected (flat, every component meets the generic fibre), hence integral. An automorphism trivial on Ô_{Y,y} is trivial on O_{Y,y}, hence on the function field, hence on Y_R. |
| N8 covering vs local isomorphism | RESOLVED | L214 | "topological covering (BR L425-428: the universal cover)". BR L425–426 verified. |
| N9 local-algebra lemma compression | RESOLVED | L239–240 | k = R/2, and the surjection of 2-dimensional domains R[[x,y]]/(xy−2) → A is an isomorphism; pointer to the pinned GRAPH_LEMMA Lemma 3.1. |
| Defect 1 (Raynaud functoriality) | RESOLVED | L200–227 | Its only residue (N1) is resolved. Lemma R is now proved from BR plus one declared, standard formal-geometry input. |
| Defect 8 (X_R = Y_R/G) | RESOLVED | L246–249 | "on the elliptic locus Y → X is finite and G-invariant, and Y/G → X is finite and birational onto the normal X, hence an isomorphism". Correct: both are finite over A¹_j, generic fibres satisfy Y_Q/G ≅ X_Q (Galois group G), and X is normal (Česnavičius §2.6). Then Zariski's main theorem applies, and the completed-stalk formula follows by the decomposition-group argument. |

## (c) New derivation and restored arguments

1. **NERON IDENTIFICATION (L206–210): PASS WITH REMARKS.**
   - Argument: over the discretely valued Frac R, the Raynaud generic fibre of the formal completion of the Néron identity component 𝒜⁰ is a compact formal analytic subgroup of A^an, with special fibre the semi-abelian 𝒜⁰_k (split over F̄_2). BR §4.1's uniqueness clause holds for any complete K (BR L419) and is quoted at src L422–424. So this generic fibre equals A_0, and the equality transfers to C_2 by BR L460. Hence the torus of A_0 has the Néron special-fibre character lattice. The argument is correct.
   - Remark (a): the input "generic fibre of the completed 𝒜⁰ is a compact formal analytic subgroup with special fibre 𝒜⁰_k" is standard, but it is imported (Coleman 2000 p. 322 / Bosch–Lütkebohmert) and not local.
   - Remark (b): the locator slip, see R3-1.
   - Consequence: Lemma R step (2), u′ = π*ξ, now stands on BR plus this input. Steps (1) and (3) are unchanged from rev 2, and I passed them there.
2. **R3 local quotient Y/G (L246–249): PASS.** As in (b), defect 8.
3. **R3 effectiveness of the stabilizer (L256–257): PASS.** As in (b), N7. The integrality of Y_R is implicit but immediate.
4. **R3 h_3 orbit count (L261–263): PASS.**
   - Each of the four order-3 subgroups of A_4 fixes exactly one line of E[3], and 2 or 0 lines of E[l] according as l ≡ 1 or 2 mod 3.
   - A pair is fixed by at most one such subgroup, because Stab(C_3) is cyclic of order 3 (L252).
   - Orbits of such pairs have size 4, so h_3 = 8/4 = 2 or 0, and h_1 = (4(l+1) − 4h_3)/12 = (l∓1)/3.
   - Hence Σ1/e_x = (l+1)/3.
   - Regression (rev 2 delta): l = 11, 19, 43, 67, 131.
5. **R3 local-algebra lemma completion (L239–240): PASS.**
6. **R3 locator (L234): PASS.**
7. **Other rev 3 edits, all PASS:**
   - I10 L46–47: Thm 2.3 is declared unused. This matches sec 6 and G2 at L185.
   - R11 L302–303: 1703.02951v3 L62–63 contains "In particular, Conjecture 1.1 holds in the case when E is semistable".
   - R9 and R13 custody text (L293–297, L313–319): R13's summary of my rev 2 delta is accurate.

## (d) Sec 0

Sec 0 is **unchanged**. It is byte-identical in rev 3, rev 2 and rev 0. Sections 2, 3, 4, 5, 7, 8 and 9 are also byte-identical between rev 2 and rev 3 (section-wise sha256).

## (e) New defects

- **R3-1 — NON-BLOCKING (cosmetic).** L208 cites "BR's uniqueness clause (L421-423)". In `src/baker_rabinoff_1308.3864.txt` the clause is at L422–424; L421 closes the §4 preamble. The content is unaffected.

No other new defect.

## (f) Consolidated gate verdicts for rev 3

- **G1: PASS.**
  - Primary fine-chart route verified in local text: Česnavičius (2.6.1), §2.6 L372–375, §3.8 L684–687, and GRAPH_LEMMA Lemma 3.1.
  - The free (Z/3)^× quotient and the local Y/G quotient are argued; the stabilizers are explicit and verified.
  - Effectiveness, the invariants UV = 2^{e_x}, Σ1/e_x = (l+1)/3 and Φ_J⊗Z_2 = Z/4 all check.
  - The cusp placement is verified from Edixhoven p. 7.
- **G2: PASS WITH REMARKS.** Lemma R is proved: (1) and (3) from BR, (2) via the Néron identification. The pairing chain (4.5.2) / Thm 2.9 / Rem 6.3 is transported correctly, there is no factor e_x, and u_x ≡ 2 mod 4 follows. Remark: two inputs at this crux are non-local and I did not read them. They are the Néron-completion input (Coleman 2000 p. 322 / Bosch–Lütkebohmert) and Coleman's proof behind BR Rem 6.3 (BR itself states the remark). Both are declared in R9. No open defect.
- **G3: PASS.**
- **G4: PASS.** Edixhoven p. 4 and p. 6 (the Ω(cusps) completed stalk at ∞) and p. 9 (W_d swap criterion) are verified. The Atkin–Lehner sign a_p = −ε_p remains a declared textbook import with local support from CS §7.3.
- **G5: PASS.** The inherited N1 is resolved.
- **G6: PASS.**
- **G7: PASS.**

## Commands run

- `uptime` checks (1-minute load 3.0–4.5).
- `shasum -a 256` of rev 3, rev 2, the check script and its output. `cmp` of the supplied diff against `diff -u` (identical). `shasum -a 256 -c MANIFEST.sha256` (all OK). Section-wise sha256 comparison of rev 2 and rev 3, and of sec 0 against rev 0.
- `sed -n` on the BR local text (L418–428, L458–461, L489–492) for the locators.
- Read tool on the arXiv PDF of math/0312019v1, cached by the earlier WebFetch (sha256 `b6ebb9ad…`): pages 4 and 9 (pages 1 and 5–8 were read in the rev 2 delta).
- `nice -n 19 python3 referee_1/delta_rev3_checks.py`: `DELTA_REV3_CHECKS_OK` (explicit c_4 values, parity, integrality), under 2 s. Output in `referee_1/delta_rev3_checks_output.txt`.
- Hashes of the files used: `referee_1/DELTA3_FILES_READ.sha256`.
