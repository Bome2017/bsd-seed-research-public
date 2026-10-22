# Class-lift coupling, continued from Codex's interrupted run: six more class-carrying controls, none unrepairable

2026-10-14. Claude (Opus 5.5), continuing Codex's `BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13` in a copy, at the user's
request while Codex is unavailable. **Codex's original folder is untouched**; this folder began byte-identical to it
(`ORIGINAL_MANIFEST_AT_COPY.sha256`, 257 files verified). Grade: exact number-field arithmetic with certified class groups
(`bnfcertify` = 1), Codex's unchanged templates, independent matrix and Hensel re-checks; same-session, not human review.
**Endpoint effect: none. FIN, ORDER9 and Q36 are unchanged.** Everything here is at coefficient 3 on control curves.

## 1. Where Codex stopped, verified

Codex had finished more than its `STATE.json` (still "running", 18:24) said. Its draft `arithmetic/REPORT.md` (18:28) and its
reviews show the first 24 candidates scanned and all three class-carrying curves (718b1, 997c1, 1070a1) fully analyzed, each with
the class direction repaired by units into rational points. Every Codex check was replayed in this copy and reproduced
byte-for-byte: the three exact-identity reviews, the local-leaf replay, the 718b1 ray-pushout check, the saved-matrix review, the
rational Hensel review and the independent coupling elimination (`continuation/replay/`).

The open item in Codex's `RESUME.md` was the continued search for "an unrepairable class": a class direction that no global-unit
correction makes admissible, i.e. a positive class-defect rank at some admission block.

## 2. What was run

- **Extended scan, cap reassessed from results** (3 class-carrying fields in the first 24): the next 24 rows of the same Cremona
  list, same filters, with Codex's GP field-scan script extracted verbatim from `search/scan.py` and its limits unchanged
  (`search/scan_ext.py`, `SCAN_STATE_EXT.json`). Outcome: 3 certified class-carrying fields (1141a1, 1480a1, 1525c1),
  19 provisional class-3-zero screens, 2 timeouts that had already printed class group C3 (1246c1, 1613a1).
  1613a1's certification also timed out at 600 s inside the scan. It was analyzed from its saved class group, and a separate
  `bnfcertify` of that exact saved file then returned 1 after 1,296 s (`search/1613a1_grh/certify_saved.*`), so its row is certified.
- **Retries** of those two timeouts with the alarm raised from 90 s to 600 s, in separate folders `search/*_retry600/` (the
  original timeout records are kept). 1246c1 certified in 134 s.
- **Per-curve pipeline** (`continuation/run_curve.sh`): Codex's `analyze_template.gp`, `checks/coupling.py`,
  `local_certify_template.gp`, the 1070a1 `witnesses.gp` and identity review with the label substituted, the saved-matrix review,
  a label-generic copy of the Hensel review, and an exact transvection check (a prime q with v_q(Δ) = 1, q ∤ c₄).
- **One script limitation fixed, not hidden:** 1525c1's Cremona row lists its rational 2-torsion point as a third point; its mod-3
  Kummer column is zero, which made the witness script's two-point solve fail. `witnesses_2gens.gp` drops only zero point columns
  and completes; the failed run is kept.

## 3. Results

See `ALL_RELEVANT_CURVES.md` / `.json` for the full table.

| curve | by | class group | admitted unit, class (joint) | class defect rank (joint) | class direction repaired into | anti-unit rejected at split prime | full image via q |
|---|---|---|---|---|---|---|---|
| 718b1 | Codex | C3 | 1, 1 | 0 | P1 + 2P2 | 829 | 359 |
| 997c1 | Codex | C3 | 1, 1 | 0 | 2P1 + P2 | 223 | 997 |
| 1070a1 | Codex | C3 | 1, 1 | 0 | 2P1 + P2 | 433 | 107 |
| 1141a1 | Claude | C3 | 1, 1 | 0 | 2P1 + P2 | 73 | 163 |
| 1246c1 | Claude | C3 | 1, 1 | 0 | P1 | 1609 | 89 |
| 1480a1 | Claude | C3 | 1, 1 | 0 | P1 + P2 | 13 | 37 |
| 1525c1 | Claude | C12 | 1, 1 | 0 | 2P1 + P2 | 229 | 61 |
| 1613a1 | Claude | C3 (certified separately, 1,296 s) | 1, 1 | 0 | 2P2 | 1171 | 1613 |

In every row: certified class group, full joint kernel of dimension 2 equal to the span of the two rational-point Kummer classes
(so the pair is 3-saturated and Sel₃ has dimension 2 under the retained Schaefer–Stoll source theorem), exact tau and point cube
identities, local rows reproduced at higher precision, and positive rational Hensel margins.

## 4. What the pattern is

The same mechanism appears in all nine curves, all with certified class groups. The scalar condition leaves two anti-invariant unit directions; one is
rejected by the global additivity (affine-line norm) test, with an explicit split residue prime where the cubic-residue product
along a torsion triple is not a cube; local conditions agree. So the admitted unit space is one-dimensional. Both rational points
have valuation zero, and the valuation-zero joint kernel equals the two-dimensional point plane. The admitted class direction is
therefore forced to be occupied by a rational point after a unit correction: "class survives and is a point" in Codex's branch list.

An unrepairable class would need both point directions to be unit-supported while a class source is present. In every control
found so far, the affine norm rejects one anti-unit exactly when the class source is present, matching Codex's observation of
Smith factors (1,3) here versus (3,3) for the class-free controls and the seed's positive span. The record's written norm-index
deduction relates that index to a ratio of class numbers of the point field and the dual field. A plausible but **unproved**
reading: the branch Codex was searching for needs the dual field to carry extra 3-class as well. Testing that needs the dual
field's class group, which no run here computed.

## 5. Scope and limits

- 48 candidates scanned in all: 9 class-carrying fields with certified class groups (3 Codex, 6 continuation). The provisional class-3-zero screens are GRH-conditional and are not
  used for any upper bound. The candidate list is Cremona's, ordered by conductor; this is not a random sample.
- No unrepairable class was found. That is a scoped observation on these curves, not a theorem that none exists.
- Nothing here bounds Ш across coefficient primes or touches the seed's good primes. The seed's own p = 3 excess has the
  filtration (0,1,1) (`BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13`); these controls show what the class-supported direction looks
  like when Ш[3] = 0.
- Nothing was pushed. When Codex returns it can resume its own folder and compare against this copy file by file.
