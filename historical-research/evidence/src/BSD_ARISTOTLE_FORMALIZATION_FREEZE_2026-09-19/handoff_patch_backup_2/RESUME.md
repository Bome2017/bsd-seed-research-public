# RESUME — BSD_CODEX6_MASTER_HANDOFF (2026-09-19)
## 1. Status / verdict
COMPLETE — `CODEX6_HANDOFF_PATCHED_A1_FREEZE`. Twelve files; nothing merged; read-only outside this folder.
## 2. Completed
Original hand-off (`CODEX6_HANDOFF_READY`) plus the p = 5 patch: the rigorous p = 5 upgrade is FINISHED and SEALED
(`P5_RIGOROUS_SHA5_ZERO_CONFIRMED`); Sha[5^∞] = 0 is PROVED_COMPUTER_ASSISTED with node N7 upgraded from CERT-NUM;
#Sha[30^∞] = 9 carries no CERT-NUM qualifier. R2 wording aligned with the source-reading addendum (OPEN provenance seam,
narrowed to the canonical-vs-Gross period comparison for p = 3 with 3 ∣ N).
Second patch: the CRITERION_SS hostile gate (`CRITERION_SS_VALID_WITH_CORRECTIONS`) arrived after the p = 5 patch. Good supersingular
primes (23, 29, 131, …) now have a PROVED depth-2 SEMI_DECISION route (c_r(θ₁) ≢ 0 mod p ⇒ Sha[p^∞] = 0, r ≤ p − 1); no bit computed;
re-derived cost ≈ 270 / 460 CPU-h at 23 / 29 (growing like p²) makes it a per-prime fallback, not the global FIN solution.
Patch log: STATE.json `patch_log`.
- 15:12Z: compact R2-bridge record added (FORMULA_FRONTIER §5).
- later: FORMULA frontier frozen at two levels; D ≤ 174; normalisation seam recorded (DO_NOT_RESURRECT rows added then: now numbered 30–33).
- cross-family patch (Opus, after the Codex frontier attack `BSD_FRONTIER_UNKNOWN`):
  - Reg, Ω·Reg and q_∞ ∈ (35.99427, 36.00573) are now PROVED_COMPUTER_ASSISTED (Codex certificate, replayed by Opus). The stale "Reg = PARI" statements are corrected.
  - WC is recorded as weaker than LINE but NOT shown easier than FIN (Q0 kill gate).
  - FORMULA has three incomparable certificates (§0b).
  - FIN does not give #Sha = 9.
  - DO_NOT_RESURRECT: duplicate IDs fixed; 40 rows.
- A1 successor freeze recorded (scoped fact only): WC finite algebra MACHINE-CHECKED, CONDITIONAL, A1_FULL; antecedent NOT PROVED; FIN UNCHANGED (SOURCE_AND_HASH_INDEX §2d; DO_NOT_RESURRECT row 41). A2: no freeze yet.
## 3. Open
Nothing stale known. FIN / FORMULA architecture unchanged.
## 4. Active jobs
None (no computation of the project was running at patch time).
## 5. Files
See MANIFEST.sha256 (covers every file here except itself).
## 6. Resume commands
`cd ~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19 && shasum -a 256 -c MANIFEST.sha256`
## 7. Resources
Source hashes: SOURCE_AND_HASH_INDEX.md (§2 = sealed p = 5 artefacts; §2b = CRITERION_SS gate; §2c = Codex frontier attack + Opus cross-check).
## 8. Next three actions
1. Hand 00_READ_FIRST.md to Codex/Astra. 2. Nothing else. 3. No merge.
## 9. Provisional vs verified
State summary, not new mathematics. Every "audited" label inside is a same-model-family audit. The full verification of
P5_MANIFEST.sha256 (9 424 files) is as reported by its owning session; here only the five report files and its STATE.json were checked.
