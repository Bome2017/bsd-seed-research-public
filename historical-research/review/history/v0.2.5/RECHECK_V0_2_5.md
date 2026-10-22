# v0.2.5 (local, unreleased): settled results banked

This revision preserves v0.2.4 (local commit `001a49f`). It adds results that are settled at their stated grades,
revises five claims, and states the provenance at p = 3 exactly. No statement, grade label or certificate of v0.2.4 is
changed except as listed.

1. **Primary components at 17 ≤ p ≤ 47 (claim S.17-47, Theorem `thm:singletons`).** `Sha[p^∞] = 0` for
   p = 17, 19, 23, 29, 31, 37, 41, 43, 47.
   - For one auxiliary prime ℓ ≡ 1 (mod p) with v_p(ℓ − 1) = 1, ℓ ∤ pN and p ∤ #E(F_ℓ), the singleton coefficient
     `C_2(p,ℓ) = Σ_{a=1}^{ℓ−1} C(ind_g(a) mod p, 2)·[a/ℓ]⁺` (g the least primitive root mod ℓ; symbols certified in (1/1024)Z)
     is nonzero mod p, with C_0 = 0 and C_1 ≡ 0:

     | p | 17 | 19 | 23 | 29 | 31 | 37 | 41 | 43 | 47 |
     |---|---|---|---|---|---|---|---|---|---|
     | ℓ | 103 | 191 | 47 | 233 | 311 | 149 | 83 | 173 | 283 |
     | C_2 mod p | 7 | 6 | 9 | 6 | 3 | 1 | 15 | 15 | 42 |

   - Ota's Theorem 6.4 (arXiv:1509.00682v1, the version read at source; no ordinarity hypothesis, so 23 and 29 are
     covered) gives `Sha[p] = 0`, with no finiteness assumed. Grade: computer-assisted, with a preprint-read import.
   - Reviews, per prime: 17, 19, 23, 29 by a same-family model audit (PASS_AT_RETAINED_GRADE; 1,140 intervals; not
     cross-family; radii at 17 and 23 about 99% of the half-spacing); 37 and 41 by Codex and ChatGPT Pro model checks;
     31, 43, 47 by a Codex audit (1,528 intervals). The large corpus files were not rehashed. No human review.
   - Consequence (S.FIN): given FIN, `#Sha = 9t²` with every prime factor of t at least 53, so `#Sha = 9` or
     `#Sha ≥ 25,281`. X.14 now states that the ladder was stopped at 13, resumed through 47 and stopped again, that a
     prime settled out of order does not move the threshold, and that depth three at 17 belonged to the cyclotomic
     criterion, not to the singleton route.
   - A residue observation, not a theorem: the normalized residues are consistent with a putative common integer
     congruent to 288 modulo 17·19·…·47 = 20,475,850,236,047; no such scalar is constructed.
2. **The prime 3.**
   - **S.3L (exact computation).** `Sha[3] ⊇ (Z/3)²`. Two explicit ternary cubics on the minimal model have E's
     invariants, are everywhere locally soluble, and together with κ(P₁), κ(P₂) have F₃-rank 4 in `Sel_3(E/Q)` (cubic
     residue symbols at 79 degree-one primes of the flex field). Imports: rank ≤ 2, `E(Q)_tors = Z/2`, Hensel,
     Hasse–Weil, the class maps. No GRH, Skinner, Skinner–Urban or Kato input.
   - **S.3F (published theorem applied to the certificate).** `Sha[3^∞]` is finite: Kato 2004 Thm 18.4 at p = 3 with
     α = a₃ = −1 (not a Tate curve), `a₂ ≠ 0` from the certified `a_{4,2} = 15480`, and rank 2.
   - **S.3's qualification, stated exactly.** For this curve the printed proof of Skinner's Theorem A passes through
     Skinner–Urban Thm 3.6.1, which uses SU Prop. 12.3.6 twice; its printed proof does not cover the inert prime 2243
     (removed factor `1 − 2243⁻²` with v₃ = 1). One use is repaired by a nonvanishing argument; the other needs SU
     Prop. 13.4.1(ii) for the seed data (MS-13.4.1(ii), lower-bound direction, unproved). The Kato direction at the
     congruent forms needs a canonical-versus-good period comparison at weight ≥ 8 (MS-B1), in none of the sources
     read. An SU-free upper bound `#Sha[3^∞] ≤ 9` is OPEN; candidate routes MS-B1, MS-R3 (Ochiai), MS-R24 (Kato 12.5(4)
     plus an integral Coleman map at nonsplit 3), or GRH plus one Cassels–Tate value (not computed). S.3's statement
     and grade label are unchanged; Remark `rem:su` is rewritten to match.
