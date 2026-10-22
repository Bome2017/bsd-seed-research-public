# Seal readiness — H41 mod-4 successor proof object (2026-09-16). NOT SEALED; sealing awaits operator instruction.
Reviewed text: PROOF.md revision 3, sha256 71024db1ca0893acf7cd20bd271fc80be5a6faf209feb15635b3a8d24201f2e3 (history/revision_0..2 preserved; diffs in history/).
| review | text | verdict | blocking |
|---|---|---|---|
| referee_1 VERDICT.md | rev 0 0cf7a5f9... | PASS WITH REMARKS | 0 |
| referee_2 VERDICT.md + REPAIR_CHECK.md | rev 1 953d4d6c... | PASS WITH REMARKS | 0 |
| referee_1 DELTA_REV2.md / referee_2 DELTA_REV2.md | rev 2 c5d806de... | ACCEPT WITH REMARKS / ACCEPT WITH REMARKS | 0 / 0 |
| referee_1 DELTA_REV3.md / referee_2 DELTA_REV3.md | rev 3 71024db1ca0893ac... | ACCEPT WITH REMARKS / ACCEPT WITH REMARKS | 0 / 0 |
Final gate verdicts on rev 3: referee_1 G1 PASS, G2 PASS WITH REMARKS (unread Coleman/BL inputs, listed in R9), G3-G7 PASS; referee_2 G1-G3 PASS,
G4 PASS WITH REMARKS (Atkin–Lehner sign, D12), G5-G7 PASS. Sec 0 byte-identical across rev 0, 1, 2, 3. Checks: checks/run_all_checks.py (fail-closed)
exit 0 with Cremona ecdata; output byte-identical rev 2 = rev 3; mutation tests exit 1 (author: 3; referee_1: 1; referee_2: 4).
Claims at seal: Theorem P (positive H41: E_0 = E, t = 2, 4 lambda odd, twist BSD(2), BSD qualified by BH Rem 2.11) and Corollary N (negative:
E_0 = E, t = 4, 4 lambda odd, same twist conclusions), relative to imports I1-I13 and R9. Post-review errata: ERRATA_AFTER_REVIEW.md (E1-E3,
non-blocking, text unchanged). Two-independent-review standard: MET (two fresh no-repair referees, both on the final text via delta review).
