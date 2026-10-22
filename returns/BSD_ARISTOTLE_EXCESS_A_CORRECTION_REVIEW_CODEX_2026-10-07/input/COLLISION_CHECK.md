# COLLISION_CHECK

Searches were run with ripgrep over HISTORICAL_STOPS_AND_CORRECTIONS.md, reading_set/ and
current_overlay/. The table gives the hit counts for the listed patterns:

| pattern | files hit |
|---|---|
| p-adic regulator | 39 |
| p-adic height | 28 |
| Kato | 277 |
| Skinner | 30 |
| Bertolini.?Darmon | 35 |
| Jochnowitz | 10 |
| Schneider | 18 |
| Kolyvagin structure/conjecture, ν+1, W. Zhang | 40+ (first 40 listed in NOTES.md) |
| 2603.12357 / Da Ronche | 5 (references only; paper text absent) |

## Per-candidate matches

### A1/A2 (derived Heegner / Kolyvagin ν)
- `current_overlay/.../download_sources/4fbf3521eaa7/HEEGNER_NU.md`, with its Lean file
  `Coinvariant/KolyvaginOrder.lean`. Verdict there: NU_LE_TWO_RESTATES_SELMER, and on the
  minimal-twist set ν_p ≤ 2 ⇔ ν_p = 1 ⇔ Sha[p]=0.
- `current_overlay/.../download_sources/474218aa6a00/output-final_aristotle/research_return/RESULT.md`
  covers the cross-prime index ι(ℓ) built from derived Heegner points at supersingular inert ℓ.
  Its open inputs are (A) a mod-(ℓ+1) formula and (B) a Lang–Trotter supply.
  Its Proposition 4 shows archimedean heights fail.
- LOCAL_ATTEMPT.md, Candidate 1: Proposition 5.8 rank-dependence.

**What this run changes:** nothing. *(Corrected 2026-10-07.)* The first version claimed to link
the higher-Fitting augmentation ideal to the HEEGNER_NU criterion. That link is withdrawn
(CORRECTIONS_2026-10-07.md, C1–C4). A2 is a full collision with HEEGNER_NU.md and with the W3
return's HEEGNER_NU_NOTE.md §3. A1 has no recorded collision beyond LOCAL_ATTEMPT.md, and it was
not developed.

### −23 twist (searched in the second pass; missed in the first)
- `reading_set/.../_work/d23_twist_2026-09-21/` (RESULT.md, PROOF.md, DESIGN.md, RESULT.json, logs)
  holds the 2026-09-21 Arb certificate.
- `reading_set/.../BSD_TWIST_D23_CERTIFICATE_2026-09-21/` and
  `.../bridge_repair_assessment_2026-09-21/D23_COVERAGE_REVIEW.md` hold the endpoint and coverage
  rechecks.
- `current_overlay/.../BSD_ARISTOTLE_W3_P17_P19_RETURN_2026-10-06/HEEGNER_NU_NOTE.md` §3 and
  `w3_p17/TWIST23_RESULTS.json` hold the floating-point value.
- FULL_COMPENDIUM.md has headings at lines 331, 343, 520, 1039, 1075, 1099, 1172 and 16399.

See TWIST_D23_TRACE.md.

### A3 (Kato + p-adic leading term)
- HISTORICAL_STOPS_AND_CORRECTIONS.md, line ~30727 and ~33658: d-infinity / Lemma R / HGZ2.
  This route needs a rank-two Gross–Zagier formula with one rational constant.
- Same file, line ~44664 (A2 row): no general p-adic regulator nondegeneracy theorem.
  Seed regulators are certified only at p = 3, 5, 17. Line ~51408 corrects the wording.
- guide/03_WALL_ATLAS.md W24 (Kato index b_p, dim Sha[p] <= b_p − 2) and W05.

**What this run changes:** nothing beyond stating the inequality with all terms explicit.

## Not developed (seen in the record, no new input available to this run)
Bertolini–Darmon level raising and Jochnowitz congruences, visibility, the 1-motive and
determinant line, and the class-group receiver. Each needs a uniform mod-p nonvanishing of a
p-dependent special value, which is the same missing arrow.