3. **Bad primes.** B.18: at 2243, 4547, 5843, `C_0 ≡ C_1 ≡ 0` and `C_2 ≢ 0 (mod p)` at a suitable auxiliary ℓ imply
   `Sha[p^∞] = 0` (Bullach–Honnor Thm 1.4(b), preprint; `θ_BH = θ_pipeline/2`); no coefficient evaluated. B.8 records
   it as a further sufficient criterion at 4547. X.16 keeps the old cost models and adds the BH model (about 24k, 32k,
   74k core-hours, partial; checkpoint storage at least 0.80, 1.34, 5.80 TB in the current evaluator; HOLD).
4. **Reductions.** B.16 (G2): for p ∉ {2, 3, 5, 2243, 4547, 5843} infinitely many auxiliaries with nondegenerate tame
   regulator (existential; proves nothing about Sha). B.17: the corrected Kato factorization of the quadratic witness
   (finite-quotient identity; excludes 19). B.19 (Theorem W): for p ∉ B* = {2, 3, 19, 59, 487, 2243, 4547, 5843}, the
   ratio `C_2/((a_ℓ − 2)R_{p,ℓ})` does not depend on the auxiliary; nothing across primes, nothing about w ≠ 0, nothing
   about 288. B.11 cross-references the residue observation as related, not equivalent, and records at conjecture grade
   (BKS Conj. 2.3) `K_E = 4·c∞·#Sha·Tam/tors²` (calibrated 68/68 and 7/7 on Sha = 1 curves; the #Sha factor tested on
   194040co6, 17/17, powers of 2 only), so `K_E = 32·#Sha` here and `288 = 32·9`.
5. **Coordinates.** P₁ = (4547, 327384), P₂ = (5184, 281520) on `y² = x³ − 22735x² + 106272484x`; (−3031, 327384),
   (−2394, 281520) on the minimal model (`x_min = x_short − 7578`). Every place checked pairs them correctly; §2 now
   states the minimal-model coordinates. The places checked are listed in `review/V025_BANK_APPLIED.json`.
6. **§11.** One scoped sentence: the screened sources contain no published theorem giving a uniform-in-p input
   (p-adic height nondegeneracy, or mod-p nonvanishing of depth-two Mazur–Tate coefficients) for any rank-≥2 curve;
   such inputs are known per (E, p). This is the current known frontier of the sources read.

**Evidence.**
- 114 files are appended, byte-identical to their originals, by `tools/build_evidence_transition.py`. All 3,389 v0.2.4
  provenance rows, 36,076 exclusions and 6 redactions are preserved byte for byte. The retained reviewed differences are
  125 and 7; the three beyond v0.2.4's 122 are the p13 binding fields, kept at their historical values.
- **Retained source changes.** Five master files that v0.2.4 copied (00_READ_FIRST.md, MANIFEST.sha256,
  MASTER_BSD_DAG.md, RESUME.md, SOURCE_BINDINGS.json) were later edited in place at their source. The released copies
  are the master as integrated on 2026-09-21 and are kept byte for byte. The unmodified tool rejects this, correctly;
  it now takes an explicit `--retained-source-changes` declaration (`review/V025_RETAINED_SOURCE_CHANGES.json`: released
  and current source hashes). Any undeclared change is still rejected. Its self-test has 19 rejection cases (7 new).
