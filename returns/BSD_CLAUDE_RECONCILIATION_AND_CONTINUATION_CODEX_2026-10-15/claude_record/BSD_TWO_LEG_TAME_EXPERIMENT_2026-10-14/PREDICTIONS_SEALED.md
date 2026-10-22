# Two-leg predictions — SEALED 2026-10-15T01:27:19Z before any modular symbol was computed

- File: predictions.json, sha256 f3f57041150fcae07fb0aa14e7566024e972ea6b43718f4a6c8858761bad59bc
- Source: outputs/reg2.txt (step 1, heights only; 1,333 pairs, l2 <= 200, five control curves).
- 1,378 (pair, q) rows; 714 clean (q !| cexp*idx_M); 512 clean rows predict a NONZERO mixed term mod q.
- Both polarization identities (b from Q1+Q2, and from Q1+Q2 vs Q1-Q2) agree on all 714 clean rows.
- Test: c11 == pred11 (mod q^e). Code checks (forced by distribution relation): c20 == pred20 (mod q^e1),
  c02 == pred02 (mod q^e2), c00 = 0, c10 == 0 (mod q^e1), c01 == 0 (mod q^e2).
- Kill rule: any clean row with c20 or c02 mismatch => code/convention bug, no conclusion on c11.
  If pure terms all pass and c11 mismatches at clean rows => the single-global-form shape is FALSE as stated;
  then run the pre-registered lambda = c11/Dmix tabulation (RESUME.md).
