# Singleton-witness audit (ChatGPT Pro), condensed record

**The review.** Relayed by the user on 2026-09-26. It covered bundle `BSD_PRO_SINGLETON_AUDIT_2026-09-26.zip`, sha256
c9eef97d…: 29/29 manifest entries and 26/26 source bindings passed, and the inputs were unchanged. The reviewer read
Ota, arXiv:1509.00682v1, itself. Its machine-readable checks are in `SINGLETON_AUDIT_EXACT_CHECKS.json`.

**Overall verdict: SOUND_WITH_CORRECTIONS.**
- The mathematical route is sound at p = 17 with l = 103, and at the supersingular p = 23 (l = 47) and p = 29 (l = 59),
  at the retained arithmetic-import grade. No prior finiteness of Sha is used.
- The acceptance machinery needed corrections.

| # | assertion | verdict | key source (Ota v1) |
|---|---|---|---|
| 1 | S = {103} admissible at 17 (E(F₁₀₃)[17] = 0; v₁₇(102) = 1 sufficient, not required) | CONFIRMED | Thm 1.5, p. 3; §6.2/Thm 6.4, p. 37 |
| 2 | frozen c₂ is the leading coefficient (the minus symbols cancel under projection) | CONFIRMED + F1 | Def. 2.1/Rem. 2.2, p. 5; Lemmas 5.2–5.3, p. 29 |
| 3 | no Sha-finiteness assumption (a mod-p Selmer-dimension argument) | CONFIRMED | Cor. 4.19, p. 26; proof of Thm 6.4, p. 38 |
| 4 | seed hypotheses at 17 (Thm 5.17: no semistability requirement, and c_E = 1 not required) | CONFIRMED at the retained-import grade | Thm 5.17, p. 36 |
| 5 | supersingular 23 and 29 (no ordinary-only restriction) | CONFIRMED at the same grade | Lemma 5.5, p. 30; Thm 5.9, p. 32 |
| 6 | generator invariance: c₂′ = v²c₂ + ((v² − v)/2)c₁, so c₂′ = u⁻²c₂ | CONFIRMED | Def. 3.2, p. 7 (the calculation is the reviewer's) |
| 7 | pipeline normalization and regression | NEEDS_CORRECTION (acceptance machinery) | p. 5; Rem. 6.5, p. 38 |
| 8 | the singleton D_l^(2) is distinct from the two-prime D_l^(1)D_m^(1) | CONFIRMED | Def. 3.2; proof of Thm 6.4, p. 38 |

## Findings, and what the custodian did (2026-09-26)

- **F1 (should-fix): notation.** The plus-only projection, the minus cancellation, I against J, and the c_E factor.
  **Fixed** in spec v1.1.
- **F2 (blocking): duplicate labels passed `p3_check.py`.** The new `checker/singleton_check.py` requires the exact
  label set, each label once. The audit's attack is now INVALID (control `duplicate_label_audit_attack`).
- **F3 (blocking): COUNT matched by substring; parameters unbound; stale outputs.** **Fixed:**
  - the numeric fields are parsed;
  - PARAMS must equal the frozen command line;
  - a manifest binds the engine and output hashes;
  - the launcher refuses an existing output folder;
  - controls cover a false COUNT, a wrong sign, Q or T, and stale PARAMS.
- **F4 (should-fix): the regression printed without asserting.** **Fixed** by `compare_asserting.sage`: the genuine
  run exits 0, and the tampered one exits 1.
- **F5 (should-fix): no singleton postprocessor.** **Supplied:** `singleton_check.py`, with the verdicts NONZERO,
  INCONCLUSIVE_ZERO and INVALID; 20 controls pass.
- **F6 (should-fix): corpus and storage wording.** **Fixed.**
  - The launcher reads the corpus read-only, never runs Stage W, and fails if any coefficient file changes during the
    run.
  - The corpus was pre-verified: 2,649 segments hash to their receipts.
  - The roots are pinned.
  - About 0.1 GB of new output storage is stated.
- **F7 (note): the scope of the auxiliary-prime remarks.** Fixed in the route note.
- **F8 (note): a path.** Fixed in spec v1.1.

`p3_check.py` in the certified core was **not modified**, because it belongs to earlier certified runs. Its F2/F3
weaknesses are recorded, and a retrospective check of the p ≤ 13 outputs is available if wanted.

**The reviewer could not check:** PARI and Sage/eclib replays; FLINT/Arb, so arbcore was not rerun; the production
corpus custody (the custodian has since checked it); the verifier implementation; the full seed proofs; and the seed
symbols.