- The check reports are bound as frozen copies; their live files have since gained later sections outside this scope.

**Bindings.** The transition record is `review/V025_BANK_APPLIED.json`. `tools/verify_patch_release.py` now delegates to
`tools/verify_v025_transition.py`, which:
- reconstructs v0.2.4 from `review/history/v0.2.4/` and proves the file set EQUAL to the v0.2.4 manifest;
- runs the unmodified v0.2.4 checker there (which reconstructs v0.2.3 and runs every earlier check);
- checks the v0.2.5 delta by exact rows, exact lists and set equality with uniqueness: claim order; field changes;
  new claims; text edits; appended evidence rows; retained rows; generated outputs; bound bytes;
- enforces grade and wording bounds fixed in the checker itself: no banked claim may exceed its governing grade, change
  S.3's grade label, drop a mandatory qualifier, or say "only/all that remains"; new manuscript and README text may
  carry no process markers.

`--negative-controls` corrupts throwaway copies with a maximal rebinding adversary, which recomputes every table, record,
claim-delta and manifest hash it can reach. The unmodified copy passes, and each corruption fails at its named check:

| control | first failing check |
|---|---|
| an appended row omitted; a v0.2.4 row omitted | provenance rows and evidence/src files correspond one to one |
| a duplicate rebinding an omitted row (appended region; v0.2.4 region) | no provenance path occurs twice |
| a byte of a preserved v0.2.4 copy altered | preserved v0.2.4 base copies intact |
| a byte of a retained master copy altered, its row rebound | every reconstructed file has its v0.2.4 hash |
| metadata of an appended row changed | the appended rows are exactly one per declared addition |
| S.3F rewritten to assert the order (text exceeds its grade) | S.3F within its grade and wording bound |
| the same-family audit relabelled cross-family; a preprint import relabelled published | S.17-47 within its bound |
| B.18 upgraded from conditional to theorem | B.18 within its bound |
| S.3's grade label changed | S.3 within its bound |
| "all that remains" added to a claim | no claim says "only/all that remains" |
| an undeclared manuscript edit | 11_remaining.tex equals v0.2.4 plus exactly the declared edits |
| a process marker added to the README through a rebound declared edit | no internal process marker added to README.md |
| an undeclared evidence file | the file set is exactly v0.2.4 plus the declared additions |

`tools/verify_release.py` passes 18/18 on this tree (3,503 evidence files; 362 claim evidence items, 83 claims). The
released `verify_certificate.gp` of S.3L, replayed from a temporary copy with PARI 2.17, prints output identical to its
released log apart from the timing lines.

**Not changed.** O.1–O.4, R.7, S.U, the grade labels of S.3, FIN, ORDER9 and Q36, every certificate,
`tools/verify_release.py`, `tools/verify_v024_transition.py`, `tools/build_evidence.py`, the Makefile, and the title-page
date and tag.

**Known limits carried forward (not repaired here).**
- O.1's qualification still lists "good ordinary p ≥ 17" and the supersingular 23, 29 among the remaining regimes, and
  O.2's says "gcd(t, 30030) = 1" and "#Sha < 2601 would suffice". Both remain true as stated but are no longer sharp.
  The O-claims are outside this revision.
- `coverage/COVERAGE.md` is not regenerated: its evidence counts have been stale since v0.2.4.
- `review/VERIFICATION_RUN.md` still records the 2026-09-23 run.
- `tools/verify_v024_transition.py` checks a v0.2.4 tree. Run directly on this tree it fails by design; the v0.2.5
  checker runs it inside the reconstructed v0.2.4 tree.

From the bundle root run:

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
python3 tools/verify_v025_transition.py --negative-controls
shasum -a 256 -c MANIFEST.sha256
```

**Open.** FIN, ORDER9 and Q36 remain open.
