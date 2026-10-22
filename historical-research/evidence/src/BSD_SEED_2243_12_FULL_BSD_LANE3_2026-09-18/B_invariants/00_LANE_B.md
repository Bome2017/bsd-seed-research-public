# Lane 3 / B — Arithmetic invariants of the seed E (2243, 12): report

E: y² = x³ − 22735x² + 106272484x (= x³ − 5Ax² + 4ABx; m = 2243, A = 4547, B = 5843), with T = (0,0), P₁ = (4547, 327384) and
P₂ = (5184, 281520). No analytic function (L-series, `analytic_rank`, `sha().an()`, `lfun`) was called on E or E′.

Everything here is author-computed. An independent referee audited it (`../audits/AUDIT_B.md`, verdict PASS_WITH_CORRECTIONS: one
BLOCKING correction and four non-blocking notes). All five are applied; see "Audit response" at the end. B.7 was produced by a second
lane-B instance, and I re-ran it myself (byte-identical output; RESUME §4b). CPU used for the lane: **≈ 7 CPU-min in total across both
instances before the audit, plus ≈ 3.0 CPU-min for the audit repair** (`cpu_log.tsv`, which includes a manual estimate of 65 s for one
killed job). The cap was 30 CPU-min. Maximum RSS was 0.3 GB, and there were never more than 2 heavy
processes.

## Headline

**E(Q) = ⟨T⟩ × ⟨P₁, P₂⟩ ≅ Z/2 × Z², with the index proved to be exactly 1.** Route (a), eclib saturation, was complete as delivered.
Route (b), the Silverman bound plus ratpoints enumeration plus Hermite, is complete after the enumeration-box fix of AUDIT_B
correction #1; that fix changed no enumerated point set. **Sha(E/Q)[2^∞] = 0 (PROVED).
∏c_p = 16. The certified values are Ω_E = 0.0560898030388728088966188036158607683422700957, Reg(E) = 17.7965174724903402991749412194360384163049724638
and C = Ω·Reg·16/4 = 3.9928126392393669180685520022091539473553366203. So BSD predicts L″(E,1)/2 = C·#Sha(E).
For E′ = E/⟨T⟩, C′ = C exactly, and Sha(E) ≅ Sha(E′).**

This supersedes the brief's "saturation known only mod 5": E(Q) is now fully saturated at every prime.

## Labeled claims

| # | claim | label | file |
|---|---|---|---|
| 1a | E₀ is a global minimal model: u = 1, v_p(Δ) < 12 for all p. Reduced form [0, −1, 0, −66020924, −65074271436] via x = x_r + 7578 | PROVED | 01 |
| 1b | Néron differential ω = dx/(2y). Δ = 2⁸·3²·2243·4547³·5843² > 0, so 2 real components. N = 2³·3·2243·4547²·5843 | PROVED | 01 |
| 2 | E(Q)_tors = Z/2 = ⟨T⟩. Evidence: elltors, three Sage algorithms, #E(F₅) = 8, #E(F₇) = 10; E(Q)[2] = Z/2 since the discriminant 9mA is not a square | PROVED | 02 |
| 3 | c₂ = 2 (I₁*), c₃ = 2 (I₂, **non-split**), c₂₂₄₃ = 1 (I₁, **split**), c₄₅₄₇ = 2 (III), c₅₈₄₃ = 2 (I₂, **non-split**); ∏ = 16; w = +1. PARI `elllocalred` and Sage's generic Tate implementation agree, and the result matches the brief | PROVED | 03 |
| 4a | rank E(Q) = 2: 2-descent upper bound (mwrank and PARI `ellrank`); lower bound from Reg(P₁,P₂) ≠ 0 (certified) | PROVED | 04 |
| 4b | [E(Q) : ⟨T, P₁, P₂⟩] = 1, route (a): eclib saturation (index bound 2, 2-saturation proved, q ≤ 31); mwrank reports "full Mordell-Weil basis determined unconditionally", with basis {P₂, −P₁−P₂+T} | PROVED | 04 |
| 4c | Same, route (b), bound and search: Silverman 1990 Thm 1.1 bound B = 20.329 (maximum of the refined and crude published forms, constant 0.973); complete ratpoints enumeration over 16 quartic covers to naive height 22.829 (validated against brute force and against explicit combinations). The denominator range was truncated for 8 quartics as first delivered. It was corrected per AUDIT_B #1 to the full box e ≤ e^{H/2}, and the rerun gives the same point set (`out/s04b_box_audit.out`) | PROVED (after the AUDIT_B #1 fix) | 04 |
| 4d | Route (b) conclusion: λ ≥ 2.5, and Hermite γ₂ = 2/√3 gives index ≤ (2/√3)√Reg/λ = 1.948 < 2. PARI `ellsaturation(…, 100)` agrees | PROVED (after the AUDIT_B #1 fix) | 04 |
| 4e | λ = min ĥ(non-torsion) = ĥ(P₁+P₂) = 4.1284775508657867469994460134150421604. Attained with the refined constant (H = 20.679) and, after AUDIT_B #2, with B = 20.329 (H = 24.529, full box, `out/s04b_pari_lam42_crude.out`) | attained: PROVED; value: CERTIFIED_NUMERIC | 04, 06 |
| 5a | dim Sel^ψ(E) = dim Sel^ψ̂(E′) = 2, dim Sel₂(E) = 3, and 3 = rank 2 + dim E(Q)[2] 1 | PROVED (mwrank, Sage/Miller, PARI; calibrated on 7 Cremona curves with known Sha) | 05 |
| 5b | **Sha(E/Q)[2] = 0, hence Sha(E/Q)[2^∞] = 0**. Also Sha(E′/Q)[2^∞] = 0 | PROVED | 05 |
| 6a | Ω_E = 2ω₁ = 0.05608980303887280889661880361586076834227009573326993315960213 (radius < 10⁻¹⁰⁰⁰, Arb AGM enclosure) | CERTIFIED_NUMERIC | 06 |
| 6b | Reg(E) = 17.7965174724903402991749412194360384163049724637781885322663 (radius 4.4·10⁻⁶⁵; Tate series with a rigorous tail) | CERTIFIED_NUMERIC | 06 |
| 6c | Normalisations calibrated. For 389a1, 1088j1 and 1088j2 (the latter two have Δ > 0, rank 2 and rational 2-torsion), Ω and Reg reproduce Cremona curvedata to all 29 printed digits | CERTIFIED_NUMERIC | 06 |
| 7a | C = Ω·Reg·∏c_p/#tors² = 3.99281263923936691806855200220915394735533662030720 (radius 1·10⁻⁶⁵). PARI `ellbsd`·Reg agrees | CERTIFIED_NUMERIC | 07 |
| 7b | L″(E,1)/2 = C·#Sha(E/Q) | CONDITIONAL(BSD for E); not computed here | 07 |
| 7c | E′ = [0, 45470, 0, 91790289, 0], globally minimal, ψ*ω′ = ω. c′ = (2, 2, 2, 2, 1) at (2, 3, 2243, 4547, 5843) with types III*, I₄ non-split, I₂ split, III, I₁ non-split; ∏ = 16. E′(Q)_tors = Z/2 | PROVED | 07 |
| 7d | E′(Q) = ⟨T′⟩ × ⟨R′ = (−2243, −107664), ψP₁⟩. Proof: Kummer map, plus #Sel^ψ = 4, plus 4b/4c. The eclib cross-check gives saturation index 1 | PROVED | 07 |
| 7e | Ω′ = Ω, Reg′ = Reg = 17.79651747249034029917… (balls), C′ = C | CERTIFIED_NUMERIC | 07 |
| 7f | C′/C = 1: exactly Ω′/Ω, which lies in {1/2, 1}, and the certified ball selects 1 | PROVED (ball: 1 ± 5·10⁻⁶⁶) | 07 |
| 7g | Sha(E) ≅ Sha(E′) as groups: ψ is an isomorphism on ℓ-primary parts for odd ℓ, and both 2-parts are 0. So Cassels' check passes | PROVED | 07 |

## What this lane does NOT establish
- #Sha(E/Q), its finiteness, and its ℓ-primary parts for odd ℓ other than 5 (the 5-part is in the brief, via the v₂(c₀) ≤ 8 lemma). **UNKNOWN here.**
- The analytic side: L″(E,1) and analytic rank 2 are lane A's work. Nothing analytic was computed here.
- The Manin constant: not touched (brief).

## Open items / caveats
1. The Silverman 1990 paper is not available locally, and the referee could not retrieve it either. Route (b) needs only the
   LOWER-side refined constant (h − ĥ ≤ 2(h(j)/24 + μ + 0.973) = 16.479 on E_r). That form is corroborated by two independent
   implementations: Sage `silverman_height_bound` (source read by the referee) and eclib `htconst.cc`, which Sage cites for the
   0.961 constant. The crude form's transcription, from the paper's abstract, is NOT confirmed from the primary source. It is not
   load-bearing, because route 4c uses B = the maximum of all four one-sided constants. Route 4b (eclib) does not depend on any of this.
2. **Dead artefact (AUDIT_B note #3).** `out/s07b_Eprime_enum.out` comes from the killed first launch of the E′
   Silverman-plus-enumeration route. It contains a FAILED self-validation line ("enumerator 2 points, brute force 2 points, equal: 0").
   **It is cited by no claim and supports nothing.** 7d is proved via the Kummer map. That output was written by an earlier version of
   `scripts/s07b_Eprime_enum.gp`: the output is dated 11:06 and the script was edited at 11:08; the output prints "H=Hv", which the
   current file cannot print. The earlier version was not preserved, so the cause of "equal: 0" cannot be determined. Diagnostic
   (`scripts/s07b_validation_diag.gp`, `out/s07b_validation_diag.out`, 16.7 CPU-s): the current enumeration logic at H = 10.5 on E′
   agrees exactly with brute force, with both the truncated box and the full box (7 points up to sign). The dead script now has a DEAD
   header and the corrected box. It has not been rerun.
3. The optional last block of `s07c_scaling.sage` (which real component ψ(E(R)) lands on) failed on a symbol error. It is not used.
4. One independent audit has been done (AUDIT_B, PASS_WITH_CORRECTIONS). The referee independently recomputed Δ, torsion, c₂ by 2-adic
   point counting, Ω by AGM and by quadrature, the heights by a separate Tate-series code and by the doubling limit, Reg, C, and the
   isogeny facts. Every PROVED item still depends on the correctness of eclib, PARI 2.17.3, Sage/Miller descent and Arb ball arithmetic,
   which were cross-checked against each other and against Cremona's database.

## Files
- Item files: `01_minimal_model.md` … `07_bsd_constant_isogenous.md`.
- Scripts: `scripts/`. Outputs: `out/`.
- CPU ledger: `cpu_log.tsv`.
- Restart state: `RESUME.md` and `STATE.json`, with sha256 of every artifact.

## Audit response (to `../audits/AUDIT_B.md`, verdict PASS_WITH_CORRECTIONS; repair done 2026-09-18 ≈ 23:10–23:18Z)

All five corrections are accepted and applied. None is rejected, so there is no `REBUTTAL.md`. Repair CPU: 178.9 CPU-s, all
under `nice -n 15` and `timeout` via `run.sh`, one gp process at a time, RSS ≤ 12 MB. No production streaming job was run.

| # | referee's correction | severity | what was done | result |
|---|---|---|---|---|
| 1 | `scripts/s04b_enum_lib.gp` passed `[Mmax, min(emax,Mmax)]` to `hyperellratpoints`, which truncated the denominator range for the 8 quartics with \|s\| > 7579 (s = ±2A, ±2B, ±AB, ±2AB). So the completeness of route (b) was not established by the lane's artefacts. | **BLOCKING** (labels of 4c/4d) | The pre-audit library and the 6 affected outputs were preserved in `scripts/superseded_truncbox/` and `out/superseded_truncbox/`. The library now passes `[Mmax, emax]` (commented in place). New `scripts/s04b_box_audit.gp` compares both boxes on the 8 quartics at every search height used (11, 18.979, 20.679, 22.829, 24.529). All s04b scripts were rerun (validate, pari, simpleform, lam42, crosscheck, combo_heights). The proof text in 04 now states the box, the lowest-terms argument for X = M/e, the PARI `[N,D]` semantics, and the correction. | Only s = +AB gains points: X = ±48/4115 = ±(2P₁+2P₂+T), h_r = 24.9296, and X = ±96/6275 = ±(2P₁+T), h_r = 24.7036 (at H = 11 also ±1/12, ±1/36, h_r = 17.05, 16.63). Every extra point has h_r > H and is filtered. Compared with the pre-audit outputs, only the raw quartic-point counts (+8) and timings change. Validate still agrees with brute force, and crosscheck and combo_heights are byte-identical. λ ≥ 2.5, n ≤ 1.948 and index 1 are unchanged. The 4c/4d PROVED labels are restored "after the AUDIT_B #1 fix". This matches the referee's scratchpad result. |
| 2 | 4e ("λ attained") used only the refined constant (H = 20.679) and the truncated box. | non-blocking | Rerun with B = 20.329, the maximum of all four constants (H = 24.529), with the corrected box: new `scripts/s04b_pari_lam42_crude.gp`, `out/s04b_pari_lam42_crude.out`, 106.2 CPU-s. | 12 points up to sign incl. T; the one new point is the combination with h_r = 23.757, ĥ = 21.0025. The only non-torsion points with ĥ < 4.2 are ±(P₁+P₂), ±(P₁+P₂+T). λ = 4.128477550865786746999446013415042160376 is attained, and n ≤ 1.179905. Crosscheck at this H: 12/12, 0 missing, 0 extra. 4e no longer depends on the choice of constant. |
| 3 | `out/s07b_Eprime_enum.out` (killed job) contains a failed self-validation line ("equal: 0") and should be marked dead. | non-blocking | Marked DEAD in caveat 2 and in a header of `scripts/s07b_Eprime_enum.gp`. The same box truncation in that script was fixed for hygiene; it has not been rerun. Diagnostic `scripts/s07b_validation_diag.gp` (16.7 CPU-s). | The output was produced by an earlier, unpreserved version of the script (output 11:06, script edit 11:08; the output prints "H=Hv", which the current file cannot print), so the cause of "equal: 0" cannot be determined. The current enumeration logic at H = 10.5 on E′ agrees exactly with brute force under both boxes (7 points up to sign). No claim cites this route. |
| 4 | State that route (b) needs only the lower-side refined constant, and that the crude form is unconfirmed from a primary source. | non-blocking | Added a "Which side is needed" paragraph to 04 §4.2 and rewrote caveat 1 above. | Only h − ĥ ≤ 2(h(j)/24 + μ + 0.973) = 16.479 is needed. It is corroborated by Sage and eclib. The crude form is unconfirmed and not load-bearing, because B = 20.329 is the maximum. |
| 5 | Reword the headline "two independent routes". | non-blocking | Headline and the 04 result paragraph reworded. | Route (a), eclib, was complete as delivered. Route (b) is complete after the #1 box fix. |

Unchanged by the repair: every certified number (Ω, Reg, C, Ω′, Reg′), every other label, and every other item file (01–03, 05–07).
Status of the independent verification: the referee independently recomputed the items listed at the end of AUDIT_B. Corrections
#1 and #2 are author re-checks of the referee's own finding and agree with the referee's scratchpad values. They are not a second
audit.

New or changed files (sha256): `scripts/s04b_enum_lib.gp` ad53c658…; `scripts/superseded_truncbox/s04b_enum_lib.gp` 8fd49a9e… (the
pre-audit file); `scripts/s04b_box_audit.gp` d141cfa9…, `out/s04b_box_audit.out` 0e203dfc…;
`scripts/s04b_pari_lam42_crude.gp` b1a6bb8c…, `out/s04b_pari_lam42_crude.out` 63530065…; `scripts/s07b_validation_diag.gp` c536bcb6…,
`out/s07b_validation_diag.out` 1ca932b6…; the regenerated `out/s04b_{enum_validate,pari,pari_simpleform,pari_lam42,enum_crosscheck,combo_heights}.out`.
Full hashes are in `RESUME.md` §5 and `STATE.json`.
